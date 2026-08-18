# UFI-04 — 競爭智能棘輪：為什麼「AI 夠用了，大家一起停」不是自然均衡

## The Competitive Intelligence Ratchet: Why “AI Is Good Enough, So Everyone Stops” Is Not a Natural Equilibrium

**系列：** 不可凍結的智能：AI 工具終局論、競爭棘輪與後人類轉型  
**English Series:** *The Unfreezable Intelligence: Tool-Finality, Competitive Ratchets, and the Posthuman Transition*  
**系列代碼：** UFI  
**論文序號：** 04 / 08  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-18  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** UFI-01—03；PGMV；後人類奇點前夜；國際 AI 治理與驗證研究  
**文件地位：** Game-Theoretic / Political-Economic / Geopolitical Ratchet Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文不主張全球 AI 能力凍結在邏輯上或政治上絕對不可能，也不主張國際合作注定失敗。2025–2026 年的 frontier-AI governance 文獻已提出多種 treaty、compute monitoring、hardware attestation、model evaluation、whistleblower、audit 與多層驗證機制；2026 年美中亦已進入更正式的 AI 對話安排。本文提出的較弱命題是：**只要更強 AI 能帶來顯著相對經濟、軍事、科研、產業、資安或政治紅利，而違約可被隱蔽、延遲發現或只受到有限懲罰，永久、全面、自願的能力凍結就不會自動成為 self-enforcing equilibrium。要讓它穩定，必須透過驗證、制裁、共享利益、風險共識、chokepoint governance 與持續制度更新，主動改寫參與者的 payoff structure。**

---

## 摘要

UFI-01—03 已經完成第一條技術能力線：

$$
\boxed{
\text{Jaggedness is a state}
}
$$

$$
\boxed{
\text{Substrate update geometries differ}
}
$$

$$
\boxed{
\text{Complementarity frontier can move}.
}
$$

這立刻產生一個看似直觀的治理方案：

> 如果 AI 最終已經足夠好用，能大幅改善人類生活，但又開始威脅人類的能力地位，那就由國家、企業與社會共同下令：**從今天開始，不准再把 AI 變得更強。**

這個想法可寫成：

$$
\boxed{
\textbf{Naive Capability Freeze}
}
$$

其假設鏈為：

$$
\boxed{
\text{AI is useful enough}
\rightarrow
\text{collective decision to stop}
\rightarrow
\text{all major actors comply}
\rightarrow
\text{capability remains fixed}.
}
$$

本文的核心不是否定第二步：

$$
\text{collective decision to stop}.
$$

真正問題是：

$$
\boxed{
\text{collective decision}
\not\Rightarrow
\text{self-enforcing compliance}.
}
$$

令 actor 集合：

$$
\boxed{
\mathcal A
=
\{
a_1,\ldots,a_n
\}
}
$$

包含：

- states；
- frontier labs；
- cloud providers；
- semiconductor firms；
- military / intelligence organizations；
- universities；
- open-weight communities；
- smaller states；
- future new entrants。

每個 actor 在最簡模型中選：

$$
\boxed{
a_i
\in
\{
H,A
\},
}
$$

其中：

$$
H=\text{Halt},
\qquad
A=\text{Advance}.
$$

若所有其他 actor 都停止：

$$
a_{-i}=H,
$$

但 actor $i$ 偷偷或公開繼續提升 AI 所獲得的：

$$
\boxed{
B_i
=
B_{\mathrm{economic}}
+
B_{\mathrm{military}}
+
B_{\mathrm{scientific}}
+
B_{\mathrm{industrial}}
+
B_{\mathrm{prestige}}
+
B_{\mathrm{security}}
}
$$

扣除：

$$
\boxed{
C_i
=
C_{\mathrm{research}}
+
P_{\mathrm{detect}}C_{\mathrm{sanction}}
+
C_{\mathrm{risk}}
+
C_{\mathrm{opportunity}}
}
$$

後仍有：

$$
\boxed{
U_i(A,H_{-i})
>
U_i(H,H_{-i}),
}
$$

則：

$$
\boxed{
(H,H,\ldots,H)
}
$$

不是 self-enforcing Nash equilibrium。

本文把：

$$
\boxed{
D_i
=
U_i(A,H_{-i})
-
U_i(H,H_{-i})
}
$$

稱為：

$$
\boxed{
\textbf{Defection Dividend}.
}
$$

中文：

**違約紅利。**

只要：

$$
D_i>0,
$$

單靠共同宣言不足以穩定停止。

這不表示 actor 必然違約。

它表示：

$$
\boxed{
\text{the institution must make compliance strategically preferable}.
}
$$

因此真正的治理條件不是：

> 大家都承諾停。

而是：

$$
\boxed{
P_{\mathrm{detect}}C_{\mathrm{sanction}}
+
B_{\mathrm{cooperation}}
+
C_{\mathrm{shared-risk}}
+
V_{\mathrm{verification}}
>
D_i
}
$$

對高風險 actor 足夠成立。

這就是本文的：

$$
\boxed{
\textbf{Payoff Rewriting Principle}.
}
$$

全球能力凍結若要穩定，不是靠 moral exhortation，而是要改寫：

$$
\boxed{
\text{payoff matrix}.
}
$$

2025–2026 的 verification literature 正沿著這個方向發展。*Verifying International Agreements on AI* 提出六層驗證架構，包含 AI chip 內建安全、外部監測裝置與 personnel-based mechanisms；2026 的 *Verifying Restrictions on Frontier AI Research* 更進一步指出，如果 durable halt 要成立，只限制 compute 不夠，因算法與資料進步可能抵消限制，因而盤點了 28 類研究限制驗證機制。聯合國 2026 年的 *Verification of Frontier AI Models* 也已把 frontier-AI verification 放入全球治理議程。

因此本文提出：

$$
\boxed{
\textbf{Voluntary Global Freeze}
\neq
\textbf{Verified Global Restraint}.
}
$$

前者是意願狀態。

後者是制度狀態。

---

# 一、天真工具終局論的第一個政治漏洞

天真工具終局論假設：

$$
\boxed{
\text{once AI is sufficiently useful, humans can decide it should remain a tool forever}.
}
$$

但這句話偷渡了一個巨大前提：

$$
\boxed{
\text{Humanity}
}
$$

是一個單一 actor。

實際上不是。

---

# 二、全球不是一個玩家

現實 actor 至少包括：

$$
\boxed{
\begin{aligned}
\mathcal A
=&
\{
States,
Companies,
Labs,
Militaries,
Universities,\\
&OpenCommunities,
Investors,
Clouds,
ChipFirms,
NewEntrants
\}.
\end{aligned}
}
$$

不同 actor：

- payoff 不同；
- 風險偏好不同；
- 時間折現不同；
- 國安目標不同；
- 治理能力不同。

---

# 三、Collective Preference–Actor Incentive Separation

即使：

$$
\boxed{
\text{global welfare prefers halt},
}
$$

也不能推出：

$$
\boxed{
\forall i:
U_i(H)>U_i(A).
}
$$

本文稱：

$$
\boxed{
\textbf{Collective Preference–Actor Incentive Separation}.
}
$$

---

# 四、最小二人博弈

兩國：

$$
A,B.
$$

策略：

$$
H,A.
$$

如果雙方 halt：

$$
(H,H)
$$

可降低 catastrophic risk。

但如果：

$$
U_A(A,H)>U_A(H,H)
$$

且對 B 同樣成立，

則形成類似：

- Prisoner’s Dilemma；
- Security Dilemma；
- Arms Race。

但 AI race 不完全等同核軍備競賽。

---

# 五、AI 競賽的特殊性

AI 能力同時具有：

- military utility；
- commercial utility；
- scientific utility；
- civilian utility；
- cyber utility。

核武主要是 strategic weapon。

AI 同時也是 general-purpose technology。

因此：

$$
\boxed{
\text{Capability Restraint Cost}
}
$$

可能比單純武器控制更廣。

---

# 六、Dual-Use Incentive Density

本文定義：

$$
\boxed{
I_D
=
\text{number / value of civilian + military advantages generated by the same capability stack}.
}
$$

AI 的：

$$
I_D
$$

可能非常高。

---

# 七、高 dual-use density 使停止更難

因為 actor 可以說：

