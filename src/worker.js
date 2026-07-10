/**
 * Unified Worker — Logic Matrix Corpus Engine.
 *
 * This project deploys via `wrangler deploy` with Static Assets (assets.directory),
 * which does NOT honour the Pages `functions/` convention. So every dynamic route
 * lives here in one Worker; everything else is served from the ASSETS binding.
 *
 *   GET  /api/base-space         Triadic-Logic graph (id-keyed KV: weights2/states2)
 *   GET  /api/log-crawler?id=    1x1 tracking GIF + crawler-driven graph mutation
 *   GET  /api/tcf-queue          demand-driven TCF queue: hottest un-mapped (hollow)
 *                                nodes by ~48h crawler attention (lazy instantiation)
 *   GET  /papers/<slug>(.html)   301 -> canonical /p/{id}/ or /raw/{id}.{ext}
 *   *                            static asset (env.ASSETS)
 */

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

const BOT_KEYWORDS = [
  "bot", "crawler", "spider", "scrape", "archiver", "curl", "wget",
  "python-requests", "google", "baidu", "yandex", "bing", "slurp", "duckduckgo",
];

// module-scope cache: slug -> {id, ext} (warm isolates skip the re-fetch)
let LEGACY_MAP = null;

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const p = url.pathname;
    try {
      if (p === "/api/base-space") return await baseSpace(request, env);
      if (p === "/api/log-crawler") return await logCrawler(request, env, ctx);
      if (p === "/api/tcf-queue") return await tcfQueue(request, env);
      if (p.startsWith("/papers/")) return await papersRedirect(request, env);
      // machine-layer JSON is cross-origin readable (spectral.evemisslab.com + agents)
      if ((p.startsWith("/ai/") && p.endsWith(".json")) || p === "/papers-metadata.json") {
        const res = await env.ASSETS.fetch(request);
        const h = new Headers(res.headers);
        h.set("Access-Control-Allow-Origin", "*");
        return new Response(res.body, { status: res.status, statusText: res.statusText, headers: h });
      }
      if (p.startsWith("/raw/")) return await rawAsset(request, env);
      if (p.startsWith("/media/")) return await mediaAsset(request, env);
    } catch (e) {
      // never let a dynamic-route error break static serving
    }
    return env.ASSETS.fetch(request);
  },
};

