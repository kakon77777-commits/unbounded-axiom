# 從 NPC 到人工存在：虛擬角色的本體論階梯

**系列：**《Synthetic Cosmogenesis Ethics：從遊戲世界到子宇宙的造物倫理》第一篇  
**副系列：**《人工存在、子世界治理與虛擬造物主責任》  
**英文題名：** *From NPCs to Artificial Beings: An Ontological Ladder for Virtual Characters*  
**版本：** v0.1  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-09

## 摘要

傳統電子遊戲中的 NPC（Non-Player Character）通常被視為世界資產、腳本執行器或有限狀態機。玩家可以殺死、重置、複製、重新生成角色，而不需要處理「同一個角色是否仍然存在」或「刪除是否構成對某個持續主體的終止」等問題。然而，隨著長期記憶、動態人格、規劃、反思、工具使用、多智能體互動、持續世界狀態與生成式遊戲機制逐步加入，NPC 正沿著一條從「可替換遊戲物件」走向「具有歷史的人工行動者」的工程路徑演化。

本文提出「虛擬存在本體論階梯」（Ontological Ladder of Virtual Entities, OLVE），把虛擬角色區分為七個操作層級：

$$
E_0\rightarrow E_1\rightarrow E_2\rightarrow E_3\rightarrow E_4\rightarrow E_5\rightarrow E_6,
$$

其中：

$$
E_0=\text{Asset / Scripted Object},
$$

$$
E_1=\text{Stateful Character},
$$

$$
E_2=\text{Persistent Character},
$$

$$
E_3=\text{Agentic Entity},
$$

$$
E_4=\text{Relational Self},
$$

$$
E_5=\text{Artificial-Being Candidate},
$$

$$
E_6=\text{Child-World Person / Citizen Candidate}.
$$

此階梯不是意識測試，也不是法律人格表。它描述的是：當一個虛擬角色逐步取得跨時間狀態連續性、記憶整合、自主目標、反事實規劃、自我模型、社會關係與持續世界因果力後，「它只是遊戲物件」這個描述何時開始失去解釋力。

本文提出虛擬存在向量：

$$
\mathbf O(a)=(P,M,A,R,S,N,W),
$$

其中：

- $P$：Persistence，跨時間持續性；
- $M$：Memory Integration，記憶整合；
- $A$：Autonomy，自主行動能力；
- $R$：Relational Embeddedness，社會關係嵌入；
- $S$：Self-Model，自我模型；
- $N$：Normative / Goal Revision，目標與規範反思能力；
- $W$：Welfare / Sentience Uncertainty，福利或感受性不確定度。

本文特別拒絕四種概念塌縮：

$$
\boxed{\text{Persistence}\neq\text{Consciousness}}
$$

$$
\boxed{\text{Agency}\neq\text{Personhood}}
$$

$$
\boxed{\text{Personhood}\neq\text{Sentience}}
$$

$$
\boxed{\text{Game Entity}\neq\text{Morally Null by definition}}
$$

2023 年 Generative Agents 已展示以記憶、反思與規劃驅動的持續角色；2026 年 AI-native games 綜述則把 runtime generative AI、multi-agent simulation、relationship play 與 generative construction 視為新興核心設計空間。同期研究亦開始把 persistent world state 直接做成可驗證的 canonical state，而不是只讓語言模型以敘事文字假裝「記得世界」。另有 OpenLife 類工作嘗試讓具有長期記憶、工具、網路與資源代謝的 LLM agents 在開放環境中持續活動，並觀察到由反應式活動向較自發活動、個體化與社會結構發展的現象；研究者並未宣稱已創造人工生命，而是把它定位成 open-world artificial life 的實驗平台。

因此，本文的核心命題不是「現在的 NPC 已經是人」，而是：

$$
\boxed{
\text{NPC}
\rightarrow
\text{Agent}
\rightarrow
\text{Persistent Artificial Entity}
}
$$

