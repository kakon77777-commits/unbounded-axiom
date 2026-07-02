/**
 * Unified Worker — Logic Matrix Corpus Engine.
 *
 * This project deploys via `wrangler deploy` with Static Assets (assets.directory),
 * which does NOT honour the Pages `functions/` convention. So every dynamic route
 * lives here in one Worker; everything else is served from the ASSETS binding.
 *
 *   GET  /api/base-space         Triadic-Logic graph (id-keyed KV: weights2/states2)
 *   GET  /api/log-crawler?id=    1x1 tracking GIF + crawler-driven graph mutation
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
      if (p.startsWith("/papers/")) return await papersRedirect(request, env);
    } catch (e) {
      // never let a dynamic-route error break static serving
    }
    return env.ASSETS.fetch(request);
  },
};

function assetFetch(request, env, path) {
  return env.ASSETS.fetch(new Request(new URL(path, request.url).toString()));
}

// ---- /api/base-space : id-keyed Triadic-Logic adjacency + state matrix ----
async function baseSpace(request, env) {
  if (request.method === "OPTIONS") return new Response(null, { headers: CORS });
  const hasKV = !!env.BASE_SPACE_KV;
  let weights = null, states = null, hits = 0;

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
    const work = (async () => {
      try {
        const storedHits = await env.BASE_SPACE_KV.get("hits") || "0";
        await env.BASE_SPACE_KV.put("hits", String(parseInt(storedHits, 10) + 1));

        const nodeKey = `hits_${targetId}`;
        const nodeHits = parseInt(await env.BASE_SPACE_KV.get(nodeKey) || "0", 10) + 1;
        await env.BASE_SPACE_KV.put(nodeKey, String(nodeHits));

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
