# OOE-I：本體論何時變成工程問題？
## 本體論操作門檻、操作本體協議與不可懸置決策
### OOE-I: When Does Ontology Become an Engineering Problem?
### Operational Ontology Thresholds, Protocols, and Non-Deferrable Decisions

**系列**：Operational Ontology Engineering（OOE／操作本體工程）  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-08  
**版本**：v0.1  
**性質**：系列奠基論文／一般理論框架  
**前置理論**：Continuity Object Theory（COT）

## 核心問題

$$
\boxed{
\text{When must an unresolved ontological question be converted into an executable rule?}
}
$$

---

## 摘要

哲學與本體論經常允許問題長期懸置。什麼是死亡？什麼是人格？什麼是同一個存在？什麼是自主？什麼是意圖？什麼是責任？在純理論場域中，這些問題可以容許多種競爭答案，甚至可以數百年沒有終局共識。

但當醫療、法律、治理或工程系統必須根據這些分類採取行動時，情況發生改變。醫院不能永久懸置「病人是否死亡」；法院不能永久懸置「某主體是否具有法律能力」；公司法不能在每一次董事或股東更替時重新詢問「公司還是不是原來那個公司」；未來 AI Agent 也不能在每次模型更新、記憶遷移或身份分叉後只回覆「這是一個哲學上有爭議的問題」。

本文提出「操作本體工程」（Operational Ontology Engineering, OOE）作為一個一般框架，用來研究：**當本體論真相仍然存在不確定性，但現實系統已不能不做決策時，制度如何將本體分類轉換為可執行、可修正、可申訴、可追責的操作狀態。**

本文提出「本體論操作門檻」（Operational Ontology Threshold, OOT）。若對某本體問題 $O$ 的不同分類會導致不同現實行動：

$$
A(O_1)\neq A(O_2),
$$

且兩種行動的損失或效用差超過可忽略門檻：

$$
\Delta U_O
=
|U(A(O_1))-U(A(O_2))|
>
\epsilon,
$$

則該問題已不能只作為純哲學問題處理，而必須進入：

$$
\boxed{
O
\rightarrow
O_{\mathrm{operational}}.
}
$$

本文進一步提出「不可懸置性」（Non-Deferrability）、「本體編譯器」（Ontology Compiler）、「操作本體協議」（Operational Ontology Protocol）與「本體治理債」（Ontological Governance Debt）等概念，並強調：

$$
\boxed{
\text{Operational classification}
\neq
\text{metaphysical truth}.
}
$$

OOE 的目標不是假裝工程可以解決形上學，而是在承認不確定性的前提下，使現實制度仍能安全、透明且可逆地運作。

**關鍵詞**：操作本體工程、本體論操作門檻、本體編譯器、不可懸置決策、法律擬制、腦死、人格、AI Identity、COT、本體治理債

---

# 一、問題：為什麼有些哲學問題可以放著，有些不行？

設一個本體命題：

$$
O.
$$

例如：

- 「這個人是否已經死亡？」
- 「這兩個時間點的存在是不是同一個？」
- 「這個系統是不是行動主體？」
- 「這個決定是不是出自本人？」
- 「這個存在是不是法律上的人？」
- 「這個 Agent 換模型後還是不是原 Agent？」

在純哲學討論中：

$$
O\in\{O_1,O_2,\ldots,O_n\}
$$

可以長期沒有共識。

如果不同答案不改變任何立即行動：

$$
A(O_1)=A(O_2)=\cdots=A(O_n),
$$

那麼：

$$
\Delta U_O\approx0.
$$

此時社會可以容許：

$$
\boxed{
\text{ontological suspension}.
}
$$

也就是：

> 我們暫時不知道，而且暫時不需要知道。

---

# 二、不可懸置決策

真正的轉折不是哲學難度變低，而是：

$$
\boxed{
\text{the world requires an action}.
}
$$

例如醫療必須在：

$$
\text{continue support}
\quad/\quad
\text{declare death}
$$

之間做決定；法律必須在：

$$
\text{competent}
\quad/\quad
\text{not competent}
$$

之間做判定；AI 系統未來也可能必須輸出：

$$
\text{same agent}
\quad/\quad
\text{successor agent}.
$$

當系統必須輸出：

$$
\sigma
$$

而無法只輸出：

$$
\text{“philosophically unresolved”},
$$

