# 內家拳的數學架構：因果邏輯與公式骨架

> 三篇論文（主論文五層剛體框架 / 軟體動力學補完 / 通用運動引擎）的壓縮提取。只保留因果鏈與數學形式，剔除數值範例、數據表、案例、商業與訓練敘述。

---

## 0. 本構基礎

人體建模為 $n$ 個剛體經關節連接：$B_i \in \mathbb{R}^3 \times SO(3)$，廣義座標 $q \in \mathbb{R}^m$，狀態 $x = [q,\dot q]^T$。

**正向運動學**與**雅可比**：

$$p = f_{FK}(q), \qquad \dot p = J(q)\dot q$$

**拉格朗日動力學標準形式**（後續所有層的物理底座）：

$$M(q)\ddot q + C(q,\dot q)\dot q + G(q) = \tau + J^T F_{ext}$$

因果地位：物理層是本體論基礎。沒有穩定結構則無法施力，沒有高效傳導則力無法輸出，沒有人體幾何則無法設計策略 → Level 1–4 全部以此為前提。

---

## Level 0 — 物理基礎層

### 0.1 開鏈 / 閉鏈與「整」

常態人體為開鏈，末端剛度低、易被外力擾動。當兩個以上末端同時接觸固定物體時形成閉鏈，引入約束 $g(q)=0$。

等效剛度（末端受力位移響應 $F = K_{eq}\,\Delta x$）：

$$K_{eq,\text{open}} = (J M^{-1} J^T)^{-1}, \qquad K_{eq,\text{closed}} \gg K_{eq,\text{open}}$$

**因果**：閉鏈減少自由度 → 剛度躍升 → 外力被整個幾何結構共同承擔而非集中單一關節。「整勁」＝把身體調整為閉鏈機構。

### 0.2 動態穩定性與 ZMP

靜態條件僅要求質心投影落在支撐多邊形內：

$$P(t) = \text{ConvexHull}\{p_1,\dots,p_k\}, \qquad c_{proj}(t) \in P(t)$$

加速運動時慣性力產生額外力矩，靜態條件失效。定義零力矩點：

$$\sum_{i=1}^{n}\big[(p_i - p_{ZMP})\times(m_i g + m_i \ddot p_i)\big] = 0$$

平地顯式解：

$$x_{ZMP} = \frac{\sum m_i(\ddot z_i + g)x_i - \sum m_i \ddot x_i z_i}{\sum m_i(\ddot z_i + g)}$$

**動態穩定定理**：系統在 $t$ 動態穩定 $\iff p_{ZMP}(t) \in P(t)$。

退化關係：當 $\ddot c = 0$ 時 $p_{ZMP} \approx c_{proj}$，動態條件回到靜態條件。

### 0.3 結構奇異點（弱點的精確定義）

$$U(x) = d(p_{ZMP},\partial P) = \min_{q \in \partial P}\|p_{ZMP} - q\|$$

$U \to 0$ 即臨界失穩態。「化勁」＝施力把對方 $p_{ZMP}$ 推向 $\partial P$ 使 $U \to 0$；一旦 $U < U_{crit}$ 立即切換發勁。

### 0.4 力鏈傳導效率

$$\eta = \frac{\|F_{output}\|}{\|F_{ground}\|}, \qquad \eta = \prod_{i} \eta_i, \quad \eta_i = 1-\gamma_i$$

耗散機制為粘彈性（Kelvin–Voigt）：

$$F_{joint} = k\,\Delta x + c\,\dot x, \qquad P_{loss} = c\|\dot x\|^2$$

**關鍵因果**：粘性耗散 $\propto$ 速度平方 → 高速戰鬥必然高耗散，這是核心矛盾。

- **鬆**：最小化粘性耗散，$\;\text{鬆} \iff \min \sum_i c_i$
- **整**：最小化傳導路徑損耗，化為圖上最短路徑問題

$$\min_{\text{path}} \sum_{e \in \text{path}} w_e, \qquad w_e = 1-\eta_e$$

