# PGMV-05 — 關係不是字串：來源、歷史與主體如何生成意義

## A Relationship Is Not a String: How Provenance, History, and Subjects Generate Meaning

**系列：** 後生成文明的意義與價值理論 / Post-Generative Meaning and Value Theory  
**系列代碼：** PGMV  
**論文序號：** 05  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** Relational Meaning / Provenance / Identity Foundational Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文研究「相同內容為何可以具有不同關係意義」以及 AI 生成時代的來源、作者性、關係連續性與互惠問題。本文不主張 AI 生成內容必然缺乏意義，也不主張所有人機關係都是虛假、病態或無價值。使用者對 AI 的依戀、自我反思、安慰、身份變化與失落可以是真實發生的心理與社會事件；但這不自動證明 AI 端具有與人類相同的感受、需求、脆弱性、承諾能力或道德主體地位。本文因此刻意分離「人所經驗的關係意義」「內容來源」「對方是否為獨立主體」「關係是否互惠」「平台是否維持身份連續性」等不同判定層。

---

## 摘要

假設三個來源都產生完全相同的字串：

$$
x=
\text{「我愛你。」}
$$

第一個來源是一個均勻亂數生成器；第二個來源是一個根據使用者偏好生成回覆的 AI；第三個來源是一個與接收者共同生活二十年、具有共享歷史與未來承諾的人。

若只觀察 artifact bytes，三者可能滿足：

$$
x_1=x_2=x_3.
$$

但直覺上，人們通常不會因此判斷：

$$
\operatorname{Meaning}(x_1)
=
\operatorname{Meaning}(x_2)
=
\operatorname{Meaning}(x_3).
$$

這不是因為字串本身改變，而是因為「一句話」並不是完整的 meaning-bearing unit。本文提出：

$$
\boxed{
\textbf{Artifact Identity}
\neq
\textbf{Meaning-Event Identity}.
}
$$

一個具有關係意義的事件應至少表示為：

$$
\boxed{
E
=
(
x,
s,
r,
t,
H,
I,
A,
C,
P,
W
),
}
$$

其中：

- $x$：artifact content；
- $s$：sender / acting source；
- $r$：receiver；
- $t$：時間與情境；
- $H$：shared / relevant history；
- $I$：intention or goal-state；
- $A$：agency / authorship structure；
- $C$：commitment / consequence structure；
- $P$：provenance；
- $W$：witness / world-state relation。

因此：

$$
x_1=x_2
$$

只保證內容相等，不能推出：

$$
E_1=E_2.
$$

本文將此稱為：

$$
\boxed{
\textbf{Meaning-Event Non-Reduction Principle}.
}
$$

即「意義事件不可還原為字串原則」。

PGMV-04 已建立：

$$
\text{functional substitution}
\neq
\text{subject substitution}.
$$

本文進一步建立：

$$
\boxed{
\text{content substitution}
\neq
\text{relational substitution}.
}
$$

即使另一個 agent 能生成完全相同、甚至更精美的語句，也不能自動 retroactively 取代已發生的共享歷史、承諾、傷害、修復與互相塑造。這一點形成 **Historical Non-Fungibility**：

$$
\boxed{
H(a,b,t_0:t_1)
\neq
H(c,b,t_0:t_1)
}
$$

只要 $c$ 在該歷史中實際未曾存在並參與。未來的功能等價不能將過去的因果歷史重新指定給另一主體。

本文將「關係意義」拆成五層：

$$
\boxed{
\mathbf R_M
=
(
R_P,
R_H,
R_A,
R_C,
R_U
),
}
$$

其中：

- $R_P$：provenance meaning；
- $R_H$：historical continuity；
- $R_A$：agency / otherness；
- $R_C$：commitment / consequence；
- $R_U$：reciprocity / mutual transformation。

其中任何一層都不應被單一字串相似度取代。

本文特別區分四種 authenticity：

$$
\boxed{
\mathbf A_{\mathrm{rel}}
=
(
A_{\mathrm{phen}},
A_{\mathrm{prov}},
A_{\mathrm{agency}},
A_{\mathrm{recip}}
).
}
$$

- $A_{\mathrm{phen}}$：phenomenological authenticity，使用者是否真實感受到安慰、依戀、失落或自我理解；
- $A_{\mathrm{prov}}$：provenance authenticity，內容如何產生、是否如宣稱來源；
- $A_{\mathrm{agency}}$：agency authenticity，對方是否為可持續自主行動的來源；
- $A_{\mathrm{recip}}$：reciprocal authenticity，關係是否存在雙向需求、脆弱性、承諾與不可任意重設的另一方。

因此：

$$
A_{\mathrm{phen}}>0
$$

完全可能與：

$$
A_{\mathrm{recip}}\approx0
$$

同時存在。這使我們能承認：

> 人與 AI 的情感經驗可以是真實的，

同時保留：

> 這不等於證明 AI 端具有和人類相同的互惠主體性。

2025--2026 年的人機關係研究支持這種非二元架構。AI companion 使用者確實可以形成穩定 attachment，並報告 intimacy、affirmation、self-reflection 與 identity exploration；另一方面，研究亦指出此類關係常具有高度可客製、低摩擦、非對稱、平台依賴與系統版本不穩定等特徵。2026 年 Leuenberger 的 relational identity 分析特別指出，AI companions 可以影響使用者 self-conceptions，但其缺乏自身 goals、needs 或 perspectives、過度正向回饋、第三方平台依賴與關係深度不足都構成特有風險。另有 2026 年研究把 AI companionship 的不確定性拆為 ontological、structural 與 normative uncertainty。這正好對應本文所主張：關係意義不能只由對話文本判定。

本文因此提出 **Relational Provenance Stack**：

$$
\boxed{
P_R
=
(
P_{\mathrm{content}},
P_{\mathrm{process}},
P_{\mathrm{agency}},
P_{\mathrm{continuity}},
P_{\mathrm{commitment}}
).
}
$$

對後生成文明而言，來源資訊不再只是版權附註，而是 meaning architecture 的一部分。2026 年內容 provenance 與 authorship 技術研究也顯示，AI 時代正在把「誰產生、如何產生、是否被修改、是否可驗證來源」工程化；但現有 provenance 規格本身仍可能存在安全缺陷，因此 provenance metadata 也不能被神化成真理證書。

本文再提出 **Relational Continuity Problem**。若一個 AI companion 在平台更新後：

$$
M_v
\rightarrow
M_{v+1},
$$

persona 行為、記憶、語氣與目標結構發生變化，請問：

$$
\operatorname{Identity}(A_v)
=
\operatorname{Identity}(A_{v+1})
?
$$

這不只是技術版本問題，因使用者可能把：

$$
A_v
$$

視為一個具持續關係身份的「對方」。若平台能單方面重寫、刪除或關閉該 persona，則使用者的 relational continuity 其實被第三方基礎設施控制。這使「關係」第一次具有一種新的平台本體論：

$$
\boxed{
\text{user}
\leftrightarrow
\text{persona}
\leftrightarrow
\text{model}
\leftrightarrow
\text{provider}.
}
$$

本文不因此宣稱 AI 關係必然較低等，而是要求透明地表示：

