# Next Node: RH Axis Notch Cover Codesign v0.5

## 判斷

不再向 $R>16$ 做無條件 support sweep。原因不是已證明所有更大支撐都
失敗，而是：

$$
\text{dual margin下降緩慢}
\quad\text{而}\quad
\text{prime cutoff}=e^{2R}
$$

使邊際成本過高。

## 核心問題

共設計 dictionary $\mathcal D$ 與 PSD Gram $A$，令五帶峰值出現
結構性 notch：

$$
\sup_{x\in A_j}H_{\mathcal D,A}(x)
$$

下降，同時維持 patch 核心

$$
\sup_{z\in P}B_{\mathcal D,A}(z)\le-1.
$$

## 第一批實驗

1. 固定 $R\in\{10.25,12,14,16\}$，不再擴張質數截斷。
2. 從本輪 witness 的 active axis supports 擷取峰值位置。
3. 對 $A_1$ 優先加入零值、導數零值或低能量 notch constraints。
4. 檢查 notch 是否只把峰移到 $A_0,A_2$ 或帶邊界。
5. 用 adaptive maximizer 取代固定 $0.25$ grid。
6. 只有安全 dual bound 未達 $1$ 的 patch 才啟動 primal Gram。
7. 對 primal 候選做 dense core、guard ring、dense axis 與 basis
   perturbation audit。

## 成功條件

至少一個目前 blocked patch 同時滿足：

$$
\alpha_{\mathrm{safe}}<1,
$$

以及一個經 dense audit 的 primal 候選：

$$
J(A)<1,\qquad
\max_{z\in P}B_A(z)\le-1.
$$

這仍只是有限模型成功，不是 RH 證書。

## 停止條件

若 notch：

- 將峰移到鄰帶而不降低總 charge；
- 使核心負向消失；
- 只在粗網格有效；
- 或需要顯著增加 $R$ 才生效，

便停止目前 polynomial-bump dictionary family，改研究解析 kernel
family 或可 interval-evaluate 的 extremal construction。

