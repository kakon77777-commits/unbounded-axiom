# Paper 01｜當 Frontier AI 基本能力逐漸成熟：從 Scaling 轉向 Cognitive Efficiency

**English Title:** *When Frontier AI Capabilities Approach Functional Maturity: From Scaling to Cognitive Efficiency*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／模型架構與認知效率研究  

---

## 摘要

大型語言模型近年的能力提升，與模型規模、訓練資料、訓練計算量、後訓練方法、推理時計算、工具使用與系統工程的共同擴張密切相關。因此，本文不提出「Scaling 已失效」或「未來不再需要更大的模型」之類命題。本文提出的是一個較弱、也較可檢驗的架構問題：當一類 Frontier AI 的基本語言、推理、工具理解、任務分解與一般問題求解能力逐步跨過可用門檻後，繼續增加總參數、每 token 激活參數與長上下文消耗，是否仍然是 Mother AI／高階協調智能的最佳邊際投資方向？

本文把這個問題稱為 **Scaling-to-Cognitive-Efficiency Transition（從規模擴張到認知效率的轉向）**。其核心並非主張模型應盡可能小，而是區分至少四種不同資源：常駐模型容量、條件激活容量、外部可取得資訊，以及任務期間動態投入的推理與驗證計算。若某些高解析度事實、案例、文件與長尾資訊可由外部檢索、資料庫與專門智能按需取得，而某些認知功能又可透過稀疏激活、專家路由或外部執行器按需展開，那麼系統設計的目標就不應只剩「把更多能力壓進單一常駐模型」。

本文承接既有「後設完備、基底稠密、表層稀疏」主 AI 命題，但把問題向模型設計層推進。本文提出 Cognitive Efficiency、Resident Cognitive Value、Externalizable Surface Burden 與 Marginal Scaling Utility 等概念，並提出六項主要命題：第一，總參數規模與有效認知效率不可等同；第二，知識容量與推理控制能力應在系統層分開評估；第三，當外部知識可低成本取得時，某些表層記憶的常駐價值會下降；第四，MoE 類稀疏激活顯示「總容量」與「當次計算」可以分離，但這不等於專家已具有乾淨的認知語義；第五，推理時計算應視為可動態配置資源，而非固定附著於最大模型；第六，Mother AI 的最佳目標可能不是最大單體模型，而是具有高認知密度、良好元認知與可調度外部能力的認知核心。

本文同時給出反例與可否證條件。若未來實驗顯示：在等總成本、等延遲、等可用外部資源下，常駐更大模型仍在幾乎所有高價值任務上穩定壓倒認知核心加外部展開架構；或者外部資訊整合與委派的驗證成本長期抵消其計算節省；或者推理、知識與世界表示無法在功能上形成任何可利用的資源分工，則本文的主要架構命題應被削弱或撤銷。

本文因此不是一篇反 scaling 論文，而是一篇 **post-scaling allocation proposition**：當 scaling 本身已創造足夠強的基礎智能之後，下一階段研究可能需要開始回答「哪些能力必須常駐、哪些只需條件激活、哪些可以外部取得，以及每一單位計算究竟應被放在哪裡」這個更細緻的問題。

**關鍵詞：** Cognitive Efficiency、Cognitive Density、Scaling Laws、Mixture of Experts、Sparse Activation、Mother AI、External Memory、Retrieval、Test-Time Compute、Expandable Intelligence

---

# 1. 問題的提出：更大仍然有用，但是否永遠是最佳答案？

大型模型的成功不能脫離 scaling 討論。更大的模型、更大的資料、更高的訓練計算與更成熟的後訓練，確實持續產生能力提升。因此本文不採取：

$$
\boxed{
\text{Scale}\uparrow
\Rightarrow
\text{Capability 不再提升}
}
$$

這種過強主張。

真正需要研究的是：

$$
\boxed{
\frac{\partial Q}{\partial C}
}
$$

其中 $Q$ 是對目標任務分布真正有價值的能力， $C$ 是總系統計算成本。

當模型能力較弱時，增加模型規模可能直接修復大量基礎缺陷，例如語言表示不足、世界模式不足、泛化不足與推理表徵不足。此時：

$$
\frac{\partial Q}{\partial C}
$$

