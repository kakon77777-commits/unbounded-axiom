# Series C / Paper 04 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 04 fresh-search grounding；不得自動沿用為 Paper 05 的 fresh search。

## 1. Lean Kernel / TCB
Source: Lean Language Reference, Elaboration and Compilation
- Lean 的 trusted kernel 是較小的 core type checker。
- 新增 definitions / inductive types 前由 kernel 檢查。
- 官方文件指出存在 Rust 與 Lean 的 independent re-implementations，並鼓勵 cross-check。
- 意義：把高階生成工具與最終 trusted checker 分離，降低 reasoning-tool bug 直接升格成 theorem 的風險。

## 2. Validating a Lean Proof
Source: Lean official documentation
- 高風險情境建議 comparator + sandbox + exported proof + official kernel / external checker。
- 官方列出 remaining assumptions：logic、comparator plumbing、sandbox、共同 checker bug、人為 theorem-statement 錯誤。
- 意義：formal proof 依然是 conditional trust chain，不是絕對 oracle。

## 3. Lean 4.32.1 / 4.32.2
Source: Lean official release notes
- 4.32.1：修正 kernel soundness bug。
- 4.32.2：再次修正 kernel soundness bug；官方說明某 bug 可使 kernel 接受 False。
- 最新 stable release list 在 2026-08-10 已到 Lean 4.33.0。
- 意義：implementation-level trusted base 必須被獨立審計與版本化。

## 4. CompCert
Source: CompCert 3.17 official documentation
- 對 compiler passes 做 semantic preservation proof。
- 若 source program 已被 sound verification 證明滿足 property，CompCert 的 compiler-correctness argument可把該 property 帶到 generated code。
- 意義：formal proof 可以「關閉一個 translation boundary」，但不負責 world-level specification 是否正確。

## 5. Nix Reproducible Builds
Source: NixOS official project documentation
- 相同 source 在 independent infrastructure 得到 bit-for-bit identical results 可增加 source↔artifact provenance 信心。
- 官方同時指出 repeated build 本身不能證明 reproducibility，timestamp 等 nondeterminism 仍可能存在。
- 意義：reproducibility 是 provenance/reconstruction property，不是 semantic truth。

## 6. AlphaEvolve
Source: Google DeepMind official publication
- 候選 programs 由 automated evaluators verify、run、score。
- 意義：AI generation 由 machine execution 提供 objective / quantifiable evaluation loop，但只在 evaluator 定義的 task domain 內成立。

## 7. VeriAct
arXiv:2604.00280
- 研究發現 verifier-accepted formal specifications 中，仍有大量 incorrect / incomplete cases。
- 建立 Spec-Harness，檢查 specification correctness/completeness，而不只 verifier pass。
- 意義：formal verification 最大的 boundary 之一是 specification fidelity。

## 8. AgentForge
arXiv:2604.13120
- 把 sandboxed execution 當成每次 code change propagation 前的 mandatory verification。
- 意義：execution feedback 可作為比純 next-token plausibility 更異質的 feedback channel。

## 9. Scaling Agentic Verifier
arXiv:2602.04254
- execution-based agent 主動找 discriminative inputs，產生 counterexamples 區分 candidate programs。
- 意義：外部執行器不只是 pass/fail oracle，也能成為 active experimental instrument。

## 10. OpenProver
arXiv:2607.09217
- Agentic / interactive theorem proving with Lean 4 verification。
- 意義：LLM 生成與 formal kernel validation 的分工已成為 2026 automated-theorem-proving 系統的明確架構方向。

## Paper 04 定位

本篇不把「計算機是客觀的」當 metaphysical axiom。
本篇提出的是工程型、條件型定義：
- fixed artifact / input / environment 後，結果不依賴 source Agent 的語言權威；
- artifact 可重放；
- trust assumptions 可列舉；
- failure surface 可局部化；
- 可用 independent implementations 降低 common-mode implementation risk；
- world-level truth 仍需要 specification fidelity 與 external grounding。
