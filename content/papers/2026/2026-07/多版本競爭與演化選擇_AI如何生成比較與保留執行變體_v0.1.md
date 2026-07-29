# 多版本競爭與演化選擇：AI 如何生成、比較與保留執行變體

## Multi-Version Competition and Evolutionary Selection: How AI Generates, Compares, and Retains Executable Variants

**系列名稱**：AI 自適應封裝與遞歸演化計算論（AI-Adaptive Encapsulation and Recursive Evolutionary Computation, AEREC）  
**系列編號**：EML-AEREC-2026-06  
**作者**：Neo.K（許筌崴）with Aletheia（GPT）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1 多版本競爭與選擇框架初稿  
**日期**：2026 年 7 月 29 日  
**文件定位**：多版本演化、候選族群、Pareto 選擇、環境適應度、版本保種、專用化與通用化

---

## 摘要

AI 自適應封裝不應被理解為每一代只生成一個新版本，再以單一效能指標決定是否替換舊版本。真實應用同時面對多種硬體、資料分布、工作負載、能源限制、延遲要求、安全級別、網路條件與治理政策。某一版本可能在低延遲環境中最優，卻在能源、記憶、可維護性或安全性上顯著劣化；另一版本可能在平均情況下普通，卻在故障、離線、分布外輸入或低資源環境中更穩健。若演化引擎只保留單一「冠軍版本」，系統容易因 benchmark 過度擬合、環境漂移、硬體改變或共同失敗模式而失去韌性。

本文提出「多版本競爭與演化選擇」框架。第 $n$ 代演化族群表示為：

$$
\mathcal P_n
=
\left\{
P_{n,1},P_{n,2},\ldots,P_{n,k}
\right\}.
$$

每個版本不只是一份程式碼，而是一組跨層基因型：

$$
g(P_{n,i})
=
\left(
g_{\mathrm{repr}},
g_{\mathrm{alg}},
g_{\mathrm{data}},
g_{\mathrm{IR}},
g_{\mathrm{compiler}},
g_{\mathrm{runtime}},
g_{\mathrm{package}},
g_{\mathrm{hardware}},
g_{\mathrm{governance}}
\right),
$$

並在環境 $E$ 中形成可觀測表現型：

$$
\phi(P_{n,i},E)
=
\left(
\text{行為},
\text{成本},
\text{風險},
\text{可靠性},
\text{證據強度}
\right).
$$

版本適應度不由單一速度決定，而由功能契約、環境條件、多目標成本、剩餘風險、驗證強度與多樣性價值共同構成：

$$
\mathcal F(P\mid E)
=
\mathcal F_{\mathrm{contract}}
+
\mathcal F_{\mathrm{performance}}
+
\mathcal F_{\mathrm{robustness}}
+
\mathcal F_{\mathrm{evidence}}
+
\mathcal F_{\mathrm{diversity}}
-
\mathcal F_{\mathrm{risk}}.
$$

本文區分「淘汰」、「停用」、「隔離」、「保種」與「歸檔」。未被選為當前正式版本，不代表該版本毫無價值。某些版本應作為低資源備援、異質硬體版本、災難恢復版本、反事實基準、歷史錨點或多樣性保種而被保留。本文因此提出版本生態，而不是單線版本鏈。

本文進一步提出環境條件化 Pareto 前沿：

$$
\mathcal P^\star(E)
=
\operatorname{Pareto}
\left(
\mathcal P_n\mid E
\right),
$$

以及動態版本選擇器：

$$
P_t^\star
=
\arg\min_{P\in\mathcal P^\star(E_t)}
J_{\mathbf w_t}(P),
$$

其中 $E_t$ 是當前環境， $\mathbf w_t$ 是當前成本權重。若環境辨識不確定，系統應保守退回通用穩定版，而不是強行選擇高度專用版本。

本文也處理候選生成與遺傳式組合。AI 可以將已證實有效的局部改寫重組為新版本，但局部有效不保證組合有效。版本交叉、模組合併與多層改寫必須經過介面、效果、時序、資源與治理驗證。本文提出版本譜系、改寫來源圖、貢獻歸因、近親退化與共享漏洞風險。

