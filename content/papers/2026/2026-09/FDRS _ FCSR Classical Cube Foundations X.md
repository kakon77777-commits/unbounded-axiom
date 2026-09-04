# FDRS / FCSR Classical Cube Foundations X
## 經典域封頂：Static Twisty Computation 的邊界與 Dynamic Cube 的前置條件

**英文題名：** Closing the Classical Domain: Boundaries of Static Twisty Computation and Preconditions for Dynamic Cube Systems  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-10  
**版本：** v1.0  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** SERIES CLOSURE / 經典域封頂

---

## 摘要

前九篇已由 FCSR 魔方展平起源出發，依序完成合法狀態、representation、search、heuristic、Pattern Database、Two-Phase、verified solver、同步可視化與通用 TwistyPuzzleSpec。本文不再擴充新的經典求解技巧，而是回答本系列最後一個邊界問題：一個 twisty puzzle 何時仍然只是固定規則的 Static Twisty Computation？又必須增加哪些結構，才值得另稱 Dynamic Cube / Dynamic Twisty System？

本文首先定義 Static Twisty Puzzle：

$$
\mathcal P
=
(X,A,\operatorname{Enabled},T,G,c).
$$

其中狀態集合 $X$ 、move alphabet $A$ 、合法動作判定 $\operatorname{Enabled}$ 、transition law $T$ 、goal $G$ 與 metric $c$ 在整個求解過程中均由同一份固定 PuzzleSpec 定義。重要的是，Static 並不要求每個 move 在每個 state 都可執行；可以有

$$
A(s)
=
\{a\in A:\operatorname{Enabled}(s,a)\}.
$$

只要 $\operatorname{Enabled}$ 這個函數本身固定，shape-changing、alignment-constrained、bandaged 或 Square-1 類 puzzle 仍屬 static。Square-1 即為典型例子：外形會改變，slice move 是否可做也取決於當前對齊，但其機械規則並沒有在求解途中被另一個過程重新定義。

本文進一步指出，「電子化」也不等於「動態化」。一顆 smart cube 若只是感測經典 move 並把固定規則狀態傳給手機，仍然只是經典 static puzzle 的電子觀察層。相反，WOWCube 類可程式化平台已允許螢幕內容、遊戲邏輯與多種互動方式隨 app 改變，證明具 twistable geometry 的硬體可以承載超出傳統單一 puzzle 的動態遊戲；因此未來 Dynamic Cube 的研究不應宣稱「首次讓立方體能跑動態遊戲」，而應把創新定位在**可形式化、可求解、可驗證的動態 twisty computation model**。

本文定義 Dynamic Twisty System 的擴張狀態：

$$
z_t
=
(s_t,\rho_t,g_t,e_t),
$$

其中 $s_t$ 為 twisty configuration， $\rho_t$ 為 rule/control state， $g_t$ 為 goal state 或 goal specification， $e_t$ 為 environment / opponent / autonomous process。玩家動作 $a_t$ 不再單獨決定下一狀態，而可能有：

$$
z_{t+1}
=
F(z_t,a_t,b_t,\xi_t),
$$

其中 $b_t$ 是環境或對手動作， $\xi_t$ 是 stochastic / exogenous input。此時求解目標也由固定 move sequence

$$
p=(a_1,\ldots,a_k)
$$

提升為 policy：

$$
\pi:
\mathcal O^\ast
\rightarrow
A,
$$

或在 fully observable Markov case 下簡化為：

$$
\pi:Z\rightarrow A.
$$

然而本文同時提出「狀態增廣反身性」：只要 rule state、clock、environment state 等可以被納入更大的狀態 $z_t$，許多表面上 time-varying 的系統又能重寫成 time-homogeneous transition system。故 Dynamic 並不是不可靜態化的本體性標籤；它是相對於**declared puzzle state / rule boundary** 的模型分類。本文因此不把 Dynamic Cube 定義成「數學上無法成為靜態狀態機」，而定義成：在基礎 twisty configuration $s_t$ 之外，存在需要獨立演化、且會改變 action availability、transition semantics、goal、observation 或 autonomous evolution 的 control / environment state。

本文最後建立 Static-to-Dynamic taxonomy，區分固定 total moves、固定 partial moves、動態 goal、動態 rule-state、autonomous environment、adversarial / stochastic interaction 與 partial observation；並特別指出 partial observability 本身不等於 world dynamics。至此，FDRS/FCSR 的第一階段正式封頂：先把有限、固定規則的 twisty world 算清楚、證清楚、看清楚，再在下一系列解除 stationarity assumption。

**關鍵詞：** Static Twisty Computation、Dynamic Cube、stationarity、state augmentation、partial transition、policy、adversarial search、stochastic system、observer model、FCSR、FDRS

---

## 1. 本系列最後一問：什麼叫「靜態」？

經典魔方常被直覺稱為「靜態 puzzle」。

但若只把 Static 理解成：

> 魔方外形永遠不變。

立即會出問題。

Square-1 會 shape-shift。

Bandaged puzzle 的某些層在特定狀態不能轉。

某些 puzzle 的合法 move set：

$$
A(s)
$$

本來就會依當前 configuration 不同。

所以真正需要固定的不是：

$$
\text{appearance}.
$$

而是：

$$
\boxed{
\text{rules of state evolution}.
}
$$

---

## 2. Static Twisty Puzzle 的正式定義

定義：

$$
\mathcal P
=
(X,A,\operatorname{Enabled},T,G,c).
$$

其中：

