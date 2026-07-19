# 多指生物耦合權杖域：組合區間、門檻重建與能力映射模型

## 摘要

本文在個人生物模糊權杖域之上，提出「多指生物耦合權杖域」。同一個人的多根手指並非單純重複驗證，而可形成不同的組合、耦合區間與能力語義。指定雙指、任意 $k$ 指、跨手組合與高風險多指組合，可以分別對應讀取、寫入、部署、管理、撤銷與恢復等不同能力域。

本文區分三種主要模型：固定組合耦合、任意 $k$ 指門檻重建、加權模糊耦合。多指結果不直接暴露於外部 Token，也不應被視為多個完全獨立因素；它們主要提高偽造成本、容錯能力與能力分級精度。真正的極高風險授權仍應結合裝置、PIN 或硬體安全金鑰。

**關鍵詞：** 多指生物辨識、耦合區間、門檻秘密分享、能力映射、模糊融合、多因素授權

---

## 一、研究命題

設一位使用者註冊的手指集合為：

$$
\mathcal F_u=
\{f_1,f_2,\ldots,f_m\}
$$

每根手指具有自己的模糊生物區域：

$$
\mathcal B_{u,i}
=
\mathcal B_{u,i}^{\mathrm{core}}
\cup
\mathcal B_{u,i}^{\mathrm{fuzzy}}
$$

單指模型只使用：

$$
\mathcal B_{u,i}
\rightarrow
\mathcal D_{u,i}
$$

多指模型則建立：

$$
\Psi_G
\left(
\mathcal B_{u,i_1},
\ldots,
\mathcal B_{u,i_k}
\right)
\rightarrow
\mathcal D_{u,G}
$$

其中：

$$
G\subseteq\mathcal F_u
$$

為本次參與驗證的手指組合。

核心命題是：

> 不同手指組合不只提高信心，還可以進入不同的隱藏能力域。

因此：

$$
\mathcal D_{u,\{\mathrm{左食指},\mathrm{右拇指}\}}
\neq
\mathcal D_{u,\{\mathrm{左拇指},\mathrm{右食指}\}}
$$

---

## 二、單指根值與區間

每根手指 $f_i$ 經過可撤銷轉換與模糊重建後得到根值：

$$
S_i=
\operatorname{Rep}_i
(
\widetilde z_i,
P_i
)
$$

其單指區間起點：

$$
L_{i,c,e,v_i}
=
\operatorname{OS2IP}
\left(
\operatorname{PRF}_{S_i}
(
\mathrm{realm}
\parallel c
\parallel e
\parallel v_i
)
\right)
\bmod M
$$

對應區間：

$$
\mathcal I_{i,c,e,v_i}
=
[
L_{i,c,e,v_i},
L_{i,c,e,v_i}+W_c
)
\pmod M
$$

這些單指區間是多指耦合的基礎，但耦合結果不能簡單使用普通交集。

---

## 三、為什麼不能直接使用區間交集

若定義：

$$
\mathcal I_G=
\bigcap_{i\in G}\mathcal I_i
$$

則會面臨：

1. 隨機映射後的區間可能完全不相交；
2. 任一單指的微小版本變化可能使交集消失；
3. 不同區間寬度造成不穩定；
4. 普通交集沒有密碼學混合性；
5. 外部可觀察結構可能降低不可連結性。

因此，應先建立高維乘積域：

$$
\mathcal P_G=
\prod_{i\in G}\mathcal I_i
$$

再透過密碼學耦合函數：

$$
\Psi_G:
\mathcal P_G
\rightarrow
\mathbb Z_M
$$

映射為新的耦合域。

---

## 四、固定組合耦合

對指定手指組合：

$$
G=
\{i_1,\ldots,i_k\}
$$

先將手指識別碼以固定順序編碼：

$$
\operatorname{Encode}(G)
$$

例如：

$$
\mathrm{LT}<\mathrm{LI}<\mathrm{LM}<\cdots<\mathrm{RT}
$$

耦合根：

$$
K_G=
\operatorname{HKDF}
\left(
H(
\operatorname{Encode}(G)
\parallel
S_{i_1}
\parallel\cdots\parallel
S_{i_k}
),
\mathrm{salt},
\mathrm{context}
\right)
$$

