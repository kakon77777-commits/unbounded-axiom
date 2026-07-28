// Dynamic Semantic Revealing — pure scoring/ranking core.
// Spec: content/papers/2026/2026-07/02_動態語義顯影_本地端實作技術白皮書_v0.1.md (lm-001785)
//
// No DOM / Worker / fetch APIs in this file on purpose: it is imported both by
// lexical-search-worker.js (the browser) and tests/test_semantic_search.mjs
// (plain Node) so the exact same scoring logic that ships is the logic tested.
//
// Implements Phase 0+1 (exact + lexical retrieval, relation channel), Phase 2
// (§7 concept dictionary + query expansion), Phase 3's fusion side (§9
// weights.semantic), and Phase 5's chunk-level fusion (§17.2/§26 Phase 5):
// scoreCorpus takes an optional pre-computed `semanticScores`
// Map<docIndex, {score, source, heading}> (score 0..1; source is "doc" or
// "chunk"; heading is the matched section's heading text or null) and folds
// it in with the same max-fusion pattern as the alias/related-term/relation
// passes. Computing that Map is deliberately NOT this file's job — it
// requires an async embedding model and fetched vector files, both
// DOM/Worker-only concerns (see semantic-vector.js) — this file stays
// synchronous and dependency-free so the same scoring logic runs identically
// in the browser Worker and in tests/test_semantic_search.mjs under plain Node.

export const DEFAULT_WEIGHTS = {
  exact_title: 1.00,
  exact_summary: 0.82,
  alias_title: 0.88,
  lexical: 0.60,
  semantic: 0.55,
  series_relation: 0.25,
  direct_link_relation: 0.30,
  anchor_bonus: 0.08,
  // Not in the spec's own §9.1 table — that table has no dedicated bucket for
  // a dictionary "related" term (as opposed to an "alias", which does have
  // alias_title). A related-term hit is a weaker, indirect signal — closer to
  // §10's Tier D "低分語義近似" than to a real title match — so it's floored
  // low on purpose, not tuned to reach A/B on its own.
  related_term: 0.45,
};

export const DEFAULT_TIERS = { tier_A: 0.82, tier_B: 0.68, tier_C: 0.54, tier_D: 0.38 };

// §7.3 "展開限制" — must not recurse/expand without bound.
export const DEFAULT_EXPANSION_LIMITS = {
  max_aliases: 8,
  max_related_terms: 6,
  max_graph_depth: 1,
  min_expansion_confidence: 0.60,
};

// §20 多樣性重排 — see diversityRerank() below for the full reasoning.
export const DEFAULT_DIVERSITY = { max_per_series_top_10: 4, max_same_title_prefix_top_10: 3 };

// §19's 5 relation types, keyed by the single-letter type code semantic_layer.py
// writes into each doc's compact "r" list ([targetId, typeCode] pairs). Labels
// describe the CANDIDATE doc (the one this relation entry is attached to) --
// see the relation-pass comment in scoreCorpus for the previous/next direction
// derivation. weightKey picks which §9.1 raw channel weight applies before the
// tier_D floor (see that same comment for why the specific value barely
// matters today -- both available weights land below tier_D either way).
const REL_TYPE_META = {
  s: { label: "與直接結果屬於同系列", relation: "same_series", weightKey: "series_relation" },
  p: { label: "是已匹配結果的後續版本", relation: "next_version_of", weightKey: "direct_link_relation" },
  n: { label: "是已匹配結果的前一版本", relation: "previous_version_of", weightKey: "direct_link_relation" },
  e: { label: "與直接結果有明確引用關係", relation: "explicit_link", weightKey: "direct_link_relation" },
  k: { label: "與直接結果共享核心關鍵詞", relation: "same_primary_keyword", weightKey: "series_relation" },
};