本文最後主張，多版本競爭的目標不是創造永遠贏過所有版本的單一終極程式，而是維持一個能在環境變動、風險出現與新硬體到來時，快速切換、重新組合與繼續演化的合法版本族群。

**關鍵詞**：多版本競爭、演化選擇、版本族群、Pareto 前沿、適應度、變體多樣性、版本保種、AI 自適應封裝、專用化

---

## 1. 問題的提出：為什麼不能只保留最快版本

假設候選版本有：

$$
P_a,
P_b,
P_c.
$$

其中：

- $P_a$ 平均延遲最低；
- $P_b$ 能源最低；
- $P_c$ 在故障與分布外輸入下最穩定。

若只以平均延遲排序：

$$
P_a
=
\arg\min_P J_L(P),
$$

系統會淘汰 $P_b$ 與 $P_c$ 。

但若部署環境從雲端切換到邊緣設備，或正式資料分布改變，原本的冠軍版本可能立即退化。

因此：

$$
\boxed{
\text{某一環境中的最優版本，不等於所有未來環境中的最優版本。}
}
$$

多版本競爭要解決的不是「誰永遠最好」，而是：

- 哪些版本在什麼環境下更好；
- 哪些版本應正式啟用；
- 哪些版本應作為備援；
- 哪些版本應被隔離；
- 哪些版本雖不部署，仍值得保留。

---

## 2. 版本族群

第 $n$ 代版本族群定義為：

$$
\boxed{
\mathcal P_n
=
\left\{
P_{n,1},
P_{n,2},
\ldots,
P_{n,k}
\right\}.
}
$$

每個版本均共享：

- 身分根；
- 基礎功能契約；
- 權威程式本體來源；
- 演化歷史；
- 治理框架。

但可具有不同：

- 演算法；
- 資料結構；
- 編譯策略；
- 硬體映射；
- 封裝方式；
- 適用域；
- 成本向量；
- 附加契約。

### 2.1 版本狀態

$$
s(P)
\in
\left\{
\mathsf{candidate},
\mathsf{verified},
\mathsf{active},
\mathsf{standby},
\mathsf{preserved},
\mathsf{deprecated},
\mathsf{quarantined},
\mathsf{archived}
\right\}.
$$

### 2.2 族群不是版本垃圾場

不是所有歷史版本都應進入活動族群。活動族群只保留仍具有部署、備援、比較、組合或知識價值的版本。

---

## 3. 版本基因型與表現型

### 3.1 基因型

版本的跨層結構可表示為：

$$
g(P)
=
\left(
g_{\mathrm{task}},
g_{\mathrm{repr}},
g_{\mathrm{alg}},
g_{\mathrm{data}},
g_{\mathrm{IR}},
g_{\mathrm{compiler}},
g_{\mathrm{runtime}},
g_{\mathrm{package}},
g_{\mathrm{hardware}},
g_{\mathrm{interface}},
g_{\mathrm{governance}}
\right).
$$

它描述版本「如何被實現」。

### 3.2 表現型

版本在環境 $E$ 下的實際表現為：

$$
\phi(P,E)
=
\left(
Y,
\mathbf J,
R,
A,
Z
\right),
$$

其中：

- $Y$ ：可觀測行為；
- $\mathbf J$ ：成本向量；
- $R$ ：風險；
- $A$ ：可用性與穩健性；
- $Z$ ：證書與證據強度。

### 3.3 基因型不直接決定表現型

同一版本在不同環境中：

$$
\phi(P,E_1)
\neq
\phi(P,E_2).
$$

所以版本不能脫離環境被宣稱為絕對快速或絕對穩健。

---

## 4. 環境空間

令環境為：

$$
E
=
\left(
H,
O,
W,
D,
N,
C,
R,
T
\right),
$$

其中：

- $H$ ：硬體；
- $O$ ：作業系統與執行時；
- $W$ ：工作負載；
- $D$ ：資料分布；
- $N$ ：網路與外部依賴；
- $C$ ：成本權重；
- $R$ ：風險與權限；
- $T$ ：期限與時序要求。

### 4.1 環境分區

環境可以被分為：

$$
\mathcal E
=
\left\{
E_1,E_2,\ldots,E_m
\right\}.
$$

每個區域對應一組近似穩定的執行條件。

### 4.2 環境漂移