方向損耗與力—骨夾角耦合：$\gamma_i = \gamma_0(1 - |\hat f \cdot \hat b_i|)$；當 $\hat f \parallel \hat b_i$ 時 $\gamma_i = 0$（完美傳導）。

---

## Level 1 — 資訊處理層

### 1.1 狀態與觀測

對手狀態 $x = [q,\dot q,c,p_{ZMP},F_{contact}]^T$，為部分可觀測。觀測模型：

$$z_{vision} = h_{vision}(x) + v_{vision}, \qquad z_{touch} = h_{touch}(x) + v_{touch}$$

協方差的距離依賴（決定模態優劣的根源）：

$$R_{vision}(d) = \begin{cases} \sigma_0^2 I + \alpha d^2 I & d > d_0 \\ \infty\cdot I & d < d_0 \;(\text{焦距失效}) \end{cases} \qquad R_{touch}(d) = \sigma_1^2 I\, e^{-\beta d}$$

### 1.2 模態切換定理

$$d_{crit} = \arg\min_d\big[\,\mathrm{tr}(R_{vision}(d)) - \mathrm{tr}(R_{touch}(d))\,\big]$$

$$\text{Primary Sensor} = \begin{cases} \text{Vision} & d > d_{crit} \\ \text{Touch} & d \le d_{crit} \end{cases}$$

**因果**：估計不確定性 $\propto \mathrm{tr}(R)$ → 選使其最小者。貼身時視覺焦距失效、觸覺延遲低且不隨距離退化 → 「聽勁」＝在 $d < d_{crit}$ 切換到觸覺模態的狀態估計。

### 1.3 主動感知（問勁）

$$u_{probe}^* = \arg\max_u I(x;z\mid u)$$

$$I(x;z) = H(x) - H(x\mid z) = \tfrac12 \log\frac{\det P_{prior}}{\det P_{post}}$$

最大化資訊 $\iff$ 最小化 $\det P_{post}$。最優探測方向沿最大不確定性方向，即協方差最大特徵向量：

$$P\,v_{max} = \lambda_{max} v_{max}, \qquad \hat u_{opt} = v_{max}$$

### 1.4 貝氏估計（聽勁的實作 = EKF）

遞迴濾波：

$$\text{預測：}\; p(x_t\mid z_{1:t-1}) = \int p(x_t\mid x_{t-1})\,p(x_{t-1}\mid z_{1:t-1})\,dx_{t-1}$$

$$\text{更新：}\; p(x_t\mid z_{1:t}) = \frac{p(z_t\mid x_t)\,p(x_t\mid z_{1:t-1})}{\int p(z_t\mid x_t)\,p(x_t\mid z_{1:t-1})\,dx_t}$$

非線性系統線性化 $F = \partial f/\partial x|_{\hat x}$、$H = \partial h/\partial x|_{\hat x}$，EKF：

$$\dot{\hat x} = f(\hat x,u), \qquad \dot P = FP + PF^T + Q$$

$$K = PH^T(HPH^T + R)^{-1}, \quad \hat x \leftarrow \hat x + K(z - h(\hat x)), \quad P \leftarrow (I-KH)P$$

神經對應：小腦前向模型＝預測步；預測誤差 $e = z_{actual} - z_{predicted}$ 即更新步殘差 $z - h(\hat x)$。

---

## Level 2 — 控制層

### 2.1 李雅普諾夫穩定性

$V(x) > 0\;(x\neq0)$、$V(0)=0$、$\dot V = \nabla V \cdot f \le 0$（穩定）；$\dot V < 0$（漸進穩定）。

人體平衡的李雅普諾夫函數：

$$V(x) = \underbrace{\tfrac12 m\|\dot c\|^2 + mgz_c}_{\text{機械能}} + \underbrace{\kappa\, d^2(p_{ZMP},\,c_P^*)}_{\text{結構偏差}}$$

### 2.2 化勁的雙重穩定性

我方與對方為耦合系統，$F_{opp\to self} = -F_{self\to opp}$。控制目標：