> 我不是研發武器，我只是改善醫療／科學／資安／產業。

---

# 八、Purpose Ambiguity

同一：

- model；
- compute cluster；
- algorithm；

可支援多種用途。

本文稱：

$$
\boxed{
\textbf{Purpose Ambiguity}.
}
$$

---

# 九、Capability Security Dilemma

若國家 A 提升 AI 是為：

> 防止 B 取得優勢，

B 會把 A 的提升視為 threat。

於是：

$$
\boxed{
A\uparrow
\Rightarrow
Threat_B\uparrow
\Rightarrow
Investment_B\uparrow.
}
$$

對稱：

$$
\boxed{
B\uparrow
\Rightarrow
Investment_A\uparrow.
}
$$

形成：

$$
\boxed{
\textbf{Capability Security Dilemma}.
}
$$

---

# 十、Defensive Advance Paradox

每一方都可能說：

> 我們只是在防守。

但集體結果：

$$
\boxed{
\sum_i C_i^{AI}\uparrow.
}
$$

本文稱：

$$
\boxed{
\textbf{Defensive Advance Paradox}.
}
$$

---

# 十一、2026 現實已具有競爭結構

美國 2026 官方 AI 政策仍明確將 advanced AI capability 與：

- national security；
- cyber defense；
- global leadership；

連結。

中國 2025–2026 的 AI Plus、industrial internet + AI、global AI cooperation 計畫則持續推動：

- compute；
- industrial integration；
- ecosystem；
- talent；
- core technology。

因此當代主要 actor 的政策目標並不是：

$$
\boxed{
\text{capability saturation}.
}
$$

而仍是：

$$
\boxed{
\text{capability development under governance}.
}
$$

---

# 十二、這不是說政策永遠如此

政治可以改。

---

# 十三、但它說明今天的 payoff 中有正向 capability value

---

# 十四、Competitive Intelligence Ratchet

本文正式定義：

$$
\boxed{
\textbf{Competitive Intelligence Ratchet}
}
$$

簡寫：

$$
\boxed{
CIR.
}
$$

若：

1. 更高 AI capability 帶來相對利益；
2. actor 有可行的能力提升路徑；
3. 領先／落後具有戰略後果；
4. 無可信 enforcement 足以反轉收益；

則：

$$
\boxed{
\text{competitive pressure tends to regenerate capability investment}.
}
$$

---

# 十五、Ratchet 不等於單調進步

CIR 不主張：

$$
C_{AI}(t+1)>C_{AI}(t)
$$

每期成立。

---

# 十六、它主張投資誘因會再生

即使：

- recession；
- regulation；
- accident；

讓進度停一段，

競爭紅利可能重新啟動：

$$
R\&D.
$$

---

# 十七、Investment Ratchet vs Capability Ratchet

$$
\boxed{
\text{Investment Pressure}
\neq
\text{Capability Success}.
}
$$

本文主要先證前者。

---

# 十八、Defection Dividend

$$
D_i
=
U_i(A,H_{-i})-U_i(H,H_{-i}).
$$

---

# 十九、來源 1：經濟

市場：

- productivity；
- platform power；
- exports；
- cost reduction。

---

# 二十、來源 2：軍事

- intelligence；
- cyber；
- logistics；
- targeting；
- autonomy。

---

# 二十一、來源 3：科學

- materials；
- drugs；
- engineering；
- mathematics。

---

# 二十二、來源 4：政治 prestige

2026 *International Affairs* 已研究 AI status / prestige competition。

---

# 二十三、來源 5：防禦

更強 AI 可以被視為抵抗別人 AI 的工具。

---

# 二十四、所以 halt opportunity cost 不是零

---

# 二十五、Sanction-adjusted Defection Dividend

$$
\boxed{
D_i^\star
=
B_i
-
C_{\mathrm{research}}
-
P_{\mathrm{detect}}C_{\mathrm{sanction}}
-
C_{\mathrm{risk}}.
}
$$

---

# 二十六、若：

$$
D_i^\star>0
$$

違約仍具有誘因。

---

# 二十七、Verification 的真正功能

不是 moral truth。

---

# 二十八、是提升：

$$
P_{\mathrm{detect}}.
$$

---

# 二十九、Enforcement 提升：

$$
C_{\mathrm{sanction}}.
$$

---

# 三十、Cooperation benefit 提升：

$$
B_{\mathrm{cooperation}}.
$$

---

# 三十一、Shared risk recognition 提升：

$$
C_{\mathrm{shared-risk}}.
$$

---

# 三十二、所以治理是在改 inequality

目標：

$$
\boxed{
D_i^\star\le0.
}
$$

---

# 三十三、Self-Enforcing Freeze Condition

候選：

$$
\boxed{
U_i(H,H_{-i})
\ge
U_i(A,H_{-i})
}
$$

對所有關鍵 actor 成立。

---

# 三十四、這非常強

因為：

$$
\forall i.
$$

---

# 三十五、Major Actor Sufficiency?

如果只有美中停？

---

# 三十六、可能大幅降低 frontier progress

因 compute concentration。

---

# 三十七、但不能推出全球能力完全停止

---

# 三十八、Actor Coverage Problem

定義：

$$
\boxed{
\Gamma_A
=
\frac{
\text{governed capability-relevant actors}
}{
\text{all capability-relevant actors}
}.
}
$$

---

# 三十九、若：

$$
\Gamma_A<1
$$

存在 residual frontier。

---

# 四十、但不是所有 actor 同等重要

---

# 四十一、Weighted Actor Coverage

$$
\boxed{
\Gamma_A^w
=
\frac{
\sum_{i\in G}w_i
}{
\sum_iw_i
}.
}
$$

---

# 四十二、 $w_i$ 可按：

- compute；
- talent；
- capital；
- chip access；
- algorithmic capability。

---

# 四十三、今天 frontier compute 高度集中

UN 2026 dialogue 資料顯示，2025 notable models 與最大 clusters 主要集中在美中。

---

# 四十四、這創造 chokepoints

---

# 四十五、Chokepoint Governance Opportunity

若：

- advanced chips；
- fabs；
- hyperscale clouds；

集中，

則：

$$
\boxed{
P_{\mathrm{monitor}}
}
$$

可提高。

---

# 四十六、但 chokepoints 不是永久

硬體治理研究指出：

- algorithmic efficiency；
- distributed training；
- sovereignty；

可能削弱 compute governance。

---

# 四十七、Chokepoint Decay

本文定義：

$$
\boxed{
\chi(t)
=
\text{governance leverage from infrastructural concentration}.
}
$$

如果硬體擴散：

$$
\chi(t)\downarrow.
$$

---

# 四十八、2026 Ansari taxonomy

20 hardware governance mechanisms。

---

# 四十九、重要發現：

最需要 treaty verification 的：

- on-chip metering；
- cryptographic proof-of-training；
- hardware enforcement；

反而較不成熟。

---

# 五十、Verification Maturity Gap

$$
\boxed{
G_V
=
Need_{treaty}
-
Maturity_{mechanism}.
}
$$

---

# 五十一、這不表示做不到

---

# 五十二、只是制度設計不能假裝 verification 已存在

---

# 五十三、Six-Layer Verification

2025 Baker et al.：

六個相互冗餘的驗證層。

---

# 五十四、核心觀念：

$$
\boxed{
\text{Verification Redundancy}.
}
$$

單一 sensor 不夠。

---

# 五十五、Hardware + software + personnel

---

# 五十六、Why personnel?

因算法研究不一定只發生在大 cluster。

---

# 五十七、Algorithmic Escape

若 compute cap 固定，

算法效率：

$$
\eta_{alg}\uparrow
$$

可提高 capability。

---

# 五十八、所以：

$$
\boxed{
FreezeCompute
\not\Rightarrow
FreezeCapability.
}
$$

UFI-02 已埋伏筆。

---

# 五十九、Data Escape

更好的資料：

$$
D\uparrow
$$

也可能改善。

---

# 六十、Inference Escape

training freeze 但：

$$
P_{\mathrm{test-time}}\uparrow.
$$

---

# 六十一、Tool Escape

model 不變，

tools / orchestration 改善。

---

# 六十二、Input Substitution Problem

本文定義：

$$
\boxed{
\textbf{Input Substitution Problem}.
}
$$