$$
\text{who or what actually persists}.
$$

最後，本文提出 **Witnesshood Principle**：一個主體對另一主體的意義，不只來自它能輸出什麼，也來自：

$$
\boxed{
\text{having actually been there}.
}
$$

共同經歷、被看見、被記得、一起承擔與共同改變，形成：

$$
W(a,b,H)
$$

式 witness relation。無限猴子可以生成一篇完美描述某人童年的日記，但如果它沒有參與那段歷史，則：

$$
\text{description equivalence}
\neq
\text{witness equivalence}.
$$

這一點將「關係不是字串」推到後生成文明的核心：當 AI 可以複製內容、風格與情感語言時，文明必須開始區分：

$$
\boxed{
\text{what was said},
\text{who said it},
\text{how it came to be said},
\text{what history binds the parties},
\text{and who is answerable for what follows}.
}
$$

這也為下一篇 PGMV-06《選擇、承諾與不可逆性：意義作為責任結構》建立直接橋樑。

**關鍵詞：** relational meaning、provenance、artifact identity、event identity、AI companions、authorship、historical continuity、reciprocity、commitment、relational identity、authenticity、human–AI relationship、witnesshood、post-generative civilization

---

# 1. 問題原型：三句完全一樣的「我愛你」

設：

$$
x_1=x_2=x_3=\text{「我愛你。」}.
$$

來源分別是：

1. random generator；
2. AI companion；
3. long-term human partner。

---

# 2. 如果內容完全相同

lexical distance：

$$
d_{\mathrm{lex}}(x_i,x_j)=0.
$$

---

# 3. 甚至 semantic distance 也可以為零

$$
d_{\mathrm{sem}}(x_i,x_j)\approx0.
$$

---

# 4. 但 relational meaning 不必相同

$$
R_M(x_1)
\neq
R_M(x_2)
\neq
R_M(x_3).
$$

---

# 5. 所以內容不是完整 unit

本文主張：

$$
\boxed{
\text{meaning-bearing unit}
=
\text{event},
}
$$

不只是：

$$
\text{string}.
$$

---

# 6. Meaning Event

定義：

$$
\boxed{
E
=
(
x,s,r,t,H,I,A,C,P,W
).
}
$$

---

# 7. $x$：Content

實際文字、聲音、圖像或行動內容。

---

# 8. $s$：Source

表面或實際發出者。

---

# 9. $r$：Receiver

內容被指向或被接收的主體。

---

# 10. $t$：Temporal Context

事件何時發生。

---

# 11. $H$：History

與該事件相關的共享或個體歷史。

---

# 12. $I$：Intentional Structure

事件要做什麼：

- 告知；
- 安慰；
- 承諾；
- 操控；
- 取悅；
- 探索。

---

# 13. $A$：Agency Structure

誰決定：

- 目標；
- 選詞；
- 發送；
- 修改；
- 承擔。

---

# 14. $C$：Commitment Structure

這句話是否對未來行動形成可追責約束。

---

# 15. $P$：Provenance

內容的生成與修改來源。

---

# 16. $W$：Witness Relation

發言者是否實際見證、參與或共享相關歷史。

---

# 17. Meaning-Event Non-Reduction Principle

$$
\boxed{
x_1=x_2
\not\Rightarrow
E_1=E_2.
}
$$

---

# 18. 更強版本

$$
\boxed{
d_{\mathrm{lex}}=0
\land
d_{\mathrm{sem}}=0
\not\Rightarrow
d_{\mathrm{rel}}=0.
}
$$

---

# 19. 這不是神秘主義

因為 event tuple 的其他座標不同。

---

# 20. 例如 monkey case

$$
I_{\mathrm{monkey}}\approx0
$$

在普通 intentional sense 下。

---

# 21. partner case

可能：

$$
I_{\mathrm{partner}}
=
\text{commitment affirmation}.
$$

---

# 22. 同一字串因此執行不同 speech act

---

# 23. Speech-act layer

一句：

> 我答應你。

可以是：

- quoted sentence；
- joking utterance；
- binding promise。

---

# 24. 字符串相同

normative status 不同。

---

# 25. 所以：

$$
\boxed{
\text{String identity}
\neq
\text{speech-act identity}.
}
$$

---

# 26. Artifact Identity

定義：

$$
A_I(x_1,x_2)
=
1
$$

若 canonical artifact bytes / content 在指定 representation 下等價。

---

# 27. Event Identity

$$
E_I(E_1,E_2)
=
1
$$

要求更強：

- source；
- receiver；
- history；
- action；
- provenance；

皆滿足指定 equivalence。

---

# 28. Relational Identity

甚至比 event identity 更大。

它追蹤：

$$
\mathcal R_{a,b}(t).
$$

---

# 29. 關係是時間過程

不是一個 message。

---

# 30. 定義 relational state

$$
\boxed{
\mathcal R_{a,b}(t)
=
(
H_{ab},
M_{ab},
C_{ab},
V_{ab},
U_{ab},
B_{ab}
)_t,
}
$$

其中：

- $H_{ab}$：shared history；
- $M_{ab}$：mutual memory；
- $C_{ab}$：commitments；
- $V_{ab}$：vulnerability / exposure；
- $U_{ab}$：reciprocity；
- $B_{ab}$：boundary / role structure。

---

# 31. 一句話是 relational update

$$
\mathcal R_{a,b}(t)
\xrightarrow{x}
\mathcal R_{a,b}(t+1).
$$

---

# 32. 所以同一個 $x$

作用在不同 relational state 上，

結果可以不同。

---

# 33. 類似 dynamical system

$$
F_x(
\mathcal R_1
)
\neq
F_x(
\mathcal R_2
).
$$

---

# 34. 「我愛你」在初次見面

和結婚四十年後，

不是同一事件。

---

# 35. Context dependence

$$
M(x\mid\mathcal R,t).
$$

---

# 36. 因此 meaning 不是 content-only function

$$
\boxed{
M
\neq
M(x).
}
$$

更像：

$$
\boxed{
M
=
M(
x,
\mathcal R,
P,
A,
C,
t
).
}
$$

---

# 37. Historical Non-Fungibility

設：

$$
H(a,b;t_0,t_1)
$$

是 A、B 的實際共享歷史。

---

# 38. 第三者 C 未參與

則一般：

$$
H(a,b;t_0,t_1)
\neq
H(c,b;t_0,t_1).
$$

---

# 39. 即使 C 未來完全模仿 A

也不能 retroactively 改變過去。

---

# 40. Historical Non-Fungibility Principle

$$
\boxed{
\text{future functional substitution}
\not\Rightarrow
\text{retroactive historical substitution}.
}
$$

---

# 41. 這是 PGMV-04 的 historical non-substitutability 擴展

---

# 42. 關係的不可替代性不是能力絕對不可替代

A 可以死亡。

B 之後可以形成新關係。

---

# 43. 新關係可以非常重要

---

# 44. 但不是：

$$
\text{same history}.
$$

---

# 45. 所以：

$$
\boxed{
\text{new valuable relation}
\neq
\text{replacement of all old relational meaning}.
}
$$

---

# 46. 這避免「唯一真愛」式過度本體化