export const DEFAULT_CONFIG = {
  semantic_search_enabled: true,
  search: { minimum_results: 5, max_results: 200, initial_threshold: 0.78, threshold_step: 0.08, absolute_floor: 0.28 },
  channels: { exact: true, lexical: true, dictionary: true, semantic: true, relations: true },
  tiers: DEFAULT_TIERS,
  weights: DEFAULT_WEIGHTS,
  expansion_limits: DEFAULT_EXPANSION_LIMITS,
  diversity: DEFAULT_DIVERSITY,
  display: { default_mode: "reveal", tier_a_opacity: 1.0, tier_b_opacity: 0.92, tier_c_opacity: 0.62, tier_d_opacity: 0.38, hidden_opacity: 0.12 },
  debounce_ms: 300,
  max_query_length: 80,
};

const CJK_RE = /[㐀-鿿]/;

// §6.1 query normalization: NFKC (also folds fullwidth->halfwidth), lowercase,
// collapse whitespace, trim. §6.2 explicitly forbids stripping digits, version
// numbers, math symbols, greek letters, hyphens, abbreviations — NFKC+lowercase
// alone never touches any of those, so nothing further is needed here.
export function normalizeQuery(raw) {
  if (!raw) return "";
  return String(raw).normalize("NFKC").toLowerCase().replace(/\s+/g, " ").trim();
}

function isCjk(ch) { return CJK_RE.test(ch); }

// Latin/number runs become whole tokens; CJK (no word boundaries) becomes
// overlapping character bigrams, per §16.1's "trigram / token overlap" plan.
export function tokenize(s) {
  const tokens = [];
  let buf = "";
  const flush = () => { if (buf) { tokens.push(buf); buf = ""; } };
  for (const ch of s) {
    if (isCjk(ch)) { flush(); }
    else if (/[a-z0-9+.\-]/i.test(ch)) { buf += ch; }
    else { flush(); }
  }
  flush();
  const cjkOnly = Array.from(s).filter(isCjk);
  for (let i = 0; i < cjkOnly.length - 1; i++) tokens.push(cjkOnly[i] + cjkOnly[i + 1]);
  if (cjkOnly.length === 1) tokens.push(cjkOnly[0]);
  return tokens.filter(Boolean);
}

export function trigrams(s) {
  const chars = Array.from(s.replace(/\s+/g, ""));
  if (chars.length < 3) return chars.length ? [chars.join("")] : [];
  const grams = [];
  for (let i = 0; i <= chars.length - 3; i++) grams.push(chars.slice(i, i + 3).join(""));
  return grams;
}

function overlapRatio(queryTokens, docTokenSet) {
  if (!queryTokens.length || !docTokenSet.size) return 0;
  let hit = 0;
  for (const t of queryTokens) if (docTokenSet.has(t)) hit++;
  return hit / queryTokens.length;
}

