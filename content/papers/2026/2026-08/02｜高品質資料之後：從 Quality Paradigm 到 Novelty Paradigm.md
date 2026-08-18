# 02｜高品質資料之後：從 Quality Paradigm 到 Novelty Paradigm
## Beyond High-Quality Data: From the Quality Paradigm to the Novelty Paradigm

**系列：**《可執行資料與深層解構學習》  
**篇次：** 02 / 10  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1 Research Draft  
**日期：** 2026-08-16  
**文件性質：** AI 資料理論／合成資料／新穎性搜尋／Quality-Diversity／可執行驗證  
**範圍聲明：** 本文討論一般 AI 資料、合成資料與可驗證生成，不涉及特定私人學術資料庫或特定資料格式商業化。  

---

## 摘要

AI 時代的資料研究長期以「高品質資料」為核心語言：乾淨、正確、去重、來源可靠、格式一致、標註準確的資料，被視為優質訓練資產。此一觀點在資料稀缺、人工標註昂貴、錯誤難以自動驗證的時代具有高度合理性。然而，當生成式模型開始大量產生候選資料，而程式執行、模擬器、形式驗證器、單元測試、狀態不變量與自動評測器可以快速排除大量錯誤候選時，「高品質」可能逐步由主要優化目標轉化為進場門檻。

本文提出「品質—新穎性相變命題」（Quality-to-Novelty Transition Hypothesis）：

$$
\boxed{
Q(x)\geq\tau_Q
\quad\Longrightarrow\quad
Q\text{ 由主要競爭維度逐步轉為 admission constraint}
}
$$

當大量資料都已通過最低有效性、可重現性與來源要求時，真正開始稀缺的可能不再是「資料是否足夠好」，而是：

$$
\boxed{
N(x\mid K_t)
}
$$

即候選資料 $x$ 相對於當前知識庫 $K_t$ 所增加的結構新穎性、行為新穎性、組合新穎性與可遷移新穎性。

本文區分「表面差異」與「結構新穎性」，指出重新命名、參數微調、文風變化與語句重寫並不足以構成高價值新穎資料。真正的新穎性必須與既有知識空間的結構距離、功能差異與可重用機制相關。

本文進一步吸收 Novelty Search、MAP-Elites 與 Quality-Diversity（QD）研究的思想，將資料選擇由單一品質排序改寫為「有效性門檻 + 新穎性／多樣性 + 局部品質」的多維搜索問題。本文同時加入 synthetic data 的限制：遞迴以模型生成資料取代真實資料可能造成分布尾部消失與 model collapse，因此「新穎資料範式」不是鼓勵無限制自我生成，而是要求保留真實基線、歷史樣本、分布覆蓋與可驗證增益。

本文最終提出「Verified Novelty Corpus」與「Executable Novelty Space」概念。其核心不是蒐集最多資料，而是建立一個由可驗證候選所構成、能度量彼此結構距離並持續向未知區域擴展的資料空間：

$$
\boxed{
\mathcal K_{t+1}
=
\mathcal K_t
\cup
\left\{
x:
x\in\mathcal A
\land
N(x\mid\mathcal K_t)\geq\tau_N
\right\}.
}
$$

這為後續遊戲解構、可執行因果資料、AI 生成新遊戲智能架構與意圖重建建立資料理論基礎。

**關鍵詞：** 高品質資料、新穎資料、Synthetic Data、Novelty Search、Quality-Diversity、MAP-Elites、Model Collapse、Executable Validation、資料選擇、AI 自我生成

---

# 1. 問題：如果所有候選都「品質很好」，還剩下什麼？

傳統資料工程常以：

$$
Q(x)
$$

表示某筆資料 $x$ 的品質。

 $Q$ 可以綜合：

- 正確性；
- 完整性；
- 一致性；
- 格式；
- 標註；
- 來源；
- 去重；
- 可讀性；
- 任務相關性。

因此典型的資料選擇問題可以表示為：

$$
\boxed{
\max_{x\in D}Q(x).
}
$$

