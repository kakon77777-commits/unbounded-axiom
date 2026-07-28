// Dynamic Semantic Revealing — Phase 3 vector channel.
// Spec: content/papers/2026/2026-07/02_動態語義顯影_本地端實作技術白皮書_v0.1.md, §16.2
// ("前端精確結果 + 本地向量 API 結果 = 融合顯影 … 若 API 失效，系統退化為精確搜尋，不得整體失效")
// and §26 Phase 3 ("建立文件級嵌入；API 回傳語義結果；加入 C 級顯示").
//
// This site is fully static (dist/ rebuilt from scratch every build — see
// build.py's shutil.rmtree(DIST_DIR)) and every prior phase deliberately
// avoided a server component (§16.1: "無伺服器；不需 API"). Rather than add a
// networked API or a Cloudflare Workers AI binding (a new account-level infra
// dependency), the "API" here is in-browser WASM inference
// (@huggingface/transformers, loaded from jsDelivr — see loadModel() below
// for why a self-hosted copy of the npm dist file does not work unbundled)
// running in this same Worker, compared against the pre-computed document
// vectors from scripts/build_embeddings.py. Same effect as §16.2 — exact
// search never depends on this module, and every export here degrades to
// "no semantic scores" (an empty Map) rather than throwing, so a model-load
// failure (offline, unsupported browser, low-memory mobile) can never break
// the rest of the search per the spec's own "不得整體失效" requirement.
//
// Model: BAAI/bge-small-zh-v1.5 (ONNX: Xenova/bge-small-zh-v1.5), chosen and
// calibrated against this corpus in the implementing session -- see
// scripts/build_embeddings.py's module docstring for the full reasoning.
// The library, model, and ONNX WASM runtime all load from their standard CDN
// locations (jsdelivr / huggingface.co), same as any typical unbundled
// transformers.js deployment -- one-time, browser-cached downloads, not a
// per-query dependency, which is the actual thing §16.1 was avoiding by not
// standing up a networked search API.

const MODEL_NAME = "Xenova/bge-small-zh-v1.5";
const VECTORS_URL = "/ai/semantic-vectors.bin";
const VECTORS_META_URL = "/ai/semantic-vectors-meta.json";
const CHUNKS_URL = "/ai/semantic-chunks.bin";
const CHUNKS_META_URL = "/ai/semantic-chunks-meta.json";

// Calibrated against the real corpus (1881 docs) with a spread of queries
// from "clearly unrelated" (raw cosine maxing out ~0.47-0.48 even for the
// BEST-matching document) to "deeply, repeatedly covered topic" (Riemann
// Hypothesis papers reaching ~0.68 for genuinely on-topic hits). BGE's own
// model card explicitly warns raw cosine is not a fixed-threshold confidence
// value ("a similarity score greater than 0.5 does not indicate similar...
// what matters is relative order"), so these are corpus-calibrated absolute
// floor/ceiling constants (not a per-query relative rescale, which would
// wrongly inflate the "best of a bad bunch" for an off-topic query into
// looking like a strong semantic match) mapping the OBSERVED useful range
// onto [0,1] before the §9 weights.semantic multiplier is applied:
//   floor  (~0.50): below this, even nonsense queries drift this high just
//                    from generic academic-paper embedding-space proximity
//                    -- never a real signal, clamped to 0 contribution.
//   ceiling (~0.62): a very strong, dedicated topical match (reaches close to
//                    weights.semantic's full ceiling, landing in Tier C);
//                    a merely-good match (e.g. 0.55-0.60 raw) lands mid-range,
//                    consistent with Tier D per §10 ("低分語義近似").
const RAW_FLOOR = 0.50;
const RAW_CEILING = 0.62;

let modelPromise = null;
let vectorsPromise = null;
let state = { status: "idle", error: null }; // idle -> loading -> ready | failed

function normalizeRaw(raw) {
  if (raw <= RAW_FLOOR) return 0;
  if (raw >= RAW_CEILING) return 1;
  return (raw - RAW_FLOOR) / (RAW_CEILING - RAW_FLOOR);
}