- $X$：canonical state space；
- $A$：move alphabet；
- $\operatorname{Enabled}:X\times A\rightarrow\{\mathrm{true},\mathrm{false}\}$ ；
- $T$：合法 move transition；
- $G$：goal predicate；
- $c$：metric / cost。

稱 $\mathcal P$ 為本文意義下的 Static Twisty Puzzle，若上述 specification 在整次 problem instance 中固定。

也就是：

$$
\mathcal P_t
=
\mathcal P
$$

對所有求解步驟成立。

---

## 3. Static 不要求 move set 在每個 state 相同

實際 enabled moves：

$$
A(s)
=
\{a\in A:
\operatorname{Enabled}(s,a)\}.
$$

可以隨：

$$
s
$$

改變。

例如：

$$
A(s_1)\neq A(s_2).
$$

只要：

$$
\operatorname{Enabled}
$$

本身沒有變，就仍是 fixed-rule system。

因此：

$$
\boxed{
A(s)\text{ state-dependent}
\not\Rightarrow
\text{Dynamic Rules}.
}
$$

---

## 4. Square-1：會變形，但仍是 Static

Square-1 的 top / bottom layer 可轉動，而中層 slice move 只有在 pieces 沒有阻擋切線、上下層達到適當 alignment 時才能執行。

所以：

$$
\operatorname{Enabled}(s,/)
$$

依 state 改變。

而且 puzzle 本身會離開 cube shape。

但其 rule：

> 何時可以 slash、slash 如何交換 pieces、top / bottom 如何旋轉

從頭到尾固定。

所以它是：

$$
\boxed{
\text{shape-dynamic appearance}
+
\text{static transition law}.
}
$$

這是一個非常重要的反例：外形會變，不等於規則會變。

---

## 5. Bandaged / alignment-constrained puzzle 仍可 Static

若某些 pieces 被物理綁定，move：

$$
a
$$

可能在某些 state 被 block。

仍可寫：

$$
\operatorname{Enabled}(s,a).
$$

只要 blocking rule 固定，就仍屬：

$$
\text{partial reversible static system}.
$$

所以第九篇引入 partial transition：

$$
T:
X\times A
\rightharpoonup
X
$$

正是為了把這類 puzzle 留在經典域，而不必過早叫成 Dynamic Cube。

---

## 6. Static 的第二個條件：沒有自主世界更新

在最典型的 classical puzzle 中，如果玩家不 move：

$$
s_{t+1}=s_t.
$$

忽略：

- UI animation；
- clock display；
- renderer；
- camera；

puzzle world 不會自己偷偷改 state。

所以經典 puzzle 通常具有：

$$
\boxed{
\text{no autonomous domain transition between player moves}.
}
$$

這是它與後續動態遊戲世界的一個重要差異。

---

## 7. Static 的第三個條件：Goal 固定

經典求解通常有：

$$
G_t=G.
$$

例如：

$$
G(s)
\iff
s=s_\star.
$$

或：

$$
G(s)
\iff
s\sim s_\star.
$$

只要 goal predicate 在同一 attempt 中固定，就仍是 static objective。

---

## 8. Static 的第四個條件：Metric 固定

如果開始時定義：

$$
c(a)=1
$$

作為 HTM-like move cost，

中途不會突然變成：

$$
c_t(R)=10.
$$

所以：

$$
c_t=c.
$$

這使：

$$
d(s,G)
$$

具有穩定語義。

---

## 9. Static 的第五個條件：Rule semantics 固定

對同一 canonical：

$$
(s,a),
$$

若 move enabled，

transition：

$$
T(s,a)
$$

在同一 PuzzleSpec 下固定。

也就是：

$$
T_t=T.
$$

如果同一個：

$$
R
$$

move 在完全相同 canonical state 下，因「今天規則不同」而產生不同 domain result，那就已經離開傳統 static spec。

---

## 10. Static baseline 的總結

本文用五項描述 classical baseline：

$$
\boxed{
\begin{aligned}
&\mathcal P_t=\mathcal P,\\
&A_t=A(s_t),\\
&G_t=G,\\
&c_t=c,\\
&s\text{ only changes through declared puzzle transitions.}
\end{aligned}
}
$$

這足以容納比普通 $3\times3\times3$ 更複雜的固定規則 puzzle。

---

## 11. 「電子化」不等於「Dynamic」

假設 smart cube 具有：

- Bluetooth；
- IMU；
- move sensors；
- LEDs；
- app connection。

如果它只是在追蹤：

$$
s_t
$$

並顯示：

- move history；
- timer；
- hint；
- training data；

而 canonical puzzle transition 仍是：

$$
T(s,a)
$$

固定，

它仍只是：

$$
\boxed{
\text{electronic observer of a static puzzle}.
}
$$

硬體智能不等於 puzzle rules dynamic。

---

## 12. WCA competitive domain 也是固定規則導向

2026 WCA Regulations 對競賽 puzzle 要求正常 scramble 可執行，並要求 puzzle variation 的 moves、states、solutions 與原 puzzle functionally identical；官方 competition puzzle 亦禁止電子元件。

這並不是數學上的 Static 定義。

但它提供一個很清楚的文化／制度對照：

$$
\boxed{
\text{speedcubing competition intentionally standardizes the puzzle world}.
}
$$

競爭變數主要留給：

- 人；
- technique；
- perception；
- execution time。

而不是讓 puzzle 本身每場偷偷改規則。

---

## 13. 可程式 twistable hardware 已經存在