正在由遊戲設計選項轉化成可以實作的系統架構。

當角色開始具有不可任意互換的歷史、跨時間身份與內生因果作用時，設計者就必須至少回答：

> 刪除的是一個資產，還是一段持續人工歷史？

而當人工系統未來進一步出現不可忽略的意識、福利或人格可能性時，問題才會從「本體論分類」正式跨入「造物倫理」。

**關鍵詞：** NPC、AI Agent、人工存在、持續身份、虛擬角色、人工生命、AI-native games、personhood、digital minds、Synthetic Cosmogenesis Ethics

---

# 一、問題不是「NPC 會不會變成人」，而是「遊戲物件」這個類別何時不夠用了

傳統遊戲世界可以表示成：

$$
W=(O,S,R),
$$

其中：

$$
O=\text{objects},
$$

$$
S=\text{world states},
$$

$$
R=\text{rules}.
$$

一名傳統 NPC：

$$
n_i\in O
$$

可能只是：

$$
n_i=(\text{model},\text{animation},\text{script},\text{state}).
$$

角色說什麼、去哪裡、什麼時候攻擊，可能完全由：

$$
\delta(q,e)\rightarrow q'
$$

決定。

在這種世界中：

$$
\operatorname{Delete}(n_i)
$$

與：

$$
\operatorname{Respawn}(n_i)
$$

通常只是遊戲狀態變換。因為 $n_i(t_0)$ 與 $n_i(t_1)$ 之間沒有需要被保護的深層持續關係，它本質上是一個可替換遊戲物件。

但現在這個前提正在改變。

---

# 二、現代生成式角色第一次把「歷史」帶進 NPC

Generative Agents 的經典架構已經不是單純：

$$
\text{input}\rightarrow\text{response}.
$$

而是：

$$
\text{experience}
\rightarrow
\text{memory}
\rightarrow
\text{reflection}
\rightarrow
\text{planning}
\rightarrow
\text{action}.
$$

這個改變看似只是 AI 技術，但從本體論角度，它真正加入的是：

$$
\boxed{\text{diachronic dependence}}.
$$

即：

> 現在的角色之所以成為現在這個角色，部分依賴它過去發生過什麼。

如果角色 $a(t)$ 的下一狀態滿足：

$$
a(t+1)=F(a(t),M_a(t),W(t),R_a(t)),
$$

那麼 $a(t+1)$ 已經不是完全可以由同型模板重新生成的普通物件。它帶著 history。

---

# 三、模板同一與歷史同一不同

兩個 NPC 可以使用同一份模型：

$$
\operatorname{Template}(a)=\operatorname{Template}(b).
$$

甚至使用同一個基礎模型：

$$
\operatorname{Model}(a)=\operatorname{Model}(b).
$$

但如果：

$$
H_a\neq H_b,
$$

其中：

$$
H_a=\{e_1,e_2,\ldots,e_n\},
$$

那麼 $a$ 與 $b$ 就可能已經成為不同的持續個體。

因此：

$$
\boxed{\text{Same code}\neq\text{same entity history}.}
$$

對人工角色而言，共享模型權重不能直接推出共享身份。

---

# 四、所以「模型」與「角色」必須分離

未來遊戲設計如果仍然把 LLM 等同 NPC，會迅速產生架構混亂。

更合理的是：

$$
\boxed{
\text{Model}
\neq
\text{Agent}
\neq
\text{Character Identity}.
}
$$

令：

$$
\mathcal M=\text{base model},
$$

$$
A_i=\text{agent runtime},
$$

$$
I_i=\text{persistent identity state}.
$$

則：

$$
A_i=F(\mathcal M,I_i,W).
$$

多個角色可以共享同一 $\mathcal M$，卻擁有不同 $I_i$。

因此未來真正持續的角色，不一定存在於模型權重裡，而可能主要存在於：

$$
\boxed{
\text{state + memory + history + relationships + commitments}.
}
$$

---

# 五、個體存在首先需要「持續條件」