// §6.3 expand_query / §7 專屬詞典: does the (already-normalized) query name a
// known concept — by its canonical name, one of its aliases, or a partial
// match against either — and if so, what ELSE does that concept go by?
// max_graph_depth is fixed at 1 by construction: this walks straight from the
// query to a matching concept's own alias/related lists and stops there, it
// never follows a related term to ITS concept and expands again.
export function expandQuery(queryNorm, dictionary, limits) {
  const empty = { aliases: [], related: [] };
  if (!queryNorm || !dictionary || !dictionary.length) return empty;
  const L = limits || DEFAULT_EXPANSION_LIMITS;

  const aliasHits = [];
  const relatedHits = [];
  for (const entry of dictionary) {
    const canonicalNorm = normalizeQuery(entry.canonical);
    const aliasMatch = (entry.aliases || []).find((a) => normalizeQuery(a.term) === queryNorm);
    const canonicalMatch = canonicalNorm === queryNorm;
    // a loose (substring) match only counts for queries with enough signal to
    // not match everything — a 1-char query would "loosely match" half the dictionary
    const looseMatch = !aliasMatch && !canonicalMatch && queryNorm.length >= 2 && (
      canonicalNorm.includes(queryNorm)
      || (entry.aliases || []).some((a) => normalizeQuery(a.term).includes(queryNorm))
    );
    if (!aliasMatch && !canonicalMatch && !looseMatch) continue;

    for (const a of (entry.aliases || [])) {
      if (a.weight < L.min_expansion_confidence) continue;
      if (normalizeQuery(a.term) === queryNorm) continue; // don't "expand" the query into itself
      aliasHits.push({ term: a.term, weight: a.weight, concept_id: entry.concept_id, canonical: entry.canonical });
    }
    if (!canonicalMatch) {
      // the query hit this concept via an alias (or a loose partial match) —
      // the canonical name itself is then a valid expansion target too.
      aliasHits.push({ term: entry.canonical, weight: aliasMatch ? aliasMatch.weight : 0.75, concept_id: entry.concept_id, canonical: entry.canonical });
    }
    for (const r of (entry.related || [])) {
      if (r.weight < L.min_expansion_confidence) continue;
      relatedHits.push({ term: r.term, weight: r.weight, concept_id: entry.concept_id, canonical: entry.canonical });
    }
  }

  function dedupeSortCap(arr, cap) {
    const seen = new Set();
    const out = [];
    for (const x of arr) {
      const k = normalizeQuery(x.term);
      if (!k || seen.has(k)) continue;
      seen.add(k);
      out.push(x);
    }
    out.sort((a, b) => b.weight - a.weight);
    return out.slice(0, cap);
  }

  return {
    aliases: dedupeSortCap(aliasHits, L.max_aliases),
    related: dedupeSortCap(relatedHits, L.max_related_terms),
  };
}

// Precompute per-document derived fields once at index-load time so a search
// on every keystroke doesn't re-tokenize 1800+ documents from scratch (§23.1
// performance budget: front-end results inside 500ms).
export function prepareDocument(doc) {
  if (doc._prepared) return doc;
  const titleNorm = normalizeQuery(doc.t || "");
  const summaryNorm = normalizeQuery(doc.s || "");
  const headingsNorm = (doc.h || []).map((h) => normalizeQuery(h));
  const bagText = [doc.t, doc.s, ...(doc.h || [])].filter(Boolean).join(" ");
  doc._titleNorm = titleNorm;
  doc._summaryNorm = summaryNorm;
  doc._headingsNorm = headingsNorm;
  doc._tokenSet = new Set(tokenize(normalizeQuery(bagText)));
  doc._trigramSet = new Set(trigrams(titleNorm + summaryNorm));
  doc._keywordsNorm = (doc.k || []).map((k) => normalizeQuery(k));
  doc._prepared = true;
  return doc;
}

export function prepareIndex(documents) {
  documents.forEach(prepareDocument);
  return documents;
}

