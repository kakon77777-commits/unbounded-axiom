# 補充論文 S2：刺激不是一條軸——ADHD 的刺激偏好向量與風險分離假說

**英文題名：** Stimulation Is Not One Axis: A Multidimensional Preference and Risk-Separation Hypothesis for ADHD  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論建模／認知動機研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 0. 邊界聲明

本文不是臨床研究、診斷工具或醫療建議。本文不主張 ADHD 個體都追求刺激、風險或新奇，也不主張任何刺激偏好可用來診斷 ADHD。

本文最核心的修正是：

$$
\boxed{
\text{stimulation seeking}
\neq
\text{risk seeking}
\neq
\text{sensory-intensity seeking}.
}
$$

---

## 摘要

ADHD 常被口語簡化為「需要刺激」或「追求刺激」，但「刺激」本身不是單一物理量。新穎資訊、認知複雜度、快速回饋、社會競爭、感官強度、結果不確定性、控制感與身體危險都可以帶來 arousal 或 engagement，卻具有完全不同的效用與成本。

現有文獻支持這種拆分。reward、novelty、delay aversion 與 boredom 是彼此相關但不等同的研究路徑；2026 年研究開始直接檢查 curiosity 與 ADHD traits。2025 年青少年 ADHD risk-taking 研究更發現，ADHD 組較高的是 prosocial risk-taking，而 negative 與 positive risk-taking 並未同樣出現 group difference，直接提醒「risk」本身就有不同類型。2026 年成人 risk-taking 研究也持續指出 ADHD characteristics 與不同 risk domains 的關係並不一致。

本文提出「Multidimensional Stimulation Preference Hypothesis, MSPH」。對活動 $a$ 定義刺激向量：

$$
\mathbf s(a)
=
\left(
N,
I,
C,
F,
U,
A,
V,
Q,
X,
D
\right),
$$

其中分別表示 novelty、information gain、cognitive complexity、feedback speed、uncertainty、agency、sensory intensity、social competition、physical risk 與 delay structure。

個體偏好為：

$$
\mathbf w_i.
$$

成本敏感度為：

$$
\mathbf r_i.
$$

則活動效用：

$$
U_i(a)
=
\mathbf w_i^\top \mathbf s(a)
-
\mathbf r_i^\top \mathbf c(a).
$$

因此一個人可以高度偏好 cognitive novelty 而強烈厭惡 physical risk；可以喜歡遊戲的探索、策略與系統深度，而不特別偏好高 sensory intensity。這不是例外，而是多維偏好模型的自然結果。

---

## 1. 「刺激」至少包含十個不同維度

本文候選：

$$
\mathbf s(a)
=
(
N,I,C,F,U,A,V,Q,X,D
).
$$

### $N$：Novelty

新東西、新規則、新問題。

### $I$：Information Gain

每單位時間獲得多少新資訊。

### $C$：Cognitive Complexity

是否需要建模、推理、策略。

### $F$：Feedback Speed

行動到結果之間多久得到回饋。

### $U$：Uncertainty

結果是否未知。

### $A$：Agency

是否由本人控制、選擇、探索。

### $V$：Sensory Intensity

聲光、速度、震動、畫面刺激。

### $Q$：Social Competition

勝負、排名、即時他人回饋。

### $X$：Physical Risk

受傷、死亡、失控的真實身體風險。

### $D$：Delay Structure

獎勵或結果是否延遲。

---

## 2. Sensation Seeking 不等於 Novelty Seeking

高：

$$
V
$$

與高：

$$
N
$$

可以分離。

理論研究可能：

$$
N,I,C,U\uparrow,
$$

但：

$$
V\approx0.
$$

極限運動則可能：

$$
N,V,X\uparrow.
$$

兩者不能只用「刺激高」表示。

---

## 3. Novelty 不等於 Risk

若新奇活動：

$$
X\approx0,
$$

仍可以：

$$
N\uparrow.
$$

例如：

- 新數學問題；
- 新遊戲系統；
- 新化學反應；
- 新語言；
- 新資料集。

