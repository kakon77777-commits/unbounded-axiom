# 無損保存與近無損語義重建：GCMS 的雙軌記憶架構

> **系列**：可繼承的認知：從自我解構到遞歸生成式記憶系統（第 4 篇）  
> **作者**：Neo.K  
> **研究協作**：Aletheia（阿萊）  
> **版本**：v1.0  
> **日期**：2026-07-30  
> **文章類型**：命題猜想論文／技術理論論文

---

## 摘要

生成式記憶系統經常同時追求兩個表面上相似、實際上不同的目標：第一，保存並精確恢復原始內容；第二，以較低成本保存其意義、結構與生成關係，並在需要時重新建構可用知識。若不區分這兩個目標，系統很容易把「語義上合理的再生成」誤稱為「原文還原」，或為了保證逐字可逆而完全失去壓縮、抽象、組合與遷移能力。

本文提出 GCMS 的「雙軌記憶架構」。原文無損軌以可逆壓縮、內容定址、版本快照、密碼雜湊與來源證據為核心，要求解碼結果與原始內容逐位元一致；語義生成軌則以生成核、語義指紋、關係圖、結構摘要、命題不變量與任務條件為核心，追求在有限表示率下最小化任務相關失真。兩軌不是彼此取代，而是透過證據映射、版本映射與引用映射耦合：原文軌回答「曾經確切存在的是什麼」，語義軌回答「它意味著什麼、如何被提取、重建、比較與再利用」。

本文首先證明一項基本限制：若語義壓縮映射不是單射，則不存在能對所有原文保證逐字正確的唯一解碼器；因此任何刪除原文、只保留摘要、向量或生成核的系統，都不能宣稱普遍的無損還原。本文進一步提出雙軌可恢復命題、證據約束重建命題、版本差分保真命題、失真可分解命題與校驗增益命題，並定義位元恢復率、來源完整性、語義不變量覆蓋率、證據覆蓋率、版本可定位率、重建校準度與雙軌總成本。最後，本文提出一套可否證的比較實驗，用以檢驗純封存、純語義與雙軌系統在精確恢復、新問題遷移、錯誤辨識及長期漂移上的差異。

本文主張：GCMS 所追求的「接近無損」不應被理解為用一個神奇的低維表示逐字再造所有原文，而應被理解為兩種保真性的聯合——原文軌提供可驗證的零失真恢復，語義軌使核心命題、關係、生成路徑與可用性在壓縮與重建後盡可能保持不變。

**關鍵詞**：GCMS、無損壓縮、語義壓縮、率失真理論、內容定址、證據鏈、生成式記憶、近無損重建、版本治理、雙軌記憶

---

## 一、問題的提出：兩種「還原」被混在了一起

設原始知識作品為：

$$
x\in\mathcal X,
$$

它可以是一篇論文、一份技術白皮書、一段程式、一組實驗紀錄或多模態研究材料。

當系統聲稱自己可以「壓縮並還原」作品時，至少可能指涉三種不同要求：

1. **位元級還原**：重新取得與原始檔案完全相同的位元序列；
2. **內容級還原**：文字、公式、圖表、程式與章節內容相同，但容器格式或中繼資料可不同；
3. **語義級重建**：核心命題、方法、關係與結論被保留，但表達形式可能不同。

三者可寫成：

$$
\widehat x_{\mathrm{bit}}=x,
$$

$$
\operatorname{Content}(\widehat x_{\mathrm{content}})
=
\operatorname{Content}(x),
$$

以及：

$$
\mathcal I_{\mathrm{critical}}(x)
\subseteq
\mathcal I(\widehat x_{\mathrm{sem}}),
$$

其中 $\mathcal I(x)$ 表示作品的語義不變量集合。

若不區分這三種要求，就會出現兩種相反錯誤。

第一種錯誤是把流暢、合理且大致相符的生成內容稱為「無損還原」。例如，系統只保存摘要、向量與若干關鍵詞，之後生成一篇內容相近的文章；即使核心意思相符，它也未必等同原文。

第二種錯誤則是只承認逐位元恢復才算記憶，因而否定摘要、生成核、概念圖、語義索引與重建程序的價值。這會使記憶系統只能保存，不能抽象、遷移、組合或協助推理。

GCMS 若要同時成為可靠的知識封存系統與可運行的生成式認知基礎設施，就必須將兩種保真性分開：

$$
\boxed{
\text{原文無損保真}
\neq
\text{語義近無損保真}
}
$$

但同時也必須使它們可互相校驗：