// Score ONE document against an already-normalized query. Relation/Tier-D
// scoring needs corpus-wide context (which siblings also matched) and is
// applied afterwards in scoreCorpus(), not here.
export function scoreDocument(doc, queryNorm, queryTokens, queryTrigrams, weights) {
  const w = weights || DEFAULT_WEIGHTS;
  const reasons = [];
  const channels = new Set();
  let best = 0;

  if (queryNorm) {
    if (doc._titleNorm.includes(queryNorm)) {
      channels.add("exact");
      reasons.push({ tier: "A", label: "標題精確命中", field: "title", matched_text: queryNorm });
      best = Math.max(best, w.exact_title);
    }
    for (let i = 0; i < doc._headingsNorm.length; i++) {
      if (doc._headingsNorm[i].includes(queryNorm)) {
        channels.add("exact");
        reasons.push({ tier: "A", label: "章節標題命中", field: "heading", matched_text: doc.h[i] });
        best = Math.max(best, w.exact_title * 0.95);
        break;
      }
    }
    if (doc._summaryNorm.includes(queryNorm)) {
      channels.add("exact");
      reasons.push({ tier: "B", label: "摘要精確命中", field: "summary", matched_text: queryNorm });
      best = Math.max(best, w.exact_summary);
    }
    for (let i = 0; i < doc._keywordsNorm.length; i++) {
      if (doc._keywordsNorm[i] === queryNorm) {
        channels.add("exact");
        reasons.push({ tier: "A", label: "關鍵詞精確命中", field: "keyword", matched_text: doc.k[i] });
        best = Math.max(best, w.alias_title);
        break;
      }
    }
  }

  if (queryTokens.length) {
    const ov = overlapRatio(queryTokens, doc._tokenSet);
    if (ov > 0) {
      channels.add("lexical");
      const s = w.lexical * ov;
      reasons.push({ tier: ov >= 0.6 ? "B" : "C", label: "詞彙相似命中", field: "title/summary/headings", overlap: Number(ov.toFixed(2)) });
      best = Math.max(best, s);
    }
  }

  if (!channels.has("exact") && queryTrigrams.length) {
    const tgOv = overlapRatio(queryTrigrams, doc._trigramSet);
    if (tgOv > 0) {
      channels.add("lexical");
      const s = w.lexical * 0.7 * tgOv;
      if (s > 0) reasons.push({ tier: "C", label: "字元近似命中", field: "title/summary", overlap: Number(tgOv.toFixed(2)) });
      best = Math.max(best, s);
    }
  }

  return { score: Math.min(1, best), channels: Array.from(channels), reasons };
}

export function assignTier(score, tiers) {
  const t = tiers || DEFAULT_TIERS;
  if (score >= t.tier_A) return "A";
  if (score >= t.tier_B) return "B";
  if (score >= t.tier_C) return "C";
  if (score >= t.tier_D) return "D";
  return null;
}

export function buildThresholdLadder(cfg) {
  const s = cfg.search;
  const ladder = [];
  let t = s.initial_threshold;
  while (t > s.absolute_floor + 1e-9) {
    ladder.push(Number(t.toFixed(2)));
    t -= s.threshold_step;
  }
  ladder.push(s.absolute_floor);
  return ladder;
}

// §11.1 non-zero mechanism: relax the threshold step by step until at least
// `minimum_results` survive, or fall back to a straight top-N. Always reports
// whether/how much it relaxed so the UI can show §11.2's honest disclosure text
// instead of silently passing off a low-confidence result as a direct hit.
//
// `low_confidence` is judged from the BEST result actually returned, not from
// how far the ladder had to relax to pad the *count* up to minimum — those are
// different facts. A query with one dead-on exact match plus 8 same-series
// Tier D siblings had to relax all the way to fill 5 slots, but the top hit is
// completely solid, so §11.2 message 1 ("加入詞彙與語義近似結果") applies, not
// message 2 ("沒有找到高可信度直接結果") — message 2 is reserved for when
// nothing returned reaches Tier B or better.
export function ensureMinimumResults(scored, cfg) {
  const ladder = buildThresholdLadder(cfg);
  const minimum = cfg.search.minimum_results;
  for (let i = 0; i < ladder.length; i++) {
    const threshold = ladder[i];
    const selected = scored.filter((r) => r.score >= threshold);
    if (selected.length >= minimum) {
      return { results: selected, threshold, relaxed: i > 0, low_confidence: !bestIsConfident(selected, cfg) };
    }
  }
  // Ran the whole ladder down to absolute_floor and still short of `minimum`
  // candidates — §11.1's own fallback: a straight top-N over ALL scored docs
  // (not just whatever cleared absolute_floor), so the count promise holds
  // even for a corpus with very few genuinely-related documents.
  const fallback = scored.slice(0, minimum);
  return { results: fallback, threshold: null, relaxed: true, low_confidence: !bestIsConfident(fallback, cfg) };
}