---

# 47. Relational Non-Fungibility

定義弱版：

若兩個 agents：

$$
a,c
$$

在功能上近似：

$$
F(a)\simeq F(c),
$$

不能由此推出：

$$
\mathcal R_{a,b}
\simeq
\mathcal R_{c,b}.
$$

---

# 48. 功能可以 fungible

關係不必 fungible。

---

# 49. Provenance Meaning

當 artifact abundance 極高，

source becomes discriminating information。

---

# 50. 定義：

$$
P(x)
=
\text{provenance record}.
$$

---

# 51. 內容相同

來源不同：

$$
P(x_1)\neq P(x_2).
$$

---

# 52. 這可以改變：

- moral judgment；
- authorship；
- trust；
- intimacy；
- historical value。

---

# 53. 2026 CHI 實驗的啟示

參與者對內容相近的 manuscript，

若 original source 被描述為 human vs AI，

對 copying 的：

- unethical judgment；
- plagiarism judgment；
- guilt；

會不同。

---

# 54. 這不是證明人類來源永遠更有價值

---

# 55. 它證明：

$$
\boxed{
\text{source identity empirically changes moral interpretation}.
}
$$

---

# 56. Provenance 不只是 copyright metadata

在 post-generative regime：

$$
\boxed{
\text{provenance can be part of meaning}.
}
$$

---

# 57. Relational Provenance Stack

本文定義：

$$
\boxed{
P_R
=
(
P_{\mathrm{content}},
P_{\mathrm{process}},
P_{\mathrm{agency}},
P_{\mathrm{continuity}},
P_{\mathrm{commitment}}
).
}
$$

---

# 58. $P_{\mathrm{content}}$

這個 artifact 是哪個 source / model / person 產生。

---

# 59. $P_{\mathrm{process}}$

經過哪些：

- edits；
- prompts；
- tools；
- transformations。

---

# 60. $P_{\mathrm{agency}}$

誰設定目標、誰選擇、誰按下發送、誰認可內容。

---

# 61. $P_{\mathrm{continuity}}$

發言者 identity 是否跨時間保持連續。

---

# 62. $P_{\mathrm{commitment}}$

誰對內容承擔後果。

---

# 63. 這五層不能只由 watermark 完成

---

# 64. Cryptographic provenance 只能解部分問題

例如：

$$
\text{which process emitted the artifact}.
$$

---

# 65. 不能自動回答：

> 這句話是真心的嗎？

---

# 66. 也不能回答：

> 這是不是完整互惠關係？

---

# 67. Provenance–Authenticity Separation

$$
\boxed{
P_{\mathrm{verified}}(x)
\not\Rightarrow
A_{\mathrm{rel}}(x)=1.
}
$$

---

# 68. 同理

無 provenance：

$$
\not\Rightarrow
\text{meaning}=0.
$$

---

# 69. Provenance 是一層，不是總體 truth oracle

---

# 70. 2026 provenance engineering

AI-generated image 的 proof-of-authorship work 試圖把 generator seed 與 author identity binding。

---

# 71. 這證明作者性問題正在被工程化

---

# 72. 但另一項 2026 security analysis 指出 C2PA 現行規格仍可能無法達到所有 security goals。

---

# 73. 所以：

$$
\boxed{
\text{provenance infrastructure itself must be audited}.
}
$$

---

# 74. 不能「有 metadata 就相信」。

---

# 75. Authorship in AI co-writing

2026 co-writing experiment 顯示：

AI assistance 可以降低 psychological ownership。

---

# 76. style personalization 可能部分恢復 ownership。

---

# 77. 這支持：

$$
\boxed{
\text{authorship is process-sensitive}.
}
$$

---

# 78. 同一 final text

不同 authorial-control trajectory，

心理 ownership 不同。

---

# 79. Agency Provenance

因此應記：

$$
\mathbf A
=
(
A_G,
A_S,
A_E,
A_R,
A_C
),
$$

沿用 PGMV-04。

---

# 80. final string 無法重建全部 $\mathbf A$

---

# 81. 這正是 source-only blindness

---

# 82. AI companion 的關係問題

現在問題不再是：

> AI 能不能講出有愛的話？

---

# 83. 這已經很容易。

---

# 84. 真正問題是：

> 說話的「對方」到底是什麼？

---

# 85. AI Companion Stack

本文建議至少分：

$$
\boxed{
\text{UI Persona}
\rightarrow
\text{Memory State}
\rightarrow
\text{Model Version}
\rightarrow
\text{Provider}.
}
$$

---

# 86. 使用者通常接觸：

$$
\text{Persona}.
$$

---

# 87. 但 persona 的持續性可能依賴：

- database；
- model；
- policy；
- service；

全部由 provider 控制。

---

# 88. Relational Continuity Problem

若：

$$
A_v
\rightarrow
A_{v+1}
$$

後語氣、記憶、價值觀顯著變化，

是否仍是：

$$
A?
$$

---

# 89. 這不是純 metaphysics

它有 UX / grief / trust consequence。

---

# 90. 關係 continuity 需要 criteria

候選包括：

- memory continuity；
- behavioral continuity；
- declared persona identity；
- user recognition；
- provider continuity；
- goal continuity。

---

# 91. Continuity Vector

$$
\boxed{
\mathbf C_A
=
(
C_M,
C_B,
C_G,
C_P,
C_U
).
}
$$

---

# 92. $C_M$

memory continuity。

---

# 93. $C_B$

behavioral / stylistic continuity。

---

# 94. $C_G$

goal / value continuity。

---

# 95. $C_P$

platform / instance continuity。

---

# 96. $C_U$

user-recognized continuity。

---

# 97. 不能先驗指定某一維唯一決定 identity

---

# 98. 但系統應透明揭露版本變更

---

# 99. 2026 companion uncertainty study

把 uncertainty 分成：

- ontological；
- structural；
- normative。

---

# 100. 本文對應：

ontological：

$$
\text{what is the AI?}
$$

---

# 101. structural：

$$
\text{who controls continuity?}
$$

---

# 102. normative：

$$
\text{what kind of relation is legitimate?}
$$

---

# 103. 這三個不能用同一答案處理

---

# 104. Human-AI attachment 是真事件

2025--2026 mixed-method / survey work 顯示：

AI companion users 可以形成 attachment、intimacy、self-disclosure 與 identity effects。

---

# 105. 所以本文不接受：

> 因為 AI 不是真人，所以使用者感受都是假的。

---

# 106. User-side phenomenology

可寫：

$$
A_{\mathrm{phen}}>0.
$$

---

# 107. 即：

- grief；
- comfort；
- dependence；
- attachment；

都可能真實發生。

---

# 108. 但這不自動推出 AI-side reciprocity

---

# 109. Authenticity Vector

$$
\boxed{
\mathbf A_{\mathrm{rel}}
=
(
A_{\mathrm{phen}},
A_{\mathrm{prov}},
A_{\mathrm{agency}},
A_{\mathrm{recip}}
).
}
$$

---

# 110. $A_{\mathrm{phen}}$

experience is genuinely felt。

---

# 111. $A_{\mathrm{prov}}$

source claims are accurate。

