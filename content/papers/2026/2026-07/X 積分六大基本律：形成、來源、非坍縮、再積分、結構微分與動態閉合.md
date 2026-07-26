---
title: "X 積分六大基本律：形成、來源、非坍縮、再積分、結構微分與動態閉合"
subtitle: "The Six Fundamental Laws of the X-Integral: Formation, Provenance, Non-Collapse, Re-Integration, Structural Differentiation, and Dynamic Closure"
version: "v0.1"
date: "2026-07-24"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Foundational Axiomatic Paper"
keywords:
  - X 積分
  - 積分形成律
  - 來源保存律
  - 非坍縮律
  - 再積分守衛律
  - 結構微分律
  - 動態整體閉合律
  - 無數值代數
  - 合法性演算
---

# X 積分六大基本律：形成、來源、非坍縮、再積分、結構微分與動態閉合

## 摘要

本文建立 X 積分代數的六條基本律：積分形成律、來源保存律、非坍縮律、再積分守衛律、結構微分律與動態整體閉合律。這六條律不是 X 積分的附加性質，而是判定某種結構操作是否有資格被稱為 X 積分的最低理論核心。

X 積分不以數值、測度或面積為基礎。其對象是攜帶屬性、類型、範疇、關係、邊界與合法條件的 X 結構。一次 X 積分不是把多個對象加總，而是在明確上下文、關係模式與邊界條件下，使若干來源結構形成一個更高整體。此整體必須保存其來源，避免將必要差異非法抹除，並在再次積分前重新接受守衛判定。X 微分則反向揭露結構形成所依賴的差異、來源、關係、邊界與障礙。若一個結構可在持續積分中維持身份、來源與合法接口，則形成動態整體閉合。

本文首先建立 X 積分系統的最小語法與判定形式，隨後逐條給出六大基本律的形式表達、強弱版本、失敗模式及相互依賴。最後提出 X 積分最低完備性命題：一個結構操作只有同時滿足形成、來源、非坍縮、守衛、可微分揭露與動態閉合條件，才能成為持續 X 積分系統中的合法積分。

---

## 1. 理論位置

X 積分的應用可以涉及群、環、域、拓撲、類型系統、知識結構、語義系統、權限系統與動態本體論。然而，若在應用之前沒有先建立基本律，則下列表達：

$$
\int_{\rho}X
$$

仍可能只是「加入條件」的裝飾性記號。

因此，X 積分理論必須先回答六個問題：

1. 什麼條件下，一次積分可以形成？
2. 積分後，原始來源是否仍可追蹤？
3. 積分是否非法抹除原本必要的差異？
4. 一次積分合法，是否代表可以繼續積分？
5. 如何從積分結果中揭露其結構差異與形成條件？
6. 持續積分如何形成一個不靜止、但仍保持身份的整體？

這六個問題分別對應：

$$
\boxed{
\text{積分形成律}
}
$$

$$
\boxed{
\text{來源保存律}
}
$$

$$
\boxed{
\text{非坍縮律}
}
$$

$$
\boxed{
\text{再積分守衛律}
}
$$

$$
\boxed{
\text{結構微分律}
}
$$

$$
\boxed{
\text{動態整體閉合律}
}
$$

---

## 2. 最小形式背景

### 2.1 X 結構

一個 X 結構暫記為：

$$
X
=
\langle
A_X,
T_X,
C_X,
R_X,
B_X,
P_X
\rangle,
$$

其中：

- $A_X$ ：屬性；
- $T_X$ ：類型；
- $C_X$ ：範疇位置；
- $R_X$ ：已知關係；
- $B_X$ ：結構邊界；
- $P_X$ ：允許與禁止的操作條件。

此表示不是宣稱 X 必須被還原為普通有序組，而是列出任何合法 X 判定至少可能涉及的結構面向。

### 2.2 上下文

所有判定相對於上下文 $\Gamma$ ：

$$
\Gamma
=
\langle
\mathcal X,
\mathcal T,
\mathcal R,
\mathcal B,
\mathcal P,
\mathcal F
\rangle.
$$

其中：

- $\mathcal X$ ：已宣告 X 結構；
- $\mathcal T$ ：類型與範疇規則；
- $\mathcal R$ ：合法關係；
- $\mathcal B$ ：邊界規則；
- $\mathcal P$ ：操作權限；
- $\mathcal F$ ：形成規則。

### 2.3 基本判定

$$
\Gamma\vdash X\;\operatorname{form}
$$

表示 X 可在 $\Gamma$ 中形成。

