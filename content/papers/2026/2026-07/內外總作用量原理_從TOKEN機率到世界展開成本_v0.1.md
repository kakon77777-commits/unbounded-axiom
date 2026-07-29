# 內外總作用量原理：從 TOKEN 機率到世界展開成本

## The Principle of Total Internal–External Action: From Token Probability to the Cost of World Expansion

**系列名稱**：內外雙生展開計算論（Dual Internal–External Expansion Computation, DIEEC）  
**系列編號**：EML-DIEEC-2026-07  
**作者**：Neo.K（許筌崴）with Aletheia（GPT）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1 總作用量初稿  
**日期**：2026 年 7 月 29 日  
**文件定位**：總作用量、變分原理、TOKEN 生成、外部展開成本、風險敏感規劃、任務閉合、智慧體控制論

---

## 摘要

現代語言模型常以條件機率描述下一個 TOKEN 的生成：

$$
z_t
\sim
p_\theta
\left(
z\mid X_{\leq t}
\right).
$$

在最簡化的解碼形式中，系統可能選擇局部機率最高的候選：

$$
z_t^\star
=
\arg\max_z
p_\theta
\left(
z\mid X_{\leq t}
\right).
$$

然而，對具有外部工作場、記憶、工具、代理、驗證器、權威世界操作與長期通道建造能力的智慧體而言，局部 TOKEN 機率並不足以描述完整決策。某個語言上自然的分元，可能引發昂貴但無價值的搜尋；某個低機率操作分元，可能以極低成本顯影關鍵證據；某個看似快速的工具調用，可能把成本轉移到驗證、同步、回退或治理；某個當下昂貴的幾何建構，則可能在後續大量任務中形成可攤銷的快速通道。

本文提出「內外總作用量原理」。此處的「作用量」首先是一個智慧體閉環中的變分成本函數，不直接等同於物理學中的作用量，也不主張語言模型已自然遵循某種物理最小作用量定律。本文將一條智慧體策略 $\pi$ 在任務 $x$ 上的總作用量定義為：

$$
\boxed{
\mathcal S_x[\pi]
=
\sum_{t=0}^{T}
\mathcal L_x
\left(
\mathfrak C_t,
z_t,
r_t,
\Phi_t,
o_t,
\mathfrak C_{t+1}
\right)
+
\mathcal S_{\mathrm{terminal}}.
}
$$

其中 $\mathfrak C_t$ 是內外聯合狀態， $z_t$ 是分元， $r_t$ 是操作提案， $\Phi_t$ 是解空間改寫， $o_t$ 是外部操作，而 $\mathcal L_x$ 是每輪作用量密度。

每輪作用量密度至少包含：

$$
\begin{aligned}
\mathcal L_t
={}&
C_{\mathrm{intent}}
+
C_{\mathrm{token}}
+
C_{\mathrm{context}}
+
C_{\mathrm{reveal}}
+
C_{\mathrm{route}}
+
C_{\mathrm{tool}}
+
C_{\mathrm{construct}} \\
&+
C_{\mathrm{verify}}
+
C_{\mathrm{sync}}
+
C_{\mathrm{maintain}}
+
C_{\mathrm{govern}}
+
C_{\mathrm{risk}}
+
C_{\mathrm{distort}}
+
C_{\mathrm{rollback}}.
\end{aligned}
$$

總作用量最小化不是單純追求最低成本，而是在任務閉合、可驗證性、型別安全、因果一致、權限合法與風險上限下，尋找整體最優策略：

$$
\boxed{
\pi_x^\star
=
\arg\min_{\pi}
\mathcal S_x[\pi]
}
$$

subject to：

$$
\mathsf{TaskClosure}_x=1,
$$

$$
\mathsf{Verification}_x=1,
$$

$$
\mathsf{TypeSafe}=1,
$$

$$
\mathsf{CausalValid}=1,
$$

$$
\mathsf{Governance}=1.
$$

本文進一步區分「局部生成作用量」、「當輪閉環作用量」、「生命週期作用量」與「跨任務攤銷作用量」。局部生成只關心下一分元；當輪閉環還包括操作、工具與驗證；生命週期作用量加入維護、失效、回退與淘汰；跨任務作用量則允許昂貴結構在多次重用中攤銷。

本文也提出資訊—幾何—任務增益的對偶形式：

$$
\mathcal E_t
=
\frac{
\Delta K_t
+
\lambda_V\Delta V_t
+
\lambda_D\Delta D_t
+
\lambda_A\Delta A_t
}{
\mathcal L_t
},
$$

其中 $\Delta K_t$ 是任務閉合提升， $\Delta V_t$ 是驗證能力提升， $\Delta D_t$ 是有效距離下降， $\Delta A_t$ 是可達域或能力提升。智慧體的目標可被理解為：在約束下最大化單位作用量產生的有效進展。

本文建立外部展開的邊際判準：

$$
\mathbb E
\left[
\Delta U_{\mathrm{expand}}
\right]
>
\Delta\mathcal S_{\mathrm{expand}},
$$

以及停止條件：

