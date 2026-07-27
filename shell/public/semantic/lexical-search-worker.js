// Web Worker: owns the semantic index + scoring loop off the main thread, per
// spec §16.1 ("以 Web Worker 完成：精確搜尋／token overlap／trigram／欄位加權／顯影控制").
import { scoreCorpus, prepareIndex, DEFAULT_CONFIG } from "./semantic-core.js";

let documents = null;
let dictionary = [];
let config = DEFAULT_CONFIG;
let meta = null;
let loadError = null;

async function ensureLoaded() {
  if (documents || loadError) return;
  try {
    const [idxRes, cfgRes, dictRes] = await Promise.all([
      fetch("/ai/semantic-index.min.json"),
      fetch("/semantic/search.config.json").catch(() => null),
      fetch("/ai/semantic-dictionary.min.json").catch(() => null),
    ]);
    if (!idxRes.ok) throw new Error(`index fetch failed: ${idxRes.status}`);
    const idx = await idxRes.json();
    documents = prepareIndex(idx.documents || []);
    meta = { count: idx.count, generated_at: idx.generated_at, build_id: idx.build_id, channels: idx.channels };
    if (cfgRes && cfgRes.ok) {
      try {
        const loaded = await cfgRes.json();
        config = {
          ...DEFAULT_CONFIG, ...loaded,
          search: { ...DEFAULT_CONFIG.search, ...loaded.search },
          tiers: { ...DEFAULT_CONFIG.tiers, ...loaded.tiers },
          weights: { ...DEFAULT_CONFIG.weights, ...loaded.weights },
          channels: { ...DEFAULT_CONFIG.channels, ...loaded.channels },
          expansion_limits: { ...DEFAULT_CONFIG.expansion_limits, ...loaded.expansion_limits },
          display: { ...DEFAULT_CONFIG.display, ...loaded.display },
        };
      } catch { /* keep DEFAULT_CONFIG */ }
    }
    // Dictionary is optional — Phase 2 degrades to Phase 1 (no expansion) if
    // it's missing or fails to parse, exactly like the config fetch above.
    if (dictRes && dictRes.ok) {
      try {
        const loadedDict = await dictRes.json();
        dictionary = loadedDict.entries || [];
      } catch { /* keep dictionary = [] */ }
    }
  } catch (e) {
    loadError = String(e && e.message || e);
    documents = [];
  }
}

self.onmessage = async (e) => {
  const { type, query, reqId } = e.data || {};
  if (type === "init") {
    await ensureLoaded();
    self.postMessage({ type: "ready", reqId, meta, config, error: loadError });
    return;
  }
  if (type === "search") {
    await ensureLoaded();
    if (loadError) {
      self.postMessage({ type: "error", reqId, error: loadError });
      return;
    }
    const t0 = Date.now();
    const result = scoreCorpus(documents, query, config, dictionary);
    self.postMessage({ type: "result", reqId, query, result, meta, latency_ms: Date.now() - t0 });
  }
};