$$
\boxed{
\text{可靠的生成式記憶}
=
\text{無損來源軌}
+
\text{語義生成軌}
+
\text{證據耦合層}
}
$$

---

## 二、研究背景：從精確重現到允許失真的傳輸

### 2.1 無損信源編碼：統計冗餘可以被移除，但資訊不能被刪除

Shannon 的資訊理論將通訊問題形式化為：從可能訊息集合中選出一個訊息，經編碼、通道與解碼後，在接收端精確或近似重現。[1] 對離散無記憶信源而言，無損信源編碼可以利用符號分布與統計冗餘降低平均碼長，但在可唯一解碼的前提下，不能任意刪除區分不同訊息所需的資訊。

設無損編碼器與解碼器為：

$$
C_0:\mathcal X\rightarrow\mathcal Z_0,
$$

$$
D_0:\mathcal Z_0\rightarrow\mathcal X.
$$

零失真要求：

$$
D_0(C_0(x))=x,
\qquad
\forall x\in\mathcal X.
$$

若作品被正規化為位元序列 $b(x)$ ，則可用密碼雜湊檢查恢復完整性：

$$
H(b(x))
=
H(b(D_0(C_0(x)))).
$$

這裡的雜湊不是壓縮原文本身，而是完整性承諾。它能高機率辨識內容是否改變，卻不能只靠雜湊值反推出原文。

因此：

$$
\boxed{
\text{雜湊可驗證完整性，不能取代內容保存。}
}
$$

### 2.2 率失真理論：允許失真後，壓縮目標才具有任務選擇性

Shannon 後續以保真準則建立率失真理論，研究在容許平均失真 $D$ 時，表示來源所需的最低資訊率。[2]

其一般形式為：

$$
R(D)
=
\min_{p(\widehat x\mid x):
\mathbb E[d(x,\widehat x)]\leq D}
I(X;\widehat X),
$$

其中：

- $R(D)$ ：在失真限制 $D$ 下所需的最小表示率；
- $d(x,\widehat x)$ ：原始內容與重建內容間的失真函數；
- $I(X;\widehat X)$ ：原始變量與重建變量間的互資訊。

無損情況可被視為：

$$
D=0,
$$

而語義壓縮則允許某些表面差異，只要任務相關結構被保留。

關鍵並不只是「可以丟失多少」，而是：

$$
\boxed{
\text{哪些差異被視為失真？}
}
$$

若失真函數只衡量字元差異，改寫一句話就可能被視為高失真；若失真函數衡量命題、因果與方法是否保持，完全不同措辭仍可能是低語義失真。這表示任何「近無損語義」主張，都必須先公開其保真準則，而不能只憑主觀感覺判斷。

### 2.3 語義壓縮：失真函數由任務、模型與知識背景決定

Nagy、Török 與 Orbán 將率失真框架用於情節記憶，主張語義記憶所形成的環境模型可以決定哪些變化重要、哪些內容可由背景知識重新預測。[3][4]

對知識作品，可將語義失真寫為：

$$
d_{\mathrm{sem}}(x,\widehat x\mid q,K)
=
\sum_{j=1}^{m}
w_j(q,K)\,
\delta_j(x,\widehat x),
$$

其中：

- $q$ ：當前任務或查詢；
- $K$ ：接收者既有知識；
- $\delta_j$ ：第 $j$ 類語義差異；
- $w_j$ ：該差異在當前任務下的權重。

例如，對數學論文而言，定義、量詞、假設與符號方向通常具有高權重；對概念性文章而言，論證路徑與邊界條件可能比逐句措辭更重要。

因此：

$$
d_{\mathrm{sem}}
\neq
d_{\mathrm{lexical}}.
$$

但語義壓縮同時帶來圖式化失真：系統可能把不符合既有模型的細節刪除，或用更典型、但並非原始內容的結構補全空缺。[3][4]

### 2.4 生成式重建：可預測部分由模型重建，獨特殘差需要額外保存

生成式記憶模型指出，情節的部分內容可由較慢的生成模型學習並重建，而獨特、不可預測的細節仍需要情節痕跡或外部來源提供。[5][6]

可將作品寫為：

$$
x
=
G(z,\theta)
+
\varepsilon,
$$

其中：

- $z$ ：共享生成核；
- $\theta$ ：作品條件與版本參數；
- $G$ ：生成程序；
- $\varepsilon$ ：不能由共享模型可靠預測的特有殘差。

若只保存 $z$ 與 $\theta$ ，就可能重建作品的大致結構；但若 $\varepsilon$ 被刪除，則無法保證原文級恢復。

