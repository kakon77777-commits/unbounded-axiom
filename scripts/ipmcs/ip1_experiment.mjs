// IPMCS Phase IP-1 -- Offline Experiment.
// Question (IPMCS v0.1 section 14): without changing the Vectorize index or
// improving ANN recall itself, how many of the 12 real G_miss objects (Phase
// C2's verified Vectorize recall gap) can be rescued by adding query branches
// and non-semantic retrieval channels?
//
// Reuses REAL production code, not reimplementations:
//   - exact/lexical: shell/public/semantic/semantic-core.js's scoreDocument()
//   - semantic: the SAME pinned Node q8 encoder + live Vectorize HTTP query
//     verified in Phase C1/C2 (scripts/phase-c-encoder-compare/)
import { pipeline } from "@huggingface/transformers";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import {
  normalizeQuery, tokenize, trigrams, prepareIndex, scoreDocument,
} from "../../shell/public/semantic/semantic-core.js";

process.loadEnvFile(new URL("../phase-c-encoder-compare/.env", import.meta.url));

const HERE = import.meta.dirname;
const REPO_ROOT = path.resolve(HERE, "..", "..");
const GMISS_PATH = path.join(REPO_ROOT, "scripts/phase-c-encoder-compare/c2-recall-gap-analysis-2026-08-15.json");
const DOC_INDEX_PATH = path.join(REPO_ROOT, "dist/ai/semantic-index.min.json");
const OUT_PATH = path.join(HERE, "ip1-results-2026-08-15.json");

const MODEL_NAME = "Xenova/bge-small-zh-v1.5";
const PINNED_REVISION = "75c43b069aac4d136ba6bc1122f995fedcfd2781";
const INDEX_NAME = "logic-matrix-dsrs-v1-index-v1";
const ACCOUNT_ID = process.env.CLOUDFLARE_ACCOUNT_ID;
const API_TOKEN = process.env.CLOUDFLARE_API_TOKEN;
const QUERY_INSTRUCTION = "为这个句子生成表示以用于检索相关文章："; // dsrs-v1.json embedding_space.query_prefix

// --- Query branches, hand-authored per IPMCS section 15's MVP branch types ---
// (original is implicit -- it's the query that already produced the known miss)
const BRANCHES = {
  "動態不動點": [
    { type: "terminology_expansion", text: "dynamic fixed point" },
    { type: "semantic_paraphrase", text: "系統狀態隨時間演化但收斂至某個不變點的現象" },
  ],
  "AI 主體性": [
    { type: "terminology_expansion", text: "AI agency 人工智慧能動性" },
    { type: "semantic_paraphrase", text: "人工智慧是否具備自主意識或能動性" },
  ],
  "兩個不同來源獨立得出相同結論的現象": [
    { type: "terminology_expansion", text: "獨立收斂" },
    { type: "semantic_paraphrase", text: "不同研究路徑各自發現相似的結果" },
  ],
  "研究計畫的檢查點機制": [
    { type: "terminology_expansion", text: "Research Program checkpoint 階段性完成點" },
    { type: "semantic_paraphrase", text: "一系列論文如何標記其完成狀態" },
  ],
  "自我指涉與遞迴結構": [
    { type: "terminology_expansion", text: "自指 self-reference recursion" },
    { type: "semantic_paraphrase", text: "一個系統描述或包含自己的結構" },
  ],
  "當一個系統的每個組成部分都被逐漸替換之後，它還是原來的那個系統嗎": [
    { type: "terminology_expansion", text: "忒修斯之船" },
    { type: "terminology_expansion", text: "identity persistence under component replacement" },
    { type: "counterexample", text: "如果組成部分是一次性全部替換而非逐步替換，是否仍是同一個系統" },
  ],
};