$$
\Gamma\vdash X:\mathcal A
$$

表示 X 在 $\Gamma$ 中具有類型 $\mathcal A$ 。

$$
\Gamma\vdash X\bowtie_{\rho}Y
$$

表示 X 與 Y 可依關係模式 $\rho$ 共同積分。

$$
\Gamma\vdash\mathsf I_{\rho}(X;Y):Z
$$

表示 X 與 Y 經由 $\rho$ 合法積分形成 Z。

$$
\Gamma\vdash\mathsf D_{\kappa}(Z):\Delta_{\kappa}Z
$$

表示依差異模式 $\kappa$ 對 Z 進行結構微分。

---

## 3. 法則、規則與定理的區別

本文將六個核心命題稱為「基本律」，但其內部包含三種不同層次。

### 3.1 形成規則

規定某種表達式何時有資格形成，例如：

$$
\frac{
\Gamma\vdash X:\mathcal A
\qquad
\Gamma\vdash Y:\mathcal B
\qquad
\Gamma\vdash X\bowtie_{\rho}Y
}{
\Gamma\vdash\mathsf I_{\rho}(X;Y):\mathcal C
}.
$$

### 3.2 保存公理

規定合法積分不可違反的最低不變性，例如來源保存與非坍縮。

### 3.3 可推導定理

由形成規則與保存公理推出的結果，例如積分路徑可回溯、非法再積分不可形成、動態整體的局部身份保存。

六大基本律因此不是單一種類的句子，而是一組共同構成 X 積分核心的形式原則。

---

# 第一基本律：積分形成律

## 4. 積分形成律的直觀內容

積分形成律回答：

> 在什麼條件下，若干 X 結構有資格形成一個新的 X 整體？

X 積分不能由符號並置自動產生。必須至少存在：

- 合法輸入；
- 明確關係；
- 類型相容；
- 範疇相容或合法橋接；
- 邊界轉換；
- 積分權限；
- 可形成的輸出類型。

### 4.1 基本形式

若：

$$
\Gamma\vdash X:\mathcal A,
$$

$$
\Gamma\vdash Y:\mathcal B,
$$

$$
\Gamma\vdash X\bowtie_{\rho}Y,
$$

$$
\Gamma\vdash
\operatorname{Bd}_{\rho}(X,Y)\rightsquigarrow B_Z,
$$

$$
\Gamma\vdash
\operatorname{Perm}_{\mathsf I}(\rho;X,Y),
$$

則：

$$
\boxed{
\Gamma\vdash
\mathsf I_{\rho}(X;Y):\mathcal C.
}
$$

形式規則為：

$$
\frac{
\Gamma\vdash X:\mathcal A
\quad
\Gamma\vdash Y:\mathcal B
\quad
\Gamma\vdash X\bowtie_{\rho}Y
\quad
\Gamma\vdash\operatorname{Bd}_{\rho}(X,Y)\rightsquigarrow B_Z
\quad
\Gamma\vdash\operatorname{Perm}_{\mathsf I}(\rho;X,Y)
}{
\Gamma\vdash\mathsf I_{\rho}(X;Y):\mathcal C
}.
$$

### 4.2 單體形成

若積分處理的是 X 的內部展開，則：

$$
\frac{
\Gamma\vdash X:\mathcal A
\quad
\Gamma\vdash\operatorname{Expandable}_{\rho}(X)
\quad
\Gamma\vdash\operatorname{Perm}_{\mathsf I}(\rho;X)
}{
\Gamma\vdash\mathsf I_{\rho}(X):\mathcal A'
}.
$$

### 4.3 最小形成條件

定義：

$$
\operatorname{FormCond}_{\Gamma}(\rho;X,Y)
$$

為：

$$
\operatorname{Typed}(X,Y)
\land
\operatorname{Related}_{\rho}(X,Y)
\land
\operatorname{CategoryLegal}_{\rho}(X,Y)
\land
\operatorname{BoundaryLegal}_{\rho}(X,Y)
\land
\operatorname{Permitted}_{\rho}(X,Y).
$$

則：

$$
\boxed{
\operatorname{FormCond}_{\Gamma}(\rho;X,Y)
\Longrightarrow
\Gamma\vdash\mathsf I_{\rho}(X;Y)\;\operatorname{form}.
}
$$

### 4.4 非充分關係

僅僅存在某種關係並不足以形成積分：

$$
\Gamma\vdash XRY
$$

不自動推出：

$$
\Gamma\vdash\mathsf I_R(X;Y).
$$