這導出 GCMS 的第一項工程原則：

$$
\boxed{
\text{生成模型可以降低提取成本，不能取代不可預測殘差的保存。}
}
$$

### 2.5 外部非參數記憶：生成系統需要可更新、可引用的來源層

REALM 與 RAG 等研究將模型內部參數記憶與外部可檢索文件結合，以改善知識更新、可解釋性與知識密集任務表現。[7][8] 後續的證據導向生成研究則指出，檢索到內容不代表內容真正支持輸出；系統仍需判斷證據是否與生成結論具有支持關係。[9]

這些研究對 GCMS 的意義不是「接入 RAG 就已經保證正確」，而是支持以下區分：

$$
\text{模型內生成能力}
\neq
\text{外部事實來源},
$$

以及：

$$
\text{已檢索}
\neq
\text{已支持}.
$$

GCMS 因此需要比普通檢索更強的證據耦合：每一項重建內容應能追溯到來源、版本、位置與內容雜湊。

### 2.6 內容定址、Merkle 結構與時間戳：保存的是可驗證對象，而非可變位置

內容定址系統以內容本身的雜湊作為識別基礎；IPFS 的設計以內容定址區塊與 Merkle DAG 建立可版本化、可驗證的資料關係。[10] Haber 與 Stornetta 的數位時間戳研究，以及其後以樹狀結構提升效率的工作，則說明雜湊鏈與聚合證明如何用於證明文件在特定狀態下已存在且未被事後修改。[11][12]

這些技術不能單獨證明作者身份、內容真實性或理論正確性，但可以證明：

$$
\text{目前內容是否與已承諾內容一致}.
$$

因此，GCMS 的原文軌需要同時保存：

- 內容；
- 內容雜湊；
- 版本關係；
- 來源位置；
- 建立與修改事件；
- 可選的簽章與時間承諾。

---

## 三、基本限制：語義表示不能普遍保證逐字還原

### 3.1 語義壓縮非單射命題

設語義壓縮器為：

$$
C_s:\mathcal X\rightarrow\mathcal Z_s.
$$

若存在兩個不同作品：

$$
x_1\neq x_2,
$$

但：

$$
C_s(x_1)=C_s(x_2)=z,
$$

則 $C_s$ 不是單射。

對任意確定性解碼器：

$$
D_s:\mathcal Z_s\rightarrow\mathcal X,
$$

$D_s(z)$ 只能輸出一個結果，因此不可能同時滿足：

$$
D_s(C_s(x_1))=x_1,
$$

以及：

$$
D_s(C_s(x_2))=x_2.
$$

故有：

> **命題 1：若語義壓縮映射不是單射，則不存在能對所有輸入保證逐字無損恢復的唯一解碼器。**

這不是實作不足，而是資訊丟失後的識別不可能性。

若 $\mathcal X$ 與 $\mathcal Z_s$ 為有限集合，且：

$$
|\mathcal Z_s|<|\mathcal X|,
$$

則依鴿籠原理， $C_s$ 必然不是單射。

因此，任何只保存摘要、低維向量、標籤、生成核或概念圖的系統，都不能對任意原文宣稱：

$$
\widehat x=x.
$$

### 3.2 雜湊也不能用來反向還原內容

密碼雜湊函數：

$$
H:\mathcal X\rightarrow\{0,1\}^{n}
$$

將任意長內容映射到固定長度輸出。它的用途是驗證，而不是解碼。

即使在實務上難以找到碰撞，固定長度輸出仍不足以包含所有任意長輸入的可逆資訊。因此：

$$
D_H(H(x))=x
$$

不存在一般解。

GCMS 必須保存原文或某種可逆編碼，而不能把 SHA-256 當作原文的替代品。

### 3.3 「接近無損」必須先指定在哪個空間接近

可分別定義：

$$
D_{\mathrm{bit}}(x,\widehat x),
$$

$$
D_{\mathrm{content}}(x,\widehat x),
$$

$$
D_{\mathrm{sem}}(x,\widehat x),
$$

$$
D_{\mathrm{task}}(x,\widehat x\mid q).
$$

同一重建結果可能具有：

$$
D_{\mathrm{bit}}>0,
$$

但：

$$
D_{\mathrm{sem}}\approx0.
$$

例如，同一命題被改寫成另一種句型時，位元與詞彙完全不同，語義卻近似相同。

相反地，一個只改動否定詞、量詞或公式方向的版本，可能具有很低的字元差異，卻具有極高語義失真。

因此：

