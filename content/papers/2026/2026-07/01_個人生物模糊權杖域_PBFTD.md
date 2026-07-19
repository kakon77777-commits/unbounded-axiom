# 個人生物模糊權杖域：以個人專屬區間、模糊區間與時間類型切分生成短效能力權杖

## 摘要

本文提出「個人生物模糊權杖域」模型。與直接對指紋雜湊、由指紋生成固定密鑰或使用生物辨識解鎖單一永久權杖不同，本模型將生物特徵視為一個可漂移、可更新、可撤銷轉換的個人隱藏座標。系統先由多次生物樣本建立個人核心區、模糊區與拒絕區，再透過受保護轉換與模糊重建機制取得個人根種子。該根種子不直接成為權杖，而是用來建立服務、用途、時間與版本相關的內部生成區間，最後再配合密碼學安全亂數生成外部不可區分的短效能力權杖。

本文重點在於：個人專屬區間可以存在，但它必須保持隱藏；外部權杖仍應具有完整亂數外觀與足夠安全熵。

**關鍵詞：** 生物模糊區間、個人權杖域、模糊提取器、能力權杖、可撤銷生物辨識、時間窗、偽隨機函數

---

## 一、研究動機

一般 API Token 多由安全亂數直接生成：

$$
T\overset{\$}{\leftarrow}\{0,1\}^n
$$

此方式在密碼學上合理，但對個人身份、使用情境、風險等級與生物授權缺少內在結構。

另一方面，直接使用：

$$
T=H(b)
$$

其中 $b$ 為生物樣本，則存在以下問題：

1. 同一指紋每次掃描並不完全相同；
2. 生物資料不可真正更換；
3. 固定雜湊可能形成跨服務追蹤識別碼；
4. 權杖缺少時間、用途與撤銷版本；
5. 生物特徵的有效熵與密碼學亂數不是同一概念。

因此，本文不將生物特徵映射為單一點，而是映射為個人穩定但容許漂移的區域。

---

## 二、生物樣本與個人模糊區間

設使用者 $u$ 在時間 $t$ 的生物樣本為：

$$
b_{u,t}
$$

特徵提取器為：

$$
\phi:\mathcal B\rightarrow\mathbb R^d
$$

得到：

$$
z_{u,t}=\phi(b_{u,t})
$$

註冊時收集 $n$ 個樣本：

$$
Z_u=
\{z_{u,1},\ldots,z_{u,n}\}
$$

定義穩健中心：

$$
\mu_u=
\operatorname{RobustCenter}(Z_u)
$$

定義變異矩陣：

$$
\Sigma_u=
\operatorname{RobustCovariance}(Z_u)
$$

新樣本 $z$ 與個人分布的距離可表示為：

$$
d_u(z)=
\sqrt{
(z-\mu_u)^\top
(\Sigma_u+\varepsilon I)^{-1}
(z-\mu_u)
}
$$

定義三層區域：

### 核心區

$$
\mathcal B_u^{\mathrm{core}}
=
\{z:d_u(z)\leq\alpha_u\}
$$

### 模糊區

$$
\mathcal B_u^{\mathrm{fuzzy}}
=
\{z:\alpha_u<d_u(z)\leq\beta_u\}
$$

### 拒絕區

$$
\mathcal B_u^{\mathrm{reject}}
=
\{z:d_u(z)>\beta_u\}
$$

因此，生物驗證結果不是單純布林值，而是：

$$
h_u(z)\in
\{
\mathrm{core},
\mathrm{fuzzy},
\mathrm{reject}
\}
$$

---

## 三、模糊區間的權限意義

核心區與模糊區不應改變權杖的密碼學強度，而應改變能力限制。

定義能力政策函數：

$$
\Pi(h,c,risk)
\rightarrow
(scope,exp,max\_uses,step\_up)
$$

例如：

### 核心區

$$
h=\mathrm{core}
$$

可允許：

- 讀取；
- 一般寫入；
- 短效部署；
- 低風險自動化。

### 模糊區

$$
h=\mathrm{fuzzy}
$$

可限制為：

- 唯讀；
- 更短有效時間；
- 單次使用；
- 要求再掃描；
- 要求第二因素；
- 禁止根權限操作。

### 拒絕區

$$
h=\mathrm{reject}
$$

不得生成能力權杖。

關鍵原則：