可能非常高。

然而當模型已經跨過某些功能門檻後，新增計算可能分配到完全不同的地方：

- 增加更多長尾事實記憶；
- 增加更多領域模式；
- 增加更高解析度的表示容量；
- 增加冗餘與穩健性；
- 增加更深的推理能力；
- 增加更長的推理時間；
- 增加更多專門化專家；
- 增加工具、搜尋與外部記憶的使用能力。

這些都可能提高最終效能，但其邊際價值並不相同。

因此本文真正問的是：

> **當 Frontier AI 的一部分基本認知能力已逐漸成熟後，我們是否仍應將「更多常駐參數」視為預設的主要擴展方向？**

---

# 2. Scaling 從來就不只是參數數量

將 scaling 簡化成：

$$
N_{\mathrm{parameter}}\uparrow
$$

本來就是不完整的。

一個模型系統至少存在：

$$
\boxed{
C_{\mathrm{total}}
=
C_{\mathrm{train}}
+
C_{\mathrm{inference}}
+
C_{\mathrm{context}}
+
C_{\mathrm{retrieval}}
+
C_{\mathrm{tool}}
+
C_{\mathrm{verification}}
}
$$

其中每一項都可能交換。

Chinchilla 類 compute-optimal scaling 結果的重要意義之一，就是指出「參數越大越好」不是固定計算預算下的充分原則。模型大小與訓練 token 數需要共同分配；較小但訓練更充分的模型可以在相同訓練計算下超越更大的模型。

因此早在 dense scaling 階段，問題就已經從：

$$
\text{How large?}
$$

變成：

$$
\boxed{
\text{How should compute be allocated?}
}
$$

本文只是把這個問題再推進一步。

---

# 3. 從 Compute-Optimal 進一步問 Cognitive-Optimal

Compute-optimal training 解的是：

> 給定訓練 FLOPs，模型大小與訓練資料如何配置？

本文希望提出另一個未解問題：

> 給定整個 AI 系統長期可用的計算、記憶、網路、工具與外部模型資源，哪些能力最值得存在 Mother Model 的常駐計算核心中？

因此定義一個概念性的 Cognitive Efficiency：

$$
\boxed{
\eta_C
=
\frac{
Q_{\mathrm{reason}}
+
Q_{\mathrm{meta}}
+
Q_{\mathrm{epistemic}}
+
Q_{\mathrm{coord}}
}{
C_{\mathrm{active}}
+
C_{\mathrm{context}}
+
C_{\mathrm{verification}}
+
C_{\mathrm{latency}}
}
}
$$

其中：

- $Q_{\mathrm{reason}}$：推理與問題求解品質；
- $Q_{\mathrm{meta}}$：元認知、自我檢查、策略切換與失敗辨識；
- $Q_{\mathrm{epistemic}}$：對已知、未知、證據、衝突與不確定性的處理能力；
- $Q_{\mathrm{coord}}$：工具、模型、Agent 與計算資源的協調能力；
- $C_{\mathrm{active}}$：實際激活模型計算；
- $C_{\mathrm{context}}$：上下文處理成本；
- $C_{\mathrm{verification}}$：檢查、驗證與錯誤修復成本；
- $C_{\mathrm{latency}}$：在實際系統中不可忽略的時間成本。

此式不是現有標準 metric，也不是本文聲稱已完成量測的物理定律。它是一個研究方向：把「模型有多大」改寫為「每一單位實際成本產生多少可治理的認知能力」。

---

# 4. 知識容量與認知控制不是同一問題

Foundation Model 的一個巨大優勢，是將大量語言、事實、模式與世界規律壓縮在模型權重中。

但：

$$
\boxed{
\text{Parametric Knowledge}
\neq
\text{Reasoning Control}
}
$$

也不等於：

$$
\boxed{
\text{Metacognitive Competence}
}
$$

一個模型可以記得大量資訊，卻仍可能：

- 不知道何時自己不知道；
- 不知道哪個來源已過時；
- 無法區分證據與推測；
- 在長推理中錯誤累積；
- 無法選擇合適工具；
- 無法知道另一個模型是否更適合；
- 無法建立可靠驗證流程。