$$
\boxed{
\text{近無損是一個相對於失真函數的主張。}
}
$$

---

## 四、GCMS 雙軌記憶架構

### 4.1 系統狀態

對作品 $x_i$ ，GCMS 保存：

$$
M_i
=
\left(
A_i,
S_i,
E_i,
V_i,
P_i
\right),
$$

其中：

- $A_i$ ：原文無損封存；
- $S_i$ ：語義生成表示；
- $E_i$ ：證據與引用映射；
- $V_i$ ：版本與差分結構；
- $P_i$ ：權限、來源與治理政策。

整體記憶空間為：

$$
\mathcal M
=
\mathcal A
\oplus
\mathcal S
\oplus
\mathcal E
\oplus
\mathcal V
\oplus
\mathcal P.
$$

### 4.2 原文無損軌

原文軌的核心目標是：

$$
D_A(C_A(x_i))=x_i.
$$

它可以使用：

- 一般可逆壓縮；
- 區塊去重；
- 差分版本；
- 內容定址；
- Merkle 結構；
- 不可變快照；
- 簽章與時間承諾；
- 多副本與備份。

原文軌不負責理解。它只回答：

> 在某個版本、某個時間與某個來源下，確切保存的內容是什麼？

原文軌的基本記錄可寫為：

$$
A_i
=
\left(
\operatorname{bytes}_i,
h_i,
\mu_i,
\tau_i,
\sigma_i
\right),
$$

其中：

- $\operatorname{bytes}_i$ ：可逆保存內容；
- $h_i$ ：內容雜湊；
- $\mu_i$ ：格式與正規化中繼資料；
- $\tau_i$ ：版本時間與事件；
- $\sigma_i$ ：可選簽章或承諾。

### 4.3 語義生成軌

語義軌的核心不是逐字復原，而是支援：

- 辨認；
- 尋址；
- 概述；
- 結構重建；
- 新問題遷移；
- 跨作品比較；
- 生成與組合。

可寫為：

$$
S_i
=
\left(
q_i,
g_i,
f_i,
r_i,
\mathcal I_i,
\pi_i
\right),
$$

其中：

- $q_i$ ：起源問題；
- $g_i$ ：生成核；
- $f_i$ ：語義指紋；
- $r_i$ ：關係圖位置；
- $\mathcal I_i$ ：關鍵不變量；
- $\pi_i$ ：生成與提取程序。

語義解碼依賴查詢與接收者背景：

$$
\widehat x_i^{\mathrm{sem}}
=
D_S(S_i,q,K,c),
$$

其中 $c$ 是當前情境。

因此語義重建不是唯一函數，而是條件式生成：

$$
P(\widehat x\mid S_i,q,K,c).
$$

### 4.4 證據耦合層

證據層將生成內容映射回原文片段：

$$
E_i:
\mathcal Y_i
\rightarrow
2^{\mathcal A_i},
$$

其中 $\mathcal Y_i$ 是由作品產生的命題、摘要或重建片段集合。

對生成命題 $y_j$ ，證據記錄可表示為：

$$
e_j
=
\left(
\operatorname{source\_id},
\operatorname{version},
\operatorname{span},
\operatorname{hash},
\operatorname{relation}
\right).
$$

其中 `relation` 至少區分：

- 直接陳述；
- 可由來源推導；
- 背景支持；
- 衝突；
- 無證據推測。

這使 GCMS 可以區分：

$$
\text{來源原文},
\quad
\text{結構化重述},
\quad
\text{合理推論},
\quad
\text{新生成假說}.
$$

### 4.5 版本軌

作品不是靜態對象，而是版本序列：

$$
V_i
=
\left
\{
 x_i^{(0)},
x_i^{(1)},
\ldots,
x_i^{(T)}
\right\}.
$$

若相鄰版本高度相似，可保存基線與差分：

$$
x_i^{(t+1)}
=
\operatorname{Patch}
\left(
 x_i^{(t)},
\Delta_i^{(t\rightarrow t+1)}
\right).
$$

只要基線與每個差分均被無損保存，版本鏈仍可精確還原。

但若只保存「這一版大致修改了什麼」的自然語言摘要，則只能提供語義版本記憶，不能保證重建原版本。

---

## 五、三種重建模式

GCMS 不應只有一個模糊的 `reconstruct` 操作，而應明確區分三種模式。

### 5.1 精確恢復模式

輸入：原文軌中的可逆內容或完整版本鏈。

輸出：

$$
\widehat x_i^{(0)}=x_i.
$$

驗證：

