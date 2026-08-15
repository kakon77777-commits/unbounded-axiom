// Phase C1.1: Tokenizer Collision Audit.
// The Phase C0 oracle contains a real, confirmed (SHA-256 byte-identical)
// vector collision: DSRS / AICL / CASP / SSSP / MCP / "∀x∃y" all produce the
// EXACT SAME 512-dim browser-q8 output. This script tokenizes the raw
// queries (with the same query_instruction prefix production uses) and
// prints input_ids/tokens/attention_mask to find the actual mechanism,
// rather than stop at "probably an [UNK] collapse."
import { AutoTokenizer } from "@huggingface/transformers";
import { readFileSync } from "node:fs";
import path from "node:path";

const HERE = import.meta.dirname;
const REPO_ROOT = path.resolve(HERE, "..", "..");
const ORACLE_PATH = path.join(REPO_ROOT, "registry/embedding-profiles/oracle/browser-q8-oracle-2026-08-15.json");
const MODEL_NAME = "Xenova/bge-small-zh-v1.5";

const COLLISION_HASH = "d88bf7654443db0ffcfaa00cafd9e7e968cd367d3543f79f97451655cfae3efe";

async function main() {
  const oracle = JSON.parse(readFileSync(ORACLE_PATH, "utf-8"));
  const instruction = oracle.query_instruction;
  const collided = oracle.results.filter(r => r.sha256 === COLLISION_HASH).map(r => r.query);
  const others = oracle.results.filter(r => r.sha256 !== COLLISION_HASH).map(r => r.query).slice(0, 3);

  console.error(`confirmed collided queries (${collided.length}): ${JSON.stringify(collided)}`);

  const tokenizer = await AutoTokenizer.from_pretrained(MODEL_NAME);

  const report = [];
  for (const q of [...collided, ...others]) {
    const full = instruction + q;
    const encoded = tokenizer(full, { padding: true, truncation: true });
    const ids = Array.from(encoded.input_ids.data, x => Number(x));
    const tokens = tokenizer.tokenize(full);
    const attn = Array.from(encoded.attention_mask.data, x => Number(x));
    report.push({ query: q, is_collided: collided.includes(q), input_ids: ids, tokens, attention_mask: attn });
    console.error(`\nquery=${JSON.stringify(q)} collided=${collided.includes(q)}`);
    console.error(`  input_ids: ${JSON.stringify(ids)}`);
    console.error(`  tokens:    ${JSON.stringify(tokens)}`);
  }

  // pairwise check: do ALL collided queries share the identical input_ids sequence?
  const collidedRows = report.filter(r => r.is_collided);
  const idSeqs = collidedRows.map(r => JSON.stringify(r.input_ids));
  const allSameIds = idSeqs.every(s => s === idSeqs[0]);
  console.error(`\nAll ${collidedRows.length} collided queries produce IDENTICAL input_ids sequence: ${allSameIds}`);

  const { writeFileSync } = await import("node:fs");
  writeFileSync(path.join(HERE, "c1_1-tokenizer-audit-2026-08-15.json"), JSON.stringify({
    generated_at_note: "Phase C1.1, 2026-08-15",
    collision_sha256: COLLISION_HASH,
    collided_queries: collided,
    all_collided_share_identical_input_ids: allSameIds,
    rows: report,
  }, null, 2), "utf-8");
  console.error(`\nwrote c1_1-tokenizer-audit-2026-08-15.json`);
}

main().catch(e => { console.error(e); process.exit(1); });