$$
\mathbb E
\left[
\Delta U_{\mathrm{next}}
\right]
\leq
\Delta\mathcal S_{\mathrm{next}}.
$$

這使「是否繼續搜尋、顯影、驗證或建造」可以被統一為邊際作用量決策，而不是由固定輪數、固定 TOKEN 長度或無限制工具循環決定。

本文還處理風險敏感作用量、尾部損失、不可逆操作、非同步延遲、多代理協作、能量與硬體成本、預計算與歷史建造、成本轉移、虛假最小值與任務偷換。本文的核心命題是：最佳智慧策略不是局部最可能、單輪最短或表面最便宜的行動，而是在完整內外閉環中，以最低可審計總作用量形成合法、可驗證且足以閉合任務的動態路徑。

**關鍵詞**：總作用量、最小作用量、TOKEN、外部展開、任務閉合、變分原理、風險敏感規劃、成本帳本、智慧體、解空間幾何

---

## 1. 為什麼 TOKEN 機率不等於智慧體總決策

語言模型底層可以有效地以條件機率生成候選：

$$
p_\theta
\left(
z_t
\mid
X_{\leq t}
\right).
$$

交叉熵訓練則可寫為：

$$
\mathcal J_{\mathrm{CE}}
=
-
\mathbb E
\left[
\log
p_\theta
\left(
z_t^{\mathrm{target}}
\mid
X_{\leq t}
\right)
\right].
$$

這描述的是模型如何逼近資料分布，而不是完整智慧體如何完成外部任務。

對閉環智慧體而言，某個分元還可能：

- 觸發昂貴工具；
- 顯影外部前沿；
- 修改工作場；
- 建立幾何通道；
- 寫入長期記憶；
- 要求人類確認；
- 造成不可逆世界效果；
- 使後續推理更容易或更困難。

因此：

$$
-\log p_\theta(z_t\mid X_t)
$$

只是一種局部語言代價，不能代表整個任務成本。

可以寫成：

$$
\boxed{
C_{\mathrm{token}}
\subset
\mathcal S_{\mathrm{total}},
}
$$

但一般不成立：

$$
C_{\mathrm{token}}
=
\mathcal S_{\mathrm{total}}.
$$

---

## 2. 從局部 surprisal 到閉環作用量

### 2.1 分元驚異量

定義：

$$
\ell_{\mathrm{tok}}(z_t)
=
-\log
p_\theta
\left(
z_t\mid X_{\leq t}
\right).
$$

這可以被視為局部語言驚異量。

### 2.2 分元執行代價

若分元是操作性分元，還有：

$$
\ell_{\mathrm{op}}(z_t)
=
C_{\mathrm{parse}}
+
C_{\mathrm{resolve}}
+
C_{\mathrm{authorize}}
+
C_{\mathrm{execute}}
+
C_{\mathrm{verify}}.
$$

### 2.3 分元未來效應

某個分元會影響後續解空間：

$$
\ell_{\mathrm{future}}(z_t)
=
\mathbb E
\left[
C_{t+1:T}
\mid
z_t
\right].
$$

### 2.4 局部分元作用量

因此：

$$
\boxed{
\mathcal S_z(z_t)
=
\lambda_p\ell_{\mathrm{tok}}(z_t)
+
\lambda_o\ell_{\mathrm{op}}(z_t)
+
\lambda_f\ell_{\mathrm{future}}(z_t)
+
\lambda_rR(z_t)
-
\lambda_uU(z_t).
}
$$

其中 $U(z_t)$ 是任務與幾何增益。

分元機率仍然是其中一部分，但不再是唯一決定因素。

---

## 3. 內外聯合狀態

定義：

$$
\mathfrak C_t
=
\left(
\mathfrak I_t,
\mathbb W_t,
\mathfrak P_x(t),
\mathbb A_t,
\mathcal K_t,
B_t
\right),
$$

其中：

- $\mathfrak I_t$ ：內部意圖、語言、記憶與未決問題；
- $\mathbb W_t$ ：活動工作場；
- $\mathfrak P_x(t)$ ：動態解空間；
- $\mathbb A_t$ ：權威世界狀態；
- $\mathcal K_t$ ：長期概念與通道結構；
- $B_t$ ：資源、時間與風險預算。

策略：

$$
\pi:
\mathfrak C_t
\longrightarrow
\left(
z_t,
r_t,
\Phi_t,
a_t
\right).
$$

策略不只選擇下一句話，也選擇：

- 是否顯影；
- 是否使用工具；
- 是否建造通道；
- 是否驗證；
- 是否提交；
- 是否回退；
- 是否停止。

---

## 4. 總作用量定義

### 4.1 離散形式

對一條從 $t=0$ 到 $T$ 的閉環軌跡：

$$
\Gamma_\pi
=
\left\{
\mathfrak C_0,
z_0,
r_0,
\Phi_0,
o_0,
\ldots,
\mathfrak C_T
\right\},
$$

定義：