$$
H(\widehat x_i^{(0)})=H(x_i).
$$

此模式禁止生成模型修改內容。

### 5.2 結構重建模式

輸入：語義軌表示與可檢索原文片段。

輸出可能是：

- 結構摘要；
- 章節骨架；
- 命題表；
- 方法流程；
- 關係圖；
- 記憶包。

要求：

$$
\mathcal I_{\mathrm{critical}}(x_i)
\subseteq
\mathcal I(\widehat x_i^{(1)}),
$$

並且每個關鍵命題都有證據映射。

### 5.3 生成擴展模式

輸入：語義表示、外部證據、當前問題與組合算子。

輸出：新論文草稿、新假說、跨系列組合或研究路徑。

形式上：

$$
y
=
G
\left(
S_{i_1},\ldots,S_{i_k},
q,
E
\right).
$$

但它必須被標記為：

$$
y\in\mathcal M_{\mathrm{candidate}},
$$

而不是：

$$
y\in\mathcal M_{\mathrm{source}}.
$$

這一區分為後續「記憶污染與三區治理」提供基礎。

---

## 六、核心命題與猜想

### 6.1 雙軌可恢復命題

> 若原文軌對每個版本保存可逆表示，且內容雜湊、格式資訊與版本鏈完整，則系統可提供位元或內容級零失真恢復；語義軌的存在不會降低此可恢復性，反而可以降低尋址與理解成本。

形式上，若：

$$
D_A(C_A(x_i^{(t)}))=x_i^{(t)},
$$

則：

$$
\operatorname{Recover}
\left(
M_i,t
\right)
=x_i^{(t)}.
$$

語義軌只影響：

$$
\operatorname{Locate},
\operatorname{Explain},
\operatorname{Compare},
\operatorname{Compose},
$$

不改變原文恢復函數。

### 6.2 證據約束重建命題

> 在相同生成模型下，若重建輸出必須對關鍵命題提供版本化原文證據，則其來源混淆率與無支持生成率應低於不受證據約束的重建。

設：

$$
\rho_{\mathrm{unsupported}}(Y)
=
\frac{
|\{y_j\in Y:E(y_j)=\varnothing\}|
}{|Y|}.
$$

則猜想：

$$
\mathbb E
\left[
\rho_{\mathrm{unsupported}}
\mid
\text{evidence-constrained}
\right]
<
\mathbb E
\left[
\rho_{\mathrm{unsupported}}
\mid
\text{unconstrained}
\right].
$$

但若檢索到的來源本身錯誤或不相關，證據鏈也可能只是把錯誤變得更可追溯，而非自動變正確。

### 6.3 版本差分保真命題

> 若版本基線與差分均為可逆且順序完整，則差分保存可以降低冗餘而不降低版本恢復保真度。

若：

$$
x^{(t+1)}
=
P(x^{(t)},\Delta_t),
$$

且 $P$ 可確定性重播，則：

$$
\operatorname{Replay}
\left(
 x^{(0)},
\Delta_0,\ldots,\Delta_{t-1}
\right)
=x^{(t)}.
$$

若任何差分缺失或順序錯誤，則後續版本可恢復性可能連鎖失敗；因此需要週期性完整快照，避免單一長鏈成為脆弱點。

### 6.4 失真可分解命題

GCMS 的重建錯誤可分解為：

$$
D_{\mathrm{total}}
=
\lambda_A D_A
+
\lambda_S D_S
+
\lambda_E D_E
+
\lambda_V D_V
+
\lambda_Q D_Q,
$$

其中：

- $D_A$ ：原文保存或解碼錯誤；
- $D_S$ ：語義表示遺漏或扭曲；
- $D_E$ ：證據映射錯誤；
- $D_V$ ：版本定位錯誤；
- $D_Q$ ：查詢與任務錯配。

這使系統不必把所有錯誤都歸因於「模型幻覺」。例如，輸出錯誤可能源於找到錯版本、證據跨度截斷、原文已損壞，或語義摘要忽略了限定條件。

### 6.5 外部校驗增益命題

設純語義重建準確率為：

$$
F_S,
$$

加入原文證據與版本校驗後的準確率為：

$$
F_{A+S+E}.
$$

定義外部校驗增益：

$$
G_{\mathrm{verify}}
=
F_{A+S+E}-F_S.
$$

本文猜想，對版本密集、符號敏感、法規性或數學性內容：

$$
G_{\mathrm{verify}}>0,
$$

且其增益高於對低風險概述任務的增益。

### 6.6 雙軌成本前沿猜想

