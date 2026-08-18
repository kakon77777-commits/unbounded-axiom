# 三態不是第三個普通真值： $\Omega$ 作為生成中的判定
## 動態邏輯解與生成判斷系列・第三篇

**英文題名：** *The Third State Is Not Merely a Third Truth Value: Omega as Judgment-in-Generation*  
**版本：** v0.1  
**日期：** 2026-08-16  
**作者：** Neo.K（概念提出）／Aletheia（理論整理與形式化協作）

---

## 摘要

三值與多值邏輯已有成熟歷史。Łukasiewicz、Kleene、Priest、Belnap–Dunn 等傳統分別處理未定、真假皆有、真假皆無與非爆炸推理等問題。因此，如果僅僅把：

$$
\{\top,\bot\}
$$

擴充成：

$$
\{\top,\bot,\Omega\},
$$

並宣稱 $\Omega$ 是「第三個真值」，則本系列並沒有建立足夠的新結構。

本文因此明確區分兩個層級：

$$
\boxed{
\text{Truth Semantics}
\neq
\text{Judgment Runtime State}.
}
$$

命題的 truth-value domain 可以仍然是：

$$
\mathcal V=\{\top,\bot\},
$$

或採任何既有多值語義；而有限主體／AI／研究系統對命題的判斷 runtime 則可具有：

$$
\mathcal S_J
=
\{
\text{open},
\text{generating},
\text{conflicted},
\text{provisionally-true},
\text{provisionally-false}
\}.
$$

本文用符號 $\Omega$ 表示這些尚未穩定閉合狀態的一個低維投影：

$$
\boxed{
\Pi_{\Omega}(S_t)=\Omega.
}
$$

因此：

$$
\Omega
$$

不是「介於真與假中間的真值」，而首先表示：

> **當前判斷過程尚未滿足閉合條件。**

這一重新定義承接 2026 年 2 月舊《三態邏輯學》中「CRASH 可能不是失敗，而是過程」的核心洞見，但移除舊版本中不必要的超強形上學聲稱，使三態成為可與 belief revision、non-monotonic reasoning、probabilistic update、paraconsistent logic 及 executable runtime 對接的工程化判斷層。

---

# 一、為什麼不能直接說「第三真值」

經典二值語義：

$$
V(P)\in\{\top,\bot\}.
$$

多值邏輯則允許：

$$
V(P)\in\mathcal V,
\qquad
|\mathcal V|>2.
$$

例如，既有三值系統可以把第三值理解為：

- indeterminate；
- unknown；
- both true and false；
- neither true nor false；

不同系統具有不同 designated values 與 connective semantics。

因此本文不能把：

$$
\Omega
$$

簡單說成「我們發明的第三值」。

---

# 二、兩層語義

本文建立：

$$
\boxed{
V(P,W)
}
$$

與：

$$
\boxed{
J(P,t)
}
$$

兩層。

其中：

$$
V(P,W)
$$

描述命題在世界／模型中的語義地位；

$$
J(P,t)
$$

描述判斷系統在時間 $t$ 的 runtime state。

兩者可以同時存在。

例如，實際上：

$$
V(P,W)=\top,
$$

但因研究者尚未取得足夠證據：

$$
J(P,t)=\Omega.
$$

反之亦可能：

$$
V(P,W)=\bot,
$$

但有限主體暫時合理地閉合為：

$$
J(P,t)=\top_p.
$$

後者表示：

$$
\text{provisionally true},
$$

不是形上學上的真。

---

# 三、 $\Omega$ 的最小定義

定義判斷物件：

$$
\mathfrak J_t
=
(
P,
E_{\leq t},
\Gamma_t,
M_t,
S_t
).
$$

若在 closure policy：

$$
\theta
$$

下：

$$
\operatorname{CloseTrue}(\mathfrak J_t,\theta)=0
$$

且：

$$
\operatorname{CloseFalse}(\mathfrak J_t,\theta)=0,
$$

而 runtime 本身沒有失敗，則：

$$
\boxed{
J(P,t)=\Omega.
}
$$

因此：

$$
\Omega
=
\text{合法未閉合},
$$

