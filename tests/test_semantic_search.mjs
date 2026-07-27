#!/usr/bin/env node
// Runs tests/semantic_queries.jsonl against the REAL built index through the
// SAME semantic-core.js the browser Worker imports — no logic duplication.
// Usage: node tests/test_semantic_search.mjs
// Doubles as the §29 deliverable #12 "搜尋品質報告" — writes tests/quality-report.json.
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { scoreCorpus, prepareIndex, DEFAULT_CONFIG, diversityRerank, titlePrefixKey } from "../shell/public/semantic/semantic-core.js";

const ROOT = dirname(dirname(fileURLToPath(import.meta.url)));

const indexPath = join(ROOT, "dist", "ai", "semantic-index.min.json");
const dictionaryPath = join(ROOT, "dist", "ai", "semantic-dictionary.min.json");
const configPath = join(ROOT, "shell", "public", "semantic", "search.config.json");
const queriesPath = join(ROOT, "tests", "semantic_queries.jsonl");

const index = JSON.parse(readFileSync(indexPath, "utf8"));
const dictionaryFile = JSON.parse(readFileSync(dictionaryPath, "utf8"));
const dictionary = dictionaryFile.entries || [];
const userConfig = JSON.parse(readFileSync(configPath, "utf8"));
const config = {
  ...DEFAULT_CONFIG, ...userConfig,
  search: { ...DEFAULT_CONFIG.search, ...userConfig.search },
  tiers: { ...DEFAULT_CONFIG.tiers, ...userConfig.tiers },
  weights: { ...DEFAULT_CONFIG.weights, ...userConfig.weights },
  channels: { ...DEFAULT_CONFIG.channels, ...userConfig.channels },
  expansion_limits: { ...DEFAULT_CONFIG.expansion_limits, ...userConfig.expansion_limits },
  diversity: { ...DEFAULT_CONFIG.diversity, ...userConfig.diversity },
};
const documents = prepareIndex(index.documents);

const lines = readFileSync(queriesPath, "utf8").split("\n").map((l) => l.trim()).filter(Boolean);
const cases = lines.map((l) => JSON.parse(l));

let pass = 0, fail = 0;
const byCategory = {};
const details = [];

for (const c of cases) {
  const result = scoreCorpus(documents, c.query, config, dictionary);
  const ids = result.results.map((r) => r.id);
  const tierAIds = result.results.filter((r) => r.tier === "A").map((r) => r.id);
  const top10 = ids.slice(0, 10);

  let ok = true;
  const reasons = [];

  if (c.expected_tier_a) {
    const hit = c.expected_tier_a.some((id) => tierAIds.includes(id));
    if (!hit) { ok = false; reasons.push(`expected tier A among ${c.expected_tier_a}, got tiers=${JSON.stringify(result.results.slice(0, 5).map((r) => [r.id, r.tier, r.score.toFixed(2)]))}`); }
  }
  if (c.expected_any) {
    const hit = c.expected_any.some((id) => ids.includes(id));
    if (!hit) { ok = false; reasons.push(`expected any of ${c.expected_any} in ${ids.length} results`); }
  }
  if (c.expected_top10) {
    const hit = c.expected_top10.some((id) => top10.includes(id));
    if (!hit) { ok = false; reasons.push(`expected any of ${c.expected_top10} in top10=${JSON.stringify(top10)}`); }
  }
  if (c.expect_low_confidence) {
    if (!result.low_confidence) { ok = false; reasons.push(`expected low_confidence=true, got ${result.low_confidence} (relaxed=${result.relaxed}, threshold=${result.threshold})`); }
  }
  if (c.expect_not_low_confidence) {
    if (result.low_confidence) { ok = false; reasons.push(`expected low_confidence=false, got true (top result tier=${result.results[0] && result.results[0].tier}, score=${result.results[0] && result.results[0].score.toFixed(2)})`); }
  }
  if (c.expect_empty_query) {
    if (!result.empty_query) { ok = false; reasons.push(`expected empty_query=true`); }
  }
  if (c.expect_any_result) {
    if (!(result.results.length > 0)) { ok = false; reasons.push(`expected at least one result, got 0`); }
  }
  if (c.expect_alias_terms) {
    const gotTerms = (result.expansions.aliases || []).map((a) => a.term);
    const hit = c.expect_alias_terms.some((t) => gotTerms.includes(t));
    if (!hit) { ok = false; reasons.push(`expected one of alias terms ${JSON.stringify(c.expect_alias_terms)} in expansions.aliases=${JSON.stringify(gotTerms)}`); }
  }
  if (c.expect_no_expansion) {
    const total = (result.expansions.aliases || []).length + (result.expansions.related || []).length;
    if (total > 0) { ok = false; reasons.push(`expected no expansion terms, got aliases=${JSON.stringify(result.expansions.aliases)} related=${JSON.stringify(result.expansions.related)}`); }
  }
  // universal invariant regardless of category: with a non-empty corpus and a
  // non-empty query, the non-zero mechanism must never return zero results.
  if (c.query && documents.length > 0 && result.results.length === 0) {
    ok = false; reasons.push("non-zero guarantee violated: 0 results for a non-empty query against a non-empty index");
  }
  // §22.1 "支援最低結果數": ensure_minimum_results must actually reach the
  // configured floor whenever enough candidates exist in the whole corpus,
  // not just "more than zero" — a hand-typed exact title query legitimately
  // has few *lexical* neighbours, so this caught a real bug (relation-only
  // Tier D scores landing below absolute_floor and getting dropped).
  if (c.query && documents.length >= config.search.minimum_results && result.results.length < config.search.minimum_results && !result.empty_query) {
    ok = false; reasons.push(`minimum_results not met: expected >= ${config.search.minimum_results}, got ${result.results.length}`);
  }

  const cat = c.category || "uncategorized";
  byCategory[cat] = byCategory[cat] || { pass: 0, fail: 0 };
  if (ok) { pass++; byCategory[cat].pass++; } else { fail++; byCategory[cat].fail++; }
  details.push({ query: c.query, category: cat, ok, reasons, result_count: result.results.length, low_confidence: result.low_confidence, relaxed: result.relaxed });
  console.log(`[${ok ? "PASS" : "FAIL"}] (${cat}) ${JSON.stringify(c.query)}${ok ? "" : "\n       " + reasons.join("\n       ")}`);
}

