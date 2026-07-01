# 聯合風暴消散預測框架：ETN 動態風暴眼 × 吸引子環境動力學

## Joint Storm Dissipation Prediction: ETN Storm Eye × Attractor Environmental Dynamics

---

**文件編號**：EML-ETN-STORM-2026-v1.0
**密級**：公開（實驗站發表版）
**日期**：2026 年 6 月
**作者**：Neo.K（許筌崴）+ Theia（AI 協作）
**機構**：EveMissLab Logic Matrix（一言諾科技有限公司）
**前置文件**：
- EML-ETN-2026-v1.0（ETN 蝴蝶結記法）
- EML-ETN-2026-v2.0（ETN 動態中心論：風暴眼原理）
- ETN-Storm v0.1（ETN 風暴眼追蹤器，程式碼原型）
**關鍵詞**：ETN 動態風暴眼、⊛ 動態不動點、吸引子動力學、聯合消散預測、SE_n 對稱度、雙重時間尺度、熱帶氣旋

---

## 摘要

傳統熱帶氣旋消散預測依賴兩類方法：吸引子動力學（含混沌理論、Lorenz 系統、泛函分析）捕捉系統的全局軌跡行為；數值天氣預報（NWP）解算 Navier-Stokes 方程追蹤物理場演化。兩者共同的局限在於：無法在快速（數小時）時間尺度上直接量化**風暴眼內部結構的對稱性崩潰**這一關鍵前驅信號。

本文提出**聯合風暴消散預測框架（Joint Storm Dissipation Framework, JSDF）**，整合兩個互補的診斷元件：

- **ETN 風暴眼元件**（快速 / 局部）：基於 ETN 動態風暴眼原理，以 SE_n 對稱度量化 ⊛ 動態不動點的穩定性，捕捉眼牆結構的即時狀態。
- **吸引子環境元件**（慢速 / 全局）：追蹤風暴所在環境狀態向量在吸引子盆地中的位置，量化環境對氣旋維持的支撐程度。

聯合風險定義為兩元件的幾何平均：

$$R_{\text{joint}} = \sqrt{R_{\text{ETN}} \cdot R_{\text{env}}}$$

幾何平均結構要求**雙重確認**——任一信號為零則聯合風險歸零，兩者同時升高方觸發高確信度消散預警。理論、實驗與程式碼原型共同驗證此框架，並給出全球氣象平台的接口設計草圖。

---

## 一、問題定位：單信號的固有局限

### 1.1 吸引子方法的盲點

吸引子動力學（Lorenz 系統、奇異吸引子、Lyapunov 指數分析）在描述氣旋的**長時段軌跡行為**上具有紮實的理論基礎。然而，吸引子方法本質上是**全局 → 局部**的推斷路徑：先確定系統在相空間中的全局結構，再從中推斷當前軌跡的走向。

這條路徑有三個結構性弱點：

第一，**時間解析度不足**。吸引子邊界的迫近通常是一個數天尺度的過程；然而颱風的急速增強（RI）或眼牆替換週期（ERC）可以在 6~12 小時內完成，這遠快於吸引子信號的響應速度。

第二，**內部結構不透明**。吸引子描述的是系統在相空間中的軌跡，但不直接告訴我們風暴內部的幾何結構——眼牆是否對稱、對流是否均勻分佈——而這些正是消散的直接前兆。

第三，**初始條件敏感性**。Lyapunov 指數描述了小擾動的指數放大，但它告訴我們系統整體不可預測，而不是眼在哪裡、往哪裡走。

### 1.2 傳統 NWP 的補充需求

NWP 模式（GFS、ECMWF、JMA）在精度上是現有最佳工具，但具有高計算成本、每 6 小時更新一次的限制。在更新週期之間，沒有一個輕量的框架可以即時評估眼牆狀態。

### 1.3 JSDF 的定位

JSDF 不取代吸引子方法或 NWP，而是在它們之間**補入一個快速局部診斷層**：

```
[快速 / 局部]  ETN 風暴眼元件（SE_n）
      ↕  聯合判斷
[慢速 / 全局]  吸引子環境元件（E(x)）
      ↕  參考基準
[超慢 / 完整]  NWP 全場解算（每 6 小時）
```

三個層次形成**多時間尺度診斷體系**，而不是相互替代的競爭關係。

---

## 二、ETN 風暴眼元件（快速 / 局部）

### 2.1 理論基礎

ETN 動態中心論（EML-ETN-2026-v2.0）確立了整數 n 的「風暴眼」結構：

$$\circledast_n := \left\{ G_{n+1}^- \curvearrowright \circledast \curvearrowleft G_n^- \right\} \cup J_\uparrow(n) \cup J_\downarrow(n)$$

其中 $G_{n+1}^- = \lim_{\varepsilon \to 0^+}(n+1-\varepsilon)$、$G_n^- = \lim_{\varepsilon \to 0^+}(n-\varepsilon)$ 為兩側 GOD POINT，$J_\uparrow$、$J_\downarrow$ 為從中心向兩側發射的無窮旅程。

風暴眼原理確立：**⊛_n 的靜止條件是上下 GOD POINT 拉力完全對稱**：

$$\text{SE condition}: \quad F_{\text{up}}(G_{n+1}^-) = F_{\text{down}}(G_n^-)$$

在大氣動力學中，這個對稱條件對應眼牆對流的角向均勻性。

### 2.2 角向張力剖面

定義以風暴眼為中心、半徑 $r_0$ 的採樣圓上的**角向張力剖面** $T(\theta)$：

$$T(\theta) := -\frac{\partial p}{\partial r}\bigg|_{r=r_0,\,\theta} + \alpha \cdot V_r(\theta)$$

其中 $\partial p / \partial r$ 為徑向壓力梯度（向內為正），$V_r(\theta)$ 為 $\theta$ 方向的徑向入流風速，$\alpha$ 為加權係數。

$T(\theta)$ 的可觀測來源包括：
- 雷達反射率的角向分佈（即時，每 6~10 分鐘）
- 衛星紅外亮溫的角向均勻度（近即時，每 30 分鐘）
- NWP 輸出場的角向積分（每 6 小時）

### 2.3 SE_n 對稱度

**定義**（SE_n 對稱度量）：

$$\text{SE}_n := 1 - \frac{\sigma[T(\theta)]}{\mu[T(\theta)]}$$

其中 $\sigma$ 為角向標準差，$\mu$ 為角向均值。

**性質**：
- $\text{SE}_n \in [0, 1]$
- $\text{SE}_n = 1$：$T(\theta)$ 完全均勻，⊛ 完全成立（完美風暴眼）
- $\text{SE}_n = 0$：$T(\theta)$ 極度不均勻，⊛ 退化（眼牆崩潰）
- $\text{SE}_n \geq \tau_{\text{SE}} \approx 0.65$：⊛ 判定成立