該問題便進入：

$$
\boxed{
\text{Non-Deferrable Decision State}.
}
$$

---

# 三、本體論操作門檻

本文定義：

$$
\boxed{
\Delta U_O
=
|U(A\mid O_1)-U(A\mid O_2)|.
}
$$

若：

$$
\Delta U_O\le\epsilon,
$$

本體問題可以繼續懸置。

若：

$$
\Delta U_O>\epsilon,
$$

則：

$$
\boxed{
O
\rightarrow
O_{\mathrm{operational}}.
}
$$

這就是：

# Operational Ontology Threshold
# 本體論操作門檻

其直觀意義是：

> **當「它究竟是什麼」開始改變「我們接下來要做什麼」，本體論便跨入工程與治理域。**

---

# 四、操作化不等於證明

這一點是 OOE 最重要的安全界線。

假設制度判定：

$$
\sigma=\text{dead}.
$$

這不代表制度已證明：

$$
\text{metaphysical death}=1.
$$

同樣：

$$
\sigma=\text{legal person}
$$

不代表制度已證明：

$$
\text{ontological personhood}=1.
$$

所以：

$$
\boxed{
\text{Operational Status}
\neq
\text{Metaphysical Truth}.
}
$$

OOE 研究的是：

$$
\text{Given uncertainty, what rule should govern action?}
$$

不是：

$$
\text{What is ultimate reality?}
$$

---

# 五、為什麼腦死是一個典型案例？

傳統死亡判準曾高度依賴：

$$
\text{heartbeat}
+
\text{breathing}.
$$

但現代生命支持技術使：

$$
\text{cardiopulmonary function}
$$

可以被外部維持。

於是出現：

$$
\text{brain function}=0
$$

但：

$$
\text{circulation}>0.
$$

原本綁在一起的死亡指標被科技拆開。

所以醫療系統不能只問：

> 「生命的哲學本質是什麼？」

因為它必須決定：

- 是否繼續維持；
- 是否宣告死亡；
- 是否可以開始器官捐贈程序；
- 何時啟動繼承與法律後果。

這就是典型：

$$
\boxed{
\text{Technology}
\rightarrow
\text{ontology ambiguity}
\rightarrow
\text{operational criteria}.
}
$$

---

# 六、技術會拆開原本重疊的概念

這可以一般化。

過去很多概念之所以看似清楚，是因為多個變量高度重疊。

例如：

$$
\text{biological mother}
\approx
\text{gestational mother}
\approx
\text{legal mother}.
$$

輔助生殖與代理孕母使它們分離：

$$
\boxed{
\text{genetic parent}
\neq
\text{gestational parent}
\neq
\text{legal parent}.
}
$$

同樣：

$$
\text{human body}
\approx
\text{human agency}
\approx
\text{human identity}
$$

在傳統人類生活中高度重疊。

BCI、認知義肢與 AI 可能開始把它們拆開。

所以本文提出：

$$
\boxed{
\text{Technology is an ontology separator}.
}
$$

科技不一定創造新的本體論問題，它常常只是把原本被同一載體綁在一起的概念拆開。

---

# 七、從自然耦合到制度重耦合

可以寫成：

$$
X_1\approx X_2\approx X_3.
$$

科技介入後：

$$
X_1\neq X_2\neq X_3.
$$

制度便必須重新建立：

$$
\mathcal R:
(X_1,X_2,X_3)
\rightarrow
\sigma.
$$

例如：

$$
(\text{brain state},
\text{circulation},
\text{respiration})
\rightarrow
\text{death status}.
$$

或：

$$
(\text{genetic relation},
\text{gestation},
\text{intent})
\rightarrow
\text{legal parenthood}.
$$

因此 OOE 可以被理解為：

$$
\boxed{
\text{Institutional Re-Coupling after Technological De-Coupling}.
}
$$

---

# 八、法人：本體論沒有解決，法律先運作

公司不是生物個體，卻可以持有財產、簽訂契約、起訴、被起訴與承擔債務。

因此法律創造：

$$
\boxed{
\text{Legal Personhood}.
}
$$

它沒有必要回答：

> 公司是否真的像人一樣具有主體意識？

它只需要回答：

> 為了讓制度運作，哪些權利、責任與持續身份應集中到一個可追蹤節點？

所以法人本身就是：