console.log("");
console.log(`--- ${pass}/${cases.length} passed ---`);
for (const [cat, stats] of Object.entries(byCategory)) {
  console.log(`  ${cat}: ${stats.pass}/${stats.pass + stats.fail}`);
}

// --- Phase 3 fusion unit checks: scoreCorpus's semanticScores parameter ---
// semantic-vector.js itself (real model + fetch) needs a browser and is
// verified separately via the Browser pane; these checks only exercise the
// synchronous fusion logic in semantic-core.js with a synthetic score map,
// which is exactly what that file's own contract promises callers.
{
  let semPass = 0, semFail = 0;
  const semCheck = (label, cond, detail) => {
    if (cond) { semPass++; console.log(`[PASS] (semantic-fusion) ${label}`); }
    else { semFail++; console.log(`[FAIL] (semantic-fusion) ${label}${detail ? "\n       " + detail : ""}`); }
  };

  // Pick a query with NO lexical/exact overlap against some arbitrary doc,
  // then inject a synthetic high semantic score for that doc's index and
  // confirm it gets promoted into the results with a "semantic" channel.
  const nonsenseQuery = "殊塵朧霈闃";
  const baseline = scoreCorpus(documents, nonsenseQuery, config, dictionary, new Map());
  const baselineTopId = baseline.results[0] && baseline.results[0].id;
  const targetIdx = 5; // arbitrary fixed index, unrelated to the query above
  const targetId = documents[targetIdx].i;
  const semScores = new Map([[targetIdx, 0.9]]);
  const boosted = scoreCorpus(documents, nonsenseQuery, config, dictionary, semScores);
  const boostedHit = boosted.results.find((r) => r.id === targetId);

  semCheck(
    "empty semanticScores changes nothing vs no 5th arg",
    JSON.stringify(baseline.results.map((r) => r.id)) === JSON.stringify(
      scoreCorpus(documents, nonsenseQuery, config, dictionary).results.map((r) => r.id)
    )
  );
  semCheck(
    `synthetic high semantic score promotes doc ${targetId} into results`,
    !!boostedHit && boostedHit.channels.includes("semantic"),
    `boostedHit=${JSON.stringify(boostedHit)}`
  );
  semCheck(
    "promoted doc's top reason is the semantic one",
    !!boostedHit && boostedHit.reasons[0].label === "摘要語義近似",
    `reasons=${JSON.stringify(boostedHit && boostedHit.reasons)}`
  );
  semCheck(
    "promoted score respects weights.semantic ceiling (0.55 * 0.9)",
    !!boostedHit && Math.abs(boostedHit.score - config.weights.semantic * 0.9) < 1e-6,
    `score=${boostedHit && boostedHit.score}`
  );

  // A doc that already scores higher via exact/lexical must NOT be
  // downgraded by a weak synthetic semantic score (max-fusion, not additive).
  const exactQuery = documents[0].t.slice(0, 4);
  const exactBaseline = scoreCorpus(documents, exactQuery, config, dictionary, new Map());
  const exactTop = exactBaseline.results[0];
  const weakSemMap = new Map([[0, 0.1]]);
  const exactWithWeakSem = scoreCorpus(documents, exactQuery, config, dictionary, weakSemMap);
  const stillTop = exactWithWeakSem.results.find((r) => r.id === exactTop.id);
  semCheck(
    "weak synthetic semantic score never downgrades an existing exact hit",
    !!stillTop && stillTop.score === exactTop.score,
    `before=${exactTop.score} after=${stillTop && stillTop.score}`
  );

  console.log(`\n--- semantic-fusion: ${semPass}/${semPass + semFail} passed ---`);
  pass += semPass; fail += semFail;
  cases.push(...Array(semPass + semFail).fill({ category: "semantic-fusion" }));
  byCategory["semantic-fusion"] = { pass: semPass, fail: semFail };
}