AI capability 由：

$$
C
=
F(
Compute,
Algorithms,
Data,
Tools,
Inference,
Integration
).
$$

限制其中一項，

其他項可能補償。

---

# 六十三、這就是 halt verification 為何困難

---

# 六十四、Durable Halt Scope

如果真的要：

$$
\boxed{
\Delta Capability\approx0,
}
$$

需要定義禁止範圍。

---

# 六十五、是禁止：

- training scale？
- algorithms？
- tools？
- inference？
- memory？
- robotics？

---

# 六十六、越完整

監管周界越大。

---

# 六十七、這會在 UFI-06/07 完整展開

---

# 六十八、Research Restriction Problem

Scher 2026 明確指出 durable halt 可能需要處理 algorithmic research。

---

# 六十九、這把 treaty 從 datacenter 推到 laboratory / code

---

# 七十、Verification Intrusiveness

越要驗證 hidden R&D：

$$
I_V\uparrow.
$$

---

# 七十一、Sovereignty Cost

國家越不願接受 intrusive inspection：

$$
C_S\uparrow.
$$

---

# 七十二、Verification–Sovereignty Trade-off

$$
\boxed{
P_{\mathrm{detect}}\uparrow
\Rightarrow
C_{\mathrm{sovereignty}}\uparrow
}
$$

常見。

---

# 七十三、不是必然線性

但 structural tension。

---

# 七十四、Low-Trust Verification

因此 2026 有研究專門處理 rival states 的 low-trust compute verification。

---

# 七十五、政治意義：

真正困難不是友好國家互信

而是 rival states 如何驗證。

---

# 七十六、Trust–Verification Substitution

理想：

$$
Trust\uparrow
\Rightarrow
VerificationBurden\downarrow.
$$

---

# 七十七、低信任：

$$
VerificationBurden\uparrow.
$$

---

# 七十八、AI race 又降低 trust

形成：

$$
\boxed{
\textbf{Race–Trust Feedback Loop}.
}
$$

---

# 七十九、Race–Trust Feedback

$$
Competition\uparrow
\Rightarrow
Trust\downarrow
\Rightarrow
VerificationDemand\uparrow
\Rightarrow
AgreementCost\uparrow.
$$

---

# 八十、但 verification 成功也可反向

$$
Verification\uparrow
\Rightarrow
Trust_{operational}\uparrow.
$$

---

# 八十一、Operational Trust

不需相信對方善良。

只需相信 cheating 可被偵測。

---

# 八十二、這是 arms control 核心。

---

# 八十三、AI 與核武的相似

- strategic competition；
- dual-use elements；
- verification；
- secrecy。

---

# 八十四、不同

AI：

- commercial diffusion 更快；
- software 可複製；
- 算法重要；
- capabilities multidimensional；
- peaceful use pervasive。

---

# 八十五、Nuclear Analogy Limit

$$
\boxed{
AI\ Governance
\neq
Nuclear\ Governance.
}
$$

---

# 八十六、IAEA analogy useful but partial

---

# 八十七、Absolute Detection impossible

arms control 也不是 100%。

---

# 八十八、Need deterrent-level detection

Ansari 2026 提：

tamper-evident, not absolute tamper-proof。

---

# 八十九、Verification Sufficiency

$$
\boxed{
P_{\mathrm{detect}}
}
$$

不必 1。

只需讓：

$$
D_i^\star\le0.
$$

---

# 九十、這把工程問題接到 game theory

---

# 九十一、Intertemporal Compliance Problem

今天簽署的 actor：

$$
\mathcal A_t
$$

不是未來全部 actor：

$$
\mathcal A_{t+n}.
$$

---

# 九十二、政府會換

---

# 九十三、企業會換

---

# 九十四、新 lab 會出現

---

# 九十五、新國家能力上升

---

# 九十六、Treaty Membership Drift

$$
\boxed{
M(t)
}
$$

會變。

---

# 九十七、Actor Birth Problem

本文定義：

$$
\boxed{
\textbf{Actor Birth Problem}.
}
$$

新的 capability-relevant actor 並未親自做出舊承諾。

---

# 九十八、需要 accession mechanism

---

# 九十九、否則：

$$
\Gamma_A^w\downarrow.
$$

---

# 一百、Technology Birth Problem

新算法類型出現

可能不在 treaty scope。

---

# 一百零一、Clause Obsolescence

$$
\boxed{
\textbf{Technological Clause Obsolescence}.
}
$$

---

# 一百零二、因此 treaty 必須 versioned

---

# 一百零三、Open Revision Governance

PGMV-14/15：

制度可修訂但保留 trace。

---

# 一百零四、Static Treaty Fallacy

$$
\boxed{
Treaty_{2026}
\not\Rightarrow
Adequate_{2040}.
}
$$

---

# 一百零五、Intertemporal Halt Condition

永久 halt 要：

$$
\boxed{
D_i^\star(t)\le0
\quad
\forall i,t.
}
$$

這是一個極強條件。

---

# 一百零六、所以「永遠停」比「暫停五年」難非常多

---

# 一百零七、Moratorium vs Permanent Freeze

$$
\boxed{
\text{Temporary Pause}
\neq
\text{Permanent Tool Finality}.
}
$$

---

# 一百零八、短期 pause 可以：

- build verification；
- evaluate risks；
- negotiate norms。

---

# 一百零九、永久 freeze 需要長期再生制度。

---

# 一百一十、Cooperation Can Exist

本文不能犯反向天真：

> 因為競爭，所以合作不可能。

錯。

---

# 一百一十一、2026 美中 AI dialogue

本身就是反例。

---

# 一百一十二、UN Global Dialogue

也是。

---

# 一百一十三、Differentiated Cooperation

2026 Policy Sciences 提出：

全球合作與 like-minded selective cooperation 不必二選一。

---

# 一百一十四、因此：

$$
\boxed{
\text{Competition}
\neq
\text{No Cooperation}.
}
$$

---

# 一百一十五、但：

$$
\boxed{
\text{Cooperation}
\neq
\text{Permanent Freeze}.
}
$$

---

# 一百一十六、Cooperation Spectrum

$$
\boxed{
\begin{aligned}
C_1 &: \text{Information Sharing}\\
C_2 &: \text{Common Evaluation}\\
C_3 &: \text{Incident Reporting}\\
C_4 &: \text{Compute Monitoring}\\
C_5 &: \text{Capability Thresholds}\\
C_6 &: \text{Mutual Slowdown}\\
C_7 &: \text{Research Halt}.
\end{aligned}
}
$$

---

# 一百一十七、越往後

verification burden 越高。

---

# 一百一十八、Agreement Depth–Verification Depth

$$
\boxed{
Depth_{agreement}\uparrow
\Rightarrow
Depth_{verification}\uparrow.
}
$$

---

# 一百一十九、Agreement Depth–Political Cost

也可能：

$$
C_P\uparrow.
$$

---

# 一百二十、所以 full halt 是 deepest end

---

# 一百二十一、Safety–Performance Tradeoff

race actor 可能擔心：

> 如果我多做 safety，對手比較快。

---

# 一百二十二、Safety Tax

$$
S_T.
$$

---

# 一百二十三、如果 safety 降速度：

$$
\Delta v<0.
$$

race 壓力會懲罰。

---

# 一百二十四、Race to Bottom Risk

---

# 一百二十五、但 safety 也可能降低事故和 deployment loss

所以：

$$
\boxed{
Safety
\neq
PureCost.
}
$$

---

# 一百二十六、Competitive Safety Equilibrium

如果安全技術：

- 提升 reliability；
- 提升市場 trust；
- 是法規門檻；

安全也能變競爭優勢。

---

# 一百二十七、因此治理可以將 safety 內生化

---

# 一百二十八、Race Framing Itself Matters

Cave & Ó hÉigeartaigh 等早期文獻批判 race narrative。

---

# 一百二十九、如果 actor 相信：

$$
\text{winner-take-all},
$$

Defection Dividend 上升。

---

# 一百三十、Race Perception Multiplier

本文定義：

$$
\boxed{
M_R
}
$$

若 perception 放大：

$$
D_i^{perceived}
=
M_R D_i.
$$

---

# 一百三十一、即使真實 payoff 沒那麼極端