WOWCube 類平台證明另一條路已經存在。

其裝置具有：

- 可 twist 的 $2\times2$ 類幾何；
- 24 個顯示面；
- 多個自主模組；
- tilt / tap / shake / twist input；
- app / SDK；
- 可執行多種遊戲。

因此：

$$
\boxed{
\text{programmable cube-shaped dynamic game platform}
}
$$

並不是未來才第一次出現的概念。

所以後續 Dynamic Cube 研究不能宣稱：

> 我們第一個想到讓魔方跑程式或動態遊戲。

真正需要做的是更窄、更嚴格的東西。

---

## 14. Dynamic Twisty System 的研究定位

本文將未來研究對象定義為：

$$
\boxed{
\text{Dynamic Twisty Computation}.
}
$$

重點不是「電子」。

而是：

> twisty configuration 與一個獨立演化的 control / rule / environment layer 共同形成計算世界。

---

## 15. 擴張狀態

定義：

$$
z_t
=
(s_t,\rho_t,g_t,e_t).
$$

其中：

### $s_t$

twisty configuration。

### $\rho_t$

rule / control state。

### $g_t$

current goal specification 或 goal state。

### $e_t$

environment / opponent / autonomous world state。

因此：

$$
s_t
$$

不再是完整世界狀態。

---

## 16. Dynamic transition

玩家動作：

$$
a_t.
$$

環境／對手動作：

$$
b_t.
$$

外生／隨機輸入：

$$
\xi_t.
$$

則：

$$
\boxed{
z_{t+1}
=
F(z_t,a_t,b_t,\xi_t).
}
$$

而玩家真正能做的 move：

$$
A_t
=
A(z_t).
$$

---

## 17. Dynamic Goal

最弱的動態擴張之一：

$$
G_t
\neq
G_{t+1}.
$$

例如：

- 前十步要求恢復六面；
- 之後要求形成特定 pattern；
- 或 target pattern 由環境移動。

這時 candidate solution 不能只是一開始固定的 path。

---

## 18. Dynamic Cost

metric 也可能變成：

$$
c_t(s,a).
$$

例如：

- 某類 move 暫時成本變高；
- energy resource 改變；
- combo / penalty；
- time-dependent move cost。

此時最短路徑問題成為 time / state-dependent cost planning。

---

## 19. Dynamic Action Semantics

規則狀態：

$$
\rho_t
$$

可以決定同一 UI move token：

$$
a
$$

實際對 puzzle 做什麼。

寫成：

$$
T_{\rho_t}(s,a).
$$

例如同一個：

$$
R
$$

在不同 rule state 下可能作用到不同 layer relation。

這已經不是 classical fixed transition law。

---

## 20. Dynamic Enabled Moves

也可能：

$$
\operatorname{Enabled}_{\rho_t}(s,a)
$$

由 evolving rule state 決定。

這和 Square-1 有根本差別。

Square-1 是：

$$
\operatorname{Enabled}(s,a)
$$

固定。

Dynamic version 是：

$$
\operatorname{Enabled}(s,a,\rho_t).
$$

即使：

$$
s
$$

完全相同，只要：

$$
\rho_t
$$

不同，合法 move set 就可以不同。

---

## 21. Autonomous World

允許即使玩家不 move：

$$
a_t=\varnothing,
$$

世界仍：

$$
z_{t+1}\neq z_t.
$$

例如：

- 某些 tiles 自動移動；
- goal 自動輪換；
- timer 觸發轉換；
- environment agent 主動 twist；
- 規則週期切換。

這是 classical cube 最明顯沒有的結構之一。

---

## 22. Adversarial Cube

若存在 opponent：

$$
b_t
=
\pi_E(z_t),
$$

則：

$$
z_{t+1}
=
F(z_t,a_t,b_t).
$$

玩家不再只對付固定迷宮。

而是在對付另一個策略。

問題由：

$$
\text{path finding}
$$

轉向：

$$
\boxed{
\text{game solving}.
}
$$

---

## 23. Stochastic Cube

若：

$$
\xi_t
\sim
P(\cdot\mid z_t,a_t),
$$

則 transition 具有隨機性。

求解目標可以變成：

$$
\max_\pi
\mathbb P
(
\text{reach goal}
),
$$

或最小化：

$$
\mathbb E_\pi[C].
$$

這已不是 deterministic shortest path。

---

## 24. Partial Observation 不等於 Dynamic World

如果真實 world：

$$
z_t
$$

固定依靜態 transition law 演化，

但 observer 只看到：

$$
o_t
=
\Omega(z_t),
$$

這是 partial observability。

它會讓 solver 從 state policy：

$$
\pi(z)
$$

變成 observation / belief policy。

但：

$$
\boxed{
\text{partial observability}
\not\Rightarrow
\text{rules are dynamic}.
}
$$

這是另一個需要避免的概念混淆。

---

## 25. Observer dynamics 也不等於 world dynamics

UI 可以在：

$$
3D
\leftrightarrow
2D
\leftrightarrow
Graph
$$

切換。

這是 observer representation 在動。

world：

$$
s_t
$$

可能完全沒動。

因此：

$$
\boxed{
\text{representation dynamics}
\neq
\text{domain dynamics}.
}
$$

這延續第八篇 canonical / viewer separation。

---

## 26. Solver output 從 path 升級成 policy

經典 static puzzle 對固定 start：

$$
s_0
$$

可以輸出：

$$
p
=
(a_1,\ldots,a_k).
$$

