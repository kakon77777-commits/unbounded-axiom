# 附錄 A：演算法形式化、程式範例與可行性論證

### EveMissLab 工作論文 · 附錄（v0.1 草稿）

本附錄承擔本文刻意推遲的工作：把網頁中實際運行的三個演算法——AFSA、退火 Langevin／Fokker–Planck 測度流、自適應 AMF——逐一抽出，各自配上形式化後的數學定義與更新方程式、基本的程式語言範例（以 Python／NumPy 為例），並論證「為何可以這樣辦到」。本版為初稿，符號與書目將於後續版本統一收斂；程式範例以可讀與忠於網頁邏輯為先，未針對效能優化。

---

## A.0 共同設定與記號

設搜索域 $\Omega = [\ell, u]^d \subset \mathbb{R}^d$（網頁中 $d=2$），食物濃度／適應度場為 $f:\Omega\to\mathbb{R}$。本文一律處理**最大化**問題：尋找 $x^\star \in \arg\max_{x\in\Omega} f(x)$。種群為 $N$ 個點 $X=\{x_i\}_{i=1}^N$。$\Pi_\Omega$ 表示對域的逐分量投影（clamp）。「公告牌」記錄歷史全局最佳 $b_k = \max_{t\le k}\max_i f(x_i^{(t)})$。

衡量成本的單位是**函數評估次數**（evaluations），記 $\mathcal{E}$；演算法的優劣以「達到給定解品質所耗的 $\mathcal{E}$」衡量，而非迭代次數。本文所有對打皆以 $b$ 對 $\mathcal{E}$ 的曲線比較，並以同一初始種群 $X^{(0)}$ 餵給所有競爭者以消除初始偶然性。

容差命中定義為 $f^\star - b_k < \theta$，其中 $f^\star=\max_\Omega f$（以細網格掃描近似），$\theta = 0.01\,(f_{\max}-f_{\min})$ 為地形幅度的百分之一。

---

## A.1 AFSA（人工魚群演算法）

### A.1.1 形式化

魚 $i$ 的狀態為位置 $x_i\in\Omega$、適應度 $Y_i=f(x_i)$。參數：視野 $V$、步長 $s$、擁擠度因子 $\delta\in(0,1]$、覓食重試次數 $T_p$、種群 $N$。

定義「朝目標前進一步」算子（步長帶隨機縮放）：

$$
\mathrm{move}(x, x_t) \;=\; \Pi_\Omega\!\left( x + s\,\xi\,\frac{x_t-x}{\lVert x_t-x\rVert} \right),\qquad \xi\sim U(0,1).
$$

視野鄰域 $\mathcal{N}_i=\{\,j\neq i:\lVert x_j-x_i\rVert\le V\,\}$，鄰數 $n_f=\lvert\mathcal{N}_i\rvert$。

**覓食 Prey.** 對 $k=1,\dots,T_p$：抽 $x_j=\Pi_\Omega\!\big(x_i+V\,\eta\big)$，$\eta\sim U(-1,1)^d$；若 $f(x_j)>Y_i$ 則回傳 $\mathrm{move}(x_i,x_j)$ 並終止。若 $T_p$ 次皆失敗，回傳隨機步 $\Pi_\Omega\!\big(x_i+s\,\eta\big)$。

**聚群 Swarm.** 中心 $x_c=\tfrac{1}{n_f}\sum_{j\in\mathcal{N}_i}x_j$。若 $f(x_c)>Y_i$ 且 $n_f<\delta N$（中心更優且不擁擠），回傳 $\mathrm{move}(x_i,x_c)$；否則退回 Prey。

**追尾 Follow.** 取 $j^\star=\arg\max_{j\in\mathcal{N}_i}f(x_j)$，並計其鄰擁擠度 $n_f'=\lvert\{k\neq j^\star:\lVert x_k-x_{j^\star}\rVert\le V\}\rvert$。若 $f(x_{j^\star})>Y_i$ 且 $n_f'<\delta N$，回傳 $\mathrm{move}(x_i,x_{j^\star})$；否則退回 Prey。

