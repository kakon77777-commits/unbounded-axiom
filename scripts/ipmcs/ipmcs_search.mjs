// IPMCS Phase IP-2 -- Runtime Integration -- + IP-3 -- External Expansion --
// + IP-4 -- ANLA-native Addressing.
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
// Query branching defaults to just the original query. Pass opts.diverge:true
// to layer IP-3's real LLM-based divergence on top (divergeBranches() below,
// a thin subprocess call into ai-web-research's actual diverge() -- 5 DRC
// categories, real Vertex AI calls, not reimplemented or simulated). Callers
// may instead pass their own opts.branches directly (as IP-1 did by hand).
//
// Pass opts.expandAddress:true to attach IP-4's ANLA-verified provenance to
// each result (expandAddresses() below -- another thin subprocess call, this
// time into anla_address/resolve_address.py, which re-extracts the object
// from a real anla1-packed archive of content/papers/ and reports
// digest_verified only when that full BLAKE3 hash chain actually re-ran and
// matched, never a fabricated true).
import { pipeline } from "@huggingface/transformers";
import { readFileSync } from "node:fs";
import path from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import {
  normalizeQuery, tokenize, trigrams, prepareIndex, scoreDocument,
} from "../../shell/public/semantic/semantic-core.js";

const execFileAsync = promisify(execFile);

// IPMCS Phase IP-3: real LLM-based query divergence, via a thin CLI wrapper
// around ai-web-research's actual diverge() (D:\Ai\work together\ai-web-research
// -- a separate Python repo, real crawler.research.diverge(), 5 DRC categories:
// semantic/task/source/language/perspective). Each call is a real LLM request
// (Vertex, per that repo's .env) with a real, small cost -- not simulated.
const AI_WEB_RESEARCH_DIR = "D:\\Ai\\work together\\ai-web-research";
const AI_WEB_RESEARCH_PYTHON = path.join(AI_WEB_RESEARCH_DIR, ".venv", "Scripts", "python.exe");
const DIVERGE_CLI = path.join(AI_WEB_RESEARCH_DIR, "diverge_cli.py");

/** Calls the REAL diverge() (subprocess, not reimplemented). Returns
 * [{type: "original", text: query}, {type: "semantic", text: ...}, ...] --
 * flattens diverge()'s 5 categories into IPMCS branches, original first,
 * capped at maxBranches beyond the original to bound LLM-call fan-out cost
 * on the downstream retrievers (each branch triggers its own Vectorize query). */
export async function divergeBranches(query, { maxBranches = 6 } = {}) {
  const branches = [{ type: "original", text: query }];
  try {
    const { stdout } = await execFileAsync(AI_WEB_RESEARCH_PYTHON, [DIVERGE_CLI, query], {
      cwd: AI_WEB_RESEARCH_DIR, timeout: 30000, encoding: "utf-8",
      env: { ...process.env, PYTHONIOENCODING: "utf-8" },
    });
    const result = JSON.parse(stdout.trim().split("\n").pop());
    const seen = new Set([query]);
    outer: for (const [category, queries] of Object.entries(result.branches || {})) {
      for (const text of queries) {
        if (seen.has(text)) continue;
        seen.add(text);
        branches.push({ type: category, text });
        if (branches.length - 1 >= maxBranches) break outer;
      }
    }
  } catch (e) {
    console.error(`divergeBranches: diverge() call failed, falling back to original-only: ${e.message}`);
  }
  return branches;
}

// IPMCS Phase IP-4: ANLA-native addressing. logic-matrix-corpus.anla (built by
// anla_address/build_archive.py, gitignored/regenerable, ~88MB) is a real
// anla1 archive of content/papers/ -- BLAKE3 content-addressed, chunk- and
// file-level hash verified on every extract. ANLA_PYTHON is a plain system
// interpreter (not a project venv): resolve_address.py manages its own
// sys.path into ANLA's checkout, no package install required.
const ANLA_PYTHON = "C:\\Users\\kakon\\AppData\\Local\\Python\\bin\\python.exe";
const ANLA_ADDRESS_DIR = path.join(import.meta.dirname, "anla_address");
const RESOLVE_ADDRESS_CLI = path.join(ANLA_ADDRESS_DIR, "resolve_address.py");