耦合區間起點：

$$
L_{G,c,e,v}
=
\operatorname{OS2IP}
\left(
\operatorname{PRF}_{K_G}
(
\mathrm{realm}
\parallel c
\parallel e
\parallel v
)
\right)
\bmod M
$$

耦合區間：

$$
\mathcal I_{G,c,e,v}
=
[
L_{G,c,e,v},
L_{G,c,e,v}+W_{G,c}
)
\pmod M
$$

此模式適合：

- 指定雙指啟動 Production 部署；
- 指定跨手組合啟動管理操作；
- 指定三指啟動撤銷或恢復流程。

---

## 五、手指組合即能力語義

定義能力映射：

$$
\Gamma(G)
=
(
c,
scope,
exp,
max\_uses,
approval
)
$$

範例：

| 手指組合 | 能力類型 | 限制 |
|---|---|---|
| 任一已註冊單指 | 低風險讀取 | 一小時 |
| 指定雙指 | 寫入或提交 | 十分鐘 |
| 跨手雙指 | Production 部署 | 六十秒、一次 |
| 任意三指 | 管理操作 | 三十秒、一次 |
| 指定三指＋PIN | 密鑰輪替 | 單次 |
| 多指＋硬體金鑰 | 根域恢復 | 離線或高保證程序 |

此處的重要性在於：

$$
\Gamma(G_1)\neq\Gamma(G_2)
$$

即使 $|G_1|=|G_2|$ ，不同組合仍可對應不同能力。

---

## 六、任意 $k$ 指門檻模型

若希望註冊 $m$ 根手指，而任意 $k$ 根都能重建能力根，不能只將手指根值 XOR。

先產生隨機個人根秘密：

$$
K_u\overset{\$}{\leftarrow}\{0,1\}^{256}
$$

以門檻秘密分享切分：

$$
K_u
\xrightarrow{(k,m)}
\{
\sigma_1,\ldots,\sigma_m
\}
$$

每個分享值由對應手指根值保護：

$$
C_i=
\operatorname{AEAD}_{\operatorname{KDF}(S_i)}
(
\sigma_i
)
$$

當任意 $k$ 根手指成功驗證後：

$$
K_u=
\operatorname{Recover}
(
\sigma_{i_1},\ldots,\sigma_{i_k}
)
$$

再依實際組合與上下文生成子域：

$$
K_{G,c,e,v}
=
\operatorname{HKDF}
\left(
K_u,
H(
\operatorname{Encode}(G)
\parallel c
\parallel e
\parallel v
)
\right)
$$

此設計同時達成：

- 任意 $k$ 指容錯；
- 不同組合仍有不同子域；
- 個別手指可撤銷；
- 不必要求所有手指永久可用。

---

## 七、加權模糊耦合

每根手指不只有成功與失敗，也有匹配品質：

$$
q_i\in[0,1]
$$

狀態：

$$
h_i\in
\{
\mathrm{core},
\mathrm{fuzzy},
\mathrm{reject},
\mathrm{missing}
\}
$$

定義耦合可信度：

$$
Q_G
=
\sum_{i\in G}w_iq_i
+
\sum_{\substack{i,j\in G\\i<j}}
\lambda_{ij}q_iq_j
$$

其中：

- $w_i$ ：單指可信權重；
- $\lambda_{ij}$ ：兩指耦合權重。

可以設定：

$$
\lambda_{\mathrm{cross-hand}}
>
\lambda_{\mathrm{same-hand}}
$$

理由是跨手組合在操作習慣、偽造成本與採集情境上可能具有不同安全意義。

但 $Q_G$ 不應直接決定權杖長度或密碼學熵，只決定：

$$
scope,\quad exp,\quad max\_uses,\quad step\_up
$$

例如：

$$
(\mathrm{core},\mathrm{core})
\rightarrow
\mathrm{deploy}
$$

$$
(\mathrm{core},\mathrm{fuzzy})
\rightarrow
\mathrm{write}
\ \text{或要求第三指}
$$

$$
(\mathrm{fuzzy},\mathrm{fuzzy})
\rightarrow
\mathrm{read\ only}
$$