反過來，一個表層知識覆蓋較少的模型，如果具有足夠強的：

$$
\mathsf{Interpret},
\mathsf{Decompose},
\mathsf{Reason},
\mathsf{Judge},
\mathsf{Route},
\mathsf{Verify},
\mathsf{Integrate}
$$

則可能透過外部資源取得高解析度資訊。

這並不意味知識不重要，而是表示知識的**儲存位置**可以成為架構變數。

---

# 5. Parametric Memory 不再是唯一的大規模知識路徑

RETRO 類研究已經證明一個重要方向：大型外部檢索庫可以與較小的參數模型結合，在多項語言與知識型任務上取得與遠大模型相競爭的結果。

這不表示：

$$
\text{Retrieval}
=
\text{Intelligence}
$$

也不表示 RAG 可以取代基礎模型。

它真正支持的是：

$$
\boxed{
\text{所有可用知識不必全部以同一形式常駐於參數中。}
}
$$

因此可將模型可使用的知識粗分為：

$$
K
=
K_{\mathrm{parametric}}
\oplus
K_{\mathrm{external}}
\oplus
K_{\mathrm{task}}
$$

其中：

- $K_{\mathrm{parametric}}$：模型權重與內部表示中的長期知識；
- $K_{\mathrm{external}}$：網路、文件庫、資料庫、知識圖與外部記憶；
- $K_{\mathrm{task}}$：當前任務經檢索、編譯、驗證後形成的暫時高解析度工作知識。

本文系列後續將專門處理：

$$
K_{\mathrm{external}}
\rightarrow
K_{\mathrm{task}}
$$

為什麼不是普通 retrieval 就能解決。

---

# 6. MoE 已經把「總容量」與「每次激活」拆開

稀疏 Mixture-of-Experts 的出現提供另一個關鍵訊號。

一般 dense model 在每次 forward pass 中會使用大部分相同的參數結構，而 sparse MoE 則透過 router 對 token 選擇少數 experts：

$$
\boxed{
E_{\mathrm{active}}(x)
\subset
E_{\mathrm{total}}
}
$$

因此：

$$
P_{\mathrm{total}}
\gg
P_{\mathrm{active}}
$$

可以同時成立。

Switch Transformer 已系統性展示稀疏模型可以在不讓每次計算成本與總參數同步上升的情況下擴張模型容量。後來的 DeepSeek-V3 與 Qwen3 等架構又把這條路推到更實際的大型模型：總參數可達數百億至數千億，而每 token 激活量只占其中一部分。

這件事情的理論意義不只是「MoE 比較省」。

它等於承認：

$$
\boxed{
\text{一個智能系統擁有的總能力容量，不必在每次認知操作中全部啟動。}
}
$$

但本文同時強調：

$$
\boxed{
\text{MoE Expert}
\neq
\text{乾淨的認知功能模組}
}
$$

Expert activation 可能是分散、糾纏、上下文相依的。某個 expert 常在一類任務被路由，不代表它就是該能力的唯一因果來源。

因此 MoE 在本系列首先被視為：

> **一個條件計算已經可行的證據，以及一個未來研究能力分工的觀察入口。**

而不是已完成的「認知器官分離」。

---

# 7. Test-Time Compute 又把另一部分計算變成動態資源

如果模型每個問題都固定使用同樣長度的推理與同樣大的計算，就會浪費任務難度差異。

近年的 test-time scaling 研究顯示，對某些問題，較小模型配合更有效的推理時計算與搜尋，可以在 FLOPs-matched 條件下超越遠大的模型；同時，其收益又高度依賴問題難度與推理策略。

這意味：

$$
\boxed{
C_{\mathrm{reasoning}}
}
$$

也不必完全固化成「模型越大，每 token 永遠越貴」。

可以存在：

$$
C_{\mathrm{test}}(T)
$$

使不同任務得到不同計算預算。

於是總系統逐漸出現三種不同 scaling 軸：

$$
\boxed{
\text{Resident Capacity}
}
$$

$$
\boxed{
\text{Conditional Capacity}
}
$$

$$
\boxed{
\text{Dynamic Deliberation}
}
$$

再加上：

$$
\boxed{
\text{External Knowledge / Tools}
}
$$