$$
E_{t+1}
\neq
E_t.
$$

漂移可能來自：

- 輸入變化；
- 新硬體；
- 併發改變；
- 網路狀態；
- 能源政策；
- 安全事件；
- 法規；
- 模型或依賴更新。

---

## 5. 適應度不是單一分數

版本適應度可定義為：

$$
\mathcal F(P\mid E)
=
\mathcal F_C
+
\mathcal F_P
+
\mathcal F_R
+
\mathcal F_Z
+
\mathcal F_D
-
\mathcal F_X.
$$

其中：

- $\mathcal F_C$ ：契約符合度；
- $\mathcal F_P$ ：效能與成本；
- $\mathcal F_R$ ：穩健性與恢復能力；
- $\mathcal F_Z$ ：證據強度；
- $\mathcal F_D$ ：多樣性與備援價值；
- $\mathcal F_X$ ：風險、維護與遷移負擔。

但不應把所有維度強制壓縮成單一永久分數。更穩健的方式是保存向量：

$$
\mathbf F(P\mid E).
$$

---

## 6. 契約先於競爭

版本必須先通過功能契約門：

$$
P
\equiv_{\mathcal C}
P^\ast.
$$

不符合契約的候選，不應因為更快而進入競爭。

所以合法競爭集合為：

$$
\mathcal P_n^{\mathrm{legal}}
=
\left\{
P\in\mathcal P_n
\mid
P\equiv_{\mathcal C}P^\ast
\right\}.
$$

競爭發生在合法版本之間，而不是以效能交換功能身分。

---

## 7. 環境條件化 Pareto 前沿

對環境 $E$ ：

$$
\mathcal P^\star(E)
=
\operatorname{Pareto}
\left(
\mathcal P_n^{\mathrm{legal}}\mid E
\right).
$$

若版本 $P_a$ 在所有主要成本維度都不差於 $P_b$ ，且至少一項更好，則：

$$
P_a
\prec_E
P_b.
$$

被支配版本可以退出活動前沿，但仍可能因：

- 不同環境；
- 不同證書；
- 不同失敗模式；
- 備援價值；

而被保留。

---

## 8. 多環境前沿

單一環境前沿不足以支撐長期系統。

可定義跨環境前沿：

$$
\mathcal P^\star_{\mathcal E}
=
\bigcup_{E\in\mathcal E}
\mathcal P^\star(E).
$$

某版本可能只在一個小環境區域中最優，但若該區域具有高價值或高風險，仍值得保存。

### 8.1 環境覆蓋率

版本族群覆蓋率可定義為：

$$
\operatorname{Coverage}
\left(
\mathcal P_n,\mathcal E
\right)
=
\frac{
\mu
\left(
\bigcup_{P\in\mathcal P_n}
\operatorname{Domain}(P)
\right)
}{
\mu(\mathcal E)
}.
$$

---

## 9. 正式版本、備援版本與保種版本

### 9.1 正式版本

當前被環境選擇器啟用的版本。

### 9.2 備援版本

在正式版本失敗、環境不確定或證書失效時切換。

### 9.3 保種版本

不一定部署，但保留其：

- 不同演算法族；
- 不同硬體路徑；
- 不同依賴；
- 不同失敗模式；
- 不同歷史證據。

保種的目的不是懷舊，而是維持演化多樣性。

### 9.4 歷史錨點

保留早期穩定版本，用於：

- 錨點驗證；
- 契約漂移檢查；
- 長期比較；
- 災難恢復。

---

## 10. 多樣性的工程價值

若所有版本都源自同一演算法、同一編譯器、同一依賴與同一硬體，它們可能共享同一漏洞。

定義版本距離：

$$
d(P_i,P_j)
=
w_gd_g
+
w_ad_a
+
w_dd_d
+
w_hd_h
+
w_xd_x.
$$

其中可包含：

- 基因型距離；
- 演算法距離；
- 資料表示距離；
- 硬體距離；
- 外部依賴距離。

族群多樣性為：

$$
\mathcal D(\mathcal P)
=
\frac{
2
}{
k(k-1)
}
\sum_{i<j}
d(P_i,P_j).
$$

### 10.1 多樣性不是越大越好

過度多樣會增加：

- 驗證；
- 維護；
- 部署；
- 知識；
- 遷移；