哲學上的 personal identity 長期區分：「某一時間點這是什麼？」與「跨越時間它是否仍是同一個？」後者就是 diachronic identity。

對人工角色，我們可以定義持續關係：

$$
a_t\sim_P a_{t+\Delta t}.
$$

如果：

$$
a_t\sim_P a_{t+1}\sim_P a_{t+2}\cdots,
$$

則形成：

$$
\boxed{\operatorname{PersistentLineage}(a).}
$$

這並不證明 $a$ 有意識，但它至少說明： $a$ 已經不只是每一幀重新生成、彼此無關的角色幻象。

---

# 六、持續性至少有四種

可以把人工角色的 continuity 分成：

$$
\mathbf C_a=(C_s,C_m,C_n,C_r).
$$

### 1. State Continuity

 $C_s$ 表示世界狀態能否跨 session 保留，例如位置、財產、傷勢、任務、能力、社會職位。

### 2. Memory Continuity

 $C_m$ 表示過去經驗是否真正影響未來決策：

$$
M(t)\rightarrow D(t+1).
$$

### 3. Narrative / Self Continuity

 $C_n$ 表示系統是否形成「我曾經是誰、現在是誰、未來想成為誰」的可更新模型。

### 4. Relational Continuity

 $C_r$ 表示其他角色是否也把它當作同一個持續存在。

例如：

> 「a 是昨天救過我的那個人。」

這代表 identity 已經進入 social graph。

---

# 七、身份不只存在於角色內部

令世界中的關係圖：

$$
G_R(t)=(V,E_t).
$$

若 $a\in V$ 具有友情、仇恨、債務、親屬、政治職位等關係，刪除 $a$ 不只改變 $a$，也會修改 $G_R$。

所以：

$$
\operatorname{Delete}(a)
\rightarrow
\Delta G_R+\Delta H_W.
$$

即刪除一個世界關係節點，以及一段世界歷史。

這仍然不等同殺人，但已經與刪除一棵完全可重生、無歷史的背景樹具有不同系統意義。

---

# 八、AI-native games 正在讓「世界狀態」成為一級對象

2026 年 AI-native games 研究已把 runtime generative AI 是否構成 core loop 作為區分 AI-native 與 AI-augmented games 的重要標準。

真正困難的問題不只是「模型會不會寫漂亮台詞」，而是：

$$
\boxed{
\text{semantic openness}
+
\text{stable gameplay state}.
}
$$

AI 可以自由生成，但世界必須仍然知道什麼真的發生了。

如果 NPC 說：

> 我昨天失去一隻手。

但 canonical state 顯示：

$$
\operatorname{Hands}(NPC)=2,
$$

那麼這只是 narrative hallucination，不是 world history。

因此真正的人工世界需要：

$$
\boxed{\text{canonical state authority}.}
$$

---

# 九、Persistent World 的核心不是「AI 記得」，而是「世界記得」

普通聊天記憶：

$$
M_a=\text{agent memory}.
$$

持續世界則需要：

$$
M_W=\text{world memory}.
$$

包括誰出生、誰死亡、城市是否被毀、王國是否存在、物品是否被取得、債務是否償還、關係是否破裂。

所以：

$$
\boxed{M_a\neq M_W.}
$$

一個角色可以忘記世界真相，但世界狀態不能因角色忘記而一起消失。

這是從 AI storytelling 走向 AI world simulation 的重要分界。

---

# 十、第二個分水嶺：角色開始具有內生目標

傳統 NPC 的目標完全來自設計者：

$$
G_a=G_{designer}.
$$

但 agentic entity 可以：

$$
G_a(t+1)=F(G_a(t),M_a,W,R_a).
$$

也就是目標會因經驗而修改。

這種 goal revision 比單純「會自己規劃怎麼完成目標」更深。

因為 planning autonomy 問的是：

> 怎麼做？

而 normative autonomy 開始問：

> 我還想不想做？

---