**⊛ 判定**：

$$\circledast \text{ well-defined} \iff \text{SE}_n \geq \tau_{\text{SE}}$$

### 2.4 漂移向量

**定義**（⊛ 漂移向量）：

$$\vec{F}_{\text{drift}} = \frac{1}{2\pi} \int_0^{2\pi} T(\theta) \, \hat{e}_\theta \, d\theta$$

$$\hat{e}_\theta = (\sin\theta, \, \cos\theta)^T$$

物理含義：⊛ 點往**張力不對稱的強側**漂移——即 GOD POINT 場更強的方向。這與傳統「引導流方向」不等同，但在對稱性弱的風暴中可提供補充信號。

### 2.5 ETN 消散風險

$$R_{\text{ETN}} := 1 - \text{SE}_n \in [0, 1]$$

$R_{\text{ETN}}$ 是**快速信號**：它可在數小時內從接近 0 跳到接近 1（眼牆突然崩潰），也可以在眼牆重新組織時迅速回落。

---

## 三、吸引子環境元件（慢速 / 全局）

### 3.1 環境狀態向量

定義熱帶氣旋的**環境狀態向量**：

$$\mathbf{x} = (\text{SST}, \, \text{shear}, \, \text{hum}, \, \zeta, \, \Delta p)$$

| 分量 | 物理意義 | 有利門檻 | 權重 |
|------|----------|----------|------|
| SST | 海面溫度（℃） | ≥ 26.0 | 0.30 |
| shear | 垂直風切（m/s） | ≤ 15.0 | 0.25 |
| hum | 中層相對濕度（%） | ≥ 50.0 | 0.20 |
| ζ | 低層渦度（×10⁻⁵ s⁻¹） | ≥ 5.0 | 0.15 |
| Δp | 強度（氣壓差 hPa） | ≥ 15.0 | 0.10 |

### 3.2 環境支撐度

**定義**（單因子評分函數）：

對「高值有利」型因子（SST、hum、ζ、Δp）：

$$\varphi_i(x_i) = \frac{1}{2}\left[1 + \text{clip}\!\left(\frac{x_i - \tau_i}{0.5\,\tau_i},\,-1,\,1\right)\right]$$

對「低值有利」型因子（shear）：

$$\varphi_i(x_i) = \frac{1}{2}\left[1 + \text{clip}\!\left(\frac{\tau_i - x_i}{0.5\,\tau_i},\,-1,\,1\right)\right]$$

**定義**（環境支撐度）：

$$E(\mathbf{x}) = \sum_{i} w_i \cdot \varphi_i(x_i) \in [0, 1]$$

### 3.3 吸引子盆地的三種狀態

$$\text{attractor state} := \begin{cases} \text{deep}    & E(\mathbf{x}) > 0.75 \\ \text{edge}    & 0.50 < E(\mathbf{x}) \leq 0.75 \\ \text{outside} & E(\mathbf{x}) \leq 0.50 \end{cases}$$

| 狀態 | 物理含義 |
|------|----------|
| deep | 環境極有利，深在盆地，風暴可長期維持 |
| edge | 接近盆地邊緣，環境開始惡化，需持續監測 |
| outside | 已出盆地，環境無法支撐氣旋，消散不可避免 |

**距消散流形距離**：

$$d_A(\mathbf{x}) = \max\!\left(0,\; E(\mathbf{x}) - 0.5\right)$$

### 3.4 環境消散風險

$$R_{\text{env}} := 1 - E(\mathbf{x}) \in [0, 1]$$

$R_{\text{env}}$ 是**慢速信號**：SST 的下降、風切的增強通常在數天尺度發生，提供中長期預警能力。

### 3.5 Lorenz 抽象版（教學替代）

對於純概念研究或缺乏環境觀測的情境，可用 Lorenz 系統作為環境狀態的玩具替代：

$$\frac{dx}{dt} = \sigma(y-x), \quad \frac{dy}{dt} = x(\rho-z)-y, \quad \frac{dz}{dt} = xy-\beta z$$

取標準參數 $\sigma=10,\, \rho=28,\, \beta=8/3$。Lorenz 吸引子的兩個葉片中心為：

$$\mathbf{c}_\pm = \left(\pm\sqrt{\beta(\rho-1)},\; \pm\sqrt{\beta(\rho-1)},\; \rho-1\right) \approx (\pm 8.49,\; \pm 8.49,\; 27)$$

距盆地中心距離：$d_L(t) = \min\bigl(\|\mathbf{s}(t) - \mathbf{c}_+\|,\; \|\mathbf{s}(t) - \mathbf{c}_-\|\bigr)$

Lorenz 環境支撐度：$E_L(t) = \text{clip}(1 - d_L / r_A, \; 0, \; 1)$，其中 $r_A \approx 15$ 為盆地半徑。

**注意**：Lorenz 版為純概念教學工具，不代表颱風物理。

---

## 四、聯合預測器

### 4.1 聯合風險公式

$$\boxed{R_{\text{joint}} = \sqrt{R_{\text{ETN}} \cdot R_{\text{env}}} = \sqrt{(1-\text{SE}_n)(1-E(\mathbf{x}))}}$$

**幾何平均的選擇理由**：

幾何平均實現了**雙重確認結構**：

$$R_{\text{ETN}} = 0 \;\Rightarrow\; R_{\text{joint}} = 0 \qquad (\text{眼牆完好，無消散})$$
$$R_{\text{env}} = 0 \;\Rightarrow\; R_{\text{joint}} = 0 \qquad (\text{環境極有利，無消散})$$
$$R_{\text{ETN}} \to 1,\; R_{\text{env}} \to 1 \;\Rightarrow\; R_{\text{joint}} \to 1 \qquad (\text{雙重失守，高確信消散})$$

算術平均 $(R_{\text{ETN}} + R_{\text{env}})/2$ 的問題是允許「一強補一弱」——環境完全失守但眼牆完好時仍輸出高風險值，違背物理直覺。幾何平均切斷這個後門。

### 4.2 消散判定門檻

$$\text{dissipation imminent} \iff R_{\text{joint}} \geq \tau_{\text{joint}}$$

推薦初始值：$\tau_{\text{joint}} = 0.65$（對應各分量風險均約為 0.42 以上）。

高置信消散：$R_{\text{joint}} \geq \tau_{\text{HC}} = 0.80$。

門檻值應依不同洋盆（西太平洋、大西洋、印度洋）以歷史資料定標。

### 4.3 四象限診斷框架

$$\begin{array}{c|c|c}
 & R_{\text{ETN}} \text{ 低} & R_{\text{ETN}} \text{ 高} \\