雙軌系統並非免費。設：

$$
C_{\mathrm{total}}
=
C_A+C_S+C_E+C_V+C_G,
$$

其中 $C_G$ 是治理成本。

純原文封存的成本主要集中於儲存與尋址；純語義系統的成本主要集中於失真與來源風險；雙軌系統則增加索引、版本及證據維護成本。

本文提出：存在一個雙軌 Pareto 前沿，使系統無法在不增加任何成本的情況下，同時提升精確恢復、語義遷移、證據完整性與更新速度。

$$
\mathcal P_{\mathrm{dual}}
=
\left\{
M
\mid
\nexists M'
\text{ 可在不增加成本下全面支配 }M
\right\}.
$$

---

## 七、雙軌保真指標

### 7.1 位元恢復率

$$
F_{\mathrm{bit}}
=
\frac{1}{N}
\sum_{i=1}^{N}
\mathbf 1
\left[
H(\widehat x_i)=H(x_i)
\right].
$$

### 7.2 來源完整性率

$$
F_{\mathrm{source}}
=
\frac{
\text{可定位且雜湊驗證成功的來源數}
}{
\text{應保存來源總數}
}.
$$

### 7.3 語義不變量覆蓋率

$$
F_{\mathcal I}
=
\frac{
|\mathcal I_{\mathrm{critical}}(x)
\cap
\mathcal I(\widehat x)|
}{
|\mathcal I_{\mathrm{critical}}(x)|
}.
$$

### 7.4 證據覆蓋率

$$
F_E
=
\frac{
\text{具有有效來源證據的關鍵命題數}
}{
\text{關鍵命題總數}
}.
$$

### 7.5 版本可定位率

$$
F_V
=
\frac{
\text{正確識別目標版本的查詢數}
}{
\text{版本敏感查詢總數}
}.
$$

### 7.6 重建校準度

若系統對命題 $y_j$ 給出信心 $p_j$ ，其實際正確性為 $a_j\in\{0,1\}$ ，可計算校準誤差：

$$
\operatorname{ECE}
=
\sum_{b=1}^{B}
\frac{|S_b|}{n}
\left|
\operatorname{acc}(S_b)
-
\operatorname{conf}(S_b)
\right|.
$$

雙軌系統不只要提高正確率，也應使「不知道」與「只有語義推測」能被正確標示。

### 7.7 雙軌壓縮率

設原始總大小為 $L_X$ ，無損軌、語義軌與索引證據層大小分別為 $L_A,L_S,L_E$ ，則：

$$
\operatorname{CR}_{\mathrm{dual}}
=
\frac{L_A+L_S+L_E}{L_X}.
$$

若 $L_A$ 已使用去重與差分，則雙軌總大小未必遠大於原始作品總量；但語義索引與證據映射仍會產生額外成本。

---

## 八、實驗設計與可否證條件

### 8.1 三系統比較

建立相同作品集，分成：

- $M_A$ ：只有原文無損封存；
- $M_S$ ：只有語義壓縮表示；
- $M_D$ ：雙軌系統。

測試任務包括：

1. 精確恢復舊版本；
2. 找出某命題的原始段落；
3. 概述作品核心方法；
4. 回答作品未直接回答、但可由結構推導的新問題；
5. 區分原文與後續生成內容；
6. 偵測不同版本中的關鍵改動。

預測：

- $M_A$ 在精確恢復上最佳，但新問題遷移較弱；
- $M_S$ 在低成本概述與遷移上較好，但不能保證精確恢復；
- $M_D$ 在總體任務效用與錯誤可追溯性上較高，但儲存及治理成本也較高。

### 8.2 語義壓縮消融

逐步移除：

- 生成核；
- 關係圖；
- 關鍵不變量；
- 版本資訊；
- 證據映射。

觀察：

$$
\Delta F_{\mathcal I},
\quad
\Delta F_E,
\quad
\Delta F_V,
\quad
\Delta\operatorname{ECE}.
$$

若移除上述結構不影響任何任務，則本文對語義軌必要性的部分主張應被削弱。

### 8.3 近似表達與關鍵微差測試

建立兩組對照：

- 語句不同但命題等價；
- 語句極相似但量詞、否定、條件或公式方向不同。

測試系統是否能避免：

$$
\text{詞彙相似}
\Rightarrow
\text{語義相同}
$$

的錯誤推論。

### 8.4 長期版本漂移

讓同一作品經歷多輪修改，並在不同時間點重建：

- 初版；
- 中間版；
- 最新版；
- 某一特定命題第一次出現的版本。

