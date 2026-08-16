// Tests the REMOTE (Workers) MCP server through the real MCP protocol over
// real HTTP -- point BASE_URL at a local `wrangler dev` instance first, then
// re-run against the live production URL after deploy. Not a unit test of
// src/mcp.js's internals; this exercises the same StreamableHTTP path a real
// ChatGPT/Claude.ai connector would use.
import { Client } from "@modelcontextprotocol/client";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/client";

const BASE_URL = process.argv[2] || "http://localhost:8799";

const client = new Client({ name: "ipmcs-remote-test-client", version: "0.1.0" });
const transport = new StreamableHTTPClientTransport(new URL(`${BASE_URL}/mcp`));

await client.connect(transport);
console.error(`connected to ${BASE_URL}/mcp`);

const { tools } = await client.listTools();
console.error(`listTools -> ${tools.length} tools: ${tools.map(t => t.name).join(", ")}`);

function printResult(label, result) {
  const text = result.content?.[0]?.text ?? "(no text content)";
  console.error(`\n--- ${label} ---`);
  console.error(text.length > 1000 ? text.slice(0, 1000) + "\n...[truncated]" : text);
}

const search = await client.callTool({
  name: "search_identity",
  arguments: { query: "動態不動點", topK: 3 },
});
printResult("search_identity(動態不動點, topK:3)", search);

const obj = await client.callTool({ name: "get_object", arguments: { paper_id: "lm-002549" } });
printResult("get_object(lm-002549)", obj);

const addr = await client.callTool({ name: "expand_address", arguments: { paper_id: "lm-002549" } });
printResult("expand_address(lm-002549)", addr);

const addrMissing = await client.callTool({ name: "expand_address", arguments: { paper_id: "lm-999999" } });
printResult("expand_address(lm-999999, should not exist)", addrMissing);

await client.close();
console.error("\nall tool calls completed through the real remote MCP protocol.");
