// Logic Matrix / IPMCS -- remote MCP surface, served at /mcp on the SAME Worker
// as the rest of the site (src/worker.js dispatches here).
//
// This is a DELIBERATELY SMALLER tool surface than the local stdio server
// (scripts/ipmcs/mcp_server.mjs, IP-5): exact+lexical search + ANLA address
// lookup only, no semantic/embedding channel and no LLM-based query
// divergence. Two independent reasons, not one:
//
//   1. The pinned encoder (Xenova/bge-small-zh-v1.5, whose score_calibration
//      floor/ceiling this whole DSRS stack was fit against) cannot run in a
//      Workers V8 isolate -- researched, not assumed: onnxruntime-web's own
//      WASM binary already exceeds Cloudflare's 25MB per-asset cap before any
//      model weights load (huggingface/transformers.js#1521), and Workers AI
//      has no bge-small-zh-v1.5 equivalent (switching encoders would
//      invalidate the calibration and require re-measuring it, not something
//      to do silently). Confirmed with Neo 2026-08-16: ship exact+lexical+
//      ANLA addressing now, semantic search stays local-only until there's a
//      real remote-compute answer (e.g. Cloudflare Containers running the
//      unchanged encoder).
//   2. expand_query (LLM-based divergence) has a real per-call API cost and
//      this endpoint is meant to be added with NO AUTH in ChatGPT/Claude.ai
//      connector dialogs -- an open, unmetered LLM-costing tool on a public
//      no-auth surface is a real exposure Neo hasn't been asked about yet,
//      independent of the encoder question. Left out of v1 for that reason,
//      not forgotten.
//
// search_views is also dropped here (not merely unmentioned): its only real
// value is the chunk-v1 view, which -- see semantic-core.js's own comment --
// only ever has semantic-channel coverage. Without semantic it would be a
// tool that always returns empty, which is worse than not exposing it.
//
// expand_address here reports what the LAST anla_address/build_archive.py run
// verified, not a live re-check (no Python/anla1 runtime, no 88MB archive
// fetch+parse per request in a Worker). Labeled distinctly from the local
// server's live-verified `digest_verified` field precisely so a caller can't
// mistake "this was true as of the last local build" for "I just checked."
import { createMcpHandler, McpServer } from "@modelcontextprotocol/server";
import * as z from "zod";
import {
  normalizeQuery, tokenize, trigrams, prepareIndex, scoreDocument,
} from "../shell/public/semantic/semantic-core.js";

let _documentsCache = null;
let _docByIdCache = null;
let _addressesCache = null;

async function loadDocuments(request, env) {
  if (_documentsCache) return { documents: _documentsCache, docById: _docByIdCache };
  const res = await env.ASSETS.fetch(new Request(new URL("/ai/semantic-index.min.json", request.url)));
  const raw = await res.json();
  _documentsCache = prepareIndex(raw.documents);
  _docByIdCache = new Map(_documentsCache.map(d => [d.i, d]));
  return { documents: _documentsCache, docById: _docByIdCache };
}

async function loadAddresses(request, env) {
  if (_addressesCache) return _addressesCache;
  try {
    const res = await env.ASSETS.fetch(new Request(new URL("/ai/anla-addresses.json", request.url)));
    _addressesCache = res.ok ? await res.json() : { addresses: {} };
  } catch (e) {
    _addressesCache = { addresses: {} };
  }
  return _addressesCache;
}

function textResult(value) {
  return { content: [{ type: "text", text: JSON.stringify(value, null, 2) }] };
}

/** Real exact+lexical search over the whole corpus -- the SAME scoreDocument()
 * used by the local IP-5 server and the site's own client-side search, not a
 * separate reimplementation. */
