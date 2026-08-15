// Phase C1.3.1: close the exact gap the 9th review round identified --
// c1_3_revision_pin.mjs only compared (browser oracle) vs (pinned node),
// and matching aggregate cosine-range statistics against a THIRD reference
// is not the same as directly proving (unpinned node) == (pinned node).
// This script computes both directly, from the SAME process, and compares
// via SHA-256 (byte-identical check, same method as the original oracle
// collision discovery) -- not just cosine similarity.
import { pipeline } from "@huggingface/transformers";
import { readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import path from "node:path";

const HERE = import.meta.dirname;
const REPO_ROOT = path.resolve(HERE, "..", "..");
const ORACLE_PATH = path.join(REPO_ROOT, "registry/embedding-profiles/oracle/browser-q8-oracle-2026-08-15.json");
const OUT_PATH = path.join(HERE, "c1_3_1-pin-equivalence-2026-08-15.json");

const MODEL_NAME = "Xenova/bge-small-zh-v1.5";
const PINNED_REVISION = "75c43b069aac4d136ba6bc1122f995fedcfd2781";

function sha256OfFloat32(vec) {
  const buf = Buffer.from(new Float32Array(vec).buffer);
  return createHash("sha256").update(buf).digest("hex");
}

async function main() {
  const oracle = JSON.parse(readFileSync(ORACLE_PATH, "utf-8"));
  const instruction = oracle.query_instruction;

  console.error("loading UNPINNED (main) node q8 ...");
  const modelMain = await pipeline("feature-extraction", MODEL_NAME, { dtype: "q8" });
  console.error("loading PINNED (75c43b0...) node q8 ...");
  const modelPinned = await pipeline("feature-extraction", MODEL_NAME, { dtype: "q8", revision: PINNED_REVISION });

  const rows = [];
  let mismatches = 0;
  for (const r of oracle.results) {
    const outMain = await modelMain(instruction + r.query, { pooling: "mean", normalize: true });
    const outPinned = await modelPinned(instruction + r.query, { pooling: "mean", normalize: true });
    const vecMain = Array.from(outMain.data);
    const vecPinned = Array.from(outPinned.data);
    const shaMain = sha256OfFloat32(vecMain);
    const shaPinned = sha256OfFloat32(vecPinned);
    const identical = shaMain === shaPinned;
    if (!identical) mismatches++;
    rows.push({ query: r.query, sha256_main: shaMain, sha256_pinned: shaPinned, byte_identical: identical });
    console.error(`  ${r.query}: byte_identical=${identical}`);
  }

  writeFileSync(OUT_PATH, JSON.stringify({
    generated_at: new Date().toISOString(),
    purpose: "Phase C1.3.1: direct (unpinned main) vs (pinned 75c43b0...) node-q8 comparison, SHA-256 byte-identity, not just aggregate cosine-range matching against a third reference.",
    pinned_revision: PINNED_REVISION,
    query_count: rows.length,
    mismatches,
    all_byte_identical: mismatches === 0,
    rows,
  }, null, 2), "utf-8");

  console.error(`\n${rows.length - mismatches}/${rows.length} byte-identical. wrote ${OUT_PATH}`);
}

main().catch(e => { console.error(e); process.exit(1); });
