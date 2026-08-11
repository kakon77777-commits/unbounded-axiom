# X 分數結構微積分純數學實戰 III：射影直線、換圖證書與無窮遠點的非奇異性判定

**英文題名**：*X-Fraction Structural Calculus: Pure Mathematics Experiment III — The Projective Line, Chart-Transition Certificates, and the Non-Singularity of the Point at Infinity*

**版本**：v0.1  
**日期**：2026-07-26  
**系列位置**：X 分數結構微積分純數學實戰 III  
**前篇 I**：《X 分數結構微積分純數學實戰 I：可去表示缺口、局部化與來源非坍縮》  
**前篇 II**：《X 分數結構微積分純數學實戰 II：一般局部化、 $S$ -湮滅與強迫來源坍縮》  
**性質**：純數學壓力測試、射影語義修正案、主論文 v0.2 改版依據  
**狀態**：可供內部檢驗；尚非最終公理版

---

## 摘要

本文對 X 分數結構微積分進行第三次純數學實戰。前兩次實戰分別證明：

$$
\text{表示合法性}
\neq
\text{商類合法性},
$$

以及：

$$
\text{來源差異}
\neq
\text{商類差異}.
$$

本次考察域 $k$ 上的射影直線：

$$
\mathbb P^1(k)
=
\left(
k^2\setminus\{(0,0)\}
\right)/k^\times.
$$

射影點由非零齊次對：

$$
(a,b)\neq(0,0)
$$

形成，並在同步非零縮放下識別：

$$
(a,b)
\sim_{\mathbb P}
(\lambda a,\lambda b),
\qquad
\lambda\in k^\times.
$$

本文得到三項核心結果。

第一，射影分數線不是普通代數商的另一種寫法。普通商：

$$
\frac ab
$$

要求：

$$
b\neq0,
$$

而射影點：

$$
[a:b]
$$

只要求：

$$
(a,b)\neq(0,0).
$$

因此：

$$
[1:0]
\in
\mathbb P^1(k)
$$

是合法射影點，但：

$$
\frac10
$$

不是 $k$ 中的合法商。把兩者視為同一對象是關係型別錯誤。

第二，同一方程：

$$
ad-bc=0
$$

可以判定普通分式相等，也可以判定射影點相等；但兩種判定的形成域與證書型別不同。公式相同不足以決定關係本體：

$$
\boxed{
C_{\mathrm{quot}}
\not\equiv
C_{\mathrm{proj}}.
}
$$

第三，射影直線不能由單一全域商座標描述。它由兩張仿射圖：

$$
U_0=\{[a:b]:a\neq0\},
$$

$$
U_1=\{[a:b]:b\neq0\}
$$

覆蓋。在重疊區中，座標：

$$
u=\frac ba,
\qquad
v=\frac ab
$$

滿足：

$$
uv=1.
$$

若選擇：

$$
j:k\hookrightarrow\mathbb P^1(k),
\qquad
j(v)=[v:1]
$$

作為仿射嵌入，則：

$$
\infty=[1:0]
$$

只是 $U_1$ 的圖表邊界；它在另一張圖 $U_0$ 中具有合法座標：

$$
u=0.
$$

由於 $\mathbb P^1$ 在此點附近仍同構於仿射直線，無窮遠點不是幾何奇點。故 X 奇點分類必須加入：

$$
\boxed{
\operatorname{ChartFail}
\not\Rightarrow
\operatorname{ObjectSingular}.
}
$$

本輪沒有產生新的射影幾何定理。新增價值是把射影形成、縮放商化、圖表選擇、正規化、換圖、圖表邊界、替代圖實現與全域黏合整理為同一個可稽核的 X 證書架構。

**關鍵詞**：X 積分；X 分數；射影直線；齊次座標；帶類型分數線；仿射圖；換圖；無窮遠點；圖表邊界；奇點分類

---

# 第一部　結果先行

## 0.1 本輪最短結論

在射影直線中：

$$
\boxed{
[1:0]
\text{ 合法},
\qquad
\frac10
\text{ 不合法}.
}
$$

兩者不矛盾，因為：

$$
/_{\mathrm{projective}}
\not\equiv
/_{\mathrm{quot}}.
$$

## 0.2 第一個核心修正

射影關係中，第二來源不是全域分母。

在形成射影點前，兩個來源應稱為：

$$
\operatorname{HomCoord}_0(a),
\qquad
\operatorname{HomCoord}_1(b),
$$

而不是預先固定為：

$$
\operatorname{Numerator}(a),
\qquad
\operatorname{Denominator}(b).
$$

只有選定圖表後，其中一個非零座標才暫時扮演正規化參照。

因此，X 分數來源角色必須由關係型別決定：

$$
\boxed{
\operatorname{Role}_{\rho,0},
\quad
\operatorname{Role}_{\rho,1},
}
$$

不能把所有二元分數結構都預設成分子—分母。

## 0.3 第二個核心修正

同一代數式：

$$
ad-bc=0
$$

可出現在兩種不同判定中。

普通商：

$$
\frac ab=\frac cd
$$

要求：

$$
b\neq0,
\qquad
d\neq0.
$$

射影相等：

$$
[a:b]=[c:d]
$$

要求：

$$
(a,b)\neq(0,0),
\qquad
(c,d)\neq(0,0).
$$

所以：

$$
\boxed{
\text{證明公式相同}
\not\Rightarrow
\text{被證明的關係同型}.
}
$$

## 0.4 第三個核心修正

圖表失敗不是對象失敗。

對：

$$
P_\infty=[1:0],
$$

仿射座標：

$$
v=\frac ab
$$

不可形成，因為 $b=0$ 。

但另一圖表座標：

$$
u=\frac ba
$$

合法且等於零。

因此：

$$
\boxed{
\neg\operatorname{ChartLegal}_{U_1}(P_\infty)
\quad\land\quad
\operatorname{ChartLegal}_{U_0}(P_\infty).
}
$$

不能由第一項推出：

$$
\neg\operatorname{ObjectLegal}(P_\infty).
$$

## 0.5 第四個核心修正

射影整體不是一個全域數值座標，而是一個圖冊黏合：

$$
\boxed{
\mathbb P^1
\cong
\mathbb A^1_u
\cup_{\mathbb G_m}
\mathbb A^1_v,
\qquad
v=u^{-1}.
}
$$

所以動態整體閉合律應允許：

$$
\text{atlas-valued whole},
$$

而不要求：

$$
\text{single-global-coordinate whole}.
$$

## 0.6 總判定

本輪總判定為：

$$
\boxed{
\operatorname{PassWithGeometricCoreRevision}.
}
$$

---

# 第二部　研究問題與失敗標準

## 1. 核心研究問題

本輪問題是：

> 當分數字形進入射影幾何時，X 分數系統能否區分普通商與齊次比例、接受縮放等價、正確處理圖表邊界、建立合法換圖，並把兩個局部坐標再積分為不具單一全域座標的整體？

## 2. 測試假設

### H1：射影保守性

忘卻 X 證書後，所得對象必須回到標準射影直線：

