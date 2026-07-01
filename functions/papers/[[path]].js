// functions/papers/[[path]].js
// Catch-all: dynamically 301 ANY /papers/<slug>(.html) to its id-native target.
// Resolves <slug> -> {id, ext} via a lean /papers-legacy-map.json the build emits.
let MAP_CACHE = null;

export async function onRequest(context) {
  const { request, params, next } = context;
  const url = new URL(request.url);

  // params.path is an array for [[path]] (e.g. ["2050.md.html"] or ["sub","x.md"]).
  const parts = Array.isArray(params.path) ? params.path : [params.path].filter(Boolean);
  const last = parts.length ? decodeURIComponent(parts[parts.length - 1]) : "";

  // Strip a single trailing .html (legacy PAGE form: <slug>.<ext>.html or <slug>.html).
  // Whatever remains is the legacy slug exactly as keyed in papers.json (e.g. "2050.md").
  const isLegacyPage = last.endsWith(".html");
  const slug = isLegacyPage ? last.slice(0, -5) : last;
  if (!slug) return next();

  // Load + cache the slug -> {id, ext} map (small; see data_threading for shape).
  if (!MAP_CACHE) {
    try {
      const res = await fetch(new URL("/papers-legacy-map.json", url.origin));
      MAP_CACHE = res.ok ? await res.json() : {};
    } catch (e) { MAP_CACHE = {}; }
  }

  const entry = MAP_CACHE[slug];
  if (!entry) return next(); // unknown legacy slug -> let Pages 404

  // Legacy PAGE  (/papers/<slug>.html)      -> canonical page  /p/<id>/
  // Legacy RAW   (/papers/<slug>, no .html) -> raw file        /raw/<id>.<ext>
  const target = isLegacyPage
    ? `/p/${entry.id}/`
    : `/raw/${entry.id}.${entry.ext}`;

  return new Response(null, {
    status: 301,
    headers: {
      "Location": target + url.search,
      "Cache-Control": "public, max-age=31536000, immutable"
    }
  });
}