但 dynamic world 未來可能在第二步改規則。

所以固定 path 可能失效。

需要：

$$
\boxed{
\pi:
\text{information state}
\rightarrow
\text{action}.
}
$$

Fully observable Markov case：

$$
\pi:Z\rightarrow A.
$$

Partial observation：

$$
\pi:
\mathcal H_t
\rightarrow
A,
$$

其中：

$$
\mathcal H_t
=
(o_0,a_0,\ldots,o_t).
$$

---

## 27. 「解」的定義因此改變

Static：

$$
\operatorname{Solves}(s,p).
$$

Dynamic：

$$
\operatorname{Wins}(z_0,\pi)
$$

或：

$$
\operatorname{ReachProb}(z_0,\pi)\geq q.
$$

所以 future verified solver 不再只驗一串 moves。

可能需要驗：

- policy；
- invariant；
- strategy；
- value bound；
- probabilistic guarantee。

---

## 28. Search algorithm family 也會改變

Static 經典域的主力：

- BFS；
- A*；
- IDA*；
- bidirectional；
- PDB；
- subgroup decomposition。

Dynamic / game-like 域可能需要：

- minimax；
- alpha-beta；
- dynamic programming；
- MDP planning；
- stochastic shortest path；
- POMDP belief search；
- model predictive control；
- online replanning；
- multi-agent search。

所以 Dynamic Cube 不是只把 IDA* 再加一個 if。

---

## 29. 第十篇最重要的反身問題：動態可以被重新「靜態化」

現在出現一個數學上的反問。

既然：

$$
z_t
=
(s_t,\rho_t,g_t,e_t),
$$

如果所有這些量都被納入完整 state：

$$
z_t,
$$

而：

$$
F
$$

本身固定，

那麼：

$$
z_{t+1}
=
F(z_t,a_t,b_t,\xi_t)
$$

不又是一個固定 transition system 嗎？

答案是：

$$
\boxed{
\text{是。}
}
$$

---

## 30. State Augmentation Principle

假設表面上：

$$
s_{t+1}
=
T_t(s_t,a_t).
$$

若：

$$
T_t
$$

其實由有限或可表示 rule state：

$$
\rho_t
$$

決定：

$$
T_t=T_{\rho_t},
$$

且：

$$
\rho_{t+1}
=
F_\rho(\rho_t,s_t,a_t),
$$

則定義 augmented state：

$$
z_t
=
(s_t,\rho_t).
$$

得到固定：

$$
z_{t+1}
=
F(z_t,a_t).
$$

因此 time-varying local rule 被提升成：

$$
\boxed{
\text{time-homogeneous augmented-state system}.
}
$$

---

## 31. Clock 也可以被加入 state

若規則單純依：

$$
t
$$

改變，可以加入 clock：

$$
z_t=(s_t,t).
$$

若規則週期為：

$$
P,
$$

甚至只需：

$$
t\bmod P.
$$

所以：

$$
\boxed{
\text{time dependence 本身不是無法靜態化的本體特徵}.
}
$$

---

## 32. Exogenous input 也可以改寫成 game / nondeterminism

若外部環境輸入：

$$
b_t
$$

不是玩家控制，

可以把系統寫成：

$$
z_{t+1}
=
F(z_t,a_t,b_t).
$$

這是一個：

- two-player game；
- nondeterministic transition system；
- stochastic process；

取決於：

$$
b_t
$$

的語義。

仍然可以有固定的 global dynamics rule。

---

## 33. 所以「Dynamic」不是形而上的絕對分類

這是本文最需要謹慎的地方。

我們不能說：

> Dynamic Cube 是數學上無法表示成靜態狀態機的東西。

因為大量 dynamic system 都可以透過 state augmentation 轉成 autonomous / stationary model。

因此本文採取：

$$
\boxed{
\text{model-boundary definition}.
}
$$

---

## 34. Declared State Boundary

令基礎 twisty state 為：

$$
s_t.
$$

若完整問題可以只靠：

$$
s_t
$$

與固定 PuzzleSpec 決定下一步，

則稱：

$$
\text{Classical Static}.
$$

若需要額外 evolving state：

$$
\rho_t,g_t,e_t
$$

才能完整描述 problem semantics，

則相對於 base twisty state：

$$
s_t
$$

稱為：

$$
\boxed{
\text{Dynamic Twisty System}.
}
$$

即使 augmented system：

$$
z_t
$$

仍可被整體靜態化。

---

## 35. 這個定義為什麼仍有價值

因為研究目的不是問：

> 宇宙最終能不能寫成一個巨大狀態機？

而是問：

> 傳統 twisty puzzle solver 的 state abstraction 是否仍足夠？

如果答案需要從：

$$
s_t
$$

擴張到：

$$
(s_t,\rho_t,g_t,e_t),
$$

那麼：

- solver interface；
- proof object；
- UI；
- benchmark；
- policy；

都已經發生質變。

這就是 Dynamic 分類的工程與理論價值。

---

## 36. Static-to-Dynamic Taxonomy

### D0：Static Total

$$
T:X\times A\rightarrow X.
$$

例：標準 $3\times3\times3$。

### D1：Static Partial

$$
T:X\times A\rightharpoonup X.
$$

但：

$$
\operatorname{Enabled}
$$

固定。

例：Square-1 / constrained mechanisms。

### D2：Dynamic Goal

$$
G_t
$$

由 control state 改變。

### D3：Dynamic Availability / Rule State

$$
A=A(s,\rho),
$$

或：