$$
U(\operatorname{XProjLine}(k))
\cong
\mathbb P^1(k).
$$

### H2：關係型別決定形成規則

系統必須區分：

$$
/_{\mathrm{quot}}
$$

與：

$$
/_{\mathrm{projective}}.
$$

### H3：縮放商化合法

對任意：

$$
\lambda\in k^\times,
$$

必須接受：

$$
[a:b]
=
[\lambda a:\lambda b].
$$

### H4：圖表覆蓋

每個射影點至少進入一張合法圖表。

### H5：換圖守衛

只有在：

$$
a\neq0,
\qquad
b\neq0
$$

時，才可同時使用兩張圖並執行反演換圖。

### H6：無窮遠點非奇點

對指定仿射嵌入的無窮遠點，圖表失敗不得被誤判為射影對象奇點。

### H7：圖冊整體閉合

兩張圖應可在合法重疊上黏合為 $\mathbb P^1$ ，即使不存在單一全域仿射座標。

## 3. 明確失敗條件

若系統出現下列任一結果，本輪即判定失敗：

1. 因第二座標為零而拒絕 $[1:0]$ ；
2. 接受 $[0:0]$ 為射影點；
3. 允許使用 $\lambda=0$ 作為射影縮放；
4. 把 $[1:0]$ 當成域 $k$ 中未定義的普通商 $\operatorname{Quot}_k(1,0)$ ；
5. 把 $ad-bc=0$ 的字形相同當成兩種關係同型的充分理由；
6. 在 $a=0$ 或 $b=0$ 時強行執行雙向換圖；
7. 把單一圖表失敗分類為射影直線的幾何奇點；
8. 宣稱射影直線具有單一全域仿射座標；
9. 因來源表示不同而拒絕合法縮放等價；
10. 把仿射無窮遠點說成未指定圖表也絕對存在的固有標記。

---

# 第三部　標準射影基線

## 4. 射影直線的定義

令 $k$ 為域。

定義：

$$
\mathbb P^1(k)
:=
\left(
k^2\setminus\{(0,0)\}
\right)/{\sim_{\mathbb P}},
$$

其中：

$$
(a,b)\sim_{\mathbb P}(c,d)
$$

若且唯若存在：

$$
\lambda\in k^\times
$$

使：

$$
(c,d)
=
(\lambda a,\lambda b).
$$

等價類記為：

$$
[a:b].
$$

## 4.1 X 射影形成記號

本文保留冒號字形：

$$
[a:b]
$$

以避免把射影點誤讀成普通商。

在 X 形成層可寫為：

$$
\operatorname{XProjFrac}^{\Gamma}(a,b)
:=
\mathsf I_{\mathrm{projective}}^{\Gamma}(a;b),
$$

其關係證書明示：

$$
\rho
=
/_{\mathrm{projective}}.
$$

忘卻 X 軌跡後：

$$
U_{\mathbb P}
\left(
\operatorname{XProjFrac}^{\Gamma}(a,b)
\right)
=
[a:b].
$$

## 5. 為何排除 $(0,0)$

零向量不張成一維子空間。

此外，若允許：

$$
(0,0),
$$

則它不能藉由非零縮放正規化成任一：

$$
[1:u]
$$

或：

$$
[v:1].
$$

所以形成守衛是：

$$
\boxed{
\operatorname{ProjForm}(a,b)
\Longleftrightarrow
(a,b)\neq(0,0).
}
$$

它不是：

$$
b\neq0.
$$

## 6. 為何縮放量必須非零

若允許：

$$
\lambda=0,
$$

則每個非零對都會被送到：

$$
(0,0).
$$

這會使縮放作用離開形成域，並破壞等價關係。

因此：

$$
\boxed{
\lambda\in k^\times
}
$$

是射影商化的必要守衛。

## 7. 行列式判準

對兩個合法齊次對：

$$
p=(a,b),
\qquad
q=(c,d),
$$

定義射影缺陷：

$$
\Delta_{\mathbb P}(p,q)
:=
ad-bc.
$$

則：

$$
\boxed{
[a:b]=[c:d]
\Longleftrightarrow
ad-bc=0.
}
$$

### 證明

若：

$$
(c,d)
=
(\lambda a,\lambda b),
$$

則：

$$
ad-bc
=
a(\lambda b)-b(\lambda a)
=
0.
$$

反向地，假設：

$$
ad-bc=0.
$$

若 $a\neq0$ ，令：

$$
\lambda=\frac ca.
$$

由：

$$
ad=bc
$$

可得：

$$
d=\lambda b.
$$

由於 $(c,d)\neq(0,0)$ ，此 $\lambda$ 非零。

若 $a=0$ ，則 $b\neq0$ 。由：

$$
-bc=0
$$

可得：

$$
c=0.
$$

再令：

$$
\lambda=\frac db.
$$

即可得到：

$$
(c,d)
=
(\lambda a,\lambda b).
$$

證畢。

## 8. 射影縮放證書

定義：

$$
\operatorname{ProjScaleCert}
\big(
(a,b),(c,d);\lambda
\big)
$$

成立，若且唯若：

$$
\lambda\in k^\times,
$$

$$
c=\lambda a,
$$

$$
d=\lambda b.
$$

證書至少記錄：

$$
C_{\mathrm{scale}}
=
\left(
\lambda,
c=\lambda a,
d=\lambda b,
\lambda\neq0
\right).
$$

---

# 第四部　同一公式，不同關係

## 9. 普通商相等

若：

$$
b\neq0,
\qquad
d\neq0,
$$

則：

$$
\frac ab
=
\frac cd
$$

若且唯若：

$$
ad-bc=0.
$$

這是域 $k$ 中兩個商值的相等。

## 10. 射影點相等

若：

$$
(a,b)\neq(0,0),
$$

$$
(c,d)\neq(0,0),
$$

則：

$$
[a:b]
=
[c:d]
$$

若且唯若：

$$
ad-bc=0.
$$

這是一維子空間或齊次比例類的相等。

## 11. 公式不足以指定本體

兩個判定共享：

$$
ad-bc=0,
$$

但其前提不同：

| 判定 | 輸入形成域 | 結果型別 |
| --- | --- | --- |
| 普通商相等 | $b,d\neq0$ | $k$ 中的元素相等 |
| 射影點相等 | 兩個齊次對皆非零 | $\mathbb P^1(k)$ 中的點相等 |

例如：

$$
[1:0]=[\lambda:0]
$$

對所有 $\lambda\in k^\times$ 成立。

但：

$$
\frac10,
\qquad
\frac{\lambda}{0}
$$

都不是 $k$ 中的合法商。

因此：

$$
\boxed{
\operatorname{ProofShape}
\neq
\operatorname{RelationType}.
}
$$

## 12. 關係標記證書

任何使用：

$$
ad-bc=0
$$

的證書都必須同時標記：

$$
\rho
\in
\left\{
/_{\mathrm{quot}},
/_{\mathrm{projective}}
\right\}.
$$

因此：