因此：

$$
\boxed{
N\uparrow
\not\Rightarrow
X\uparrow.
}
$$

---

## 4. Risk 本身也不是一種

2025 adolescent ADHD study 將 risk 分成：

$$
R^{-}
=
\text{negative risk},
$$

$$
R^{+}
=
\text{positive risk},
$$

$$
R^{P}
=
\text{prosocial risk}.
$$

ADHD 組較高的是：

$$
R^{P},
$$

而 negative／positive risk 並未都出現 group difference。

因此：

$$
\boxed{
\text{risk-taking}
\neq
\text{one latent behavior}.
}
$$

---

## 5. Reward 與 Delay 要分開

一個活動可以：

$$
R_{\text{reward}}\uparrow
$$

但：

$$
D_{\text{delay}}\uparrow.
$$

例如完成一篇論文的價值很高，但回饋很晚。

ADHD delay-aversion literature 的重要之處在於：

$$
\boxed{
\text{reward value}
\neq
\text{delay cost}.
}
$$

---

## 6. Boredom 不是「刺激量不足」這麼簡單

2026 boredom–ADHD meta-analysis 得到約：

$$
r\approx0.40
$$

的 aggregate association。

但 boredom 可以由：

- low information gain；
- low agency；
- repetitive predictability；
- task mismatch；
- inability to engage attention；

形成。

因此：

$$
B
=
F
\left(
N,I,A,C,F,\text{state}
\right),
$$

而不是：

$$
B
=
-\text{stimulation scalar}.
$$

---

## 7. Curiosity 提供新的研究入口

2026 研究開始直接檢驗 ADHD traits 與 curiosity。

若 curiosity 是：

$$
\text{information-seeking drive},
$$

它與：

$$
\text{physical thrill seeking}
$$

不是同一構念。

這正是 MSPH 需要的分離。

---

## 8. 個體刺激權重

定義：

$$
\mathbf w_i
=
(w_N,w_I,w_C,w_F,w_U,w_A,w_V,w_Q,w_X,w_D).
$$

兩個人都可被描述為「喜歡刺激」，但：

$$
\mathbf w_i
\neq
\mathbf w_j.
$$

例如：

$$
w_N,w_I,w_C\gg0,
$$

但：

$$
w_X\ll0.
$$

是一個完全合法的 profile。

---

## 9. 成本向量

活動也有：

$$
\mathbf c(a)
=
(
C_{\text{threat}},
C_{\text{fatigue}},
C_{\text{social}},
C_{\text{money}},
C_{\text{time}},
C_{\text{uncertainty}}
).
$$

個體成本敏感度：

$$
\mathbf r_i.
$$

因此：

$$
U_i(a)
=
\mathbf w_i^\top\mathbf s(a)
-
\mathbf r_i^\top\mathbf c(a).
$$

---

## 10. 同樣新奇，效用可以完全相反

活動 $a$：

$$
N(a)=1,
\quad
X(a)=0.
$$

活動 $b$：

$$
N(b)=1,
\quad
X(b)=1.
$$

若：

$$
r_X\gg0,
$$

則：

$$
U_i(a)\gg U_i(b).
$$

所以：

$$
\boxed{
\text{novelty preference}
+
\text{risk aversion}
}
$$

完全可以共存。

---

## 11. 遊戲也不是一種刺激

FPS 偏：

$$
V,F,Q\uparrow.
$$

策略／模擬偏：

$$
C,I,A,U\uparrow.
$$

沙盒偏：

$$
A,N,C\uparrow.
$$

探索 RPG 偏：

$$
N,I,U,A\uparrow.
$$

所以「喜歡遊戲」不能用一個 reward dimension 解釋。

---

## 12. Intellectual Stimulation

本文定義：

$$
S_{\mathrm{intellectual}}
=
f(N,I,C,U,A).
$$

可以高到：

$$
S_{\mathrm{intellectual}}\gg0
$$

同時：

$$
S_{\mathrm{sensory}}\approx0.
$$