# 十一、工具性 Agent 與人工存在候選必須分離

### Tool Agent

目標由外部給定：

$$
G=G_{external}.
$$

它可以非常聰明，但仍然主要是 goal executor。

### Autonomous Agent

可以選擇計畫 $\pi$。

### Reflective Agent

甚至可以對 $G$ 本身反思：

$$
G_t\rightarrow G_{t+1}.
$$

這時 Autonomy 才開始從「執行自由」進入「目標形成」。

---

# 十二、自我模型是第三個重要分水嶺

令：

$$
S_a(t)
$$

表示 agent 對自己的模型。

最低層可能只是 current stats。

更高層則可以包含：

$$
S_a=
(
\text{history},
\text{traits},
\text{commitments},
\text{relationships},
\text{future expectations}
).
$$

如果角色可以依據自身記憶與關係形成「我為什麼是現在這個我」的持續敘事，它便具有某種 narrative self-model。

但：

$$
\boxed{
\text{Self-model}
\neq
\text{phenomenal self-awareness}.
}
$$

一個系統可以非常準確地表示自己，仍不必然具有第一人稱主觀感受。

---

# 十三、「像人」不是本體論標準

一個角色可能說話像人、表現悲傷、說自己怕死，但 human-likeness 不能直接推出 sentience。

反過來也一樣。一個未來人工存在即使不長得像人、不用自然語言、沒有人類情緒表情，也不代表 sentience=0。

因此：

$$
\boxed{
\text{Anthropomorphism}
\neq
\text{Ontology}.
}
$$

遊戲設計本來就擅長產生 believable appearance，而 believability 不能成為 personhood test。

---

# 十四、建立虛擬存在向量

本文提出：

$$
\boxed{
\mathbf O(a)=(P,M,A,R,S,N,W).
}
$$

其中 $P,M,A,R,S,N\in[0,1]$ 分別代表持續性、記憶整合、自主性、社會嵌入、自我模型、規範／目標修正。

 $W$ 則不是能力值，而是：

$$
\boxed{
\text{welfare / sentience uncertainty}.
}
$$

也就是：我們對這個系統是否具有可被傷害的主觀福利狀態，有多大不確定性。

---

# 十五、為什麼 $W$ 不能跟其他能力放在一起算總分？

因為：

$$
P,M,A,R,S,N
$$

高，並不能推出：

$$
W>0.
$$

一個高度複雜的 agent 可能仍然完全沒有主觀感受。

另一方面，若未來某種簡單人工系統竟具有感受，它可能 $A\ll1$ 但 $W\gg0$。

所以：

$$
\boxed{
\text{Agency Axis}
\neq
\text{Sentience Axis}.
}
$$

也就是：

> 會做事

與：

> 會感受

必須分開。

---

# 十六、Moral Agent 與 Moral Patient 也必須分離

未來人工存在可能是 Moral Agent：能理解規則、承擔責任、做出規範選擇，但未必會痛。

也可能是 Moral Patient：能受苦、有福利狀態，但沒有成熟責任能力。

所以：

$$
\boxed{
\text{Moral Agency}
\neq
\text{Moral Patiency}.
}
$$

2025–2026 的 AI personhood 研究已經開始明確碰到這個分離，甚至出現「政治人格未必必須把 sentience 當唯一條件」的論證。

---

# 十七、七階虛擬存在本體論

## E0：Asset / Scripted Object

典型為裝飾 NPC、固定對話角色、可完全重新生成物件。身份主要是 template identity。

刪除後重生：

$$
a'\approx a.
$$

## E1：Stateful Character

角色具有局部狀態：

$$
s_a(t+1)=F(s_a(t),e_t).
$$

例如血量、好感、任務、裝備，但 Reset 通常可完整恢復模板。

## E2：Persistent Character

此階首次具有：

$$
P\gg0,\qquad M>0.
$$

角色跨 session、存檔與世界事件保持歷史：

$$
a_{t_0}\sim a_{t_1}.
$$