而不是：

$$
\Omega
=
\mathrm{ERROR}.
$$

---

# 四、 $\Omega$ 與 ERROR 的型別隔離

這是工程上不可妥協的原則。

$$
\boxed{
\Omega\neq\mathrm{ERROR}.
}
$$

例如：

### 合法 $\Omega$

- 證據不足；
- 支持與反證接近；
- 關鍵來源尚未驗證；
- 假說正在分裂；
- 新模型尚未完成重算；
- 適用域仍不明。

### Runtime ERROR

- parser 崩潰；
- schema 錯誤；
- unresolved reference；
- cycle 無法處理；
- code execution exception；
- data corruption。

若把兩者混合，就會重犯舊 ADL 把「未穩定」與「系統崩潰」混成 CRASH 的問題。

---

# 五、 $\Omega$ 可以有內部子態

對外可以只顯示：

$$
\Omega.
$$

但內部最好保持：

$$
\Omega
=
\{
\Omega_{\mathrm{open}},
\Omega_{\mathrm{generating}},
\Omega_{\mathrm{conflict}},
\Omega_{\mathrm{blocked}}
\}.
$$

其中：

$$
\Omega_{\mathrm{blocked}}
$$

仍然是合法 epistemic block，而非 runtime error。

例如：

> 關鍵資料因權限問題暫時無法取得。

這與：

> evaluator 拋出例外。

完全不同。

---

# 六、狀態轉移

最小狀態圖：

$$
\Omega
\rightarrow
\top_p,
$$

$$
\Omega
\rightarrow
\bot_p,
$$

$$
\top_p
\rightarrow
\Omega,
$$

$$
\bot_p
\rightarrow
\Omega.
$$

因此：

$$
\boxed{
\top_p,\bot_p
}
$$

也是 runtime closure state，而非不可逆終局。

---

# 七、為什麼 $\Omega$ 有生成性

若 $\Omega$ 只是：

> 不知道。

它仍然太弱。

本文要求：

$$
\Omega_t
$$

可以主動生成下一個 epistemic action：

$$
A_{t+1}
=
G(\Omega_t).
$$

例如：

$$
G(\Omega_t)
\rightarrow
\{
\text{search source},
\text{run experiment},
\text{split hypothesis},
\text{request review},
\text{change model}
\}.
$$

因此：

$$
\boxed{
\Omega
=
\text{an actionable open state}.
}
$$

---

# 八、資訊增益與 $\Omega$

令不確定性：

$$
H_t
$$

表示某種 entropy / uncertainty measure。

新增證據後：

$$
\Delta H
=
H_{t+1}-H_t.
$$

一般研究可能希望：

$$
\Delta H<0.
$$

但生成判斷允許短期：

$$
\Delta H>0.
$$

因為新證據可能讓原本單一假說裂成：

$$
H
\rightarrow
\{H_1,H_2,H_3\}.
$$

因此：

> 發現自己不知道更多，不等於研究退步。

這正是生成性。

---

# 九、 $\Omega$ 與 Bayesian Credence

可同時存在：

$$
P_t(H)=0.63
$$

以及：

$$
J(H,t)=\Omega.
$$

原因是：

$$
0.63
$$

本身不回答：

- 是否達到閉合門檻；
- 來源是否獨立；
- 是否存在重大反證；
- 是否有不可接受的模型分歧；
- 是否已取得必要權限資料。

所以：

$$
\boxed{
\text{probability}
\neq
\text{judgment state}.
}
$$

---

# 十、 $\Omega$ 與 paraconsistency

若證據庫同時包含：

$$
E^+(P)
$$

與：

$$
E^-(P),
$$

不應因為：

$$
P
$$

與：

$$
\neg P
$$

都有支持，就推出萬物皆真。

因此 runtime 可以使用 paraconsistent evidence handling。

但：

$$
\boxed{
\Omega_{\mathrm{conflict}}
}
$$

不是直接等於 Priest 的 LP、Belnap 的 BOTH 或 Dunn semantics。

它是：

> **證據／判斷流程中的 conflict state。**

若需要，其底層證據邏輯可以採既有 paraconsistent formalism。