這個思路在歷史上十分合理。

當人工標註昂貴、資料雜訊高、模型難以辨識錯誤時，優先提升 $Q$ 能有效改善模型。

DataComp-LM 的大規模受控實驗也顯示，資料集設計本身會顯著影響模型表現；其研究比較去重、filtering、mixing 等策略，並指出 model-based filtering 可以形成更有效的預訓練資料。

因此本文不是否定：

$$
\text{Quality matters}.
$$

本文提出的是另一個問題：

> 當生成與驗證成本都下降，且大量候選已經通過品質門檻時，單純繼續最大化品質是否仍是正確的資料選擇目標？

---

# 2. 生成成本下降造成的資料條件改變

令資料生成成本為：

$$
C_G(t).
$$

在生成式 AI 時代，可預期大量領域中：

$$
\frac{dC_G}{dt}<0.
$$

特別是在：

- 程式碼；
- 數學題；
- 模擬情境；
- 遊戲規則；
- 任務軌跡；
- synthetic QA；
- 軟體操作案例；
- scenario generation；

等領域，AI 可以快速產生候選。

因此資料瓶頸由：

$$
\boxed{
\text{Candidate Scarcity}
}
$$

逐步轉成：

$$
\boxed{
\text{Candidate Selection}.
}
$$

也就是：

> 我們不再缺候選，而是缺少判斷哪些候選值得保留的方法。

---

# 3. 驗證能力上升造成第二個條件改變

並非所有 AI 生成資料都可自動驗證。

但有一類領域具有高度有利的性質：

$$
\boxed{
\text{Executable Verifiability}.
}
$$

例如：

## 3.1 程式碼

可以使用：

- compiler；
- unit test；
- integration test；
- benchmark；
- fuzzing；
- static analysis。

## 3.2 數學與形式系統

部分問題可以使用：

- proof checker；
- CAS；
- theorem prover；
- symbolic verification。

## 3.3 遊戲與模擬

可以使用：

- game runtime；
- state invariant；
- replay；
- simulation；
- performance profiling；
- behavioral tests。

## 3.4 Agent 工作流

可以檢查：

- final state；
- tool output；
- database state；
- file state；
- task completion；
- transaction correctness。

當：

$$
C_V(t)
$$

表示驗證成本時，在上述領域亦可能出現：

$$
\frac{dC_V}{dt}<0.
$$

因此：

$$
\boxed{
C_G\downarrow
+
C_V\downarrow
}
$$

形成新的資料生產條件。

---

# 4. 品質從 Optimization Target 轉為 Admission Threshold

令 admissible set 為：

$$
\boxed{
\mathcal A_t
=
\left\{
x:
Q(x)\geq\tau_Q
\land
R(x)\geq\tau_R
\land
P(x)\geq\tau_P
\right\}.
}
$$

其中：

- $Q(x)$：品質／有效性；
- $R(x)$：可重現性；
- $P(x)$：來源、血緣或生成 provenance 完整度。

只有：

$$
x\in\mathcal A_t
$$

的候選才有資格進入下一階段。

在這個框架裡，品質依然重要。

但其角色改變了。

原本：

$$
\boxed{
Q=\text{Optimization Target}.
}
$$

逐漸變成：

$$
\boxed{
Q=\text{Admission Constraint}.
}
$$

也就是：

> 品質不夠，直接淘汰；品質夠了，再比較其他維度。

---

# 5. 為什麼「高品質」會出現範疇不足？

假設存在：

$$
x_1,x_2,\ldots,x_{1000000}
$$

且全部滿足：

$$
Q(x_i)\geq0.98.
$$

此時「品質高」已無法有效排序它們。

例如：

### 候選 A

已知演算法的變數重新命名。

### 候選 B

已知場景的文字改寫。

### 候選 C

已知行為樹只改一個 threshold。

### 候選 D

產生新的 scheduler + memory + interrupt 組合。

如果 A、B、C、D 都能通過格式與功能測試，則：

$$
Q(A)\approx Q(B)\approx Q(C)\approx Q(D).
$$