因為關係可能：

- 不具備積分權限；
- 只存在於元層；
- 破壞邊界；
- 混同範疇；
- 造成不可接受坍縮。

### 4.5 形成失敗

若任一必要條件缺失：

$$
\neg\operatorname{FormCond}_{\Gamma}(\rho;X,Y),
$$

則：

$$
\boxed{
\Gamma\nvdash
\mathsf I_{\rho}(X;Y)
\;\operatorname{form}.
}
$$

此結果不是零，不是假值，而是表達式沒有形成資格。

---

# 第二基本律：來源保存律

## 5. 來源保存律的直觀內容

來源保存律回答：

> 積分形成新整體後，原始構成者與其進入整體的方式是否仍可辨識？

若 X 與 Y 被積分為 Z：

$$
Z
=
\mathsf I_{\rho}(X;Y),
$$

則 Z 必須保存：

- X 的來源身份；
- Y 的來源身份；
- 關係 $\rho$ ；
- 積分發生的上下文；
- 邊界轉換；
- 形成順序或形成路徑；
- 哪些新關係由此次積分生成。

### 5.1 基本形式

若：

$$
\Gamma\vdash
Z=\mathsf I_{\rho}(X;Y),
$$

則存在來源嵌入或來源痕跡：

$$
\iota_X:X\hookrightarrow_{\rho}Z,
$$

$$
\iota_Y:Y\hookrightarrow_{\rho}Z.
$$

並且存在來源投影或來源恢復判定：

$$
\pi_X^{\mathrm{src}}(Z)\simeq X,
$$

$$
\pi_Y^{\mathrm{src}}(Z)\simeq Y.
$$

因此：

$$
\boxed{
\operatorname{Src}(Z)
\supseteq
\{(X,\iota_X),(Y,\iota_Y),\rho,\Gamma\}.
}
$$

### 5.2 弱來源保存

弱版本只要求來源可辨識：

$$
X,Y\in\operatorname{Trace}(Z).
$$

### 5.3 強來源保存

強版本要求來源連同其原始結構、進入方式與邊界都可回溯：

$$
\operatorname{Recover}_{\mathrm{src}}(Z)
=
\langle
X,Y,\rho,\Gamma,B_X,B_Y
\rangle.
$$

### 5.4 新生成關係的來源

若 Z 中存在新關係 $\sigma$ ，則必須有：

$$
\sigma\in
\operatorname{Gen}_{\rho}(X,Y,\Gamma)
$$

或明確證書：

$$
\operatorname{Cert}(\sigma\mid X,Y,\rho,\Gamma).
$$

不得出現：

$$
\sigma\in R_Z
$$

但：

$$
\sigma\notin R_X,
\quad
\sigma\notin R_Y,
\quad
\sigma\notin\operatorname{Gen}_{\rho}(X,Y,\Gamma),
$$

且沒有合法生成證書。

### 5.5 來源消失失敗

若積分後無法回答：

- 此部分從何而來；
- 此關係由何產生；
- 此邊界為何改變；
- 此類型何時形成；

則來源保存律失敗。

---

# 第三基本律：非坍縮律

## 6. 非坍縮律的直觀內容

非坍縮律回答：

> 積分形成整體時，是否非法抹除了構成者之間仍然必要的差異？

積分不是把所有部分變成同一物。若：

$$
X\not\equiv Y,
$$

則積分後不能僅因 X 與 Y 共存於 Z，便推出：

$$
\iota_X(X)\equiv\iota_Y(Y).
$$

### 6.1 基本形式

若：

$$
\Gamma\vdash X\not\equiv_{\delta}Y,
$$

其中 $\delta$ 是在當前積分中必須保存的差異，且：

$$
Z=\mathsf I_{\rho}(X;Y),
$$

則：