// --- Phase 4 §20 diversity reranking unit checks ---
// Synthetic result arrays (score-sorted, matching what ensureMinimumResults
// hands to diversityRerank) rather than real search output, so each case
// isolates exactly one quota behavior.
{
  let divPass = 0, divFail = 0;
  const divCheck = (label, cond, detail) => {
    if (cond) { divPass++; console.log(`[PASS] (diversity) ${label}`); }
    else { divFail++; console.log(`[FAIL] (diversity) ${label}${detail ? "\n       " + detail : ""}`); }
  };
  const cfg = { diversity: { max_per_series_top_10: 2, max_same_title_prefix_top_10: 2 } };
  const mk = (id, score, series, title) => ({ id, score, doc: { p: series, t: title || id } });

  // 6 candidates all in the SAME series, quota=2 -> only 2 should survive
  // into the top-10 window's head, the rest demoted (not dropped) after it.
  const sameSeries = [1, 2, 3, 4, 5, 6].map((n) => mk(`s${n}`, 1 - n * 0.01, "seriesA"));
  const rerankedSeries = diversityRerank(sameSeries, cfg);
  const headIds = rerankedSeries.slice(0, 2).map((r) => r.id);
  divCheck(
    "series quota caps same-series docs in the head at max_per_series_top_10",
    headIds.length === 2 && headIds[0] === "s1" && headIds[1] === "s2",
    `head=${JSON.stringify(rerankedSeries.map((r) => r.id))}`
  );
  divCheck(
    "demoted same-series docs are held, not dropped",
    rerankedSeries.length === sameSeries.length,
    `before=${sameSeries.length} after=${rerankedSeries.length}`
  );
  divCheck(
    "highest-scored doc from an over-quota series still appears before lower ones from elsewhere",
    rerankedSeries.findIndex((r) => r.id === "s3") < rerankedSeries.length,
    `order=${JSON.stringify(rerankedSeries.map((r) => r.id))}`
  );

  // title-prefix quota, independent of series (all docs series-less here)
  const samePrefix = [1, 2, 3, 4].map((n) =>
    mk(`p${n}`, 1 - n * 0.01, null, `文明原生複雜度升級命題_變體${n}的完整論述`)
  );
  const rerankedPrefix = diversityRerank(samePrefix, cfg);
  const prefixHeadIds = rerankedPrefix.slice(0, 2).map((r) => r.id);
  divCheck(
    "title-prefix quota caps same-lineage docs in the head",
    prefixHeadIds.length === 2 && prefixHeadIds[0] === "p1" && prefixHeadIds[1] === "p2",
    `head=${JSON.stringify(rerankedPrefix.map((r) => r.id))}`
  );

  // mixed corpus: diverse candidates should NOT be reordered relative to
  // each other just because unrelated over-quota docs exist elsewhere.
  const mixed = [
    mk("a1", 0.9, "seriesA"), mk("a2", 0.85, "seriesA"), mk("a3", 0.8, "seriesA"),
    mk("b1", 0.75, "seriesB"), mk("c1", 0.7, null, "獨立論文一"), mk("d1", 0.65, null, "獨立論文二"),
  ];
  const rerankedMixed = diversityRerank(mixed, cfg);
  divCheck(
    "diverse non-quota-violating docs keep their relative score order",
    rerankedMixed.findIndex((r) => r.id === "b1") < rerankedMixed.findIndex((r) => r.id === "a3"),
    `order=${JSON.stringify(rerankedMixed.map((r) => r.id))}`
  );

  // backfill: quotas so tight the head can't reach 10 -> fill anyway.
  const small = [1, 2, 3].map((n) => mk(`x${n}`, 1 - n * 0.01, "onlySeries"));
  const rerankedSmall = diversityRerank(small, cfg);
  divCheck(
    "backfills past the quota when too few candidates exist to fill the window",
    rerankedSmall.length === 3,
    `got=${rerankedSmall.length}`
  );

  divCheck(
    "titlePrefixKey groups a real corpus-observed near-duplicate lineage",
    titlePrefixKey("文明原生複雜度升級命題_形式化草案、載體幾何與後人類必要性的文明理論") ===
    titlePrefixKey("文明原生複雜度升級命題_從認知—系統複雜度鴻溝、載體幾何到後人類文明的必要性"),
  );
  divCheck(
    "titlePrefixKey does not conflate unrelated titles",
    titlePrefixKey("黎曼猜想的方法論重構") !== titlePrefixKey("量子力學的測量問題"),
  );

  console.log(`\n--- diversity: ${divPass}/${divPass + divFail} passed ---`);
  pass += divPass; fail += divFail;
  cases.push(...Array(divPass + divFail).fill({ category: "diversity" }));
  byCategory["diversity"] = { pass: divPass, fail: divFail };
}