但顯然：

$$
N(D\mid K_t)
\gg
N(A\mid K_t).
$$

因此「品質」沒有錯。

錯的是把：

$$
\boxed{
\text{Validity}
}
$$

與：

$$
\boxed{
\text{Knowledge Gain}
}
$$

壓成同一個標量。

---

# 6. 新穎性不是「以前沒出現過這個字串」

最簡單的新穎性可以理解為：

$$
x\notin K_t.
$$

但這太弱。

假設：

```text
attack_power = 10
```

改成：

```text
attack_power = 11
```

雖然位元內容不同，但：

$$
N\approx0.
$$

同樣：

```text
Fireball
```

改成：

```text
Iceball
```

如果機制完全一致，亦不應視為高結構新穎性。

因此本文區分四種 novelty。

---

# 7. 四類新穎性

## 7.1 表面新穎性

$$
N_{\text{surface}}
$$

包括：

- 文字不同；
- 名稱不同；
- 圖像不同；
- 語法不同；
- 參數微調。

這是最容易大量生成的一類。

---

## 7.2 結構新穎性

$$
N_{\text{struct}}
$$

表示：

- graph topology 改變；
- subsystem 組成不同；
- dependency 不同；
- information flow 不同；
- state decomposition 不同；
- control structure 不同。

這比文字差異更重要。

---

## 7.3 行為新穎性

$$
N_{\text{behavior}}
$$

即在相同或相似環境下，系統產生新的行為軌跡。

令：

$$
\tau(x)
$$

為系統 $x$ 的 trajectory distribution。

則可比較：

$$
d_B(\tau(x_i),\tau(x_j)).
$$

---

## 7.4 功能／遷移新穎性

$$
N_{\text{transfer}}
$$

指某候選不只在單一 benchmark 有差異，而能提供新的：

- reusable primitive；
- composition；
- general rule；
- cross-domain mapping；
- failure recovery；
- adaptation strategy。

這通常是最有研究價值的一類。

---

# 8. 一個最小新穎性函數

令當前知識庫為：

$$
K_t=\{x_1,\ldots,x_n\}.
$$

對候選：

$$
x^\*
$$

可定義最簡距離式 novelty：

$$
\boxed{
N(x^\*\mid K_t)
=
\min_{x_i\in K_t}
d(x^\*,x_i).
}
$$

其中：

$$
d
$$

不應只使用文字 embedding 距離。

更合理的 $d$ 可以綜合：

$$
\boxed{
d
=
w_s d_{\text{struct}}
+
w_b d_{\text{behavior}}
+
w_f d_{\text{functional}}
+
w_c d_{\text{causal}}
}
$$

其中：

- $d_{\text{struct}}$：結構差異；
- $d_{\text{behavior}}$：行為差異；
- $d_{\text{functional}}$：功能差異；
- $d_{\text{causal}}$：因果機制差異。

---

# 9. Novelty Search：為什麼「不要只追最佳解」？

Lehman 與 Stanley 的 Novelty Search 提出一個反直覺思想：

> 在某些問題中，直接追逐單一 objective 可能造成 deceptive search；改為獎勵行為新穎性，反而能找到更有價值的解。

其核心不是：

$$
\max f(x)
$$

而是增加：

$$
\boxed{
\rho(x)=\text{behavioral novelty}.
}
$$

這與本文的資料問題具有高度類比性。

若所有候選都只依：

$$
Q(x)
$$

排序，生成系統可能快速收斂到：

$$
\boxed{
\text{High-Quality Repetition}.
}
$$

也就是：

> 每筆資料都很好，但它們彼此幾乎一樣。

---

# 10. Quality-Diversity：品質與多樣性不是二選一

Novelty Search 並不意味應永久放棄品質。

後續 Quality-Diversity（QD）研究更直接處理：

$$
\boxed{
\text{Quality}
+
\text{Diversity}.
}
$$

MAP-Elites 的重要思想之一，是不只尋找一個 global optimum，而是在不同 behavioral niches 中保存各自高表現的解。