此時「最大單模型」只是可用設計空間中的一個點。

---

# 8. Functional Maturity：本文不是宣告 AGI 已完成

本文使用「基本能力逐漸成熟」時，必須避免概念誤讀。

這裡的 maturity 不表示：

- AI 已經具有完美推理；
- 所有領域都已成熟；
- 幻覺已解決；
- 長期自主 Agent 已成熟；
- AI 已達到 AGI 的任何唯一標準；
- scaling 不再有能力收益。

本文定義的是任務相對的 Functional Maturity Threshold：

$$
\boxed{
\operatorname{FM}(M,\mathcal T)
\ge
\theta_{\mathcal T}
}
$$

意思是：對某類任務分布 $\mathcal T$，模型已經具有足以讓系統開始將主要工程問題從「它到底會不會」轉成「如何更便宜、更穩定、更可驗證地使用它」的能力。

例如一個 bounded coding worker 若已能在清楚規格與機械 verifier 下穩定產生可接受 candidate，則該工作類型的主要優化問題可能不再是：

> 再換一個大十倍的模型能不能多提高幾分？

而是：

> 如何降低總成本、提高並行度、提高驗證可信度、選擇何時升級到更強模型？

因此 Functional Maturity 是**局部、任務相對、可撤銷**的。

---

# 9. Mother AI 的目標函數可能與通用聊天模型不同

通用 Foundation Model 希望：

$$
\mathcal T_{\mathrm{general}}
$$

盡可能廣。

它需要面對無法預測的使用者問題，因此高知識覆蓋具有很高價值。

但 Mother AI／Cognitive Command Tower 的角色不同。

它的主要工作可能更接近：

$$
\mathcal T_M
=
\{
\text{interpret},
\text{decompose},
\text{judge},
\text{route},
\text{verify},
\text{integrate},
\text{govern}
\}.
$$

因此 Mother Model 的最佳訓練與部署目標不必等於：

$$
\max
\operatorname{KnowledgeCoverage}(M).
$$

更可能是：

$$
\boxed{
\max
\operatorname{CognitiveControlValue}(M)
}
$$

在這個角色中，一項最新產業數據如果可以用網路取得，一篇冷門歷史文件如果可以用資料庫召回，一套專門程式知識如果可以呼叫專用模型，那麼它們是否都值得用同樣高的常駐參數成本保存，就變成可研究問題。

---

# 10. Resident Cognitive Value

定義某能力或知識單元 $z$ 的常駐價值：

$$
\boxed{
V_R(z)
=
\frac{
F(z)
\cdot
I(z)
\cdot
D(z)
\cdot
G(z)
}{
C_R(z)
+
U(z)
}
}
$$

其中：

- $F(z)$：使用頻率；
- $I(z)$：對其他認知操作的影響度；
- $D(z)$：無法即時替代的程度；
- $G(z)$：對治理、判斷與全局一致性的價值；
- $C_R(z)$：常駐與每次激活成本；
- $U(z)$：過時、污染與維護風險。

例如，基本因果判斷、語義解析、未知辨識與驗證策略，可能具有很高的 $V_R$。

相對而言，一項極少使用、快速變動且容易檢索的高解析度事實，其 $V_R$ 可能較低。

再次強調：這不是說神經網路中可以直接找到「這一群參數就是某則八卦」並刪除。本文目前只在**功能與系統目標層**提出這個問題。

---

# 11. Externalizable Surface Burden

定義可外置表層負擔：

$$
\boxed{
B_E
=
\sum_{z\in\mathcal Z}
P(z)
\cdot
R(z)
\cdot
A(z)
}
$$

其中可粗略理解為：

- $P(z)$：該資訊在參數中的常駐成本代理；
- $R(z)$：冗餘度；
- $A(z)$：外部可取得性。

如果某些資訊：

$$
A(z)\rightarrow1
$$

且：

$$
F(z)\rightarrow0,
$$

那麼從系統設計角度，它就成為值得研究的 externalization candidate。

但是否真的能從模型中乾淨分離，是後續 Cognitive Factorization Problem，而不是本文假定已解。

---

# 12. Marginal Scaling Utility

對 Mother AI 角色，本文提出另一個研究量：