**行為選擇與公告牌.** 對每條魚，模擬 Swarm 與 Follow 兩候選、取結果適應度較高者；若二者皆不優於 $Y_i$，執行 Prey。所有魚更新後，以最優個體刷新公告牌。終止條件為達容差或迭代上限。

### A.1.2 程式範例（Python／NumPy）

```python
import numpy as np

def afsa_step(X, f, lo, hi, visual=1.2, step=0.4, delta=0.62, try_num=5):
    """單次 AFSA 迭代。X: (N,d) 種群；f: 適應度（最大化）；lo,hi: 域邊界。"""
    N, d = X.shape
    Y = np.array([f(x) for x in X])

    def move(x, target):
        v = target - x
        nv = np.linalg.norm(v)
        if nv < 1e-9:
            return x.copy()
        return x + step * np.random.rand() * v / nv

    def neighbors(i):
        dist = np.linalg.norm(X - X[i], axis=1)
        idx = np.where(dist <= visual)[0]
        return idx[idx != i]

    def prey(i):
        for _ in range(try_num):
            xj = X[i] + visual * np.random.uniform(-1, 1, d)
            if f(xj) > Y[i]:
                return move(X[i], xj)
        return X[i] + step * np.random.uniform(-1, 1, d)  # 隨機遊走

    def swarm(i):
        nb = neighbors(i); nf = len(nb)
        if nf == 0:
            return None
        xc = X[nb].mean(axis=0)
        if f(xc) > Y[i] and nf < delta * N:
            return move(X[i], xc)
        return None

    def follow(i):
        nb = neighbors(i)
        if len(nb) == 0:
            return None
        j = nb[int(np.argmax(Y[nb]))]
        nf2 = int(np.sum(np.linalg.norm(X - X[j], axis=1) <= visual) - 1)
        if Y[j] > Y[i] and nf2 < delta * N:
            return move(X[i], X[j])
        return None

    Xn = X.copy()
    for i in range(N):
        cands = [c for c in (swarm(i), follow(i)) if c is not None]
        best = max(cands, key=lambda c: f(c)) if cands else None
        Xn[i] = best if (best is not None and f(best) > Y[i]) else prey(i)
    return np.clip(Xn, lo, hi)
```

### A.1.3 為何如此／它在做什麼

AFSA 沒有收斂性證明，它是一個啟發式：其有效性來自三股力的協同，而非任何定理。覓食是帶隨機回退的局部上升，提供探索與「跳出局部最優」的隨機性來源——重試次數 $T_p$ 越小，隨機遊走機會越多，越容易逃離局部峰。聚群與追尾是朝參考點（質心、最優鄰居）的吸引，負責資訊共享與利用。擁擠度因子 $\delta$ 限制吸引的規模，是它唯一的多樣性保存機制：當局部聚集超過 $\delta N$，吸引被否決，迫使魚轉向別處。

從本文脊椎的角度看，AFSA 的本質是「吸引（向質心／最優）＋隨機回退（覓食失敗時）」的混合，這正是漂移加擴散的離散、語意化版本。它的可讀性高，但代價是把搜索動力學切成數個離散行為分支、以擁擠度數人頭這種粗糙的方式近似多樣性控制——這也是它在崎嶇多峰地形上不穩定的根源。

---

## A.2 退火 Langevin／Fokker–Planck 測度流

### A.2.1 形式化

把搜索的主體從個體升格為機率測度 $\rho_t$（種群是它的取樣）。**過阻尼 Langevin 擴散**（對最大化 $f$）為

$$
\mathrm{d}X_t \;=\; \nabla f(X_t)\,\mathrm{d}t \;+\; \sqrt{2T}\,\mathrm{d}W_t,
$$