$$
\boxed{
\Gamma\vdash
\iota_X(X)
\not\equiv_{\delta'}
\iota_Y(Y)
\quad\text{於 }Z.
}
$$

其中 $\delta'$ 是 $\delta$ 在積分後的合法延續。

### 6.2 差異核

定義 X 與 Y 的必要差異核：

$$
\Delta_{\Gamma}^{\mathrm{ess}}(X,Y).
$$

非坍縮要求：

$$
\boxed{
\Delta_{\Gamma}^{\mathrm{ess}}(X,Y)
\rightsquigarrow
\Delta_{\Gamma'}^{\mathrm{ess}}
\left(
\iota_X(X),
\iota_Y(Y)
\right).
}
$$

### 6.3 合法商化不是坍縮

若積分的目的本來就是依等價關係 $\sim$ 進行商化：

$$
Z=\mathsf I_{\sim}(X),
$$

則部分差異可以被識別。

但必須同時保留：

- 使用了何種等價關係；
- 哪些差異被識別；
- 哪些差異仍被保存；
- 商化後的等價類來源。

所以：

$$
\boxed{
\text{合法商化}
\neq
\text{無條件坍縮}.
}
$$

### 6.4 完全同一化條件

只有當存在明確合法判定：

$$
\Gamma\vdash X\equiv_{\rho}Y,
$$

且積分模式 $\rho$ 明確要求同一化，才可有：

$$
\iota_X(X)\equiv\iota_Y(Y).
$$

### 6.5 非坍縮失敗

以下情況構成失敗：

- 類型差異被隱藏；
- 對象層與元層被混同；
- 原因與結果被視為同一；
- 比喻橋接被誤認為本體同一；
- 局部等價被擴張成全域同一；
- 商化規則未宣告便消除差異。

---

# 第四基本律：再積分守衛律

## 7. 再積分守衛律的直觀內容

再積分守衛律回答：

> 一次積分成功後，是否可以自動繼續積分？

答案是否定的。

若：

$$
Z=\mathsf I_{\rho}(X;Y),
$$

這只表示 Z 已合法形成為新 X 結構，不表示：

$$
\mathsf I_{\sigma}(Z;W)
$$

必然合法。

每次再積分都必須重新檢查新的類型、範疇、來源、邊界、衝突與非坍縮條件。

### 7.1 守衛函子

定義再積分守衛：

$$
\mathsf G_{\Gamma}
(\sigma;Z,W).
$$

其內容至少包括：

$$
\mathsf G_{\Gamma}
=
\mathsf G_{\mathrm{type}}
\land
\mathsf G_{\mathrm{category}}
\land
\mathsf G_{\mathrm{source}}
\land
\mathsf G_{\mathrm{boundary}}
\land
\mathsf G_{\mathrm{conflict}}
\land
\mathsf G_{\mathrm{noncollapse}}
\land
\mathsf G_{\mathrm{permission}}.
$$

### 7.2 基本形式

若：

$$
\Gamma\vdash Z:\mathcal C,
$$

$$
\Gamma\vdash W:\mathcal D,
$$

$$
\Gamma\vdash Z\bowtie_{\sigma}W,
$$

且：

$$
\Gamma\vdash
\mathsf G_{\Gamma}(\sigma;Z,W),
$$

則：

$$
\boxed{
\Gamma\vdash
\mathsf I_{\sigma}(Z;W)
\;\operatorname{form}.
}
$$

形式規則：

$$
\frac{
\Gamma\vdash Z:\mathcal C
\quad
\Gamma\vdash W:\mathcal D
\quad
\Gamma\vdash Z\bowtie_{\sigma}W
\quad
\Gamma\vdash\mathsf G_{\Gamma}(\sigma;Z,W)
}{
\Gamma\vdash\mathsf I_{\sigma}(Z;W):\mathcal E
}.
$$

### 7.3 第一次合法不傳遞

一般而言：

$$
\Gamma\vdash\mathsf I_{\rho}(X;Y)
$$

不推出：

$$
\Gamma\vdash
\mathsf I_{\sigma}
\left(
\mathsf I_{\rho}(X;Y);W
\right).
$$

這稱為：

$$
\boxed{
\text{積分合法性的非自動傳遞性。}
}
$$

### 7.4 守衛可更新

積分後上下文可能改變：

$$
\Gamma
\rightsquigarrow
\Gamma'.
$$

因此下一層守衛應在 $\Gamma'$ 中判定：

$$
\mathsf G_{\Gamma'}
(\sigma;Z,W),
$$

而不能沿用舊上下文的結論。

### 7.5 停止前沿

若守衛不成立：

$$
\Gamma\nvdash
\mathsf G_{\Gamma}(\sigma;Z,W),
$$

則積分鏈在 Z 處停止。

定義：

$$
\operatorname{Frontier}_{\mathsf I}(Z)
=
\{
\sigma
\mid
\mathsf G_{\Gamma}(\sigma;Z,W)
\text{ 失敗}
\}.
$$

---

# 第五基本律：結構微分律

## 8. 結構微分律的直觀內容

結構微分律回答：

> 如何從一個已形成的 X 整體中，揭露其必要差異、來源、關係、邊界、前沿與障礙？

X 微分不必將整體拆回原樣，也不是數值變化率。它是一種有模式的結構揭露。

### 8.1 微分模式

設：

$$
\kappa
\in
\{
\mathrm{src},
\mathrm{rel},
\mathrm{type},
\mathrm{boundary},
\mathrm{frontier},
\mathrm{obstruction},
\mathrm{quotient},
\mathrm{history}
\}.
$$

則：

$$
\mathsf D_{\kappa}(Z)
$$

揭露 Z 在模式 $\kappa$ 下的結構差異。

### 8.2 基本形式

若：

$$
\Gamma\vdash Z:\mathcal C,
$$

且：

$$
\Gamma\vdash
\operatorname{Differentiable}_{\kappa}(Z),
$$

則：

$$
\boxed{
\Gamma\vdash
\mathsf D_{\kappa}(Z)
:
\Delta_{\kappa}Z.
}
$$

形式規則：

$$
\frac{
\Gamma\vdash Z:\mathcal C
\quad
\Gamma\vdash\operatorname{Differentiable}_{\kappa}(Z)
}{
\Gamma\vdash\mathsf D_{\kappa}(Z):\Delta_{\kappa}Z
}.
$$

### 8.3 對積分結果的微分

若：

$$
Z=\mathsf I_{\rho}(X;Y),
$$

則來源微分至少應揭露：

$$
\mathsf D_{\mathrm{src}}(Z)
\succeq
\langle X,Y,\rho\rangle.
$$

關係微分至少應揭露：

$$
\mathsf D_{\mathrm{rel}}(Z)
\succeq
\operatorname{Rel}_{\rho}(X,Y).
$$

邊界微分至少應揭露：

$$
\mathsf D_{\mathrm{boundary}}(Z)
\succeq
\partial Z.
$$

### 8.4 條件還原

若積分滿足強來源保存、非坍縮與邊界可逆，則：

$$
\boxed{
\mathsf D_{\mathrm{src}}
\left(
\mathsf I_{\rho}(X;Y)
\right)
\simeq
\langle X,Y,\rho\rangle.
}
$$

但一般不要求：

$$
\mathsf D(\mathsf I(X))=X.
$$

因為積分可能生成：

- 新關係；
- 新類型；
- 新邊界；
- 新整體身份；
- 不可逆商化。

### 8.5 微分非唯一性

不同 $\kappa$ 會揭露不同面向：

$$
\mathsf D_{\mathrm{src}}(Z)
\not\simeq
\mathsf D_{\mathrm{frontier}}(Z).
$$

因此 X 微分不是單一無條件算子，而是一族受模式與合法性約束的結構揭露算子。

### 8.6 微分的完備性要求

對指定模式 $\kappa$ ，若微分宣稱完整，則不得遺漏所有在 $\kappa$ 下必要的結構資訊。

定義：

$$
\operatorname{Complete}_{\kappa}
\left(
\mathsf D_{\kappa}(Z)
\right).
$$

這使 X 微分可被檢驗，而不是任意解讀。

---

# 第六基本律：動態整體閉合律

## 9. 動態整體閉合律的直觀內容

動態整體閉合律回答：

> 持續積分如何形成一個內容不斷變動、但仍維持結構身份的整體？

靜態閉包只要求操作後不離開某集合。X 的動態閉合則要求：

- 新積分仍進入同一持續整體；
- 來源歷史仍可追蹤；
- 必要差異仍保存；
- 邊界可以合法演化；
- 整體具有下一次積分接口；
- 整體身份不因內容增長而任意消失。

### 9.1 持續整體

記 X 的持續整體為：

$$
\mathsf C[X].
$$

其基本自指形式為：

$$
\boxed{
\mathsf C[X]
\simeq
\mathsf I_{\mathrm{cont}}
\left(
X;
\mathsf C[X]
\right).
}
$$

此式不表示 $\mathsf C[X]$ 靜態等於自身，而表示：

> 將 X 與其已形成的持續整體再次合法積分後，仍落在同一整體身份類中。

### 9.2 動態身份

定義動態身份關係：

$$
\simeq_{\mathrm{dyn}}.
$$

若：

$$
\mathsf C_{t+1}
=
\mathsf I_{\rho_t}
(\mathsf C_t;X_t),
$$

且：

$$
\mathsf C_{t+1}
\simeq_{\mathrm{dyn}}
\mathsf C_t,
$$

則內容可以改變，但持續身份被保存。

此處 $t$ 僅是元層索引，不是 X 對象層的數值測量。

### 9.3 閉合條件

動態整體閉合至少要求：

$$
\operatorname{SourceClosed},
$$

$$
\operatorname{DifferenceClosed},
$$

$$
\operatorname{BoundaryEvolvable},
$$

$$
\operatorname{GuardPreserved},
$$

$$
\operatorname{IdentityPersistent},
$$

$$
\operatorname{Reintegrable}.
$$

因此：

$$
\operatorname{DynClosed}(\mathsf C[X])
$$

當且僅當：

$$
\forall Z
\left[
Z\in\mathsf C[X]
\land
\mathsf G(\rho;Z,Y)
\Longrightarrow
\mathsf I_{\rho}(Z;Y)
\in_{\mathrm{dyn}}
\mathsf C[X]
\right].
$$

### 9.4 動態閉合不是無限吞併

若任何 Y 都能被無條件加入，則不是閉合，而是失去邊界。

動態整體必須同時有：

$$
\operatorname{Accept}_{\mathsf C}(Y)
$$

與：

$$
\operatorname{Reject}_{\mathsf C}(Y).
$$

即具有可接受與不可接受的形成條件。

### 9.5 身份保存與內容變化

動態整體允許：

$$
\operatorname{Content}(\mathsf C_{t+1})
\not\equiv
\operatorname{Content}(\mathsf C_t),
$$

但要求：

$$
\operatorname{IdentityCore}(\mathsf C_{t+1})
\simeq
\operatorname{IdentityCore}(\mathsf C_t).
$$

若身份核心也被合法改寫，則必須形成新的持續整體類型，而不能假裝仍完全相同。

---

# 六律之間的依賴

## 10. 邏輯順序

六條律不是彼此平行的清單，而具有依賴順序：

$$
\boxed{
\text{形成}
\to
\text{來源}
\to
\text{非坍縮}
\to
\text{守衛}
\to
\text{微分}
\to
\text{動態閉合}.
}
$$

### 10.1 無形成則無積分

若積分形成律不成立，後續所有保存與閉合問題都無對象可談。

### 10.2 無來源則無法判斷坍縮

若來源不可追蹤，就無法判定哪些差異被抹除。

### 10.3 無非坍縮則守衛失真

若上一層已失去必要差異，下一層守衛便可能基於錯誤結構判定。

### 10.4 無守衛則持續積分失控

若每次再積分不重新判定，持續積分會退化為無條件吞併。

### 10.5 無微分則不可檢查

若無法揭露來源、差異、邊界與障礙，就無法驗證積分是否合法。

### 10.6 無閉合則只有有限構造

若沒有動態整體閉合，X 積分只能描述一次性結構組合，不能成為持續代數。

---

## 11. 六律的統一形式

定義一個候選積分：

$$
Z
=
\mathsf I_{\rho}(X;Y).
$$

它成為合法 X 積分，至少需要：

$$
\operatorname{Form}(Z),
$$

$$
\operatorname{SrcPres}(Z),
$$

$$
\operatorname{NonCollapse}(Z),
$$

$$
\operatorname{Guardable}(Z),
$$

$$
\operatorname{StructDiff}(Z),
$$

$$
\operatorname{DynClosable}(Z).
$$

統一寫為：

$$
\boxed{
\operatorname{XInt}_{\Gamma}
(\rho;X,Y;Z)
}
$$

當且僅當：

$$
\begin{aligned}
&
\operatorname{FormCond}_{\Gamma}(\rho;X,Y)
\\
&\land
\operatorname{SrcPres}_{\Gamma}(X,Y,\rho;Z)
\\
&\land
\operatorname{NonCollapse}_{\Gamma}(X,Y;Z)
\\
&\land
\operatorname{Guardable}_{\Gamma}(Z)
\\
&\land
\operatorname{StructDiff}_{\Gamma}(Z)
\\
&\land
\operatorname{DynClosable}_{\Gamma}(Z).
\end{aligned}
$$

---

## 12. 最低 X 積分完備性命題

### 命題

若一個候選操作 $\mathsf J$ 對任意合法輸入只滿足形成條件，但不滿足來源保存、非坍縮、再積分守衛、結構微分或動態閉合中的任一項，則 $\mathsf J$ 最多是一種結構組合操作，不能構成完整的持續 X 積分。

形式上：

$$
\operatorname{Form}(\mathsf J)
\land
\neg
\left[
\operatorname{SrcPres}
\land
\operatorname{NonCollapse}
\land
\operatorname{Guardable}
\land
\operatorname{StructDiff}
\land
\operatorname{DynClosable}
\right]
$$

推出：

$$
\boxed{
\mathsf J
\notin
\operatorname{FullXIntegral}.
}
$$

### 意義

這條命題把 X 積分與普通：

- 合併；
- 串接；
- 聯集；
- 圖節點聚合；
- 型別封裝；
- 公理附加；
- 集合閉包；

區分開來。

---

## 13. 失敗模式矩陣

| 失敗律 | 表面現象 | 深層問題 |
|---|---|---|
| 積分形成律失敗 | 任何東西都可積分 | 無合法性邊界 |
| 來源保存律失敗 | 不知結構從何而來 | 不可追溯、不可驗證 |
| 非坍縮律失敗 | 所有差異被統一 | 類型與範疇混同 |
| 再積分守衛律失敗 | 一次合法後無限合法 | 持續生成失控 |
| 結構微分律失敗 | 無法揭露內部條件 | 不能分析與反證 |
| 動態整體閉合律失敗 | 每次積分都成為新碎片 | 無持續身份 |

---

## 14. 最小示例

設：

$$
\Gamma\vdash A:\mathcal A,
$$

$$
\Gamma\vdash B:\mathcal B,
$$

$$
\Gamma\vdash A\bowtie_{\rho}B.
$$

形成：

$$
C=\mathsf I_{\rho}(A;B).
$$

### 14.1 形成律

$$
\Gamma\vdash C:\mathcal C.
$$

### 14.2 來源保存律

$$
\operatorname{Src}(C)
=
\langle A,B,\rho,\Gamma\rangle.
$$

### 14.3 非坍縮律

若：

$$
A\not\equiv B,
$$

則：

$$
\iota_A(A)\not\equiv\iota_B(B).
$$

### 14.4 再積分守衛律

若欲加入 D：

$$
\mathsf I_{\sigma}(C;D),
$$

必須先有：

$$
\mathsf G_{\Gamma'}(\sigma;C,D).
$$

### 14.5 結構微分律

$$
\mathsf D_{\mathrm{src}}(C)
\simeq
\langle A,B,\rho\rangle.
$$

### 14.6 動態整體閉合律

若 C 屬於持續整體 $\mathsf C[A]$ ，且 D 通過守衛，則：

$$
\mathsf I_{\sigma}(C;D)
\in_{\mathrm{dyn}}
\mathsf C[A].
$$

---

## 15. 對抽象代數應用的約束

此前可將群寫成：

$$
\operatorname{Grp}(X,\ast)
=
\int_{\mathrm{inv}}
\int_{\mathrm{id}}
\int_{\mathrm{assoc}}
\int_{\mathrm{cl}}
(X;\ast).
$$

但六律要求每一層都回答：

- 此公理為何可被積分？
- 前一層結構如何嵌入下一層？
- 哪些差異被保存？
- 下一層積分需要哪些守衛？
- 如何微分出缺失公理？
- 整條鏈是否形成同一持續結構？

因此，真正完整的群 X 積分不是只有巢狀記號，而是：

$$
\operatorname{Grp}_X
=
\left\langle
\int_{\mathrm{inv}}
\int_{\mathrm{id}}
\int_{\mathrm{assoc}}
\int_{\mathrm{cl}}
(X;\ast),
\operatorname{Cert}_{6L}
\right\rangle,
$$

其中：

$$
\operatorname{Cert}_{6L}
$$

是六律合法性證書。

---

## 16. 六律合法性證書

定義：

$$
\operatorname{Cert}_{6L}(Z)
=
\langle
C_F,
C_S,
C_N,
C_G,
C_D,
C_C
\rangle,
$$

其中：

- $C_F$ ：積分形成證書；
- $C_S$ ：來源保存證書；
- $C_N$ ：非坍縮證書；
- $C_G$ ：再積分守衛證書；
- $C_D$ ：結構微分證書；
- $C_C$ ：動態整體閉合證書。

完整 X 積分應滿足：

$$
\operatorname{Verify}
\left(
\operatorname{Cert}_{6L}(Z)
\right)
=
\operatorname{Valid}.
$$

此處 $\operatorname{Valid}$ 是元層判定，不是數值結果。

---

## 17. 可推導的初步定理

### 定理一：來源可追蹤定理

若 Z 滿足形成律與強來源保存律，則存在合法來源微分，使：

$$
\mathsf D_{\mathrm{src}}(Z)
\simeq
\operatorname{Src}(Z).
$$

### 定理二：非法坍縮可檢出定理

若 Z 滿足來源保存律與結構微分律，且某必要差異未在 Z 中延續，則非坍縮律失敗可由差異微分檢出。

### 定理三：再積分非傳遞定理

存在 X、Y、Z 與關係 $\rho,\sigma$ ，使：

$$
\Gamma\vdash\mathsf I_{\rho}(X;Y)
$$

但：

$$
\Gamma\nvdash
\mathsf I_{\sigma}
\left(
\mathsf I_{\rho}(X;Y);Z
\right).
$$

### 定理四：動態身份保存定理雛形

若持續積分鏈中的每一步皆滿足六律，且身份核心在每一步合法延續，則整條鏈形成一個動態閉合整體。

---

## 18. 尚未解決的問題

### 18.1 最小來源保存程度

是否所有 X 積分都必須允許完整來源恢復，或弱追蹤已足夠？

### 18.2 必要差異的判定

如何形式化：

$$
\Delta_{\Gamma}^{\mathrm{ess}}(X,Y)?
$$

不同上下文可能認定不同差異為必要。

### 18.3 守衛可判定性

再積分守衛是否能在一般情況下機器判定，或只能在受限子系統中判定？

### 18.4 微分唯一性

給定相同模式 $\kappa$ ，結構微分是否存在正規形？

### 18.5 動態身份核心

何種結構構成：

$$
\operatorname{IdentityCore}(\mathsf C)?
$$

其改變到何種程度仍可稱為同一持續整體？

### 18.6 六律是否獨立

六條律能否由其中部分推出，或存在彼此獨立模型？

---

## 19. 後續形式化順序

正式研究應按以下順序推進：

### 第一階段

形式化積分形成律與類型判定。

### 第二階段

建立來源圖、來源嵌入與來源微分。

### 第三階段

定義必要差異核與非坍縮判定。

### 第四階段

建立再積分守衛與停止前沿。

### 第五階段

建立結構微分模式與完備性。

### 第六階段

建立動態身份、持續整體與閉合定理。

只有完成上述六階段後，群、環、域、商化、完備化與 Lie 理論的 X 積分實作，才具有正式理論地基。

---

## 20. 結論

X 積分不能只被定義為「持續加入結構」。若沒有基本律，任何附加公理、合併關係或形成閉包的操作，都可以被任意稱為積分。

本文提出的六條基本律建立了最低區辨標準：

$$
\boxed{
\text{積分形成律}
}
$$

確保積分不是任意並置。

$$
\boxed{
\text{來源保存律}
}
$$

確保整體不失去其形成歷史。

$$
\boxed{
\text{非坍縮律}
}
$$

確保整合不等於抹除差異。

$$
\boxed{
\text{再積分守衛律}
}
$$

確保持續積分不是無條件吞併。

$$
\boxed{
\text{結構微分律}
}
$$

確保整體可被揭露、分析與驗證。

$$
\boxed{
\text{動態整體閉合律}
}
$$

確保反覆積分能形成一個持續而非碎裂的整體。

六律共同構成：

$$
\boxed{
\operatorname{XInt}
=
\operatorname{Formation}
\land
\operatorname{Provenance}
\land
\operatorname{NonCollapse}
\land
\operatorname{Guard}
\land
\operatorname{Differentiation}
\land
\operatorname{DynamicClosure}.
}
$$

因此，X 積分的核心不只是：

$$
\text{一直積分},
$$

而是：

$$
\boxed{
\text{一直合法形成、一直保存來源、一直不坍縮、一直重新守衛、一直可被微分揭露，並一直維持動態整體。}
}
$$

---

## 附錄 A：六律簡表

| 基本律 | 核心問題 | 最小要求 |
|---|---|---|
| 積分形成律 | 積分能否形成？ | 類型、關係、邊界、權限合法 |
| 來源保存律 | 從何而來？ | 構成者、關係與形成史可追蹤 |
| 非坍縮律 | 差異是否被抹除？ | 必要差異在整體中延續 |
| 再積分守衛律 | 能否繼續積分？ | 每層重新判定 |
| 結構微分律 | 能否揭露內部結構？ | 來源、差異、邊界與障礙可分解 |
| 動態整體閉合律 | 能否形成持續整體？ | 身份、來源、邊界與接口持續 |

---

## 附錄 B：一句話定義

> 完整 X 積分是這樣一種結構形成：它必須合法形成、保存來源、避免必要差異坍縮、在每次再積分前重新通過守衛、能被結構微分揭露，並在持續變化中維持動態整體閉合。