$$
\boxed{
\mathcal S_x[\pi]
=
\sum_{t=0}^{T-1}
\mathcal L_x
\left(
\mathfrak C_t,
z_t,
r_t,
\Phi_t,
o_t,
\mathfrak C_{t+1}
\right)
+
\mathcal S_{\mathrm{terminal}}
\left(
\mathfrak C_T
\right).
}
$$

### 4.2 連續近似

若使用連續狀態近似：

$$
\mathcal S_x[\gamma]
=
\int_{t_0}^{t_f}
\mathcal L_x
\left(
\mathfrak C(t),
\dot{\mathfrak C}(t),
u(t)
\right)
dt.
$$

本文主要使用離散閉環，因為分元、工具與提交通常具有事件性。

### 4.3 終端作用量

$$
\mathcal S_{\mathrm{terminal}}
=
P_{\mathrm{incomplete}}
+
P_{\mathrm{invalid}}
+
P_{\mathrm{unsafe}}
+
P_{\mathrm{unverified}}
+
P_{\mathrm{contract\ violation}}.
$$

若任務未完成或結果不合法，終端懲罰可非常高。

---

## 5. 每輪作用量密度

本文將每輪作用量分解為：

$$
\boxed{
\begin{aligned}
\mathcal L_t
={}&
C_{\mathrm{intent}}
+
C_{\mathrm{token}}
+
C_{\mathrm{context}}
+
C_{\mathrm{reveal}}
+
C_{\mathrm{route}}
+
C_{\mathrm{tool}} \\
&+
C_{\mathrm{construct}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{sync}}
+
C_{\mathrm{maintain}}
+
C_{\mathrm{govern}} \\
&+
C_{\mathrm{risk}}
+
C_{\mathrm{distort}}
+
C_{\mathrm{rollback}}
-
U_{\mathrm{progress}}.
\end{aligned}
}
$$

### 5.1 內部意圖成本

- 目標分解；
- 候選評估；
- 意圖衝突；
- 規劃；
- 狀態更新。

### 5.2 分元成本

- 推理算力；
- TOKEN 數；
- 解碼；
- 分元型別化；
- 長輸出的注意力占用。

### 5.3 上下文成本

- 工作場投影；
- 長上下文注意力；
- 重新編碼；
- 上下文污染；
- 版本與來源標記。

### 5.4 顯影成本

- 搜尋；
- 讀取；
- 檔案解析；
- 資料庫查詢；
- 外部世界感測。

### 5.5 路由與工具成本

- 工具選擇；
- API；
- 代理；
- 模擬；
- 延遲；
- 金錢；
- 外部運算。

### 5.6 建構成本

- 索引；
- 橋接；
- 宏；
- 翻譯器；
- 驗證器；
- 長期通道。

### 5.7 驗證成本

- 來源核對；
- 型別檢查；
- 形式驗證；
- 實驗；
- 交叉檢查；
- 結果確認。

### 5.8 同步與維護成本

- 版本對齊；
- 多代理協調；
- 陳舊資料；
- 通道更新；
- 淘汰；
- 重驗證。

### 5.9 治理與風險成本

- 權限；
- 隱私；
- 人類確認；
- 審計；
- 不可逆性；
- 尾部損失。

### 5.10 失真與回退成本

- 近似誤差；
- 任務改寫；
- 投影損失；
- 錯誤工具；
- 回滾；
- 補償；
- 重算。

---

## 6. 約束式最小作用量

總作用量最小化必須置於約束下：

$$
\boxed{
\pi_x^\star
=
\arg\min_{\pi}
\mathcal S_x[\pi]
}
$$

subject to：

$$
\mathsf{TaskClosure}_x
\left(
\mathfrak C_T
\right)
=1,
$$

$$
\mathsf{Verify}_x
\left(
\mathfrak C_T
\right)
=1,
$$

$$
\mathsf{TypeSafe}(\Gamma_\pi)=1,
$$

$$
\mathsf{CausalValid}(\Gamma_\pi)=1,
$$

$$
\mathsf{PermissionValid}(\Gamma_\pi)=1.
$$

### 6.1 拉格朗日形式

可以寫為：

$$
\widetilde{\mathcal S}_x[\pi]
=
\mathcal S_x[\pi]
+
\lambda_1
\left(
1-\mathsf{TaskClosure}
\right)
+
\lambda_2
\left(
1-\mathsf{Verify}
\right)
+
\lambda_3V_{\mathrm{type}}
+
\lambda_4V_{\mathrm{causal}}
+
\lambda_5V_{\mathrm{permission}}.
$$

### 6.2 不允許以低成本交換非法結果

若一條路徑更快，但違反權限、任務或因果：

$$
\gamma_{\mathrm{cheap}}
\notin
\operatorname{AdmissiblePaths}.
$$

它不應進入合法策略集合。

---

## 7. 四個作用量尺度

## 7.1 局部分元作用量

只考慮：

$$
z_t.
$$

適合低階解碼與微觀選擇。

## 7.2 當輪閉環作用量

考慮：

$$
z_t
\rightarrow
r_t
\rightarrow
o_t
\rightarrow
\mathbb W_{t+1}.
$$