因此，可將資料庫想像成：

$$
\mathcal B
=
\{
B_1,B_2,\ldots,B_m
\}
$$

每個 bin / niche：

$$
B_j
$$

保存該行為區域中最有價值的候選。

這意味著資料選擇問題可以從：

$$
\boxed{
\text{Find the best data}
}
$$

轉變成：

$$
\boxed{
\text{Fill the useful knowledge space with strong, diverse examples}.
}
$$

---

# 11. 從 High Quality Corpus 到 Quality-Diversity Corpus

傳統 corpus：

$$
D_Q
=
\operatorname{TopK}_{x\in D}Q(x).
$$

本文提出另一種構造：

$$
\boxed{
D_{QD}
=
\bigcup_{j=1}^{m}
\operatorname{Elite}(B_j).
}
$$

也就是：

> 不把所有容量浪費在同一種「好資料」上，而是在不同結構區域保留局部最優樣本。

對 AI 訓練而言，這可能意味：

- 不同策略；
- 不同錯誤模式；
- 不同架構；
- 不同時間尺度；
- 不同風格；
- 不同資源約束；
- 不同解題路徑；
- 不同失敗恢復方式。

---

# 12. 資料的新目標：Coverage

因此除了：

$$
Q
$$

與：

$$
N
$$

還需要：

$$
C=\text{Coverage}.
$$

令設計／行為空間為：

$$
\Omega.
$$

資料庫 $D$ 的覆蓋可以粗略表示為：

$$
\boxed{
C(D)
=
\frac{
\mu\left(
\bigcup_{x\in D}B_\epsilon(x)
\right)
}{
\mu(\Omega)
}.
}
$$

其中：

$$
B_\epsilon(x)
$$

為候選周圍的局部區域。

實務上不需要真的知道完整 $\Omega$。

我們可以持續估計：

> 還有哪些已知類型、狀態、行為與架構區域沒有樣本？

---

# 13. 合成資料最大的誘惑

生成式 AI 使以下循環非常誘人：

$$
M_t
\rightarrow
D_{t+1}^{syn}
\rightarrow
M_{t+1}
\rightarrow
D_{t+2}^{syn}
\rightarrow
\cdots
$$

也就是：

$$
\boxed{
\text{Model}
\rightarrow
\text{Synthetic Data}
\rightarrow
\text{Next Model}.
}
$$

若生成成本極低，似乎可以無限擴張資料。

但這裡存在重大限制。

---

# 14. Model Collapse：生成不等於創新

Shumailov 等人的研究指出，若生成模型持續以先前模型生成的資料進行遞迴訓練，可能出現 model collapse；資料分布尾部與低機率事件會逐步消失。

其他後續研究亦指出，synthetic data 的影響與 training workflow 有關；保留或累積 real data 與 synthetic data，可能比每輪完全以生成資料替換原資料穩定。

因此本文拒絕：

$$
\boxed{
\text{More Synthetic Data}
\Rightarrow
\text{More Knowledge}.
}
$$

甚至可能存在：

$$
\boxed{
\text{Synthetic Volume}\uparrow
\quad\land\quad
\text{Distributional Novelty}\downarrow.
}
$$

這是非常重要的反直覺情形。

---

# 15. Novelty Paradigm 不是「讓模型自己亂想」

本文所稱：

# Novelty Paradigm

不是：

> 不管對錯，只要以前沒看過就收。

真正條件是：

$$
\boxed{
\text{Validity}
\land
\text{Novelty}
\land
\text{Coverage Contribution}.
}
$$

更完整可以表示為：

$$
\boxed{
A(x)
=
\mathbf 1[
Q(x)\geq\tau_Q
]
\cdot
\mathbf 1[
R(x)\geq\tau_R
]
\cdot
\mathbf 1[
P(x)\geq\tau_P
].
}
$$

只有：

$$
A(x)=1
$$

才計算 novelty。

---

# 16. Verified Novelty Corpus

本文提出：