$$\boxed{\;\nabla V_{self}\cdot f_{self}(x_{self},u_{self}) \le 0 \quad\text{(自穩)}\;}$$
$$\boxed{\;\nabla V_{opp}\cdot f_{opp}(x_{opp},F_{self\to opp}) \ge \epsilon > 0 \quad\text{(破敵)}\;}$$

即 $\dot V_{self} \le 0$ 而 $\dot V_{opp} \ge \epsilon$。硬抗使雙方同耗能；化勁＝順勢退讓 $u_s = \alpha\dot\theta_o$ 使對方無阻力而 $\dot V_{opp}$ 加速。

### 2.3 最優控制

$$J = \int_{t_0}^{t_f}\!\big[\,\|u\|^2 + \lambda_1 V_{self}(x_{self}) - \lambda_2\, U(x_{opp})\,\big]\,dt$$

硬約束 $p_{ZMP,self} \in P_{self}$。哈密頓量與龐特里亞金原理：

$$H = L(x,u) + \lambda^T f(x,u), \qquad \dot\lambda = -\nabla_x H, \qquad u^* = \arg\min_u H$$

解得最優控制律：

$$u^* = -\tfrac12\Big(\lambda_s^T \tfrac{\partial f_{self}}{\partial u} + \lambda_o^T \tfrac{\partial f_{opp}}{\partial u}\Big)^{\!T}$$

實時近似採模型預測控制（receding horizon）：每步解有限時域問題，僅執行 $u^*(t)$ 後重解。

### 2.4 混合自動機（剛柔切換）

$$\mathcal{H} = (Q, X, U, F, G, R), \qquad Q = \{\text{SOFT},\,\text{HARD}\}$$

- SOFT（化勁）：$\min\|u\|^2$、$\max I(x_{opp};z)$、$\max(-U_{opp})$
- HARD（發勁）：$\max\;\alpha(t)\eta F_{ground}$，須於 $\Delta t_{strike}$ 內完成

**守衛條件** SOFT $\to$ HARD：

$$G = 1 \iff U(x_{opp}) < U_{crit} \;\wedge\; x_{opp} \in I_\tau \;\wedge\; U(x_{self}) > U_{safe}$$

HARD $\to$ SOFT：$t - t_{switch} > \Delta t_{strike}$ 或 $U(x_{opp}) > U_{recover}$。

**混合系統穩定性定理**：若存在共同李雅普諾夫函數使 $\nabla V \cdot F(q,x,u) < 0$ 對所有模式成立，則任意切換序列下漸進穩定。HARD 時間極短且處高剛度閉鏈，故 $\dot V_{self} \approx 0$。

---

## Level 3 — 幾何層

### 3.1 可達集

瞬時可達集（受關節限 $Q$ 約束，故非球體而是扭曲殼層）：

$$R(t) = \{p \in \mathbb{R}^3 : \exists q \in Q,\; p = f_{FK}(q)\}$$

動態可達集（引入時間預算 $\tau$ 與速度/加速度上界）：

$$R_\tau(t) = \{p : \exists u(\cdot),\; p = f_{FK}(q(t+\tau)),\; \|\omega\| \le \omega_{max},\, \|\dot\omega\| \le \alpha_{max}\}$$

單調性：$R_{\tau_1} \subseteq R_{\tau_2}$（$\tau_1 < \tau_2$）；$\lim_{\tau\to0}R_\tau = \{p_{current}\}$，$\lim_{\tau\to\infty}R_\tau = R(t)$。

### 3.2 戰術分區

$$S_{self} = R_{self}\setminus R_{opp},\quad S_{opp} = R_{opp}\setminus R_{self},\quad E = R_{self}\cap R_{opp},\quad N = \mathbb{R}^3\setminus(R_{self}\cup R_{opp})$$

距離優勢函數：$\Delta(t) = d(p_{self},\partial E) - d(p_{opp},\partial E)$，策略保持 $\Delta > 0$。

### 3.3 不可逃逸集（絕殺的幾何）