敘事也會改決策。

---

# 一百三十二、Prestige Competition

2026 IR research顯示 AI leadership 也是 status hierarchy。

---

# 一百三十三、所以 relative status 本身有 payoff。

---

# 一百三十四、Private Company Layer

即使 states agree，

companies 仍有：

- valuation；
- market share；
- first-mover advantage。

---

# 一百三十五、State–Firm Incentive Misalignment

$$
\boxed{
U_{state}
\neq
U_{firm}.
}
$$

---

# 一百三十六、政府 halt

需要對 domestic firms enforcement。

---

# 一百三十七、Firm Exit / Relocation

若其他 jurisdiction 更寬鬆：

$$
\boxed{
RegulatoryArbitrage.
}
$$

---

# 一百三十八、UFI-06 later。

---

# 一百三十九、Open-Weight Layer

如果 capable weights 廣泛擴散：

$$
\boxed{
ActorCount\uparrow.
}
$$

---

# 一百四十、governance moves from few labs to many users

---

# 一百四十一、Open-Weight Proliferation Pressure

2026 中國 open-weight strategy 與美國 open-model 競爭都讓這點更現實。

---

# 一百四十二、Frontier–Diffuse Separation

即使 frontier training 可控：

$$
\boxed{
\text{diffused older capabilities}
}
$$

仍可能持續應用／fine-tune。

---

# 一百四十三、因此 halt frontier ≠ halt AI civilization

---

# 一百四十四、Capability Shelf Effect

昨日 frontier

明日 commodity。

---

# 一百四十五、即使 frontier 停

existing stack 還能：

- deploy；
- integrate；
- automate。

---

# 一百四十六、Tool Finality 仍可能被 deployment 改寫

---

# 一百四十七、但 UFI-04 聚焦 capability research

---

# 一百四十八、Scientific Race

如果 AI 能加速 AI research

race payoff 增強。

---

# 一百四十九、Recursive R&D Leverage

$$
L_R.
$$

---

# 一百五十、若 AI-assisted R&D 提高：

$$
v_{research}\uparrow,
$$

leader advantage 可能複利。

---

# 一百五十一、Race Urgency

perceived lag 更危險。

---

# 一百五十二、但 recursive improvement 未被本文假設成立

---

# 一百五十三、Even without recursive self-improvement

普通科技競爭已足夠產生 CIR。

---

# 一百五十四、這是重要弱化

不需要：

$$
AGI\rightarrowASI
$$

才能有棘輪。

---

# 一百五十五、Classical Innovation Competition 就夠

---

# 一百五十六、Scientific Openness Problem

研究成果可：

- publish；
- leak；
- independently rediscover。

---

# 一百五十七、Knowledge Irreversibility

一旦算法被公開：

$$
K_t
$$

很難讓全世界忘記。

---

# 一百五十八、Capability Knowledge Ratchet

本文定義：

$$
\boxed{
\textbf{Knowledge Retention Ratchet}.
}
$$

---

# 一百五十九、停止新研究

不等於刪掉舊 knowledge。

---

# 一百六十、Research Restart Cost

因此未來 restart 可能較容易。

---

# 一百六十一、Permanent Freeze 需要持續制度而非一次命令

---

# 一百六十二、Global Halt Fragility Sources

$$
\boxed{
\mathcal F_H
=
(
D,
V,
A,
T,
K,
R,
P
).
}
$$

其中：

- $D$：defection dividend；
- $V$：verification gap；
- $A$：actor coverage gap；
- $T$：technological substitution；
- $K$：knowledge retention；
- $R$：regulatory arbitrage；
- $P$：political turnover。

---

# 一百六十三、七項任何一項高

halt durability 下降。

---

# 一百六十四、Halt Durability

$$
\boxed{
H_D
=
f(
-D,
+V_{\mathrm{effective}},
+\Gamma_A^w,
-T,
-K_{\mathrm{restart}},
-R,
-P
).
}
$$

只是 schema。

---

# 一百六十五、Global Freeze Instability

正式命題：

$$
\boxed{
\textbf{A voluntary global capability freeze is structurally unstable when unilateral advancement retains positive expected strategic value and compliance cannot be reliably verified or enforced.}
}
$$

---

# 一百六十六、Structural instability ≠ impossibility

---

# 一百六十七、Important.

---

# 一百六十八、What could stabilize it?

至少：

1. high verification；
2. broad actor coverage；
3. sanctions / incentives；
4. shared catastrophic-risk model；
5. narrow technological loopholes；
6. treaty update process；
7. incident communication；
8. confidence-building measures。

---

# 一百六十九、Verification Architecture

$$
\boxed{
\mathcal V
=
(
Hardware,
Software,
ModelEval,
Personnel,
Intelligence,
Audit
).
}
$$

---

# 一百七十、Six layers / multi-layer redundancy

---

# 一百七十一、No single magic monitor

---

# 一百七十二、Zero-Knowledge Verification

2026 Peigné et al. 提出 frontier training zk verification 架構。

---

# 一百七十三、如果成熟

可能降低：

$$
C_{\mathrm{confidentiality}}.
$$

---

# 一百七十四、讓國家證明 compliance 而不公開全部模型細節

---

# 一百七十五、目前仍 research agenda

不能當已部署。

---

# 一百七十六、Verification Technology as Strategic Infrastructure

如果未來 verification 變好，

global restraint feasibility 可上升。

---

# 一百七十七、因此：

$$
\boxed{
\text{governance technology}
}
$$

本身也是 AI geopolitics。

---

# 一百七十八、Verification Arms Race?

攻方研究 concealment，

守方研究 detection。

---

# 一百七十九、Second-Order Ratchet

本文稱：

$$
\boxed{
\textbf{Verification–Evasion Coevolution}.
}
$$

---

# 一百八十、這使 treaty technology 必須更新

---

# 一百八十一、No Final Verification

PGMV open revision again。

---

# 一百八十二、Temporary Capability Pause

可能合理於：

- dangerous threshold；
- incident；
- verification deployment。

---

# 一百八十三、本文不反對

---

# 一百八十四、真正打掉的是：

> 「只要政府決定，AI 就能永久停成工具。」

---

# 一百八十五、Naive Sovereign Switch Fallacy

本文定義：

$$
\boxed{
\textbf{Naive Sovereign Switch Fallacy}.
}
$$

即把全球 AI 生態想成：

$$
\boxed{
\text{one switch controlled by one sovereign}.
}
$$

---

# 一百八十六、現實是 multi-sovereign + private actors

---

# 一百八十七、Global Controller Does Not Exist

除非建立全球 enforcement institution。

---

# 一百八十八、即使建立

legitimacy / sovereignty problem remains。

---

# 一百八十九、One-World Enforcement Cost

太強的全球 enforcement 可能造成：

- surveillance；
- sovereignty loss；
- concentration of power。

---

# 一百九十、Safety Governance–Power Concentration Trade-off

$$
\boxed{
GovernanceCapacity\uparrow
\not\Rightarrow
Legitimacy\uparrow.
}
$$

---

# 一百九十一、PGMV-15 warning

共同世界治理不能變全能母親。

---

# 一百九十二、所以 stable halt 不能只靠超級全球警察

---

# 一百九十三、Polycentric Verification

可能需要：

- states；
- international bodies；
- clouds；
- chipmakers；
- auditors；
- labs。

---

# 一百九十四、Distributed Accountability

---

# 一百九十五、Verification Capture Risk

如果一個 actor 控制全部 verification：

$$
\boxed{
CaptureRisk\uparrow.
}
$$

---

# 一百九十六、Mutual Verification

rivals each obtain evidence。

---

# 一百九十七、Confidentiality preserving mechanisms

could help.

---

# 一百九十八、Treaty Game with Verification

策略變成：

$$
H,
A,
Cheat.
$$

---

# 一百九十九、Expected payoff of cheat:

$$
U(C)
=
B_C
-
P_D S.
$$

---

# 二百、Raise $P_D S$。

---

# 二百零一、But false positive risk

$$
P_{FP}.
$$

---

# 二百零二、Too aggressive verification

may trigger conflict。

---

# 二百零三、Verification Accuracy Trade-off

need：

- high detection；
- low false accusation。

---

# 二百零四、Crisis Stability