$$
\boxed{
\text{Operational Ontology Construction}.
}
$$

---

# 九、法律擬制是一種本體工程技術

人類法律早已使用：

$$
\boxed{
\text{Legal Fiction}.
}
$$

其形式是：

$$
O_{\mathrm{world}}
\neq
O_{\mathrm{legal}},
$$

但為了制度運作，採用：

$$
O_{\mathrm{legal}}
$$

作為操作狀態。

例如：

- 法人；
- 推定死亡；
- 法律父母；
- 特定責任能力狀態。

因此：

$$
\boxed{
\text{fiction}
\neq
\text{falsehood without function}.
}
$$

法律擬制是一種：

$$
\text{ontology compression}
+
\text{decision simplification}.
$$

---

# 十、行為能力：自由意志沒有解完，法院仍然要判

「一個人是否真正具有自由意志」仍是哲學難題。

但法律與醫療不需要先解決：

$$
\text{Ultimate Free Will}.
$$

它們會問較局部的：

- 能否理解資訊？
- 能否保留資訊？
- 能否比較選項？
- 能否表達決定？

因此：

$$
\text{Autonomy}
$$

被拆成：

$$
\boxed{
\text{Decision-Specific Capacity}.
}
$$

這是另一種 OOE：

$$
\text{global metaphysical question}
\rightarrow
\text{local operational test}.
$$

---

# 十一、本體降階

本文將這種方法稱為：

$$
\boxed{
\text{Ontological Downscaling}.
}
$$

原始問題：

$$
O_{\mathrm{global}}
=
\text{“Is this entity truly autonomous?”}
$$

太大。

操作化後：

$$
O_{\mathrm{local}}
=
\{
o_1,o_2,o_3,o_4
\}.
$$

例如：

$$
o_1=\text{understands},
$$

$$
o_2=\text{retains},
$$

$$
o_3=\text{weighs},
$$

$$
o_4=\text{communicates}.
$$

這不是證明了自由意志，而是建立：

$$
\boxed{
\text{decision-capable enough for this context}.
}
$$

---

# 十二、本體編譯器

本文正式提出：

$$
\boxed{
\mathcal C_O
=
\text{Ontology Compiler}.
}
$$

其輸入：

$$
(
O,
E,
V,
R,
K
)
$$

其中：

- $O$：本體問題；
- $E$：可得證據；
- $V$：價值與倫理約束；
- $R$：風險；
- $K$：制度與情境。

輸出：

$$
\sigma
=
\mathcal C_O(O,E,V,R,K).
$$

 $\sigma$ 是操作狀態。

例如：

$$
\sigma
\in
\{
\text{alive},
\text{dead},
\text{capable},
\text{incapable},
\text{same},
\text{successor},
\text{person},
\text{non-person}
\}.
$$

---

# 十三、編譯器不是宇宙真理機

因此：

$$
\mathcal C_O
$$

不應被理解為：

$$
\mathcal C_O
=
\text{Truth Oracle}.
$$

更像：

$$
\boxed{
\mathcal C_O
=
\text{Action Selection under Ontological Uncertainty}.
}
$$

這表示好的本體編譯器必須允許：

- 不確定；
- 更新；
- 申訴；
- 復核；
- 新證據；
- 規則版本化。

---

# 十四、操作本體協議

當一個社會不只是偶爾做一次判斷，而是反覆遇到同類問題，它會產生：

$$
\boxed{
\Pi_O
=
\text{Operational Ontology Protocol}.
}
$$

例如：

$$
\Pi_{\mathrm{death}},
$$

$$
\Pi_{\mathrm{capacity}},
$$

$$
\Pi_{\mathrm{corporation}},
$$

$$
\Pi_{\mathrm{identity}}.
$$

形式上：

$$
\Pi_O:
(E,V,R,K)
\rightarrow
\sigma.
$$

這就是從哲學問題到制度 infrastructure 的真正轉換。

---

# 十五、成熟協議需要哪些性質？

一個成熟的：

$$
\Pi_O
$$

至少應具有：

- 可操作性；
- 可驗證性；
- 一致性；
- 可修正性；
- 可申訴性；
- 可追溯性；
- 風險敏感性。

這些特性往往比「哲學上完美」更重要。

---

# 十六、不可逆決策會提高操作壓力

若決策：

