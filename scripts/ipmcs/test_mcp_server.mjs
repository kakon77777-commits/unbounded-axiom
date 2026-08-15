// IP-5 end-to-end test: spawns mcp_server.mjs as a real subprocess over the
// real MCP stdio protocol (not a direct function call) and exercises each
// tool through it -- the actual trigger mechanism another AI would use, not
// a shortcut around it.
import { Client } from "@modelcontextprotocol/client";
import { StdioClientTransport } from "@modelcontextprotocol/client/stdio";
import { fileURLToPath } from "node:url";

const client = new Client({ name: "ipmcs-test-client", version: "0.1.0" });
const transport = new StdioClientTransport({
  command: process.execPath,
  args: [fileURLToPath(new URL("./mcp_server.mjs", import.meta.url))],
});

await client.connect(transport);
console.error("connected.");

const caps = client.getServerCapabilities();
console.error("server capabilities.tools present:", !!caps.tools);

const { tools } = await client.listTools();
console.error(`listTools -> ${tools.length} tools: ${tools.map(t => t.name).join(", ")}`);

function printResult(label, result) {
  const text = result.content?.[0]?.text ?? "(no text content)";
  console.error(`\n--- ${label} ---`);
  console.error(text.length > 1200 ? text.slice(0, 1200) + "\n...[truncated]" : text);
}

// get_object: real metadata lookup, no search
const obj = await client.callTool({ name: "get_object", arguments: { paper_id: "lm-002549" } });
printResult("get_object(lm-002549)", obj);

// expand_address: real ANLA digest verification through the protocol
const addr = await client.callTool({ name: "expand_address", arguments: { paper_id: "lm-002549" } });
printResult("expand_address(lm-002549)", addr);

// unknown id -- must not fabricate a false verification
const addrMissing = await client.callTool({ name: "expand_address", arguments: { paper_id: "lm-999999" } });
printResult("expand_address(lm-999999, should not exist)", addrMissing);

// search_identity: real exact/lexical/semantic search, no divergence (keep cost/time down)
const search = await client.callTool({
  name: "search_identity",
  arguments: { query: "動態不動點", expandAddress: true, topK: 3 },
});
printResult("search_identity(動態不動點, expandAddress:true, topK:3)", search);

// search_views: filtered to chunk-v1 only
const views = await client.callTool({
  name: "search_views",
  arguments: { query: "動態不動點", view: "chunk-v1", topK: 5 },
});
printResult("search_views(動態不動點, chunk-v1)", views);

// expand_query: real LLM call (small real cost) -- last untested tool; a
// prior assumption that a thin wrapper "must be fine by inspection" was
// exactly what let the search_views bug through, so this gets a real run too.
const expanded = await client.callTool({
  name: "expand_query",
  arguments: { query: "忒修斯之船", maxBranches: 4 },
});
printResult("expand_query(忒修斯之船, maxBranches:4)", expanded);

await client.close();
console.error("\nall tool calls completed through the real MCP protocol.");