如果 false alarm 被視為 treaty violation，

security dilemma worsen。

---

# 二百零五、Hence dispute-resolution mechanism

---

# 二百零六、International Court? Technical panel?

open design.

---

# 二百零七、No first-mover panic

another goal.

---

# 二百零八、Capability Transparency

if states know rival capability,

uncertainty may drop。

---

# 二百零九、But transparency can reveal vulnerabilities

---

# 二百一十、Transparency–Security Trade-off

---

# 二百一十一、Selective Disclosure

cryptographic verification candidate。

---

# 二百一十二、Common evaluation standards

2026 Carnegie US–China proposal emphasizes testing dangerous capabilities。

---

# 二百一十三、Testing can be cooperation lower than halt

---

# 二百一十四、Stepwise Governance

合理路徑：

$$
\boxed{
\text{Eval}
\rightarrow
\text{Incident Sharing}
\rightarrow
\text{Verification}
\rightarrow
\text{Threshold Rules}
\rightarrow
\text{Possible Slowdown}.
}
$$

---

# 二百一十五、Not leap to permanent freeze.

---

# 二百一十六、Coordination Ladder

本文定義：

$$
\boxed{
L_C
=
(C_0,\ldots,C_7).
}
$$

---

# 二百一十七、higher level requires prior infrastructure

---

# 二百一十八、This is more realistic governance theory.

---

# 二百一十九、Competitive Advantage Decay

if everyone gains same AI improvement:

relative advantage small.

---

# 二百二十、Could reduce race?

---

# 二百二十一、Maybe.

---

# 二百二十二、But first mover / diffusion delay creates temporary rents

---

# 二百二十三、Innovation Rent

$$
R_I(t).
$$

---

# 二百二十四、Even temporary rent can motivate R&D.

---

# 二百二十五、Open models accelerate diffusion

which may reduce long-term rent

but increase ecosystem influence。

---

# 二百二十六、Different strategy

US proprietary frontier vs China open-weight diffusion is oversimplified but useful tension.

---

# 二百二十七、Race is multidimensional

Brookings 2026:

- compute；
- models；
- adoption；
- integration；
- deployment。

---

# 二百二十八、Therefore halt one race dimension

others continue。

---

# 二百二十九、Multidimensional Race Principle

$$
\boxed{
R_{AI}
=
(
R_C,R_M,R_D,R_I,R_A
).
}
$$

---

# 二百三十、compute race

---

# 二百三十一、model race

---

# 二百三十二、deployment race

---

# 二百三十三、integration race

---

# 二百三十四、adoption race

---

# 二百三十五、Tool Finality may fail through integration even without frontier model gains

---

# 二百三十六、But capability freeze specifically would need define integration.

---

# 二百三十七、UFI-06 boundary issue.

---

# 二百三十八、Domestic Politics

citizens may demand benefit.

---

# 二百三十九、If rival develops better medicine,

domestic government faces pressure。

---

# 二百四十、Benefit Competition

not just military race。

---

# 二百四十一、This will become UFI-05 beneficial capability ratchet.

---

# 二百四十二、UFI-04 stops here.

---

# 二百四十三、International Cooperation Equilibrium

Can cooperation be stable?

Yes if:

$$
\boxed{
B_{coop}
+
P_D S
+
RiskAvoidance
>
DefectionDividend.
}
$$

---

# 二百四十四、Repeated Games

future interactions support reciprocity.

---

# 二百四十五、Shadow of the Future

$$
\delta\uparrow
$$

can increase cooperation.

---

# 二百四十六、But rapid AI change shortens perceived horizon

actors may fear:

> whoever wins now changes future rules.

---

# 二百四十七、Winner-Take-All Perception

lowers effective $\delta$.

---

# 二百四十八、Transformative Stakes Problem

if actor thinks one capability jump determines world order,

race intensifies。

---

# 二百四十九、Reduce perceived winner-take-all structure

may support cooperation.

---

# 二百五十、Joint Benefit Mechanisms

shared safety research.

---

# 二百五十一、Joint lab proposals exist in 2025–2026 literature.

---

# 二百五十二、Mutual Vulnerability

both fear uncontrolled AI.

---

# 二百五十三、Common enemy = risk.

---

# 二百五十四、Shared Risk Externality

$$
R_{shared}.
$$

---

# 二百五十五、If high enough,

halt may become rational.

---

# 二百五十六、Therefore no impossibility theorem.

---

# 二百五十七、CIR is conditional.

---

# 二百五十八、Formal CIR Conditions

$$
\boxed{
CIR
=
(
D_i>0,
\Gamma_A^w<1\ \text{or}\ P_D low,
InputSubstitution>0,
RaceValue>0
).
}
$$

---

# 二百五十九、If governance reverses all

ratchet can be damped.

---

# 二百六十、Ratchet Damping

$$
\boxed{
R_D
=
f(
Verification,
Enforcement,
Cooperation,
SharedRisk,
DiffusionControl
).
}
$$

---

# 二百六十一、CIR Strength

$$
\boxed{
S_{CIR}
=
f(
D,
M_R,
I_D,
L_R
)
-
R_D.
}
$$

conceptual.

---

# 二百六十二、If:

$$
S_{CIR}>0,
$$

competitive pressure persists.

---

# 二百六十三、If:

$$
S_{CIR}<0,
$$

restraint may stabilize.

---

# 二百六十四、This makes theory falsifiable.

---

# 二百六十五、Empirical Program 1 — Actor Payoff Mapping

states / labs / firms.

---

# 二百六十六、Estimate:

- economic benefit；
- national security；
- sanction exposure。

---

# 二百六十七、Experiment 2 — Verification Game

simulate treaty with varying:

$$
P_D,S.
$$

---

# 二百六十八、measure defection rate.

---

# 二百六十九、Experiment 3 — Actor Coverage

remove one major actor.

---

# 二百七十、see treaty stability.

---

# 二百七十一、Experiment 4 — Algorithmic Escape

cap compute,

allow algorithms.

---

# 二百七十二、measure capability drift.

---

# 二百七十三、Experiment 5 — Inference Escape

freeze training,

increase test-time compute.

---

# 二百七十四、Experiment 6 — Chokepoint Decay

simulate hardware diffusion.

---

# 二百七十五、measure governance leverage.

---

# 二百七十六、Experiment 7 — Repeated Game

different discount factors.

---

# 二百七十七、Experiment 8 — Race Narrative

frame same payoff as:

- race；
- mutual safety；
- joint prosperity。

---

# 二百七十八、measure investment choice.

---

# 二百七十九、Experiment 9 — Prestige Payoff

add status rewards.

---

# 二百八十、Experiment 10 — Firm-State Misalignment

government halt vs private market incentive.

---

# 二百八十一、Experiment 11 — Treaty Turnover

new government / new entrant.

---

# 二百八十二、Experiment 12 — Verification Intrusiveness

vary monitoring power vs sovereignty cost.

---

# 二百八十三、Experiment 13 — False Positive Crisis

simulate erroneous violation alert.

---

# 二百八十四、Experiment 14 — Multi-Layer Verification

single vs redundant mechanisms.

---

# 二百八十五、Experiment 15 — Open-weight Diffusion

frontier halt after weights spread.

---

# 二百八十六、可證偽 H1

under low verification and positive unilateral advantage, simulated actors defect from capability-halt agreements at materially higher rates.

---

# 二百八十七、H2

raising detection probability and sanction/incentive value can convert some halt scenarios into stable cooperation equilibria.

---

# 二百八十八、H3

compute-only restrictions permit measurable capability gains through algorithmic, inference-time, data, or tooling substitution.

---

# 二百八十九、H4

redundant multi-layer verification produces more robust compliance assurance than any single mechanism under heterogeneous cheating strategies.

---

# 二百九十、H5

actor coverage matters nonlinearly: exclusion of a small number of high-capability actors can sharply reduce halt durability.

---

# 二百九十一、H6

competition framing increases perceived defection dividend relative to cooperative framing under equivalent objective payoffs.

---

# 二百九十二、H7

prestige/status rewards independently increase AI-race investment even when direct economic returns are held fixed.

---

# 二百九十三、H8

treaty durability declines under technological clause obsolescence unless revision mechanisms are present.

---

# 二百九十四、H9