# **Verified Novelty Corpus, VNC**

令：

$$
\mathcal V_t
$$

為時間 $t$ 的已驗證新穎資料庫。

更新規則可寫為：

$$
\boxed{
\mathcal V_{t+1}
=
\mathcal V_t
\cup
\left\{
x:
A(x)=1
\land
N(x\mid\mathcal V_t)\geq\tau_N
\right\}.
}
$$

這裡：

- validity 決定能否進門；
- novelty 決定是否值得增加；
- quality 可在局部 niche 內決定是否替換既有樣本。

---

# 17. 局部 Elite 替換

如果：

$$
x
$$

與：

$$
y
$$

屬於同一 niche：

$$
B(x)=B(y),
$$

而：

$$
Q(x)>Q(y),
$$

則可以：

$$
\boxed{
x\succ y.
}
$$

保留 $x$ 作為該區域的新 elite。

因此資料庫不必永遠增長。

它可以：

$$
\boxed{
\text{Expand when novel}
+
\text{Replace when locally better}.
}
$$

這使資料庫同時具有：

- 增長；
- 壓縮；
- 更新；
- 去重；
- 競爭。

---

# 18. Executable Novelty Space

對於可執行系統，本文進一步提出：

# **Executable Novelty Space**

令候選系統：

$$
x
$$

經過：

$$
x
\xrightarrow{\text{compile}}
r_x
\xrightarrow{\text{execute}}
\tau_x
\xrightarrow{\text{evaluate}}
E_x.
$$

其中：

- $r_x$：runtime；
- $\tau_x$：行為軌跡；
- $E_x$：評測結果。

此時 novelty 不再只是語義距離。

可以直接比較：

$$
\boxed{
N_{\text{exec}}(x)
=
f(
\text{architecture},
\text{trajectory},
\text{resource use},
\text{failure modes},
\text{outcomes}
).
}
$$

---

# 19. 為什麼遊戲特別適合？

遊戲可以提供：

$$
\boxed{
S_t
+
A_t
+
T
+
R
+
G
+
E.
}
$$

其中：

- $S_t$：狀態；
- $A_t$：行動；
- $T$：轉移；
- $R$：規則；
- $G$：目標；
- $E$：評估。

因此 AI 可以生成一個新的遊戲 AI controller：

$$
\pi^\*,
$$

然後直接跑。

如果它：

- 能編譯；
- 不 crash；
- 不違反 invariant；
- 達成任務；
- 行為穩定；
- 與既有 controller 有結構或行為差異；

則：

$$
\pi^\*
$$

可以成為 VNC 候選。

---

# 20. 風格開始成為有效資料的另一個座標

當：

$$
Q(x)\geq\tau_Q
$$

且：

$$
N(x)\geq\tau_N,
$$

仍然可能存在大量候選。

例如兩個 NPC 系統：

$$
A
$$

與：

$$
B
$$

都能完成任務。

但：

- $A$ 保守；
- $B$ 冒險；
- $A$ 高效率；
- $B$ 高戲劇性；
- $A$ 可預測；
- $B$ 產生 emergent surprise。

因此還需要：

$$
\boxed{
S(x)=\text{Style / Value Coordinates}.
}
$$

這表示資料選擇最後可能不是一維 ranking。

而是：

$$
\boxed{
(Q,N,U,S,C)
}
$$

的多目標空間。

---

# 21. Pareto Frontier 取代單一總分

若：

$$
x
$$

在新穎性高、效率低；

而：

$$
y
$$

在效率高、新穎性低；

不一定存在：

$$
x>y.
$$

因此應保留：

$$
\boxed{
\mathcal P
=
\operatorname{ParetoFront}
(Q,N,U,S,C).
}
$$

也就是一批不同方向上具有價值的候選。

這與 Quality-Diversity 的精神高度相容。

---

# 22. 「新穎」也可能是垃圾

必須特別排除一個誤解。

如果 AI 生成：

- 無法執行；
- 隨機噪聲；
- 奇怪 graph；
- 無法完成任何任務；
- 沒有可解釋作用；