function bestIsConfident(results, cfg) {
  return results.length > 0 && results[0].score >= cfg.tiers.tier_B;
}

// §20 多樣性重排 (diversity reranking): a title's "lineage" prefix — the run
// of characters before the first series-separator-like punctuation. Doesn't
// claim any relationship (unlike "series"/"r", which come from real curated
// Program membership) — this is presentation-only grouping to avoid the top
// of a result list reading as N near-duplicates of the same paper, not a
// fact shown to the user. A short minimum (4) keeps trivially-common openers
// from grouping unrelated titles; titles with no separator in the first 40
// chars just become their own singleton group (never triggers the quota).
export function titlePrefixKey(title) {
  const n = normalizeQuery(title || "");
  const m = n.match(/^[^_\-—:：（(]{4,40}/);
  return m ? m[0] : n;
}

// Greedy single pass over the already score-sorted results: fill the first
// 10 slots only with candidates that don't push either quota over its limit,
// holding everything else back to fill in afterward (still in score order —
// nothing is dropped, an over-quota candidate just loses its early slot to a
// more diverse neighbour). "series" quota only applies to docs that actually
// carry a Program label (`doc.p`) — real curated membership, per
// semantic_layer.py's _compact(); doc-less/unlabelled candidates are never
// quota-limited by series, only by title-prefix. If the quotas are so tight
// the window can't reach 10 candidates (e.g. a query whose only matches all
// share one series), backfill unconditionally from the held-back queue in
// its own score order — matching this module's existing non-zero-results
// philosophy: a full top-10 beats a strictly-diverse-but-short one.
export function diversityRerank(results, cfg) {
  const d = (cfg && cfg.diversity) || DEFAULT_DIVERSITY;
  if (!d || d.max_per_series_top_10 == null) return results;
  const WINDOW = 10;
  const head = [];
  const heldBack = [];
  const seriesCount = new Map();
  const prefixCount = new Map();

  for (const r of results) {
    if (head.length >= WINDOW) { heldBack.push(r); continue; }
    const seriesKey = r.doc.p || null;
    const prefixKey = titlePrefixKey(r.doc.t);
    const seriesN = seriesKey ? (seriesCount.get(seriesKey) || 0) : 0;
    const prefixN = prefixCount.get(prefixKey) || 0;
    const seriesOk = !seriesKey || seriesN < d.max_per_series_top_10;
    const prefixOk = prefixN < d.max_same_title_prefix_top_10;
    if (seriesOk && prefixOk) {
      head.push(r);
      if (seriesKey) seriesCount.set(seriesKey, seriesN + 1);
      prefixCount.set(prefixKey, prefixN + 1);
    } else {
      heldBack.push(r);
    }
  }
  while (head.length < WINDOW && heldBack.length) head.push(heldBack.shift());
  return head.concat(heldBack);
}

// Full corpus search: exact+lexical scoring pass, then a dictionary-expansion
// pass (§7 — alias/related-term hits, only when the query itself names a
// known concept), then a relation pass that gives real Tier D ("same series")
// credit ONLY to documents whose `r` list (built from registry/programs/*.json
// — real curated membership, never guessed) contains a sibling that already
// scored at Tier B or better on this same query. A doc with no related_ids
// never gets a Tier D score out of thin air, and a doc with no dictionary hit
// never gets an alias score out of thin air either.
export function scoreCorpus(documents, rawQuery, config, dictionary, semanticScores) {
  const cfg = config || DEFAULT_CONFIG;
  const weights = cfg.weights || DEFAULT_WEIGHTS;
  const queryNorm = normalizeQuery(rawQuery);
  const original = rawQuery == null ? "" : String(rawQuery);

  if (!queryNorm) {
    return { query: { original, normalized: "" }, results: [], relaxed: false, low_confidence: false, empty_query: true, total_candidates: documents.length, expansions: { aliases: [], related: [] } };
  }
  if (queryNorm.length > (cfg.max_query_length || 80)) {
    return scoreCorpus(documents, original.slice(0, cfg.max_query_length || 80), cfg, dictionary, semanticScores);
  }

  const queryTokens = tokenize(queryNorm);
  const queryTrigrams = trigrams(queryNorm);
  const expansions = cfg.channels.dictionary !== false
    ? expandQuery(queryNorm, dictionary || [], cfg.expansion_limits)
    : { aliases: [], related: [] };

  let scored = documents.map((d) => {
    const r = scoreDocument(d, queryNorm, queryTokens, queryTrigrams, weights);
    return { id: d.i, doc: d, score: r.score, channels: r.channels, reasons: r.reasons };
  });

  if (expansions.aliases.length || expansions.related.length) {
    for (const r of scored) {
      const doc = r.doc;
      for (const a of expansions.aliases) {
        const an = normalizeQuery(a.term);
        if (!an) continue;
        let field = null;
        if (doc._titleNorm.includes(an)) field = "title";
        else if (doc._keywordsNorm.includes(an)) field = "keyword";
        else if (doc._summaryNorm.includes(an)) field = "summary";
        if (!field) continue;
        // §10 A 級 explicitly lists "人工別名命中" as a valid exact-tier signal —
        // scaling the base alias_title weight by this specific alias's own
        // confidence lets a high-confidence alias reach Tier A like a real
        // title hit, while a merely-adequate one (near min_expansion_confidence)
        // lands lower, same pattern as the lexical/relation passes above.
        const s = Math.min(1, weights.alias_title * a.weight);
        if (s > r.score) {
          r.score = s;
          r.channels = Array.from(new Set([...r.channels, "alias"]));
          r.reasons = [{ tier: "A", label: `命中已確認別名「${a.term}」`, field, matched_text: a.term, expansion_term: a.term, relation: "alias", concept_id: a.concept_id }, ...r.reasons];
        }
        break; // one alias hit is enough signal for this doc; don't keep stacking
      }
      for (const rel of expansions.related) {
        const rn = normalizeQuery(rel.term);
        if (!rn) continue;
        const field = doc._titleNorm.includes(rn) ? "title" : (doc._summaryNorm.includes(rn) ? "summary" : null);
        if (!field) continue;
        const s = Math.min(1, weights.related_term * rel.weight);
        if (s > r.score) {
          r.score = s;
          r.channels = Array.from(new Set([...r.channels, "related_term"]));
          r.reasons = [{ tier: "D", label: `與相關詞「${rel.term}」近似`, field, matched_text: rel.term, expansion_term: rel.term, relation: "related", concept_id: rel.concept_id }, ...r.reasons];
        }
        break;
      }
    }
  }

  // §9 weights.semantic / §26 Phase 3+5: semanticScores is an optional
  // Map<docIndex, {score, source, heading}> pre-computed by
  // semantic-vector.js (query embedding + cosine similarity against
  // pre-built document AND chunk vectors, already floor/ceiling-rescaled —
  // see that file for why a fixed corpus-calibrated rescale is used instead
  // of raw cosine or a per-query relative one). source is "doc" (whole-
  // document title+summary+headings vector, Phase 3) or "chunk" (a specific
  // section's vector, Phase 5 §17.2/§17.3) — the label/field below reflect
  // whichever one actually produced the winning score, so the UI never
  // claims "summary similarity" when what really matched was one paragraph
  // on page 8 (§15: a hit reason must name what actually matched, not just
  // assert "AI thinks so"). Absent/empty (model still loading, load failed,
  // browser unsupported) degrades to exactly today's exact+lexical+
  // dictionary+relations behavior — this is the §16.2 "若 API 失效，系統退化
  // 為精確搜尋" requirement, satisfied structurally: nothing above this block
  // knows or cares whether semanticScores exists.
  if (cfg.channels.semantic !== false && semanticScores && semanticScores.size) {
    scored.forEach((r, i) => {
      const hit = semanticScores.get(i);
      if (!hit || hit.score <= 0) return;
      const s = weights.semantic * hit.score;
      if (s > r.score) {
        r.score = s;
        r.channels = Array.from(new Set([...r.channels, "semantic"]));
        const isChunk = hit.source === "chunk";
        const label = isChunk
          ? (hit.heading ? `段落語義近似（${hit.heading}）` : "段落語義近似")
          : "摘要語義近似";
        r.reasons = [{
          tier: "C", label, field: isChunk ? "chunk" : "summary",
          semantic_score: Number(hit.score.toFixed(2)), semantic_source: hit.source,
        }, ...r.reasons];
      }
    });
  }

  if (cfg.channels.relations) {
    const strongIds = new Set(scored.filter((r) => r.score >= cfg.tiers.tier_B).map((r) => r.id));
    for (const r of scored) {
      if (r.score < cfg.tiers.tier_D && (r.doc.r || []).length) {
        // r.doc.r is [[targetId, typeCode], ...] (§19's 5 relation types —
        // see semantic_layer.py's module docstring for how each is sourced).
        // A pair [targetId, "p"] on r.doc means targetId is r.doc's OWN
        // previous version, i.e. r.doc is the LATER one -- the label below
        // describes r.doc (why IT is included), which is the inverse of
        // what the stored type says about targetId; verified against a
        // concrete constructed example before trusting this, given how many
        // direction bugs today's earlier KaTeX regex work turned up.
        const relatedStrong = r.doc.r.filter(([tid]) => strongIds.has(tid) && tid !== r.id);
        if (relatedStrong.length) {
          const [targetId, rtype] = relatedStrong[0];
          const meta = REL_TYPE_META[rtype] || REL_TYPE_META.s;
          // weights.series_relation/direct_link_relation (§9.1) are *raw
          // channel* scores meant to be re-weighted by the §9.2 fusion
          // formula's G coefficient (0.10) before comparison against tier
          // thresholds — this MVP skips that second fusion stage (see module
          // header) and takes a plain max() across channels instead, so a
          // bare 0.25-0.30 would fall below both tier_D (0.38) and, worse,
          // the absolute_floor (0.28) and get silently dropped by
          // ensureMinimumResults. Floor a relation-only score at tier_D
          // itself: a confirmed relation is definitionally what Tier D means
          // (§10), never invisible.
          const s = Math.max(weights[meta.weightKey], cfg.tiers.tier_D);
          if (s > r.score) {
            r.score = s;
            r.channels = Array.from(new Set([...r.channels, "relation"]));
            // Prepend, not append: this relation score just BEAT every reason
            // scoreDocument found (that's the `s > r.score` guard above), so it
            // is now the actual explanation for this doc's tier — the reason
            // shown first in the UI (§15) must track whichever signal is
            // actually winning, not just accumulation order.
            r.reasons = [{ tier: "D", label: meta.label, field: "related_ids", relation: meta.relation, related_to: targetId }, ...r.reasons];
          }
        }
      }
    }
  }

  scored.sort((a, b) => b.score - a.score);
  if (documents.length === 0) {
    return { query: { original, normalized: queryNorm, tokens: queryTokens }, results: [], relaxed: false, low_confidence: false, empty_index: true, total_candidates: 0, expansions };
  }

  const { results, threshold, relaxed, low_confidence } = ensureMinimumResults(scored, cfg);
  const diversified = diversityRerank(results, cfg);
  const tiered = diversified
    .slice(0, cfg.search.max_results || 200)
    .map((r) => ({ ...r, tier: assignTier(r.score, cfg.tiers) || "D" }));

  return {
    query: { original, normalized: queryNorm, tokens: queryTokens },
    results: tiered,
    expansions,
    threshold,
    relaxed,
    low_confidence,
    total_candidates: scored.length,
  };
}