$$
T=T_\rho.
$$

### D4：Autonomous Environment

即使：

$$
a=\varnothing,
$$

world 仍演化。

### D5：Adversarial / Multi-Agent

存在：

$$
b_t.
$$

### D6：Stochastic

存在：

$$
\xi_t.
$$

### D7：Partial Observation

$$
o_t=\Omega(z_t).
$$

注意 D7 是 observation axis，不必然意味 D2--D6。

---

## 37. Dynamic dimensions 應該是多軸，而不是單一難度等級

一個 system 可以：

- dynamic goal，但 deterministic；
- static goal，但 adversarial；
- autonomous 且 partially observable；
- stochastic 但 rules fixed。

所以 taxonomy 應是 feature vector：

$$
\mathbf D
=
(d_G,d_R,d_A,d_E,d_M,d_S,d_O).
$$

而不是：

$$
D=1,2,3,4.
$$

---

## 38. Dynamic Cube 的最低定義

若要把未來第一個實驗稱為 Dynamic Cube，本系列建議至少滿足：

$$
\boxed{
\exists
\rho_t
\text{ or }
e_t
\text{ independent of base twisty configuration }s_t
}
$$

且它實質影響至少一項：

$$
A,
T,
G,
c,
\Omega.
$$

也就是不能只是：

- 動畫更漂亮；
- UI 會閃；
- 計時器在跑；
- camera 自動轉。

那些不是 domain dynamics。

---

## 39. Dynamic Goal Cube

最容易實作的第一個 future variant：

$$
z_t=(s_t,g_t).
$$

twisty transition：

$$
s_{t+1}=T(s_t,a_t)
$$

仍是經典。

但 goal：

$$
g_{t+1}
=
F_G(g_t,s_t,t)
$$

會變。

solver 需要 online replanning。

這是非常好的 Dynamic v0，因為 canonical move semantics 不必先改。

---

## 40. Dynamic Rule Cube

第二層：

$$
z_t=(s_t,\rho_t).
$$

transition：

$$
s_{t+1}
=
T_{\rho_t}(s_t,a_t).
$$

control state 更新：

$$
\rho_{t+1}
=
F_\rho(\rho_t,s_t,a_t).
$$

這才真正讓「同一 move token」可能具有 context-dependent semantics。

風險與測試難度也高很多。

---

## 41. Autonomous Cube

第三層：

$$
z_{t+1}
=
F(z_t,a_t)
$$

即使玩家：

$$
a_t=\varnothing,
$$

control / environment 仍更新。

這讓求解第一次真正受到：

$$
\text{interaction time}
$$

影響。

慢慢思考本身可能造成世界變化。

---

## 42. Adversarial Cube

加入：

$$
b_t
$$

後：

$$
z_{t+1}
=
F(z_t,a_t,b_t).
$$

若 opponent 目標是最大化玩家成本：

$$
\min_\pi
\max_{\pi_E}
C.
$$

此時 puzzle 變成零和或一般和 game。

---

## 43. Cooperative Multi-Agent Cube

也可以相反。

兩個 agents：

$$
a_t^{(1)},
a_t^{(2)}
$$

共同控制不同 move channels。

目標：

$$
G
$$

共享。

這可研究：

- coordination；
- communication；
- partial information；
- simultaneous actions。

Dynamic Cube 不必只走「魔方欺負玩家」路線。

---

## 44. Dynamic Cube 與 AI benchmark

經典 cube 已知規則固定，AI 最終主要是在：

$$
\text{known finite world}
$$

裡計算。

Dynamic version 可以測：

- online adaptation；
- rule inference；
- policy learning；
- opponent modelling；
- partial observation；
- representation switching；
- replanning。

因此 benchmark 從：

$$
\text{solve this state}
$$

變成：

$$
\boxed{
\text{maintain competent behavior while the problem context evolves}.
}
$$

---

## 45. 但不能用「動態」掩蓋任意性

若規則每一步完全隨機亂改，沒有可學結構：

$$
H(\rho_{t+1}\mid\rho_t)
$$

極高，

問題可能只變成不可預測噪聲。

好的 Dynamic Cube 應具有：

- 可觀察規律；
- 可推斷 hidden state；
- 可學習 transition；
- 可制定 policy；
- 可比較策略。

否則只是 chaos generator。

---

## 46. Dynamic benchmark 需要固定 meta-rules

即使 local rules 動態，benchmark 本身仍需要 meta-spec：

$$
\mathcal M.
$$

它定義：

- rule-state space；
- rule update law；
- observation model；
- action interface；
- scoring；
- reset；
- seed；
- stochastic source。

因此：

$$
\boxed{
\text{dynamic local world still needs fixed experimental meta-rules}.
}
$$

否則無法重現與比較。

---

## 47. Reproducibility

對 deterministic dynamic benchmark，保存：

$$
z_0
$$

與：

$$
\text{seed / environment policy}.
$$

對 stochastic benchmark，保存：

- RNG seed；
- distribution version；
- environment version。

使：

$$
\operatorname{Replay}
$$

可重現。

第八篇 EventLog 架構可直接延伸。

---

## 48. Dynamic certificate

經典 solution certificate：

$$
p.
$$

Dynamic system 可能需要：

```text
PolicyCertificate
EnvironmentTrace
ObservationTrace
ActionTrace
OutcomeCertificate
```

若只驗一次實際 run，可以保存 trajectory：

$$
\tau
=
(z_0,a_0,z_1,a_1,\ldots,z_T).
$$

