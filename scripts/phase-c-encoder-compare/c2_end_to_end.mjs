// Phase C2: First End-to-End Server DSRS Semantic Runtime.
//
//   text query -> pinned Node q8 encoder -> Vectorize HTTP query
//   (returnValues:true, both namespaces) -> score_calibration (0.50/0.62)
//   -> sub-floor filter -> chunk->document max fold -> compare against
//   the browser-equivalent result.
//
// Deliberately semantic-channel only (per the Phase C handoff: no lexical,
// dictionary, relations, RRF, or MCP in this pass). Queries Vectorize
// directly over HTTP with the query vector in the request body -- no
// upsert/delete workaround needed (that was only ever required to get a
// 512-float vector into the `wrangler` CLI without hitting the Windows
// command-line length limit; a real HTTP POST body has no such limit).
//
// The "browser-equivalent" comparison target is NOT re-fetched from a live
// browser -- it's reconstructed by applying this SAME calibration+fold
// formula to the exact local cosine scores C1.2 already computed for the
// real browser-q8 oracle vectors (registry/generated/*.f32.bin sweep,
// zero ANN). That is a faithful reproduction of what shell/public/semantic/
// semantic-vector.js's semanticScores() would return for the same query,
// without needing to relaunch a browser to prove it again.
import { pipeline } from "@huggingface/transformers";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";

process.loadEnvFile(new URL("./.env", import.meta.url));

const HERE = import.meta.dirname;
const REPO_ROOT = path.resolve(HERE, "..", "..");
const ORACLE_PATH = path.join(REPO_ROOT, "registry/embedding-profiles/oracle/browser-q8-oracle-2026-08-15.json");
const C1_2_PATH = path.join(HERE, "c1_2-exact-drift-2026-08-15.json");
const OUT_PATH = path.join(HERE, "c2-end-to-end-2026-08-15.json");

const MODEL_NAME = "Xenova/bge-small-zh-v1.5";
const PINNED_REVISION = "75c43b069aac4d136ba6bc1122f995fedcfd2781"; // C1.3.1-verified
const INDEX_NAME = "logic-matrix-dsrs-v1-index-v1";
const ACCOUNT_ID = process.env.CLOUDFLARE_ACCOUNT_ID;
const API_TOKEN = process.env.CLOUDFLARE_API_TOKEN;
if (!ACCOUNT_ID || !API_TOKEN) throw new Error("CLOUDFLARE_ACCOUNT_ID / CLOUDFLARE_API_TOKEN missing from .env");

const RAW_FLOOR = 0.50;
const RAW_CEILING = 0.62;
const TOP_K = 30; // well under the 50-cap that applies when returnValues:true

function calibrate(raw) {
  if (raw <= RAW_FLOOR) return 0;
  if (raw >= RAW_CEILING) return 1;
  return (raw - RAW_FLOOR) / (RAW_CEILING - RAW_FLOOR);
}

