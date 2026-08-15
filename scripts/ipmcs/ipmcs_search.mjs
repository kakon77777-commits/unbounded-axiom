// IPMCS Phase IP-2 -- Runtime Integration.
//
// Generalizes IP-1's one-off experiment (hardcoded to the 6 known G_miss
// queries) into a real, reusable retriever: ipmcsSearch(query, opts) works
// for ANY query, not just the ones already used to validate the approach.
//
// Retrievers (IP-0's frozen definitions, scripts/ipmcs/ip0-definitions.json):
//   - exact/lexical: shell/public/semantic/semantic-core.js's real scoreDocument()
//   - semantic: the pinned Node q8 encoder (C1.3.1-verified) + live Vectorize
//     (returnValues:true, both namespaces) -- the SAME real, recall-gapped
//     index, not a synthetic stand-in.
//
// Query branching here defaults to just the original query -- IP-2's job is
// wiring the retriever + identity fold into reusable runtime code, not
// improving divergence (that's ai-web-research's diverge(), IP-3's job).
// Callers MAY pass their own opts.branches to layer divergence on top.
import { pipeline } from "@huggingface/transformers";
import { readFileSync } from "node:fs";
import path from "node:path";
import {
  normalizeQuery, tokenize, trigrams, prepareIndex, scoreDocument,
} from "../../shell/public/semantic/semantic-core.js";

process.loadEnvFile(new URL("../phase-c-encoder-compare/.env", import.meta.url));

const HERE = import.meta.dirname;
const REPO_ROOT = path.resolve(HERE, "..", "..");
const DOC_INDEX_PATH = path.join(REPO_ROOT, "dist/ai/semantic-index.min.json");

const MODEL_NAME = "Xenova/bge-small-zh-v1.5";
const PINNED_REVISION = "75c43b069aac4d136ba6bc1122f995fedcfd2781"; // C1.3.1-verified
const INDEX_NAME = "logic-matrix-dsrs-v1-index-v1";
const ACCOUNT_ID = process.env.CLOUDFLARE_ACCOUNT_ID;
const API_TOKEN = process.env.CLOUDFLARE_API_TOKEN;
const QUERY_INSTRUCTION = "为这个句子生成表示以用于检索相关文章："; // dsrs-v1.json embedding_space.query_prefix

let _documentsCache = null;
let _docByIdCache = null;
let _modelCache = null;

function loadDocuments() {
  if (_documentsCache) return { documents: _documentsCache, docById: _docByIdCache };
  const raw = JSON.parse(readFileSync(DOC_INDEX_PATH, "utf-8"));
  _documentsCache = prepareIndex(raw.documents);
  _docByIdCache = new Map(_documentsCache.map(d => [d.i, d]));
  return { documents: _documentsCache, docById: _docByIdCache, build_id: raw.build_id };
}

async function loadModel() {
  if (_modelCache) return _modelCache;
  _modelCache = await pipeline("feature-extraction", MODEL_NAME, { dtype: "q8", revision: PINNED_REVISION });
  return _modelCache;
}

async function vectorizeQuery(namespace, vector, topK = 30) {
  const url = `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/vectorize/v2/indexes/${INDEX_NAME}/query`;
  const res = await fetch(url, {
    method: "POST",
    headers: { Authorization: `Bearer ${API_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ vector, topK, namespace, returnValues: false, returnMetadata: "all" }),
  });
  const body = await res.json();
  if (!body.success) throw new Error(`Vectorize query failed (${namespace}): ${JSON.stringify(body.errors)}`);
  return body.result.matches;
}

/**
 * Run IPMCS over the WHOLE corpus for one query (+ optional branches).
 * Returns { objects: [{object_id, title, has_exact, max_score, paths}], per_branch }
 * ranked by (has_exact desc, max_score desc) -- a simple, explicitly
 * provisional fusion policy (see module docstring); NOT dsrs-v1.json's
 * fusion_profile, which governs the browser/MCP semantic-only channel, not
 * this cross-retriever identity layer.
 */
export async function ipmcsSearch(query, opts = {}) {
  const branches = opts.branches || [{ type: "original", text: query }];
  const topK = opts.topK ?? 10;
  const { documents, docById } = loadDocuments();
  const model = await loadModel();

  const objectHits = new Map(); // object_id -> [{view, retriever, branch_type, branch_text, score}]
  const perBranch = [];

  for (const branch of branches) {
    const branchHits = [];

    // exact + lexical, real production scorer, over the WHOLE corpus
    const qNorm = normalizeQuery(branch.text);
    const qTokens = tokenize(qNorm);
    const qTrigrams = trigrams(qNorm);
    for (const doc of documents) {
      const r = scoreDocument(doc, qNorm, qTokens, qTrigrams, undefined);
      if (r.score > 0) {
        for (const ch of r.channels) branchHits.push({ object_id: doc.i, view: "document", retriever: ch, score: r.score });
      }
    }

    // semantic, pinned encoder + live Vectorize, both namespaces
    const out = await model(QUERY_INSTRUCTION + branch.text, { pooling: "mean", normalize: true });
    const vec = Array.from(out.data);
    const [docMatches, chunkMatches] = await Promise.all([
      vectorizeQuery("document", vec, topK * 3),
      vectorizeQuery("chunk", vec, topK * 3),
    ]);
    for (const m of docMatches) branchHits.push({ object_id: m.id, view: "document", retriever: "semantic", score: m.score });
    for (const m of chunkMatches) {
      const parentId = m.metadata?.paper_id;
      if (parentId) branchHits.push({ object_id: parentId, view: "chunk-v1", retriever: "semantic", score: m.score });
    }

    for (const h of branchHits) {
      if (!objectHits.has(h.object_id)) objectHits.set(h.object_id, []);
      objectHits.get(h.object_id).push({ ...h, branch_type: branch.type, branch_text: branch.text });
    }
    perBranch.push({ branch_type: branch.type, branch_text: branch.text, hit_count: branchHits.length });
  }

  const objects = [...objectHits.entries()].map(([object_id, paths]) => {
    const doc = docById.get(object_id);
    const hasExact = paths.some(p => p.retriever === "exact");
    const maxScore = Math.max(...paths.map(p => p.score));
    return { object_id, title: doc?.t ?? null, has_exact: hasExact, max_score: maxScore, paths };
  });
  objects.sort((a, b) => (b.has_exact - a.has_exact) || (b.max_score - a.max_score));

  return { query, branches: branches.map(b => b.type), objects: objects.slice(0, topK), per_branch: perBranch };
}

// CLI smoke-test entry point: node ipmcs_search.mjs "<query>"
if (import.meta.url === `file://${process.argv[1]}`.replace(/\\/g, "/") || process.argv[1]?.endsWith("ipmcs_search.mjs")) {
  const query = process.argv[2];
  if (!query) {
    console.error("usage: node ipmcs_search.mjs \"<query>\"");
    process.exit(1);
  }
  const result = await ipmcsSearch(query);
  console.error(`query=${JSON.stringify(query)} -> ${result.objects.length} objects`);
  for (const o of result.objects) {
    console.error(`  ${o.object_id}  has_exact=${o.has_exact}  max_score=${o.max_score.toFixed(4)}  channels=${[...new Set(o.paths.map(p => p.retriever))].join(",")}`);
  }
  console.log(JSON.stringify(result, null, 2));
}