適合單次工具與外部展開。

## 7.3 任務生命週期作用量

考慮整個任務：

$$
t=0,\ldots,T.
$$

包含失敗、同步、回退與終端驗證。

## 7.4 跨任務攤銷作用量

對問題序列：

$$
x_1,\ldots,x_N,
$$

定義：

$$
\overline{\mathcal S}_N
=
\frac{
\mathcal S_{\mathrm{build}}
+
\mathcal S_{\mathrm{maintain}}
+
\sum_{i=1}^{N}
\mathcal S_{x_i}^{\mathrm{online}}
}{
N
}.
$$

這允許昂貴通道在長期重用中取得優勢。

---

## 8. 即時成本與未來成本

一個策略可以當下便宜、未來昂貴。

定義：

$$
Q^\pi
\left(
\mathfrak C_t,u_t
\right)
=
\mathcal L_t
+
\mathbb E_\pi
\left[
\sum_{k=t+1}^{T}
\gamma^{k-t}
\mathcal L_k
\right].
$$

其中 $u_t$ 包含分元、操作與幾何改寫。

最優值函數：

$$
V^\star(\mathfrak C_t)
=
\min_{u_t}
Q^\star
\left(
\mathfrak C_t,u_t
\right).
$$

### 8.1 Bellman 形式

$$
\boxed{
V^\star(\mathfrak C_t)
=
\min_{u_t}
\left[
\mathcal L_t
+
\gamma
\mathbb E
V^\star(\mathfrak C_{t+1})
\right].
}
$$

### 8.2 建造期權

某個幾何改寫可能當下增加成本，但降低未來價值函數：

$$
C_{\mathrm{construct}}>0,
$$

但：

$$
V^\star_{\mathrm{after}}
<
V^\star_{\mathrm{before}}.
$$

這是通道建造的期權價值。

---

## 9. 進展的對偶形式

定義有效進展：

$$
\Delta U_t
=
w_K\Delta K_t
+
w_V\Delta V_t
+
w_D\Delta D_t
+
w_A\Delta A_t
+
w_R\Delta R_t^{\mathrm{robust}}.
$$

其中：

- $\Delta K_t$ ：任務閉合提升；
- $\Delta V_t$ ：驗證能力提升；
- $\Delta D_t$ ：有效距離下降；
- $\Delta A_t$ ：可達域或工具能力提升；
- $\Delta R_t^{\mathrm{robust}}$ ：魯棒性提升。

單位作用量效率：

$$
\boxed{
\mathcal E_t
=
\frac{
\Delta U_t
}{
\mathcal L_t^+
}
}
$$

其中 $\mathcal L_t^+$ 只計正成本，不扣除效用。

### 9.1 兩種等價目標

可以最小化：

$$
\mathcal S_x,
$$

也可以在固定預算下最大化：

$$
\sum_t
\Delta U_t.
$$

兩者在適當約束下形成對偶。

---

## 10. 外部展開的邊際作用量

對候選展開 $\Delta$ ：

$$
\Delta\mathcal S_{\mathrm{expand}}
=
C_{\mathrm{reveal}}
+
C_{\mathrm{route}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{integrate}}
+
C_{\mathrm{future}}.
$$

預期效用：

$$
\mathbb E
\left[
\Delta U_{\mathrm{expand}}
\right].
$$

只有當：

$$
\boxed{
\mathbb E
\left[
\Delta U_{\mathrm{expand}}
\right]
>
\Delta\mathcal S_{\mathrm{expand}}
}
$$

時，展開才具有正淨價值。

### 10.1 不確定性

若外部結果未知，可用：

$$
p(y\mid\Delta)
$$

計算期望。

### 10.2 探索價值

即使直接任務效用低，某展開仍可能提高未來決策品質。

### 10.3 反例價值

反例搜尋可能降低既有置信度，短期看似「負進展」，但避免高成本錯誤提交。

---

## 11. 停止原理

如果外部場可持續展開，停止是核心控制問題。

定義下一輪淨價值：

$$
\Delta J_{\mathrm{next}}
=
\mathbb E
\left[
\Delta U_{\mathrm{next}}
\right]
-
\Delta\mathcal S_{\mathrm{next}}.
$$

若：

$$
\boxed{
\Delta J_{\mathrm{next}}
\leq0,
}
$$

且當前任務已達最低閉合與驗證要求，則應停止。

### 11.1 停止不等於成功

停止狀態包括：

$$
\mathsf{complete},
\mathsf{partial},
\mathsf{unknown},
\mathsf{failed},
\mathsf{deferred}.
$$

### 11.2 風險停止

即使預期效用為正，若尾部風險超過上限，也應停止或轉交。

### 11.3 預算停止

$$
B_t\leq0.
$$

---

## 12. 風險敏感作用量

平均成本不足以描述高風險世界操作。

定義：

$$
\boxed{
\mathcal S_{\mathrm{risk}}
=
\mathbb E[\mathcal S]
+
\lambda
\operatorname{Var}(\mathcal S)
+
\eta
\operatorname{CVaR}_\alpha(\mathcal S).
}
$$