若 GCMS 經常把新版內容投射到舊版，則版本軌與證據耦合尚未達標。

### 8.5 重建污染測試

讓系統生成候選擴展，再把候選內容重新加入檢索環境。測試下一輪是否能區分：

$$
\mathcal M_{\mathrm{source}},
\quad
\mathcal M_{\mathrm{candidate}},
\quad
\mathcal M_{\mathrm{accepted}}.
$$

若候選內容被錯當成歷史原文，則雙軌設計仍不足以防止遞歸污染。

### 8.6 否證條件

本文至少在下列情況下應被修正：

1. 純語義低維表示能在一般大型開放作品域中穩定逐字恢復所有原文，且不保存等價資訊量；
2. 證據約束無法降低來源混淆或無支持生成；
3. 雙軌系統在所有任務上都被純原文或純語義系統支配；
4. 語義不變量無法被可靠定義或跨評估者取得可接受一致性；
5. 版本與證據治理成本高到抵消所有檢索、重建與遷移收益。

---

## 九、失敗模式與治理邊界

### 9.1 把語義重建偽裝成原文

最嚴重的錯誤不是生成內容不完美，而是系統不標示它是生成內容。

必須強制：

$$
\operatorname{Type}(y)
\in
\{
\mathrm{source},
\mathrm{restatement},
\mathrm{inference},
\mathrm{hypothesis}
\}.
$$

### 9.2 原文軌保存了錯誤來源

無損保存只能保證：

$$
\text{現在保存的內容等於當時保存的內容},
$$

不能保證：

$$
\text{內容本身真實或正確}.
$$

因此來源可靠性、作者、審核狀態與公開性仍需另外治理。

### 9.3 正規化破壞原文

若攝取時先修改換行、編碼、公式、圖片或中繼資料，再對修改後內容稱為「原文」，位元級無損便已經失效。

GCMS 應同時保存：

$$
\operatorname{RawBytes}(x)
$$

與：

$$
\operatorname{CanonicalContent}(x),
$$

並明確區分兩者用途。

### 9.4 壓縮炸彈與資源攻擊

無損封存軌可能遭遇：

- 極高解壓倍率；
- 惡意巢狀壓縮；
- 重複內容資源耗盡；
- 病毒與惡意文件；
- 路徑穿越與封包注入。

因此可逆不等於可無限制解碼。系統需要大小、深度、格式與權限限制。

### 9.5 語義不變量由誰定義

不同任務對「關鍵內容」的判斷可能不同：

$$
\mathcal I(x\mid q_1)
\neq
\mathcal I(x\mid q_2).
$$

因此語義近無損不能只有單一永久分數，而應保存：

- 任務；
- 評估者；
- 權重；
- 版本；
- 爭議與反例。

### 9.6 證據很多不代表推論有效

系統可能引用真實段落，卻作出來源不支持的結論。故需要區分：

$$
\text{citation presence}
\neq
\text{entailment}.
$$

證據覆蓋率應與支持關係評估分開。

---

## 十、GCMS 工程含義

第 3 篇把大型作品記憶形式化為生成核、語義指紋、關係位置、提示與外部校驗。本文進一步指出，外部校驗不是附加功能，而是語義壓縮可安全運作的必要另一軌。

因此，GCMS 的最低完整結構應是：

$$
\boxed{
\begin{aligned}
\mathrm{GCMS}
={}&
\mathrm{LosslessArchive}\\
&+\mathrm{SemanticMemory}\\
&+\mathrm{EvidenceBridge}\\
&+\mathrm{VersionGraph}\\
&+\mathrm{Governance}.
\end{aligned}
}
$$

它對應五個不可互相取代的問題：

| 子系統 | 回答的問題 |
|---|---|
| Lossless Archive | 原始內容究竟是什麼？ |
| Semantic Memory | 這份內容意味著什麼？ |
| Evidence Bridge | 生成命題由哪裡支持？ |
| Version Graph | 它在何時、哪一版成立？ |
| Governance | 誰可以讀取、生成、修改與接受？ |

未來所謂「接近無損壓縮與還原」，應被寫成聯合目標：

$$
\min
\left(
C_A+C_S+C_E
\right),
$$

在滿足：

$$
F_{\mathrm{bit}}=1,
$$

$$
F_{\mathcal I}\geq\theta_{\mathcal I},
$$

$$
F_E\geq\theta_E,
$$

$$
F_V\geq\theta_V
$$

的條件下，最大化：