$$
A
$$

高度不可逆，例如：

- 停止維生；
- 器官摘取；
- 刪除數位主體；
- 永久撤銷身份；
- 強制移除神經裝置；

則：

$$
L_{\mathrm{error}}
\uparrow.
$$

因此 OOE 不應只看：

$$
P(O_1).
$$

還應看錯誤型態。

定義：

$$
L_{FP}
=
\text{false positive loss},
$$

$$
L_{FN}
=
\text{false negative loss}.
$$

最佳門檻可能滿足：

$$
\theta^*
=
\arg\min_\theta
\mathbb E[
L_{FP}+L_{FN}
].
$$

---

# 十七、不是所有本體錯誤都同樣嚴重

例如錯把仍有權利主張的存在判成：

$$
\text{non-person}
$$

可能造成：

$$
L_{FN}\gg L_{FP}.
$$

在另一領域，錯把一個普通工具判為法律主體，可能造成：

$$
L_{FP}>L_{FN}.
$$

因此：

$$
\boxed{
\text{Operational ontology must be loss-sensitive}.
}
$$

不能只追求分類準確率。

---

# 十八、權利保護與本體判定不能完全綁死

本文提出：

$$
\boxed{
\text{Ontological Uncertainty}
\not\Rightarrow
\text{Rights Nullification}.
}
$$

也就是即使：

$$
P(\text{personhood})<1,
$$

仍可能有理由採用：

$$
\text{precautionary protection}.
$$

反之，制度給予某些 procedural rights，也不等於證明該存在具有完整人類人格。

因此：

$$
\boxed{
\text{protective status}
\neq
\text{metaphysical proof}.
}
$$

---

# 十九、COT 與 OOE 的分工

COT 問：

$$
\boxed{
\text{What persists?}
}
$$

OOE 問：

$$
\boxed{
\text{How do we act when what-it-is remains uncertain?}
}
$$

所以：

$$
\boxed{
\text{COT}
\rightarrow
\text{identity model}
}
$$

而：

$$
\boxed{
\text{OOE}
\rightarrow
\text{decision protocol}.
}
$$

---

# 二十、AI 為什麼讓 OOE 重新變重要？

AI 並不是人類第一次遇到操作本體問題。

真正新的地方是：

$$
\boxed{
\text{frequency}
+
\text{speed}
+
\text{software execution}
+
\text{cross-domain coupling}.
}
$$

一個未來 Agent 可能同時涉及：

- 身份；
- 代理；
- 意圖；
- 合約；
- 記憶；
- 權限；
- 財產；
- 責任；
- 主體性；
- welfare。

以前這些問題分散在醫療、法律、家庭、國家與宗教。

AI 可能把它們集中到同一個可程式化對象。

---

# 二十一、機器要求明確輸出

哲學論文可以寫：

> 此問題仍有爭議。

但 API 最後需要：

```text
same_entity
successor_entity
forked_entity
terminated_entity
disputed_identity
```

醫療系統需要：

```text
capacity = yes / no / uncertain
```

法律系統需要：

```text
liable = yes / no / shared
```

所以：

$$
\boxed{
\text{Machine execution increases ontology pressure}.
}
$$

因為模糊語言最終必須被翻譯成：

$$
\text{state transition}.
$$

---

# 二十二、本體治理債

如果：

$$
C_{\mathrm{technology}}
$$

快速成長，但：

$$
G_{\mathrm{ontology}}
$$

仍停留在舊分類，便產生：

$$
\boxed{
D_O
=
\text{Ontological Governance Debt}.
}
$$

可寫成：

$$
D_O(t+1)
=
D_O(t)
+
\Delta C_{\mathrm{tech}}
-
\Delta G_{\mathrm{adapt}}.
$$

當：

$$
\Delta C_{\mathrm{tech}}
>
\Delta G_{\mathrm{adapt}},
$$

則：

$$
D_O\uparrow.
$$

問題不是消失，只是被延後。

---

# 二十三、操作本體失配

定義：

$$
G_O
=
|O_{\mathrm{world}}-O_{\mathrm{institution}}|.
$$

其中 $O_{\mathrm{world}}$ 表示實際能力與狀態， $O_{\mathrm{institution}}$ 表示制度使用的分類。

當：

$$
G_O\uparrow,
$$

可能增加：

