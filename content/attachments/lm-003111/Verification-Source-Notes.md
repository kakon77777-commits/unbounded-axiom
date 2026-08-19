# Verification and source notes

Verification date: 2026-08-14.

Freshly verified primary sources:

1. Cloudflare, "Introducing Pay Per Crawl: Enabling Content Owners to Charge AI Crawlers for Access", 2025-07-01.
2. Cloudflare, "Announcing the Monetization Gateway: charge for any resource behind Cloudflare via x402", 2026-07-01.
3. Cloudflare, "Making AI search smarter", 2026-07-01. The post explicitly describes the shift from Pay Per Crawl toward Pay Per Use and gives the example that one page can be crawled once yet used in many answers, or crawled repeatedly and never used.
4. Cloudflare, "Unmasking the crawls with Attribution Business Insights", 2026-07-01. The product motivation is to distinguish crawler traffic that provides business value from traffic that only consumes resources.
5. Cloudflare Agents docs, "Agentic Payments", updated 2026-06-03.
6. Cloudflare Agents docs, "x402", updated 2026-06-03.
7. Cloudflare Agents docs, "Charge for MCP tools", updated 2026-06-03. The docs support per-tool-call payment via paidTool.
8. Cloudflare Agents docs, "Charge for HTTP content", updated 2026-06-03.
9. x402 Foundation / Linux Foundation announcement, 2026-07-14.

Boundary notes:
- TTSA, the seven-dimensional traffic state, Machine Attention Depth, Executable Attention, Machine Attention Quality, Traffic Persistence Value, downstream reach, typed traffic tensor, and the formal scalar-insufficiency results are proposed in this paper.
- Cloudflare and x402 are used as current engineering evidence that machine traffic is becoming differentiated by actor, intent, usage, and payment state. They are not treated as the source of the TTSA formal theory.
- Automated traffic is deliberately broader than Machine Attention.
- The depth ladder is an operational taxonomy, not a universal physical scale.