async function vectorizeQuery(namespace, vector) {
  const url = `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/vectorize/v2/indexes/${INDEX_NAME}/query`;
  const res = await fetch(url, {
    method: "POST",
    headers: { Authorization: `Bearer ${API_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ vector, topK: 30, namespace, returnValues: false, returnMetadata: "all" }),
  });
  const body = await res.json();
  if (!body.success) throw new Error(`Vectorize query failed: ${JSON.stringify(body.errors)}`);
  return body.result.matches;
}

async function main() {
  const gmiss = JSON.parse(readFileSync(GMISS_PATH, "utf-8"));
  const docIndexRaw = JSON.parse(readFileSync(DOC_INDEX_PATH, "utf-8"));
  const documents = prepareIndex(docIndexRaw.documents.map(d => ({ ...d, id: d.i })));
  const docById = new Map(documents.map(d => [d.i, d]));

  console.error(`loaded ${documents.length} documents, doc index build_id=${docIndexRaw.build_id}`);
  console.error(`loading pinned Node q8 encoder ...`);
  const model = await pipeline("feature-extraction", MODEL_NAME, { dtype: "q8", revision: PINNED_REVISION });

  const objectResults = new Map(); // object_id -> { rescued: bool, paths: [] }
  const gmissObjects = new Set();
  for (const q of gmiss.per_query_with_gaps) for (const id of q.missing_from_server_topK30) gmissObjects.add(id);
  for (const id of gmissObjects) objectResults.set(id, { rescued: false, paths: [] });

  const perQueryLog = [];

  for (const qRow of gmiss.per_query_with_gaps) {
    const originalQuery = qRow.query;
    const targets = new Set(qRow.missing_from_server_topK30);
    const branches = [{ type: "original", text: originalQuery }, ...(BRANCHES[originalQuery] || [])];

    const branchLog = [];
    for (const branch of branches) {
      const hits = []; // {object_id, view, retriever}

      // --- exact + lexical, via the REAL production scorer ---
      const qNorm = normalizeQuery(branch.text);
      const qTokens = tokenize(qNorm);
      const qTrigrams = trigrams(qNorm);
      for (const targetId of targets) {
        const doc = docById.get(targetId);
        if (!doc) continue;
        const r = scoreDocument(doc, qNorm, qTokens, qTrigrams, undefined);
        if (r.score > 0) {
          for (const ch of r.channels) hits.push({ object_id: targetId, view: "document", retriever: ch, score: r.score });
        }
      }

      // --- semantic, via pinned encoder + LIVE Vectorize (the real, recall-gapped index) ---
      const out = await model(QUERY_INSTRUCTION + branch.text, { pooling: "mean", normalize: true });
      const vec = Array.from(out.data);
      const [docMatches, chunkMatches] = await Promise.all([
        vectorizeQuery("document", vec),
        vectorizeQuery("chunk", vec),
      ]);
      for (const m of docMatches) {
        if (targets.has(m.id)) hits.push({ object_id: m.id, view: "document", retriever: "semantic", score: m.score });
      }
      for (const m of chunkMatches) {
        const parentId = m.metadata?.paper_id;
        if (parentId && targets.has(parentId)) hits.push({ object_id: parentId, view: "chunk-v1", retriever: "semantic", score: m.score });
      }

      // --- identity fold: record every hit against its canonical object ---
      for (const h of hits) {
        const rec = objectResults.get(h.object_id);
        rec.rescued = true;
        rec.paths.push({ query: originalQuery, branch_type: branch.type, branch_text: branch.text, view: h.view, retriever: h.retriever, score: h.score });
      }

      branchLog.push({ branch_type: branch.type, branch_text: branch.text, hit_count: hits.length, hits });
      console.error(`  [${originalQuery.slice(0, 12)}...] branch="${branch.type}" hits=${hits.length}`);
    }
    perQueryLog.push({ query: originalQuery, targets: [...targets], branches: branchLog });
  }

  const rescued = [...objectResults.entries()].filter(([, v]) => v.rescued);
  const rescueRate = rescued.length / gmissObjects.size;

  const report = {
    generated_at: new Date().toISOString(),
    purpose: "IPMCS Phase IP-1 offline experiment result",
    G_miss_count: gmissObjects.size,
    rescued_count: rescued.length,
    rescue_rate: rescueRate,
    per_object: Object.fromEntries([...objectResults.entries()].map(([id, v]) => [id, v])),
    per_query: perQueryLog,
  };
  writeFileSync(OUT_PATH, JSON.stringify(report, null, 2), "utf-8");
  console.error(`\nRescue Rate: ${rescued.length}/${gmissObjects.size} = ${(rescueRate * 100).toFixed(1)}%`);
  console.error(`wrote ${OUT_PATH}`);
}

main().catch(e => { console.error(e); process.exit(1); });