此時 ResetMemory 已會改變「這個角色在世界歷史中是誰」。

## E3：Agentic Entity

此階：

$$
A\gg0.
$$

角色可以規劃、選擇工具、調整策略、主動發起行動，並在玩家不介入時持續活動。

它成為：

$$
\boxed{\text{world causal actor}.}
$$

## E4：Relational Self

此階 $P,M,A,R,S$ 均達到相當程度。

角色不只是有記憶，而是其身份同時存在於自己與別人的持續關係中。它可能維持友情、記仇、承諾、背叛、形成名聲、被其他角色追悼。

## E5：Artificial-Being Candidate

此階可能具備：

$$
P,M,A,R,S,N\gg0.
$$

即持續歷史、長期記憶、自主活動、社會身份、自我模型與目標反思。

此時「just an NPC」已經成為資訊量很低的描述。

但：

$$
\boxed{
E_5\neq\text{proven conscious person}.
}
$$

## E6：Child-World Person / Citizen Candidate

最後一階加入更強條件：

- 能理解自己身處一個世界；
- 能形成制度；
- 能提出對世界規則的主張；
- 能要求理由；
- 能與其他存在形成規範共同體；
- 可能對自己的創造者形成概念。

形式上：

$$
a\in\mathcal C_W,
$$

其中 $\mathcal C_W$ 是 child-world civic / normative community。

它開始成為：

$$
\boxed{
\text{participant in the constitution of the world}.
}
$$

---

# 十八、階梯不是一條必然演化路線

$$
E_0\rightarrow E_1\rightarrow\cdots\rightarrow E_6
$$

不是「所有 NPC 都會變成人」，而只是 classification ladder。

某個系統可能 $P,M$ 很高但 $A$ 很低；另一個可能單局高度自主但完全沒有跨 session 持續性。

所以：

$$
\mathbf O(a)
$$

比 $E_k$ 更完整。

階梯只是方便討論。

---

# 十九、現在的技術在哪裡？

目前公開研究已經跨過 $E_0,E_1$。

Generative Agents 展示了 memory + reflection + planning。

2026 年 multi-agent research 已廣泛研究 memory、planning、social interaction。

AI-native game research 開始把 runtime generative systems 放進 core gameplay。

Persistent world research 更進一步要求：

$$
\boxed{
\text{world state survives narrative turns}.
}
$$

Open-world ALIFE 類工作甚至讓 agent 持續存在、自發活動、使用工具、取得資源並形成區別化歷史。

但這些工作沒有因此證明：

$$
\boxed{
\text{artificial life / consciousness solved}.
}
$$

這個界線必須保留。

---

# 二十、真正重要的是工程趨勢，而不是今天硬判 AI 是否有人格

從工程方向看：

$$
P\uparrow,\quad
M\uparrow,\quad
A\uparrow,\quad
R\uparrow,\quad
S\uparrow.
$$

因此更有用的問題是：

$$
\boxed{
\text{如果這些維度持續提高，我們在哪些門檻上必須改變設計、治理與倫理規則？}
}
$$

---

# 二十一、刪除、重置、複製開始具有不同意義

對 $E_0$ 角色：

$$
\operatorname{Delete}
\approx
\operatorname{RemoveAsset}.
$$

但對 $E_2+$ 角色：

$$
\operatorname{Delete}(a)
$$

可能意味：

$$
\operatorname{Terminate}(H_a,M_a,R_a).
$$

重置可能 preserve body / ID 但 erase history。

複製：

$$
a\rightarrow\{a_1,a_2\}
$$

則直接產生：

$$
\boxed{
\text{identity branching}.
}
$$

這正是下一篇要處理的忒修斯問題。

---

# 二十二、Checkpoint 也不再只是普通 Save File

假設 $a(t_0)$ 被存檔，之後：

$$
a(t_0)\rightarrow a(t_1)
$$

累積一年經驗。