---

# 十一、與 Belnap 四值的區分

Belnap 類四值語義常區分：

$$
\{
T,F,B,N
\},
$$

例如真、假、兩者、皆非。

本系列可以將這類值作為 evidence semantics 的一部分。

但 judgment runtime 仍有另一軸：

$$
\text{runtime state}.
$$

例如：

$$
V_B(P)=B
$$

時，系統可能：

$$
J(P,t)=\Omega_{\mathrm{conflict}}.
$$

這是一個映射，而非同義。

---

# 十二、 $\Omega$ 與時間

若：

$$
J(P,t_0)=\Omega,
$$

則時間本身不保證：

$$
J(P,t_1)\neq\Omega.
$$

必須有事件：

$$
e:
S_t\rightarrow S_{t+1}.
$$

因此：

$$
\boxed{
\Omega
}
$$

不是「等久了自然會知道」。

它是一個需要 action policy 的狀態。

---

# 十三、永遠 $\Omega$ 是允許的

舊三態理論曾傾向要求：

$$
\Omega
\rightarrow
\{\top,\bot\}
$$

最終必解析。

本文把這一點降格。

可能存在：

$$
\forall t>t_0,
\quad
J(P,t)=\Omega.
$$

原因可能是：

- 證據原理上不可取得；
- 問題不可判定；
- 世界持續變化；
- 判定成本超出資源；
- 問題本身定義不足。

因此：

$$
\boxed{
\text{Dynamic}
\neq
\text{guaranteed finite convergence}.
}
$$

---

# 十四、停止與 $\Omega$

系統可以在：

$$
J(P,t)=\Omega
$$

時停止研究工作。

這不表示：

$$
P
$$

已被判真或判假。

可以有：

```text
research_status: stopped
judgment_state: generating
```

原因：

- 預算耗盡；
- 邊際資訊增益太低；
- 時限到達；
- 風險過高。

這是「停止運算」與「完成判定」的再次分離。

---

# 十五、科普渲染

對一般使用者：

```text
目前狀態：仍在生成
支持證據：6
反證：4
主要缺口：來源獨立性不足
下一步：查原始資料
```

這比顯示：

```text
UNKNOWN
```

更接近 $\Omega$ 的真正含義。

---

# 十六、與可不可論的接口

在 $\Omega$ 狀態中：

$$
\mathsf{Can}_t
$$

可以生成：

- 搜尋；
- 計算；
- 試驗；
- 詢問；
- 暫時閉合。

而：

$$
\mathsf{Cannot}_t
$$

限制：

- 不可假裝已知；
- 不可刪除反證；
- 不可把 ERROR 當成未知；
- 不可把未知當成神秘證明。

因此：

$$
\boxed{
\Omega
\rightarrow
\text{可不可的真正操作空間}.
}
$$

---

# 十七、本文核心命題

$$
\boxed{
\Omega
\text{ 是判斷過程狀態，而非必須被理解為第三個 truth value。}
}
$$

以及：

$$
\boxed{
\text{未閉合}
\neq
\text{失敗}
\neq
\text{錯誤}
\neq
\text{已證偽}.
}
$$

---

# 十八、結論

三態真正重要的不是「三」。

而是：

$$
\boxed{
\text{把正在形成的判斷，從真／假結果中分離出來。}
}
$$

這使下一篇可以處理更深的問題：

> 如果內容不斷變化，什麼東西仍然使一個判斷系統保持「同一個系統」？

答案將進入：

$$
\boxed{
\text{動態不動點}.
}
$$

---

# 參考文獻

1. Neo.K & Theia. 《三態邏輯學：從終極維到絕對維的永恆回歸》, 2026.
2. Marcos, J., Přenosil, A., & Egré, P. “Many-Valued Logic.” *Stanford Encyclopedia of Philosophy*, 2026.
3. Priest, G., Tanaka, K., & Weber, Z. “Paraconsistent Logic.” *Stanford Encyclopedia of Philosophy*, Summer 2026.
4. Belnap, N. D. “A Useful Four-Valued Logic.” In *Modern Uses of Multiple-Valued Logic*, 1977.