其中 $W_t$ 為 $d$ 維標準布朗運動，$T>0$ 為溫度。其法則 $\rho_t$ 滿足 **Fokker–Planck 方程**

$$
\partial_t \rho \;=\; -\nabla\!\cdot\!\big(\rho\,\nabla f\big) \;+\; T\,\Delta\rho.
$$

**穩態分布（Gibbs 測度）.** 令穩態流 $J=\rho\nabla f - T\nabla\rho = 0$，得 $\nabla\log\rho = \nabla f/T$，故

$$
\rho_\infty(x) \;\propto\; \exp\!\big(f(x)/T\big).
$$

當 $T\to 0^+$，$\rho_\infty$ 集中於 $f$ 的全局最大點集——這就是退火的數學意義。

**Wasserstein 梯度流身分.** 上述 FP 方程是自由能泛函

$$
\mathcal{F}(\rho) \;=\; -\!\int_\Omega f\,\rho\,\mathrm{d}x \;+\; T\!\int_\Omega \rho\log\rho\,\mathrm{d}x
$$

在 Wasserstein-2 度量下的梯度流（JKO 格式）。第一項（位能）驅動質量湧向高 $f$ 區（利用），第二項（熵）使質量擴散（探索），$T$ 是兩者的權衡。**關鍵觀察**：AFSA 必須用擁擠度因子手工塞入的「多樣性／反塌縮」機制，在這裡是熵項的自然後果，由 $\nabla\!\cdot(T\nabla\rho)$ 這一擴散項導出，而非憑空設定。

**離散化（Euler–Maruyama）.** 每粒子

$$
x_i \;\leftarrow\; \Pi_\Omega\!\Big( x_i + \Delta t\,\nabla f(x_i) + \sqrt{2T\Delta t}\;\zeta \Big),\qquad \zeta\sim\mathcal{N}(0,I_d).
$$

退火時間表 $T_k=\max(T_{\min},\,T_0\,\gamma^{k})$。若 $\nabla f$ 不可解析，以中央差分近似 $\partial_{x^{(m)}} f \approx \big(f(x+h e_m)-f(x-h e_m)\big)/(2h)$，每步耗 $2d$ 次評估。

### A.2.2 程式範例（Python／NumPy）

```python
import numpy as np

def fd_grad(f, h):
    """中央差分梯度算子；每次呼叫耗 2d 次評估。"""
    def g(x):
        d = len(x); out = np.zeros(d)
        for m in range(d):
            e = np.zeros(d); e[m] = h
            out[m] = (f(x + e) - f(x - e)) / (2 * h)
        return out
    return g

def langevin_step(X, grad_f, lo, hi, T, dt=0.01, clip=0.5):
    G = np.array([grad_f(x) for x in X])           # 漂移方向（梯度）
    drift = dt * G
    dn = np.linalg.norm(drift, axis=1, keepdims=True)
    drift = drift * np.minimum(1.0, clip / np.maximum(dn, 1e-12))  # 漂移上限（數值穩定）
    noise = np.sqrt(2 * T * dt) * np.random.randn(*X.shape)        # 擴散項
    return np.clip(X + drift + noise, lo, hi)

def anneal(T0, gamma, k, Tmin=0.02):
    return max(Tmin, T0 * (gamma ** k))
```

### A.2.3 為何如此（可行性與收斂性）

這套機制之所以「辦得到」，有嚴格理論支撐，而非經驗巧合。其一，穩態存在且明確：法則收斂到 Gibbs 測度 $\rho_\infty\propto e^{f/T}$，故在固定 $T$ 下，採樣會集中於高適應度區，集中程度由 $1/T$ 控制。其二，全局最優可達：經典模擬退火結果（Geman–Geman、Hwang 等）指出，只要退火夠慢（如 $T_k\sim c/\log k$），過程依機率收斂到全局最優；實務上幾何冷卻 $T_0\gamma^k$ 是更快但無嚴格保證的折衷。其三，粒子實現合法：$N$ 個粒子是 $\rho_t$ 的經驗測度近似，$N\to\infty$ 時它們實現 FP 流；有限 $N$ 則是其蒙地卡羅版本。