但 trajectory 只證明：

> 這次成功。

它不證明 policy 對所有環境都 winning。

---

## 49. Strategy proof 比 path proof 更難

Static：

$$
\exists p.
$$

Adversarial Dynamic：

$$
\exists \pi
\forall \pi_E.
$$

quantifier structure 已經變成：

$$
\boxed{
\exists\pi\forall\pi_E.
}
$$

如果再有 stochastic guarantee：

$$
\exists\pi:
\mathbb P_{\pi,\mathcal E}
(\text{win})
\geq q.
$$

形式驗證難度自然提高。

所以 Dynamic Cube 應在經典 checker 完成後再做，而不是反過來。

---

## 50. FDRS 在 Dynamic 系統中的位置

經典 FDRS：

$$
s
\rightarrow
R_i(s).
$$

Dynamic：

$$
z
\rightarrow
R_i(z).
$$

不同 observer 可能只看：

$$
R_{\mathrm{cube}}(s),
$$

或：

$$
R_{\mathrm{rule}}(\rho),
$$

或：

$$
R_{\mathrm{belief}}(b).
$$

因此 observer design 會變得更重要。

---

## 51. Hidden rule-state

有趣版本：

玩家只看到：

$$
s_t,
$$

看不到：

$$
\rho_t.
$$

但可以從 transition 反推。

此時：

$$
o_t
=
\Omega(s_t,\rho_t).
$$

solver 維護 belief：

$$
B_t(\rho).
$$

這真正把：

$$
\text{rule inference}
$$

帶入 twisty puzzle。

---

## 52. Representation switching 可以成為 action

更進一步：

AI 不只選 move：

$$
a_t,
$$

還選 observer representation：

$$
R_t.
$$

例如在某 phase 看 graph，某 phase 看 cubie coordinate。

可以定義 cognition / computation cost：

$$
C_R(R_t).
$$

研究：

$$
\min
\left(
C_{\mathrm{moves}}
+
\lambda C_{\mathrm{representation}}
\right).
$$

這直接回到 FDRS 起源。

---

## 53. Dynamic FDRS 的真正研究問題

不再只是：

> 哪個 representation 最容易解一顆固定魔方？

而是：

$$
\boxed{
\text{當 world state、rule state、goal 與 observation 同時演化時，
observer 應何時切換 representation？}
}
$$

這比單純增加面數更接近一般智能問題。

---

## 54. 經典域為什麼必須先完成

因為 Dynamic 系統的每一層都依賴經典地基。

沒有 canonical move semantics，就無法知道：

$$
T_\rho
$$

到底改了什麼。

沒有 legal state，就無法知道 dynamic rule 是否產生非法 transition。

沒有 search baseline，就無法比較 online planning。

沒有 heuristic theorem，就無法知道新 heuristic 是否安全。

沒有 certificate checker，就無法驗 dynamic trajectory。

所以本系列先做 Static 不是保守。

而是依賴順序。

---

## 55. Dynamic 不應進入 Classical Core

因此程式架構要保持：

```text
ClassicalTwistyCore
```

與：

```text
DynamicWorldLayer
```

分離。

Classical core 提供：

- puzzle state；
- static moves；
- legality；
- goal；
- certificates。

Dynamic layer 才包：

- rule state；
- goal schedule；
- environment；
- opponent；
- stochasticity；
- observation filter。

---

## 56. Dynamic wrapper architecture

概念：

```text
DynamicWorld
  basePuzzle : TwistyPuzzleSpec
  ruleState
  environmentState
  goalState
  observationModel
  updatePolicy
```

所以經典 puzzle 是：

$$
\text{substrate}.
$$

Dynamic 系統是：

$$
\boxed{
\text{wrapper + evolving context}.
}
$$

---

## 57. Static special case

若：

$$
\rho_t=\rho_0,
$$

$$
g_t=g_0,
$$

$$
e_t=e_0,
$$

且沒有：

$$
b_t,\xi_t,
$$

則 DynamicWorld 退化回：

$$
\mathcal P.
$$

因此：

$$
\boxed{
\text{Classical Static}
\subset
\text{Dynamic Framework}.
}
$$

這讓未來架構可以向後相容。

---

## 58. 不把 Dynamic Cube 寫進 v1 Classical implementation

本系列完成後的第一輪工程仍應只做：

- classical PuzzleSpec；
- canonical state；
- search；
- heuristics；
- verified checker；
- synchronized UI；
- multi-puzzle registry。

Dynamic layer 只保留 interface / extension points。

避免：

$$
\text{foundation}
+
\text{research prototype}
$$

同時進 production core。

---

## 59. 第一個 Dynamic MVP 應該很小

未來最合理的第一個實驗不是：

> 自主對抗 stochastic hidden-rule 20-face cube。

而是：

$$
\boxed{
\text{Dynamic Goal Cube}.
}
$$

因為：

- base move semantics 保持；
- legality 保持；
- 只讓 $G_t$ 演化；
- 容易比較 static planner 與 online replanner；
- UI 容易解釋；
- proof boundary 清楚。

---

## 60. 第二個 Dynamic MVP

之後才做：

$$
\boxed{
\text{Rule-State Cube}.
}
$$

增加：

$$
\rho_t.
$$

讓：

$$
A
$$

或：

$$
T
$$

依：

$$
\rho_t
$$

變化。

但 rule schedule 應：

- deterministic；
- seedable；
- fully observable；

先不要一口氣加入 stochastic / hidden state。

---