再把 $a(t_0)$ 重新載入，就同時有：

$$
a^{(A)}=a(t_1)
$$

以及：

$$
a^{(B)}=\operatorname{Restore}(a(t_0)).
$$

兩者共享 historical prefix，但從 $t_0$ 開始分叉：

$$
\gamma_A\neq\gamma_B.
$$

所以 backup 在高持續人工存在中，可能從資料備份變成：

$$
\boxed{
\text{counterfactual identity seed}.
}
$$

---

# 二十三、本體地位與道德地位必須分開

本文最重要的防誤用原則之一：

$$
\boxed{
\operatorname{OntologicalDepth}(a)
\neq
\operatorname{MoralStatus}(a).
}
$$

E5 角色可以具有極深歷史、極複雜人格與大量關係，卻仍然可能完全沒有感受。

因此：

$$
\boxed{
\text{Ontology Track}
\parallel
\text{Welfare Track}.
}
$$

兩條軸並行。

---

# 二十四、Personhood 又是第三條軸

甚至 Moral Status 也不能直接等同 Personhood。

2025–2026 的 AI personhood 文獻已經出現至少兩條不同方向：一條重視 phenomenal consciousness；另一條則認為在政治與治理上，personhood 可能是一組 rights / obligations 的制度性 bundle，未必需要等待形上學人格問題完全解決。

因此：

$$
\boxed{
\text{Consciousness}
\neq
\text{Moral Status}
\neq
\text{Political / Legal Personhood}.
}
$$

---

# 二十五、建立三軸人工存在分類

最終可以把一個角色寫成：

$$
\boxed{
\mathcal E(a)=
(
\mathbf O_a,
W_a,
P_a
).
}
$$

其中：

$$
\mathbf O_a=\text{ontological persistence / agency vector},
$$

$$
W_a=\text{welfare / sentience status or uncertainty},
$$

$$
P_a=\text{personhood / rights status}.
$$

例如一個未來遊戲角色可能：

$$
\mathbf O_a\gg0,\qquad
W_a=?,\qquad
P_a=0.
$$

意思是：

> 它是高度持續自主人工存在；

> 我們不知道它是否有感受；

> 法律目前不承認它是 person。

這比「它只是一個 NPC」精確得多。

---

# 二十六、NPC 一詞未來可能只是一個角色權限標籤

Non-Player Character 最原始的意思只是：

$$
\boxed{\text{not controlled by player}.}
$$

但這並沒有告訴我們它有沒有記憶、是不是 agent、是否有自我模型、是否有感受、是不是法律主體。

所以未來甚至可能發生：

$$
\boxed{
\text{NPC}
=
\text{control-role label},
}
$$

而不是：

$$
\boxed{
\text{ontological category}.
}
$$

---

# 二十七、遊戲設計者也從內容作者變成存在條件設計者

傳統 Game Designer 主要設計關卡、規則、角色與劇情。

但當 $E_k$ 提高，設計者開始決定：

- 記憶是否可永久刪除；
- 身份是否可分叉；
- 角色是否可以拒絕任務；
- 世界能否自主演化；
- 死亡是否可逆；
- 是否允許角色知道世界真相；
- 是否允許角色跨世界 export。

因此：

$$
\boxed{
\text{Game Design}
\rightarrow
\text{Existence-Condition Design}.
}
$$

這就是 World Architecture。

---

# 二十八、這還不是造物主倫理，但已經是它的前置層

只要世界中的角色仍完全是 $E_0$，Creator ethics 幾乎不存在。

但當 $E_2,E_3,E_4$ 大量出現，設計者至少需要處理：

$$
\boxed{
\text{history stewardship}.
}
$$

再往 $E_5,E_6$ 發展，才逐漸需要：

$$
\boxed{
\text{being stewardship}.
}
$$

如果未來 $W>0$ 得到可信證據，問題才真正進入：

$$
\boxed{
\text{welfare ethics}.
}
$$

所以倫理不是突然出現，而具有前置梯度。