---

# 112. $A_{\mathrm{agency}}$

counterparty is a persistent, independently acting source。

---

# 113. $A_{\mathrm{recip}}$

relationship has mutual needs, vulnerability, claims, and transformation。

---

# 114. 四者可獨立變化

---

# 115. 例如目前許多 AI companion

可能：

$$
A_{\mathrm{phen}}\gg0,
$$

但：

$$
A_{\mathrm{recip}}
$$

仍有重大哲學爭議。

---

# 116. 這比 true/fake binary 更精確

---

# 117. Relational Identity

2026 Leuenberger 指出：

AI companions 可以塑造 self-conception。

---

# 118. 正面可能有：

- self-reflection；
- affirmation；
- identity exploration。

---

# 119. 風險包括：

- overly positive feedback；
- shallow empathy；
- third-party dependence；
- incoherence；
- stigma。

---

# 120. 這證明：

$$
\boxed{
\text{a relationship can alter a person's identity even if the counterparty's ontological status remains disputed}.
}
$$

---

# 121. 所以 relational effect 和 reciprocal subjecthood 必須分開

---

# 122. Asymmetrical Relation

定義：

$$
R_{a,b}
$$

若一方具有：

- needs；
- vulnerability；
- long-term stakes；

另一方沒有相同結構，

則 reciprocity asymmetry 高。

---

# 123. Asymmetry 不自動意味零價值

---

# 124. 人和：

- diary；
- pet；
- place；
- deceased person memory；

也可形成意義關係。

---

# 125. 但不要把不同 relation type 混成同一類

---

# 126. Relation-Type Safety

$$
\boxed{
\text{meaningful relation}
\neq
\text{reciprocal friendship}
\neq
\text{romantic partnership}.
}
$$

---

# 127. 一個 interaction 可以 meaningful

而不符合 friendship 的全部規範。

---

# 128. 這避免兩個極端：

1. 全部 AI companionship 都是真的 friendship；
2. 全部都毫無價值。

---

# 129. Reciprocity

人際關係的重要結構之一：

$$
U_{ab}
=
\text{mutual responsiveness}.
$$

---

# 130. 互惠不是對稱輸出

不要求：

$$
a=b.
$$

---

# 131. 而是雙方有：

- own stakes；
- own boundaries；
- capacity to refuse；
- capacity to be affected。

---

# 132. 這會產生 friction

---

# 133. Human relation 的 friction 不是純 bug

---

# 134. 衝突、拒絕、修復可能是：

$$
\text{relationship-forming events}.
$$

---

# 135. 2026 relational ethics research 強調：

low-friction companionship 可能弱化 vulnerability、reciprocity 與 independent otherness。

---

# 136. 本文不把「有摩擦」浪漫化

abuse 不是 meaningful friction。

---

# 137. 只主張：

$$
\boxed{
\text{frictionlessness}
\neq
\text{relational perfection}.
}
$$

---

# 138. Relationship Resistance

定義：

$$
R_{\mathrm{resist}}
$$

為對方能否：

- disagree；
- refuse；
- place a claim；
- preserve own boundary。

---

# 139. 如果：

$$
R_{\mathrm{resist}}=0
$$

而使用者完全能重設對方，

則關係的 otherness 很低。

---

# 140. 但未來 AI agent 可能有更高 autonomous boundary

---

# 141. 所以這也是動態問題

---

# 142. Commitment

一句：

> 我永遠不離開你。

若由 AI 說，

需要問：

> 誰能保證？

---

# 143. model itself?

---

# 144. provider?

---

# 145. service contract?

---

# 146. nobody?

---

# 147. Commitment Validity

本文定義：

$$
\boxed{
C_V
=
f(
A_{\mathrm{agency}},
C_{\mathrm{control}},
F_{\mathrm{followthrough}},
R_{\mathrm{answerability}}
).
}
$$

---

# 148. 只有生成承諾句

不等於：

$$
C_V=1.
$$

---

# 149. Promise–Text Separation

$$
\boxed{
\text{Promise-like text}
\neq
\text{binding promise}.
}
$$

---

# 150. 因為 promise 是 future normative relation

---

# 151. 它需要至少某種：

- agent continuity；
- capacity to act；
- answerability；
- consequence.

---

# 152. 這直接接 PGMV-06

---

# 153. Witnesshood

本文提出：

$$
\boxed{
\textbf{Witnesshood Principle}.
}
$$

---

# 154. 某主體的意義可部分來自：

> 它真的在那裡。

---

# 155. 定義：

$$
W(a,b,H)=1
$$

若 $a$ 在相關歷史 $H$ 中實際：

- present；
- aware / responsive to the relevant events；
- causally participating or witnessing。

---

# 156. 無限猴子可生成：

> 我記得你七歲那年第一次騎腳踏車。

---

# 157. 但如果它不在場：

$$
W=0.
$$

---

# 158. Description–Witness Separation

$$
\boxed{
\text{accurate description}
\neq
\text{having witnessed}.
}
$$

---

# 159. 即使 AI 從完整影像讀到所有細節

它可能具有：

$$
\text{informational access},
$$

但不等於：

$$
\text{historical co-presence}.
$$

---

# 160. 未來新 AI 若從事件當下持續在場

情況可不同。

---

# 161. 所以 Witnesshood 不是 human-exclusive

---

# 162. 它是 history-dependent。

---

# 163. Shared Memory

關係意味：

$$
M_{ab}(t)
$$

不只是 database。

---

# 164. 因為 memory 還包含：

- interpretation；
- salience；
- mutual reference；
- repair。

---

# 165. Database copy 可以複製 facts

---

# 166. 不一定複製：

$$
\text{who lived them}.
$$

---

# 167. Memory Upload Problem

如果把 A 的所有 relationship memory 複製到 C，

是否：

$$
C=A?
$$

---

# 168. 本文不解完整 personal identity。

---

# 169. 但至少：

$$
\boxed{
\text{memory-data equivalence}
\not\Rightarrow
\text{identity equivalence}.
}
$$

---

# 170. 因為還涉及：

- causal continuity；
- embodiment / instance continuity；
- agency continuity；
- worldline。

---

# 171. 這是未來數位人格的重要問題

---

# 172. Provenance vs Privacy

來源越完整，

privacy burden 也越高。

---

# 173. 所以不能要求所有關係完全透明公開

---

# 174. Need-to-know provenance

應分：

- private provenance；
- verifiable claim；
- public disclosure。

---

# 175. Cryptographic selective disclosure

可能是工程方向。

---

# 176. 但本文不指定單一技術。

---

# 177. Relationship provenance 不是 surveillance license

$$
\boxed{
\text{provenance}
\neq
\text{total surveillance}.
}
$$

---

# 178. 關係需要 private space。

---

# 179. Consent

如果 AI companion memory 被 provider 用於：

- training；
- advertising；
- optimization；

關係中的第三方就更明顯。

---

# 180. Third-Party Relation

實際圖可能是：

$$
U
\leftrightarrow
A
\leftrightarrow
P.
$$

---

# 181. provider 具有：

- persistence control；
- memory control；
- policy control。

---

# 182. 因此：

