// Phase C1: Node.js reference query encoder vs the browser-q8 oracle.
// Deliberately the SAME library (@huggingface/transformers), same model,
// same pooling/normalize, same query_instruction as the browser -- only the
// RUNTIME varies (Node vs browser WASM). Also runs fp32 as a second,
// lower-priority comparison point (the handoff calls this "if convenient").
//
// This script only computes vectors and writes local files -- it does not
// touch Vectorize. The retrieval-drift step (feeding these vectors into the
// live index) is orchestrated separately (see PHASE_C1_NOTES.md in this
// directory) so a wrangler CLI failure can't lose the (slow, model-inference)
// encoding work.
import { pipeline } from "@huggingface/transformers";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";

const HERE = import.meta.dirname;
const REPO_ROOT = path.resolve(HERE, "..", "..");
const ORACLE_PATH = path.join(REPO_ROOT, "registry/embedding-profiles/oracle/browser-q8-oracle-2026-08-15.json");
const COMPARISON_OUT = path.join(HERE, "comparison-2026-08-15.json");
const TESTVEC_NDJSON_OUT = path.join(HERE, "test-vectors-2026-08-15.ndjson");

const MODEL_NAME = "Xenova/bge-small-zh-v1.5";

function l2norm(vec) {
  let s = 0;
  for (const x of vec) s += x * x;
  return Math.sqrt(s);
}
function cosine(a, b) {
  let dot = 0, na = 0, nb = 0;
  for (let i = 0; i < a.length; i++) { dot += a[i] * b[i]; na += a[i] * a[i]; nb += b[i] * b[i]; }
  return dot / (Math.sqrt(na) * Math.sqrt(nb));
}
function maxAbsDiff(a, b) {
  let m = 0;
  for (let i = 0; i < a.length; i++) m = Math.max(m, Math.abs(a[i] - b[i]));
  return m;
}
function meanAbsDiff(a, b) {
  let s = 0;
  for (let i = 0; i < a.length; i++) s += Math.abs(a[i] - b[i]);
  return s / a.length;
}

async function main() {
  const oracle = JSON.parse(readFileSync(ORACLE_PATH, "utf-8"));
  const instruction = oracle.query_instruction;
  if (typeof instruction !== "string") throw new Error("oracle query_instruction missing");

  console.error(`node ${process.version}, loading ${MODEL_NAME} dtype=q8 ...`);
  const t0 = performance.now();
  const modelQ8 = await pipeline("feature-extraction", MODEL_NAME, { dtype: "q8" });
  console.error(`  q8 loaded in ${(performance.now() - t0).toFixed(0)}ms`);

  console.error(`loading ${MODEL_NAME} dtype=fp32 ...`);
  const t1 = performance.now();
  const modelFp32 = await pipeline("feature-extraction", MODEL_NAME, { dtype: "fp32" });
  console.error(`  fp32 loaded in ${(performance.now() - t1).toFixed(0)}ms`);

  const comparisons = [];
  const testVectorLines = [];

  for (let i = 0; i < oracle.results.length; i++) {
    const r = oracle.results[i];
    const browserVec = r.values;

    const outQ8 = await modelQ8(instruction + r.query, { pooling: "mean", normalize: true });
    const nodeQ8 = Array.from(outQ8.data);

    const outFp32 = await modelFp32(instruction + r.query, { pooling: "mean", normalize: true });
    const nodeFp32 = Array.from(outFp32.data);

    comparisons.push({
      query: r.query,
      browser_q8_norm: r.l2_norm,
      node_q8: {
        norm: l2norm(nodeQ8),
        cosine_vs_browser: cosine(browserVec, nodeQ8),
        max_abs_diff_vs_browser: maxAbsDiff(browserVec, nodeQ8),
        mean_abs_diff_vs_browser: meanAbsDiff(browserVec, nodeQ8),
      },
      node_fp32: {
        norm: l2norm(nodeFp32),
        cosine_vs_browser: cosine(browserVec, nodeFp32),
        max_abs_diff_vs_browser: maxAbsDiff(browserVec, nodeFp32),
        mean_abs_diff_vs_browser: meanAbsDiff(browserVec, nodeFp32),
      },
    });

    testVectorLines.push(JSON.stringify({ id: `test-browser-${i}`, values: browserVec, namespace: "phase-c-test", metadata: { query: r.query, source: "browser-q8" } }));
    testVectorLines.push(JSON.stringify({ id: `test-nodeq8-${i}`, values: nodeQ8, namespace: "phase-c-test", metadata: { query: r.query, source: "node-q8" } }));

    console.error(`  [${i + 1}/${oracle.results.length}] ${r.query} :: cos(q8)=${cosine(browserVec, nodeQ8).toFixed(6)} cos(fp32)=${cosine(browserVec, nodeFp32).toFixed(6)}`);
  }

  writeFileSync(COMPARISON_OUT, JSON.stringify({
    generated_at: new Date().toISOString(),
    node_version: process.version,
    model_artifact: MODEL_NAME,
    oracle_source: path.relative(REPO_ROOT, ORACLE_PATH),
    query_count: comparisons.length,
    comparisons,
  }, null, 2), "utf-8");

  writeFileSync(TESTVEC_NDJSON_OUT, testVectorLines.join("\n") + "\n", "utf-8");

  const q8Cosines = comparisons.map(c => c.node_q8.cosine_vs_browser);
  const fp32Cosines = comparisons.map(c => c.node_fp32.cosine_vs_browser);
  console.error(`\nq8   cosine: min=${Math.min(...q8Cosines).toFixed(6)} max=${Math.max(...q8Cosines).toFixed(6)}`);
  console.error(`fp32 cosine: min=${Math.min(...fp32Cosines).toFixed(6)} max=${Math.max(...fp32Cosines).toFixed(6)}`);
  console.error(`wrote ${COMPARISON_OUT}`);
  console.error(`wrote ${TESTVEC_NDJSON_OUT} (${testVectorLines.length} test vectors, namespace=phase-c-test)`);
}

main().catch(e => { console.error(e); process.exit(1); });