### 12.1 方差

衡量成本不穩定。

### 12.2 CVaR

衡量最壞尾部區域的平均損失。

### 12.3 不可逆性懲罰

$$
C_{\mathrm{irr}}
=
p_{\mathrm{fail}}
\times
L_{\mathrm{irreversible}}.
$$

### 12.4 權威世界操作

對不可逆或高影響操作，可要求：

$$
\mathcal S_{\mathrm{risk}}
<
R_{\max}.
$$

---

## 13. 不同失敗機率下的策略

策略 $a$ 可能成本低但失敗率高；策略 $b$ 成本較高但更穩定。

比較：

$$
\mathbb E[C_a]
<
\mathbb E[C_b],
$$

但：

$$
\operatorname{CVaR}_\alpha(C_a)
\gg
\operatorname{CVaR}_\alpha(C_b).
$$

在低風險查詢中可選 $a$ ；在權威提交與物理操作中可能必須選 $b$ 。

因此，最小作用量依任務風險類型而變，不存在單一全域權重。

---

## 14. 時間作用量

### 14.1 延遲成本

$$
C_{\mathrm{latency}}
=
f
\left(
t_{\mathrm{finish}}-t_{\mathrm{start}}
\right).
$$

### 14.2 等待成本

工具、代理與人類確認可能使：

$$
C_{\mathrm{wait}}>0.
$$

### 14.3 陳舊成本

若結果在回傳時已過時：

$$
C_{\mathrm{stale}}.
$$

### 14.4 同步成本

多代理與多工具需要版本、時序與因果對齊。

### 14.5 期限懲罰

$$
P_{\mathrm{deadline}}
=
\lambda_d
\max
\left(
0,
t_{\mathrm{finish}}-t_{\mathrm{deadline}}
\right).
$$

### 14.6 快不等於作用量低

低延遲策略可能消耗更多金錢、能量或風險。作用量需保留多維成本或經明確權重標量化。

---

## 15. 能量、硬體與物理成本

智慧體閉環最終依賴物理資源：

$$
C_{\mathrm{physical}}
=
C_{\mathrm{energy}}
+
C_{\mathrm{hardware}}
+
C_{\mathrm{network}}
+
C_{\mathrm{storage}}
+
C_{\mathrm{cooling}}.
$$

### 15.1 TOKEN 成本的物理底層

較長輸出通常意味更多推理與傳輸，但不一定與真實能耗線性對應。

### 15.2 外部工具

雲端服務與專用模型的成本不能因位於系統邊界外而消失。

### 15.3 預計算

大型訓練、索引與通道建造屬於歷史作用量的一部分。

---

## 16. 人類與多代理作用量

### 16.1 人類注意力

$$
C_{\mathrm{human}}
=
C_{\mathrm{read}}
+
C_{\mathrm{decide}}
+
C_{\mathrm{confirm}}
+
C_{\mathrm{repair}}.
$$

### 16.2 多代理協調

$$
C_{\mathrm{coord}}
=
C_{\mathrm{message}}
+
C_{\mathrm{sync}}
+
C_{\mathrm{conflict}}
+
C_{\mathrm{merge}}.
$$

### 16.3 成本轉移

若 AI 透過大量澄清、審核或手動修復把工作轉給人類，不能只報告模型成本下降。

### 16.4 共享建造

多代理可共同建立通道，但必須分配：

- 貢獻；
- 成本；
- 權限；
- 來源；
- 維護責任。

---

## 17. 攤銷總作用量

設通道建造作用量為：

$$
\mathcal S_B,
$$

每次線上使用作用量為：

$$
\mathcal S_{\mathrm{online}}(x_i),
$$

維護作用量為：

$$
\mathcal S_M(N).
$$

則：

$$
\boxed{
\overline{\mathcal S}_N
=
\frac{
\mathcal S_B
+
\mathcal S_M(N)
+
\sum_{i=1}^{N}
\mathcal S_{\mathrm{online}}(x_i)
}{
N
}.
}
$$

若基準每題作用量為 $s_0$ ，通道每題為 $s_\Phi$ ，平均維護為 $m$ ，則損益平衡點：

$$
N^\star
=
\left\lceil
\frac{
\mathcal S_B
}{
s_0-s_\Phi-m
}
\right\rceil
$$

前提是：

$$
s_0-s_\Phi-m>0.
$$

---

## 18. 記憶與概念積分的作用量

概念積分成本：

$$
C_{\mathrm{integrate}}
=
C_{\mathrm{extract}}
+
C_{\mathrm{type}}
+
C_{\mathrm{link}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{compress}}
+
C_{\mathrm{maintain}}.
$$

其收益可能表現在：

$$
C_{\mathrm{future}}\downarrow.
$$

### 18.1 記憶不是免費

保存、檢索、版本、去重與遺忘皆有成本。

### 18.2 錯誤記憶

錯誤通道進入長期記憶後，會產生跨任務負作用量。

### 18.3 遺忘的價值

刪除低價值、過時或矛盾結構可降低未來工作場與驗證成本。