它可能離已知資料很遠：

$$
d(x,K_t)\gg0.
$$

但這不代表它有價值。

因此：

$$
\boxed{
\text{Distance}
\neq
\text{Useful Novelty}.
}
$$

真正需要的是：

$$
\boxed{
\text{Admissible Novelty}.
}
$$

即：

$$
N_A(x)
=
A(x)\cdot N(x).
$$

---

# 23. Novelty 與 Utility 也不可混淆

某個候選可能：

$$
N(x)\gg0
$$

但：

$$
U(x)\approx0.
$$

例如一個非常新的控制架構，但沒有任何實際優勢。

另一候選可能：

$$
N(y)\approx0.1
$$

但：

$$
U(y)\gg0.
$$

它只是已知架構的小改進，卻把成本降低 80%。

因此資料價值不應化約為 novelty。

本文提出：

$$
\boxed{
V(x)
=
f(
Q,N,U,C,S,T
)
}
$$

其中：

- $Q$：valid quality；
- $N$：novelty；
- $U$：utility；
- $C$：coverage contribution；
- $S$：style/value coordinate；
- $T$：transferability。

---

# 24. 從 Dataset 到 Explored Space

傳統 Dataset 是：

$$
D=\{x_1,\ldots,x_n\}.
$$

但 VNC 更像：

$$
\boxed{
\mathcal S_t
=
\text{Explored Knowledge / Design Space}.
}
$$

資料庫不只回答：

> 我們有多少筆資料？

而回答：

> 我們探索過哪些區域？

以及：

> 還有哪些區域是空白？

這會使資料工程開始接近：

$$
\boxed{
\text{Search Science}.
}
$$

---

# 25. 邊界推進

令：

$$
\partial\mathcal S_t
$$

表示當前已探索空間的邊界。

真正有研究價值的生成，可以理解為：

$$
\boxed{
x^\*
\in
\operatorname{Neighborhood}
(
\partial\mathcal S_t
)
}
$$

且：

$$
A(x^\*)=1.
$$

也就是：

> 不只是重複內部已知區域，而是在仍可驗證的前提下向外推進。

---

# 26. 人類資料與歷史資料仍然重要

Novelty Paradigm 絕不能被理解成：

> 以後全部使用 AI 自己生成的資料。

真實資料、歷史資料與人類產物具有至少三種重要作用：

## 26.1 Anchor

提供：

$$
\boxed{
\text{Distribution Anchor}.
}
$$

避免生成系統逐代偏離現實與歷史基線。

## 26.2 Tail Preservation

保留低頻但重要事件。

## 26.3 External Surprise

人類世界與自然世界可以持續提供模型本身未預期的新結構。

因此：

$$
\boxed{
D_{\text{real}}
+
D_{\text{historical}}
+
D_{\text{synthetic}}
}
$$

比：

$$
D_{\text{synthetic-only}}
$$

更符合本文框架。

---

# 27. 生成資料應保留 genealogy

每個 synthetic candidate 應至少保存：

```text
candidate_id
parent_ids
generator_model
generation_prompt
source_context
mutation_operator
validation_tests
novelty_score
niche_id
utility_score
accepted_or_rejected
rejection_reason
```

因此：

$$
\boxed{
\text{Synthetic Data}
}
$$

不是無來源資料。

它應具有：

$$
\boxed{
\text{Generation Provenance}.
}
$$

---

# 28. Rejected Data 也可能有研究價值

一般資料清理會丟棄：

$$
x_{\text{fail}}.
$$

但在生成—驗證研究中，失敗資料可記錄：

- deadlock；
- crash；
- unstable policy；
- reward hacking；
- bad composition；
- excessive resource use；
- pathological strategy。

因此可以建立：

$$
\boxed{
D^{-}
=
\text{Rejected / Failure Corpus}.
}
$$

這對 AI 學習：

> 哪些方向不要走。

非常重要。

---

# 29. 新穎性不是一次計算，而是動態量

如果今天：