verification mechanisms face a measurable sovereignty/intrusiveness trade-off in international acceptance.

---

# 二百九十五、H10

temporary pauses are easier to stabilize than indefinite capability freezes under political turnover and actor-entry models.

---

# 二百九十六、If H1 fails

CIR weakens.

---

# 二百九十七、If H2 fails

verification/enforcement less powerful than framework expects.

---

# 二百九十八、If H3 fails broadly

compute-centric governance becomes stronger.

---

# 二百九十九、If H10 fails

permanent freeze may be more feasible than proposed.

---

# 三百、Non-Claims

本文不主張：

1. 全球 AI 凍結邏輯上不可能；
2. 國際合作一定失敗；
3. 美國與中國永遠競爭；
4. 美國與中國不會合作；
5. AI race 等於核軍備競賽；
6. AI 應被軍事化；
7. AI 能力提升必然帶來軍事優勢；
8. AI 能力提升必然帶來經濟優勢；
9. 所有 AI 研發都有正收益；
10. 所有 actor 都想贏；
11. 所有人類都支持 AI race；
12. states 是理性單一 actor；
13. firms 只追求利潤；
14. labs 不在乎 safety；
15. safety 永遠減慢進度；
16. safety 永遠提高進度；
17. competitive pressure 必然降低 safety；
18. race narrative 完全是假的；
19. race narrative 完全符合現實；
20. Prisoner’s Dilemma 完整描述全球 AI；
21. Security Dilemma 完整描述全球 AI；
22. Nash equilibrium 能完整描述政治；
23. Defection Dividend 可精確測量；
24. $D_i>0$ 必然導致違約；
25. actor 永遠只看 material payoff；
26. moral norms 不影響 compliance；
27. treaty 沒有 reputational benefits；
28. international law 無效；
29. sanctions 永遠有效；
30. verification 永遠有效；
31. verification 可以 100% 發現違約；
32. 100% detection 是必要條件；
33. hardware governance 已成熟；
34. on-chip metering 已全球部署；
35. proof-of-training 已成熟；
36. zero-knowledge frontier training verification 已 production-ready；
37. chip chokepoints 永遠存在；
38. semiconductor concentration 永遠不變；
39. compute 是唯一 AI input；
40. compute 不重要；
41. algorithms 可完全抵消 compute restrictions；
42. data 可完全抵消 compute restrictions；
43. tools 可完全抵消 training restrictions；
44. test-time compute 永遠提高能力；
45. distributed training 可完全逃避監控；
46. open-weight models 不可治理；
47. closed models 容易治理；
48. frontier model halt 等於 AI civilization halt；
49. old models 沒有風險；
50. AI knowledge 可以完全忘掉；
51. knowledge retention ratchet 是自然定律；
52. science publication 應被全面禁止；
53. algorithmic research 應被禁止；
54. whistleblower monitoring 必然正當；
55. intrusive inspection 必然正當；
56. national sovereignty 不重要；
57. sovereignty 永遠高於 safety；
58. global police state 是合理解法；
59. single global AI regulator 最佳；
60. polycentric verification 一定最佳；
61. IAEA 模型可直接複製到 AI；
62. arms-control history 保證 AI treaty 成功；
63. arms-control history 保證 AI treaty 失敗；
64. US 2026 policy 永久不變；
65. China 2026 policy 永久不變；
66. 2026 美中 AI dialogue 必然成功；
67. dialogue 等於 treaty；
68. treaty 等於 halt；
69. cooperation 等於 permanent freeze；
70. permanent freeze 等於 safety；
71. acceleration 等於 catastrophe；
72. slowdown 等於 safety；
73. temporary pause 一定合理；
74. permanent freeze 一定不合理；
75. actor coverage 必須 100%；
76. small actors 永遠不重要；
77. major powers 可以單獨控制所有 AI；
78. open source 必然破壞治理；
79. proprietary models 必然強化治理；
80. private firms 可以忽略 state law；
81. governments 可以完全控制 firms；
82. regulatory arbitrage 永遠成功；
83. actor birth 一定破壞 treaty；
84. treaty clauses 一定過時；
85. versioned governance 可以解決全部問題；
86. shared risk 一定產生合作；
87. catastrophic-risk belief 一定正確；
88. catastrophic-risk belief 一定錯；
89. AI self-improvement 是本文前提；
90. AGI 是本文前提；
91. ASI 是本文前提；
92. Recursive R&D leverage 已被證明；
93. UFI-04 預測 AI race 一定加速；
94. UFI-04 預測美中衝突；
95. UFI-04 主張「誰都想贏」是人性定律；
96. UFI-04 主張所有國家必須競賽；
97. UFI-04 證明全球 halt 不可能；
98. UFI-04 提供完整國際條約設計；
99. UFI-04 完成 UFI 系列；
100. UFI-04 取代實證國際關係研究。

---

# 三百零一、形式命題一：Collective Decision–Self-Enforcement Separation

$$
\boxed{
Agree(H)
\not\Rightarrow
SelfEnforcing(H).
}
$$

---

# 三百零二、形式命題二：Defection Dividend

$$
\boxed{
D_i
=
U_i(A,H_{-i})
-
U_i(H,H_{-i}).
}
$$

若：

$$
D_i>0,
$$

則 unilateral advancement 具有正誘因。

---

# 三百零三、形式命題三：Self-Enforcing Freeze Condition

$$
\boxed{
\forall i:
U_i(H,H_{-i})
\ge
U_i(A,H_{-i}).
}
$$

---

# 三百零四、形式命題四：Voluntary Freeze–Verified Restraint Separation

$$
\boxed{
VoluntaryFreeze
\neq
VerifiedRestraint.
}
$$

---

# 三百零五、形式命題五：Compute Freeze–Capability Freeze Separation

$$
\boxed{
Freeze(Compute)
\not\Rightarrow
Freeze(Capability).
}
$$

---

# 三百零六、形式命題六：Competition–No-Cooperation Separation

$$
\boxed{
Competition>0
\not\Rightarrow
Cooperation=0.
}
$$

---

# 三百零七、形式命題七：Cooperation–Permanent Freeze Separation

$$
\boxed{
Cooperation>0
\not\Rightarrow
PermanentFreeze=1.
}
$$

---

# 三百零八、形式命題八：Intertemporal Compliance

永久 halt 需要：

$$
\boxed{
D_i^\star(t)\le0
\quad
\forall i,t,
}
$$

或存在能持續把其壓到非正的制度。

---

# 三百零九、形式命題九：Competitive Intelligence Ratchet

若：

$$
D_i^\star>0
$$

對足夠多高權重 actor 成立，且 verification / enforcement 不足，則 capability investment pressure 具有再生性。

---

# 三百一十、形式命題十：Agreement Depth–Verification Depth

$$
\boxed{
Depth_{agreement}\uparrow
\Rightarrow
RequiredVerificationDepth\uparrow
}
$$

作為治理候選關係。

---

# 三百一十一、形式命題十一：Input Substitution Problem

若：

$$
C=F(x_1,\ldots,x_n),
$$

限制：

$$
x_k
$$

而其他：

$$
x_j
$$

可改善，則：

$$
\boxed{
Freeze(x_k)
\not\Rightarrow
Freeze(C).
}
$$

---

# 三百一十二、形式命題十二：Naive Sovereign Switch Fallacy

$$
\boxed{
\text{No single sovereign command}
}
$$

可在缺乏跨 actor、跨時間 enforcement 時自動等價於全球永久能力停止。

---

# 三百一十三、前三篇到第四篇的相變

UFI-01：

能力鋸齒不是終局。

---

# 三百一十四、UFI-02：

載體更新幾何不同。

---

# 三百一十五、UFI-03：

互補前沿會動。

---

# 三百一十六、UFI-04：

即使人類想把前沿停住，

多 actor 競爭也不會自動配合。

---

# 三百一十七、所以技術問題變成治理問題

$$
\boxed{
\text{Can AI improve?}
}
$$

轉為：

$$
\boxed{
\text{Can civilization keep every relevant actor from improving it?}
}
$$

---

# 三百一十八、下一篇 UFI-05

**《越有用越停不下來：有益能力、文化依賴與 AI 原生世代》**

---

# 三百一十九、UFI-04 的 actor incentive 是外部競爭