成本。

所以需要最小有效多樣性，而非無限制增加變體。

---

## 11. 共同失敗模式

兩個版本即使程式碼不同，也可能依賴：

- 同一第三方庫；
- 同一模型；
- 同一資料源；
- 同一編譯器；
- 同一協議；
- 同一硬體；
- 同一權限策略。

可建立共同依賴圖：

$$
G_{\mathrm{common}}
=
\left(
V,E
\right).
$$

若多個版本共享高風險節點，表面多樣性不等於真實韌性。

### 11.1 失敗相關性

$$
\rho_{ij}^{\mathrm{fail}}
=
\operatorname{Corr}
\left(
F_i,F_j
\right).
$$

備援版本應盡量降低失敗相關性。

---

## 12. 候選生成策略

新一代候選可由：

$$
\widetilde{\mathcal P}_{n+1}
=
\mathcal M
\left(
\mathcal P_n,
K_n,
F_n,
E_n,
B_n
\right)
$$

生成。

其中 $\mathcal M$ 可包括：

- 變異；
- 重組；
- 特化；
- 簡化；
- 反向恢復；
- 外部新技術導入。

---

## 13. 變異

變異是對單一版本進行局部或跨層修改：

$$
P'
=
\mu(P).
$$

### 13.1 局部變異

- 編譯參數；
- 批次；
- 快取；
- 模組邊界；
- 記憶布局。

### 13.2 結構變異

- 演算法替換；
- IR 重組；
- 服務拆合；
- 硬體遷移。

### 13.3 風險感知變異

高風險區域限制改寫距離：

