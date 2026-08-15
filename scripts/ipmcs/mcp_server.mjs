// IPMCS Phase IP-5 -- MCP Surface.
//
// A real, locally-runnable MCP server (stdio transport) over IP-2/IP-3/IP-4's
// already-built, already-tested runtime (ipmcs_search.mjs). Not a Cloudflare
// Worker deployment yet -- ipmcsSearch()/divergeBranches()/expandAddresses()
// depend on Node's fs, child_process (Python subprocess calls) and a locally-
// run @huggingface/transformers pipeline, none of which run in Workers. That
// migration is a separate, later step (and per project-logic-matrix-mcp
// memory: createMcpHandler, not the deprecated McpAgent, when it happens).
// This phase's job is the tool SURFACE, over the real runtime, testable today.
//
// Uses @modelcontextprotocol/server v2 (McpServer + StdioServerTransport,
// 2026-07-28 MCP spec) -- verified against the current published README and
// npm registry before use, not assumed from training data (the same class of
// staleness that made McpAgent look current when it was already deprecated).
//
// Tool surface vs. the IPMCS spec's suggested list (IPMCS_v0.1 section 23:
// search_identity / expand_query / search_views / get_object / get_evidence /
// get_paths / get_conflicts / expand_address):
//   IMPLEMENTED, each a thin wrapper over a real function -- no reimplementation:
//     search_identity -> ipmcsSearch()
//     expand_query     -> divergeBranches()
//     search_views     -> ipmcsSearch(), filtered to one view's paths
//     get_object       -> getObject()
//     expand_address   -> expandAddresses()
//   DELIBERATELY NOT IMPLEMENTED this phase (would require capabilities that
//   don't exist yet -- listing them build fake data, exactly what this whole
//   session's discipline argues against; changepoint-v1 was deferred the same
//   way in IP-1/IP-2 for the same reason):
//     get_evidence  -- needs cross-object contradiction/support detection;
//                      ai-web-research has this for WEB-crawled evidence, but
//                      nothing analogous exists for Logic Matrix's own corpus.
//     get_paths     -- search_identity's objects[].paths already IS this, for
//                      a specific query; a standalone stateless get_paths(id)
//                      with no query has no well-defined real answer (paths
//                      are relative to a search, not an object's own property).
//     get_conflicts -- same gap as get_evidence.
import { McpServer } from "@modelcontextprotocol/server";
import { StdioServerTransport } from "@modelcontextprotocol/server/stdio";
import * as z from "zod";
import { ipmcsSearch, divergeBranches, expandAddresses, getObject } from "./ipmcs_search.mjs";

const server = new McpServer({ name: "logic-matrix-ipmcs", version: "0.1.0" });

function textResult(value) {
  return { content: [{ type: "text", text: JSON.stringify(value, null, 2) }] };
}

server.registerTool(
  "search_identity",
  {
    description: "IPMCS core search: runs a query across exact/lexical/semantic retrievers "
      + "(and optionally real LLM-based query divergence), folds every hit back to its "
      + "canonical Logic Matrix paper_id, and returns ranked objects each carrying the full "
      + "set of paths (branch + view + retriever) that found them -- not just a score.",
    inputSchema: {
      query: z.string().describe("search query, natural language or terminology, any language"),
      diverge: z.boolean().optional().describe("layer real LLM-based query divergence on top (ai-web-research's diverge(), real Vertex AI call, has a small real cost). Default false."),
      expandAddress: z.boolean().optional().describe("attach ANLA-verified provenance (digest_verified + object_id/content_hash) to each result. Default false."),
      topK: z.number().int().min(1).max(50).optional().describe("max objects to return, default 10"),
    },
  },
  async ({ query, diverge, expandAddress, topK }) => {
    const result = await ipmcsSearch(query, { diverge, expandAddress, topK });
    return textResult(result);
  },
);

server.registerTool(
  "expand_query",
  {
    description: "Real LLM-based query divergence (ai-web-research's diverge(), 5 categories: "
      + "semantic/task/source/language/perspective). Returns the branches WITHOUT running a "
      + "search -- useful for inspecting what IPMCS's divergence would try before spending the "
      + "retrieval cost. Each call is a real, small-cost Vertex AI request, not simulated.",
    inputSchema: {
      query: z.string(),
      maxBranches: z.number().int().min(1).max(20).optional().describe("cap on branches beyond the original, default 6"),
    },
  },
  async ({ query, maxBranches }) => {
    const branches = await divergeBranches(query, maxBranches ? { maxBranches } : undefined);
    return textResult({ query, branches });
  },
);

server.registerTool(
  "search_views",
  {
    description: "search_identity restricted to one segmentation view (document = whole-paper "
      + "hits, chunk-v1 = section/passage-level hits from the DSRS Vectorize chunk namespace). "
      + "The restriction applies BEFORE ranking, not as a post-hoc filter: ranking and topK are "
      + "computed from that view's hits alone, so an object relevant only at chunk level still "
      + "surfaces (a naive filter-after-slice approach was tried and dropped -- it silently lost "
      + "chunk-only objects whenever they didn't also rank in the top results by whole-document "
      + "relevance). Note chunk-v1 currently only has semantic-channel coverage: exact/lexical "
      + "scoring in this codebase runs over whole documents only, so has_exact is always false "
      + "for a chunk-v1-only view -- a real limitation of what's built, not a query bug.",
    inputSchema: {
      query: z.string(),
      view: z.enum(["document", "chunk-v1"]).describe(
        "changepoint-v1 is in the IPMCS spec's view list but not implemented for this corpus yet "
        + "(no markdown-aware structural segmenter wired up -- see project-logic-matrix-mcp memory)"),
      topK: z.number().int().min(1).max(50).optional(),
    },
  },
  async ({ query, view, topK }) => {
    const result = await ipmcsSearch(query, { topK: topK ?? 10, views: [view] });
    return textResult({ query, view, objects: result.objects });
  },
);

server.registerTool(
  "get_object",
  {
    description: "Look up a Logic Matrix paper's own metadata (title, section headings) by "
      + "paper_id, with no search involved.",
    inputSchema: { paper_id: z.string() },
  },
  async ({ paper_id }) => {
    const obj = getObject(paper_id);
    return textResult(obj ?? { object_id: paper_id, found: false });
  },
);

server.registerTool(
  "expand_address",
  {
    description: "IP-4: resolve a Logic Matrix paper_id to its ANLA-verified canonical address "
      + "(object_id, content_hash, byte size) by re-extracting it from the real anla1-packed "
      + "archive of content/papers/ and checking its full chunk+file hash chain. "
      + "digest_verified is only ever true when that chain actually ran and matched.",
    inputSchema: { paper_id: z.string() },
  },
  async ({ paper_id }) => {
    const provenance = await expandAddresses([paper_id]);
    return textResult(provenance.get(paper_id) ?? { digest_verified: false, reason: "no ANLA address for this paper_id" });
  },
);

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("logic-matrix-ipmcs MCP server ready (stdio)");
}

main();