漂移上限（clip）不屬於理論本體，它只是離散化的數值穩定器：在 Rastrigin 這類梯度振幅極大的地形上，$\Delta t\,\nabla f$ 單步可能過大導致發散，clip 將其限幅。它不改變穩態，只保證歐拉離散不爆。本文 Ackley 一戰中測度流昂貴的評估成本，幾乎全來自 `fd_grad` 的 $2d$ 次評估；若 $\nabla f$ 解析可得，此成本即消失——這是脊椎在「梯度可得」情境下的真實效能，與其在「需數值梯度」情境下被懲罰的表象，必須分開評估。

---

## A.3 AMF（自適應測度流）

### A.3.1 形式化

AMF 的設計目標是消除對地形敏感的參數（$T_0,\Delta t,\mathrm{clip}$），代之以尺度無關、可自我調節的機制。令 $\mathrm{span}=u-\ell$ 為域寬。

**方向歸一漂移（尺度無關）.** 只取梯度方向，不取其大小：

$$
d_i \;=\; \eta\cdot\mathrm{span}\cdot\tau\cdot\frac{\nabla f(x_i)}{\lVert\nabla f(x_i)\rVert+\epsilon},
$$

其中 $\tau\in(0,1]$ 為無量綱溫度因子，$\eta$ 為「每步前進域寬之比例」（預設 $0.02$），$\epsilon$ 為防零除的微量（$10^{-9}$）。

**噪聲（亦尺度無關）.** $\;\sigma\cdot\mathrm{span}\cdot\tau\cdot\zeta,\quad \zeta\sim\mathcal{N}(0,I_d)$。更新：

$$
x_i \;\leftarrow\; \Pi_\Omega\!\big( x_i + d_i + \sigma\,\mathrm{span}\,\tau\,\zeta \big).
$$

**自適應溫度時間表（回饋式）.** 每迭代先幾何冷卻 $\tau\leftarrow\max(\tau_{\min},\,c\,\tau)$；同時監看全局最佳，若連續 $W$ 步無改善（停滯）則重加熱 $\tau\leftarrow\min(1,\,r\,\tau)$ 並重置停滯計數。預設 $c=0.99$、$r=3$、$W=25$、$\tau_{\min}=0.02$。

### A.3.2 程式範例（Python／NumPy）

```python
import numpy as np

def amf_step(X, grad_f, lo, hi, tau, span, eta=0.02, sigma=0.045):
    G = np.array([grad_f(x) for x in X])
    norms = np.linalg.norm(G, axis=1, keepdims=True) + 1e-9
    drift = eta * span * tau * (G / norms)               # 僅方向，尺度無關
    noise = sigma * span * tau * np.random.randn(*X.shape)
    return np.clip(X + drift + noise, lo, hi)

def amf_update_tau(tau, improved, stag, W=25, cool=0.99, reheat=3.0, tmin=0.02):
    tau = max(tmin, tau * cool)                            # 幾何冷卻
    if improved:
        stag = 0
    else:
        stag += 1
        if stag > W:                                      # 停滯重加熱
            tau = min(1.0, tau * reheat)
            stag = 0
    return tau, stag
```

### A.3.3 為何如此（尺度不變性、重加熱、精度稅與修補）

**尺度不變性的論證.** 適應度線性重標 $f\mapsto af+b$（$a>0$）下，方向歸一漂移 $\nabla f/\lVert\nabla f\rVert$ 不變，噪聲不依賴 $f$ 亦不變，故軌跡分布不變——這使同一組 $(\eta,\sigma,c,r,W)$ 能跨越適應度尺度迥異的地形。域尺度重標 $\Omega\mapsto\lambda\Omega$ 下，漂移與噪聲皆隨 $\mathrm{span}$ 等比縮放，動力學相似。這正是「一組元參數零重調打多張地形」在原理上成立的根據。