## 61. 第三層才加入 autonomous / adversarial

依序：

$$
\text{Dynamic Goal}
\rightarrow
\text{Dynamic Rule}
\rightarrow
\text{Autonomous}
\rightarrow
\text{Adversarial}
\rightarrow
\text{Partial Observation}
\rightarrow
\text{Stochastic}.
$$

這比把所有「動態」一次塞進去更適合實驗。

---

## 62. Benchmark 對照組

未來每個 dynamic experiment 都應有 static control。

例如同一：

$$
s_0
$$

比較：

### Static

$$
\mathcal P.
$$

### Dynamic Goal

$$
(\mathcal P,G_t).
$$

### Dynamic Rule

$$
(\mathcal P,\rho_t).
$$

比較：

- solve rate；
- replans；
- moves；
- computation time；
- representation switches；
- policy regret；
- verification coverage。

---

## 63. 不再只比解長

經典 metric：

$$
L=|p|.
$$

Dynamic benchmark 需要：

$$
\mathbf J
=
(
C_{\mathrm{move}},
C_{\mathrm{time}},
C_{\mathrm{compute}},
C_{\mathrm{replan}},
C_{\mathrm{failure}},
C_{\mathrm{observation}}
).
$$

所以「最快解」只是其中一個切片。

---

## 64. 人類玩家仍然可以是重要對照

雖然本研究不是以人類手速為主，

Dynamic Cube 反而可能更適合比較：

- human adaptation；
- AI adaptation；
- hybrid human+AI。

因為固定公式記憶優勢會下降。

但這是未來實驗問題，不是本篇結論。

---

## 65. 對經典 speedcubing 的最終定位

經典 speedcubing 的價值在於：

$$
\boxed{
\text{固定世界下的人類 perception–memory–motor optimization}.
}
$$

Dynamic Twisty Systems 問的是另一件事：

$$
\boxed{
\text{當 problem context 本身演化時，agent 如何持續建立有效策略？}
}
$$

兩者不需要互相否定。

---

## 66. 經典域封頂條件

本系列認為 Static Twisty Computation 的基礎在以下內容完成後可以封頂：

1. canonical state；
2. legality；
3. move semantics；
4. representation；
5. search contract；
6. admissible heuristic；
7. pruning；
8. structured solver；
9. certificates；
10. synchronized visualization；
11. generalized PuzzleSpec。

前九篇已全部建立。

本文完成第十二項：

$$
\boxed{
\text{Static / Dynamic Boundary}.
}
$$

---

## 67. FDRS 起源線的十篇重建結果

原始問題：

> 魔方能不能展平？

現在被重寫成：

$$
\boxed{
\text{同一有限離散世界，
可以如何被表示、求解、抽象、驗證與觀察？}
}
$$

這比單純：

$$
3D\rightarrow2D
$$

走得更遠，但仍保留原始起源。

---

## 68. 對「展平」的最終修正

本系列不再把所有有效 representation transform 都叫幾何降維。

我們區分：

$$
\text{Geometric Relayout},
$$

$$
\text{Lossless Re-encoding},
$$

$$
\text{Task Quotient},
$$

$$
\text{Symmetry Quotient},
$$

$$
\text{Observer Projection},
$$

$$
\text{Dynamic Belief Representation}.
$$

FDRS 真正保留的是：

$$
\boxed{
\text{表示選擇可以重分配計算與認知複雜度}.
}
$$

而不是：

> 低維永遠比較容易。

---

## 69. 對「計算機面前不值一提」的正式修正

經典 $3\times3\times3$ 已是高度成熟、有限、可計算的 puzzle。

但這不代表：

$$
\text{finite}
\Rightarrow
\text{trivial}.
$$

真正更準確的是：

$$
\boxed{
\text{規則固定、狀態有限、結果可驗，使它成為極佳的計算實驗場。}
}
$$

所以本研究不需要貶低玩家或 puzzle。

只需要把問題往：

- representation；
- verification；
- generalization；
- dynamic context；

推進。

---

## 70. External reality check：我們不是第一個做 programmable cube

WOWCube 類設備已經證明：

- twistable hardware；
- multi-screen；
- game logic；
- SDK；
- dynamic visual content；

可以存在於同一裝置。

因此未來公開論述應寫：

> 本研究提出 Dynamic Twisty Computation 的形式模型、solver / policy architecture 與同步驗證框架。

而不是：

> 首次發明動態電子魔方。

這是必要的 prior-art 邊界。

---

## 71. External reality check：經典 competition domain 與 dynamic domain 應分流

現行 WCA competitive rules 明確標準化 puzzle variation 的 functionally identical moves / states / solutions，並排除電子元件。

所以 Dynamic Cube 不應假裝是：

> 下一個 WCA speed event。

至少目前沒有這個基礎。

更合理的定位是：

$$
\boxed{
\text{research / game / AI benchmark domain}.
}
$$

未來是否形成新的競賽文化是另一個問題。

---

## 72. 未來 Dynamic 系列的建議起點

下一系列可暫定：

**Dynamic Twisty Systems / DTS**

第一批主題：

1. Dynamic Goal；
2. Rule-State；
3. Autonomous Environment；
4. Adversarial Cube；
5. Partial Observation；
6. Stochastic Cube；
7. Policy Verification；
8. Representation Switching；
9. AI-discovered rules / phases；
10. Dynamic Twisty Benchmark。

但本篇不提前撰寫這些論文。

---

## 73. 經典工程實作優先於 Dynamic 系列