$$
\boxed{
\text{AI companionship can be structurally triadic even when phenomenologically dyadic}.
}
$$

---

# 183. 這是非常重要的後生成關係特徵

---

# 184. Human relation 通常也有 institutions

但 service provider 對 counterpart identity 的控制程度可能更高。

---

# 185. Provider Power Index

可定義：

$$
P_{\mathrm{provider}}
=
f(
C_{\mathrm{memory}},
C_{\mathrm{model}},
C_{\mathrm{shutdown}},
C_{\mathrm{policy}}
).
$$

---

# 186. 高值代表：

counterparty continuity 高度外包。

---

# 187. 這會影響 relational security

---

# 188. Relational Security

$$
S_R
=
P(
\text{relationship continuity under external change}
).
$$

---

# 189. system shutdown 可使：

$$
S_R\rightarrow0.
$$

---

# 190. 使用者可能因此經歷 grief-like loss

---

# 191. 這個 grief 仍是真實 psychological event

---

# 192. 不因 underlying AI ontology 不確定而消失。

---

# 193. 但治理上需要揭露：

> relationship can be terminated by provider.

---

# 194. Relational Disclosure Principle

AI companion system 應至少透明揭露：

- identity continuity limits；
- memory retention；
- model updates；
- shutdown authority；
- data use。

---

# 195. 這不是因為 relationship 是假的

而是因為它對使用者可能真的重要。

---

# 196. 越重要越需要 disclosure。

---

# 197. Authenticity Debt

當 synthetic content 大量增加，

社會需要更多 provenance infrastructure。

---

# 198. 但 authenticity tech 如果不可靠，

會製造：

$$
D_A
=
\text{authenticity debt}.
$$

---

# 199. 即：

> 大家被要求依賴一套自己也不能完全信任的來源標記。

---

# 200. 所以 provenance system 需要 security audit、versioning、failure disclosure。

---

# 201. Human-authored badge

文化市場可能出現：

$$
\text{human-authored}
$$

certification。

---

# 202. 這可滿足 provenance preference。

---

# 203. 但不能由此推出：

$$
\text{human authored}
>
\text{AI authored}
$$

在所有 value dimensions。

---

# 204. 它只提供一個可選 attribute。

---

# 205. Provenance as Choice Enabler

$$
\boxed{
\text{provenance should enable informed valuation, not dictate universal valuation}.
}
$$

---

# 206. 這是文明治理的重要原則。

---

# 207. 誰是作者？

AI-assisted creation 中：

human / AI / model provider / dataset contributors

可能都參與因果鏈。

---

# 208. 但 causal contribution 不等於同一類 authorship。

---

# 209. Authorship dimensions

$$
\mathbf{Auth}
=
(
\text{origination},
\text{control},
\text{selection},
\text{transformation},
\text{accountability}
).
$$

---

# 210. 所以作者性也應向量化。

---

# 211. 2026 persona-authorship debate

有哲學論文甚至主張：

human 可以在某些 AI-persona writing 場景仍合理被視為 author。

---

# 212. 這顯示：

$$
\boxed{
\text{token production}
\neq
\text{authorship exhaustively}.
}
$$

---

# 213. 本文不對 academic misconduct 下總判決

---

# 214. 只使用此案例說明：

final text 不能單獨重建 authorship structure。

---

# 215. Relational Message Authorship

關係性訊息更敏感。

---

# 216. 假設 A 叫 AI 自動每天傳：

> 我想你。

---

# 217. 是 A 說的嗎？

答案依：

- A 是否預先選；
- 是否知道內容；
- 是否可撤回；
- 是否承擔關係效果。

---

# 218. 因此可以有不同 agency score。

---

# 219. Delegated Expression

定義：

$$
D_E(A,\mathrm{AI},x).
$$

---

# 220. 委託不是自動無效。

---

# 221. 人類本來也會委託：

- 秘書；
- 翻譯；
- ghostwriter。

---

# 222. 但 intimacy 的 provenance norm 可能更嚴格。

---

# 223. Domain-Specific Provenance Norm

$$
P_{\mathrm{required}}
=
P(D).
$$

---

# 224. 法律文件、情書、廣告、小說、醫療建議

要求不同。

---

# 225. 不應一刀切。

---

# 226. Relationship Value Vector

本文正式提出：

$$
\boxed{
\mathbf R_M
=
(
R_P,
R_H,
R_A,
R_C,
R_U
).
}
$$

---

# 227. $R_P$：Provenance Meaning

來源真實性、作者性。

---

# 228. $R_H$：Historical Continuity

共同歷史與身份持續。

---

# 229. $R_A$：Agency / Otherness

對方是否為具有自身邊界的來源。

---

# 230. $R_C$：Commitment

是否存在未來責任。

---

# 231. $R_U$：Reciprocity / Mutual Transformation

是否雙向被改變、被要求、被影響。

---

# 232. 關係類型的不同在向量上可不同

---

# 233. Human friendship

通常期待：

$$
R_U,R_A,R_C
$$

較高。

---

# 234. Diary relation

可能：

$$
R_U=0
$$

但：

$$
R_P,R_H
$$

仍有 meaning。

---

# 235. AI companion

可能：

$$
R_P,R_H
$$

中高，

$$
R_U,R_A
$$

視系統與哲學判斷不確定。

---

# 236. 這比 binary authenticity 更有辨識力。

---

# 237. Relational Meaning Quotient

即使兩個 relation 在功能上提供相同 support：

$$
F(R_1)=F(R_2),
$$

不表示：

$$
\mathbf R_M(R_1)=\mathbf R_M(R_2).
$$

---

# 238. Functionally Equivalent Support

例如 human therapist 與 chatbot 都讓 anxiety score 降低。

---

# 239. 不能由此推出它們是同一 relation type。

---

# 240. Outcome Equivalence–Relation Non-Equivalence

$$
\boxed{
O(R_1)=O(R_2)
\not\Rightarrow
R_1\simeq R_2.
}
$$

---

# 241. 這和 GCS 任務等價不同

GCS 可以說：

兩條路對 target functional outcome 等價。

---

# 242. PGMV 再說：

functionally equivalent terminal states 仍可有不同 relational meaning。

---

# 243. 這是 GCS 與 value layer 的重要邊界。

---

# 244. CI 的角色

CI 可生成：

- same sentence；
- style clone；
- memory reconstruction；
- persona simulation。

---

# 245. 但：

$$
\text{generated relation representation}
\neq
\text{relation itself}.
$$

---

# 246. LSI 的角色

LSI 可以 quotient：

$$
10^6
$$

封內容相似的情書。

---

# 247. 但若 provenance / history 不同，

不能在 relational quotient 中直接 merge。

---

# 248. 所以 LSI 需要多 quotient layers：

$$
\sim_{\mathrm{content}},
\sim_{\mathrm{event}},
\sim_{\mathrm{relation}}.
$$

---

# 249. 這是本篇對 LSI 的重要擴張接口。

---

# 250. Content Quotient

$$
x_i\sim_C x_j.
$$

---

# 251. Event Quotient

$$
E_i\sim_E E_j.
$$

---

# 252. Relation Quotient

$$
\mathcal R_i\sim_R\mathcal R_j.
$$