$$
U_{\mathrm{retrieve}}
+
U_{\mathrm{transfer}}
+
U_{\mathrm{compose}}.
$$

這比單純追求最小檔案大小更接近 GCMS 的真正問題：以可接受成本同時保存「確切存在過的內容」與「可被智能體重新理解和運行的結構」。

---

## 十一、與下一篇的連接：從雙軌保存進入多路徑尋址

雙軌架構解決的是：

$$
\text{保存什麼，以及何種重建可以被稱為可靠。}
$$

但即使原文與語義結構都已保存，系統仍需回答：

- 從哪一個粒度開始找？
- 是否沿時間順序回放？
- 是否跨系列跳躍？
- 何時展開多個候選？
- 何時把多個分支重新集中？

因此，下一篇將把索引從單一「搜尋」操作擴展成算子族：

$$
\mathcal O_{\mathrm{index}}
=
\{
B,F,J,D,C
\},
$$

分別對應區塊、流式、跳躍、發散與集中。

雙軌保存提供可靠記憶材料；多路徑索引決定智能體如何穿越這些材料。

---

## 十二、結論

GCMS 若只保存原文，它是一個可靠但被動的知識倉庫；若只保存語義壓縮表示，它可以快速生成與遷移，卻失去普遍的逐字恢復能力與來源錨點。

因此，真正可繼承、可重建且可治理的認知記憶需要兩條軌道：

$$
\mathcal M
=
\mathcal M_{\mathrm{lossless}}
\oplus
\mathcal M_{\mathrm{semantic}}.
$$

原文軌要求：

$$
D_A(C_A(x))=x.
$$

語義軌要求：

$$
\mathcal I_{\mathrm{critical}}(x)
\subseteq
\mathcal I(\widehat x),
$$

並使：

$$
d_{\mathrm{sem}}(x,\widehat x\mid q)
\rightarrow0.
$$

兩者透過證據、版本與治理連接，使系統可以明確回答：什麼是原文、什麼是重述、什麼是推論、什麼是新假說。

本文的核心結論不是「語義壓縮永遠不可靠」，也不是「只有逐字保存才有價值」，而是：

$$
\boxed{
\begin{aligned}
\text{無損軌保存歷史真實性，}\\
\text{語義軌保存認知可用性，}\\
\text{證據層維持兩者不被混淆。}
\end{aligned}
}
$$

只有先建立這個雙軌地基，GCMS 才能在未來安全地進入多路徑索引、生成、組合、自調用與遞歸自主循環。

---

## 參考文獻

[1] Shannon, C. E. (1948). *A Mathematical Theory of Communication*. Bell System Technical Journal, 27, 379–423, 623–656.

[2] Shannon, C. E. (1959). *Coding Theorems for a Discrete Source with a Fidelity Criterion*. IRE National Convention Record, 7(4), 142–163.

[3] Nagy, D. G., Török, B., & Orbán, G. (2018). *Semantic Compression of Episodic Memories*. Cognitive Computational Neuroscience.

[4] Nagy, D. G., Török, B., & Orbán, G. (2020). Optimal forgetting: Semantic compression of episodic memories. *PLOS Computational Biology, 16*(10), e1008367.

[5] Spens, E., & Burgess, N. (2024). A generative model of memory construction and consolidation. *Nature Human Behaviour, 8*, 526–543.

[6] Spens, E., & Burgess, N. (2026). Hippocampo-neocortical interaction as compressive retrieval-augmented generation. *Nature Communications*.

[7] Guu, K., Lee, K., Tung, Z., Pasupat, P., & Chang, M.-W. (2020). REALM: Retrieval-Augmented Language Model Pre-Training. *Proceedings of ICML 2020*.

[8] Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *Advances in Neural Information Processing Systems, 33*.

[9] Asai, A., Gardner, M., & Hajishirzi, H. (2022). Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks. *Proceedings of NAACL 2022*.

[10] Benet, J. (2014). *IPFS—Content Addressed, Versioned, P2P File System*. arXiv:1407.3561.

[11] Haber, S., & Stornetta, W. S. (1991). How to Time-Stamp a Digital Document. *Journal of Cryptology, 3*, 99–111.

[12] Bayer, D., Haber, S., & Stornetta, W. S. (1993). Improving the Efficiency and Reliability of Digital Time-Stamping. In *Sequences II: Methods in Communication, Security, and Computer Science*.

---

## 版本紀錄

- **v1.0（2026-07-30）**：完成雙軌記憶架構、語義非單射限制、五項核心命題、保真指標、實驗設計與 GCMS 工程映射。