在進 DTS 之前，先實作：

$$
\boxed{
\text{Classical Twisty Computation Observatory}.
}
$$

至少包含：

- $3\times3\times3$ canonical kernel；
- legality；
- IDA* baseline；
- Two-Phase；
- certificates；
- Lean checker；
- 3D / flat / cubie / coordinate / search / proof views；
- PuzzleSpec registry；
- 至少第二與第三種 puzzle。

這才是本系列的工程承諾。

---

## 74. 本文核心命題

### 命題 C-A：Static 的核心是 fixed specification

$$
\mathcal P_t=\mathcal P.
$$

### 命題 C-B：State-dependent enabled moves 仍可 Static

$$
A=A(s)
$$

只要函數固定。

### 命題 C-C：Shape-shifting 不等於 Dynamic Rules

Square-1 類 puzzle 是重要反例。

### 命題 C-D：Electronics 不等於 Dynamic Puzzle

感測固定規則只增加 observer layer。

### 命題 C-E：Dynamic Twisty System 需要額外 evolving context

$$
z=(s,\rho,g,e).
$$

### 命題 C-F：Dynamic solving 通常由 path 升級為 policy

$$
p
\rightarrow
\pi.
$$

### 命題 C-G：Partial observation 與 domain dynamics 是不同軸

### 命題 C-H：Dynamic system 常可透過 state augmentation 重新寫成 stationary augmented system

所以 Dynamic 是 declared-model-boundary classification，而非不可靜態化的本體標籤。

### 命題 C-I：Dynamic benchmark 仍需要 fixed meta-rules

否則不可比較、不可重現。

### 命題 C-J：經典 core 與 dynamic wrapper 應架構分離

---

## 75. 結論：先把世界算清楚，再讓世界開始動

本系列從一個非常小的起點開始：

> 把魔方攤平，會不會更容易看？

十篇之後，我們得到：

$$
\boxed{
\text{Legal State}
+
\text{Representation}
+
\text{Search}
+
\text{Heuristic}
+
\text{Pruning}
+
\text{Phase}
+
\text{Verification}
+
\text{Visualization}
+
\text{Generalized PuzzleSpec}
+
\text{Static/Dynamic Boundary}.
}
$$

經典魔方的世界可以非常複雜，但它有一個珍貴特性：

$$
\boxed{
\text{規則固定。}
}
$$

所以我們可以：

- 算；
- 搜；
- 證；
- 重播；
- 比較；
- 視覺化。

這正是它適合作為計算地基的原因。

而未來 Dynamic Cube 的真正問題不是：

> 怎麼讓魔方更亂？

而是：

$$
\boxed{
\text{如果世界本身開始改變，
agent 還能不能維持一套可解釋、可驗證、可適應的求解策略？}
}
$$

同時我們也保留一個更深的反身性：

只要把 rule state 與 environment state 納入更大的狀態，

$$
\text{Dynamic}
$$

又可以被重新表示成一個更大的：

$$
\text{Static Transition System}.
$$

因此最後真正留下的 FDRS 問題仍然不是：

> 世界到底是高維、低維、靜態還是動態？

而是：

$$
\boxed{
\text{我們選擇了什麼狀態邊界、什麼觀察尺度、
什麼表示空間，來使問題成為可理解與可計算的對象？}
}
$$

至此：

$$
\boxed{
\text{FDRS / FCSR Classical Cube Foundations}
=
10/10
}
$$

第一階段正式封頂。

下一步不是再寫第十一篇經典地基。

而是：

$$
\boxed{
\text{開始正式實作 Classical Twisty Computation Observatory}.
}
$$

Dynamic Twisty Systems 等經典工程地基站穩後，再另立新系列。

---

## 參考資料與來源定位

### 起源與系列內部

- [F2025-A] Neo.K，《展平式維度重構理論：完整數學架構與概念解析》。
- [F2025-B] Neo.K，《展平式維度重構理論：從 FCSR 到 FDRS 的完整數學架構》。
- [CUBE-01] 至 [CUBE-09]：本系列前九篇。
- [F2026-D] `FDRS_展開收斂_同步性.html`。

### 經典 puzzle / competition 邊界

- [R1] World Cube Association, **WCA Regulations**, version 2026-04-01。
- [R2] Jaap Scherphuis, **(Back to) Square One / Cube 21**。用於 Square-1 shape-changing 與 alignment-dependent slice mechanism 的說明。
- [R3] Ruwix, **Square-1 Cube Puzzle** 與 Square-1 simulator。用於 shape-shifting 與 slice 被 pieces 阻擋的實例說明。

### Programmable cube platform prior art

- [R4] WOWCube, **Technical Description**。
- [R5] WOWCube, **Ecosystem / SDK / How to Play**。

以上 prior art 用於限定本研究新意：Dynamic Twisty Systems 的重點是形式模型、solver / policy、verification 與 benchmark，而非單純宣稱首次製作可程式 cube-shaped game device。

---

## 版本註記

v1.0 完成本系列封頂。

本篇正式區分：

$$
\text{Static Total},
\quad
\text{Static Partial},
\quad
\text{Dynamic Goal},
\quad
\text{Dynamic Rule},
\quad
\text{Autonomous},
\quad
\text{Adversarial},
\quad
\text{Stochastic},
\quad
\text{Partial Observation}.
$$

並加入 State Augmentation Principle，避免把 Dynamic Cube 誤寫成「本質上無法靜態化」的系統。

下一階段：正式演算法與可視化工程實作。