$$
C_{\mathrm{quot}}
=
\left(
\rho_{\mathrm{quot}},
b\neq0,
d\neq0,
ad-bc=0
\right),
$$

而：

$$
C_{\mathrm{proj}}
=
\left(
\rho_{\mathrm{projective}},
(a,b)\neq(0,0),
(c,d)\neq(0,0),
\operatorname{ProjScaleCert}
\right).
$$

兩者不可互換。

---

# 第五部　來源角色的關係依賴

## 13. 普通商中的角色

對：

$$
\frac ab,
$$

可指定：

$$
\operatorname{Role}_{\mathrm{quot},0}(a)
=
\operatorname{Numerator}(a),
$$

$$
\operatorname{Role}_{\mathrm{quot},1}(b)
=
\operatorname{Denominator}(b).
$$

其中 $b$ 必須可逆。

## 14. 射影關係中的角色

對：

$$
[a:b],
$$

兩個來源首先是齊次座標：

$$
\operatorname{Role}_{\mathrm{proj},0}(a)
=
\operatorname{HomCoord}_0(a),
$$

$$
\operatorname{Role}_{\mathrm{proj},1}(b)
=
\operatorname{HomCoord}_1(b).
$$

兩者在全域定義中對稱。

形成條件不是「第二來源可逆」，而是：

$$
(a,b)\neq(0,0).
$$

## 15. 圖表選擇才產生暫時分母

若選擇：

$$
a\neq0,
$$

則可用 $a$ 正規化並形成：

$$
u=\frac ba.
$$

此時 $a$ 才在圖表 $U_0$ 中暫時扮演除法參照。

若選擇：

$$
b\neq0,
$$

則可用 $b$ 正規化並形成：

$$
v=\frac ab.
$$

因此：

$$
\boxed{
\operatorname{DenominatorRole}
\text{ 是圖表相對角色，不是射影來源的全域身份。}
}
$$

## 16. 對 X 分數語法的要求

通用二元形成語法應使用：

$$
\operatorname{SrcSlot}_0(a),
\qquad
\operatorname{SrcSlot}_1(b),
$$

再由：

$$
\rho
$$

指定角色：

$$
\operatorname{RoleAssign}_{\rho}
:
(a,b)
\longmapsto
\big(
\operatorname{Role}_{\rho,0}(a),
\operatorname{Role}_{\rho,1}(b)
\big).
$$

所以：

$$
\boxed{
\text{分數線型別必須參與角色生成，而不只是完成後的標籤。}
}
$$

---

# 第六部　雙仿射圖

## 17. 第一張圖 $U_0$

定義：

$$
U_0
:=
\left\{
[a:b]\in\mathbb P^1(k):
a\neq0
\right\}.
$$

座標映射為：

$$
\phi_0:
U_0
\longrightarrow
k,
$$

$$
\phi_0([a:b])
=
\frac ba.
$$

其逆映射為：

$$
\phi_0^{-1}(u)
=
[1:u].
$$

因此：

$$
U_0
\cong
\mathbb A^1_u(k).
$$

## 18. 第二張圖 $U_1$

定義：

$$
U_1
:=
\left\{
[a:b]\in\mathbb P^1(k):
b\neq0
\right\}.
$$

座標映射為：

$$
\phi_1:
U_1
\longrightarrow
k,
$$

$$
\phi_1([a:b])
=
\frac ab.
$$

其逆映射為：

$$
\phi_1^{-1}(v)
=
[v:1].
$$

因此：

$$
U_1
\cong
\mathbb A^1_v(k).
$$

## 19. 圖表覆蓋

任一射影點：

$$
[a:b]
$$

滿足：

$$
(a,b)\neq(0,0).
$$

故至少有：

$$
a\neq0
$$

或：

$$
b\neq0.
$$

因此：

$$
\boxed{
\mathbb P^1(k)
=
U_0\cup U_1.
}
$$

這可形成圖表覆蓋證書：

$$
\operatorname{ChartCoverCert}
\big(
\mathbb P^1;U_0,U_1
\big).
$$

## 20. 四種輸入狀態

| 齊次條件 | $U_0$ | $U_1$ | 射影狀態 |
| --- | --- | --- | --- |
| $a\neq0,\;b\neq0$ | 合法 | 合法 | 重疊區 |
| $a\neq0,\;b=0$ | 合法 | 不合法 | $U_1$ 的邊界點 |
| $a=0,\;b\neq0$ | 不合法 | 合法 | $U_0$ 的邊界點 |
| $a=0,\;b=0$ | 不合法 | 不合法 | 射影形成失敗 |

所以：

$$
\boxed{
\text{兩張圖都失敗}
\Longleftrightarrow
\text{輸入根本不是射影點}.
}
$$

---

# 第七部　圖表正規化

## 21. $U_0$ 正規化

若：

$$
a\neq0,
$$

取縮放量：

$$
\lambda=a^{-1}.
$$

則：

$$
[a:b]
=
[1:b/a].
$$

定義：

$$
\operatorname{NormCert}_0
\big(
[a:b];a^{-1}
\big).
$$

## 22. $U_1$ 正規化

若：

$$
b\neq0,
$$

取：

$$
\mu=b^{-1}.
$$

則：

$$
[a:b]
=
[a/b:1].
$$

定義：

$$
\operatorname{NormCert}_1
\big(
[a:b];b^{-1}
\big).
$$

## 23. 正規化不是來源刪除

若原始表示為：

$$
(a,b),
$$

正規化後雖得到：

$$
(1,b/a)
$$

或：

$$
(a/b,1),
$$

仍可保存：

$$
C_{\mathrm{norm}}
=
\left(
\begin{array}{l}
\text{原齊次對},\\
\text{所選圖表},\\
\text{縮放量},\\
\text{正規化後表示},\\
\text{縮放等價證書}
\end{array}
\right).
$$

正規化層相等不表示原始表示相同。

## 24. 無全域單一正規化

規則：

$$
[a:b]
\longmapsto
[a/b:1]
$$

在 $b=0$ 時失敗。

規則：

$$
[a:b]
\longmapsto
[1:b/a]
$$

在 $a=0$ 時失敗。

因此不存在由這兩個規則之一給出的全域單一正規化。

較正確的輸出是：

$$
\boxed{
\operatorname{AtlasNormalization}
=
\left\{
\operatorname{Norm}_0,
\operatorname{Norm}_1,
\operatorname{Transition}_{01}
\right\}.
}
$$

---

# 第八部　重疊區與換圖

## 25. 重疊條件

射影點同時位於兩張圖中，若且唯若：

$$
a\neq0,
\qquad
b\neq0.
$$

因此：

$$
U_0\cap U_1
\cong
k^\times
=
\mathbb G_m(k).
$$

## 26. 換圖公式

在重疊區中：

$$
u=\frac ba,
$$

$$
v=\frac ab.
$$

所以：

$$
\boxed{
uv=1.
}
$$

亦即：

$$
v=u^{-1},
$$

$$
u=v^{-1}.
$$

## 27. 換圖證書

定義：

$$
\operatorname{ChartTransitionCert}_{01}
\big(
[a:b];u,v
\big)
$$