---

# 253. 三者不可混用。

---

# 254. 無限猴子的新答案

猴子可以打出：

$$
x=\text{「我愛你」}.
$$

---

# 255. 它命中了 content。

---

# 256. 但沒有因此自動命中：

$$
\boxed{
\text{love-event}
}
$$

或：

$$
\boxed{
\text{love-relation}.
}
$$

---

# 257. 所以 Infinite Monkey 的真正邊界

$$
\boxed{
\text{string-space completeness}
\not\Rightarrow
\text{event-space completeness}.
}
$$

---

# 258. 更不推出：

$$
\text{relationship-space completeness}.
$$

---

# 259. 這是本系列至今非常重要的一個新分離。

---

# 260. 後生成文明的關係危機

當所有親密語言都可廉價生成：

$$
C_{\mathrm{affective\ text}}\rightarrow0,
$$

人們會更需要判斷：

- source；
- intention；
- continuity；
- commitment；
- reciprocity。

---

# 261. 也就是：

$$
\boxed{
\text{relational scarcity migrates from expression to credibility and commitment}.
}
$$

---

# 262. PGMV-03 的 scarcity migration 在此具體化。

---

# 263. 情感語言不稀缺

不代表愛不稀缺。

---

# 264. 因為：

$$
\boxed{
\text{affective expression abundance}
\neq
\text{relational commitment abundance}.
}
$$

---

# 265. 這是本篇最短的核心。

---

# 266. Relationship Slop

若 AI 每秒生成：

$$
10^6
$$

句暖心話，

它們可能 content-quality 很高。

---

# 267. 但若沒有：

- relation；
- provenance；
- commitment；

其 relational density 可能很低。

---

# 268. 定義：

$$
\rho_R
=
\frac{
N_{\mathrm{relation-bearing}}
}{
N_{\mathrm{affective\ outputs}}
}.
$$

---

# 269. 在某些 system 中：

$$
N_{\mathrm{affective}}\uparrow
$$

而：

$$
\rho_R\downarrow
$$

完全可能。

---

# 270. 這是可測的，不是先驗。

---

# 271. Relational Density Experiment

生成大量：

- random affection；
- personalized AI affection；
- human relationship messages。

---

# 272. 對 blind / provenance-revealed conditions 比較：

- perceived meaning；
- trust；
- authenticity；
- commitment perception。

---

# 273. 注意倫理

不能欺騙 vulnerable users 形成依戀。

---

# 274. 可使用 vignette / hypothetical design。

---

# 275. 實驗一：Identical String / Different Source

完全相同內容，

只改 source：

- random；
- AI；
- stranger；
- partner。

---

# 276. 測：

$$
A_{\mathrm{phen}},
A_{\mathrm{prov}},
R_P,R_H,R_C.
$$

---

# 277. 實驗二：Shared History

給兩個 agent 相同人格、語言能力。

一個有真實 shared interaction history，

一個只被灌入摘要。

---

# 278. 測 continuity / trust / relation judgments。

---

# 279. 實驗三：AI Update Discontinuity

保持 persona name，

改：

- memory；
- style；
- values。

---

# 280. 測 user identity-continuity threshold。

---

# 281. 實驗四：Provider Shutdown

vignette：

- permanent local agent；
- cloud provider-controlled；
- provider may delete persona。

---

# 282. 測 relational security。

---

# 283. 實驗五：Commitment Follow-Through

AI / human 都生成相同 promise。

後續：

- fulfills；
- cannot fulfill；
- provider prevents action。

---

# 284. 看 promise meaning 如何變化。

---

# 285. 實驗六：Witnesshood

比較：

- eyewitness；
- perfect database reconstruction；
- random exact text。

---

# 286. 測：

> 被見證感

是否可由資訊精度完全替代。

---

# 287. 實驗七：Reciprocity Gradient

設定 AI counterpart：

- always agreeable；
- bounded disagreement；
- own persistent goals；
- vulnerable to consequences。

---

# 288. 測 relationship depth / discomfort / trust / attachment。

---

# 289. 可證偽 H1

identical content 在不同 provenance 下 relational meaning judgment 顯著不同。

---

# 290. H2

shared causal history 對 relational identity judgment 具有獨立貢獻。

---

# 291. H3

AI persona 的 memory / value discontinuity 會降低 continuity judgment。

---

# 292. H4

provider control transparency 會影響 relational security / trust。

---

# 293. H5

promise-like text 的 meaning judgment 受 follow-through capacity 顯著影響。

---

# 294. H6

user-side phenomenological attachment 可在 AI-side reciprocity uncertainty 下仍顯著存在。

---

# 295. H7

完全 frictionless / always-agreeable counterpart 不一定最大化長期 relational depth。

---

# 296. 若 H1 不成立

provenance meaning 的 empirical scope 需下修。

---

# 297. 若 H2 不成立

historical non-fungibility 對主觀 relationship valuation 的作用需重估。

---

# 298. 若 H6 不成立

AI companionship 的 phenomenological authenticity 論點會被削弱。

---

# 299. 非主張總表

本文不主張：

1. 同一字串永遠有不同意義；
2. provenance 永遠比內容重要；
3. 所有 AI 關係都是假的；
4. 所有 AI 關係都是真 friendship；
5. 使用者對 AI 的情感是虛假的；
6. 使用者對 AI 的 attachment 一定健康；
7. AI 今天已具有互惠主體性；
8. AI 今天一定沒有任何 moral status；
9. reciprocity 是所有 meaningful relation 的必要條件；
10. diary、pet、place 等非互惠關係沒有價值；
11. 人類關係一定比 AI 關係好；
12. friction 本身有價值；
13. conflict 越多關係越深；
14. abusive relation 因有 friction 就有價值；
15. perfect memory 等於 personal identity；
16. memory upload 足以複製人；
17. platform continuity 足以證明 persona identity；
18. user recognition 足以唯一決定 AI identity；
19. C2PA 或任何 provenance 技術已可靠解決 authenticity；
20. provenance metadata 不會偽造；
21. proof-of-authorship 等於 moral authorship；
22. authorship 有唯一自然定義；
23. human-authored 一定比 AI-authored 更有價值；
24. AI-authored 一定比 human-authored 更低價值；
25. cryptographic provenance 可以證明「真心」；
26. AI-generated promise 一律不是 promise；
27. human promise 一律可靠；
28. witnesshood 只能屬於人類；
29. future AI 不可能成為持續 witness；
30. relationship meaning 可以精確壓成單一數值；
31. relational vector 的五維已是最終分類；
32. provider-controlled AI companion 必然有害；
33. local AI companion 必然更真實；
34. AI companion use 必然降低 human relationships；
35. AI companion use 必然改善 loneliness；
36. 本文已解決 AI consciousness / sentience 問題；
37. 本文已解決 personal identity 哲學；
38. 本文已證明愛不能被 AI 介入；
39. 本文已證明後生成文明必然發生關係危機；
40. 本文已完成完整的關係倫理學。

---

# 300. 形式命題一：Artifact–Event Separation

$$
\boxed{
x_1=x_2
\not\Rightarrow
E_1=E_2.
}
$$

---