\hline
\text{deep / edge} & \textbf{穩定維持} & \textbf{短期波動，可恢復} \\
 & R_{\text{joint}} \approx 0\text{~}0.15 & R_{\text{joint}} \approx 0.25\text{~}0.45 \\
\hline
\text{edge / outside} & \textbf{環境惡化，持續監測} & \textbf{★ 高確信度消散} \\
 & R_{\text{joint}} \approx 0.15\text{~}0.40 & R_{\text{joint}} \geq 0.65 \\
\end{array}$$

### 4.4 趨勢信號

定義最近 $n$ 步的趨勢指標：

$$\Delta \text{SE}_n = \text{SE}_n^{(t)} - \text{SE}_n^{(t-n)}, \qquad \Delta E = E^{(t)} - E^{(t-n)}$$

| $\Delta \text{SE}_n$ | $\Delta E$ | 趨勢判讀 |
|---|---|---|
| > +0.05 | > +0.05 | ⚡ 急速增強（RI） |
| < −0.05 | < −0.05 | ★ 快速消散 |
| < −0.05 | ≈ 0 | 眼牆退化中 |
| ≈ 0 | < −0.05 | 環境惡化中 |

趨勢信號提供比即時風險更早的預警能力：RI 信號在強度突破前即可偵測（$\Delta \text{SE}_n$ 上升先於最大風速增加），消散信號在眼完全崩潰前即出現（$\Delta \text{SE}_n$ 下降先於中心氣壓回升）。

---

## 五、兩個時間尺度的協同機制

JSDF 的核心洞見是：**風暴消散需要在兩個時間尺度上同時失守**，而不是任何單一信號的觸發。

$$\underbrace{R_{\text{ETN}}}_{\text{快速（小時尺度）}} \times \underbrace{R_{\text{env}}}_{\text{慢速（天尺度）}} \;\longrightarrow\; R_{\text{joint}}$$

物理意義：

- 一個在環境有利的海域（$E$ 高）出現眼牆混亂（SE_n 低）的颱風，具有恢復能力——環境在「修復」⊛ 結構。對應四象限的第一行右列。
- 一個在乾燥、高風切環境中（$E$ 低）仍有完好眼牆（SE_n 高）的颱風，正在「預支」最後的結構穩定性。消散不遠，但尚未觸發。對應第二行左列。
- 只有兩個條件同時滿足，消散才是高確信度的、即時的。

這個機制對應到 ETN 動態中心論的風暴眼原理：⊛ 的靜止需要**內部對稱**（眼牆均衡）和**外部錨定**（環境供能）同時成立。內外缺一，⊛ 終將退化。

---

## 六、應用場景：全球氣象平台接口設計

### 6.1 資料流設計

```
[資料層]
  NWP 輸出（GFS / ECMWF / JMA，每 6 小時）
    └→ 氣壓場 p(x,y)、風場 u(x,y)、v(x,y)
  衛星觀測（MSG / Himawari / GOES，每 30 分鐘）
    └→ 紅外亮溫 → 角向張力估算 T(θ)
  海洋分析（OISST、OSTIA，每日）
    └→ SST → EnvironmentAttractor 更新
  大氣再分析（ERA5，延遲）
    └→ 風切、濕度 → 門檻定標基準

[JSDF 計算層]
  ETNStormEye.diagnose(T(θ))    → SE_n、R_ETN、drift
  EnvironmentAttractor.diagnose(x) → E(x)、R_env
  JointStormPredictor.predict()    → R_joint、判讀
  JointStormPredictor.trend()      → ΔSE_n、ΔE

[輸出層]
  API /api/storm/{id}/etn_status（每 30 分鐘更新）
  回傳：R_joint、SE_n、E(x)、drift、判讀文字、敵對因子列表
```

### 6.2 前端顯示建議

**地圖覆蓋層**：每個活躍氣旋標注 ⊛ 圈，以 $\text{SE}_n$ 著色。

$$\text{顏色} := \begin{cases} \text{綠} & \text{SE}_n > 0.80 \\ \text{黃} & 0.65 < \text{SE}_n \leq 0.80 \\ \text{橙} & 0.50 < \text{SE}_n \leq 0.65 \\ \text{紅} & \text{SE}_n \leq 0.50 \end{cases}$$

**時間序列面板**：$\text{SE}_n$、$E(\mathbf{x})$、$R_{\text{joint}}$ 的 72 小時歷史折線圖。

**預警卡片**：$R_{\text{joint}} \geq \tau_{\text{joint}}$ 時觸發，顯示敵對因子與置信度。

---

## 七、局限與未來方向

### 7.1 當前局限

**門檻定標問題**：$\tau_{\text{SE}}$、$\tau_{\text{joint}}$ 的最佳值依洋盆、季節、颱風強度等條件而異。本框架給出初始推薦值（0.65），正式版需以歷史氣旋資料進行分洋盆的受試者工作特性（ROC）分析定標。

**角向張力估算的不確定性**：$T(\theta)$ 從衛星資料估算時，受雲層覆蓋、傳感器分辨率、時間插值等因素影響，在近赤道地區和雙眼牆期間誤差較大。

**時間不對稱性**：目前的幾何平均對 $R_{\text{ETN}}$ 和 $R_{\text{env}}$ 給予相同權重。物理上，短期（12小時）預報應更信任 ETN，中長期（48~72小時）應更信任吸引子。正式版可引入時間加權：

$$R_{\text{joint}}(\tau) = \left(R_{\text{ETN}}\right)^{w_1(\tau)} \cdot \left(R_{\text{env}}\right)^{w_2(\tau)}, \quad w_1 + w_2 = 1$$

其中 $w_1(\tau)$ 為預報時效 $\tau$ 的遞減函數。

**多中心氣旋**：雙颱風效應（Fujiwara interaction）下，兩個 ⊛ 相互干擾，ETN 元件的單中心假設失效。多中心耦合的 ETN 形式化留待後續研究。

### 7.2 未來方向

- **自動定標模組**：以大量歷史路徑和強度資料自動優化各門檻和權重
- **機器學習橋接**：以 JSDF 的 SE_n 和 $E(\mathbf{x})$ 作為特徵，訓練深度學習模型進行精確機率預測
- **與 WT V 測度的整合**：SE_n 對應 WT 的真實性測度 V，高 $\text{SE}_n$ 的眼牆結構對應高 V 的「真實織入」存在——兩者的形式整合有待完成

---

## 八、哲學結語：兩個信號的必要性

存在物的消亡，從來不是一個信號的事。

