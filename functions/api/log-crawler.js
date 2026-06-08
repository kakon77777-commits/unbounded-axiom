export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const targetSlug = url.searchParams.get("slug");
  
  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
  
  if (request.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  const hasKV = !!env.BASE_SPACE_KV;
  const ua = request.headers.get("User-Agent") || "";
  const referer = request.headers.get("Referer") || "";
  
  const botKeywords = ["bot", "crawler", "spider", "scrape", "archiver", "curl", "wget", "python-requests", "google", "baidu", "yandex", "bing", "slurp", "duckduckgo"];
  const isBot = botKeywords.some(kw => ua.toLowerCase().includes(kw));
  
  if (hasKV && targetSlug) {
    try {
      // 1. Increment global crawler hits
      const storedHits = await env.BASE_SPACE_KV.get("hits") || "0";
      let hits = parseInt(storedHits, 10);
      hits++;
      await env.BASE_SPACE_KV.put("hits", String(hits));
      
      // 2. Log hits for this specific paper slug to drive Triadic Logic transitions
      const nodeHitsKey = `hits_${targetSlug}`;
      const storedNodeHits = await env.BASE_SPACE_KV.get(nodeHitsKey) || "0";
      let nodeHits = parseInt(storedNodeHits, 10) + 1;
      await env.BASE_SPACE_KV.put(nodeHitsKey, String(nodeHits));
      
      // 3. Extract source slug from Referer header if crawled from another paper
      let sourceSlug = null;
      if (referer) {
        try {
          const refererUrl = new URL(referer);
          if (refererUrl.pathname.includes("/papers/")) {
            const match = refererUrl.pathname.match(/\/papers\/([^\/]+)\.html/);
            if (match) {
              sourceSlug = decodeURIComponent(match[1]);
            }
          }
        } catch (e) {
          // Ignore URL parsing errors
        }
      }
      
      // 4. Update coupling weights & states matrix
      const storedWeights = await env.BASE_SPACE_KV.get("weights");
      const storedStates = await env.BASE_SPACE_KV.get("states");
      
      if (storedWeights && storedStates) {
        const weights = JSON.parse(storedWeights);
        const states = JSON.parse(storedStates);
        
        // Causal feedback: strengthen the link between source and target
        if (sourceSlug && weights[sourceSlug] && sourceSlug !== targetSlug) {
          const currentWeight = weights[sourceSlug][targetSlug] || 0;
          // Reinforce connection weight by +0.08, capped at 1.0
          weights[sourceSlug][targetSlug] = Math.min(1.0, currentWeight + 0.08);
        }
        
        // Self-Healing Triadic Logic state transitions
        if (nodeHits > 20) {
          // Resolved state: absolute truth core (⊤)
          states[targetSlug] = "true";
        } else if (nodeHits > 1) {
          // Actively evolving state: spiral state (Ω)
          states[targetSlug] = "omega";
        }
        
        await env.BASE_SPACE_KV.put("weights", JSON.stringify(weights));
        await env.BASE_SPACE_KV.put("states", JSON.stringify(states));
      }
    } catch (err) {
      // Fail-safe: do not crash crawler tracking, return tracking pixel anyway
    }
  }
  
  // Return 1x1 transparent tracking GIF
  const gifBase64 = "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
  const gifBuffer = Uint8Array.from(atob(gifBase64), c => c.charCodeAt(0));
  
  return new Response(gifBuffer, {
    headers: {
      "Content-Type": "image/gif",
      "Cache-Control": "no-cache, no-store, must-revalidate",
      "Pragma": "no-cache",
      ...corsHeaders
    }
  });
}