成立，若且唯若：

$$
a\neq0,
$$

$$
b\neq0,
$$

$$
u=b/a,
$$

$$
v=a/b,
$$

$$
uv=1.
$$

其逆證書為：

$$
\operatorname{ChartTransitionCert}_{10}.
$$

並滿足：

$$
\tau_{10}\circ\tau_{01}
=
\operatorname{id}_{\mathbb G_m},
$$

$$
\tau_{01}\circ\tau_{10}
=
\operatorname{id}_{\mathbb G_m}.
$$

## 28. 換圖守衛

若：

$$
b=0,
$$

則：

$$
v=\frac ab
$$

不可形成。

若：

$$
a=0,
$$

則：

$$
u=\frac ba
$$

不可形成。

因此：

$$
\boxed{
\operatorname{TransitionGuard}_{01}(P)
\Longleftrightarrow
P\in U_0\cap U_1.
}
$$

換圖失敗不代表射影點失敗；它只表示該點不在圖表重疊域。

---

# 第九部　無窮遠點

## 29. 選擇仿射嵌入

選定：

$$
j_1:
k
\longrightarrow
\mathbb P^1(k),
$$

$$
j_1(v)
=
[v:1].
$$

其像為：

$$
U_1.
$$

相對於此嵌入，定義：

$$
\infty_{j_1}
:=
[1:0].
$$

並有：

$$
\mathbb P^1(k)
=
j_1(k)
\sqcup
\{\infty_{j_1}\}.
$$

這是集合與幾何對象的分解，不是把 $\infty$ 加入 $k$ 後仍保持原域結構。

## 30. 無窮遠不是普通商

下式不成立：

$$
\infty_{j_1}
=
\frac10
\quad\text{作為 }k\text{ 中元素}.
$$

正確說法是：

$$
\infty_{j_1}
=
[1:0]
\quad\text{作為射影點}.
$$

因此：

$$
\boxed{
\operatorname{ProjPoint}(1,0)
\text{ 合法}
\quad\land\quad
\operatorname{Quotient}(1,0)
\text{ 不合法}.
}
$$

## 31. 替代圖表中的合法座標

 $[1:0]$ 位於：

$$
U_0,
$$

且：

$$
\phi_0([1:0])
=
\frac01
=
0.
$$

所以：

$$
\boxed{
\operatorname{ChartFail}_{U_1}([1:0])
\quad\land\quad
\operatorname{ChartLegal}_{U_0}([1:0]).
}
$$

## 32. 無窮遠的相對性

若改選另一仿射嵌入：

$$
j_0:
k
\longrightarrow
\mathbb P^1(k),
$$

$$
j_0(u)
=
[1:u],
$$

則其補點為：

$$
\infty_{j_0}
=
[0:1].
$$

因此，未指定仿射嵌入時，「哪一點是無窮遠」不是絕對資料。

應寫成：

$$
\boxed{
\infty_{\Gamma_{\mathrm{aff}}}
}
$$

而不是無上下文的：

$$
\infty.
$$

---

# 第十部　圖表邊界不是幾何奇點

## 33. 對象層與圖表層

對：

$$
P_\infty=[1:0],
$$

有：

$$
\operatorname{ObjectLegal}_{\mathbb P^1}(P_\infty)
=
\operatorname{Yes}.
$$

但：

$$
\operatorname{ChartLegal}_{U_1}(P_\infty)
=
\operatorname{No}.
$$

兩者位於不同判定層。

## 34. 為何不是奇點

 $P_\infty$ 具有鄰近圖：

$$
U_0
\cong
\mathbb A^1.
$$

在此圖中，它對應：

$$
u=0.
$$

仿射直線在此點沒有幾何奇異性。因此：

$$
\boxed{
\operatorname{ObjectSingular}_{\mathbb P^1}(P_\infty)
=
\operatorname{No}.
}
$$

## 35. 邊界證書

定義圖表邊界證書：

$$
\operatorname{ChartBoundaryCert}
\big(
P;U_i,U_j
\big)
$$

至少包含：

$$
C_{\mathrm{boundary}}
=
\left(
\begin{array}{l}
\operatorname{ObjectLegal}(P),\\
\neg\operatorname{ChartLegal}_{U_i}(P),\\
\operatorname{ChartLegal}_{U_j}(P),\\
\operatorname{AltCoordinate}_{U_j}(P),\\
\neg\operatorname{ObjectSingular}(P)
\end{array}
\right).
$$

## 36. 奇點分類修正

原有「值域邊界型」或「表示缺口型」仍不足以表達本例。

至少應區分：

1. **圖表邊界**：一張圖失敗，另一張圖合法；
2. **圖冊覆蓋失敗**：所有指定圖都失敗，但可能需要擴充圖冊；
3. **對象形成失敗**：例如 $(0,0)$ ；
4. **幾何奇點**：對象合法，但局部幾何結構真正退化；
5. **普通商逆元失敗**：只影響 $/_{\mathrm{quot}}$ 。

核心推論限制為：

$$
\boxed{
\operatorname{ChartFail}
\nRightarrow
\operatorname{ObjectSingular}.
}
$$

---

# 第十一部　來源保存與縮放非坍縮

## 37. 同一射影點的多重來源表示

取：

$$
p=(a,b),
$$

以及：

$$
q=(\lambda a,\lambda b),
\qquad
\lambda\in k^\times.
$$

則在表示層：

$$
p\neq q
$$

可以成立。

但在射影商類層：

$$
[p]_{\mathbb P}
=
[q]_{\mathbb P}.
$$

## 38. 正確的非坍縮讀法

X 系統必須同時接受：

$$
\boxed{
p\not\equiv_{\mathrm{presentation}}q
\quad\land\quad
[p]_{\mathbb P}=[q]_{\mathbb P}.
}
$$

若因來源表示不同而拒絕射影相等，則不保守。

## 39. 軌跡保存

可在 X 外加層記錄：

$$
\operatorname{ProjTrace}
\big(
p,
q,
\lambda,
C_{\mathrm{scale}},
\Gamma_{\mathrm{chart}}
\big).
$$

但這些資料不是射影點本身的唯一內在代表。

同一射影點具有整個：

$$
k^\times
$$

軌道的表示。

## 40. 正規化來源依賴圖表

對重疊區中的點：

$$
P=[a:b],
\qquad
a,b\neq0,
$$

可同時有：

$$
P=[1:u],
\qquad
u=b/a,
$$

以及：

$$
P=[v:1],
\qquad
v=a/b.
$$

兩個正規化都合法，但依賴不同圖表。

因此，不存在未指定圖表的唯一「標準分數表示」。

---

# 第十二部　射影缺陷的結構微分

## 41. 原始缺陷

對齊次對：

$$
p=(a,b),
\qquad
q=(c,d),
$$

定義：

$$
\Delta_{\mathbb P}(p,q)
=
ad-bc.
$$

## 42. 缺陷值不是射影不變量

若重縮放：

$$
p'=\lambda p,
\qquad
q'=\mu q,
$$

其中：