$$
(\mathrm{reject},*)
\rightarrow
\mathrm{deny}
$$

---

## 八、可用性與降級策略

多指驗證不能預設每次都啟用。建議採取分級策略：

### $L_0$ ：已授權工作階段

$$
\text{No New Scan}
$$

只允許低風險、已明確限定的連續操作。

### $L_1$ ：任一單指

$$
1\text{-of-}m
$$

適用於一般讀取與低風險操作。

### $L_2$ ：指定雙指或任意二指

$$
2\text{-of-}m
$$

適用於寫入、提交與一般部署。

### $L_3$ ：跨手雙指或任意三指

$$
3\text{-of-}m
$$

適用於 Production、管理與敏感資料操作。

### $L_4$ ：多指＋第二因素

$$
\text{Multi-finger}
+
\text{PIN or Hardware Key}
$$

適用於密鑰輪替、撤銷、恢復與根權限。

---

## 九、缺指、受傷與老化

要求所有指紋同時存在：

$$
f_1\land f_2\land\cdots\land f_m
$$

在實務上不可接受。系統必須允許：

- 某根手指暫時不可用；
- 指紋受傷；
- 感測器無法辨識；
- 模板老化；
- 不同裝置缺少相同感測器。

因此推薦：

$$
k<m
$$

並建立恢復政策：

$$
\operatorname{Recovery}
=
\text{Two Fingers}
+
\text{PIN}
+
\text{Trusted Device}
$$

或：

$$
\operatorname{Recovery}
=
\text{One Finger}
+
\text{Hardware Key}
+
\text{Offline Approval}
$$

---

## 十、多指並非完全獨立因素

三根手指可能仍共享：

- 同一感測器；
- 同一驅動程式；
- 同一特徵提取器；
- 同一活體檢測；
- 同一作業系統；
- 同一受感染裝置。

因此：

$$
3\text{ fingerprints}
\neq
3\text{ independent factors}
$$

多指主要提高：

- 生物偽造成本；
- 誤接受控制能力；
- 容錯與分級能力；
- 組合語義空間。

但高風險操作仍應結合：

$$
\text{Something You Are}
+
\text{Something You Have}
+
\text{Something You Know}
$$

---

## 十一、撤銷與版本模型

定義：

$$
v_i=\text{單指版本}
$$

$$
v_G=\text{組合版本}
$$

$$
v_u=\text{個人根域版本}
$$

若單指 $f_i$ 疑似受損：

$$
v_i\leftarrow v_i+1
$$

所有包含該手指的組合域失效：

$$
i\in G
\Rightarrow
\mathcal I_{G}^{(v)}
\neq
\mathcal I_{G}^{(v+1)}
$$

不包含該手指的組合可以繼續使用。

若個人根域受損：

$$
v_u\leftarrow v_u+1
$$

則所有組合域全面輪替。

---

## 十二、最終權杖

耦合域內取得安全亂數座標：

$$
r\overset{\$}{\leftarrow}\{0,1\}^{256}
$$

$$
q_G
=
L_{G,c,e,v}
+
(
\operatorname{OS2IP}(r)\bmod W_{G,c}
)
\pmod M
$$

最終權杖：

$$
T_{G,c,e,r}
=
\operatorname{PRF}_{K_B}
\left(
H(
\operatorname{Encode}(G)
)
\parallel
c
\parallel
e
\parallel
v
\parallel
q_G
\parallel
r
\parallel
scope
\parallel
resource
\parallel
exp
\parallel
jti
\right)
$$

外部不可得知：

- 使用幾根手指；
- 使用哪些手指；
- 是否跨手；
- 生物品質；
- 能力等級；
- 內部耦合域。

---

## 結論

多指生物耦合權杖域不是：

$$
\text{多掃幾根手指}
\rightarrow
\text{同一個固定密鑰}
$$

而是：

$$
\boxed{
\text{多個模糊生物區域}
\rightarrow
\text{組合或門檻耦合}
\rightarrow
\text{組合專屬能力域}
\rightarrow
\text{短效隨機能力權杖}
}
$$

不同手指組合可以成為不同能力語義，而不是只有同一身份的重複證明。這使生物辨識從「登入判斷」進一步轉化為「能力空間選擇器」。