$$I_\tau(t) = \{p_{opp} : \forall u_{opp}(\cdot),\; \exists t' \in [t,t+\tau],\; p_{opp}(t') \in R_{self}(t')\}$$

1D 追逃微分對策解：

$$I_\tau = \big[\,x_s - R + (v_s^{max}-v_o^{max})\tau,\;\; x_s + R - (v_o^{max}-v_s^{max})\tau\,\big]$$

**因果**：$v_s^{max} > v_o^{max}$ → $I_\tau$ 比 $R_{self}$ 更大（速度優勢擴大控制範圍）；反之 $\tau > R/\Delta v$ 時 $I_\tau = \varnothing$。「黏／隨」＝以接觸壓低 $v_o^{eff}$ 並動態跟隨 $\dot x_s = K(x_o - x_s) + u_s$ 使對手始終留在 $I_\tau$ 內。

### 3.4 時空錐

$$C(t_0) = \{(p,t) \in \mathbb{R}^3\times\mathbb{R}^+ : \exists u(\cdot),\; p = f_{FK}(q(t)),\; t \ge t_0\}$$

時空距離（最短到達時間）：

$$d_{ST}\big((p_0,t_0),(p_1,t_1)\big) = \min_{u(\cdot)} (t_1 - t_0)$$

時間最優為 Bang–Bang 控制，$u^* = u_{max}\,\mathrm{sgn}(p_1 - p(t))$，到達時間 $t_1 - t_0 = 2\sqrt{\|p_1-p_0\|/a_{max}}$。

**必然碰撞定理**：若 $(p^*,t^*) \in C_{opp}(t_0) \cap C_{self}(t_0)$，則雙方必於 $t^*$ 在 $p^*$ 碰撞。「後發先至」＝選擇更優時空交點，非更快。

### 3.5 測地線（圓的能量解釋）

關節空間賦黎曼度量 $ds^2 = dq^T G(q)\,dq$，最短路徑為測地線：

$$\frac{D}{dt}\frac{dq}{dt} = 0$$

非平坦空間中測地線是曲線 → 太極動作（攬雀尾、雲手）為關節空間測地線，$E_{geo} < E_{line}$。

---

## Level 4 — 衝擊動力學

### 4.1 功率—時間耦合不等式（核心物理瓶頸）

失穩窗口（客觀物理常數，不受我方控制）：

$$\Delta t_{strike} = \int_{t_0}^{t_1} \mathbf{1}_{\{U(x_{opp}(t)) \ge U_{crit}\}}\, dt$$

所需做功與最短執行時間：

$$W_{req} \approx \tfrac12 m_{opp} v_{impact}^2, \qquad \Delta t_{req} = \frac{W_{req}}{P_{muscle}}$$

**功率—時間耦合定理**：打擊成功的必要條件

$$\boxed{\; P_{muscle} \ge \dfrac{W_{req}}{\Delta t_{strike}} \;}$$

證明鏈：成功 $\Rightarrow \Delta t_{req} \le \Delta t_{strike} \Rightarrow W_{req}/P_{muscle} \le \Delta t_{strike} \Rightarrow P_{muscle} \ge W_{req}/\Delta t_{strike}$。

**推論（純柔失敗的數學必然）**：$\displaystyle\lim_{P_{muscle}\to P_{baseline}} \frac{W_{req}}{P_{muscle}} = \Delta t_{req} \to \infty$，超出窗口。

**內功只是乘數非生成器**：$P_{output} = \eta\, P_{muscle}$，$\eta$ 上限有限，無法彌補 $P_{muscle}$ 不足。

### 4.2 結構槓桿放大因子

瞬時槓桿比與有效力臂：

$$\alpha(t) = \frac{L_{self}(t)}{L_{opp}(t)}, \qquad L = \frac{\|(p-c)\times F\|}{\|F\|}$$

**奇異點處發散**：對手 $U \to 0 \Rightarrow p_{ZMP,opp} \to \partial P \Rightarrow L_{opp} \to 0 \Rightarrow \alpha(t) \to \infty$。

發勁完整力學（合 $\eta$ 與 $\alpha$）：

$$F_{impact} = \alpha(t)\cdot\eta\cdot F_{input}, \qquad \frac{F_{impact}}{F_{input}} = \alpha\eta$$

「四兩撥千斤」＝ $\alpha \gg 1$ 時小 $F_{input}$ 產生大 $F_{impact}$。

**代價（反向耦合）**：$\alpha$ 峰值瞬時即逝，有效槓桿窗口

$$\Delta t_{leverage} = \int_{t_0}^{t_1} \mathbf{1}_{\{\alpha(t)\ge\alpha_{thr}\}}\,dt$$

比 $\Delta t_{strike}$ 更短 → 對神經—肌肉協調要求更高。

### 4.3 生理加加速度（Jerk）約束

階躍切換的災難：$j = \dot a = \frac1m \dot F$，瞬間跳變 $\Rightarrow j(t_{switch}) \to \infty$。

**生理約束**：$\|j(t)\| \le J_{max}$，等價於力變化率約束 $\|\dot F\| \le m J_{max}$。

平滑過渡（Sigmoid）：

$$u(t) = u_{soft} + (u_{hard}-u_{soft})\,\sigma\!\Big(\frac{t-t_{switch}}{\tau}\Big), \qquad \sigma(x) = \frac{1}{1+e^{-\lambda x}}$$

最大力變化率 $\|\dot F\|_{max} = \|\Delta u\|\,\lambda/4\tau$，代入約束得**最小過渡時間**：

$$\boxed{\; \tau \ge \frac{\lambda\,\|\Delta u\|}{4 m J_{max}} \;}$$

**圓的必然性**：力分解 $F(t) = F(t)\hat n(t)$，jerk

$$j = \frac1m\big[\ddot F\,\hat n + 2\dot F\,\dot{\hat n} + F\,\ddot{\hat n}\big]$$

直線運動 $\dot{\hat n}=\ddot{\hat n}=0 \Rightarrow j = \frac1m\ddot F\,\hat n$，jerk 全集中單一方向。圓/螺旋運動把 jerk 分散到切向（模量變化）與法向（方向變化）兩分量。螺旋再增一自由度，進一步分散。

最優力曲線即變分問題的解：

$$\min_{F(t)} \int_0^T \|j(t)\|^2\,dt \quad \text{s.t.}\quad \int_0^T F(t)\cdot dx = W_{req} \;\Rightarrow\; \text{平滑曲線（圓/螺旋）}$$

---

## 整合 — 系統完備性與剛柔並濟

### I.1 木桶效應

五層串聯：

$$\text{系統有效性} = \min(\text{Level}_0, \text{Level}_1, \dots, \text{Level}_4)$$

純柔派缺 Level 0、4 → 若 $P_{muscle} < P_{threshold}$ 則 $\Delta t_{req} > \Delta t_{strike}$ → 系統有效性 $= 0$。非「功夫不到家」而是系統不完備。

### I.2 效率與帕累托最優

戰鬥效率 $\varepsilon = D/E_{input}$（破壞力 / 自身能耗）。

**剛柔並濟最優性定理**：純柔策略（$P_{muscle} < P_{threshold}$）被嚴格支配，不可能是帕累托最優。最優解必滿足

$$P_{muscle} \ge P_{threshold}, \qquad \eta > \eta_{min}, \qquad \alpha > 1$$

證明：構造 $P_{muscle}' = P_{threshold} + \epsilon$、其餘不變，則 $D > 0 > D(x_{柔})$ 而 $\varepsilon$ 幾乎不變 → 嚴格優於純柔解。

系統結構為乘法非加法：$\text{有效系統} = \text{道（Level 1–3）} \times \text{器（Level 0,4）}$，任一項為零則結果為零。

---

## 補充 A — 軟體動力學（粘彈性補完）

剛體假設在微觀失效：接觸力奇異（$F_{contact}\to\infty,\,\Delta t\to0$）、接觸退化為零測度點（$A_{contact}=0$，觸覺無信號）、耗散機制不明。引入粘彈性補完。

### A.1 本構與阻尼諧振子化

Kelvin–Voigt：$\sigma = C:\varepsilon + \eta:\dot\varepsilon$；一維 $\sigma = E\varepsilon + \eta\dot\varepsilon$。

軟體運動方程（$\varepsilon \approx x/L$）：

$$m\ddot x + \frac{A\eta}{L}\dot x + \frac{AE}{L}x = F(t) \;\Longrightarrow\; \ddot x + 2\zeta\omega_n\dot x + \omega_n^2 x = \frac{F(t)}{m}$$

$$\omega_n = \sqrt{\frac{AE}{mL}}, \qquad \zeta = \frac{\eta}{2\sqrt{EmL/A}}$$

### A.2 衝擊傳導：脆勁 / 沉勁 / 滲透勁

衝量 $J = \int_0^{\Delta t} F\,dt = m\,\Delta v$。欠阻尼接觸時間（半阻尼週期）：

$$\Delta t_{contact} \approx \frac{T_d}{2} = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}, \qquad \omega_d = \omega_n\sqrt{1-\zeta^2}$$