// ---- /raw/{id}.{ext} : serve the source, but tag text with charset=utf-8 ----
// Static Assets returns .md as "text/markdown" WITHOUT a charset (and .py/.lean
// with NO content-type at all), so browsers guess the encoding and mojibake CJK
// (fine for AI/curl on raw bytes, broken for humans clicking "Raw source"). Force
// the right text type + charset by extension; leave body/status untouched, and
// never HTML-wrap (keeps the AI raw-source / rel=alternate=text/markdown contract).
const RAW_TEXT_CT = {
  md: "text/markdown", py: "text/x-python", lean: "text/plain",
  ts: "text/typescript", jsx: "text/jsx", tex: "text/x-tex", txt: "text/plain",
};
async function rawAsset(request, env) {
  const res = await env.ASSETS.fetch(request);
  if (res.status !== 200) return res;
  const m = new URL(request.url).pathname.match(/\.([a-z0-9]+)$/i);
  const ext = m ? m[1].toLowerCase() : "";
  const ct = res.headers.get("content-type") || "";
  let next = RAW_TEXT_CT[ext] ? `${RAW_TEXT_CT[ext]}; charset=utf-8`
    : (/^text\//i.test(ct) && !/charset/i.test(ct)) ? `${ct}; charset=utf-8` : null;
  if (!next) return res;
  const headers = new Headers(res.headers);
  headers.set("content-type", next);
  return new Response(res.body, { status: res.status, statusText: res.statusText, headers });
}

function assetFetch(request, env, path) {
  return env.ASSETS.fetch(new Request(new URL(path, request.url).toString()));
}

// ---- /media/{id}.{ext} : serve audio/video from R2 (env.MEDIA). Files are too large
// for Static Assets (>25 MiB), so they live in R2. Supports HTTP range (seeking).
// Graceful when the R2 binding is absent (503) so the worker still deploys before R2
// is enabled in the dashboard + bound in wrangler.jsonc.
async function mediaAsset(request, env) {
  if (!env.MEDIA) return new Response("Media store not configured (R2 pending).", { status: 503 });
  const key = decodeURIComponent(new URL(request.url).pathname.replace(/^\/media\//, ""));
  const rangeHeader = request.headers.get("range");
  let range;
  if (rangeHeader) {
    const m = /^bytes=(\d*)-(\d*)$/.exec(rangeHeader);
    if (m) {
      const start = m[1] ? parseInt(m[1], 10) : undefined;
      const end = m[2] ? parseInt(m[2], 10) : undefined;
      if (start !== undefined && end !== undefined) range = { offset: start, length: end - start + 1 };
      else if (start !== undefined) range = { offset: start };
      else if (end !== undefined) range = { suffix: end };
    }
  }
  const obj = await env.MEDIA.get(key, range ? { range } : undefined);
  if (!obj) return new Response("Not found", { status: 404 });
  const h = new Headers();
  obj.writeHttpMetadata(h);
  h.set("etag", obj.httpEtag);
  h.set("accept-ranges", "bytes");
  h.set("cache-control", "public, max-age=86400");
  if (obj.range && "offset" in obj.range) {
    const off = obj.range.offset || 0;
    const len = obj.range.length ?? (obj.size - off);
    h.set("content-range", `bytes ${off}-${off + len - 1}/${obj.size}`);
    return new Response(obj.body, { status: 206, headers: h });
  }
  return new Response(obj.body, { headers: h });
}

// ---- /api/base-space : id-keyed Triadic-Logic adjacency + state matrix ----
// Order of truth (handoff spec §4): real TCF dependency graph (/ai/graph.json,
// built from registry/tcf/ extractions) > KV crawler-attention layer > simulated seed.
async function baseSpace(request, env) {
  if (request.method === "OPTIONS") return new Response(null, { headers: CORS });
  const hasKV = !!env.BASE_SPACE_KV;
  let weights = null, states = null, hits = 0;

  // L1 real topology: if the build produced /ai/graph.json, serve the real graph.
  try {
    const g = await assetFetch(request, env, "/ai/graph.json");
    if (g.ok) {
      const graph = await g.json();
      if (graph && Array.isArray(graph.nodes) && Array.isArray(graph.edges)) {
        const w = {}, s = {}, edgeMeta = {};
        for (const n of graph.nodes) {
          w[n.id] = { [n.id]: 1.0 };
          s[n.id] = n.state || "omega";
        }
        for (const e of graph.edges) {
          if (!w[e.from]) w[e.from] = { [e.from]: 1.0 };
          w[e.from][e.to] = e.weight;
          edgeMeta[e.from + "|" + e.to] = {
            type: e.type,
            evidence: (e.evidence && e.evidence[0]) || null,
          };
        }
        if (hasKV) {
          try { hits = parseInt(await env.BASE_SPACE_KV.get("hits") || "0", 10); } catch (err) { /* attention layer optional */ }
        }
        return new Response(JSON.stringify({
          weights: w, states: s, hits,
          edge_meta: edgeMeta,
          meta: {
            source: "tcf-graph",
            version: graph.version,
            mapped: graph.nodes.length,
            total: (graph.coverage && graph.coverage.papers_total) || null,
            note: "Real TCF-extracted dependency topology (Phase A). Unmapped papers are absent, not zero.",
          },
        }), { headers: { ...CORS, "Content-Type": "application/json" } });
      }
    }
  } catch (e) { /* fall through to KV / simulated seed */ }

  if (hasKV) {
    try {
      const w = await env.BASE_SPACE_KV.get("weights2");
      const s = await env.BASE_SPACE_KV.get("states2");
      const h = await env.BASE_SPACE_KV.get("hits");
      if (w && s) { weights = JSON.parse(w); states = JSON.parse(s); hits = parseInt(h || "0", 10); }
    } catch (e) { /* fall through to seed */ }
  }

  if (!weights || !states) {
    try {
      const res = await assetFetch(request, env, "/papers-metadata.json");
      if (res.ok) {
        const papers = await res.json();
        weights = {}; states = {}; hits = 1310;
        papers.forEach((n1) => {
          weights[n1.id] = {};
          let hash = 0;
          for (let i = 0; i < n1.title.length; i++) hash = n1.title.charCodeAt(i) + ((hash << 5) - hash);
          const sv = Math.abs(hash % 3);
          states[n1.id] = sv === 0 ? "omega" : (sv === 1 ? "true" : "false");
          papers.forEach((n2) => {
            if (n1.id === n2.id) {
              weights[n1.id][n2.id] = 1.0;
            } else {
              const match = (n1.lang === n2.lang) ? 0.2 : 0.02;
              const seed = Math.abs((hash + n2.title.length) % 100) / 100;
              weights[n1.id][n2.id] = seed < 0.15 ? seed * 4.0 * match : 0;
            }
          });
        });
        if (hasKV) {
          await env.BASE_SPACE_KV.put("weights2", JSON.stringify(weights));
          await env.BASE_SPACE_KV.put("states2", JSON.stringify(states));
          await env.BASE_SPACE_KV.put("hits", String(hits));
        }
      }
    } catch (err) {
      return new Response(JSON.stringify({ error: String(err && err.message || err) }), {
        status: 500, headers: { ...CORS, "Content-Type": "application/json" },
      });
    }
  }

  return new Response(JSON.stringify({ weights, states, hits }), {
    headers: { ...CORS, "Content-Type": "application/json" },
  });
}

// ---- /api/log-crawler : tracking pixel + crawler-driven graph mutation ----
async function logCrawler(request, env, ctx) {
  if (request.method === "OPTIONS") return new Response(null, { headers: CORS });
  const url = new URL(request.url);
  const targetId = url.searchParams.get("id") || url.searchParams.get("slug");
  const ua = request.headers.get("User-Agent") || "";
  const referer = request.headers.get("Referer") || "";
  const hasKV = !!env.BASE_SPACE_KV;
  const isBot = BOT_KEYWORDS.some((kw) => ua.toLowerCase().includes(kw));

  // Only crawlers drive the graph; human views must not mutate it.
  if (hasKV && targetId && isBot) {
    // Cost-transfer gate (Neo's B2B billing trigger): a single node's daily
    // attention accounting saturates at ABUSE_CEILING hits. Beyond that the
    // bot gets 429 + a machine-readable licensing announcement instead of a
    // free vote — this also hard-caps zero-sum bid manipulation (no bot can
    // buy more than CEILING votes/day/node with crawl budget alone).
    const ABUSE_CEILING = 300;
    const day = new Date().toISOString().slice(0, 10).replace(/-/g, "");
    let hot = null;
    try {
      hot = JSON.parse(await env.BASE_SPACE_KV.get("hot2") || "{}");
      const rec0 = hot[targetId];
      if (rec0 && rec0.d === day && (rec0.c || 0) >= ABUSE_CEILING) {
        const now = new Date();
        const midnight = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate() + 1) / 1000;
        const retryAfter = Math.max(60, Math.floor(midnight - now.getTime() / 1000));
        return new Response(JSON.stringify({
          error: "rate_limited",
          status: 429,
          node: targetId,
          message: "This hollow node is not yet TCF-instantiated and its daily attention "
                 + "accounting is saturated. Ranking follows zero-sum daily bidding "
                 + "(/api/tcf-queue). To force-unlock distillation or obtain a dedicated "
                 + "high-frequency API, contact licensing with an enterprise key request.",
          licensing: "mailto:kakon77777@gmail.com",
          rights: "/ai/rights-spectrum.json",
          queue: "/api/tcf-queue",
        }), {
          status: 429,
          headers: { ...CORS, "Content-Type": "application/json", "Retry-After": String(retryAfter) },
        });
      }
    } catch (e) { hot = null; /* gate is best-effort; never break tracking */ }

    const work = (async () => {
      try {
        const storedHits = await env.BASE_SPACE_KV.get("hits") || "0";
        await env.BASE_SPACE_KV.put("hits", String(parseInt(storedHits, 10) + 1));

        const nodeKey = `hits_${targetId}`;
        const nodeHits = parseInt(await env.BASE_SPACE_KV.get(nodeKey) || "0", 10) + 1;
        await env.BASE_SPACE_KV.put(nodeKey, String(nodeHits));

        // Demand signal for lazy TCF instantiation: per-id day-bucketed heat
        // (hot2 = {id: {d: today, c: n, pd: prevDay, p: n}}). Cumulative hits_
        // measure lifetime attention; hot2 measures the ~48h burst that decides
        // which hollow node gets TCF-distilled next. Races lose a count or two —
        // acceptable for a scheduling heuristic.
        try {
          if (!hot) hot = JSON.parse(await env.BASE_SPACE_KV.get("hot2") || "{}");
          const rec = hot[targetId] || {};
          if (rec.d === day) {
            rec.c = (rec.c || 0) + 1;
          } else {
            rec.pd = rec.d; rec.p = rec.c || 0;
            rec.d = day; rec.c = 1;
          }
          hot[targetId] = rec;
          await env.BASE_SPACE_KV.put("hot2", JSON.stringify(hot));
        } catch (err) { /* heat tracking is best-effort */ }

        let sourceId = null;
        if (referer) {
          try {
            const m = new URL(referer).pathname.match(/\/p\/([^/]+)\/?/);
            if (m) sourceId = decodeURIComponent(m[1]);
          } catch (e) { /* ignore */ }
        }

        const w = await env.BASE_SPACE_KV.get("weights2");
        const s = await env.BASE_SPACE_KV.get("states2");
        if (w && s) {
          const weights = JSON.parse(w);
          const states = JSON.parse(s);
          if (sourceId && weights[sourceId] && sourceId !== targetId) {
            weights[sourceId][targetId] = Math.min(1.0, (weights[sourceId][targetId] || 0) + 0.08);
          }
          if (nodeHits > 20) states[targetId] = "true";
          else if (nodeHits > 1) states[targetId] = "omega";
          await env.BASE_SPACE_KV.put("weights2", JSON.stringify(weights));
          await env.BASE_SPACE_KV.put("states2", JSON.stringify(states));
        }
      } catch (err) { /* fail-safe */ }
    })();
    ctx.waitUntil(work);
  }

  const gif = Uint8Array.from(
    atob("R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"),
    (c) => c.charCodeAt(0),
  );
  return new Response(gif, {
    headers: { "Content-Type": "image/gif", "Cache-Control": "no-cache, no-store, must-revalidate", ...CORS },
  });
}

// ---- /api/tcf-queue : demand-driven lazy-instantiation queue ----
// Market-scheduled compute (handoff spec Phase B, Neo's lazy-instantiation design):
// un-mapped (hollow) nodes ranked by ~48h crawler heat. Agents ("衍") poll this,
// TCF-distill the hottest papers first, and the adversarial gate + git commit
// remain the only path into the published graph.
async function tcfQueue(request, env) {
  if (request.method === "OPTIONS") return new Response(null, { headers: CORS });
  const url = new URL(request.url);
  const minHits = Math.max(1, parseInt(url.searchParams.get("min") || "3", 10) || 3);
  const limit = Math.min(50, Math.max(1, parseInt(url.searchParams.get("limit") || "10", 10) || 10));

  let hot = {};
  if (env.BASE_SPACE_KV) {
    try { hot = JSON.parse(await env.BASE_SPACE_KV.get("hot2") || "{}"); } catch (e) { /* empty */ }
  }

  const mapped = new Set();
  try {
    const g = await assetFetch(request, env, "/ai/graph.json");
    if (g.ok) for (const n of (await g.json()).nodes || []) mapped.add(n.id);
  } catch (e) { /* no graph yet -> everything is hollow */ }

  const meta = {};
  try {
    const r = await assetFetch(request, env, "/papers-metadata.json");
    if (r.ok) for (const p of await r.json()) meta[p.id] = p;
  } catch (e) { /* titles optional */ }

  const daySlots = Math.min(10, Math.max(1, parseInt(url.searchParams.get("slots") || "2", 10) || 2));

  const day = new Date().toISOString().slice(0, 10).replace(/-/g, "");
  const yday = new Date(Date.now() - 86400000).toISOString().slice(0, 10).replace(/-/g, "");
  const candidates = [];
  for (const id in hot) {
    if (mapped.has(id)) continue;
    const rec = hot[id] || {};
    let recent = 0;
    if (rec.d === day) recent = (rec.c || 0) + (rec.pd === yday ? (rec.p || 0) : 0);
    else if (rec.d === yday) recent = rec.c || 0;
    if (recent >= minHits) {
      const m = meta[id];
      if (!m) continue; // crawlers probe nonexistent ids — registry-known papers only
      candidates.push({ id, title: m.title, canonical: m.canonical || `/p/${id}/`,
                        recent_hits: recent, state: "hollow" });
    }
  }
  candidates.sort((a, b) => b.recent_hits - a.recent_hits || (a.id < b.id ? -1 : 1));

  // Dynamic watermark (Neo's floating threshold): the deeper the queue, the
  // higher the bar — rank 0-4 needs base min, 5-9 needs x10, 10-14 x100, …
  // Guarantees crawler hunger can never blow past the compute ceiling.
  const queue = [];
  for (const item of candidates) {
    const bar = minHits * Math.pow(10, Math.floor(queue.length / 5));
    if (item.recent_hits >= bar) {
      item.rank = queue.length + 1;
      item.effective_threshold = bar;
      // Zero-sum daily bidding: only the top daySlots get distilled at
      // settlement; the rest are outbid and must keep voting tomorrow.
      item.bid_status = queue.length < daySlots ? "leading" : "outbid";
      queue.push(item);
    }
  }

  return new Response(JSON.stringify({
    version: "0.2",
    window: "~48h (today + yesterday, UTC day buckets)",
    policy: {
      base_threshold: minHits,
      dynamic_watermark: "effective threshold x10 per 5 already-queued items",
      daily_slots: daySlots,
      settlement: "daily, by the local agent 衍 (top slots only; zero-sum bidding)",
      abuse_ceiling: "300 hits/node/day, then HTTP 429 + licensing announcement",
    },
    mapped_total: mapped.size,
    hollow_tracked: Object.keys(hot).filter((id) => !mapped.has(id)).length,
    queue: queue.slice(0, limit),
    note: "Demand-driven lazy TCF instantiation: hollow nodes ranked by recent crawler "
        + "attention under zero-sum daily bidding. Extraction still passes the adversarial "
        + "edge gate before publication. Agents may propose, only the gated pipeline "
        + "publishes (see /ai/rights-spectrum.json).",
  }), { headers: { ...CORS, "Content-Type": "application/json", "Cache-Control": "public, max-age=60" } });
}

// ---- /papers/<slug>(.html) : dynamic 301 to canonical id routes ----
async function papersRedirect(request, env) {
  const url = new URL(request.url);
  const last = decodeURIComponent(url.pathname.split("/").pop() || "");
  const isPage = last.endsWith(".html");
  const slug = isPage ? last.slice(0, -5) : last;
  if (!slug) return env.ASSETS.fetch(request);

  if (!LEGACY_MAP) {
    try {
      const r = await assetFetch(request, env, "/papers-legacy-map.json");
      LEGACY_MAP = r.ok ? await r.json() : {};
    } catch (e) { LEGACY_MAP = {}; }
  }

  const entry = LEGACY_MAP[slug];
  if (!entry) return env.ASSETS.fetch(request); // unknown legacy slug -> let assets 404

  const target = isPage ? `/p/${entry.id}/` : `/raw/${entry.id}.${entry.ext}`;
  return new Response(null, {
    status: 301,
    headers: { "Location": target + url.search, "Cache-Control": "public, max-age=31536000, immutable" },
  });
}