async function vectorizeQuery(namespace, vector) {
  const url = `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/vectorize/v2/indexes/${INDEX_NAME}/query`;
  const res = await fetch(url, {
    method: "POST",
    headers: { Authorization: `Bearer ${API_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ vector, topK: TOP_K, namespace, returnValues: true, returnMetadata: "all" }),
  });
  const body = await res.json();
  if (!body.success) throw new Error(`Vectorize query failed (${namespace}): ${JSON.stringify(body.errors)}`);
  return body.result.matches; // [{id, score, values, namespace, metadata}] -- returnValues:true is what actually
  // triggers Cloudflare's documented high-precision scoring path (not returnMetadata alone); `values` is discarded,
  // only requested because it's the documented mechanism, per dsrs-v1.json score_calibration.domain_requirement.
}

// Fold chunk-namespace hits onto their parent document, per index_profile.doc_chunk_aggregation:
// max(doc-level calibrated score, best chunk-level calibrated score) per document.
function calibrateAndFold(docMatches, chunkMatches) {
  const scores = new Map(); // doc_id -> {score, source}
  for (const m of docMatches) {
    const c = calibrate(m.score);
    if (c > 0) scores.set(m.id, { score: c, source: "doc" });
  }
  for (const m of chunkMatches) {
    const c = calibrate(m.score);
    if (c <= 0) continue;
    const docId = m.metadata?.paper_id;
    if (!docId) continue;
    const existing = scores.get(docId);
    if (!existing || c > existing.score) scores.set(docId, { score: c, source: "chunk" });
  }
  return [...scores.entries()]
    .map(([doc_id, v]) => ({ doc_id, ...v }))
    .sort((a, b) => b.score - a.score);
}

// Reconstruct the browser-equivalent result from C1.2's already-captured EXACT
// cosine scores (zero ANN, zero Vectorize) -- same calibration+fold formula,
// applied to ground truth the browser's own encoder actually produced.
function browserEquivalentFromC1_2(row) {
  const docMatches = row.document.browser_top10.map(([id, score]) => ({ id, score }));
  const chunkMatches = row.chunk.browser_top10.map(([id, score]) => {
    const docId = id.split("#")[0];
    return { id, score, metadata: { paper_id: docId } };
  });
  return calibrateAndFold(docMatches, chunkMatches);
}

function rankCorrelation(aIds, bIds) {
  const common = aIds.filter(i => bIds.includes(i));
  if (common.length < 2) return null;
  const aRanks = new Map(aIds.map((v, i) => [v, i]));
  const bRanks = new Map(bIds.map((v, i) => [v, i]));
  const n = common.length;
  const d2 = common.reduce((s, c) => s + (aRanks.get(c) - bRanks.get(c)) ** 2, 0);
  return 1 - (6 * d2) / (n * (n * n - 1));
}

async function main() {
  const oracle = JSON.parse(readFileSync(ORACLE_PATH, "utf-8"));
  const c1_2 = JSON.parse(readFileSync(C1_2_PATH, "utf-8"));
  const instruction = oracle.query_instruction;

  console.error(`loading Node q8, revision=${PINNED_REVISION} ...`);
  const model = await pipeline("feature-extraction", MODEL_NAME, { dtype: "q8", revision: PINNED_REVISION });

  const rows = [];
  for (let i = 0; i < oracle.results.length; i++) {
    const query = oracle.results[i].query;
    const c1_2Row = c1_2.per_query.find(r => r.query === query);

    const out = await model(instruction + query, { pooling: "mean", normalize: true });
    const vec = Array.from(out.data);

    const [docMatches, chunkMatches] = await Promise.all([
      vectorizeQuery("document", vec),
      vectorizeQuery("chunk", vec),
    ]);

    const serverResult = calibrateAndFold(docMatches, chunkMatches);
    const browserResult = browserEquivalentFromC1_2(c1_2Row);

    const serverIds = serverResult.map(r => r.doc_id);
    const browserIds = browserResult.map(r => r.doc_id);
    const overlapAt10 = serverIds.slice(0, 10).filter(id => browserIds.slice(0, 10).includes(id)).length;
    const top1Match = serverIds[0] === browserIds[0];

    rows.push({
      query,
      server_result_full: serverResult,
      browser_equivalent_result_full: browserResult,
      server_candidate_count: serverResult.length,
      browser_equivalent_candidate_count: browserResult.length,
      top1_match: top1Match,
      overlap_at_10: overlapAt10,
      rank_correlation: rankCorrelation(serverIds, browserIds),
    });
    console.error(`[${i + 1}/${oracle.results.length}] top1_match=${top1Match} overlap@10=${overlapAt10} server_n=${serverResult.length} browser_n=${browserResult.length}`);
  }

  const top1Matches = rows.filter(r => r.top1_match).length;
  const bothEmpty = rows.filter(r => r.server_candidate_count === 0 && r.browser_equivalent_candidate_count === 0).length;

  const report = {
    generated_at: new Date().toISOString(),
    purpose: "Phase C2: first true end-to-end server-side DSRS semantic path (text -> Node encoder -> live Vectorize -> calibration -> fold), compared against the browser-equivalent reconstruction from C1.2's exact ground truth. Semantic channel only, no lexical/dictionary/relations/RRF/MCP.",
    model_revision: PINNED_REVISION,
    index: INDEX_NAME,
    query_method: "direct Cloudflare Vectorize HTTP API (POST .../query, vector in request body) -- no CLI, no upsert/delete",
    calibration: { raw_floor: RAW_FLOOR, raw_ceiling: RAW_CEILING },
    query_count: rows.length,
    summary: {
      top1_match_rate: `${top1Matches}/${rows.length}`,
      both_empty_after_subfloor_count: bothEmpty,
    },
    per_query: rows,
  };
  writeFileSync(OUT_PATH, JSON.stringify(report, null, 2), "utf-8");
  console.error(`\ntop1 match rate: ${top1Matches}/${rows.length}`);
  console.error(`wrote ${OUT_PATH}`);
}

main().catch(e => { console.error(e); process.exit(1); });