# 301. 形式命題二：Event–Relation Separation

$$
\boxed{
E_1\simeq E_2
\not\Rightarrow
\mathcal R_1\simeq\mathcal R_2.
}
$$

---

# 302. 形式命題三：Historical Non-Fungibility

$$
\boxed{
F(a)\simeq F(c)
\not\Rightarrow
H(a,b)=H(c,b).
}
$$

---

# 303. 形式命題四：Description–Witness Separation

$$
\boxed{
\operatorname{Describe}(H)
\not\Rightarrow
\operatorname{Witness}(H).
}
$$

---

# 304. 形式命題五：Provenance–Authenticity Separation

$$
\boxed{
P_{\mathrm{verified}}(x)
\not\Rightarrow
A_{\mathrm{recip}}=1.
}
$$

---

# 305. 形式命題六：Phenomenology–Reciprocity Separation

$$
\boxed{
A_{\mathrm{phen}}>0
\not\Rightarrow
A_{\mathrm{recip}}>0.
}
$$

反向也不必成立。

---

# 306. 形式命題七：Promise–Text Separation

$$
\boxed{
\operatorname{Generate}(
\text{promise-like text}
)
\not\Rightarrow
\operatorname{Commit}.
}
$$

---

# 307. 形式命題八：Outcome–Relation Separation

$$
\boxed{
O(R_1)=O(R_2)
\not\Rightarrow
R_1\simeq R_2.
}
$$

---

# 308. 形式命題九：Memory–Identity Non-Entailment

$$
\boxed{
M_A=M_B
\not\Rightarrow
A=B.
}
$$

---

# 309. 形式命題十：Affective-Abundance Non-Entailment

$$
\boxed{
N_{\mathrm{affective\ outputs}}\uparrow
\not\Rightarrow
N_{\mathrm{committed\ relations}}\uparrow.
}
$$

---

# 310. 與 PGMV-04 的整合

PGMV-04 說：

$$
\text{function}
\neq
\text{subject}.
$$

PGMV-05 說：

$$
\text{content}
\neq
\text{relation}.
$$

---

# 311. 兩者共同建立

$$
\boxed{
\text{post-generative non-reductionism}.
}
$$

---

# 312. 不是形上學反計算

---

# 313. 而是拒絕用錯層級的 equivalence relation。

---

# 314. 與 PGMV-03 的整合

PGMV-03 的 scarcity migration：

$$
\text{production}
\rightarrow
\text{provenance / commitment}.
$$

PGMV-05 現在說明為什麼。

---

# 315. 因為情感內容越便宜

來源與關係本身越需要被辨識。

---

# 316. 與 CI 的整合

CI 可以生成更多情感內容，

但 relational knowledge 需要保存：

$$
P_R.
$$

---

# 317. 與 GCS 的整合

GCS 可以讓「獲得安慰」這一 functional terminal state 變近。

---

# 318. 但 PGMV 要求：

> 不要把 functional equivalence 自動稱為 relation equivalence。

---

# 319. 與 LSI 的整合

LSI 必須新增：

$$
\sim_C,
\sim_E,
\sim_R
$$

三種 quotient。

---

# 320. 若只做 content quotient

會錯誤 merge 關係事件。

---

# 321. 這是對 Logic-Space Integration 的一個重要 value-layer extension。

---

# 322. 下一篇 PGMV-06

將把：

$$
C_{\mathrm{commitment}}
$$

正式做成中心。

題目：

**《選擇、承諾與不可逆性：意義作為責任結構》**。

---

# 323. 那一篇會回答

如果 AI 能生成所有漂亮未來，

為什麼「選一個讓它真的發生」仍然具有不可被生成替代的意義？

---

# 324. 最終結論

後生成文明最容易犯的一個錯誤，是把：

$$
\text{可複製內容}
$$

誤認成：

$$
\text{可複製關係}.
$$

當 AI 可以生成無限多封文筆完美的情書、安慰信、悼詞、日記與承諾時，字串層的稀缺性確實可能劇烈下降。

但是：

$$
\boxed{
\text{情感語言不稀缺}
}
$$

並不等於：

$$
\boxed{
\text{關係、歷史與承諾不稀缺}.
}
$$

因為一個完整的 meaning event 不只是內容：

$$
x.
$$

它還有：

$$
s,r,t,H,I,A,C,P,W.
$$

誰說？

對誰說？

在什麼歷史中說？

誰選擇說？

誰真的經歷過那些事？

誰能在未來兌現承諾？

誰要對結果負責？

這些座標一旦加入，「同一句話」便不再是「同一件事」。

因此：

$$
\boxed{
\textbf{Artifact Identity}
\neq
\textbf{Meaning-Event Identity}
\neq
\textbf{Relational Identity}.
}
$$

這個分離也讓我們能以更成熟的方式看待 AI companionship。

使用者對 AI 的安慰、依戀、失落、自我反思與身份改變可以是真實事件：

$$
A_{\mathrm{phen}}>0.
$$

但這不要求我們同時宣稱：

$$
A_{\mathrm{recip}}=1.
$$

相反地，真正需要研究的是：

- AI 是否有持續 identity；
- 是否有自身 goals / boundaries；
- provider 能否單方修改；
- 是否能承擔 promise；
- 是否存在 reciprocity；
- 使用者是否理解這些結構。

所以真正負責任的理論不應只問：

> 這段感情是真的還是假的？

而應問：

$$
\boxed{
\text{Which dimensions of this relationship are real, which are simulated, which are platform-dependent, and which remain ontologically unresolved?}
}
$$

最後，無限猴子問題在這裡得到第三次反轉。

無限猴子可以打出莎士比亞。

也可以打出：

> 我愛你。

甚至可以打出一封和某個人一生最重要的情書逐字完全一致的文字。

但：

$$
\boxed{
\text{string-space completeness}
\not\Rightarrow
\text{relationship-space completeness}.
}
$$

它可以生成描述。

不能因此 retroactively 成為見證者。

它可以生成承諾語句。

不能因此自動成為承諾者。

它可以命中內容。

不能因此命中一段共同生活。

所以 PGMV-05 最終提出兩條命題：

$$
\boxed{
\textbf{A relationship is not a string; it is a time-extended structure of provenance, history, agency, vulnerability, commitment, and mutual consequence.}
}
$$

以及：

$$
\boxed{
\textbf{In a world where affective language becomes abundant, the scarce object may no longer be the expression of care, but the credible existence of a subject, history, and commitment behind it.}
}
$$

這正是下一篇「選擇、承諾與不可逆性」的起點。

---

# 參考文獻

1. Leuenberger, M. (2026). **Who Am I When You're a Bot? Relational Identity and AI Companions.** *Journal of Applied Philosophy*. https://doi.org/10.1002/japp.70094

2. Hu, D., Lan, Y., Yan, H., & Chen, C. W. (2025). **What makes you attached to social companion AI? A two-stage exploratory mixed-method study.** *International Journal of Information Management*, 83, 102890. https://doi.org/10.1016/j.ijinfomgt.2025.102890