$$
\lambda,\mu\in k^\times,
$$

則：

$$
\Delta_{\mathbb P}(p',q')
=
\lambda\mu\,
\Delta_{\mathbb P}(p,q).
$$

所以原始缺陷的具體值依賴表示。

## 43. 缺陷消失性是射影不變量

雖然缺陷值改變，但：

$$
\Delta_{\mathbb P}(p,q)=0
$$

若且唯若：

$$
\Delta_{\mathbb P}(p',q')=0.
$$

因此射影內在判定應保存：

$$
\operatorname{Vanish}
\big(
\Delta_{\mathbb P}
\big),
$$

而不是把未正規化的缺陷值當成射影點對的絕對數值。

## 44. 射影結構微分

可定義：

$$
\mathsf D_{\mathrm{proj}}(P,Q)
:=
\left(
\begin{array}{l}
\operatorname{DefectVanishStatus},\\
\operatorname{ScaleCertStatus},\\
\operatorname{ChartSupport}(P),\\
\operatorname{ChartSupport}(Q),\\
\operatorname{TransitionStatus},\\
\operatorname{PresentationTrace}
\end{array}
\right).
$$

其核心不是數值微分，而是回答：

$$
\boxed{
\text{哪些表示差異是齊次尺度，哪些差異仍是射影對象差異。}
}
$$

## 45. 對兩個縮放表示的輸出

若：

$$
Q=[\lambda a:\lambda b],
\qquad
\lambda\in k^\times,
$$

則：

$$
\Delta_{\mathbb P}
\big(
(a,b),(\lambda a,\lambda b)
\big)
=
0.
$$

因此：

$$
\mathsf D_{\mathrm{proj}}(P,Q)
$$

應輸出：

$$
\operatorname{SameProjectivePoint},
$$

同時保留：

$$
\operatorname{DifferentPresentation}
$$

及：

$$
\operatorname{ScaleWitness}(\lambda).
$$

---

# 第十三部　圖冊黏合

## 46. 兩個局部整體

兩張圖各自為：

$$
U_0\cong\mathbb A^1_u,
$$

$$
U_1\cong\mathbb A^1_v.
$$

它們不是互斥上下文。

## 47. 共同語境

重疊區為：

$$
U_0\cap U_1
\cong
\mathbb G_m.
$$

在此共同語境中：

$$
u\neq0,
\qquad
v\neq0,
$$

且：

$$
uv=1.
$$

所以：

$$
\operatorname{MergeGuard}(U_0,U_1)
=
\operatorname{Pass}.
$$

## 48. 黏合資料

射影直線可由下列資料重建：

$$
\mathcal A_{\mathbb P^1}
=
\left(
U_0,
U_1,
U_{01},
\tau_{01},
\tau_{10}
\right),
$$

其中：

$$
U_{01}=U_0\cap U_1,
$$

$$
\tau_{01}(u)=u^{-1},
$$

$$
\tau_{10}(v)=v^{-1}.
$$

## 49. 黏合證書

定義：

$$
\operatorname{AtlasGlueCert}
\big(
U_0,U_1,U_{01},\tau_{01}
\big)
$$

至少要求：

1. $U_0,U_1$ 各自形成；
2. $U_{01}$ 明確；
3. $\tau_{01}$ 在 $U_{01}$ 上合法；
4. $\tau_{10}$ 是其逆；
5. 兩個圖覆蓋目標整體；
6. 重疊上的表示相容。

## 50. 動態整體的正確形式

本例的整體不是：

$$
\mathbb P^1
\cong
\mathbb A^1
$$

配上一個失敗值。

而是：

$$
\boxed{
\mathbb P^1
\cong
\mathbb A^1_u
\cup_{u\mapsto u^{-1}}
\mathbb A^1_v.
}
$$

因此，X 動態整體閉合可以輸出圖冊，而非強迫壓成單一值域。

---

# 第十四部　與第二次實戰的交叉比較

## 51. 空重疊案例

第二次實戰取：

$$
R=k[X,Y]/(XY).
$$

兩個基本開集滿足：

$$
D(x)\cap D(y)
=
D(xy)
=
\varnothing.
$$

因此共同非平凡局部化不存在：

$$
\operatorname{MergeGuard}
=
\operatorname{Fail}.
$$

## 52. 非空重疊案例

本輪中：

$$
U_0\cap U_1
\cong
\mathbb G_m
\neq
\varnothing.
$$

且存在合法換圖：

$$
u\longmapsto u^{-1}.
$$

所以：

$$
\operatorname{MergeGuard}
=
\operatorname{Pass}.
$$

## 53. 守衛不是固定拒絕器

兩輪合併後可知，再積分守衛不是：

$$
\text{一律拒絕跨上下文整合},
$$

也不是：

$$
\text{一律允許跨上下文整合}.
$$

它必須依實際重疊與轉換資料輸出：

$$
\boxed{
\operatorname{Pass},
\quad
\operatorname{Fail},
\quad
\operatorname{Partial}.
}
$$

這使守衛具備可反駁性。

---

# 第十五部　X 多層形成流程

## 54. 齊次來源形成

先形成來源對：

$$
(a,b)\in k^2.
$$

## 55. 射影形成守衛

檢查：

$$
(a,b)\neq(0,0).
$$

## 56. 射影商類形成

形成：

$$
[a:b]_{\sim_{\mathbb P}}.
$$

## 57. 圖表支援判定

判定：

$$
a\neq0
$$

與：

$$
b\neq0.
$$

## 58. 仿射商座標形成

只在相應圖表中形成：

$$
u=b/a
$$

或：

$$
v=a/b.
$$

## 59. 換圖判定

只在：

$$
a,b\neq0
$$

時形成：

$$
v=u^{-1}.
$$

## 60. 圖冊再積分

最後形成：

$$
\operatorname{AtlasGlue}
\left(
U_0,U_1,\tau_{01}
\right).
$$

## 61. 完整流程

$$
\boxed{
\begin{aligned}
&\text{齊次來源對}\\
\longrightarrow\;&\text{非零對守衛}\\
\longrightarrow\;&\text{射影縮放商類}\\
\longrightarrow\;&\text{圖表支援判定}\\
\longrightarrow\;&\text{局部普通商座標}\\
\longrightarrow\;&\text{重疊換圖}\\
\longrightarrow\;&\text{圖冊整體黏合}.
\end{aligned}
}
$$

注意：

$$
/_{\mathrm{quot}}
$$

只在第五步局部出現，不是第一步的全域關係。

---

# 第十六部　六大基本律稽核

## 62. 第一律：形成律

### 原要求

合法來源與關係形成完整分數。

### 本輪發現

射影形成條件是：

$$
(a,b)\neq(0,0),
$$

而不是：

$$
b\neq0.
$$

來源角色亦須由關係型別分派。

### 判定

$$
\boxed{
\operatorname{PassWithRoleRevision}.
}
$$

## 63. 第二律：來源保存律

原始齊次對、縮放量、圖表選擇與正規化路徑均可保存為外加軌跡。

但射影點本身沒有唯一齊次代表。

