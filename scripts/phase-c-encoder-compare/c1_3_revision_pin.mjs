// Phase C1.3: Revision Pin Verification.
// Reruns the 30 oracle queries with an EXPLICIT pinned revision
// (the commit HF API reported as `main` on 2026-08-15, independently
// confirmed twice this session) instead of letting pipeline() float on
// `main`. If the drift envelope matches the unpinned node-q8 run, that's
// direct evidence the pin doesn't change anything TODAY -- upgrading
// model_revision from "inferred" to "reproduction-verified" for THIS
// commit, not proof it will always match main going forward.
import { pipeline } from "@huggingface/transformers";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";

const HERE = import.meta.dirname;
const REPO_ROOT = path.resolve(HERE, "..", "..");
const ORACLE_PATH = path.join(REPO_ROOT, "registry/embedding-profiles/oracle/browser-q8-oracle-2026-08-15.json");
const OUT_PATH = path.join(HERE, "c1_3-revision-pin-2026-08-15.json");

const MODEL_NAME = "Xenova/bge-small-zh-v1.5";
const PINNED_REVISION = "75c43b069aac4d136ba6bc1122f995fedcfd2781";

function cosine(a, b) {
  let dot = 0, na = 0, nb = 0;
  for (let i = 0; i < a.length; i++) { dot += a[i] * b[i]; na += a[i] * a[i]; nb += b[i] * b[i]; }
  return dot / (Math.sqrt(na) * Math.sqrt(nb));
}

async function main() {
  const oracle = JSON.parse(readFileSync(ORACLE_PATH, "utf-8"));
  const instruction = oracle.query_instruction;

  console.error(`loading ${MODEL_NAME} dtype=q8 revision=${PINNED_REVISION} ...`);
  const model = await pipeline("feature-extraction", MODEL_NAME, { dtype: "q8", revision: PINNED_REVISION });
  console.error("loaded.");

  const rows = [];
  for (const r of oracle.results) {
    const out = await model(instruction + r.query, { pooling: "mean", normalize: true });
    const pinnedVec = Array.from(out.data);
    const cos = cosine(r.values, pinnedVec);
    rows.push({ query: r.query, cos_browser_vs_pinned_node_q8: cos });
    console.error(`  ${r.query}: cos=${cos.toFixed(6)}`);
  }

  const cosines = rows.map(r => r.cos_browser_vs_pinned_node_q8);
  const summary = { min: Math.min(...cosines), max: Math.max(...cosines) };
  console.error(`\npinned-revision cosine range: [${summary.min.toFixed(6)}, ${summary.max.toFixed(6)}]`);

  writeFileSync(OUT_PATH, JSON.stringify({
    generated_at: new Date().toISOString(),
    pinned_revision: PINNED_REVISION,
    model_artifact: MODEL_NAME,
    dtype: "q8",
    summary,
    rows,
  }, null, 2), "utf-8");
  console.error(`wrote ${OUT_PATH}`);
}

main().catch(e => { console.error(e); process.exit(1); });