$$
x
$$

是全新架構：

$$
N(x\mid K_t)\gg0.
$$

當未來有一萬個類似架構：

$$
N(x\mid K_{t+100})\downarrow.
$$

因此：

$$
\boxed{
N=N(x\mid K_t).
}
$$

Novelty 必須相對時間與 corpus 狀態定義。

這也是它與固定品質標籤的重要差異。

---

# 30. 資料庫會產生「邊際資訊收益遞減」

對第 $n$ 筆同類資料：

$$
\Delta I_n
$$

通常可能滿足：

$$
\Delta I_{n+1}<\Delta I_n.
$$

例如已經有：

$$
10000
$$

個近似 FSM combat example，

第：

$$
10001
$$

個若沒有新的機制，資訊增益可能接近零。

這表示：

$$
\boxed{
\text{Data Count}
\neq
\text{Knowledge Count}.
}
$$

---

# 31. AI 資料選擇器的未來任務

因此未來資料 curator 不應只問：

> 這筆資料好不好？

而應問：

1. 它是否合法進入有效域？
2. 它與現有資料有多重複？
3. 它補上哪一個 niche？
4. 它帶來什麼新 mechanism？
5. 它能否跨域遷移？
6. 它是否擴大 tail coverage？
7. 它是否只增加表面多樣性？
8. 它是否值得保留而非被更好的 local elite 取代？

---

# 32. 從 Data Cleaning 到 Knowledge Frontier Management

傳統資料工程：

$$
\boxed{
\text{Collect}
\rightarrow
\text{Clean}
\rightarrow
\text{Train}.
}
$$

本文提出未來可能逐漸變成：

$$
\boxed{
\text{Generate / Observe}
\rightarrow
\text{Validate}
\rightarrow
\text{Normalize}
\rightarrow
\text{Novelty Measure}
\rightarrow
\text{Niche Placement}
\rightarrow
\text{Elite Selection}
\rightarrow
\text{Frontier Expansion}.
}
$$

這不再只是 Data Cleaning。

而是：

# **Knowledge Frontier Management**

---

# 33. 命題一：品質門檻化命題

當候選生成與驗證能力足夠高，使大量資料滿足：

$$
Q(x)\geq\tau_Q,
$$

則品質逐漸由主要排序變數轉為 admission constraint。

---

# 34. 命題二：結構新穎性優先命題

在滿足最低有效性條件後，資料的邊際價值與：

$$
N_{\text{struct}},
N_{\text{behavior}},
N_{\text{transfer}}
$$

的關係，可能高於與表面差異的關係。

---

# 35. 命題三：Quality-Diversity Corpus 命題

在固定資料預算下：

$$
|D|=B,
$$

若任務需要廣泛泛化，則覆蓋多個有效 niche 的資料集可能優於大量集中於單一高品質模式的資料集。

此命題需要後續實驗驗證，不能直接視為普遍定理。

---

# 36. 命題四：Synthetic Recursion 約束命題

若 synthetic data 由模型遞迴生成，資料治理必須保留：

- real anchors；
- historical corpus；
- distribution tails；
- novelty tracking；
- provenance；
- independent validation。

否則生成規模增加不必然帶來知識增長。

---

# 37. 命題五：可執行新穎性命題

在具有 runtime verifier 的領域，新穎資料可以被更強地定義為：

$$
\boxed{
\text{Executable}
\land
\text{Valid}
\land
\text{Structurally Novel}.
}
$$

這類資料比單純文字層新穎性更容易建立客觀驗證閉環。

---

# 38. 與下一篇的連接

到此，系列已完成兩步：

第一篇建立：

$$
\boxed{
\text{Data}
\rightarrow
\text{Data Asset}.
}
$$

第二篇建立：

$$
\boxed{
\text{High-Quality Corpus}
\rightarrow
\text{Verified Novelty Space}.
}
$$

下一個問題是：

> 哪一種現成人類產物最適合產生大量「狀態—行動—規則—結果」可驗證資料？

遊戲是一個極為特殊的答案。