### 判定

$$
\boxed{
\operatorname{PassAsPresentationTrace}.
}
$$

## 64. 第三律：非坍縮律

系統必須接受：

$$
[a:b]
=
[\lambda a:\lambda b],
\qquad
\lambda\in k^\times,
$$

同時不把兩個原始表示宣稱為字面相同。

### 判定

$$
\boxed{
\operatorname{PassWithTypedQuotient}.
}
$$

若非坍縮被理解為拒絕射影縮放商化，則失敗。

## 65. 第四律：再積分守衛律

兩張圖只在：

$$
U_0\cap U_1
\cong
\mathbb G_m
$$

上換圖。

邊界點不進入不合法轉換，但仍由另一圖覆蓋。

### 判定

$$
\boxed{
\operatorname{StrongPass}.
}
$$

## 66. 第五律：結構微分律

本輪可展開：

$$
\operatorname{DefectVanishStatus},
$$

$$
\operatorname{ScaleCert},
$$

$$
\operatorname{ChartSupport},
$$

$$
\operatorname{BoundaryMode},
$$

$$
\operatorname{TransitionStatus}.
$$

並揭露缺陷值本身不是射影不變量，只有其消失性是。

### 判定

$$
\boxed{
\operatorname{StrongPass}.
}
$$

## 67. 第六律：動態整體閉合律

兩個局部整體透過合法重疊與反演換圖形成：

$$
\mathbb P^1.
$$

這是一個沒有單一全域仿射座標的合法整體。

### 判定

若閉合允許圖冊型整體：

$$
\boxed{
\operatorname{StrongPass}.
}
$$

若閉合要求單一全域座標：

$$
\boxed{
\operatorname{Fail}.
}
$$

## 68. 六律總表

| 基本律 | 判定 | 本輪修正 |
| --- | --- | --- |
| 形成律 | 通過但需角色修正 | 射影形成使用非零齊次對 |
| 來源保存律 | 軌跡版通過 | 齊次代表不是內在唯一資料 |
| 非坍縮律 | 帶型商化版通過 | 接受縮放等價，保存表示差異 |
| 再積分守衛律 | 強通過 | 僅在 $\mathbb G_m$ 上換圖 |
| 結構微分律 | 強通過 | 保存缺陷消失性而非任意缺陷值 |
| 動態整體閉合律 | 圖冊版強通過 | 整體不必有單一全域座標 |

---

# 第十七部　對主論文公理的修正案

## 69. XF-1 修正：來源槽與角色分離

形成前先有中性來源槽：

$$
\operatorname{SrcSlot}_0(a),
\qquad
\operatorname{SrcSlot}_1(b).
$$

再由關係型別：

$$
\rho
$$

分派角色。

不得在所有關係中預設：

$$
\operatorname{Numerator},
\qquad
\operatorname{Denominator}.
$$

## 70. XF-2 加強：關係型別具生成力

關係型別不只標記結果，而必須決定：

1. 形成域；
2. 來源角色；
3. 等價關係；
4. 合法失敗；
5. 正規化方式；
6. 目標對象型別。

因此：

$$
\boxed{
\rho
\text{ 是形成規則參數，不是註解。}
}
$$

## 71. XF-3 修正：分母守衛局部化

對射影關係，全域形成不使用：

$$
\operatorname{DenLegal}(b).
$$

只有選定圖表後，才使用：

$$
\operatorname{ChartDenLegal}_{U_0}(a),
$$

或：

$$
\operatorname{ChartDenLegal}_{U_1}(b).
$$

## 72. XF-4 修正：形成分層

新增：

$$
\operatorname{HomPairForm},
$$

$$
\operatorname{ProjClassForm},
$$

$$
\operatorname{ChartLegal},
$$

$$
\operatorname{AffineCoordinateForm},
$$

$$
\operatorname{AtlasRealizable}.
$$

## 73. XF-6 加強：關係內商化

來源差異是否被識別，必須相對於指定：

$$
\sim_{\rho}.
$$

射影縮放等價為：

$$
\sim_{\mathrm{projective}},
$$

不是普通商值等價的無型複製。

## 74. XF-8 加強：換圖與黏合守衛

再積分守衛必須檢查：

$$
\operatorname{OverlapDomain},
$$

$$
\operatorname{TransitionDefined},
$$

$$
\operatorname{InverseTransition},
$$

$$
\operatorname{CoverComplete}.
$$

## 75. 奇點公理修正

加入推論禁制：

$$
\operatorname{ChartFail}
\nRightarrow
\operatorname{ObjectFail},
$$

$$
\operatorname{ChartFail}
\nRightarrow
\operatorname{ObjectSingular}.
$$

若存在替代圖，應優先輸出：

$$
\operatorname{AlternativeChartFound}.
$$

---

# 第十八部　候選定理

## 76. X 射影保守實現定理

### 定理候選

令 $k$ 為域。若 X 射影分數系統採用：

1. 形成域：

$$
k^2\setminus\{(0,0)\};
$$

2. 關係型別：

$$
/_{\mathrm{projective}};
$$

3. 縮放等價：

$$
(a,b)\sim(\lambda a,\lambda b),
\qquad
\lambda\in k^\times;
$$

4. 雙圖冊 $U_0,U_1$ ；
5. 重疊換圖 $u\leftrightarrow u^{-1}$ ；
6. 忘卻來源軌跡的語義映射；

則：

$$
U(\operatorname{XProjLine}(k))
\cong
\mathbb P^1(k).
$$

## 77. 關係型別不可由方程唯一恢復命題

存在同一方程：

$$
ad-bc=0
$$

同時支援：

$$
\operatorname{QuotientEquality}
$$

與：

$$
\operatorname{ProjectiveEquality}.
$$

因此，僅由證明終式不能唯一恢復關係型別：

$$
\boxed{
\operatorname{Equation}
\nRightarrow
\operatorname{UniqueRelationType}.
}
$$

## 78. 圖表邊界非奇點命題

若對合法對象 $P$ ，存在圖表 $U_i,U_j$ 使：

$$
P\notin U_i,
$$

$$
P\in U_j,
$$

且 $U_j$ 在 $P$ 附近為正則局部模型，則：

$$
\operatorname{ChartFail}_{U_i}(P)
$$

不能單獨推出：

$$
\operatorname{ObjectSingular}(P).
$$

 $P_\infty=[1:0]$ 即為此命題的標準例。

## 79. 圖冊閉合命題

兩個局部模型不必共享單一座標，只要存在：

$$
U_{01}=U_0\cap U_1,
$$

以及可逆換圖：

$$
\tau_{01}:U_{01}\to U_{10},
$$

並滿足覆蓋與相容條件，即可形成合法全域整體。

因此：

$$
\boxed{
\operatorname{GlobalWhole}
\nRightarrow
\operatorname{GlobalSingleCoordinate}.
}
$$

---

# 第十九部　演算法化判定草案

## 80. 輸入

輸入：

$$
\mathcal I
=
(k,(a,b),\rho,\Gamma_{\mathrm{aff}}).
$$