**方向歸一治平原.** Ackley 的平原上 $\lVert\nabla f\rVert\to 0$，純 Langevin 的漂移 $\Delta t\nabla f$ 隨之消失、退化為盲目擴散；但 $\nabla f/\lVert\nabla f\rVert$ 即使在微小梯度下仍給出方向，使 AMF 以固定的域寬比例穩定內進。這是 AMF 在 Ackley 上比手調 Langevin 更省評估的結構性原因。

**重加熱即自適應逃生.** 固定退火時間表無法因地形調整；停滯重加熱則讓溫度由「是否卡住」這個運行時訊號驅動：陷入停滯時抬高 $\tau$，重新膨脹探索半徑，類比於自適應模擬退火的再加熱。代價是評估次數——逃生能力是用 $\mathcal{E}$ 買來的（本文 Rastrigin 上 AMF 評估近乎翻倍即源於此）。

**精度稅的形式化與修補.** 病灶在於：靠近最優時改善終將停滯於容差帶內，於是重加熱不斷把 $\tau$ 踢離 $\tau_{\min}$，殘餘噪聲量級 $\sim\sigma\,\mathrm{span}\,\tau$ 持續擾動，使解無法收緊——這就是 AMF 最終差距普遍劣於專家的根源。修補方向（待形式化與實作）：引入**終局相**，以多樣性塌縮（如下節 $\lambda_2\to 0$）配合全局最佳穩定改善為觸發條件，判定真盆地已鎖定後關閉重加熱、強制 $\tau\to\tau_{\min}$ 硬退火精修，等於把「探索者」與「收割者」分為前後兩個人格。預期可退回大部分精度稅而不需人手切換。

---

## A.4 共同基礎設施與延伸焊接（待形式化）

以下為支撐對打的基礎設施與本文提及、尚待形式化的改良方向，列其數學骨架以誌後續。

**評估公平軸.** 以一個計數包裝器攔截所有對 $f$ 的呼叫，分演算法累加 $\mathcal{E}$；收斂曲線以 $b$ 對 $\mathcal{E}$ 繪製。此為對打公平性的技術保證。

**$\lambda_2$ 多樣性診斷（取代擁擠度 $\delta$）.** 對種群建半徑圖 $A_{ij}=\mathbb{1}[\lVert x_i-x_j\rVert\le r]$，度矩陣 $D=\mathrm{diag}(\sum_j A_{ij})$，Laplacian $L=D-A$。代數連通度 $\lambda_2(L)$（第二小特徵值）為連續、幾何感知的多樣性／早熟感測器：$\lambda_2\to 0$ 表示種群塌成單一連通團。可作為 commit 相觸發訊號，亦可取代 $\delta$ 的二元數人頭。

**持續同調 niching（多峰覆蓋）.** 對適應度場的超水平集過濾 $\{f\ge t\}$ 計算 barcode，每根高持續性條對應一個顯著盆地及其 prominence；據此把子群分配到不同高持續盆地，可證地覆蓋所有超過持續性門檻的峰。

**資訊幾何／自然梯度（各向異性步長）.** 把局部子群視為高斯，沿 Fisher 度量做自然梯度更新，使步長升格為度量量、自動適配局部曲率與協方差——即 CMA-ES 的核心，置於正確的抽象層級。

**終局相（精度修補）.** 如 A.3.3，以 $\lambda_2$ 塌縮 + 全局最佳穩定改善為觸發，關閉重加熱並硬退火，回收 AMF 的精度稅。

---

*本附錄為 v0.1 草稿。下一步：補齊 A.2.3 收斂性陳述的條件與引用、為 A.4 各延伸方向各立子附錄、並將程式範例整合為可重現的對打腳本。*