/** Calls the REAL resolve_address.py (subprocess). Returns a Map from
 * object_id (== IPMCS's paper_id) to {digest_verified, object_id, content_hash,
 * size, path, reason?} -- reason is only present when digest_verified is
 * false. Returns an empty Map (not fabricated per-object entries) if the
 * subprocess call itself fails, so callers degrade to "no provenance
 * attached" rather than silently claiming false verification. */
export async function expandAddresses(paperIds) {
  if (paperIds.length === 0) return new Map();
  try {
    const { stdout } = await execFileAsync(ANLA_PYTHON, [RESOLVE_ADDRESS_CLI, ...paperIds], {
      cwd: ANLA_ADDRESS_DIR, timeout: 30000, encoding: "utf-8",
      env: { ...process.env, PYTHONIOENCODING: "utf-8" },
    });
    const result = JSON.parse(stdout.trim().split("\n").pop());
    return new Map(Object.entries(result));
  } catch (e) {
    console.error(`expandAddresses: resolve_address.py call failed, no provenance attached: ${e.message}`);
    return new Map();
  }
}

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

/** Real document metadata lookup (title + section headings), no search
 * involved -- IP-5's get_object tool. Returns null for an unknown id rather
 * than a fabricated placeholder. */
export function getObject(paperId) {
  const { docById } = loadDocuments();
  const doc = docById.get(paperId);
  if (!doc) return null;
  return { object_id: paperId, title: doc.t ?? null, headings: doc.h ?? [] };
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
  const branches = opts.branches || (opts.diverge ? await divergeBranches(query, opts.divergeOpts) : [{ type: "original", text: query }]);
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

    // opts.views restricts BEFORE accumulation, not after topK slicing --
    // ranking (has_exact/max_score) and the final slice must be computed
    // from the restricted set, or an object relevant only through an
    // excluded view gets truncated away before a post-hoc filter ever sees
    // it (exactly the bug IP-5's search_views tool hit on its first real run).
    const scopedHits = opts.views ? branchHits.filter(h => opts.views.includes(h.view)) : branchHits;
    for (const h of scopedHits) {
      if (!objectHits.has(h.object_id)) objectHits.set(h.object_id, []);
      objectHits.get(h.object_id).push({ ...h, branch_type: branch.type, branch_text: branch.text });
    }
    perBranch.push({ branch_type: branch.type, branch_text: branch.text, hit_count: scopedHits.length });
  }

  const objects = [...objectHits.entries()].map(([object_id, paths]) => {
    const doc = docById.get(object_id);
    const hasExact = paths.some(p => p.retriever === "exact");
    const maxScore = Math.max(...paths.map(p => p.score));
    return { object_id, title: doc?.t ?? null, has_exact: hasExact, max_score: maxScore, paths };
  });
  objects.sort((a, b) => (b.has_exact - a.has_exact) || (b.max_score - a.max_score));
  const topObjects = objects.slice(0, topK);

  // IP-4: resolve provenance only for the results actually being returned,
  // not the whole (possibly large) hit set -- one subprocess call per query
  // regardless of topK, matching IP-3's divergeBranches fan-out discipline.
  if (opts.expandAddress) {
    const provenance = await expandAddresses(topObjects.map(o => o.object_id));
    for (const o of topObjects) o.provenance = provenance.get(o.object_id) ?? null;
  }

  return { query, branches: branches.map(b => b.type), objects: topObjects, per_branch: perBranch };
}

// CLI smoke-test entry point: node ipmcs_search.mjs "<query>"
if (import.meta.url === `file://${process.argv[1]}`.replace(/\\/g, "/") || process.argv[1]?.endsWith("ipmcs_search.mjs")) {
  const query = process.argv[2];
  const useDiverge = process.argv.includes("--diverge");
  const useAddress = process.argv.includes("--address");
  if (!query) {
    console.error("usage: node ipmcs_search.mjs \"<query>\" [--diverge] [--address]");
    process.exit(1);
  }
  const result = await ipmcsSearch(query, { diverge: useDiverge, expandAddress: useAddress });
  console.error(`query=${JSON.stringify(query)} -> ${result.objects.length} objects`);
  for (const o of result.objects) {
    const prov = o.provenance ? `  digest_verified=${o.provenance.digest_verified}` : "";
    console.error(`  ${o.object_id}  has_exact=${o.has_exact}  max_score=${o.max_score.toFixed(4)}  channels=${[...new Set(o.paths.map(p => p.retriever))].join(",")}${prov}`);
  }
  console.log(JSON.stringify(result, null, 2));
}