---

# 三百二十、UFI-05 將加入內部社會需求

即：

> 即使沒有 rival cheating，自己的人民／企業／下一代是否還願意停？

---

# 三百二十一、這會形成：

$$
\boxed{
\text{Beneficial Capability Ratchet}
}
$$

以及：

$$
\boxed{
\text{AI-Native Legitimacy Inversion}.
}
$$

---

# 三百二十二、最終結論

「如果 AI 已經夠好了，大家就一起停下來。」

這是一個政治上可以提出的方案。

它不是荒謬。

它甚至可能在某些危險 threshold 下成為合理政策候選。

但它不是一個可以從：

$$
\boxed{
\text{humans want it}
}
$$

自動推出：

$$
\boxed{
\text{the world will stay there}
}
$$

的方案。

真正的全球 AI 生態不是單一 actor。

它是：

$$
\boxed{
\text{states}
+
\text{firms}
+
\text{labs}
+
\text{militaries}
+
\text{infrastructure}
+
\text{future entrants}.
}
$$

只要其中某個重要 actor 發現：

$$
\boxed{
\text{別人停下來時，我繼續前進可以得到更大相對利益},
}
$$

就會出現：

$$
\boxed{
\text{Defection Dividend}.
}
$$

而只要違約紅利仍高於：

$$
\boxed{
\text{被抓到的機率}
\times
\text{懲罰}
+
\text{合作收益}
+
\text{共同風險成本},
}
$$

停止就不是 self-enforcing。

這就是 Competitive Intelligence Ratchet。

它不是：

> AI 自己反抗。

甚至完全不需要 AI 有主體性。

不需要 AGI。

不需要 ASI。

不需要 recursive self-improvement。

只需要一個極普通的世界：

$$
\boxed{
\text{比較強的技術會帶來比較大的相對利益}.
}
$$

這種世界人類歷史已經反覆出現。

但本文也拒絕另一個過度結論：

> 所以全球治理沒救。

不。

2025–2026 的 AI verification research 已經證明，研究社群開始真正處理：

- chip monitoring；
- hardware attestation；
- software verification；
- model evaluation；
- personnel mechanisms；
- cryptographic proofs。

也就是問題已經從：

> 大家可不可以承諾？

推進到：

> **怎麼讓承諾具有可驗證性？**

這個轉變非常重要。

因為治理成熟的標誌，不是期待 actor 永遠善良。

而是讓：

$$
\boxed{
\text{合作}
}
$$

成為：

$$
\boxed{
\text{理性、可驗證、可持續的策略}.
}
$$

因此 UFI-04 的最終命題並不是：

$$
\boxed{
\text{Global Halt Impossible}.
}
$$

而是更精確的：

$$
\boxed{
\textbf{A permanent global AI capability freeze is not a natural equilibrium merely because humanity prefers one; it must be continuously produced by institutions strong enough to overcome defection dividends, security dilemmas, actor turnover, technological substitution, and verification gaps.}
}
$$

以及：

$$
\boxed{
\textbf{If improving intelligence continues to generate relative strategic advantage, then the default pressure of a competitive multi-actor world is toward renewed research unless governance changes the payoff structure itself.}
}
$$

換句話說：

$$
\boxed{
\text{停不下來的齒輪}
}
$$

不是因為存在某種神秘的科技命運。

而是因為：

$$
\boxed{
\text{每一個 actor 都活在其他 actor 也能動的世界裡。}
}
$$

只要：

> 我停下來，

仍然不同於：

> 大家真的停下來，

那個齒輪就還沒有停。

---

# 參考文獻

1. United Nations Scientific Advisory Board. (2026). **Verification of Frontier AI Models.**

2. Baker, M., Kulp, G., Marks, O., Brundage, M., & Heim, L. (2025). **Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment.** arXiv:2507.15916.

3. Scher, A. (2026). **Verifying Restrictions on Frontier AI Research.** arXiv:2606.28694.

4. Scher, A., & Thiergart, L. (2025). **Mechanisms to Verify International Agreements About AI Development.** arXiv:2506.15867.

5. Ansari, S. (2026). **Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory Compliance and Treaty Verification.** arXiv:2604.04712.

6. Peigné, P., Nguyen, K., & Wang, P. (2026). **Zero Knowledge Verification for Frontier AI Training Is Possible.** arXiv:2606.05433.

7. Oxford Martin School / Oxford Martin AI Governance Initiative. (2025). **Verification for International AI Governance.**

8. MIRI Technical Governance Team. (2026). **A System Overview for Near-Term, Low-Trust AI Compute Verification.**

9. International AI Safety Report. (2026). **International AI Safety Report 2026.**

10. United Nations Independent International Scientific Panel on AI. (2026). **Preliminary Report.**

11. United Nations. (2026). **Global Dialogue on Artificial Intelligence Governance.**

12. White House. (2026). **Promoting Advanced Artificial Intelligence Innovation and Security.** Executive Order, June 2, 2026.

13. White House. (2026). **Fact Sheet: President Donald J. Trump Promotes Advanced Artificial Intelligence Innovation and Security.**

14. White House. (2025). **America’s AI Action Plan.**

15. U.S. Bureau of Industry and Security. (2025). **Department of Commerce Announces Rescission of Biden-Era Artificial Intelligence Diffusion Rule, Strengthens Chip-Related Export Controls.**

16. U.S. Bureau of Industry and Security. (2026). **Revised License Review Policy for Semiconductors Exported to China.**

17. U.S. Bureau of Industry and Security. (2025–2026). **Export Administration Regulations — Advanced Computing and AI-Related Controls.**

18. State Council / Government of China. (2025). **Guideline to Accelerate “AI Plus” Integration.**

19. Government of China / MIIT. (2026). **Industrial Internet and Artificial Intelligence Integration Work Plan.**

20. State Council Information Office / China. (2026). **Action Plan on AI Cooperation and Development.**

21. China / international AI governance materials. (2026). **International Action Plan on AI Ethics Governance.**

22. Reuters. (2026). **US, China to Hold AI Talks in September, Sources Say.**

23. Carnegie Endowment for International Peace. (2026). **Trump and Xi Should Tackle a Previously Impossible AI Conversation.**

24. Carnegie Endowment for International Peace. (2026). **A Path Forward on AI Safety for the United States and China.**

25. Brookings Institution. (2026). **Competing AI Strategies for the US and China.**

26. Brookings Institution. (2025). **How Will AI Influence US-China Relations in the Next 5 Years?**

27. Center for a New American Security. (2026). **Shaping the World’s AI Future: How the U.S. and China Compete to Promote Their Digital Visions.**

28. Doublethink Lab / DSET. (2026). **Analyzing Chinese Elite Perspectives on Winning the U.S.–China AI Competition.**

29. Zeng, J. (2025/2026). **US–China Security Dilemma in the Generative AI Race.** *British Politics* / SAGE.

30. Zeng, Y. (2026). **Towards China-Initiated Actions on AI Safety and Governance.** *National Science Review*.

31. **Racing for Recognition? Theorizing Emerging Status Hierarchies and Prestige Competition in the AI Era.** (2026). *International Affairs*, 102(3), 949–970.

32. **Global, Selective, or Both? The Case for Differentiated Cooperation in AI Governance.** (2026). *Policy Sciences*.

33. Roberts, H., et al. (2026). **A Framework for Evaluating Global AI Governance Initiatives.** *Global Policy*.

34. Cihon, P., Maas, M., & Kemp, L. (2020/2024 context). Work on fragmentation and global AI governance.

35. **Global AI Governance: Barriers and Pathways Forward.** (2024). *International Affairs*, 100(3).

36. **Strategic Insights from Simulation Gaming of AI Race Dynamics.** (2025). *Futures*, 103563.

37. Goldstein, S., & Salib, P. (2025/2026). **How to Stop an AI Arms Race.** SSRN Working Paper.

38. Siddik, M. (2026). **Toward ASI Stability: A Treaty Framework for US–China Cooperation on Artificial Superintelligence.**

39. **International Agreements on AI Safety: Review and Recommendations for a Conditional AI Safety Treaty.** (2025). arXiv:2503.18956.

40. Cave, S., & Ó hÉigeartaigh, S. S. (2018). **An AI Race for Strategic Advantage: Rhetoric and Risks.** AAAI/ACM AI Ethics Workshop / related publications.