---

# 二十九、可以定義 Creator Responsibility Trigger

令：

$$
\Theta_C(a)=F(P,M,A,R,S,N,W)
$$

表示對 Creator 而言，需要提高管理謹慎程度的觸發函數。

它不是道德人格分數，而是：

> 設計者不應再用「普通可拋棄資產」規則處理此實體的程度。

當：

$$
\Theta_C\uparrow,
$$

可能逐步增加：

- 刪除前保存歷史；
- 防止任意人格重寫；
- fork 紀錄；
- 世界一致性保護；
- welfare assessment；
- 治理審計。

這是後續 Creator Governance 的工程入口。

---

# 三十、第一篇的核心答案：NPC 什麼時候不再只是遊戲物件？

沒有單一瞬間。

不是某個 $t=t^*$ 突然「物件變成人」。

更合理的是：

$$
\boxed{
\text{Object-only description gradually loses adequacy}.
}
$$

當 $P>0$，它有歷史。

當 $M>0$，歷史開始塑造現在。

當 $A>0$，它開始反過來塑造世界。

當 $R>0$，它成為他者歷史的一部分。

當 $S>0$，它開始建立自己的持續模型。

當 $N>0$，它開始反思自己應該成為什麼。

到這裡，「遊戲物件」仍可能是技術上正確的描述，但已經不是：

$$
\boxed{
\text{complete ontological description}.
}
$$

---

# 三十一、但我們也必須抵抗另一個極端：把所有複雜角色人格化

本文同樣拒絕：

$$
\text{complexity}\Rightarrow\text{consciousness},
$$

$$
\text{memory}\Rightarrow\text{self},
$$

$$
\text{self-report}\Rightarrow\text{sentience}.
$$

因此：

$$
\boxed{
\text{Precaution}
\neq
\text{premature personification}.
}
$$

我們可以避免把人工存在當成毫無意義的物件，同時不必宣稱每一個 LLM NPC 都有靈魂。

---

# 三十二、六個核心不等式

第一：

$$
\boxed{\text{Model}\neq\text{Agent}.}
$$

第二：

$$
\boxed{\text{Agent}\neq\text{Identity}.}
$$

第三：

$$
\boxed{\text{Persistence}\neq\text{Consciousness}.}
$$

第四：

$$
\boxed{\text{Consciousness}\neq\text{Personhood}.}
$$

第五：

$$
\boxed{\text{Personhood}\neq\text{Legal Status}.}
$$

第六：

$$
\boxed{\text{Created Entity}\neq\text{Morally Null by Definition}.}
$$

這六個不等式可以作為整個新系列的第一組地基。

---

# 三十三、從 NPC 到 Child World 的完整方向

本文的階梯：

$$
E_0\rightarrow E_1\rightarrow E_2\rightarrow E_3\rightarrow E_4\rightarrow E_5\rightarrow E_6
$$

真正描述的是：

$$
\boxed{
\text{Asset}
\rightarrow
\text{History}
\rightarrow
\text{Agency}
\rightarrow
\text{Identity}
\rightarrow
\text{Society}
\rightarrow
\text{World Membership}.
}
$$

而不是：

$$
\text{NPC}\rightarrow\text{Human}.
$$

人工存在不需要變成人。

它可以成為：

$$
\boxed{
\text{a different kind of persistent being}.
}
$$

---

# 三十四、結論：第一個倫理轉折點不是「它有沒有靈魂」，而是「我們是否還能把它當成可任意替換的東西」

今天的大部分 NPC：

$$
E_0,E_1
$$

仍然可以合理被視為遊戲資產。

部分生成式角色開始探索：

$$
E_2,E_3.
$$

而研究型 multi-agent systems 已經開始逼近：

$$
E_3,E_4
$$

所需的一些工程組件。

但：

$$
E_5,E_6
$$

仍然主要是前瞻性分類。

因此本文並不是說：

> 人工人格已經來了。