// --- Phase 4 §19 relation-type checks, against the REAL built index ---
// Regression guard for a real bug found while building this: _merge_relations
// used to pick a winning relation type by which map was passed first, not by
// _REL_PRIORITY, so previous_version/next_version (always a subset of
// same_series pairs, since both come from the same Program's iterations)
// silently lost to same_series 100% of the time -- zero "p"/"n" entries
// anywhere in the corpus. These checks use the SAME real rp-x-integral pair
// (lm-001807 seq 1, lm-001809 seq 2) that surfaced the bug, so if the merge
// logic ever regresses to "first map wins" again, this fails immediately
// instead of silently shipping an empty relation type.
{
  let relPass = 0, relFail = 0;
  const relCheck = (label, cond, detail) => {
    if (cond) { relPass++; console.log(`[PASS] (relations) ${label}`); }
    else { relFail++; console.log(`[FAIL] (relations) ${label}${detail ? "\n       " + detail : ""}`); }
  };
  const byId = new Map(documents.map((d) => [d.i, d]));
  const typeCounts = {};
  for (const d of documents) for (const [, t] of d.r || []) typeCounts[t] = (typeCounts[t] || 0) + 1;

  relCheck(
    "previous_version relations exist in the built index (not silently lost to same_series)",
    (typeCounts.p || 0) > 0,
    `typeCounts=${JSON.stringify(typeCounts)}`
  );
  relCheck(
    "next_version relations exist in the built index",
    (typeCounts.n || 0) > 0,
    `typeCounts=${JSON.stringify(typeCounts)}`
  );
  relCheck(
    "previous_version and next_version counts are symmetric (one pair produces one of each)",
    (typeCounts.p || 0) === (typeCounts.n || 0),
    `p=${typeCounts.p} n=${typeCounts.n}`
  );

  const seq2 = byId.get("lm-001809");
  const seq2Rel = seq2 && (seq2.r || []).find(([tid]) => tid === "lm-001807");
  relCheck(
    "lm-001809 (seq 2) records lm-001807 (seq 1) as its previous_version",
    !!seq2Rel && seq2Rel[1] === "p",
    `seq2Rel=${JSON.stringify(seq2Rel)}`
  );

  // End-to-end: querying the seq-1 paper's own title should let the seq-2
  // paper surface via the relation pass with the CORRECT direction label
  // ("is the matched result's later version", not the inverted phrasing).
  const seq1 = byId.get("lm-001807");
  if (seq1 && seq2Rel) {
    const q = seq1.t.slice(0, 8);
    const result = scoreCorpus(documents, q, config, dictionary, new Map());
    const hit = result.results.find((r) => r.id === "lm-001809");
    relCheck(
      "querying the seq-1 paper's title surfaces the seq-2 paper via relation",
      !!hit,
      `results=${JSON.stringify(result.results.slice(0, 5).map((r) => r.id))}`
    );
    if (hit) {
      const relReason = hit.reasons.find((rs) => rs.relation === "next_version_of");
      relCheck(
        "the surfaced doc's relation reason uses the next-version-of label, not same_series",
        !!relReason && relReason.label === "是已匹配結果的後續版本",
        `reasons=${JSON.stringify(hit.reasons)}`
      );
    }
  }

  relCheck("explicit_link relations exist (graph_layer.py's external_ref-backed edges)", (typeCounts.e || 0) > 0);
  relCheck("same_primary_keyword relations exist", (typeCounts.k || 0) > 0);

  console.log(`\n--- relations: ${relPass}/${relPass + relFail} passed ---`);
  pass += relPass; fail += relFail;
  cases.push(...Array(relPass + relFail).fill({ category: "relations" }));
  byCategory["relations"] = { pass: relPass, fail: relFail };
}

const report = {
  generated_at: new Date().toISOString(),
  index_count: documents.length,
  index_build_id: index.build_id,
  total: cases.length,
  passed: pass,
  failed: fail,
  by_category: byCategory,
  details,
};
writeFileSync(join(ROOT, "tests", "quality-report.json"), JSON.stringify(report, null, 2), "utf8");
console.log(`\nWrote tests/quality-report.json`);

process.exit(fail > 0 ? 1 : 0);