// Loaded from jsDelivr's `+esm` endpoint rather than a self-hosted copy of
// the npm package's dist file: that dist file (transformers.web.min.js)
// contains internal bare module specifiers for optional backends (e.g.
// `import ... from "onnxruntime-web/webgpu"`) that a bundler resolves via
// node_modules/import maps at build time, but a browser loading it as a raw
// ES module cannot resolve on its own ("Failed to resolve module specifier"
// — confirmed by hand while wiring this up). jsDelivr's `+esm` build
// pre-resolves the whole dependency graph into one self-contained module,
// which is why the library's own docs use exactly this CDN pattern for
// unbundled browser/worker usage instead of a raw dist-file copy.
const LIBRARY_URL = "https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.2.0/+esm";

async function loadModel() {
  const { pipeline } = await import(/* webpackIgnore: true */ LIBRARY_URL);
  return pipeline("feature-extraction", MODEL_NAME, { dtype: "q8" });
}

async function loadVectors() {
  const [metaRes, vecRes] = await Promise.all([fetch(VECTORS_META_URL), fetch(VECTORS_URL)]);
  if (!metaRes.ok || !vecRes.ok) throw new Error("semantic-vectors fetch failed");
  const meta = await metaRes.json();
  const buf = await vecRes.arrayBuffer();
  const flat = new Float32Array(buf);
  const dim = meta.dim;
  const count = flat.length / dim;
  if (!Number.isInteger(count)) throw new Error("semantic-vectors.bin size does not match dim in meta");
  return { meta, flat, dim, count };
}

// Phase 5 (§17.2/§17.3): per-section vectors, complementary to the whole-
// document ones above -- captures WHICH passage matched, not just that some
// part of a 15,000-character paper did. Optional on top of optional: if this
// fetch fails (or is simply slower than the doc-vectors one), doc-level
// scoring alone still works, same graceful-degradation contract as
// everything else in this module. meta.doc_ids[i] is the source document for
// chunk vector i (see scripts/build_chunk_embeddings.py) -- callers need an
// id->index map (built once by the Worker, which already has the full
// document list) to fold a chunk hit back into the doc-index-keyed scores
// Map scoreCorpus expects; this module has no document list of its own.
async function loadChunkVectors() {
  const [metaRes, vecRes] = await Promise.all([fetch(CHUNKS_META_URL), fetch(CHUNKS_URL)]);
  if (!metaRes.ok || !vecRes.ok) throw new Error("semantic-chunks fetch failed");
  const meta = await metaRes.json();
  const buf = await vecRes.arrayBuffer();
  const flat = new Float32Array(buf);
  const dim = meta.dim;
  const count = flat.length / dim;
  if (!Number.isInteger(count) || meta.doc_ids.length !== count) {
    throw new Error("semantic-chunks.bin size does not match dim/doc_ids in meta");
  }
  return { meta, flat, dim, count, docIds: meta.doc_ids, headings: meta.headings || [] };
}

let chunkVectorsPromise = null;
let chunkState = { status: "idle", error: null };

// Kicks off model + vector loading in the background; never throws. Call this
// once at Worker init so loading has a head start before the first real
// search request (debounce + typing time usually cover most of it). Chunk
// vectors load on their own independent track: a chunk-fetch failure never
// touches `state`, only `chunkState` -- doc-level scoring (the Phase 3
// feature this whole module started as) must keep working even if the
// Phase 5 chunk asset 404s, is slow, or the corpus was built before chunk
// embeddings existed.
export function warmUp() {
  if (state.status === "idle") {
    state.status = "loading";
    modelPromise = loadModel().catch((e) => { state.status = "failed"; state.error = String(e); return null; });
    vectorsPromise = loadVectors().catch((e) => { state.status = "failed"; state.error = String(e); return null; });
    Promise.all([modelPromise, vectorsPromise]).then(([model, vectors]) => {
      if (model && vectors) state.status = "ready";
    });
  }
  if (chunkState.status === "idle") {
    chunkState.status = "loading";
    chunkVectorsPromise = loadChunkVectors().catch((e) => {
      chunkState.status = "failed"; chunkState.error = String(e); return null;
    });
    chunkVectorsPromise.then((chunks) => { if (chunks) chunkState.status = "ready"; });
  }
}

export function semanticStatus() {
  return { ...state, chunks: { ...chunkState } };
}