$$
H_\infty(T_{\mathrm{core}})
\approx
H_\infty(T_{\mathrm{fuzzy}})
$$

安全差異位於能力與時效，不位於權杖亂數品質。

---

## 四、可撤銷生物轉換

原始特徵不應直接用於所有服務。對每個服務領域與版本，建立不同的轉換參數：

$$
\rho_{u,s,v}
$$

轉換後特徵：

$$
\widetilde z_{u,s,v}
=
Q(
G_{\rho_{u,s,v}}(z_u)
)
$$

其中：

- $G$ ：具可撤銷性與不可連結性的轉換；
- $Q$ ：量化函數；
- $s$ ：服務領域；
- $v$ ：版本。

要求：

$$
\rho_{u,s_1,v}
\neq
\rho_{u,s_2,v}
$$

使得：

$$
\widetilde z_{u,s_1,v}
\neq
\widetilde z_{u,s_2,v}
$$

避免同一生物特徵在不同服務中形成相同表示。

---

## 五、模糊重建與個人根種子

註冊階段：

$$
(S_{u,s,v},P_{u,s,v})
=
\operatorname{Gen}
(
\widetilde z_{u,s,v}
)
$$

驗證階段：

$$
S'=
\operatorname{Rep}
(
\widetilde z'_{u,s,v},
P_{u,s,v}
)
$$

若樣本落在允許範圍：

$$
d(
\widetilde z',
\widetilde z
)
\leq\tau
$$

則：

$$
S'=S_{u,s,v}
$$

注意： $S_{u,s,v}$ 不直接作為 API Token。它只作為隱藏生成域的根。

---

## 六、個人專屬根區間

設內部邏輯空間：

$$
\mathbb Z_M,\qquad M=2^{256}
$$

個人根區間起點：

$$
L_{u,s,v}
=
\operatorname{OS2IP}
\left(
\operatorname{PRF}_{S_{u,s,v}}
(
\mathrm{issuer}
\parallel
s
\parallel
v
)
\right)
\bmod M
$$

定義根區間：

$$
\mathcal I_{u,s,v}
=
[
L_{u,s,v},
L_{u,s,v}+W_u
)
\pmod M
$$

此區間只存在於本地代理內部，外部服務不可看到其位置、寬度或使用者關係。

---

## 七、依權杖類型切分子區間

設能力類型集合：

$$
\mathcal C=
\{
\mathrm{read},
\mathrm{write},
\mathrm{deploy},
\mathrm{admin},
\mathrm{delegate},
\mathrm{revoke}
\}
$$

對類型 $c$ ，建立子區間起點：

$$
L_{u,s,c,v}
=
\operatorname{OS2IP}
\left(
\operatorname{PRF}_{S_{u,s,v}}
(
s
\parallel c
\parallel v
)
\right)
\bmod M
$$

類型子區間：

$$
\mathcal I_{u,s,c,v}
=
[
L_{u,s,c,v},
L_{u,s,c,v}+W_c
)
\pmod M
$$

因此：

$$
\mathcal I_{u,s,\mathrm{read},v}
\neq
\mathcal I_{u,s,\mathrm{admin},v}
$$

不同類型不只是權杖宣告不同，而是在內部生成域上彼此分離。

---

## 八、時間窗切分

對每種能力類型指定時間粒度：

$$
\Delta_c>0
$$

時間窗編號：

$$
e_c(t)=
\left\lfloor
\frac{t}{\Delta_c}
\right\rfloor
$$

時間子區間起點：

$$
L_{u,s,c,e,v}
=
\operatorname{OS2IP}
\left(
\operatorname{PRF}_{S_{u,s,v}}
(
s
\parallel c
\parallel e
\parallel v
)
\right)
\bmod M
$$

時間—類型區間：

$$
\mathcal I_{u,s,c,e,v}
=
[
L_{u,s,c,e,v},
L_{u,s,c,e,v}+W_c
)
\pmod M
$$

則：

$$
\mathcal I_{u,s,c,e,v}
\neq
\mathcal I_{u,s,c,e+1,v}
$$

上一時間窗不能自然延伸至下一時間窗。

---

## 九、區間內抽樣與外部權杖

產生安全亂數：

$$
r\overset{\$}{\leftarrow}\{0,1\}^{256}
$$

在內部區間取得座標：

$$
q=
L_{u,s,c,e,v}
+
\left(
\operatorname{OS2IP}(r)\bmod W_c
\right)
\pmod M
$$