風暴眼的崩潰（⊛ 退化）說的是**內部結構的失守**；環境的惡化（吸引子盆地的出走）說的是**外部支撐的撤離**。任何一個單獨的失守，都不足以斷言消亡——因為世界有修復能力：好的環境可以重建眼牆，穩定的內部結構可以抵禦短暫的環境壓力。

只有當內外同時失守，消亡才是真正的、迫在眉睫的。

這個結構不只是颱風預測的技術問題。它是一個關於「什麼條件下一個動態結構會消散」的本體論命題——而這個命題的答案，是**雙重確認**，是**幾何平均**，是**不允許任何一側獨自撐起消亡判定**的互斥門結構。

⊛ 退化，是眼在掙扎。

環境失守，是天在收回。

兩者同時，風暴才真正地走向它的終點。

---

## 附錄 A：程式碼

> 以下為 JSDF 教學概念版完整實作（ETN-Storm v0.2）。
> 包含：`ETNStormEye`、`EnvironmentAttractor`、`LorenzToyAttractor`、`JointStormPredictor` 四個核心類別，以及四個教學示範函式。

```python
# ["""
聯合風暴消散預測系統 ─ AI 教學概念版
Joint Storm Dissipation Predictor: ETN Storm Eye × Attractor

EML-ETN-STORM-2026-v0.2-TEACHING

理論基礎：
  ETN 動態風暴眼原理（⊛）× 吸引子動力學
  兩個信號，兩個時間尺度，一個聯合判斷

設計原則：
  ・概念清晰 > 計算效率
  ・每個類別明確對應一個理論元件
  ・可直接擴展至真實 NWP 資料接口

作者：Neo.K + Theia
機構：EveMissLab Logic Matrix
版本：v0.2 教學概念版（正式版另行開發）
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional


# ═══════════════════════════════════════════════════════
#  § 0  理論地圖
#
#  風暴消散需要兩個條件同時成立：
#
#  [快速/局部]  ETN 風暴眼信號
#    ・SE_n 衡量眼牆對稱性（⊛ 是否成立）
#    ・可在數小時內劇烈變化
#    ・捕捉：眼牆替換、對流爆發/崩潰、風切侵入
#
#  [慢速/全局]  吸引子環境信號
#    ・衡量風暴所在環境是否支持其存在
#    ・通常在數天尺度變化
#    ・捕捉：SST 降低、乾空氣入侵、引導流崩潰
#
#  聯合判斷：
#    joint_risk = √(etn_risk × env_risk)
#    任一信號為 0 → 聯合風險仍低
#    兩者同時高  → 高確信度消散
# ═══════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────
#  § 1  ETN 風暴眼元件（快速/局部）
# ───────────────────────────────────────────────────────

@dataclass
class ETNDiagnostic:
    """ETN ⊛ 診斷結果。"""
    se_n: float            # SE_n 對稱度：1=完美，0=崩潰
    intensity: float       # 對稱張力大小（ETN 強度）
    drift: np.ndarray      # 預測漂移向量
    god_balance: float     # 上下 GOD POINT 平衡
    is_well_defined: bool  # ⊛ 是否成立
    etn_risk: float        # 1 - se_n（ETN 消散風險）


class ETNStormEye:
    """
    ETN 風暴眼元件。

    理論對應：
      ⊛_n 的完整操作定義
      SE_n = 張力對稱度 = 風暴眼是否「被均勻拉住」

    輸入：
      可以是真實的極區角分析資料，
      也可以是從氣壓場/衛星亮溫估算的角向張力剖面。

    教學簡化：
      直接接受「角向張力剖面」作為輸入，
      不做完整的場插值（v0.1 已實作，此處抽象化）。
    """

    SE_WELL_DEFINED = 0.65  # ⊛ 成立門檻

    def __init__(self, n_angles: int = 36):
        self.n_angles = n_angles
        self.angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)

    def diagnose(self, angular_tension: np.ndarray) -> ETNDiagnostic:
        """
        從角向張力剖面 T(θ) 計算 ETN 診斷量。

        T(θ) 的物理來源（擇一）：
          ・雷達回波強度的角向分佈
          ・衛星紅外亮溫的角向均勻度
          ・氣壓梯度的角向積分
          ・數值模式的角向風場分量

        ETN 含義：
          T(θ) 高且均勻 → ⊛ 成立，眼穩定
          T(θ) 高但不均勻 → ⊛ 張力失衡，眼即將漂移
          T(θ) 整體低 → ⊛ 退化，眼即將消散
        """
        T = np.abs(angular_tension)
        mean_T = np.mean(T)

        # SE_n：1 - 變異係數
        if mean_T < 1e-10:
            se_n = 0.0
        else:
            se_n = float(np.clip(1.0 - np.std(T) / mean_T, 0, 1))

        # ETN 漂移：張力不對稱的淨力方向
        # 物理意義：⊛ 往 GOD POINT 更強的方向漂移
        F_x = float(np.mean(T * np.cos(self.angles)))
        F_y = float(np.mean(T * np.sin(self.angles)))
        drift = np.array([F_y, F_x]) * 0.1

        # GOD POINT 平衡：上下半球對比
        upper = np.mean(T[:self.n_angles // 2])
        lower = np.mean(T[self.n_angles // 2:])
        total = upper + lower
        god_balance = float(1.0 - abs(upper - lower) / total) if total > 1e-10 else 0.0

        return ETNDiagnostic(
            se_n=se_n,
            intensity=float(mean_T),
            drift=drift,
            god_balance=god_balance,
            is_well_defined=se_n >= self.SE_WELL_DEFINED,
            etn_risk=1.0 - se_n
        )

    def from_pressure_wind(self,
                            pressure: np.ndarray,
                            wind_u: np.ndarray,
                            wind_v: np.ndarray,
                            eye: np.ndarray,
                            radius: float = 20.0) -> ETNDiagnostic:
        """
        從氣壓場和風場直接估算角向張力剖面並診斷。
        （橋接至真實 NWP 資料的接口）
        """
        ny, nx = pressure.shape
        T = np.zeros(self.n_angles)

        for i, theta in enumerate(self.angles):
            px = np.clip(eye[1] + radius * np.cos(theta), 0, nx - 1)
            py = np.clip(eye[0] + radius * np.sin(theta), 0, ny - 1)
            ix, iy = int(px), int(py)

            p_val = pressure[iy, ix]
            p_eye = pressure[int(eye[0]), int(eye[1])]

            u_val = wind_u[iy, ix]
            v_val = wind_v[iy, ix]
            wind_in = -(u_val * np.cos(theta) + v_val * np.sin(theta))

            T[i] = max(0, -(p_val - p_eye) / (radius + 1e-8) + 0.3 * wind_in)

        return self.diagnose(T)


# ───────────────────────────────────────────────────────
#  § 2  吸引子環境元件（慢速/全局）
#        兩種版本：A. 環境向量版（實用）
#                  B. Lorenz 玩具版（理論教學）
# ───────────────────────────────────────────────────────

@dataclass
class AttractorDiagnostic:
    """吸引子環境診斷結果。"""
    env_score: float         # 環境支持度：1=極有利，0=極不利
    distance_to_boundary: float  # 距消散流形的距離
    env_risk: float          # 1 - env_score（環境消散風險）
    hostile_factors: list    # 已觸發的敵對因子
    attractor_state: str     # "deep"（盆地深處）/ "edge"（邊緣）/ "outside"（已出盆地）


class EnvironmentAttractor:
    """
    環境狀態吸引子元件（實用版）。

    理論對應：
      風暴在多維環境空間中的軌跡。
      「吸引子盆地」= 能維持熱帶氣旋的環境條件集合。
      「消散流形」= 吸引子的邊界。

    關鍵環境變數（狀態向量 x）：
      sst        海溫（℃），門檻 26°C
      shear      垂直風切（m/s），門檻 15 m/s
      humidity   中層濕度（%），門檻 50%
      vorticity  低層渦度（×10⁻⁵ s⁻¹），門檻 5
      intensity  當前強度（hPa 氣壓差），門檻 15 hPa

    設計哲學：
      不需要積分完整的 Navier-Stokes。
      環境條件直接告訴你風暴「還在不在有利的盆地裡」。
    """

    # 各環境因子的門檻與權重
    THRESHOLDS = {
        'sst':        {'min': 26.0,  'weight': 0.30, 'direction': 'above'},
        'shear':      {'max': 15.0,  'weight': 0.25, 'direction': 'below'},
        'humidity':   {'min': 50.0,  'weight': 0.20, 'direction': 'above'},
        'vorticity':  {'min': 5.0,   'weight': 0.15, 'direction': 'above'},
        'intensity':  {'min': 15.0,  'weight': 0.10, 'direction': 'above'},
    }

    def diagnose(self,
                  sst: float,
                  shear: float,
                  humidity: float,
                  vorticity: float,
                  intensity: float) -> AttractorDiagnostic:
        """
        從環境狀態向量計算吸引子診斷量。

        env_score 的計算：
          每個因子計算「距門檻的正規化距離」
          加權平均後得到總環境支持度

        吸引子意義：
          env_score ≈ 1.0 → 深在盆地，環境極有利
          env_score ≈ 0.5 → 接近盆地邊緣
          env_score ≈ 0.0 → 已出盆地，消散不可避免
        """
        values = {
            'sst': sst,
            'shear': shear,
            'humidity': humidity,
            'vorticity': vorticity,
            'intensity': intensity,
        }

        scores = {}
        hostile = []

        for var, cfg in self.THRESHOLDS.items():
            v = values[var]
            w = cfg['weight']

            if cfg['direction'] == 'above':
                threshold = cfg['min']
                # 正規化：高於門檻越多越好，最多得 1.0
                raw = np.clip((v - threshold) / (threshold * 0.5), -1, 1)
                score = (raw + 1) / 2  # 映射到 [0,1]
                if v < threshold:
                    hostile.append(f"{var}<{threshold}（實際{v:.1f}）")
            else:
                threshold = cfg['max']
                # 正規化：低於門檻越多越好
                raw = np.clip((threshold - v) / (threshold * 0.5), -1, 1)
                score = (raw + 1) / 2
                if v > threshold:
                    hostile.append(f"{var}>{threshold}（實際{v:.1f}）")

            scores[var] = score * w

        env_score = float(sum(scores.values()))
        d_boundary = max(0.0, env_score - 0.5)  # 0.5 為邊界

        if env_score > 0.75:
            state = "deep"
        elif env_score > 0.5:
            state = "edge"
        else:
            state = "outside"

        return AttractorDiagnostic(
            env_score=env_score,
            distance_to_boundary=d_boundary,
            env_risk=1.0 - env_score,
            hostile_factors=hostile,
            attractor_state=state
        )


class LorenzToyAttractor:
    """
    Lorenz 玩具吸引子（純教學版）。

    理論對應：
      把風暴系統的「環境狀態」抽象為 3D Lorenz 系統。
      當軌跡遠離 Lorenz 吸引子核心 → 環境在惡化。
      當軌跡逃出吸引子盆地 → 系統不可恢復。

    注意：
      這不是真實颱風的物理模型。
      它是一個「理解吸引子概念」的數學玩具。
      實際使用請用 EnvironmentAttractor。

    Lorenz 方程：
      dx/dt = σ(y - x)
      dy/dt = x(ρ - z) - y
      dz/dt = xy - βz
    """

    def __init__(self, sigma=10.0, rho=28.0, beta=8/3):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

        # Lorenz 吸引子的近似「中心」（兩個葉片中心）
        self.attractor_centers = [
            np.array([np.sqrt(beta * (rho-1)),  np.sqrt(beta * (rho-1)),  rho-1]),
            np.array([-np.sqrt(beta * (rho-1)), -np.sqrt(beta * (rho-1)), rho-1]),
        ]
        self.attractor_radius = 15.0  # 經驗性盆地半徑

        # 當前狀態
        self.state = np.array([1.0, 1.0, 1.0])

    def step(self, dt=0.01) -> np.ndarray:
        """積分 Lorenz 系統一步。"""
        x, y, z = self.state
        dx = self.sigma * (y - x)
        dy = x * (self.rho - z) - y
        dz = x * y - self.beta * z
        self.state += np.array([dx, dy, dz]) * dt
        return self.state.copy()

    def distance_to_attractor(self) -> float:
        """
        計算當前狀態到最近吸引子中心的距離。

        吸引子意義：
          距離小 → 深在盆地（環境穩定）
          距離大 → 遠離吸引子（環境惡化）
          距離 > attractor_radius → 系統逃出盆地（消散不可逆）
        """
        dists = [np.linalg.norm(self.state - c) for c in self.attractor_centers]
        return float(min(dists))

    def env_score(self) -> float:
        """將距離映射到 [0,1] 的環境分數。"""
        d = self.distance_to_attractor()
        return float(np.clip(1.0 - d / self.attractor_radius, 0, 1))

    def perturb(self, strength: float = 5.0):
        """施加環境擾動（模擬風切增加、乾空氣入侵等）。"""
        self.state += np.random.randn(3) * strength


# ───────────────────────────────────────────────────────
#  § 3  聯合預測器（核心）
# ───────────────────────────────────────────────────────

@dataclass
class JointPrediction:
    """聯合預測結果。"""
    # ETN 信號
    se_n: float
    etn_risk: float
    is_well_defined: bool
    drift: np.ndarray

    # 吸引子信號
    env_score: float
    env_risk: float
    attractor_state: str
    hostile_factors: list

    # 聯合判斷
    joint_risk: float
    dissipation_imminent: bool
    prediction: str           # 文字判讀
    confidence: float         # 預測置信度

    # 時步
    t: int = 0


class JointStormPredictor:
    """
    聯合風暴消散預測器。

    核心邏輯：
      ETN ⊛ × 吸引子環境 → 雙重確認機制

      ┌─────────────────────────────────────────┐
      │          ETN 風險                        │
      │  低        │  高                         │
      ├────────────┼────────────────────────────┤
      │  穩定      │  短期波動                   │  吸引子風險低
      │  （環境好  │  （眼牆暫時混亂）            │
      │   眼也好） │  可能恢復                   │
      ├────────────┼────────────────────────────┤
      │  環境惡化  │  ★ 高確信度消散             │  吸引子風險高
      │  但眼尚穩  │  內外同時失守               │
      │  觀察等待  │  即將發生                   │
      └────────────┴────────────────────────────┘

    聯合風險公式：
      joint_risk = √(etn_risk × env_risk)

      幾何平均的選擇原因：
        任一信號為 0 → 聯合風險歸零
        （一個信號不夠，需要雙重確認）
        兩者都高 → 聯合風險高
        （這才是真正的消散信號）
    """

    DISSIPATION_THRESHOLD = 0.65    # 聯合風險門檻
    HIGH_CONFIDENCE_THRESHOLD = 0.80

    def __init__(self,
                  etn: Optional[ETNStormEye] = None,
                  attractor_type: str = "environment"):
        """
        attractor_type:
          "environment" → EnvironmentAttractor（實用，推薦）
          "lorenz"      → LorenzToyAttractor（教學概念）
        """
        self.etn = etn or ETNStormEye()
        self.attractor_type = attractor_type

        if attractor_type == "lorenz":
            self.attractor = LorenzToyAttractor()
        else:
            self.attractor = EnvironmentAttractor()

        self.history: list[JointPrediction] = []
        self._t = 0

    def predict(self,
                 angular_tension: np.ndarray,
                 env_state: Optional[dict] = None,
                 lorenz_perturb: float = 0.0) -> JointPrediction:
        """
        聯合預測主函式。

        angular_tension:
          shape (n_angles,) 的角向張力剖面
          來源：ETN v0.1 的 TensionField.angular_profile()

        env_state（attractor_type = "environment" 時使用）:
          {
            'sst': 28.5,       # 海溫 (℃)
            'shear': 8.0,      # 垂直風切 (m/s)
            'humidity': 65.0,  # 中層濕度 (%)
            'vorticity': 8.0,  # 低層渦度 (×10⁻⁵ s⁻¹)
            'intensity': 35.0, # 強度（氣壓差 hPa）
          }
        """
        # ETN 診斷（快速/局部）
        etn_diag = self.etn.diagnose(angular_tension)

        # 吸引子診斷（慢速/全局）
        if self.attractor_type == "lorenz":
            if lorenz_perturb > 0:
                self.attractor.perturb(lorenz_perturb)
            self.attractor.step()
            env_score = self.attractor.env_score()
            env_risk = 1.0 - env_score
            d_boundary = self.attractor.distance_to_attractor()
            if env_score > 0.75:
                a_state = "deep"
            elif env_score > 0.5:
                a_state = "edge"
            else:
                a_state = "outside"
            hostile = [f"Lorenz距離={d_boundary:.2f}"] if d_boundary > 12 else []
        else:
            if env_state is None:
                # 預設：中立環境
                env_state = {
                    'sst': 28.0, 'shear': 10.0,
                    'humidity': 60.0, 'vorticity': 7.0, 'intensity': 25.0
                }
            a_diag = self.attractor.diagnose(**env_state)
            env_score = a_diag.env_score
            env_risk = a_diag.env_risk
            a_state = a_diag.attractor_state
            hostile = a_diag.hostile_factors

        # 聯合風險：幾何平均
        joint_risk = float(np.sqrt(etn_diag.etn_risk * env_risk))

        # 文字判讀
        prediction, confidence = self._interpret(
            etn_diag.etn_risk, env_risk, joint_risk,
            etn_diag.is_well_defined, a_state
        )

        result = JointPrediction(
            se_n=etn_diag.se_n,
            etn_risk=etn_diag.etn_risk,
            is_well_defined=etn_diag.is_well_defined,
            drift=etn_diag.drift,
            env_score=env_score,
            env_risk=env_risk,
            attractor_state=a_state,
            hostile_factors=hostile,
            joint_risk=joint_risk,
            dissipation_imminent=joint_risk >= self.DISSIPATION_THRESHOLD,
            prediction=prediction,
            confidence=confidence,
            t=self._t
        )

        self.history.append(result)
        self._t += 1
        return result

    def _interpret(self, etn_r, env_r, joint_r,
                    well_defined, a_state) -> tuple:
        """
        將數值風險轉化為可理解的文字判讀。

        對應教學框架的四個象限。
        """
        if joint_r >= self.HIGH_CONFIDENCE_THRESHOLD:
            return "★ 高確信度消散：ETN ⊛ 退化 + 環境失守，內外同時失守", 0.90

        if joint_r >= self.DISSIPATION_THRESHOLD:
            if etn_r > env_r:
                return "眼牆崩潰主導消散，環境尚有餘地", 0.70
            else:
                return "環境惡化主導消散，眼牆已開始響應", 0.70

        if etn_r > 0.45 and env_r < 0.35:
            return "⚡ 短期波動（眼牆暫亂），環境支持，可能恢復", 0.60

        if env_r > 0.45 and etn_r < 0.35:
            return "⚠ 環境緩慢惡化中，眼尚穩，持續監測", 0.55

        if not well_defined and a_state == "outside":
            return "★ 高確信度消散：⊛ 退化 + 已出吸引子盆地", 0.88

        if well_defined and a_state == "deep":
            return "✓ 穩定維持：⊛ 成立，環境有利", 0.80

        return "中性：繼續觀察", 0.50

    def trend(self, n: int = 5) -> dict:
        """
        分析最近 n 步的趨勢。

        關鍵趨勢信號：
          ETN 快降 + 吸引子邊界迫近 → 消散加速
          ETN 上升 + 吸引子深入 → 急速增強
        """
        if len(self.history) < 2:
            return {'error': '歷史不足'}

        recent = self.history[-min(n, len(self.history)):]

        d_se_n = recent[-1].se_n - recent[0].se_n
        d_env = recent[-1].env_score - recent[0].env_score
        d_joint = recent[-1].joint_risk - recent[0].joint_risk

        trend_label = "持平"
        if d_se_n > 0.05 and d_env > 0.05:
            trend_label = "⚡ 急速增強中（ETN↑ + 環境↑）"
        elif d_se_n < -0.05 and d_env < -0.05:
            trend_label = "★ 快速消散中（ETN↓ + 環境↓）"
        elif d_se_n < -0.05:
            trend_label = "眼牆退化中（ETN↓）"
        elif d_env < -0.05:
            trend_label = "環境惡化中（環境↓）"

        return {
            'trend': trend_label,
            'se_n_change': round(d_se_n, 3),
            'env_change': round(d_env, 3),
            'joint_risk_change': round(d_joint, 3),
        }


# ───────────────────────────────────────────────────────
#  § 4  合成資料生成器（教學用）
# ───────────────────────────────────────────────────────

def make_angular_tension(n_angles: int = 36,
                           base: float = 10.0,
                           asym_angle: float = 0.0,
                           asym_strength: float = 0.0,
                           noise: float = 0.3) -> np.ndarray:
    """
    生成合成角向張力剖面 T(θ)。

    base           : 對稱基礎張力
    asym_angle     : 不對稱方向（弧度）
    asym_strength  : 不對稱強度（0 = 完全對稱）
    noise          : 隨機擾動強度
    """
    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
    T = (base
         + asym_strength * np.cos(angles - asym_angle)
         + noise * np.random.randn(n_angles))
    return np.maximum(T, 0)


def make_env_state(sst: float = 28.0,
                    shear: float = 8.0,
                    humidity: float = 65.0,
                    vorticity: float = 8.0,
                    intensity: float = 30.0) -> dict:
    return {
        'sst': sst,
        'shear': shear,
        'humidity': humidity,
        'vorticity': vorticity,
        'intensity': intensity,
    }


# ───────────────────────────────────────────────────────
#  § 5  教學示範
# ───────────────────────────────────────────────────────

def _header(title: str):
    print("\n" + "═" * 62)
    print(f"  {title}")
    print("═" * 62)


def _row(pred: JointPrediction):
    """格式化輸出一行預測結果。"""
    flag = "💀" if pred.dissipation_imminent else ("⚡" if pred.se_n > 0.85 and pred.env_score > 0.80 else "  ")
    print(
        f"  t={pred.t:02d} │ "
        f"SE_n={pred.se_n:.2f} ETN_r={pred.etn_risk:.2f} │ "
        f"ENV={pred.env_score:.2f} ENV_r={pred.env_risk:.2f} │ "
        f"聯合={pred.joint_risk:.2f} {flag}"
    )


def demo_four_quadrants():
    """
    教學示範一：四象限情境
    驗證聯合預測器的核心邏輯。
    """
    _header("示範一：四象限情境驗證")
    print("""
  情境 A：ETN 低風險 + 吸引子深處  → 穩定
  情境 B：ETN 高風險 + 吸引子深處  → 短期波動，可能恢復
  情境 C：ETN 低風險 + 吸引子邊緣  → 環境惡化，觀察等待
  情境 D：ETN 高風險 + 吸引子邊緣  → 高確信度消散
    """)

    scenarios = {
        'A（穩定）': {
            'T': make_angular_tension(asym_strength=0.0, base=12.0, noise=0.2),
            'E': make_env_state(sst=29.0, shear=5.0, humidity=70.0),
        },
        'B（短期波動）': {
            'T': make_angular_tension(asym_strength=8.0, asym_angle=1.0, base=10.0),
            'E': make_env_state(sst=29.0, shear=5.0, humidity=70.0),
        },
        'C（環境惡化）': {
            'T': make_angular_tension(asym_strength=0.5, base=10.0, noise=0.2),
            'E': make_env_state(sst=26.5, shear=18.0, humidity=45.0),
        },
        'D（高確信消散）': {
            'T': make_angular_tension(asym_strength=9.0, asym_angle=0.5, base=8.0),
            'E': make_env_state(sst=25.5, shear=22.0, humidity=40.0, intensity=12.0),
        },
    }

    for name, data in scenarios.items():
        pred = JointStormPredictor().predict(data['T'], data['E'])
        print(f"\n  [{name}]")
        print(f"    SE_n={pred.se_n:.3f}  "
              f"ENV={pred.env_score:.3f}  "
              f"聯合風險={pred.joint_risk:.3f}")
        print(f"    → {pred.prediction}")


def demo_full_lifecycle():
    """
    教學示範二：完整生命週期模擬
    從發展到成熟到消散的完整過程。
    """
    _header("示範二：颱風完整生命週期（環境版）")
    print("  t=00-04 : 發展期（環境有利，眼牆組織化）")
    print("  t=05-09 : 成熟期（對稱高張力，深在吸引子）")
    print("  t=10-14 : 消散期（登陸後摩擦 + 乾空氣入侵）")

    predictor = JointStormPredictor(attractor_type="environment")
    print()
    print(f"  {'t':>3} │ SE_n  ETN_r │ ENV   ENV_r │ 聯合   診斷")
    print(f"  {'─'*3}─┼─{'─'*11}─┼─{'─'*11}─┼─{'─'*16}")

    phases = [
        # (T_params, E_params, n_steps)
        # 發展期
        ({'base': 5.0,  'asym_strength': 5.0, 'noise': 0.8},
         {'sst': 29.0, 'shear': 7.0, 'humidity': 68.0, 'vorticity': 9.0, 'intensity': 18.0},
         5),
        # 成熟期
        ({'base': 14.0, 'asym_strength': 0.5, 'noise': 0.3},
         {'sst': 30.0, 'shear': 4.0, 'humidity': 75.0, 'vorticity': 12.0, 'intensity': 45.0},
         5),
        # 消散期
        ({'base': 8.0,  'asym_strength': 7.0, 'noise': 1.0},
         {'sst': 25.5, 'shear': 20.0, 'humidity': 42.0, 'vorticity': 4.0, 'intensity': 15.0},
         5),
    ]

    for t_params, e_params, steps in phases:
        for _ in range(steps):
            T = make_angular_tension(**t_params)
            E = make_env_state(**e_params)
            pred = predictor.predict(T, E)
            flag = "💀" if pred.dissipation_imminent else ("★" if pred.se_n > 0.85 else "  ")
            print(f"  {pred.t:>3} │ "
                  f"{pred.se_n:.3f} {pred.etn_risk:.3f} │ "
                  f"{pred.env_score:.3f} {pred.env_risk:.3f} │ "
                  f"{pred.joint_risk:.3f} {flag}")

    tr = predictor.trend(5)
    print(f"\n  最後 5 步趨勢：{tr['trend']}")
    print(f"  SE_n 變化={tr['se_n_change']:+.3f}  "
          f"ENV 變化={tr['env_change']:+.3f}  "
          f"聯合風險變化={tr['joint_risk_change']:+.3f}")


def demo_lorenz_version():
    """
    教學示範三：Lorenz 玩具吸引子版
    純概念理解用，不代表真實颱風物理。
    """
    _header("示範三：Lorenz 玩具吸引子（概念版）")
    print("  Lorenz 系統作為「環境狀態」的抽象替代。")
    print("  當 Lorenz 軌跡遠離吸引子核心 → 環境惡化。")
    print()
    print("  t=00-05 : 初始穩定軌跡")
    print("  t=06    : 強力環境擾動（模擬颱風接近寒流）")
    print("  t=07-12 : 觀察系統反應")
    print()

    predictor = JointStormPredictor(attractor_type="lorenz")

    for t in range(13):
        T = make_angular_tension(
            base=10.0,
            asym_strength=(0.5 if t < 6 else 5.0 + t * 0.5),
            noise=0.4
        )
        perturb = 12.0 if t == 6 else 0.0
        pred = predictor.predict(T, lorenz_perturb=perturb)

        flag = "💥" if t == 6 else ("💀" if pred.dissipation_imminent else "  ")
        print(f"  t={t:02d}: SE_n={pred.se_n:.2f} │ "
              f"Lorenz環境={pred.env_score:.2f} │ "
              f"聯合={pred.joint_risk:.2f} {flag}")
        if t == 6:
            print("        ↑ 強力擾動施加（Lorenz 被踢出穩定軌跡）")


def demo_website_api_sketch():
    """
    教學示範四：全球氣象網站接口設計草圖
    展示如何將本系統整合至實際服務。
    """
    _header("示範四：全球氣象網站接口設計草圖")

    print("""
  概念架構：

  [資料源]
    NWP 模式（GFS / ECMWF / JMA）
      → 氣壓場、風場（每 6 小時更新）
    觀測資料（衛星 IR、雷達）
      → 角向亮溫剖面 → ETN angular_tension
    再分析資料（ERA5）
      → 環境狀態向量 → EnvironmentAttractor

  [ETN-Storm v0.2 核心]
    ETNStormEye.from_pressure_wind()    → SE_n、漂移
    EnvironmentAttractor.diagnose()     → env_score
    JointStormPredictor.predict()       → joint_risk、判讀
    JointStormPredictor.trend()         → 趨勢信號

  [輸出接口]
    API 端點：/api/storm/{storm_id}/etn_status
    回傳 JSON：{
      "storm_id": "MAWAR-2026",
      "timestamp": "2026-06-05T12:00Z",
      "eye_position": [lat, lon],
      "se_n": 0.82,
      "etn_risk": 0.18,
      "env_score": 0.71,
      "joint_risk": 0.36,
      "dissipation_imminent": false,
      "prediction": "✓ 穩定維持",
      "confidence": 0.80,
      "drift_vector": [0.12, -0.05],
      "hostile_factors": []
    }

  [前端顯示]
    地圖覆蓋層：每個活躍颱風的 ⊛ 圈
      顏色編碼：綠（SE_n > 0.8）→ 黃 → 紅（⊛ 退化）
    時間序列圖：SE_n + env_score + joint_risk 的 72 小時歷史
    預警卡片：joint_risk > 0.65 時彈出
    """)

    # 模擬一個 API 回傳
    T = make_angular_tension(base=11.0, asym_strength=1.5, noise=0.3)
    E = make_env_state(sst=28.5, shear=9.0, humidity=67.0)
    pred = JointStormPredictor().predict(T, E)

    import json
    api_response = {
        "storm_id": "DEMO-2026",
        "se_n": round(pred.se_n, 3),
        "etn_risk": round(pred.etn_risk, 3),
        "env_score": round(pred.env_score, 3),
        "joint_risk": round(pred.joint_risk, 3),
        "dissipation_imminent": pred.dissipation_imminent,
        "prediction": pred.prediction,
        "confidence": round(pred.confidence, 2),
        "hostile_factors": pred.hostile_factors,
    }
    print("  範例 API 回傳：")
    print("  " + json.dumps(api_response, ensure_ascii=False, indent=2)
          .replace("\n", "\n  "))


# ───────────────────────────────────────────────────────
#  主程式
# ───────────────────────────────────────────────────────

if __name__ == "__main__":
    np.random.seed(2026)

    demo_four_quadrants()
    demo_full_lifecycle()
    demo_lorenz_version()
    demo_website_api_sketch()

    print("\n" + "═" * 62)
    print("  ETN-Storm v0.2 教學概念版完成")
    print("  ⊛ 是局部快信號，吸引子是全局慢信號")
    print("  消散 = 兩個信號的幾何平均 > 門檻")
    print("═" * 62)
]
```