async function searchIdentity(request, env, query, topK) {
  const { documents, docById } = await loadDocuments(request, env);
  const addresses = (await loadAddresses(request, env)).addresses || {};

  const qNorm = normalizeQuery(query);
  const qTokens = tokenize(qNorm);
  const qTrigrams = trigrams(qNorm);

  const hitsByObject = new Map();
  for (const doc of documents) {
    const r = scoreDocument(doc, qNorm, qTokens, qTrigrams, undefined);
    if (r.score > 0) hitsByObject.set(doc.i, { doc, score: r.score, channels: r.channels });
  }

  const objects = [...hitsByObject.values()]
    .sort((a, b) => (b.channels.includes("exact") - a.channels.includes("exact")) || (b.score - a.score))
    .slice(0, topK)
    .map(({ doc, score, channels }) => {
      const addr = addresses[doc.i];
      return {
        object_id: doc.i,
        title: doc.t ?? null,
        has_exact: channels.includes("exact"),
        max_score: score,
        channels,
        anla_address: addr ? {
          object_id: addr.object_id, content_hash: addr.content_hash,
          digest_verified_at_build: true, hash_algorithm: "blake3-256",
        } : null,
      };
    });

  return { query, objects };
}

// createMcpHandler's factory receives ONLY {era, authInfo?, requestInfo?: Request}
// -- no env/bindings field exists anywhere in this library (verified by reading
// the actual .d.mts, not assumed: McpRequestContext has exactly those three
// keys). Cloudflare bindings aren't a concept this library knows about, so env
// is threaded through by closure instead: this factory function takes env as
// its own parameter, and worker.js builds a fresh handler per request (inside
// the /mcp route) rather than one reused across requests -- consistent with
// createMcpHandler's own "fresh instance serves every request" design, just
// one level further out. The module-scope caches below still work as real
// module-scope state across that repeated construction within a warm isolate.
export function createIpmcsRemoteHandler(env) {
  return createMcpHandler((context) => {
    const server = new McpServer({ name: "logic-matrix-ipmcs-remote", version: "0.1.0" });
    const request = context.requestInfo;

    server.registerTool(
      "search_identity",
      {
        description: "IPMCS search over the full Logic Matrix corpus (2600+ papers): exact "
          + "title/heading matches and lexical (trigram) similarity, ranked exact-first then "
          + "by score. This remote endpoint does NOT run the semantic/embedding channel or "
          + "LLM-based query divergence (both local-server-only, see search_identity's fuller "
          + "sibling tool on the local IPMCS MCP server) -- exact/lexical alone still finds "
          + "verbatim terminology, titles, and headings reliably.",
        inputSchema: {
          query: z.string().describe("search query, any language"),
          topK: z.number().int().min(1).max(50).optional().describe("max objects to return, default 10"),
        },
      },
      async ({ query, topK }) => textResult(await searchIdentity(request, env, query, topK ?? 10)),
    );

    server.registerTool(
      "get_object",
      {
        description: "Look up a Logic Matrix paper's own metadata (title, section headings) "
          + "by paper_id, with no search involved.",
        inputSchema: { paper_id: z.string() },
      },
      async ({ paper_id }) => {
        const { docById } = await loadDocuments(request, env);
        const doc = docById.get(paper_id);
        return textResult(doc
          ? { object_id: paper_id, title: doc.t ?? null, headings: doc.h ?? [] }
          : { object_id: paper_id, found: false });
      },
    );

    server.registerTool(
      "expand_address",
      {
        description: "Resolve a Logic Matrix paper_id to its ANLA canonical address (BLAKE3 "
          + "object_id + content_hash from a real anla1-packed archive of the corpus). "
          + "digest_verified_at_build is true only for objects whose full chunk+file hash "
          + "chain was checked during the archive's last build -- this is a build-time fact, "
          + "NOT a live per-request re-verification (the local IPMCS MCP server's "
          + "expand_address does that; this remote endpoint has no Python/anla1 runtime and "
          + "doesn't fetch+parse the ~90MB archive per call).",
        inputSchema: { paper_id: z.string() },
      },
      async ({ paper_id }) => {
        const addresses = (await loadAddresses(request, env)).addresses || {};
        const addr = addresses[paper_id];
        return textResult(addr
          ? { ...addr, digest_verified_at_build: true, hash_algorithm: "blake3-256" }
          : { digest_verified_at_build: false, reason: "no ANLA address for this paper_id" });
      },
    );

    return server;
  });
}