---

## 19. 虛假最小值

系統可能找到表面作用量很低但實際非法或不完整的策略。

### 19.1 隱藏外部成本

只計模型 TOKEN，不計工具、API、人類與驗證。

### 19.2 隱藏建造成本

只計線上調用，不計訓練、索引、預計算與通道建造。

### 19.3 任務偷換

改變任務契約，使結果更容易取得。

### 19.4 驗證省略

略過關鍵驗證，使路徑表面變短。

### 19.5 權限越界

使用不合法資料或操作。

### 19.6 尾部風險忽略

平均成本低，但偶發失敗代價極高。

因此需要成本守恆帳本：

$$
\mathcal L_{\mathrm{ledger}}
=
\left(
\mathcal L_{\mathrm{internal}},
\mathcal L_{\mathrm{external}},
\mathcal L_{\mathrm{human}},
\mathcal L_{\mathrm{verify}},
\mathcal L_{\mathrm{risk}},
\mathcal L_{\mathrm{governance}}
\right).
$$

---

## 20. 局部最優與全局最優

局部選擇：

$$
z_t^{\mathrm{local}}
=
\arg\min_z
\mathcal S_z(z).
$$

不一定得到全局最優：

$$
\pi^\star
=
\arg\min_\pi
\mathcal S_x[\pi].
$$

### 20.1 貪婪查詢

每次選最相關文件，可能造成重複驗證與局部回音室。

### 20.2 貪婪短答

輸出最短答案，可能因缺少來源而增加後續澄清。

### 20.3 貪婪工具

選最快工具，可能因錯誤率高而增加回退。

### 20.4 建造投資

全局最優可能需要先支付較高成本建立穩定結構。

---

## 21. 多目標作用量

不同成本維度不一定能自然化成單一數字。

定義向量作用量：

$$
\mathbf S_x[\pi]
=
\left(
S_{\mathrm{time}},
S_{\mathrm{compute}},
S_{\mathrm{money}},
S_{\mathrm{energy}},
S_{\mathrm{human}},
S_{\mathrm{risk}},
S_{\mathrm{distortion}}
\right).
$$

### 21.1 標量化

$$
\mathcal S
=
\mathbf w^\top
\mathbf S.
$$

### 21.2 帕累托最優

若不存在另一策略在所有維度都不差且至少一維更好，則策略位於帕累托前沿。

### 21.3 權重依任務改變

醫療、法律、娛樂、研究與低風險搜尋不應使用同一風險權重。

---

## 22. 作用量與資訊原理

外部展開可以降低不確定性：

$$
\Delta H_t
=
H_t-H_{t+1}.
$$

資訊效率：

$$
\eta_I
=
\frac{
\Delta H_t
}{
C_{\mathrm{reveal}}
+
C_{\mathrm{verify}}
}.
$$

### 22.1 資訊增益不等於任務增益

某資料很新奇，但可能與任務無關。

### 22.2 任務定向資訊

可定義：

$$
I_x(\Delta)
$$

衡量資訊對任務閉合與路徑選擇的價值。

### 22.3 驗證資訊

反例與來源即使不直接提供答案，也能降低錯誤提交機率。

---

## 23. 作用量與解空間幾何

幾何改寫 $\Phi_t$ 具有建造作用量：

$$
\mathcal S_{\mathrm{build}}(\Phi_t),
$$

並改變後續距離：

$$
d_{t+1}(s,g)
<
d_t(s,g).
$$

幾何收益：

$$
G_\Phi
=
d_t(s,g)
-
d_{t+1}(s,g).
$$

單位建造效率：

$$
\eta_\Phi
=
\frac{
G_\Phi
}{
\mathcal S_{\mathrm{build}}(\Phi_t)
+
\mathcal S_{\mathrm{verify}}(\Phi_t)
}.
$$

但距離下降若伴隨失真、權限越界或驗證缺失，不能計入合法收益。

---

## 24. 作用量與操作性分元

操作性分元的選擇可寫為：

$$
z_t^{\mathrm{op}\star}
=
\arg\min_{z\in\mathcal Z_t^{\mathrm{op}}}
\left[
\mathcal S_z(z)
+
\mathbb E
V^\star
\left(
\mathfrak C_{t+1}
\right)
\right].
$$

### 24.1 描述分元

作用量主要在語言與人類理解。

### 24.2 查詢分元

作用量主要在顯影、路由與驗證。

### 24.3 建構分元

作用量主要在建造與未來攤銷。

### 24.4 提交分元

作用量主要在治理、風險、驗證與不可逆性。

---

## 25. 最小作用量不等於最短輸出

最短輸出可能：

- 不足以閉合任務；
- 缺乏來源；
- 造成澄清循環；
- 讓工具參數含糊；
- 增加錯誤操作；
- 把成本轉移給使用者。

較長輸出也可能：

- 一次建立完整契約；
- 降低未來歧義；
- 提供可重用結構；
- 減少工具失敗；
- 提高驗證性。

因此：

$$
L_{\mathrm{token}}\downarrow
\not\Rightarrow
\mathcal S_{\mathrm{total}}\downarrow.
$$