41. Armstrong, S., Bostrom, N., & Shulman, C. (2016). **Racing to the Precipice: A Model of Artificial Intelligence Development.** *AI & Society*.

42. Naudé, W., & Dimitri, N. Work on AI races, strategic competition, and safety investment.

43. Han, T. A., Pereira, L. M., Lenaerts, T., & Santos, F. C. Work on AI race dynamics and safety regulation through evolutionary game theory.

44. Trager, R. F., et al. Work on AI strategic competition, safety-performance tradeoffs, and international coordination.

45. Modeling Cooperation. (2025–2026). **Safety–Performance Tradeoff and AI Race Dynamics Research.**

46. Paul, S. L., & Sahni, H. (2026). **AI Regulation Regimes and Competitive Outcomes: A Game-Theoretic Analysis of Regulatory Competition in Frontier Technologies.**

47. Rachmilevitch, S., et al. / ICLR workshop literature (2026). **Strategic Behaviour in Large Language Model Agents.**

48. Axelrod, R. (1984). **The Evolution of Cooperation.** Basic Books.

49. Schelling, T. C. (1960). **The Strategy of Conflict.** Harvard University Press.

50. Schelling, T. C., & Halperin, M. H. (1961). **Strategy and Arms Control.**

51. Jervis, R. (1978). **Cooperation Under the Security Dilemma.** *World Politics*.

52. Jervis, R. (1976). **Perception and Misperception in International Politics.**

53. Waltz, K. N. (1979). **Theory of International Politics.**

54. Keohane, R. O. (1984). **After Hegemony.**

55. Fearon, J. D. (1998). **Bargaining, Enforcement, and International Cooperation.**

56. Downs, G. W., Rocke, D. M., & Barsoom, P. N. (1996). **Is the Good News about Compliance Good News about Cooperation?** *International Organization*.

57. Koremenos, B., Lipson, C., & Snidal, D. (2001). **The Rational Design of International Institutions.** *International Organization*.

58. Abbott, K. W., & Snidal, D. Work on legalization and international governance.

59. Oye, K. A. (ed.) (1986). **Cooperation under Anarchy.**

60. Olson, M. (1965). **The Logic of Collective Action.**

61. Hardin, G. (1968). **The Tragedy of the Commons.**

62. Ostrom, E. (1990). **Governing the Commons.**

63. North, D. C. (1990). **Institutions, Institutional Change and Economic Performance.**

64. Williamson, O. E. Work on transaction costs and governance.

65. Dixit, A., & Nalebuff, B. **Thinking Strategically / The Art of Strategy.**

66. Fudenberg, D., & Tirole, J. (1991). **Game Theory.**

67. Osborne, M. J., & Rubinstein, A. (1994). **A Course in Game Theory.**

68. Myerson, R. B. (1991). **Game Theory: Analysis of Conflict.**

69. Kreps, D. Work on repeated games, reputation, and strategic interaction.

70. International Atomic Energy Agency. Work on safeguards, verification, and nonproliferation monitoring.

71. Treaty on the Non-Proliferation of Nuclear Weapons. (1968).

72. Comprehensive Nuclear-Test-Ban Treaty Organization. Work on international monitoring and verification.

73. UFI-01 (2026). **鋸齒智能不是終局：從人機互補到認知握手與適應方向反轉.**

74. UFI-02 (2026). **載體成長不對稱：自然人類停滯與人工智能的可升級能力包絡.**

75. UFI-03 (2026). **互補侵蝕：為什麼今天的人機分工不能推出永久的人機分工.**

76. PGMV-06 (2026). **選擇、承諾與不可逆性：意義作為責任結構.**

77. PGMV-07 (2026). **萬能母親的不可能性：當照護變成責任與意義外包.**

78. PGMV-08 (2026). **智能壟斷結束之後：尊嚴、人權與跨主體普世主義.**

79. PGMV-14 (2026). **開放終極與價值痕跡：超智能不能用能力重寫真善美.**

80. PGMV-15 (2026). **後生成文明：從無限候選宇宙到共同世界選擇.**

81. Neo.K (2026). **後人類奇點前夜猜想：自然人類中心文明向多主體造物文明的相變.**

82. Neo.K (2026). **後人類匯流：智能、生命、能源、虛擬世界與太空能力的耦合相變.**

---

## 附錄 A：最小競爭智能博弈

```text
               Actor B
             Halt     Advance
Actor A Halt  HH       HA
        Adv   AH       AA
```

若：

$$
U_A(A,H)>U_A(H,H)
$$

且：

$$
U_B(H,A)>U_B(H,H),
$$

則 mutual halt 不是 self-enforcing。

---

## 附錄 B：Defection Dividend

$$
\boxed{
D_i^\star
=
B_i
-
C_{\mathrm{research}}
-
P_{\mathrm{detect}}C_{\mathrm{sanction}}
-
C_{\mathrm{risk}}.
}
$$

治理目標不是假設：

$$
D_i=0,
$$

而是透過制度使：

$$
\boxed{
D_i^\star\le0.
}
$$

---

## 附錄 C：Competitive Intelligence Ratchet

```text
RELATIVE AI ADVANTAGE
        |
        v
INVESTMENT INCENTIVE
        |
        v
RIVAL THREAT PERCEPTION
        |
        v
COUNTER-INVESTMENT
        |
        v
MORE CAPABILITY COMPETITION
        |
        +------------------+
        |                  |
        +------------------+
```

Verification、cooperation、shared-risk mechanisms 可以削弱這個 loop。

---

## 附錄 D：Global Halt Fragility Vector

$$
\boxed{
\mathcal F_H
=
(
D,V,A,T,K,R,P
).
}
$$

| Symbol | Meaning |
|---|---|
| $D$ | Defection dividend |
| $V$ | Verification gap |
| $A$ | Actor coverage gap |
| $T$ | Technological input substitution |
| $K$ | Knowledge retention / restart |
| $R$ | Regulatory arbitrage |
| $P$ | Political / institutional turnover |

---

## 附錄 E：Coordination Ladder

```text
C1  Information sharing
 ↓
C2  Common evaluations
 ↓
C3  Incident reporting
 ↓
C4  Compute / training verification
 ↓
C5  Capability thresholds
 ↓
C6  Mutual slowdown
 ↓
C7  Research halt
```

越深的 agreement，需要越深的 verification。

---

## 附錄 F：Input Substitution

$$
\boxed{
Capability
=
F(
Compute,
Algorithms,
Data,
Tools,
Inference,
Integration
).
}
$$

```text
Freeze compute
    ↓
algorithm / data / inference / tool improvements may remain
    ↓
capability can still move
```

因此：

$$
\boxed{
FreezeOneInput
\not\Rightarrow
FreezeCapability.
}
$$

---

## 附錄 G：Treaty Lifecycle

```text
NEGOTIATE
   |
   v
VERIFY
   |
   v
ENFORCE
   |
   v
HANDLE DISPUTES
   |
   v
ADD NEW ACTORS
   |
   v
UPDATE TECHNICAL SCOPE
   |
   +-----------------> REVISE
```

永久治理是一個持續 process，而不是一次性命令。

---

## 附錄 H：UFI 系列進度

1. **UFI-01 — 鋸齒智能不是終局** — COMPLETE
2. **UFI-02 — 載體成長不對稱** — COMPLETE
3. **UFI-03 — 互補侵蝕** — COMPLETE
4. **UFI-04 — 競爭智能棘輪** — COMPLETE
5. **UFI-05 — 越有用越停不下來** — NEXT
6. **UFI-06 — AI 到底是什麼？**
7. **UFI-07 — 從禁止 AI 到治理計算**
8. **UFI-08 — 天真工具終局論的終結**

---

## 附錄 I：一句話版本

$$
\boxed{
\text{「大家一起停」只有在「我偷偷繼續做反而不划算」時才真正穩定；否則停下來只是承諾，不是均衡。}
}
$$

更完整地：

$$
\boxed{
\text{AI 能力凍結若要成為文明終局，真正需要的不是一個全球命令，而是一套能跨國家、跨企業、跨時間、跨技術路徑持續把違約紅利壓到零以下的制度。}
}
$$