這為長期學術研究的「刺激」提供不同於 thrill-seeking 的模型。

---

## 13. 刺激通道替換

同一人隨生命史可能：

$$
\mathbf w_i(t_1)
\neq
\mathbf w_i(t_2).
$$

或不同活動提供相似 latent utility：

$$
U_i(a)\approx U_i(b)
$$

但刺激成分不同。

因此可能：

$$
\text{physical novelty}
\rightarrow
\text{intellectual novelty}
$$

形成 channel substitution。

---

## 14. 與 ADHD 的關係應該是分布差異，而不是固定類型

本文不預測：

$$
\mathbf w_{\mathrm{ADHD}}
=
\text{one fixed vector}.
$$

更合理的是：

$$
p(\mathbf w\mid ADHD)
$$

和：

$$
p(\mathbf w\mid control)
$$

可能在部分維度有不同密度，但高度重疊。

因此：

$$
\boxed{
\text{ADHD-related preference shift}
\neq
\text{ADHD-specific stimulation type}.
}
$$

---

## 15. MSPH 可證偽命題

**ST-H1：** novelty、sensory intensity、physical risk、information gain 可在 factor／behavioral level 分離。  
**ST-H2：** ADHD-related traits 對不同 stimulation dimensions 的效應不同。  
**ST-H3：** risk preference 會因 risk domain 改變。  
**ST-H4：** boredom 與 low novelty 相關，但不是由 novelty 單一解釋。  
**ST-H5：** 若單一 sensation-seeking scalar 已能完整預測活動偏好，多維模型應被簡化。

---

## 16. 實驗綱領

建立正交刺激任務：

$$
N\times V\times X\times F\times A.
$$

例如同時操弄：

- 新穎／重複；
- 高／低 sensory intensity；
- 真實風險／無風險；
- 快／慢回饋；
- 高／低 agency。

測量：

$$
\text{choice},
\text{persistence},
\text{arousal},
\text{performance},
\text{subjective value}.
$$

若多維模型成立，應出現大量個體化 interaction，而不是單一「刺激越大越喜歡」。

---

## 17. 結論

「ADHD 喜歡刺激」如果不先回答：

> 喜歡哪種刺激？

幾乎沒有理論精度。

本文提出：

$$
\boxed{
\text{stimulation}
=
\text{vector},
}
$$

而不是：

$$
\text{scalar}.
$$

因此：

$$
\boxed{
\text{novelty seeking}
\neq
\text{physical risk seeking}
\neq
\text{sensory intensity seeking}
\neq
\text{information seeking}.
}
$$

真正應研究的是個體化：

$$
\mathbf w_i
$$

如何和 activity vector：

$$
\mathbf s(a)
$$

耦合。

---

## 參考文獻

1. Sethi A, et al. *A neurocomputational account of reward and novelty processing in ADHD.* 2018.  
2. Morsink S, et al. *Studying Motivation in ADHD: The Role of Internal Motives.* 2021/2022.  
3. Braams BR, van Rijn R, Leijser T, Dekkers TJ. *The Upside of ADHD-related Risk-taking: Adolescents With ADHD Report a Higher Likelihood of Engaging in Prosocial Risk-taking Behavior Than Typically Developing Adolescents.* J Atten Disord. 2025;29(10):775–786. DOI: 10.1177/10870547251321882.  
4. Fuermaier ABM, et al. *ADHD Characteristics Are Linked to Divergent Risk-Taking Behaviors.* J Atten Disord. 2026.  
5. Muris P, Otgaar H, Donkers F. *The Boredom-ADHD Nexus: A Narrative and Meta-Analytic Review of the Evidence.* Clin Child Fam Psychol Rev. 2026. DOI: 10.1007/s10567-026-00563-9.  
6. Le Cunff AL, et al. *Hyperactive–impulsive ADHD traits predict higher curiosity...* BMC Psychology. 2026.

---

**狀態：** v0.1 補充理論稿  
**新增原始臨床／人體數據：** 無