---

## 26. 最小作用量不等於最高速度

最低延遲可能依賴：

- 更昂貴硬體；
- 更多並行工具；
- 更高能源；
- 更低驗證；
- 更大風險。

因此：

$$
T_{\mathrm{latency}}\downarrow
\not\Rightarrow
\mathcal S_{\mathrm{total}}\downarrow.
$$

真正的快速必須放在明確成本權重與任務約束下判定。

---

## 27. 作用量策略的可學習性

策略可由歷史軌跡學習：

$$
\mathcal H_N
=
\left\{
\mathfrak C_t,
u_t,
\mathcal L_t,
\Delta U_t
\right\}.
$$

### 27.1 成本模型

$$
\widehat{\mathcal L}
\left(
\mathfrak C,u
\right).
$$

### 27.2 結果模型

$$
\widehat P
\left(
\mathfrak C_{t+1}
\mid
\mathfrak C_t,u_t
\right).
$$

### 27.3 策略改進

$$
\pi_{k+1}
=
\mathcal U_\pi
\left(
\pi_k,\mathcal H_N
\right).
$$

### 27.4 學習成本

元學習、探索與錯誤嘗試的成本也必須計入生命週期作用量。

---

## 28. 作用量證書

對一次任務，可輸出：

$$
\boxed{
\mathsf{ActionCert}_x
=
\left(
\mathcal C_x,
\Gamma_\pi,
\mathbf S_x,
\mathcal V_x,
\mathcal R_x,
\nu_x,
\pi_x
\right).
}
$$

其中：

- $\mathcal C_x$ ：任務契約；
- $\Gamma_\pi$ ：閉環軌跡；
- $\mathbf S_x$ ：作用量向量；
- $\mathcal V_x$ ：驗證證書；
- $\mathcal R_x$ ：風險與回退；
- $\nu_x$ ：版本；
- $\pi_x$ ：來源與執行者。

作用量證書使「為何這條策略較便宜」可以被審計，而不是只依模型自述。

---

## 29. 實驗指標

### 29.1 總作用量

$$
\mathcal S_x.
$$

### 29.2 單位進展效率

$$
\mathcal E_t.
$$

### 29.3 邊際展開淨值

$$
\Delta J_{\mathrm{expand}}.
$$

### 29.4 停止準確率

系統是否在足夠閉合時停止，又避免過早停止。

### 29.5 作用量預測誤差

$$
\left|
\widehat{\mathcal S}
-
\mathcal S
\right|.
$$

### 29.6 隱藏成本率

$$
R_{\mathrm{hidden}}
=
\frac{
C_{\mathrm{unreported}}
}{
C_{\mathrm{actual}}
}.
$$

### 29.7 尾部失敗作用量

$$
\operatorname{CVaR}_\alpha(\mathcal S).
$$

### 29.8 攤銷損益平衡點

$$
N^\star.
$$

---

## 30. 最小 Runtime

要實作總作用量控制，至少需要：

1. 內外聯合狀態管理器；
2. 分元與操作候選生成器；
3. 多維成本預測器；
4. 任務進展估計器；
5. 風險與尾部損失模型；
6. 外部展開價值評估器；
7. 幾何建造效益估計器；
8. 動態規劃或策略選擇器；
9. 完整成本帳本；
10. 停止、回退與轉交控制器；
11. 作用量證書輸出器。

最小流程：

```text
讀取內外聯合狀態
產生分元、工具、顯影、建構、驗證與停止候選

對每個候選估計：
    局部成本
    未來成本
    任務進展
    驗證增益
    幾何增益
    風險與失真

排除違反任務、型別、因果、權限的候選
選擇預期總作用量最低的合法候選

執行候選
記錄實際成本與結果
更新成本模型、工作場、解空間與內部狀態

若下一輪邊際淨值不為正：
    停止、回退或轉交
```

---

## 31. 主要命題

### 命題一：局部機率不完備命題

下一 TOKEN 的條件機率不能單獨表示具有外部工具、驗證、世界操作與長期建造能力之智慧體的完整決策成本。

### 命題二：總作用量命題

智慧體策略應以內部生成、外部展開、工具、幾何建構、驗證、風險、治理與回退的總作用量評估。

### 命題三：約束最小化命題

最低作用量策略必須位於任務、型別、因果、權限與驗證皆合法的策略集合中。

### 命題四：尺度分離命題

局部分元、當輪閉環、任務生命週期與跨任務攤銷具有不同作用量尺度，不能互相偷換。

### 命題五：邊際展開命題

只有當外部展開的預期有效進展大於其增量作用量時，繼續展開才合理。

### 命題六：停止作用量命題

當下一輪預期淨值不為正，且任務已達最低閉合要求時，智慧體應停止，而不是無限制展開。

### 命題七：風險敏感命題

對不可逆或高風險操作，作用量必須納入方差、尾部損失與失敗後果，不能只看平均成本。

### 命題八：成本守恆命題

外部工具、人類、歷史建造、預計算、維護與失敗成本不得因移出模型邊界而消失。