## 81. 關係型別檢查

若：

$$
\rho=/_{\mathrm{quot}},
$$

使用普通商形成規則。

若：

$$
\rho=/_{\mathrm{projective}},
$$

使用射影形成規則。

禁止混用。

## 82. 射影形成檢查

檢查：

$$
(a,b)\neq(0,0).
$$

若失敗，輸出：

$$
\operatorname{ProjectiveFormationFailure}.
$$

## 83. 圖表支援

計算：

$$
\chi_0(P)
=
\begin{cases}
1,&a\neq0,\\
0,&a=0,
\end{cases}
$$

$$
\chi_1(P)
=
\begin{cases}
1,&b\neq0,\\
0,&b=0.
\end{cases}
$$

這裡的 $0,1$ 僅是布林狀態編碼，不是外部權重。

## 84. 正規化

若：

$$
\chi_0(P)=1,
$$

輸出：

$$
[1:b/a]
$$

及：

$$
\operatorname{NormCert}_0.
$$

若：

$$
\chi_1(P)=1,
$$

輸出：

$$
[a/b:1]
$$

及：

$$
\operatorname{NormCert}_1.
$$

## 85. 重疊與換圖

若：

$$
\chi_0(P)=\chi_1(P)=1,
$$

輸出：

$$
\operatorname{Overlap},
$$

$$
u=b/a,
$$

$$
v=a/b,
$$

$$
uv=1.
$$

否則不執行換圖。

## 86. 邊界分類

若：

$$
\chi_0(P)=1,
\qquad
\chi_1(P)=0,
$$

輸出：

$$
\operatorname{ChartBoundary}_{U_1},
$$

而不是：

$$
\operatorname{ObjectSingularity}.
$$

對稱情況亦同。

## 87. 建議輸出

$$
\operatorname{XProjReport}
=
\left(
\begin{array}{l}
\operatorname{RelationType},\\
\operatorname{HomogeneousFormation},\\
\operatorname{ProjectiveClass},\\
\operatorname{ChartSupport},\\
\operatorname{NormalizedRepresentatives},\\
\operatorname{TransitionCertificate},\\
\operatorname{BoundaryStatus},\\
\operatorname{ObjectSingularityStatus},\\
\operatorname{SourceTrace}
\end{array}
\right).
$$

---

# 第二十部　可反駁命題

## 88. 射影點不是普通商值

可反駁主張：

> 每個射影點都是域中的一個普通商值。

反例：

$$
[1:0]\in\mathbb P^1(k),
$$

但：

$$
\operatorname{Quot}_k(1,0)
\text{ 未定義}.
$$

## 89. 第二座標非零不是射影形成條件

可反駁主張：

$$
[a:b]\text{ 合法}
\Longleftrightarrow
b\neq0.
$$

反例：

$$
[1:0]
\text{ 合法}.
$$

正確條件為：

$$
(a,b)\neq(0,0).
$$

## 90. 單圖失敗不是對象奇點

可反駁主張：

$$
\neg\operatorname{ChartLegal}_{U_1}(P)
\Longrightarrow
\operatorname{ObjectSingular}(P).
$$

反例：

$$
P=[1:0].
$$

## 91. 方程相同不保證關係同型

可反駁主張：

> 只要兩種結構都用 $ad-bc=0$ 判等，它們就是同一種分數。

普通商與射影點提供反例。

## 92. 全域整體不保證單一座標

可反駁主張：

> 若一個幾何整體合法存在，就必有單一全域普通分數座標。

反例：

$$
\mathbb P^1
=
U_0\cup U_1
$$

需要兩張圖。

---

# 第二十一部　標準數學與 X 新增層

## 93. 標準射影幾何已知內容

下列皆屬標準數學：

- $\mathbb P^1(k)$ 的縮放商定義；
- 行列式相等判準；
- 兩張仿射圖；
- 重疊區 $\mathbb G_m$ ；
- 反演換圖；
- $[1:0]$ 作為選定仿射嵌入的補點；
- 射影直線的局部正則性。

本文不把它們宣稱為 X 理論的新定理。

## 94. X 層新增的組織工作

X 框架可能新增：

1. 關係型別證書；
2. 來源角色分派；
3. 齊次形成守衛；
4. 縮放等價證書；
5. 圖表支援證書；
6. 正規化來源軌跡；
7. 換圖守衛與證書；
8. 圖表邊界分類；
9. 圖冊黏合證書；
10. 忘卻後回到標準射影幾何的保守性。

## 95. 誠實的新穎性判定

本輪最重要的理論進展不是射影直線本身，而是逼迫 X 分數回答：

$$
\boxed{
\text{「分數」究竟是字形，還是帶型形成機制？}
}
$$

若 $/_{\mathrm{projective}}$ 只是一個標籤，而底層仍強迫第二來源充當全域分母，則 X 分數無法正確容納 $\mathbb P^1$ 。

若關係型別真正決定角色、形成、商化、圖表與失敗模式，則此例可以保守實現。

---

# 第二十二部　限制

## 96. 本輪只處理域上的射影直線

本文假設：

$$
k
\text{ 是域}.
$$

對一般交換環 $R$ ， $\mathbb P^1(R)$ 的點、局部自由秩一商、可生成對與函子觀點更加細緻，不能直接把域上的判準全部照搬。

## 97. 本輪未處理高維射影空間

對：

$$
\mathbb P^n(k),
$$

需要：

$$
n+1
$$

個齊次座標與：

$$
n+1
$$

張標準仿射圖。

其換圖、覆蓋與證書數量會顯著增加。

## 98. 本輪未處理射影簇奇點

 $\mathbb P^1$ 本身平滑。

若要真正測試幾何奇點，應改取：

$$
V(F)
\subseteq
\mathbb P^n
$$

並檢查局部環、Jacobian 或其他正則性判準。

本輪只證明「圖表邊界」不等於「幾何奇點」。

## 99. 本輪未賦予無窮遠額外算術

集合分解：

$$
\mathbb P^1(k)
=
k\sqcup\{\infty\}
$$

依賴仿射嵌入。

本文沒有宣稱：

$$
k\cup\{\infty\}
$$

仍是域，也沒有定義所有涉及 $\infty$ 的算術運算。

---

# 第二十三部　三輪實戰的總整合

## 100. 第一輪：代表與商類

第一輪得到：

$$
\boxed{
\neg\operatorname{RepLegal}(E)
\nRightarrow
\neg\operatorname{ClassLegal}([E]).
}
$$

## 101. 第二輪：來源與商類

第二輪得到：

$$
\boxed{
F\not\equiv_{\mathrm{src}}G
\quad\land\quad
[F]_S=[G]_S
}
$$

可以合法同時成立。

## 102. 第三輪：圖表與對象

本輪得到：

$$
\boxed{
\neg\operatorname{ChartLegal}_{U_i}(P)
\nRightarrow
\neg\operatorname{ObjectLegal}(P).
}
$$

以及：

$$
\boxed{
\neg\operatorname{ChartLegal}_{U_i}(P)
\nRightarrow
\operatorname{ObjectSingular}(P).
}
$$