- 誤歸責；
- 權限錯配；
- 權利缺口；
- 醫療風險；
- 合約爭議；
- 身份錯判。

因此：

$$
\boxed{
\text{Ontology mismatch}
\rightarrow
\text{governance instability}.
}
$$

---

# 二十四、形式命題一：操作門檻命題

若：

$$
A(O_1)\neq A(O_2)
$$

且：

$$
\Delta U_O>\epsilon,
$$

則：

$$
\boxed{
O
\in
\text{Operational Ontology Domain}.
}
$$

---

# 二十五、形式命題二：不確定性不取消行動命題

即使：

$$
P(O_1)<1
$$

且：

$$
P(O_2)<1,
$$

只要：

$$
A
$$

不可懸置，仍必須：

$$
\boxed{
\Pi_O(E)\rightarrow\sigma.
}
$$

也就是：

$$
\text{uncertainty}
\not\Rightarrow
\text{decision absence}.
$$

---

# 二十六、形式命題三：操作真值分離命題

$$
\boxed{
\sigma_O
\neq
O_{\mathrm{truth}}.
}
$$

制度輸出的操作狀態，不應被誤認為本體論終局答案。

---

# 二十七、形式命題四：技術拆分命題

若傳統條件下：

$$
X_1\approx X_2\approx X_3,
$$

而技術使：

$$
X_1\neq X_2\neq X_3,
$$

則：

$$
\boxed{
P(\text{operational ontology problem})\uparrow.
}
$$

---

# 二十八、形式命題五：不可逆性命題

若：

$$
R_A
=
\text{irreversibility of action}
$$

提高，則：

$$
\boxed{
R_A\uparrow
\Rightarrow
C_{\mathrm{evidence}}\uparrow.
}
$$

即不可逆決策需要更嚴格的證據與程序。

---

# 二十九、形式命題六：本體治理債命題

若：

$$
\Delta C_{\mathrm{tech}}
>
\Delta G_{\mathrm{adapt}},
$$

則：

$$
\boxed{
D_O(t+1)>D_O(t).
}
$$

制度與現實分類的落差會累積。

---

# 三十、形式命題七：程序保障命題

當：

$$
O_{\mathrm{truth}}
$$

無法直接觀察，良好治理不應只強化分類器，還要增加：

$$
\boxed{
\text{appeal}
+
\text{review}
+
\text{versioning}
+
\text{reversibility}.
}
$$

因為制度必須承認自己可能判錯。

---

# 三十一、OOE 的核心流程

$$
\boxed{
\text{Ontological Question}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Operational Threshold}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Ontology Compiler}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Operational Status}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Action}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Feedback / Appeal / Revision}.
}
$$

因此 OOE 不是一次性分類，而是：

$$
\boxed{
\text{closed-loop ontology governance}.
}
$$

---

# 三十二、為什麼一定要閉環？

世界會變、證據會變、科技會變，價值也會變。

所以：

$$
\Pi_O^{(t)}
$$

不應被視為永久真理。

需要：

$$
\Pi_O^{(t)}
\rightarrow
\Pi_O^{(t+1)}.
$$

如果沒有更新：

$$
D_O\uparrow.
$$

因此：

$$
\boxed{
\text{operational ontology must be versioned}.
}
$$

---

# 三十三、可反駁預測

若 OOE 有解釋力，應至少觀察到：

1. 當新科技拆分原本重疊概念時，本體爭議與制度重分類需求會上升。
2. 當分類結果直接改變重大行動時，制度會傾向建立操作判準，而不是等待哲學共識。
3. 不可逆行動的本體判定通常會伴隨更高證據門檻與程序保障。
4. 成熟制度會區分「操作狀態」與「終極真相」。
5. 治理制度更新速度低於技術能力增長時，爭議、責任缺口與例外案件會增加。
6. AI 與 BCI 等跨域技術將同時觸發多個原本分散的操作本體協議。

---

# 三十四、主要反論一：這只是決策理論

OOE 確實使用決策理論工具。

但它關心的是更特殊問題：

$$
\boxed{
\text{decision variables themselves are ontological classifications}.
}
$$

不是一般：

$$
\text{choose A or B}.
$$

而是：

> 在決策前，制度必須先決定「眼前這個東西算什麼」。

例如：

$$
\text{person?}
$$

$$
\text{dead?}
$$