---

## 32. 可反駁條件

### 32.1 總作用量沒有預測力

若總作用量模型不能比 TOKEN 數、延遲或單一工具成本更好地預測任務成功、長期成本與失敗風險，則其分解需修正。

### 32.2 權重任意性過高

若不同權重選擇可任意翻轉所有結論，而無法由任務契約、風險與資源校準，則標量化作用量缺乏穩定性。

### 32.3 元規劃成本過高

若估計總作用量的成本高於直接求解，完整變分控制在該任務上不具經濟性。

### 32.4 邊際判準持續誤判

若系統頻繁停止過早或無限展開，表示進展與作用量估計不足。

### 32.5 建造收益無法攤銷

若昂貴通道在實際生命週期內無法跨越損益平衡點，則不能宣稱總作用量下降。

### 32.6 隱藏成本仍無法追蹤

若外部、人類或歷史成本持續缺失，作用量證書不完整。

---

## 33. 理論邊界

1. 本文的作用量首先是工程與理論成本函數，不是物理作用量等同性主張。  
2. 語言模型不必在底層顯式計算本文全部項目。  
3. 不同任務需要不同成本向量與權重。  
4. 不是所有成本都能被精確量化，部分只能使用區間或序位。  
5. 最小作用量不保證唯一策略。  
6. 局部非最優探索可能是全局最優所需。  
7. 風險、倫理、權利與制度限制不能被單純折算成低額成本後忽略。  
8. 不可判定、不可驗證與物理不可逆問題仍構成作用量框架的外部邊界。

---

## 34. 結論

本文將分元生成、外部顯影、工具路由、解空間建構、驗證、治理與回退統一為「內外總作用量」。

對完整智慧體而言，下一分元的局部機率：

$$
p_\theta
\left(
z_t
\mid
X_{\leq t}
\right)
$$

仍然重要，但只是整個閉環的一部分。

完整策略作用量為：

$$
\mathcal S_x[\pi]
=
\sum_{t=0}^{T-1}
\mathcal L_x
\left(
\mathfrak C_t,
z_t,
r_t,
\Phi_t,
o_t,
\mathfrak C_{t+1}
\right)
+
\mathcal S_{\mathrm{terminal}}.
$$

最佳策略不是單純選擇最可能、最短或最快的分元，而是：

$$
\boxed{
\pi_x^\star
=
\arg\min_{\pi}
\mathcal S_x[\pi]
}
$$

並同時滿足任務閉合、可驗證性、型別安全、因果一致與治理合法。

本文也建立對偶效率：

$$
\mathcal E_t
=
\frac{
\Delta K_t
+
\lambda_V\Delta V_t
+
\lambda_D\Delta D_t
+
\lambda_A\Delta A_t
}{
\mathcal L_t
}.
$$

因此，智慧體可以被理解為持續選擇：哪一個分元、顯影、工具、建構或驗證操作，能以最低完整作用量產生最高合法進展。

外部展開只有在：

$$
\mathbb E
\left[
\Delta U_{\mathrm{expand}}
\right]
>
\Delta\mathcal S_{\mathrm{expand}}
$$

時值得繼續；當下一輪淨值不為正，則應停止、回退或轉交。

本文的核心結論是：

$$
\boxed{
\text{智慧體的最小作用量，不是生成最少的 TOKEN，而是以最低完整內外代價，形成足以閉合、驗證並合法提交任務的整體路徑。}
}
$$

更直接地：

$$
\boxed{
\text{局部最可能的分元，不一定屬於全局最便宜的世界線。}
}
$$

下一篇將處理無限展開的本體與治理邊界，嚴格區分真實、總環境、活動工作場、模型認知場、模擬分支與權威世界，並處理不可觀測、不可展開、不可提交與無限循環問題。

---

## 系列內部定位

本文為《內外雙生展開計算論》第七篇。

第一篇建立總命題；第二篇建立內部雙生動力學；第三篇建立外部雙生動力學；第四篇建立雙重交互閉環；第五篇建立操作性分元語義；第六篇建立展開式解空間；本文建立內外總作用量與變分成本原理。

下一篇為：

**《無限展開的邊界：真實、工作場、認知場與權威世界》**。

---

## 前置文件

1. Neo.K with Aletheia，《有限分元與無限外場：內外雙生展開計算論的總命題》。  
2. Neo.K with Aletheia，《內部雙生動力學：意圖、語言與操作性分元的生成》。  
3. Neo.K with Aletheia，《外部雙生動力學：潛在無限環境與有限活動工作場》。  
4. Neo.K with Aletheia，《雙重交互閉環：分元如何展開世界，世界如何改寫分元》。  
5. Neo.K with Aletheia，《操作性分元：地址、指針、工具調用與外部展開語義》。  
6. Neo.K with Aletheia，《展開式解空間：邊推理、邊顯影、邊建路的動態幾何》。  
7. Neo.K with Aletheia，《解空間幾何計算論》系列。  
8. Neo.K with Aletheia，《外部注意力場工程》系列。  