剛體 $\Delta t \to 0$（脆，易反震）；軟體 $\Delta t$ 延長（沉，力波延後）。滲透勁峰值延遲 $t_{peak} \approx \pi/\omega_d$；粘性耗散使應力波展寬，深層滯留。

### A.3 鬆 = 低通濾波器（反直覺防禦）

傳遞函數與高頻衰減：

$$H(\omega) = \frac{1}{-\omega^2 + 2i\zeta\omega_n\omega + \omega_n^2}, \qquad |H(\omega)| \approx \frac{1}{\omega^2}\;(\omega \gg \omega_n)$$

加速度高頻分量 $|\tilde a(\omega)| \sim |\tilde F(\omega)|/(m\omega^2)$，jerk $|\tilde j(\omega)| = \omega|\tilde a| \sim |\tilde F(\omega)|/(m\omega)$。

**因果**：高頻 jerk 被軟組織以 $\propto 1/\omega$ 抑制。鬆 → 低 $E,\eta$ → 低 $\omega_n$ → 截止頻率低 → 過濾更多高頻衝擊、把衝擊攤平到長時窗、保護骨骼。僵硬肌肉（高 $\omega_n$）反而像脆陶瓷。

### A.4 接觸流形與聽勁逆問題

軟體接觸從點演化為有限面積流形 $M_{contact} = \{(x,y): g(x,y,z(x,y))=0\}$。Hertz 接觸：