// Shared cosine-similarity sweep against a flat Float32Array of stacked
// vectors. Returns Array<normalizedScore> indexed like `count`; entries for
// a zero-norm vector (no embeddable text) are left as -1 (never a valid
// cosine value) so callers can distinguish "no signal" from "signal of 0".
function sweepCosine(q, flat, dim, count) {
  const out = new Float32Array(count).fill(-1);
  let qNorm = 0;
  for (let j = 0; j < dim; j++) qNorm += q[j] * q[j];
  if (qNorm < 1e-9) return out; // degenerate query embedding
  const qMag = Math.sqrt(qNorm);
  for (let i = 0; i < count; i++) {
    const off = i * dim;
    let dot = 0;
    let dNorm = 0;
    for (let j = 0; j < dim; j++) {
      const dv = flat[off + j];
      dot += q[j] * dv;
      dNorm += dv * dv;
    }
    if (dNorm < 1e-9) continue; // zero vector -> no signal
    out[i] = dot / (qMag * Math.sqrt(dNorm));
  }
  return out;
}

// Returns a Map<doc_index, {score, source, heading}> (score: 0..1, post
// floor/ceiling rescale, BEFORE the §9 weights.semantic multiplier; source:
// "doc" | "chunk"; heading: the matched section's heading text, or null for
// a doc-level hit or a paragraph-fallback chunk with no markdown heading) or
// an empty Map if the model/doc-vectors are not ready yet or query embedding
// fails for any reason. doc_index matches semantic-index.min.json's
// documents[] array position, same order build_embeddings.py used for
// semantic-vectors.bin -- see that script's own docstring for why no
// separate id map is needed.
//
// The {source, heading} fields exist so the UI can say WHICH passage matched
// (§15's hit-reason philosophy: never just an opaque "AI thinks so") instead
// of always claiming "summary similarity" even when a chunk from page 8 of a
// 15,000-character paper is what actually won -- a real gap caught during
// manual browser verification, not something planned upfront.
//
// idToIndex (Map<doc_id, doc_index>, built once by the Worker from the
// already-loaded document list) is optional -- pass it to also fold in
// Phase 5 chunk-level hits (§17.3: max chunk similarity per document),
// merged into the SAME returned Map (the higher-scoring of doc-level vs.
// chunk-level wins per doc) so scoreCorpus still only ever sees one merged
// semantic channel. Omit it (or if chunk vectors simply aren't ready/
// available yet) and this behaves exactly as Phase 3 always did -- chunk
// scoring is strictly additive, never required.
export async function semanticScores(rawQuery, idToIndex) {
  if (state.status === "idle") warmUp();
  if (state.status !== "ready") return new Map();
  if (!rawQuery || !rawQuery.trim()) return new Map();

  try {
    const [model, vectors] = await Promise.all([modelPromise, vectorsPromise]);
    if (!model || !vectors) return new Map();

    const instruction = vectors.meta.query_instruction || "";
    const output = await model(instruction + rawQuery, { pooling: "mean", normalize: true });
    const q = output.data; // Float32Array, length === vectors.dim

    const scores = new Map();
    const docCos = sweepCosine(q, vectors.flat, vectors.dim, vectors.count);
    for (let i = 0; i < docCos.length; i++) {
      const norm = normalizeRaw(docCos[i]);
      if (norm > 0) scores.set(i, { score: norm, source: "doc", heading: null });
    }

    if (idToIndex && chunkState.status === "ready" && chunkVectorsPromise) {
      const chunks = await chunkVectorsPromise;
      if (chunks) {
        const chunkCos = sweepCosine(q, chunks.flat, chunks.dim, chunks.count);
        for (let i = 0; i < chunkCos.length; i++) {
          if (chunkCos[i] < 0) continue;
          const docIndex = idToIndex.get(chunks.docIds[i]);
          if (docIndex === undefined) continue;
          const norm = normalizeRaw(chunkCos[i]);
          const existing = scores.get(docIndex);
          if (norm > 0 && (!existing || norm > existing.score)) {
            scores.set(docIndex, { score: norm, source: "chunk", heading: chunks.headings[i] || null });
          }
        }
      }
    }

    return scores;
  } catch {
    return new Map(); // never let a runtime embedding failure break the search
  }
}