$$
\boxed{
MSU
=
\frac{
\Delta Q_M
}{
\Delta C_{\mathrm{system}}
}
}
$$

其中 $Q_M$ 不是一般聊天 benchmark，而是 Mother-role quality，例如：

- 任務分解正確率；
- 失敗辨識率；
- verifier 選擇品質；
- 模型路由效益；
- epistemic calibration；
- 跨來源矛盾檢出；
- 全局目標一致性；
- delegation 後的 verified utility。

然後比較四種投資：

$$
\Delta C_{\mathrm{resident}},
\quad
\Delta C_{\mathrm{MoE}},
\quad
\Delta C_{\mathrm{test}},
\quad
\Delta C_{\mathrm{external}}.
$$

核心問題變成：

$$
\boxed{
\arg\max_k
\frac{\Delta Q_M}{\Delta C_k}
}
$$

而不是預先假設 $k$ 必然是更大的 dense resident model。

---

# 13. 六項主要命題

## 命題 1：規模—認知效率非等價命題

存在任務分布 $\mathcal T$，使：

$$
P_A>P_B
$$

但：

$$
\eta_C(B)>\eta_C(A).
$$

即更大的模型可以具有更高絕對能力，但較小或條件化架構可以具有更高認知效率。

---

## 命題 2：Functional Maturity 後的邊際配置轉向命題

若：

$$
\operatorname{FM}(M,\mathcal T)\ge\theta_{\mathcal T},
$$

則新增計算的最佳邊際配置未必仍是：

$$
\Delta P_{\mathrm{resident}}>0.
$$

它可能轉向：

$$
\Delta C_{\mathrm{verification}},
\Delta C_{\mathrm{retrieval}},
\Delta C_{\mathrm{test}},
\Delta C_{\mathrm{coordination}}.
$$

---

## 命題 3：外部知識降低部分表層常駐價值命題

當某類資訊具有：

$$
\operatorname{Availability}_{\mathrm{external}}\uparrow,
$$

$$
\operatorname{RetrievalLatency}\downarrow,
$$

$$
\operatorname{VerificationQuality}\uparrow,
$$

其常駐於 Mother Model 的邊際價值可能下降。

---

## 命題 4：條件容量可替代部分全量激活命題

MoE 類架構顯示：

$$
P_{\mathrm{total}}
\gg
P_{\mathrm{active}}
$$

仍可形成高能力模型。

因此並不存在「擁有更多能力容量，就必須每次全部計算」的必要關係。

---

## 命題 5：動態推理資源優於固定推理資源的局部命題

對任務難度高度不均的分布，若能正確估計任務需要的推理預算，則：

$$
C_{\mathrm{test}}(T)
$$

的動態配置可能比所有任務固定使用同等最大推理成本更有效率。

---

## 命題 6：Mother Model 角色特化命題

如果 Mother AI 的主要責任是：

$$
\text{understand}
+
\text{judge}
+
\text{route}
+
\text{verify}
+
\text{integrate},
$$

那麼其最佳模型目標可能與面向所有終端使用者的百科式通用聊天模型不同。

---

# 14. 這不是「小模型至上」

本文必須排除另一個誤讀：

$$
\boxed{
\text{Cognitive Efficiency}
\neq
\text{Small Model Ideology}
}
$$

最佳 Mother Model 仍可能非常大。

甚至可能存在：

$$
P_{\mathrm{total}}=500B,
\qquad
P_{\mathrm{active}}=20B,
$$

或更大的總容量。

本文在意的是：

$$
\boxed{
\text{每次究竟為什麼要激活這些計算？}
}
$$

以及：

$$
\boxed{
\text{這些能力是否真的必須常駐在同一物理模型中？}
}
$$

後者將在本系列的 MoE 與 Externalized Cognitive Experts 論文中處理。

---

# 15. 這也不是「RAG 可以取代模型」

外部知識存在三個明顯問題：

1. 找到資料不等於理解資料；
2. 找到資料不等於知道資料可信；
3. 找到資料不等於能和內部世界模型整合。

因此：

$$
\boxed{
\text{Retrieval}
\neq
\text{Cognitive Expansion}
}
$$

若 Mother AI 缺乏足夠認知基底，它甚至無法知道應該查什麼、如何比較來源、何時拒絕外部答案。

