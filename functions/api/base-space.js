export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  
  // CORS Headers
  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
  
  if (request.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders });
  }

  // Graceful degradation fallback if KV is not bound
  const hasKV = !!env.BASE_SPACE_KV;
  
  let weights = null;
  let states = null;
  let hits = 0;
  
  if (hasKV) {
    try {
      const storedWeights = await env.BASE_SPACE_KV.get("weights2");
      const storedStates = await env.BASE_SPACE_KV.get("states2");
      const storedHits = await env.BASE_SPACE_KV.get("hits");
      
      if (storedWeights && storedStates) {
        weights = JSON.parse(storedWeights);
        states = JSON.parse(storedStates);
        hits = parseInt(storedHits || "0", 10);
      }
    } catch (e) {
      // Ignore KV read errors and fallback to initialization
    }
  }
  
  // If not found in KV (or no KV), fetch metadata and initialize
  if (!weights || !states) {
    try {
      const metadataUrl = new URL("/papers-metadata.json", request.url);
      const res = await fetch(metadataUrl);
      if (res.ok) {
        const papers = await res.json();
        
        // Generate initial deterministic weights and states
        weights = {};
        states = {};
        hits = 1310; // default initial counter
        
        papers.forEach(n1 => {
          // id-native seed: key the matrix by stable id (n1.id), not legacy slug.
          weights[n1.id] = {};

          let hash = 0;
          for (let i = 0; i < n1.title.length; i++) {
            hash = n1.title.charCodeAt(i) + ((hash << 5) - hash);
          }

          const stateVal = Math.abs(hash % 3);
          states[n1.id] = stateVal === 0 ? "omega" : (stateVal === 1 ? "true" : "false");

          papers.forEach(n2 => {
            if (n1.id === n2.id) {
              weights[n1.id][n2.id] = 1.0;
            } else {
              const match = (n1.lang === n2.lang) ? 0.2 : 0.02;
              const seedVal = Math.abs((hash + n2.title.length) % 100) / 100;
              weights[n1.id][n2.id] = seedVal < 0.15 ? seedVal * 4.0 * match : 0;
            }
          });
        });

        // Save initial state to KV if available (v2 keys; id-native)
        if (hasKV) {
          await env.BASE_SPACE_KV.put("weights2", JSON.stringify(weights));
          await env.BASE_SPACE_KV.put("states2", JSON.stringify(states));
          await env.BASE_SPACE_KV.put("hits", String(hits));
        }
      }
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 500,
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }
  }
  
  return new Response(JSON.stringify({ weights, states, hits }), {
    headers: { ...corsHeaders, "Content-Type": "application/json" }
  });
}