因為遊戲不是只有：

$$
\text{Content}.
$$

它還具有：

$$
\boxed{
\text{State}
+
\text{Action}
+
\text{Rule}
+
\text{Transition}
+
\text{Feedback}.
}
$$

因此下一篇將正式轉入：

# **03｜遊戲不是內容資料：遊戲作為可執行因果世界**

---

# 39. 結論

「高品質資料」不是錯誤概念。

但在生成與驗證能力高速提升後，它可能不足以描述新的資料選擇問題。

當：

$$
Q(x)\geq\tau_Q
$$

已變成大量候選的共同條件，新的稀缺量開始轉向：

$$
\boxed{
\text{Novelty}
+
\text{Coverage}
+
\text{Utility}
+
\text{Transferability}.
}
$$

真正成熟的生成式資料系統不應追求：

> 產生更多看起來正確的資料。

而應追求：

> 在保留真實基線、分布尾部與可驗證性的前提下，持續找到尚未被充分探索的新結構。

因此：

$$
\boxed{
\text{Data Engineering}
\rightarrow
\text{Search over Knowledge Space}.
}
$$

而對可執行系統而言，最終甚至可以形成：

$$
\boxed{
\text{Executable Novelty Space}.
}
$$

其資料不是靜態文本堆積，而是一個持續被生成、驗證、淘汰、分類、替換與向外推進的可計算設計空間。

---

# 參考資料

1. Li, J. et al. (2024). **DataComp-LM: In search of the next generation of training sets for language models.** NeurIPS 2024 Datasets and Benchmarks Track.  
   <https://arxiv.org/abs/2406.11794>  
   <https://proceedings.neurips.cc/paper_files/paper/2024/hash/19e4ea30dded58259665db375885e412-Abstract-Datasets_and_Benchmarks_Track.html>

2. Lehman, J., & Stanley, K. O. (2011). **Abandoning Objectives: Evolution Through the Search for Novelty Alone.** Evolutionary Computation, 19(2), 189–223.  
   <https://pubmed.ncbi.nlm.nih.gov/20868264/>

3. Mouret, J.-B., & Clune, J. (2015). **Illuminating search spaces by mapping elites.** arXiv:1504.04909.  
   <https://arxiv.org/abs/1504.04909>

4. Cully, A., & Demiris, Y. (2018). **Quality and Diversity Optimization: A Unifying Modular Framework.** IEEE Transactions on Evolutionary Computation, 22(2), 245–259.

5. Shumailov, I. et al. (2024). **AI models collapse when trained on recursively generated data.** Nature, 631, 755–759.  
   <https://doi.org/10.1038/s41586-024-07566-y>

6. Gerstgrasser, M. et al. (2024). **Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.** arXiv:2404.01413.  
   <https://arxiv.org/abs/2404.01413>

7. Kazdan, J. et al. (2024). **Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World.** arXiv:2410.16713.  
   <https://arxiv.org/abs/2410.16713>

8. Yang, X. et al. (2025). **Diversity-driven Data Selection for Language Model Tuning through Sparse Autoencoder.** arXiv:2502.14050.  
   <https://arxiv.org/abs/2502.14050>

---

## 系列導航

- 01｜AI 時代的資料資產：從「賣資料」到授權可計算知識
- 02｜高品質資料之後：從 Quality Paradigm 到 Novelty Paradigm
- 03｜遊戲不是內容資料：遊戲作為可執行因果世界
- 04｜商業遊戲智能考古：從 AI 名作到普通遊戲群
- 05｜遊戲解構經濟學：成本、難度、資訊增益與研究深度
- 06｜商業遊戲 AI 的隱藏層：真正稀缺的是組合，而非基礎演算法
- 07｜餵資料不等於學習：從 Raw Exposure 到深層解構學習
- 08｜理解的工程驗收：如果真的懂，就重建給我看
- 09｜合成資料之後：從模仿既有設計到探索新穎可執行設計空間
- 10｜慣老闆測試：意圖重建、設計生成與可執行世界考古