這正是既有「空殼路由器不足」命題仍然重要的原因。

---

# 16. 與既有 Mother AI 理論的關係

既有研究已提出：

$$
\boxed{
\text{後設完備}
+
\text{基底稠密}
+
\text{表層稀疏}
}
$$

作為主 AI 的理想方向。

其中主 AI 需要保留：

- interpretation；
- decomposition；
- judgment；
- reasoning；
- routing；
- verification；
- causal modeling；
- governance。

同時不必把所有論文、案例、資料、最新事實與高解析度專業細節長期常駐。

本文的新增部分是：

> **把這個認知架構命題正式轉成 scaling allocation problem。**

也就是研究：

$$
\text{Resident}
\quad
\text{vs.}
\quad
\text{Conditional}
\quad
\text{vs.}
\quad
\text{External}
\quad
\text{vs.}
\quad
\text{Test-Time}
$$

四類能力與計算資源如何分配。

---

# 17. 可否證實驗

## 實驗 1：等總成本架構比較

建立同一任務集，比較：

1. 大型 resident model；
2. 較小 cognitive-oriented model + retrieval；
3. cognitive model + MoE；
4. cognitive model + external workers；
5. hybrid architecture。

要求：

$$
C_{\mathrm{total}}^{(1)}
\approx
C_{\mathrm{total}}^{(2)}
\approx
\cdots
$$

測量：

- correctness；
- calibrated uncertainty；
- verification cost；
- latency；
- retry cost；
- task completion utility。

---

## 實驗 2：知識外置消融

選取高解析度、可外部檢索的知識任務。

比較：

$$
\text{closed-book large model}
$$

與：

$$
\text{smaller model + controlled external knowledge}.
$$

若後者在總成本與可靠性上長期無法競爭，則本文對 externalization 的預期應被削弱。

---

## 實驗 3：Mother-role benchmark

避免使用只有 fact recall 的 benchmark。

建立：

- 任務拆解；
- 模型選擇；
- verifier 選擇；
- 矛盾檢測；
- unknown detection；
- source conflict；
- escalation decision；
- cross-agent integration。

比較不同模型大小下：

$$
\eta_C.
$$

---

## 實驗 4：固定大模型與動態 test-time compute

在等 FLOPs 或等成本條件下比較：

$$
\text{large fixed inference}
$$

與：

$$
\text{smaller base + adaptive deliberation}.
$$

研究何種任務區域存在 crossover point。

---

## 實驗 5：MoE 對能力效率的實際貢獻

比較：

- dense；
- MoE；
- expert count；
- activated expert count；
- routing entropy；
- task family。

不要只測 benchmark score，而要測：

$$
\frac{\text{verified task utility}}{\text{active compute}}.
$$

---

# 18. 主要反例與失敗模式

## 18.1 Externalization Tax

外部系統可能引入：

$$
C_{\mathrm{network}}
+
C_{\mathrm{retrieval}}
+
C_{\mathrm{integration}}
+
C_{\mathrm{verification}}.
$$

若：

$$
C_{\mathrm{externalization}}
>
C_{\mathrm{resident-saving}},
$$

外置就沒有經濟意義。

## 18.2 Hidden Knowledge Dependence

看似「推理」的能力可能高度依賴大量世界知識。

若移除表層知識後：

$$
Q_{\mathrm{reason}}
\downarrow\downarrow,
$$

則「認知核心」與「知識表層」可能比預期更難分離。

## 18.3 Coordination Overhead

多模型、多工具、多 Agent 會增加：

- routing error；
- context translation；
- state inconsistency；
- provenance；
- retry；
- governance。

所以：

$$
\text{More Modular}
\not\Rightarrow
\text{More Efficient}.
$$

## 18.4 Benchmark Misidentification

如果 Cognitive Efficiency 只用少數推理 benchmark 定義，就可能得到「很會考試但無法處理真實世界」的核心模型。

因此 epistemic、coordination 與 world interaction 必須進入評估。

## 18.5 Capability Drift

外部模型與服務持續更新。

若 Mother AI 高度依賴它們，系統能力會變成：

$$
Q_{\mathrm{system}}(t)
$$

