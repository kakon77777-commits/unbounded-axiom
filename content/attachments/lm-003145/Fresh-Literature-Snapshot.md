# Series C / Paper 09 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 09 fresh-search grounding；不得自動沿用為 Paper 10 的 fresh search。

## 1. NIST AI Agent Identity and Authorization
NIST / NCCoE, 2026
- NIST 2026 推動 AI Agent Standards Initiative。
- NCCoE concept paper 專門處理 software / AI agent identity and authorization。
- 對本篇意義：agent identity、delegation、authorization 已從一般 IAM 的邊角問題變成獨立標準化領域。

## 2. OWASP Top 10 for Agentic Applications 2026
OWASP GenAI Security Project
- risk surface 包括 goal hijacking、tool misuse、identity/privilege abuse、supply chain、unexpected code execution、memory/context poisoning、inter-agent communication、cascading failures、human-agent trust exploitation、rogue agents。
- 對本篇意義：能力面新增的 tool / memory / identity / delegation 結構，幾乎直接對應新的安全面。

## 3. Security Considerations for Artificial Intelligence Agents
arXiv:2603.12230
- 來自 general-purpose agent production experience 的 security recommendations。
- 將 code-data separation、authority boundaries、execution predictability 視為 Agent 架構改變後的核心問題。
- defenses 分成 model/input mitigations、sandbox、deterministic policy enforcement。
- 對本篇意義：security surface 是 information flow + delegated authority + execution 的系統問題。

## 4. Toward Secure LLM Agents
arXiv:2606.10749
- 247-paper lifecycle / systems survey。
- prompt injection、tool-mediated control flow、persistent state corruption、multi-agent propagation 是核心區域。
- current defenses weakly compositional；long-horizon/stateful risks 評估不足。
- 對本篇意義：Agent security 已由單 prompt vulnerability 擴張到 stateful systems security。

## 5. Layered Attack Surface Model
arXiv:2604.23338
- 七層：Foundation、Cognitive、Memory、Tool Execution、Multi-Agent Coordination、Ecosystem、Governance。
- 加上四類 temporality。
- 研究明確指出使 Agent 比 chatbot 更 capable 的架構決策也會增加 adversarial surface。
- 對本篇意義：capability surface / security surface coexpansion 有直接相鄰研究。

## 6. AuthBench / Least-Privilege Authorization
arXiv:2605.14859
- 120 realistic terminal tasks。
- frontier models 在 permission inference 上同時有 under-grant 與 over-grant。
- more reasoning 不會簡單消除問題，反而收斂到 model-specific authorization attractor。
- Sufficiency-Tightness Decomposition 分開 coverage 與敏感權限 audit。
- 對本篇意義：least privilege 不是純「越嚴越好」，而是 sufficiency + tightness 的二維問題。

## 7. MiniScope
arXiv:2512.11147
- least privilege framework for tool-calling agents。
- 透過 permission hierarchy + mobile-style permission model 約束可造成的損害。
- 對本篇意義：capability scoping 是縮小 operational attack surface 的直接方式。

## 8. Compositional Authorization / Intent-Governed Authorization
arXiv:2606.03518 / 2606.22916
- 強調 delegated authority 應 explicit、limited、contextual、revocable、auditable。
- 只問 credential 是否能呼叫 endpoint 不夠，還要問 action 是否符合當前 delegated intent。
- 對本篇意義：安全 policy 所需 representation 隨 Agent autonomy 變得更細緻。

## 9. Separating Capability from Permission
arXiv:2607.23438
- 明確分離 Autonomous Capability Levels 與 Allowed Autonomy Levels。
- 高技術能力的 Agent 可以因 risk / reversibility / accountability 被部署在較低 allowed autonomy。
- 對本篇意義：安全不是降低能力本身，而是治理可使用 capability。

## 10. OpenAI frontier cyber safeguards
Official OpenAI system cards, 2026
- GPT-5.3-Codex 被視為 High capability in Cybersecurity，啟動相關 safeguards。
- GPT-5.4 Thinking 是第一個一般用途模型以 High cybersecurity capability safeguards 部署。
- GPT-5.6 family 亦被標為 High in Cybersecurity。
- 對本篇意義：capability frontier 與 safeguard frontier 在實際 frontier deployment 中已明確耦合。

## Paper 09 定位

本文不建立 offensive-security 操作指南。
本文只研究架構層關係：

$$
\mathfrak C\uparrow
\Rightarrow
\Sigma_{\mathrm{potential}}\uparrow
$$

在 controls 固定的條件下成立；

同時：

$$
\text{security-policy discrimination demands}
\uparrow
\Rightarrow
\text{security representation / observability demands}
\uparrow.
$$

這就是 Defensive Epistemic Coexpansion。