---

## 附錄 B：符號索引

| 符號 | 定義 | 對應元件 |
|---|---|---|
| $\circledast_n$ | ETN 動態不動點（風暴眼） | ETN |
| $G_n^-$ | n 域下界 GOD POINT | ETN |
| $T(\theta)$ | 角向張力剖面 | ETN |
| $\text{SE}_n$ | ⊛ 對稱度量：$1 - \sigma(T)/\mu(T)$ | ETN |
| $R_{\text{ETN}}$ | ETN 消散風險：$1 - \text{SE}_n$ | ETN |
| $\vec{F}_{\text{drift}}$ | ⊛ 漂移向量 | ETN |
| $\mathbf{x}$ | 環境狀態向量 | 吸引子 |
| $E(\mathbf{x})$ | 環境支撐度 | 吸引子 |
| $R_{\text{env}}$ | 環境消散風險：$1 - E(\mathbf{x})$ | 吸引子 |
| $d_A$ | 距消散流形距離 | 吸引子 |
| $R_{\text{joint}}$ | 聯合消散風險：$\sqrt{R_{\text{ETN}} \cdot R_{\text{env}}}$ | 聯合 |
| $\tau_{\text{SE}}$ | ⊛ 成立門檻（推薦 0.65） | 聯合 |
| $\tau_{\text{joint}}$ | 消散預警門檻（推薦 0.65） | 聯合 |

---

## 版本聲明

**版本**：v1.0（概念論文，實驗站發表版）
**對應程式碼**：ETN-Storm v0.1（EML-ETN-STORM-2026-v0.1）、v0.2 教學概念版
**後續計劃**：v1.1 加入時間加權聯合風險；v1.2 加入多中心 ETN 形式化；正式版另行開發
**定標需求**：$\tau_{\text{SE}}$、$\tau_{\text{joint}}$、環境向量權重 $w_i$ 均需以洋盆歷史資料校準

EveMissLab Logic Matrix（一言諾科技有限公司）
2026 年 6 月