## 103. 三個不可混同

三輪合併後，X 分數至少必須維持：

$$
\boxed{
\begin{aligned}
\text{表示} &\neq \text{商類},\\
\text{來源} &\neq \text{商類},\\
\text{圖表} &\neq \text{對象}.
\end{aligned}
}
$$

## 104. 六層最小架構

建議主論文 v0.2 至少採用：

1. 來源層；
2. 關係型別層；
3. 原始表示層；
4. 商類／對象層；
5. 目標圖表或語義實現層；
6. 軌跡與證書層。

必要時再加入：

7. 投影／數值層；
8. 圖冊／全域黏合層。

---

# 第二十四部　下一步

## 105. 現在應先改主論文

三輪有限形成測試已揭露足夠多的核心修正：

- 雙上下文與四層合法性；
- 一般局部化的 $S$ -湮滅；
- 來源保存強度；
- 合法強迫坍縮；
- 關係型別生成角色；
- 圖表邊界與對象奇點分離；
- 圖冊型動態整體。

因此，下一步不宜立刻進入遞歸分數。

應先完成：

$$
\boxed{
\text{《X 分數結構微積分 I》v0.2 核心改版}.
}
$$

## 106. 改版後的下一個實戰

完成 v0.2 後，再進入：

$$
\text{連分數與遞歸形成}.
$$

屆時可測試：

- 有限截斷；
- 遞歸來源軌跡；
- 不同展開路徑；
- 正規化與唯一性例外；
- 極限守衛；
- 動態整體閉合是否能跨越有限層。

---

# 第二十五部　結論

## 107. 射影分數不是普通除法

最基本的型別區分是：

$$
\boxed{
[a:b]_{/_{\mathrm{projective}}}
\not\equiv
\left(
\frac{a}{b}
\right)_{/_{\mathrm{quot}}}.
}
$$

射影點由非零齊次對形成；普通商由可逆分母形成。

## 108. 無窮遠點不是除零值

相對於：

$$
j_1(v)=[v:1],
$$

有：

$$
\infty_{j_1}=[1:0].
$$

它是射影補點，不是域中的：

$$
\operatorname{Quot}_k(1,0)
\text{ 未定義}.
$$

## 109. 無窮遠點不是幾何奇點

 $[1:0]$ 在 $U_0$ 中具有合法座標：

$$
u=0.
$$

因此：

$$
\boxed{
\text{單圖失敗}
\neq
\text{對象奇點}.
}
$$

## 110. X 分數通過的條件

X 分數只有在下列條件下通過本輪：

1. 關係型別真正生成形成規則；
2. 來源角色不被全域固定為分子—分母；
3. 縮放商化被接受；
4. 圖表與對象分層；
5. 換圖只在合法重疊上發生；
6. 整體可以由圖冊而非單一座標形成。

## 111. 最終判定

$$
\boxed{
\operatorname{PassWithGeometricCoreRevision}.
}
$$

本輪最精確的總結是：

$$
\boxed{
\text{公式可以相同，關係仍可不同；}
}
$$

$$
\boxed{
\text{座標可以失敗，對象仍可合法；}
}
$$

$$
\boxed{
\text{局部表示可以多個，全域整體仍可唯一形成。}
}
$$

---

# 附錄 A　核心公式表

## A.1 射影直線

$$
\mathbb P^1(k)
=
\left(
k^2\setminus\{(0,0)\}
\right)/k^\times.
$$

## A.2 縮放等價

$$
[a:b]
=
[\lambda a:\lambda b],
\qquad
\lambda\in k^\times.
$$

## A.3 行列式判準

$$
[a:b]=[c:d]
\Longleftrightarrow
ad-bc=0.
$$

## A.4 第一張圖

$$
U_0=\{[a:b]:a\neq0\},
$$

$$
u=b/a.
$$

## A.5 第二張圖

$$
U_1=\{[a:b]:b\neq0\},
$$

$$
v=a/b.
$$

## A.6 重疊換圖

$$
U_0\cap U_1
\cong
\mathbb G_m,
$$

$$
uv=1.
$$

## A.7 仿射嵌入與無窮遠

$$
j_1(v)
=
[v:1],
$$

$$
\infty_{j_1}
=
[1:0].
$$

## A.8 圖表邊界

$$
\operatorname{ChartFail}
\nRightarrow
\operatorname{ObjectSingular}.
$$

## A.9 圖冊黏合

$$
\mathbb P^1
\cong
\mathbb A^1_u
\cup_{\mathbb G_m}
\mathbb A^1_v.
$$

---

# 附錄 B　證書速查

## B.1 射影形成證書

$$
C_{\mathrm{form}}
=
\big(
(a,b)\neq(0,0),
\rho=/_{\mathrm{projective}}
\big).
$$

## B.2 縮放證書

$$
C_{\mathrm{scale}}
=
\big(
\lambda\in k^\times,
c=\lambda a,
d=\lambda b
\big).
$$

## B.3 圖表證書

$$
C_{\mathrm{chart},0}
=
\big(
a\neq0,
u=b/a
\big),
$$

$$
C_{\mathrm{chart},1}
=
\big(
b\neq0,
v=a/b
\big).
$$

## B.4 換圖證書

$$
C_{\mathrm{trans}}
=
\big(
a,b\neq0,
u=b/a,
v=a/b,
uv=1
\big).
$$

## B.5 邊界證書

$$
C_{\mathrm{boundary}}
=
\big(
\operatorname{ObjectLegal},
\operatorname{ChartFail}_{U_i},
\operatorname{AltChartLegal}_{U_j},
\neg\operatorname{ObjectSingular}
\big).
$$

## B.6 黏合證書

$$
C_{\mathrm{glue}}
=
\big(
U_0,U_1,U_{01},
\tau_{01},
\tau_{10},
\operatorname{CoverComplete}
\big).
$$

---

# 附錄 C　主論文 v0.2 最小移植清單

1. 將全域「分子／分母」改為關係依賴來源角色；
2. 讓 $\rho$ 決定形成域、角色、等價與結果型別；
3. 新增 $\operatorname{HomPairForm}$ ；
4. 新增 $\operatorname{ProjClassForm}$ ；
5. 新增 $\operatorname{ChartLegal}$ ；
6. 新增 $\operatorname{ChartTransitionCert}$ ；
7. 新增 $\operatorname{ChartBoundaryCert}$ ；
8. 加入「圖表失敗不推出對象奇點」；
9. 將動態整體閉合擴充為圖冊型閉合；
10. 將公式證書與關係型別證書綁定；
11. 保留縮放與正規化來源軌跡；
12. 明示無窮遠依賴仿射嵌入。

---

# 參考方向

本稿使用的標準數學背景包括：

1. 域上的射影直線；
2. 齊次座標與縮放等價；
3. 射影點的行列式判準；
4. 標準雙仿射圖；
5. 乘法群上的反演換圖；
6. 仿射嵌入與射影補全；
7. 射影直線的局部正則性。

後續正式版可對照代數幾何標準教材補入精確書目。