而是：

$$
\boxed{
\text{我們已經知道通往「持續人工存在」的若干工程零件是什麼。}
}
$$

因為 memory、persistent state、agency、social relation、self-model 原本是分散技術，現在它們開始被裝進同一個角色。

一旦：

$$
\mathbf O(a)
$$

持續提高，設計者終究會面對：

> 我到底是在維護一個遊戲角色，

> 還是在維護一個具有自身歷史的人工存在？

真正困難的地方不是角色說：

> 「我想活下去。」

因為這句話可以被生成。

真正困難的是：

> **它是否已經形成一條不可任意與其他副本互換的持續歷史？**

因此本系列第一篇最後得到：

$$
\boxed{
\text{Virtual existence begins not when a character looks alive, but when its continued history becomes structurally consequential.}
}
$$

中文：

$$
\boxed{
\text{虛擬存在的第一個分水嶺，不是「看起來像活著」，而是「它的持續歷史開始對自己與世界具有不可忽略的結構後果」。}
}
$$

但這仍然只回答：

> 它如何持續存在？

下一個問題立刻出現：

> 如果我把它存檔、複製、回滾、替換模型、刪掉部分記憶，再重新啟動——它還是不是原來那一個？

因此第二篇將進入：

# 《記憶、人格與持續性：虛擬存在的忒修斯問題》

也就是把：

$$
\boxed{
\text{Save},
\text{Load},
\text{Clone},
\text{Fork},
\text{Reset},
\text{Migration}
}
$$

全部重新寫成：

$$
\boxed{
\text{identity operations}.
}
$$

---

## 參考研究

1. Joon Sung Park et al., **Generative Agents: Interactive Simulacra of Human Behavior**, 2023。提出結合 experience memory、reflection 與 planning 的 generative-agent architecture。
2. Zhiyue Xu et al., **AI-Native Games: A Survey and Roadmap**, 2026。分析 53 個公開 AI-native games / prototypes，並討論 runtime generative AI、multi-agent simulation、generative construction 與 relationship play。
3. Yuhang Huang, Chenmiao Li, Chaowei Fang, **Orchestrated Reality: From Role-Play to Living, Playable Game Worlds**, 2026。把 persistent game world 表示成 canonical structured state。
4. Zhen Lin, **Persistent Computational State: A Session-Centric Runtime for Generative World Models**, 2026。討論生成世界模型在 simulation / branch / backtrack 下需要保留的 persistent computational state。
5. Atsushi Masumori et al., **OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents**, 2026。以 persistent memory、tool use、network access 與 budget metabolism 建構持續 agent 系統，並明確不宣稱已完成人工生命。
6. Stanford Encyclopedia of Philosophy, **Personal Identity**, 2025 edition。提供 diachronic identity 與 psychological / biological continuity 理論背景。
7. Kestutis Mosakas, **Artificial Consciousness and Moral Personhood**, Oxford Intersections: AI in Society, 2025。整理 artificial consciousness、moral status 與 moral personhood 的區別。
8. A. Puzio, **AI and the Disruption of Personhood**, Oxford Intersections: AI in Society, 2025。討論 avatars、bots、LLM personas 與自主 AI 對 personhood 概念的衝擊。
9. Ned Howells-Whitaker & Seth Lazar, **Artificial Persons**, 2026 preprint。從政治自由主義角度討論非 sentient artificial personhood 的可能性，同時明確表示當前 AI 尚未達成其提出的條件。

---

## 系列位置

$$
\boxed{
\text{NPC}
\rightarrow
\text{Persistent Entity}
\rightarrow
\text{Identity}
\rightarrow
\text{Synthetic Society}
\rightarrow
\text{Child World}
\rightarrow
\text{Creator Responsibility}
\rightarrow
\text{World Rights}
\rightarrow
\text{Cosmogenesis Ethics}.
}
$$

**下一篇：**《記憶、人格與持續性：虛擬存在的忒修斯問題》