$$
d(P,P')
\leq
\delta_R.
$$

---

## 14. 重組

若版本 $P_a$ 與 $P_b$ 分別具有優勢模組，可嘗試：

$$
P_c
=
\operatorname{Recombine}
\left(
P_a,P_b
\right).
$$

但局部優勢不保證組合後仍成立：

$$
\operatorname{Good}(m_a)
\land
\operatorname{Good}(m_b)
\nRightarrow
\operatorname{Good}(m_a\oplus m_b).
$$

原因包括：

- 介面不相容；
- 效果衝突；
- 資源競爭；
- 時序改變；
- 快取互相干擾；
- 證書不可組合。

所以重組後必須重新驗證完整候選。

---

## 15. 特化與反特化

### 15.1 特化

針對特定環境：

$$
P_E
=
\operatorname{Specialize}
\left(
P,E
\right).
$$

### 15.2 反特化

當專用版本過多時，可將共同結構抽取回通用版本：

$$
P_{\mathrm{general}}
=
\operatorname{Generalize}
\left(
P_{E_1},\ldots,P_{E_k}
\right).
$$

AEREC 不只生成專用版本，也應能壓縮版本族。

---

## 16. 譜系與來源圖

每個版本應保存父版本與改寫來源：

$$
\operatorname{Parents}(P_i)
=
\left\{
P_a,P_b,\ldots
\right\}.
$$

版本譜系圖為：

$$
G_{\mathrm{lineage}}
=
\left(
V_L,E_L
\right).
$$

### 16.1 譜系價值

可用於：

- 追溯有效改寫；
- 判斷共同失敗；
- 證書重用；
- 版本歸因；
- 回滾；
- 防止重複生成。

### 16.2 譜系不能代替驗證

父版本合法，不代表子版本合法。

---

## 17. 改寫貢獻歸因

若版本 $P_c$ 組合多個改寫：

$$
\Phi
=
\left\{
\phi_1,\ldots,\phi_m
\right\},
$$

需要估計每個改寫的貢獻。

### 17.1 消融歸因

比較：

$$
P_c
$$

與：

$$
P_c\setminus\phi_i.
$$

### 17.2 Shapley 型歸因

可近似計算改寫在不同組合中的邊際貢獻。

### 17.3 因果限制

若改寫高度交互，不能把總收益簡單平均分配。

---

## 18. 競爭機制

### 18.1 淘汰賽

逐輪比較，快速縮小候選。

優點：成本低。  
缺點：早期噪音可能淘汰好版本。

### 18.2 聯賽制

所有候選在多環境、多工作負載中比較。

優點：完整。  
缺點：成本高。

### 18.3 分層競爭

先做低成本靜態與小型基準，再讓少數候選進入完整測試。

### 18.4 在線競爭

透過小流量 A/B 或 bandit 分配真實負載。

高風險系統不應直接以正式使用者作為無限制實驗場。

---

## 19. 環境選擇器

當前合法版本集合為：

$$
\mathcal P_n(E_t)
=
\left\{
P\in\mathcal P_n
\mid
\chi_P(E_t)=1
\right\}.
$$

選擇器輸出：

$$
P_t^\star
=
\mathcal S
\left(
E_t,
\mathcal P_n,
\mathbf w_t,
R_t
\right).
$$

### 19.1 選擇器需要證書

只有在：

$$
\operatorname{ValidCert}
\left(
P,E_t
\right)=1
$$

時才可被選擇。

### 19.2 不確定環境

若：

$$
\operatorname{Uncertainty}(E_t)
>
u_{\max},
$$

應選擇：

$$
P_{\mathrm{general\ safe}}.
$$

### 19.3 切換成本

版本切換需要考慮：

- 狀態遷移；
- 快取暖機；
- 模型載入；
- 連線重建；
- 使用者中斷；
- 回滾。

---

## 20. 版本切換與遲滯

若新版本優勢為：

$$
G_{\mathrm{new}},
$$

切換成本為：

$$
C_{\mathrm{switch}},
$$

則只有：

$$
G_{\mathrm{new}}
>
C_{\mathrm{switch}}
+
\delta
$$

才切換。

其中 $\delta$ 是遲滯門檻，用於防止震盪。

---

## 21. 在線學習與版本選擇

可將版本視為多臂 bandit：

$$
\mathcal A
=
\left\{
P_1,\ldots,P_k
\right\}.
$$

每次選擇後獲得報酬：

$$
r_t
=
-
J(P_i,E_t).
$$

但軟體版本選擇與一般 bandit 不同，因為：

- 失敗可能不可逆；
- 狀態會被改變；
- 版本切換有成本；
- 使用者不能成為無限試驗對象；
- 安全與契約是硬約束。

所以需要受約束 bandit，而非純粹最大化平均報酬。

---

## 22. 保種策略

可定義保留價值：

$$
V_{\mathrm{preserve}}(P)
=
V_{\mathrm{coverage}}
+
V_{\mathrm{diversity}}
+
V_{\mathrm{fallback}}
+
V_{\mathrm{knowledge}}
-
C_{\mathrm{maintain}}.
$$

若：

$$
V_{\mathrm{preserve}}(P)>0,
$$

即使版本不是當前 Pareto 冠軍，也可以保留。

### 22.1 最小保種集

尋找：

$$
\mathcal P_{\min}
\subseteq
\mathcal P_n
$$

使其仍覆蓋主要環境、失敗模式與演算法族。

---

## 23. 版本淘汰

淘汰條件可能包括：

- 被所有合法版本支配；
- 契約失效；
- 證書不可更新；
- 依賴終止；
- 安全風險；
- 維護成本過高；
- 適用域已消失；
- 功能被更通用版本完整覆蓋。

### 23.1 淘汰不等於刪除

被淘汰版本仍可進入歸檔，用於歷史、研究與回滾證據。

---

## 24. 版本隔離

若版本具有：

- 未確認漏洞；
- 不可重現行為；
- 契約漂移；
- 供應鏈問題；
- 證書失效；

則進入：

$$
\mathsf{quarantined}.
$$

隔離版本不能被選擇器部署，但仍保留調查價值。

---

## 25. 近親退化與模式鎖定

若候選都由單一父版本的小幅變異產生，族群可能逐步失去多樣性：

$$
\mathcal D(\mathcal P_n)\downarrow.
$$

這會造成：

- 共同漏洞；
- 相同局部最優；
- 對環境漂移敏感；
- 缺乏替代演算法。

### 25.1 多源注入

定期引入：

- 新演算法；
- 新編譯器；
- 新硬體後端；
- 人類設計；
- 外部研究；
- 從早期分支重新演化。

---

## 26. 性能單一化風險

若選擇壓力只看速度：

$$
\mathcal F(P)
=
-J_T(P),
$$

族群會犧牲：

- 記憶；
- 能源；
- 可維護性；
- 安全；
- 可重現；
- 回滾；
- 依賴自主性。

因此，多版本競爭必須明確保留非速度價值。

---

## 27. 版本生態債務

版本越多，成本越高。

定義：

$$
D_{\mathrm{population}}
=
C_{\mathrm{build}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{store}}
+
C_{\mathrm{deploy}}
+
C_{\mathrm{observe}}
+
C_{\mathrm{migrate}}
+
C_{\mathrm{govern}}.
$$

族群擴張只有在邊際價值高於邊際債務時合理：

$$
\Delta V_{\mathrm{population}}
>
\Delta D_{\mathrm{population}}.
$$

---

## 28. 族群壓縮

若多個版本共享大量結構，可進行：

- 公共模組抽取；
- 參數化；
- 多版本單一二進位；
- 動態裝置路由；
- 共用證書；
- 共用依賴；
- 分層快取。

族群壓縮不是消除所有差異，而是降低重複成本。

---

## 29. 版本族與演化膠囊

演化膠囊中的：

$$
\mathcal V_n
$$

不只是輸出檔案清單，而是一個具有：

- 適用域；
- 譜系；
- 適應度；
- 證書；
- 狀態；
- 切換規則；
- 保種價值；

的版本生態。

可表示為：

$$
\mathfrak V_n
=
\left(
\mathcal P_n,
G_{\mathrm{lineage}},
G_{\mathrm{dependency}},
\mathcal F,
\mathcal S,
\mathcal Z,
\mathcal G
\right).
$$

---

## 30. 多版本與解空間幾何

不同版本可以被理解為不同的幾何通道固化結果：

$$
P_i
=
\operatorname{Materialize}
\left(
\Phi_i
\left(
\mathfrak P
\right)
\right).
$$

某版本使用折疊與壓縮；另一版本使用投影與硬體特化；第三版本保留較長路徑但提供更高可驗證性。

因此，版本族就是一組不同幾何路徑的工程化實現。

---

## 31. 多版本與內外雙生展開

外部環境變化會改變版本適應度：

$$
E_t
\longrightarrow
\mathcal F(P\mid E_t).
$$

版本執行結果又提供新觀測：

$$
P_t^\star
\longrightarrow
D_{t+1}.
$$

由此，版本選擇與外部環境形成持續閉環。

---

## 32. 主要理論命題

### 命題一：族群優於單線命題

多環境應用不應預設只有一個永久最佳版本。

### 命題二：環境相對適應度命題

版本優劣必須相對於硬體、負載、分布、風險與成本權重判斷。

### 命題三：多目標前沿命題

多版本競爭應保存環境條件化 Pareto 前沿，而非只保留單一速度冠軍。

### 命題四：變體非分叉命題

共享身分根與基礎契約的多個實現可以構成同一應用的合法版本族。

### 命題五：多樣性韌性命題

演算法、硬體、依賴與封裝多樣性可以降低共同失敗風險，但也產生治理成本。

### 命題六：保種命題

非當前最佳版本仍可能因備援、覆蓋、知識與歷史錨點價值而被保留。

### 命題七：選擇器保守命題

環境辨識不確定或證書失效時，應退回通用安全版本。

### 命題八：族群壓縮命題

版本族必須持續進行合併、抽象與淘汰，否則演化多樣性會轉化為版本債務。

---

## 33. 可反駁條件

### 33.1 多版本沒有韌性增益

若多版本相較單一版本不能提高覆蓋、恢復與環境適應，族群成本缺乏正當性。

### 33.2 選擇器長期誤選

若環境選擇器頻繁選擇劣勢版本，動態選擇可能不如固定通用版。

### 33.3 多樣性只是表面

若版本共享相同依賴與失敗模式，多樣性指標可能失真。

### 33.4 族群成本爆炸

若建置、驗證與維護成本隨版本數快速增加，必須縮小族群。

### 33.5 重組成功率低

若版本重組大多破壞契約或無法產生協同，遺傳式組合價值有限。

### 33.6 專用版本迅速過時

若環境漂移速度高於版本生成與驗證速度，特化策略可能無法攤銷。

### 33.7 保種無法恢復

若保留版本的依賴、硬體與證書已不可重建，保種只是名義保存。

---

## 34. 理論邊界

本文不主張：

- 版本越多越好；
- 生物演化比喻可以直接取代軟體驗證；
- 適應度等同單一分數；
- Pareto 前沿上的所有版本都應正式部署；
- 多樣性可以取代安全證明；
- 父版本合法就保證子版本合法；
- 在線競爭可以繞過使用者權益與治理；
- 被淘汰版本應永久刪除；
- 版本保種可以不計維護成本。

本文主張的是：

$$
\boxed{
\text{多版本不是為了累積更多程式，而是為了保留在不同環境、目標與風險下仍然合法有效的多條實現路徑。}
}
$$

---

## 35. 初步版本族資料模型

```json
{
  "population_id": "population:gen-18",
  "identity_root": "app:root-01",
  "contract": "contract:v3",
  "variants": [
    {
      "id": "variant:general-18",
      "status": "active",
      "parents": ["variant:general-17"],
      "profile": ["general", "cpu"],
      "fitness": {
        "latency": 0.71,
        "energy": 0.62,
        "robustness": 0.91,
        "evidence": 0.96
      },
      "certificates": ["cert:eq-182", "cert:sec-44"]
    },
    {
      "id": "variant:gpu-18",
      "status": "standby",
      "parents": ["variant:gpu-17", "variant:general-17"],
      "profile": ["high-throughput", "gpu"],
      "fitness": {
        "latency": 0.94,
        "energy": 0.68,
        "robustness": 0.74,
        "evidence": 0.89
      },
      "fallback": "variant:general-18"
    }
  ]
}
```

---

## 36. 結論

本文將 AI 自適應封裝中的版本管理，由單線更新提升為多版本演化生態。

第 $n$ 代版本族為：

$$
\mathcal P_n
=
\left\{
P_{n,1},
P_{n,2},
\ldots,
P_{n,k}
\right\}.
$$

每個版本具有跨層基因型：

$$
g(P),
$$

並在特定環境中形成表現型：

$$
\phi(P,E).
$$

版本競爭不以單一速度決定，而由契約、成本、穩健性、證據、風險、多樣性與備援價值共同構成。

對每個環境，系統保存：

$$
\mathcal P^\star(E)
=
\operatorname{Pareto}
\left(
\mathcal P_n\mid E
\right).
$$

選擇器則在證書與治理約束下動態選擇：

$$
P_t^\star
=
\arg\min_{P\in\mathcal P^\star(E_t)}
J_{\mathbf w_t}(P).
$$

但多版本不是無限累積。系統必須同時具備：

- 生成；
- 變異；
- 重組；
- 特化；
- 反特化；
- 比較；
- 保種；
- 淘汰；
- 隔離；
- 壓縮。

本文的核心結論是：

$$
\boxed{
\text{AI 遞歸演化的成熟形態，不是每一代只留下一個冠軍，而是維持一個能跨環境競爭、互相備援、保留多樣性並持續重組的合法版本族群。}
}
$$

真正的目標不是創造一個永遠超越所有版本的終極執行檔，而是建立：

$$
\boxed{
\text{面對環境改變時，仍能迅速選擇、恢復與繼續演化的軟體生態。}
}
$$

---

## 系列內部定位

本文為《AI 自適應封裝與遞歸演化計算論》第六篇。

前五篇分別建立總命題、應用身分、演化膠囊、全層最佳化空間與遞歸改良動力學；本文建立多版本族群、環境適應度、競爭、保種、淘汰與選擇框架。

下一篇為：

**《功能不變如何被證明：等價證書、差分驗證與安全回滾》**。

---

## 前置文件

1. Neo.K with Aletheia，《程式完成之後：AI 自適應封裝與遞歸演化計算論的總命題》。  
2. Neo.K with Aletheia，《同一個應用是什麼：功能契約、觀測等價與程式身分》。  
3. Neo.K with Aletheia，《從 EXE 與 DLL 到演化膠囊：自適應封裝的新本體》。  
4. Neo.K with Aletheia，《全層最佳化空間：從演算法、資料結構到封裝與硬體》。  
5. Neo.K with Aletheia，《無限遞歸改良動力學：觀測、診斷、生成、驗證與提交》。  
6. Neo.K with Aletheia，《解空間幾何計算論》系列。
