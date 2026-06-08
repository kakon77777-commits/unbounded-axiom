export async function onRequest(context) {
  const { request, env, next } = context;
  
  // 1. Fetch the actual file (HTML, raw Markdown, Python script, PDF, etc.)
  const response = await next();
  
  const url = new URL(request.url);
  const ua = request.headers.get("User-Agent") || "";
  const referer = request.headers.get("Referer") || "";
  
  // 2. Detect bot / crawler
  const botKeywords = ["bot", "crawler", "spider", "scrape", "archiver", "curl", "wget", "python-requests", "google", "baidu", "yandex", "bing", "slurp", "duckduckgo"];
  const isBot = botKeywords.some(kw => ua.toLowerCase().includes(kw));
  
  const hasKV = !!env.BASE_SPACE_KV;
  
  if (hasKV && isBot) {
    // Extract file name from URL path
    const pathParts = url.pathname.split("/");
    const filename = decodeURIComponent(pathParts[pathParts.length - 1]);
    
    // Normalize slug (e.g. "some-slug.md.html" -> "some-slug.md", "some-slug.md" -> "some-slug.md")
    let slug = filename;
    if (slug.endsWith(".html")) {
      slug = slug.substring(0, slug.length - 5);
    }
    
    // Run KV logging asynchronously in the background to ensure no latency penalty for crawlers
    context.waitUntil((async () => {
      try {
        // Increment global crawler hits
        const storedHits = await env.BASE_SPACE_KV.get("hits") || "0";
        let hits = parseInt(storedHits, 10) + 1;
        await env.BASE_SPACE_KV.put("hits", String(hits));
        
        // Increment hits for this specific node
        const nodeHitsKey = `hits_${slug}`;
        const storedNodeHits = await env.BASE_SPACE_KV.get(nodeHitsKey) || "0";
        let nodeHits = parseInt(storedNodeHits, 10) + 1;
        await env.BASE_SPACE_KV.put(nodeHitsKey, String(nodeHits));
        
        // Extract source slug from Referer header to compute causal coupling weights
        let sourceSlug = null;
        if (referer) {
          try {
            const refererUrl = new URL(referer);
            if (refererUrl.pathname.includes("/papers/")) {
              const refParts = refererUrl.pathname.split("/");
              let refFilename = decodeURIComponent(refParts[refParts.length - 1]);
              if (refFilename.endsWith(".html")) {
                refFilename = refFilename.substring(0, refFilename.length - 5);
              }
              sourceSlug = refFilename;
            }
          } catch (e) {
            // Ignore referer parsing errors
          }
        }
        
        // Load weights and states
        const storedWeights = await env.BASE_SPACE_KV.get("weights");
        const storedStates = await env.BASE_SPACE_KV.get("states");
        
        if (storedWeights && storedStates) {
          const weights = JSON.parse(storedWeights);
          const states = JSON.parse(storedStates);
          
          // Strengthen coupling weight if a referer hop is found
          if (sourceSlug && weights[sourceSlug] && sourceSlug !== slug) {
            const currentWeight = weights[sourceSlug][slug] || 0;
            weights[sourceSlug][slug] = Math.min(1.0, currentWeight + 0.08);
          }
          
          // Self-Healing Triadic Logic state transitions
          if (nodeHits > 20) {
            states[slug] = "true";
          } else if (nodeHits > 1) {
            states[slug] = "omega";
          }
          
          await env.BASE_SPACE_KV.put("weights", JSON.stringify(weights));
          await env.BASE_SPACE_KV.put("states", JSON.stringify(states));
        }
      } catch (err) {
        // Fail-safe
      }
    })());
  }
  
  return response;
}