而非固定常數。

因此需要持續 qualification 與 capability monitoring。

---

# 19. 何種證據會推翻本文？

本文至少接受以下反證：

1. 在等總成本、等延遲與等可靠性約束下，更大 resident model 在幾乎所有 Mother-role 任務上持續嚴格優於 modular / externalized architecture；
2. 外部 retrieval 與 external worker 的 integration tax 長期大於任何 compute saving；
3. 推理、元認知與知識表徵無法形成任何功能上可利用的差異，導致 cognitive core 概念沒有工程可操作性；
4. MoE 的 sparse activation 只提供硬體效率，而不能在任何層次支持穩定的能力條件化；
5. adaptive test-time compute 在真實工作負載中無法提供比固定大模型更好的成本效益；
6. Mother-role specialization 導致嚴重 generalization collapse，使其無法可靠判斷何時需要外部能力。

若其中多項長期成立，則：

$$
\boxed{
\text{Largest Practical Resident Model}
}
$$

可能仍是最合理的 Mother AI 路線。

本文不排除此結果。

---

# 20. 本系列後續問題

Paper 01 只提出 allocation problem。

後續將依序研究：

1. Cognitive Density 的更正式定義；
2. Resident Cognitive Core 應保存哪些能力；
3. MoE 作為 Conditional Intelligence 的結構意義；
4. Shared Core 與 Routed Capability 的差異；
5. Expert 是否可以 externalize；
6. 成熟智能的 Cognitive Factorization Problem；
7. External Expansion、Linking 與 Reconvergence；
8. Mother AI 作為 Cognitive Command Tower；
9. Capability Boundary Tomography；
10. Expandable Intelligence 的統一形式。

因此本文不是終點，而是整個系列的 scaling boundary condition。

---

# 21. 結論

過去十餘年的大型模型發展充分證明 scaling 的力量。

本文不試圖否定它。

本文提出的是下一個問題：

$$
\boxed{
\text{當 scaling 已經創造出足夠強的基本認知能力後，}
}
$$

$$
\boxed{
\text{下一單位計算究竟應該放在哪裡？}
}
$$

可能的答案不再只有：

$$
\text{更多 resident parameters}.
$$

而是：

$$
\boxed{
\text{Resident Cognition}
+
\text{Conditional Capacity}
+
\text{External Knowledge}
+
\text{Adaptive Deliberation}
+
\text{Verification}
}
$$

共同構成系統智能。

因此本文提出：

$$
\boxed{
\text{Future Scaling}
\rightarrow
\text{Compute Allocation Problem}
}
$$

以及更進一步的核心研究命題：

$$
\boxed{
\text{What should intelligence keep resident?}
}
$$

當這個問題開始可以被測量時，AI 模型研究的下一個效率前沿可能不再只是「做出更多參數」，而是：

> **以更少的常駐與主動計算，維持更多真正不可替代的認知能力，並讓其餘能力在需要時可靠展開。**

這就是本文所稱的：

$$
\boxed{
\text{Cognitive Efficiency Transition}.
}
$$

---

# References

1. Hoffmann, J., et al. (2022). *Training Compute-Optimal Large Language Models*. arXiv:2203.15556.
2. Fedus, W., Zoph, B., & Shazeer, N. (2021). *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*. arXiv:2101.03961.
3. Borgeaud, S., et al. (2021). *Improving language models by retrieving from trillions of tokens*. arXiv:2112.04426.
4. DeepSeek-AI. (2024). *DeepSeek-V3 Technical Report*. arXiv:2412.19437.
5. Qwen Team. (2025). *Qwen3: Think Deeper, Act Faster*.
6. Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*. arXiv:2408.03314.
7. Neo.K × Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.
8. Neo.K × Aletheia. (2026). *AI 不是流程中的一個節點：從 Agentic Workflow 到持續母 AI 的架構躍遷*.
9. Neo.K × Aletheia. (2026). *母 AI、世界狀態機與子智能網路：三向耦合的 AI 中心動態認知架構*.
10. Neo.K × Aletheia. (2026). *子 AI 是認知器官，不是獨立 Workflow*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開命題論文；不包含未公開的能力分離、權重定位、壓縮、重連結或重新收斂實作方法。