$$a = \Big(\frac{3FR}{4E^*}\Big)^{1/3}, \quad A = \pi a^2, \quad E^* = \frac{E}{1-\nu^2}$$

應變張量 $\varepsilon = \tfrac12[\nabla u + (\nabla u)^T]$，應力 $\sigma_{ij} = C_{ijkl}\varepsilon_{kl} + \eta_{ijkl}\dot\varepsilon_{kl}$。

**聽勁＝積分逆問題**：從接觸面應力分布反推對手合力與力矩

$$F_{opp} = \int_M \sigma(x,y)\cdot\hat n\;dA, \qquad \tau_{opp} = \int_M (r - r_{ref})\times[\sigma(x,y)\cdot\hat n]\;dA$$

補全主論文 $h_{touch}$（無窮維形變場 → 三維力的降維映射）：

$$h_{touch}(x) = \Big[\textstyle\int_M p\,dA,\;\int_M \tau_x\,dA,\;\int_M \tau_y\,dA\Big]^T$$

### A.5 鬆緊變換 = 阻尼調製

時變粘性/彈性隨肌肉激活度 $\alpha(t)\in[0,1]$：

$$\eta(t) = \eta_{min} + [\eta_{max}-\eta_{min}]\alpha(t), \qquad E(t) = E_{min} + [E_{max}-E_{min}]\alpha(t)$$

最優阻尼控制（防守，最大化吸收能量）：

$$\max_{\alpha(t)} \int_0^T E_{absorbed}\,dt, \quad E_{absorbed} = \int_0^T\!\!\int_V \eta(\alpha)\|\dot\varepsilon\|^2\,dV\,dt, \quad \text{s.t. } p_{ZMP}\in P,\, 0\le\alpha\le1$$