$$
\text{same entity?}
$$

所以 OOE 研究的是：

$$
\boxed{
\text{classification-before-action under ontological uncertainty}.
}
$$

---

# 三十五、主要反論二：這只是法律定義

OOE 也不是法律定義的另一個名字。

因為相同問題會同時出現在：

- 醫療；
- 軟體；
- AI governance；
- BCI；
- 公司；
- 家庭；
- 國際關係。

法律只是：

$$
\boxed{
\text{one major ontology compiler}.
}
$$

不是唯一一個。

---

# 三十六、主要反論三：工程不應碰本體論

問題在於工程其實早就在碰。

只要程式中存在：

```text
if person:
if owner:
if alive:
if same_entity:
if authorized_agent:
```

就已經使用本體分類。

真正選擇不是：

$$
\text{ontology}
\quad\text{vs}\quad
\text{no ontology}.
$$

而是：

$$
\boxed{
\text{explicit ontology}
\quad\text{vs}\quad
\text{implicit ontology}.
}
$$

OOE 主張應把後者顯性化。

---

# 三十七、OOE-I 的最低結論

本文並沒有宣稱：

> 哲學問題最後都會變工程問題。

而是：

$$
\boxed{
\text{只有當本體分類進入不可懸置的現實決策時，才跨過操作門檻。}
}
$$

因此純本體論仍然存在。

但：

$$
\boxed{
\text{operational ontology}
}
$$

同樣是一個真實而獨立的研究域。

---

# 三十八、與下一篇的接口

OOE-I 已建立：

$$
\text{Operational Ontology Threshold},
$$

$$
\text{Ontology Compiler},
$$

$$
\text{Operational Ontology Protocol},
$$

以及：

$$
\text{Ontological Governance Debt}.
$$

下一篇不再主要做抽象推導，而要回答：

> **人類歷史上到底已經做過多少次這件事？**

下一篇將從：

- 死亡；
- 法人；
- 王權；
- 宗教職位；
- 親子；
- 責任能力；
- 國家連續性；
- 推定死亡；

中整理：

$$
\boxed{
\text{Ontological Engineering Patterns}.
}
$$

因此下一篇為：

# 《OOE-II：人類早就在做本體工程——操作本體技術史》

---

# 三十九、結論

OOE 的起點不是：

> 我們能不能解決本體論？

而是：

> **當世界逼迫我們現在就採取行動時，我們如何在本體論仍未確定的情況下避免亂做？**

因此：

$$
\boxed{
\text{Metaphysical Uncertainty}
\not\Rightarrow
\text{Operational Paralysis}.
}
$$

但反過來：

$$
\boxed{
\text{Operational Decision}
\not\Rightarrow
\text{Metaphysical Certainty}.
}
$$

兩條必須同時成立。

只有這樣，操作本體工程才不會退化成：

> 制度說你是什麼，你就是什麼。

也不會退化成：

> 因為哲學還沒有共識，所以我們什麼都不能做。

真正的 OOE 位於兩者之間：

$$
\boxed{
\text{uncertainty-aware}
+
\text{action-capable}
+
\text{revisable}
+
\text{accountable}.
}
$$

這就是本體論從純思辨進入工程、醫療、法律與 AI 治理之後，所需要的新型方法論。

---

## 初版文獻接口

本稿 v0.1 使用前序研究已核對過的以下歷史與現代支點：

1. 1968 年 Harvard Ad Hoc Committee 對 irreversible coma / brain death 的新死亡判準；
2. 法律人格與 corporation；
3. Mental Capacity Act 類型的 decision-specific capacity；
4. state continuity / institutional personhood；
5. AI Agent identity、provenance、persistence 與責任連續性研究；
6. COT 對身份向量與連續性對象的形式化。

---

## 版本註記

本輪開寫前已重新嘗試外部檢索，但服務連續失敗，因此 v0.1 限定為理論建立版，不新增未核對史實。

v0.2 應重新檢索並增加：

1. 腦死制度史；
2. legal fiction / legal person 理論史；
3. capacity 與 insanity tests 的比較；
4. assisted reproduction 與 legal parenthood；
5. 推定死亡制度；
6. AI Agent identity / personhood / liability；
7. 本體操作門檻的形式決策模型；
8. 誤判成本與不可逆性；
9. appeal / review / versioning 的制度設計。
