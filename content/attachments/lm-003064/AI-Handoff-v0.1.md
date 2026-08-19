# AI HANDOFF — TCUE-SNS Paper 04 v0.1

## Canonical-source rules

1. `paper.md` 是唯一 canonical paper source。
2. 數學只允許 `$...$` 與 `$$...$$`。
3. 不可把 LaTeX 公式轉成 Unicode 數學字元後覆寫 source。
4. 不可進行 `unicode_escape` 類 round-trip。
5. 不可靜默修改反斜線、空白、delimiter、公式換行或符號命名。
6. 若需要 renderer-specific normalization，必須保留原 source、產生 diff、在 provenance 明示並重新驗證。
7. 後續版本修改應新增版本，不應無痕覆寫 v0.1。

## Theory constraints to preserve

- `Metacognition != Safety`。
- `Self-Awareness(R) != not-R`。
- `Detect != Interpret != Evaluate != Control != Rewrite`。
- `Presentation Depth != Deception Depth`。
- deliberate naturalness 是高階表述策略，不是「無算子」。
- sincerity 與 strategic effect 可以同時成立；不可二元化成「真誠 vs 策略」。
- `Self-Report != Self-Operator Truth`。
- `Self-Certification != Safety Certification`。
- 高反思不能被自動病理化，也不能被當成心理健康證明。
- 高元認知不得被升格為更高基本道德地位。
- Self-Model 可以進入下一輪 Choice Bottom-Space，故 profiling / self-description 具有反身擾動可能。
- External Corrigibility 必須與自我反思能力分開評估。
- 行為域需要獨立審計，但不得因此抹除第一人稱主體域。
- AI 的 metacognitive-like behavior 不得直接等同人類式 subjectivity。
- Meta expansion 必須保存 provenance、invariants、failure log、versioning 與 anti-immunization。

## Next paper

Paper 05：**認知僭越論：從可知、可推論到可控制的權力跨越**。