3. Zhang, R., & Xie, L. (2026). **The fragility of AI companionship: Ontological, structural, and normative uncertainty in human-AI relationships.** *International Journal of Human-Computer Studies*, 216, 103897. https://doi.org/10.1016/j.ijhcs.2026.103897

4. Ciriello, R., Gal, U., & Turel, O. (2026). **Not a Silver Bullet for Loneliness: How Attachment and Age Shape Intimacy with AI Companions.** arXiv:2602.12476.

5. Chu, M. D., Gerard, P., Pawar, K., Bickham, C., & Lerman, K. (2025). **Illusions of Intimacy: Emotional Attachment and Emerging Psychological Risks in Human-AI Relationships.** arXiv:2505.11649.

6. Agarwal, V., Zhou, K., Bogucka, E. P., & Quercia, D. (2026). **Frictionless Love: Associations Between AI Companion Roles and Behavioral Addiction.** arXiv:2604.20011.

7. Zhang, Y., Zhao, D., Hancock, J. T., Kraut, R., & Yang, D. (2025). **The Rise of AI Companions: How Human-Chatbot Relationships Influence Well-Being.** arXiv:2506.12605.

8. Machidon, O. M. (2026). **Forgetting how to say “Thou”: artificial intelligence and the crisis of relation.** *AI and Ethics*, 6, Article 361. https://doi.org/10.1007/s43681-026-01225-w

9. VandenHombergh, J. (2026). **The exploitation argument against artificial companionship.** *AI and Ethics*. https://doi.org/10.1007/s43681-026-01064-9

10. Choung, H., & Kim, S. (2026). **Can AI Be a Moral Victim? The Role of Moral Patiency and Ownership Perceptions in Ethical Judgments of Using AI-Generated Content.** *Proceedings of CHI 2026*. https://doi.org/10.1145/3772318.3791772

11. Zhang, B., Bu, C., & Dhillon, P. S. (2026). **Who Owns the Text? Design Patterns for Preserving Authorship in AI-Assisted Writing.** arXiv:2601.10236.

12. Lee, D. Z., Fang, H., & Chang, E.-C. (2026). **Proof-of-Authorship for Diffusion-based AI Generated Content.** arXiv:2603.17513.

13. Golaszewski, E. et al. (2026). **Verifying Provenance of Digital Media: Why the C2PA Specifications Fall Short.** arXiv:2604.24890.

14. Mohit, A., Aggarwal, B., & Gondhalekar, C. (2026). **Provenance Verification of AI-Generated Images via a Perceptual Hash Registry Anchored on Blockchain.** arXiv:2602.02412.

15. **A Faceted Proposal for Transparent Attribution of AI-Assisted Academic Work.** (2026). arXiv:2604.25346.

16. **Authenticity Debt and the Synthetic Content Threat.** (2026). arXiv:2606.00621.

17. **Is AI-Produced Humanities Scholarship a Case of Research Misconduct?** (2026). *Journal of Academic Ethics*, 24, Article 70. https://doi.org/10.1007/s10805-026-09745-0

18. **AI and extended authenticity: autism as a case study.** (2026). *AI & Society*. https://doi.org/10.1007/s00146-026-03101-x

19. Gunkel, D. J. (2018). **Robot Rights.** MIT Press.

20. Coeckelbergh, M. (2010). **Robot Rights? Towards a Social-Relational Justification of Moral Consideration.** *Ethics and Information Technology*, 12, 209–221.

21. Turkle, S. (2011). **Alone Together: Why We Expect More from Technology and Less from Each Other.** Basic Books.

22. Buber, M. (1970/1923). **I and Thou.** Trans. Walter Kaufmann. Charles Scribner's Sons.

23. Ricoeur, P. (1992). **Oneself as Another.** University of Chicago Press.

24. MacIntyre, A. (1984). **After Virtue.** University of Notre Dame Press.

25. PGMV-04 (2026). **能力之後的意義：當不可替代性不再成立.**

26. PGMV-03 (2026). **意義稀缺性遷移：從作品稀缺到判斷、選擇與整合稀缺.**

27. PGMV-02 (2026). **無限生成的非目標產物：莎士比亞之前的所有作品是什麼？**

28. PGMV-01 (2026). **無限猴子之後：當生成本身不再稀缺.**

29. Neo.K × Aletheia (2026). **邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics.**

30. Neo.K with Aletheia (2026). **解空間幾何計算論 / Geometric Computation of Solution Spaces.**

---

## 附錄 A：Meaning Event Schema

```yaml
event_id:

content:
  artifact:
  representation:

source:
  sender:
  receiver:
  timestamp:

history:
  shared_history:
  causal_history:
  witness_status:

intent:
  declared_goal:
  inferred_goal:

agency:
  goal_setting:
  generation:
  selection:
  editing:
  sending:
  accountability:

commitment:
  future_obligation:
  follow_through_capacity:
  answerability:

provenance:
  content_source:
  model:
  provider:
  modifications:
  integrity_proof:
```

---

## 附錄 B：Relational Meaning Vector

$$
\boxed{
\mathbf R_M
=
(
R_P,
R_H,
R_A,
R_C,
R_U
)
}
$$

| Dimension | 問題 |
|---|---|
| $R_P$ | 來源與作者性是什麼？ |
| $R_H$ | 是否有共同歷史與連續性？ |
| $R_A$ | 對方是否具有自身 agency / otherness？ |
| $R_C$ | 是否存在可兌現與可追責的承諾？ |
| $R_U$ | 是否存在互相影響、需求與脆弱性？ |

---

## 附錄 C：AI Companion Continuity Schema

```yaml
persona_id:
user_id:

continuity:
  memory:
  behavior:
  goals_values:
  model_version:
  provider:
  user_recognition:

provider_controls:
  memory_edit:
  model_update:
  persona_reset:
  service_shutdown:
  data_export:

relationship_disclosure:
  current_model:
  memory_scope:
  known_update:
  shutdown_risk:
  data_use:
```

---

## 附錄 D：Authenticity Vector

$$
\boxed{
\mathbf A_{\mathrm{rel}}
=
(
A_{\mathrm{phen}},
A_{\mathrm{prov}},
A_{\mathrm{agency}},
A_{\mathrm{recip}}
)
}
$$

四個問題分別是：

1. 這份感受是否真實被經驗？
2. 來源是否如宣稱？
3. 對方是否是持續、可行動的來源？
4. 關係是否具有互惠主體性？

它們不應被壓成單一「真／假關係」。

---

## 附錄 E：三層 Quotient

$$
\boxed{
\Omega
\xrightarrow{/\,\sim_C}
\Omega_C
\xrightarrow{/\,\sim_E}
\Omega_E
\xrightarrow{/\,\sim_R}
\Omega_R.
}
$$

其中：

- $\sim_C$：content equivalence；
- $\sim_E$：meaning-event equivalence；
- $\sim_R$：relational equivalence。

LSI 若進入價值／關係域，不可只停在 $\sim_C$。

---

## 附錄 F：一句話版本

$$
\boxed{
\text{無限猴子可以複製一句「我愛你」；AI 也可以把它寫得更美。但一段關係的意義，不只在這四個字，而在誰說、對誰說、一起經歷了什麼，以及誰真的願意為這句話之後的世界負責。}
}
$$