PMP 給出 **Bang–Bang 解**：

$$\alpha^*(t) = \begin{cases} 1 & \|\dot\varepsilon\| \text{ 大（外力強）} \to \text{變緊吸收} \\ 0 & \|\dot\varepsilon\| \text{ 小（無外力）} \to \text{變鬆待發} \end{cases}$$

此即「引進落空、借力打力」的數學實現。

### A.6 FEM 離散與多尺度耦合

$$M\ddot U + D(\alpha)\dot U + K(\alpha)U = F_{ext}, \qquad D(\alpha) = \beta_M(\alpha)M + \beta_K(\alpha)K(\alpha)$$

宏觀（剛體，主論文）與中觀（粘彈性）下行/上行耦合：$\tau \to F_{muscle}$（Hill 模型 $F_{muscle} = F_{max}\,a(\alpha)f_L(L)f_V(V)$）；軟體變形回饋等效阻尼 $C_{ij}^{eff} = C_{ij}^{rigid} + \Delta C_{ij}(\alpha,U)$。

**效率分解**（補全 Level 0 的 $\eta$ 微觀機制）：

$$\eta_{total} = \eta_{geometric}\cdot\eta_{soft}, \qquad \eta_{soft} = 1 - \frac{E_{dissipated}}{E_{input}}$$

$\alpha$ 高 → $\eta$ 高 → $E_{dissipated}$ 大 → $\eta_{soft}$ 低。故「鬆」同時提升傳導效率與感知信噪比。

---

## 補充 B — 通用運動引擎（可微分物理）

把五層架構工程化：Physics Core（Level 0，求解 $M\ddot q + C\dot q + G = \tau + J^T F_{ext}$，輸出 $q,\dot q,p_{ZMP},F_{contact}$）／ Control Core（Level 1–3，輸出 $\tau_{desired}$）／ Learning Core（RL 訓練策略）。

### B.1 可微分物理（梯度可反傳）

傳統物理引擎為黑箱，僅能無梯度 RL。可微分化使 $\partial q(t+\Delta t)/\partial\tau(t)$ 可計算：

- 解析微分（無約束）：$\ddot q = M^{-1}(\tau - C\dot q - G) \Rightarrow \partial\ddot q/\partial\tau = M^{-1}$
- 隱式微分（約束系統，隱式方程 $F(q',\tau)=0$）：

$$\frac{\partial q'}{\partial\tau} = -\Big(\frac{\partial F}{\partial q'}\Big)^{-1}\frac{\partial F}{\partial\tau}$$

### B.2 端到端與 RL 目標

像素 → CNN → 狀態 $s$ → 策略 $\pi(a\mid s)$ → 力矩 $\tau$ → 可微分物理 → $s'$ → 獎勵 $r$ → 全模組聯合反傳。

$$\max_\pi \mathbb{E}\Big[\sum_{t=0}^{T}\gamma^t r_t\Big]$$

$$r_t = \underbrace{w_1 r_{task}}_{\text{完成目標}} - \underbrace{w_2\|\tau\|^2}_{\text{能量}} - \underbrace{w_3\,\mathbf{1}_{\{ZMP\notin P\}}}_{\text{失衡}} - \underbrace{w_4\|j\|^2}_{\text{Jerk}}$$

獎勵函數的四項正是 Level 4 全部約束（任務、能量、ZMP 穩定、Jerk）的直接編碼 → 主論文五層在工程上閉環。

---

## 哲學結語

整套架構的因果脊骨可壓成一條：物理層界定可行域，感知層估計狀態，控制層在可行域內求解，幾何層把對手鎖入不可逃逸集，動力層受功率—時間—Jerk 三重耦合所限——而貫穿五層的唯一乘法律是 $\text{有效} = \text{道} \times \text{器}$，任何一項歸零，整個系統歸零。剝去所有數值與譬喻之後，剩下的不是武術，是一個「智能體在動態約束下執行物理任務」的最小完備方程組；太極拳只是它一個被數百年實戰退火過的解。