不能直接輸出 $q$ 。最終權杖應為：

$$
T=
\operatorname{PRF}_{K_B}
\left(
u
\parallel s
\parallel c
\parallel e
\parallel v
\parallel q
\parallel r
\parallel scope
\parallel resource
\parallel exp
\parallel jti
\right)
$$

其中：

- $K_B$ ：Broker 的權杖簽發根；
- $jti$ ：一次性識別碼；
- $scope$ ：能力範圍；
- $resource$ ：目標資源；
- $exp$ ：到期時間。

外部應無法由 $T$ 判斷：

- 使用者；
- 指紋；
- 權杖類型；
- 時間窗；
- 生物匹配品質；
- 內部區間。

---

## 十、版本演化與生物變化

生物特徵會因年齡、受傷、感測器差異與使用環境變化而漂移。因此模板必須版本化：

$$
v=0,1,2,\ldots
$$

新版根域：

$$
\mathcal I_{u,s}^{(v+1)}
\neq
\mathcal I_{u,s}^{(v)}
$$

更新期可允許有限重疊：

$$
\operatorname{Valid}
(
\mathcal I^{(v)}
)
=
1
$$

$$
\operatorname{Valid}
(
\mathcal I^{(v+1)}
)
=
1
$$

遷移完成後：

$$
\operatorname{Valid}
(
\mathcal I^{(v)}
)
=
0
$$

模板中心可在可信條件下緩慢更新：

$$
\mu_u^{(t+1)}
=
(1-\eta)\mu_u^{(t)}
+\eta z_t
$$

但必須限制漂移：

$$
\left\|
\mu_u^{(t+1)}
-
\mu_u^{(t)}
\right\|
\leq\varepsilon
$$

並要求：

$$
\mathrm{CoreMatch}
\land
\mathrm{Liveness}
\land
\mathrm{TrustedDevice}
\land
\mathrm{AdditionalFactor}
$$

以避免模板污染。

---

## 十一、形式化安全要求

### 不可逆性

從公開輔助資料與權杖，不應有效重建原始生物特徵：

$$
\Pr[
\mathcal A(P,T)\rightarrow z
]
\leq\operatorname{negl}(\lambda)
$$

### 不可連結性

不同服務的表示不可被有效關聯：

$$
\operatorname{Adv}^{\mathrm{link}}_{\mathcal A}
\leq
\operatorname{negl}(\lambda)
$$

### 可撤銷性

版本更新後，舊域不能生成新有效權杖：

$$
v'\neq v
\Rightarrow
\operatorname{Verify}_{v'}(T_v)=0
$$

### 外觀均勻性

權杖與真正均勻亂數應計算上不可區分：

$$
\left|
\Pr[\mathcal A(T)=1]
-
\Pr[\mathcal A(U_n)=1]
\right|
\leq
\operatorname{negl}(\lambda)
$$

### 模糊穩定性

合法生物漂移下，根種子應能穩定重建：

$$
d(z,z')\leq\tau
\Rightarrow
\Pr[
\operatorname{Rep}(z',P)=S
]
\geq
1-\epsilon
$$

---

## 十二、研究價值與限制

本模型的價值在於：

1. 生物特徵不再對應一個永久密鑰；
2. 個人身份、時間、用途與風險被納入生成域；
3. 核心區與模糊區能形成不同能力策略；
4. 同一人可為不同服務建立不可連結的域；
5. 權杖仍保有完整亂數外觀。

限制包括：

- 一般作業系統未必提供原始指紋特徵；
- 模糊提取器需要針對實際感測器與特徵表示設計；
- 輔助資料洩漏必須嚴格分析；
- 生物模板更新可能受到污染攻擊；
- 仍需可信本地執行環境；
- 此權杖通常先由本地 Broker 使用，不能直接取代第三方平台既有 API Key。

---

## 結論

個人生物模糊權杖域的核心不是：

$$
\text{指紋}
\rightarrow
\text{固定 Token}
$$

而是：

$$
\boxed{
\text{生物模糊區間}
\rightarrow
\text{個人隱藏生成域}
\rightarrow
\text{用途與時間子域}
\rightarrow
\text{安全亂數權杖}
}
$$

生物特徵在此扮演的是「個人域的模糊定位器與啟動器」，而不是不可撤銷的密碼本身。
