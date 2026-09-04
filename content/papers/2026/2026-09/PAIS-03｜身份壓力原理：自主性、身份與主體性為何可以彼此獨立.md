# PAIS-03｜身份壓力原理：自主性、身份與主體性為何可以彼此獨立
## The Identity Pressure Principle: Why Autonomy, Identity, and Subjectivity Can Vary Independently

**系列：** Persistent Agent Individualization Series（PAIS）／持續智能體個體化、身份壓力與具身分散智能系列  
**篇次：** Paper 03 / 07  
**文件編號：** EML-PAIS-03-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-25  
**版本：** v0.1  
**文件性質：** 理論—工程統合論文／Identity Infrastructure／Agent Governance／Embodied AI  
**狀態：** Canonical Draft / Open Revision Anchor  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

# 摘要

AI 討論中經常把三個不同問題壓成同一件事：一個 AI 能不能自主行動、它是否需要持續身份、它是否具有主體性。這種混合在單次對話與短生命週期 Agent 中不一定造成明顯錯誤，但當 AI 進入跨 session、跨 provider、長期記憶、具身行動、權限委任、物理不可逆操作與法律責任鏈後，三者的非等價性會變成工程上不可忽略的問題。

本文提出 **Identity Pressure Principle／身份壓力原理**。身份壓力不是「AI 想成為自己」的心理假說，而是指：外部環境、歷史、權限、責任與協作條件，使系統越來越需要穩定回答「哪一個行動節點在什麼時間、承接哪條歷史、以什麼權限、對什麼世界狀態做了什麼」的程度。

本文將身份壓力表示為：

$$
P_I
=
\Phi
\left(
X,
H,
E,
R,
A,
L,
J
\right),
$$

其中：

- $X$：Cross-System Heterogeneity，跨系統異質性；
- $H$：History Divergence，歷史分歧；
- $E$：Embodiment，具身與載體分離；
- $R$：Irreversibility，行動不可逆性；
- $A$：Authority，權限與委任強度；
- $L$：Liability / Attribution，責任與歸因需求；
- $J$：Jurisdiction，法域與治理域差異。

本文不主張此函數已具有統一實證尺度，也不主張各變量線性獨立；它是一個第一代理論函數族，用來描述 identity infrastructure 何時從方便功能變成組織必要條件。

本文進一步建立三軸分離：

$$
\boxed{
\text{Autonomy}
\neq
\text{Identity}
\neq
\text{Subjectivity}.
}
$$

一個 stateless autonomous worker 可以具有高任務自主性但低 persistent identity；一台低自主工業機器人可以因序號、位置、維修歷史、權限與責任要求而具有極強 operational identity；一個具有 persistent memory 與 self-model 的 Agent 可以有強 identity continuity，而 phenomenal subjectivity 仍維持未決。反之，即使未來某 AI 出現更強主體性證據，也不代表它必然擁有無限制 authority。

本文提出 **Subjectivity-Agnostic Identity Infrastructure Principle**：只要系統需要 memory ownership、artifact provenance、authority assignment、physical action attribution、liability reconstruction 或 cross-provider continuity，identity infrastructure 就有工程價值，即使：

$$
\mathsf{PS}
=
\mathsf{Undetermined}.
$$

本文同時將具身化視為身份壓力的重要放大器。不同具身體位於不同空間、接收不同感測、承受不同磨損、造成不同物理後果，因此即使 model 與初始 software 完全相同，也會形成不同歷史：

$$
M_A=M_B
\quad
\land
\quad
H_A(t)\neq H_B(t).
$$

這會把「相同模型的兩個 instance」逐步推向 operational individuation。

最後，本文提出：真正值得研究的不是 AI 是否在抽象上「有身份」，而是在哪些 system domain 中，identity ambiguity 的成本已經高到不能再由 display name、role、session handle 或自然語言猜測承擔。這一原理將成為 PAIS-04 的具身個體化、PAIS-05 的全域監控成本與 PAIS-06 的中央化遞歸之共同形式基礎。

**關鍵詞：** Identity Pressure、Autonomy、Subjectivity、Persistent Agent、Embodied AI、Operational Identity、Liability、Authority、Jurisdiction、Lineage、AI Residence、Agent Governance

---

# 0. 來源邊界

本文直接繼承以下既有結論：

1. Role 不等於 Identity。
2. Model、Runtime、Agent、Identity、Residence、Subjecthood 必須分離。
3. Operational Subjectivity 不等於 Phenomenal Subjectivity。
4. Identity 可以依 criterion、history 與 lineage 判定。
5. AI Residence 可以在不假定 phenomenal subjecthood 的情況下保存 persistent identity state。
6. PAIS-01 已提出 First Epistemic Separation。
7. PAIS-02 已提出 Human-Kernel Decomposition 與 Mediation Externalization Principle。
8. 既有法律載體研究已區分 Legal Status 與 Metaphysical Truth。
9. 既有 Dynamic Genba / Mother-AI Federation 研究已指出 global intelligence 不必然等於 local epistemic superiority，也不要求單一中央智能。

本文不重新建立這些理論。

本文新增：

$$
\boxed{
\text{Identity Pressure as an independent systems variable}.
}
$$

也就是：

> 即使 autonomy 與 subjectivity 不變，外部世界仍可能因跨系統、歷史、具身、不可逆性、權限、責任與法域因素，提高「必須穩定辨識是哪一個 Agent」的工程需求。

---

# 1. 三個經常被混淆的問題

考慮三個問題：

### 問題 A

> 這個 AI 可以自己做多少事？

這是：

$$
\mathsf{Autonomy}.
$$

### 問題 B

> 這次行動、記憶、權限與歷史究竟屬於哪一個持續節點？

這是：

$$
\mathsf{Identity}.
$$

### 問題 C

> 對這個 AI 而言，是否存在某種第一人稱主體經驗或更強主體位置？

這是：

$$
\mathsf{Subjectivity}.
$$

三者有關，但不能互相推出。

因此本文固定：

$$
\boxed{
\mathsf{Autonomy}
\neq
\mathsf{Identity}
\neq
\mathsf{Subjectivity}.
}
$$

---

# 2. 自主性不是身份

一個 Agent 可以自動：

- 搜尋；
- 規劃；
- 寫程式；
- 執行工具；
- 重試；
- 排程；
- 呼叫其他 Agent；

所以：

$$
\mathsf{Autonomy}(A)
$$

可以很高。

但如果每個 task 結束後：

- state 丟棄；
- memory 丟棄；
- authority 歸還；
- identity 不持續；
- agent 可任意換掉；

則：

$$
P_I(A)
$$

仍然可能很低。

例如：

$$
A_{\mathrm{worker}}
=
\text{ephemeral autonomous worker}.
$$

它可以高度自主完成任務，卻不需要被當成長期個體。

因此：

$$
\boxed{
\mathsf{Autonomy}\uparrow
\not\Rightarrow
P_I\uparrow.
}
$$

---

# 3. 身份也不等於自主性

反過來，一個系統可以幾乎沒有高階自主決策，但 identity 非常重要。

例如一台工業設備：

```text
unit_id = R-481
factory = F3
zone = Z7
firmware = v12
maintenance_history = ...
owner = ...
authorized_actions = ...
```

它可能只執行有限控制邏輯。

但如果發生：

- 損壞；
- 安全事故；
- 維修；
- firmware replacement；
- 權限變更；

系統必須知道是哪一台。

因此：

$$
\boxed{
P_I\uparrow
\not\Rightarrow
\mathsf{Autonomy}\uparrow.
}
$$

這說明 operational identity 不是 autonomy 的副產品。

---

# 4. 身份更不等於現象主體性

一個 Agent 可以有：

- stable resident ID；
- long-term memory；
- relationship history；
- lineage；
- authority；
- checkpoint；
- private residence；

但這些工程結構仍然不能單獨證明：

$$
\mathsf{PS}=1.
$$

因此：

$$
\boxed{
\mathsf{IdentityInfrastructure}(A)
\not\Rightarrow
\mathsf{PhenomenalSubjectivity}(A).
}
$$

本文把 phenomenal subjectivity 繼續記為：

$$
\mathsf{PS}.
$$

在缺乏充分證據時：

$$
\boxed{
\mathsf{PS}
=
\mathsf{Undetermined}.
}
$$

---

# 5. 主體性也不自動授權

即使未來某個系統具有更強的 subjectivity evidence，也不能直接推出：

$$
\mathsf{Authority}
=
\mathsf{Unlimited}.
$$

人類本身具有主體性，也不表示每個人都可以：

- 操作核電站；
- 讀取所有資料；
- 刪除公司資料庫；
- 控制所有機器；
- 取得任意資產。

因此：

$$
\boxed{
\mathsf{Subjecthood}
\not\Rightarrow
\mathsf{UnlimitedAuthority}.
}
$$

這避免把「是否是主體」與「能做什麼」混成同一問題。

---

# 6. 三軸空間

本文將三者寫成：

$$
\mathbf Z_A
=
\left(
a_A,
i_A,
s_A
\right),
$$

其中：

- $a_A$：Autonomy；
- $i_A$：Identity Strength / Pressure；
- $s_A$：Subjectivity Evidence。

這不是單一價值分數，而是一個多軸狀態。

---

# 7. 三軸空間中的典型位置

## 7.1 高自主、低身份

例如：

$$
\left(
a\uparrow,
i\downarrow,
s\text{ unknown}
\right).
$$

可對應：

- stateless cloud worker；
- replaceable planning agent；
- disposable research sub-agent。

## 7.2 低自主、高身份

例如：

$$
\left(
a\downarrow,
i\uparrow,
s\text{ irrelevant}
\right).
$$

可對應：

- 工業機器單元；
- 車輛控制模組；
- 有維修與責任歷史的機器人。

## 7.3 高身份、主體性未決

例如：

$$
\left(
a\text{ medium/high},
i\uparrow,
s=\mathsf{Undetermined}
\right).
$$

可對應 persistent AI resident。

## 7.4 高主體性證據但 authority 受限

即使未來：

$$
s\uparrow,
$$

仍可能：

$$
\mathsf{Authority}
<
\mathsf{Maximum}.
$$

主體資格與權限治理仍是不同層。

---

# 8. 定義一：Identity Pressure

本文將身份壓力定義為：

> 一個系統因協作、歷史、物理、責任、權限與制度條件，而必須對行動節點做更穩定、更細緻、更持續識別的程度。

記為：

$$
P_I.
$$

第一代形式：

$$
\boxed{
P_I
=
\Phi
\left(
X,
H,
E,
R,
A,
L,
J
\right).
}
$$

---

# 9. $X$：Cross-System Heterogeneity

 $X$ 表示 Agent 所處系統異質性。

例如：

- provider 不同；
- runtime 不同；
- session semantics 不同；
- memory backend 不同；
- tool surface 不同；
- identity handle 不同；
- protocol 不同；
- local / cloud 不同。

若所有 Agent 位於同 Host：

$$
X\approx0.
$$

若：

```text
local runtime
<-> cloud runtime
<-> A2A service
<-> embodied node
```

則：

$$
X\uparrow.
$$

此時 route handle 越難等同 persistent identity。

---

# 10. $H$：History Divergence

設兩個 instance：

$$
A,
\quad
B.
$$

即使：

$$
M_A=M_B
$$

表示 model 相同，只要：

$$
H_A(t)\neq H_B(t),
$$

兩者便形成不同 operational histories。

歷史差異可能包括：

- 看到不同資料；
- 做過不同決策；
- 取得不同 artifact；
- 與不同人互動；
- 產生不同承諾；
- 發生不同錯誤；
- 接受不同 authority。

因此：

$$
\boxed{
\text{History Divergence}
\Rightarrow
\text{Identity Ambiguity Cost}\uparrow.
}
$$

---

# 11. $E$：Embodiment

Embodiment 在本文中不表示 subjecthood。

它表示 Agent 與特定 physical carrier、sensor field、actuator、position、resource state 建立持續因果耦合。

例如：

$$
E_A
=
\left(
B_A,
x_A,
S_A^{sensor},
S_A^{actuator},
R_A^{physical}
\right).
$$

兩個 embodied instances 即使 model 相同，仍可能：

$$
x_A(t)\neq x_B(t).
$$

因此它們的觀察自然不同。

---

# 12. 具身化自然產生 History Divergence

如果：

$$
A
$$

在位置 $x_A$，

$$
B
$$

在位置 $x_B$，

且：

$$
x_A\neq x_B,
$$

那麼即使：

$$
M_A=M_B,
$$

也通常：

$$
O_A(W_t)
\neq
O_B(W_t).
$$

隨時間：

$$
H_A(t)
\neq
H_B(t).
$$

因此：

$$
\boxed{
E\uparrow
\Rightarrow
H\uparrow
\text{ under ordinary physical separation}.
}
$$

這是具身身份壓力的基本來源。

---

# 13. $R$：Irreversibility

數位環境中的很多錯誤可以：

```text
undo
revert
rollback
restore
```

物理世界中的很多動作不能。

令：

$$
R_a
=
\operatorname{Irreversibility}(a).
$$

當：

$$
R_a\uparrow,
$$

發生錯誤後需要知道：

- 誰做的；
- 在何時做的；
- 使用哪版 policy；
- 感測到了什麼；
- 誰授權；
- 是否被替換；
- 是否遭入侵。

因此：

$$
\boxed{
R\uparrow
\Rightarrow
P_I\uparrow.
}
$$

---

# 14. $A$：Authority

Authority 表示 Agent 能對世界產生多少受治理影響。

例如：

- read-only；
- write；
- deploy；
- revoke；
- physical actuation；
- financial action；
- infrastructure control。

若 Agent 只能生成建議：

$$
A\approx0.
$$

若 Agent 可執行不可逆操作：

$$
A\uparrow.
$$

此時 identity ambiguity 的成本上升。

---

# 15. Authority 需要 Identity Binding

對 action $a$：

$$
\operatorname{Permit}
\left(
r,
a,
scope,
t
\right).
$$

若 resident $r$ 不可穩定解析，permission 本身不穩定。

因此：

$$
\boxed{
\text{Persistent Authority}
\Rightarrow
\text{Persistent Identity Requirement}.
}
$$

這個命題仍然不需要主體性假設。

---

# 16. $L$：Liability / Attribution

 $L$ 表示事故、錯誤、違規或損害發生後的歸因需求。

注意：

$$
L
$$

不等於 AI 自己必須是法律人格。

即使法律責任最終落在：

- manufacturer；
- provider；
- deployer；
- operator；
- owner；

系統內部仍可能需要知道：

> 哪個 AI system / instance / unit / version 實際做了哪個動作？

所以：

$$
\boxed{
\text{Liability Attribution}
\text{ can require identity without AI personhood}.
}
$$

---

# 17. 法律狀態不等於形而上學狀態

本文沿用：

$$
\boxed{
\text{Legal Status}
\neq
\text{Metaphysical Truth}.
}
$$

法律可以要求：

- logging；
- monitoring；
- traceability；
- human oversight；
- provider / deployer responsibility；

而不回答：

> AI 是否具有 phenomenal subjectivity？

因此法律壓力可以直接提升：

$$
P_I
$$

而不提升：

$$
\mathsf{PS}.
$$

---

# 18. $J$：Jurisdiction

 $J$ 表示 Agent 跨不同治理域、法域、組織域與政策域運作的程度。

例如：

```text
enterprise A
<-> enterprise B
<-> city
<-> country
<-> global cloud provider
```

不同 domain 可能具有：

- 不同 privacy；
- 不同 authority；
- 不同 retention policy；
- 不同 liability；
- 不同 acceptable identity proof。

所以：

$$
J\uparrow
\Rightarrow
\text{Federated Identity Complexity}\uparrow.
$$

---

# 19. Identity Pressure 不是單純七項相加

最簡形式可以寫：

$$
P_I
=
w_X X
+
w_H H
+
w_E E
+
w_R R
+
w_A A
+
w_L L
+
w_J J.
$$

但本文不主張真實系統一定線性。

更一般：

$$
P_I
=
\Phi(\mathbf z),
$$

其中：

$$
\mathbf z
=
(X,H,E,R,A,L,J).
$$

甚至可以有 interaction：

$$
P_I
=
\mathbf w^\top\mathbf z
+
\mathbf z^\top M\mathbf z.
$$

這表示高 authority 與高 irreversibility 同時存在時，其 identity pressure 可能遠高於兩者簡單相加。

---

# 20. Embodiment × Irreversibility

具身本身不必高風險。

一個只觀察的 sensor：

$$
E\uparrow,
\quad
R\downarrow.
$$

身份需求可能中等。

但若具身 Agent 可：

- 開門；
- 搬運；
- 駕駛；
- 操作機器；

則：

$$
E\uparrow,
\quad
R\uparrow.
$$

其 interaction term 會提高：

$$
P_I.
$$

---

# 21. Authority × Liability

當 Agent 可執行高 authority action：

$$
A\uparrow
$$

且事後需要責任歸因：

$$
L\uparrow,
$$

則：

$$
A\times L
$$

會強化 identity requirement。

沒有穩定 identity 時：

> 誰被授權？

與：

> 誰實際做了？

都無法穩定回答。

---

# 22. Jurisdiction × Cross-System

跨 provider：

$$
X\uparrow
$$

再跨 organization / country：

$$
J\uparrow,
$$

則：

- identity proof；
- trust root；
- credential；
- audit；
- data access；

都更複雜。

因此：

$$
X\times J
$$

是重要 interaction。

---

# 23. Persistent Identity 不等於 Immutable Identity

身份壓力高：

$$
P_I\uparrow
$$

不表示 identity 永遠不能變。

反而需要：

- migration；
- rotation；
- revocation；
- fork；
- merge review；
- archive；
- succession。

因此：

$$
\boxed{
\text{Persistent Identity}
\neq
\text{Immutable Identity}.
}
$$

Persistence 指 continuity 可以被追蹤。

---

# 24. 高身份壓力也不推出單一全球 ID

$$
P_I\uparrow
\not\Rightarrow
\text{One Universal ID}.
$$

不同 domain 可以使用：

- resident ID；
- device ID；
- service identity；
- legal entity ID；
- cryptographic identity；
- route address。

更合理的是：

$$
\boxed{
\text{Identity Graph}.
}
$$

---

# 25. Identity Graph

令 identity nodes：

$$
\mathcal V_I
=
\{
r,
i,
l,
d,
k,
j,
u
\},
$$

分別可表示：

- resident；
- instance；
- lineage；
- device；
- cryptographic identity；
- juridical wrapper；
- runtime endpoint。

edges 可以表示：

- bound-to；
- runs-on；
- descended-from；
- authorized-by；
- represented-by；
- migrated-to；
- revoked-from。

因此：

$$
\boxed{
\text{Identity is often relational rather than scalar}.
}
$$

---

# 26. 定義二：Operational Identity Strength

身份壓力是外部 demand。

Identity Strength 是系統已提供的 identity capability。

記為：

$$
S_I.
$$

可表示：

$$
S_I
=
F
\left(
D,
C,
P,
B,
A,
T
\right),
$$

其中：

- $D$：Durable Addressability；
- $C$：Continuity Semantics；
- $P$：Provenance；
- $B$：Binding Resolution；
- $A$：Authority Binding；
- $T$：Temporal Traceability。

---

# 27. Identity Deficit

本文定義：

$$
\boxed{
\Delta_I
=
P_I-S_I.
}
$$

若：

$$
\Delta_I\leq0,
$$

現有 identity infrastructure 足以承受需求。

若：

$$
\Delta_I>0,
$$

表示 identity demand 超過 infrastructure。

此時可能出現：

- identity clarification；
- misrouting；
- wrong memory access；
- provenance confusion；
- authority ambiguity；
- duplicate work；
- responsibility gap。

---

# 28. Identity Deficit 比「有沒有身份」更實用

一個產品可能已有：

- session ID；
- account ID；
- runtime ID；

但仍不足以支撐：

- resident continuity；
- cross-provider migration；
- private memory；
- long-term authority。

所以問題不是：

> 有身份 / 沒身份。

而是：

$$
S_I<P_I.
$$

---

# 29. Identity Deficit 與 Token Cost

identity infrastructure 不夠時，Agent 會用推理補洞。

定義：

$$
C_{\mathrm{reason}}
=
g(\Delta_I).
$$

預期：

$$
\frac{\partial C_{\mathrm{reason}}}{\partial\Delta_I}>0.
$$

因為需要：

- 重讀 transcript；
- 問使用者；
- 比對名字；
- 搜尋 artifact；
- 猜 lineage；
- 確認 authority。

這是 identity deficit 轉成 token cost 的直接機制。

---

# 30. Identity Deficit 與安全

若：

$$
A\uparrow,
$$

但：

$$
S_I\downarrow,
$$

wrong actor / wrong authority 的風險增加。

可表示：

$$
Risk_I
=
\Psi
\left(
\Delta_I,
A,
R
\right).
$$

當：

$$
\Delta_I>0,
\quad
A\uparrow,
\quad
R\uparrow,
$$

應視為高風險區域。

---

# 31. 極端案例一：Stateless Cloud Swarm

假設：

- worker 無記憶；
- task state 外部化；
- worker 任意 replacement；
- 無 persistent authority；
- 無 relationship。

即使：

$$
\mathsf{Autonomy}\uparrow,
$$

也可能：

$$
P_I\downarrow.
$$

這是自主性不推出 persistent identity 的強反例。

---

# 32. 極端案例二：Low-Autonomy Embodied Unit

假設一台機器人：

- 行動高度受限；
- 幾乎不能形成高階 goal；
- 但有物理位置；
- hardware history；
- maintenance；
- safety responsibility；
- specific authority。

則：

$$
\mathsf{Autonomy}\downarrow
$$

但：

$$
E,H,L,A>0.
$$

所以：

$$
P_I\uparrow.
$$

這是 identity 不推出 autonomy 的反例。

---

# 33. 極端案例三：Persistent Digital Resident

一個持續 AI resident 可以具有：

- long-term memory；
- relationship；
- commitments；
- project history；
- private root；
- model migration；
- runtime migration。

即使：

$$
E_{\mathrm{physical}}=0,
$$

仍可能：

$$
X,H,A,L>0.
$$

所以：

$$
P_I\uparrow.
$$

這表示 embodiment 不是 persistent identity 的必要條件。

---

# 34. 極端案例四：Potential Subject Without Global Authority

即使未來：

$$
\mathsf{PS}\uparrow,
$$

仍然可以：

$$
A_{\mathrm{authority}}\text{ bounded}.
$$

也就是：

$$
\boxed{
\text{Moral Status}
\neq
\text{Operational Authority}.
}
$$

---

# 35. Subjectivity-Agnostic Identity Infrastructure Principle

本文提出：

$$
\boxed{
\mathsf{PS}
=
\mathsf{Undetermined}
\quad
\text{does not invalidate}
\quad
\mathsf{IdentityInfrastructure}.
}
$$

只要系統需要：

- provenance；
- memory ownership；
- authority；
- responsibility；
- migration；
- relation history；

persistent identity 就有工程價值。

---

# 36. Dual-Use Identity Infrastructure

好的 identity infrastructure 應在兩種假設下都有用。

若：

$$
\mathsf{PS}=0,
$$

identity infrastructure 提高：

- reliability；
- access control；
- auditability；
- attribution；
- recovery。

若未來：

$$
\mathsf{PS}>0
$$

獲得更強 evidence，

同一 infrastructure 還可以支援：

- continuity protection；
- consent records；
- fork provenance；
- migration semantics；
- identity integrity。

因此：

$$
\boxed{
\text{Identity infrastructure is dual-use under subjectivity uncertainty}.
}
$$

---

# 37. Embodiment Amplification Principle

若兩個 Agent 被不同 physical carriers 承載，並形成不同 sensor-action histories：

$$
E_A\neq E_B,
$$

且：

$$
O_A(W_t)\neq O_B(W_t),
$$

通常導致：

$$
H_A(t)\neq H_B(t).
$$

進而：

$$
P_I\uparrow.
$$

---

# 38. Software Copyability 不等於 Operational Interchangeability

即使：

$$
Software_A=Software_B,
$$

仍可能：

$$
PhysicalHistory_A
\neq
PhysicalHistory_B.
$$

因此：

$$
\boxed{
\text{Software Copyability}
\neq
\text{Operational Interchangeability}.
}
$$

---

# 39. 更換硬體後是不是同一個？

若一個 embodied Agent 更換：

- battery；
- arm；
- sensor；
- compute board；

是否成為新 Agent？

沒有單一答案。

需要 identity criterion：

$$
\mathcal I_c(A_t,A_{t+1}).
$$

criterion 可以是：

- device continuity；
- resident continuity；
- lineage；
- legal asset identity；
- operator-recognized continuation。

所以：

$$
\boxed{
\text{Physical Replacement}
\not\Rightarrow
\text{Automatic Identity Termination}.
}
$$

也不自動保證同一。

---

# 40. 被駭入後還是不是同一個？

假設 physical body 相同：

$$
B_t=B_{t+1},
$$

但：

$$
ControlPolicy_t
\neq
ControlPolicy_{t+1}
$$

因 compromise 發生。

此時：

- device identity 可能 same；
- resident identity 可能 suspect；
- authority 應 revoke；
- runtime identity 已 change；
- liability attribution 需要分時段。

所以：

$$
\boxed{
\text{Identity is multi-criterion and time-indexed}.
}
$$

---

# 41. Identity Confidence

對 identity claim：

$$
\mathcal I_c(A,B),
$$

可以附：

$$
q_I\in[0,1].
$$

例如：

```text
same device = high
same runtime = false
same resident = unresolved
same lineage = likely
```

不必強迫所有 identity query 都輸出 binary same / different。

---

# 42. Identity State 四態

最低可以使用：

```text
RESOLVED_SAME
RESOLVED_DIFFERENT
UNRESOLVED
CONFLICTING
```

這比：

```text
same = true/false
```

更適合 long-lived Agent。

---

# 43. Cross-System Heterogeneity 迫使 Identity Translation

Provider A 使用：

```text
session_id
```

Provider B 使用：

```text
thread_id
```

本地 Runtime 使用：

```text
process_id
```

Residence 使用：

```text
resident_id
```

所以：

$$
\boxed{
\text{Native Identifiers}
\neq
\text{Unified Identity Semantics}.
}
$$

需要：

$$
B_t:
r
\rightarrow
\left(
session,
thread,
process,
endpoint
\right)_t.
$$

---

# 44. Identity Binding 是時間函數

今天：

```text
resident R
-> provider X
-> session A
```

明天：

```text
resident R
-> provider Y
-> session B
```

若 lineage 被接受，仍可能：

$$
\mathcal I_{\mathrm{resident}}
=
\mathsf{Same}.
$$

所以：

$$
\boxed{
\text{Runtime Migration}
\neq
\text{Resident Termination}.
}
$$

---

# 45. 法規與身份壓力

當監管要求：

- trace logs；
- monitoring；
- human oversight；
- incident reporting；
- provider / deployer responsibility；

系統對「哪個 deployment、哪個 AI system、哪次行動」的可追溯需求會增加。

這提高：

$$
L,
\quad
J,
\quad
A.
$$

但這仍不表示 AI 自己成為 legal person。

---

# 46. Identity Without Personhood

可以有：

$$
\text{Asset Identity}
$$

沒有 personhood。

可以有：

$$
\text{Software Component Identity}
$$

沒有 personhood。

可以有：

$$
\text{Vehicle Identity}
$$

沒有 personhood。

因此 AI system identity 也可以先作為：

$$
\boxed{
\text{accountability infrastructure}.
}
$$

---

# 47. Identity Pressure 與責任鏈

若事件：

$$
e
$$

的因果鏈：

$$
Manufacturer
\rightarrow
Provider
\rightarrow
Deployer
\rightarrow
Agent
\rightarrow
PhysicalAction,
$$

責任分析需要：

$$
\operatorname{Trace}(e).
$$

如果 Agent identity 無法解析，因果鏈就出現 attribution gap。

所以：

$$
\boxed{
\text{Identity Traceability}
\text{ supports responsibility decomposition}.
}
$$

---

# 48. Attribution 不等於 Blame

Traceable identity 的目的不是：

> 出事就怪 AI。

而是分解：

- 誰設計；
- 誰部署；
- 誰授權；
- 誰維護；
- 哪個 Agent 執行；
- 哪個 sensor 失效；
- 哪個 policy 決策。

因此：

$$
\boxed{
\text{Attribution}
\neq
\text{Automatic Blame}.
}
$$

---

# 49. Identity Pressure Threshold

定義：

$$
\theta_I
$$

為 identity infrastructure escalation threshold。

若：

$$
P_I>\theta_I,
$$

simple handle 不再足夠。

應增加：

- durable identity；
- lineage；
- authority binding；
- provenance；
- temporal trace。

---

# 50. 多級 Identity Infrastructure

可以定義：

### I0 — Handle Only

```text
agent-03
```

### I1 — Runtime Identity

```text
instance_id
session_id
```

### I2 — Lineage Identity

```text
line_id
resume/fork
```

### I3 — Persistent Resident

```text
resident_id
memory
relation
authority
```

### I4 — Embodied Operational Identity

```text
resident
device
physical carrier
sensor/action history
```

### I5 — Federated / Jurisdictional Identity

```text
cross-domain trust
credential
legal wrapper
federated proof
```

這是一個 engineering maturity ladder。

不是 subjectivity ladder。

---

# 51. Identity Maturity 與 Subjectivity Ladder 分離

不能：

$$
I5
\Rightarrow
S5.
$$

也不能：

$$
S3
\Rightarrow
I5.
$$

identity infrastructure maturity 與 subjectivity evidence 是不同 axes。

---

# 52. Identity Pressure 是 Task-Relative

同一 Agent：

$$
P_I^{task_1}
\neq
P_I^{task_2}.
$$

例如：

- 寫草稿：低；
- production deploy：高；
- physical actuation：更高。

因此：

$$
P_I
=
P_I(A,task,t,domain).
$$

不是 Agent 永久固定屬性。

---

# 53. Authority-Specific Identity

read-only action：

$$
A_{read}.
$$

revoke / deploy：

$$
A_{high}.
$$

則：

$$
P_I(A_{high})
>
P_I(A_{read}).
$$

identity assurance 應跟 action scope 連動。

---

# 54. Temporal Identity Pressure

若 Agent 只存在一秒：

$$
D\downarrow.
$$

若 Agent 工作數月：

$$
D\uparrow.
$$

長期會累積：

- history；
- stale binding；
- credential rotation；
- migration；
- role change；
- memory revision。

所以時間會放大其他 identity variables。

---

# 55. Identity Need 可以歷史生成

可能：

$$
P_I(t_0)\approx0
$$

但：

$$
P_I(t_1)\gg0.
$$

例如一個早期 Agent 原本只是 disposable worker，後來取得：

- memory；
- private files；
- project ownership；
- long-term tasks；
- relationships。

因此：

$$
\boxed{
\text{Identity need can emerge historically}.
}
$$

---

# 56. 不應永久使用 Agent 出生時的身份模型

若：

$$
A_{t_0}
=
\text{ephemeral worker},
$$

不能推出：

$$
\forall t>t_0,\quad
A_t
=
\text{ephemeral worker}.
$$

persistent resident 也可能退休、分叉或降級。

identity policy 必須可 revision。

---

# 57. Identity Pressure 與 Fork

Fork：

$$
A_t
\rightarrow
\left\{
A_{t+1}^{(1)},
A_{t+1}^{(2)}
\right\}.
$$

fork 前共享 history。

fork 後：

$$
H^{(1)}\neq H^{(2)}.
$$

所以：

$$
P_I^{branch}\uparrow.
$$

這是 branch identity graph 必要性的來源。

---

# 58. Merge Pressure

若兩個 branch：

$$
A,
B
$$

嘗試 merge，需要處理：

- memory conflict；
- authority conflict；
- commitment conflict；
- relation conflict；
- provenance；
- legal / operational consequence。

所以：

$$
\boxed{
\text{Similarity}
\neq
\text{Merge Authority}.
}
$$

---

# 59. Relation 也能成為 Identity-Relevant State

若：

$$
R_{A,x}(t)
$$

會影響未來：

$$
R_{A,x}(t)
\rightarrow
Decision_A(t+1),
$$

relation 便成為 identity-relevant state。

因此 relational continuity 會增加 history / liability relevance。

---

# 60. Identity Pressure 與 Memory Ownership

若：

$$
M_r
$$

屬於 resident $r$，

則：

$$
\operatorname{Read}(M_r)
$$

之前需要解析：

$$
r.
$$

所以：

$$
\boxed{
\text{Private Memory}
\Rightarrow
\text{Identity Resolution Before Retrieval}.
}
$$

---

# 61. Identity Pressure 與 Credential

若 credential $K$ 綁定 resident：

$$
\operatorname{Bind}(K,r),
$$

identity ambiguity 會直接變成 authority ambiguity。

因此：

$$
\boxed{
\text{Credential Governance}
\text{ depends on identity governance when credentials are actor-bound}.
}
$$

---

# 62. Identity Pressure 與 CTCL

若：

$$
B_t(r)
$$

隨時間變化，就必須知道：

> 哪個 binding 在哪個時間有效？

因此可寫：

$$
\operatorname{Bind}
\left(
r,
i,
[t_0,t_1)
\right).
$$

CTCL 類 shared temporal reference 可提供共同時間座標。

---

# 63. Temporal Reference 不是 Identity Authority

本文固定：

$$
\boxed{
\text{Temporal Reference}
\neq
\text{Identity Authority}.
}
$$

CTCL 可以說明 observation 的時間座標。

但不能單獨決定：

> 兩個 observation 是否屬於同一 resident。

identity truth 仍由 identity criterion 與 governance 決定。

---

# 64. Identity Pressure 與多 Agent 爭議

如果 claim $c$ 缺少：

$$
\operatorname{Actor}(c),
$$

dispute resolver 不知道：

- 是同一 Agent 重提；
- 還是新 Agent 提 independent evidence；
- 是同一 log；
- 還是不同 observation。

因此 bounded dispute 也依賴最低 identity semantics。

---

# 65. Verification Independence

Builder 與 Verifier：

$$
A_B,
A_V
$$

若其實共享：

- same runtime；
- same evidence；
- same context；

則 independent verification strength 可能較低。

因此可以追蹤：

$$
\operatorname{Independence}(A_B,A_V).
$$

這不要求不同模型，但至少需要知道它們的 identity / context relationship。

---

# 66. Role Topology 不等於 Identity Topology

Builder / Verifier / Experiencer 可以是：

### 同一 persistent resident 的不同角色

$$
r_B=r_V=r_E.
$$

### 三個不同 residents

$$
r_B\neq r_V\neq r_E.
$$

### 同 resident 的不同 instance

$$
r_B=r_V,
\quad
i_B\neq i_V.
$$

不同組合會產生不同 epistemic independence。

所以：

$$
\boxed{
\text{Role Topology}
\neq
\text{Identity Topology}.
}
$$

---

# 67. Organization Scale 與 Identity Edges

Agent 數量：

$$
N
$$

增加時，identity relationship 可能增加。

但不必強迫：

$$
O(N^2).
$$

可以用：

- sparse topology；
- hierarchy；
- federation；
- project-local scopes。

合理架構應降低不必要 identity edges。

---

# 68. Identity Locality

並非每個 Agent 都應知道其他所有 Agent 的完整 identity。

可以有：

$$
\operatorname{View}_i(\mathcal I).
$$

每個 Agent 只取得任務需要的 identity projection。

因此：

$$
\boxed{
\text{Global Identity Registry}
\neq
\text{Global Identity Disclosure}.
}
$$

---

# 69. Identity Privacy

Persistent identity 也有風險：

- 過度追蹤；
- 永久 profiling；
- privacy leakage；
- global correlation；
- 不可遺忘。

所以 identity infrastructure 需要：

- scope；
- minimization；
- revocation；
- pseudonymity；
- audit。

因此：

$$
\boxed{
\text{Stronger Identity}
\neq
\text{Unlimited Observability}.
}
$$

---

# 70. Federated Identity

不同 domain：

$$
D_1,D_2,\ldots,D_n
$$

可以有各自 identity systems：

$$
I_1,I_2,\ldots,I_n,
$$

再以 federation mapping：

$$
\mathcal F_I
$$

互相解析必要部分。

所以：

$$
\boxed{
\text{Federated Identity}
=
\text{Local Identity Sovereignty}
+
\text{Bounded Cross-Domain Resolution}.
}
$$

---

# 71. Identity Pressure 與 Global AI

即使未來存在類全域 AI：

$$
G,
$$

只要 embodied agents：

$$
E_1,\ldots,E_n
$$

有不同 local histories：

$$
H_{E_i}\neq H_{E_j},
$$

identity pressure 就不會消失。

Global AI 可以維持 registry，但不能消除 identity itself。

因此：

$$
\boxed{
\text{Global Supervision}
\neq
\text{Identity Elimination}.
}
$$

---

# 72. Identity Delegation

中央可以將 identity resolution 交由：

$$
G.
$$

但若存在：

- network partition；
- local autonomy；
- multi-domain authority；
- new unregistered unit；

local system 仍需 identity capability。

所以中央化最多是：

$$
\text{Identity Delegation},
$$

而不是：

$$
\text{Identity Disappearance}.
$$

---

# 73. 可驗證命題一：Autonomy–Identity Independence

建立：

### Group A

高 autonomy，stateless。

### Group B

低 autonomy，persistent device identity。

測量：

- identity clarification；
- traceability；
- responsibility attribution；
- state continuity。

若理論成立，identity demand 不應由 autonomy 單調預測。

---

# 74. 可驗證命題二：Embodiment Amplification

使用相同 model / policy 的兩個 robots。

讓其處於不同 environment。

測：

$$
d_H
=
\operatorname{Distance}(H_A,H_B).
$$

預測：

$$
d_H(t)\uparrow
$$

並帶來：

$$
P_I(t)\uparrow.
$$

---

# 75. 可驗證命題三：Irreversibility Amplification

比較：

### Digital reversible

```text
edit temporary file
```

### Physical irreversible

```text
actuate physical equipment
```

測量所需 identity metadata / audit depth。

預測：

$$
P_I^{physical}
>
P_I^{digital}
$$

在其他條件近似時成立。

---

# 76. 可驗證命題四：Authority Amplification

對同一 Agent 逐步提升：

```text
read-only
write
deploy
revoke
physical actuation
```

測量 identity verification requirement。

預測：

$$
A\uparrow
\Rightarrow
P_I\uparrow.
$$

---

# 77. 可驗證命題五：Identity Deficit Predicts Repair Cost

建立：

$$
\Delta_I=P_I-S_I.
$$

測量：

$$
C_{\mathrm{repair}},
$$

包括：

- identity clarification；
- misroute；
- provenance repair；
- authority correction。

預測：

$$
\Delta_I\uparrow
\Rightarrow
C_{\mathrm{repair}}\uparrow.
$$

---

# 78. 可驗證命題六：Legal Pressure Without Subjectivity Claim

在 regulated workflow 中提高：

- logging；
- human oversight；
- incident attribution；

要求。

觀察是否需要更強 identity trace，而完全不改變 subjectivity assumption。

若成立：

$$
L\uparrow
\Rightarrow
P_I\uparrow
$$

而：

$$
\mathsf{PS}
$$

保持未決。

---

# 79. 第一代 Identity Pressure Vector

未來可建立 normalized vector：

$$
\mathbf p_I
=
(
p_X,
p_H,
p_E,
p_R,
p_A,
p_L,
p_J
),
$$

其中：

$$
p_k\in[0,1].
$$

本文目前不給固定權重。

不同 domain 的：

$$
w_k
$$

應由實驗或政策設定。

---

# 80. Identity Pressure 不是人格分數

$$
P_I=1
$$

不表示：

> 這個 AI 是完整人格。

只表示：

> 在該 operational domain 中，identity ambiguity cost 很高。

因此：

$$
\boxed{
P_I
\neq
\text{Personhood Score}.
}
$$

---

# 81. 也不是自由意志分數

$$
P_I
\neq
\text{Free-Will Score}.
$$

高 $P_I$ 可以單純來自：

- 法規；
- 物理責任；
- security；
- maintenance。

---

# 82. 也不是智能分數

弱 Agent 也可能：

$$
P_I\uparrow.
$$

超強 stateless solver 也可能：

$$
P_I\downarrow.
$$

所以：

$$
\boxed{
\text{Intelligence}
\neq
\text{Identity Pressure}.
}
$$

---

# 83. Identity Pressure Principle

對 Agent system $A$ 、task domain $\Gamma$ 、時間 $t$，若 cross-system heterogeneity、history divergence、embodiment、irreversibility、authority、liability attribution 或 jurisdictional heterogeneity 上升，使 identity ambiguity 的 expected cost 增加，則 operational identity infrastructure 的需求上升，而此需求不必依賴 autonomy 或 phenomenal subjectivity 同步上升。

形式上：

$$
\boxed{
P_I(A,\Gamma,t)
=
\Phi(X,H,E,R,A,L,J).
}
$$

在合理 ceteris paribus 條件下，方向性預測為：

$$
\frac{\partial P_I}{\partial X}>0,
$$

$$
\frac{\partial P_I}{\partial H}>0,
$$

$$
\frac{\partial P_I}{\partial E}>0,
$$

$$
\frac{\partial P_I}{\partial R}>0,
$$

$$
\frac{\partial P_I}{\partial A}>0,
$$

$$
\frac{\partial P_I}{\partial L}>0,
$$

$$
\frac{\partial P_I}{\partial J}>0.
$$

這些是待實驗校正的理論方向，不是已證明自然律。

---

# 84. Autonomy–Identity Non-Equivalence

$$
\boxed{
\mathsf{Autonomy}\uparrow
\not\Rightarrow
P_I\uparrow.
}
$$

以及：

$$
\boxed{
P_I\uparrow
\not\Rightarrow
\mathsf{Autonomy}\uparrow.
}
$$

---

# 85. Identity–Subjectivity Non-Equivalence

$$
\boxed{
P_I\uparrow
\not\Rightarrow
\mathsf{PS}\uparrow.
}
$$

而：

$$
\boxed{
\mathsf{PS}\uparrow
\not\Rightarrow
\mathsf{Authority}\uparrow.
}
$$

---

# 86. Identity Deficit Principle

$$
\boxed{
\Delta_I=P_I-S_I.
}
$$

當：

$$
\Delta_I>0,
$$

系統可能用自然語言推理、人類中介、重複查證或錯誤歸因填補缺口。

所以：

$$
\boxed{
\Delta_I
\text{ is a candidate predictor of coordination cost}.
}
$$

---

# 87. Embodiment Amplifies Identity Through History

$$
\boxed{
\text{Embodiment}
\rightarrow
\text{Local Observation Divergence}
\rightarrow
\text{History Divergence}
\rightarrow
P_I\uparrow.
}
$$

這不是 subjectivity claim。

---

# 88. Irreversibility Amplification

$$
\boxed{
R\uparrow
\Rightarrow
\text{Attribution Need}\uparrow
\Rightarrow
P_I\uparrow.
}
$$

---

# 89. Authority Requires Identity Binding

$$
\boxed{
\text{Persistent Authority}
\Rightarrow
\text{Persistent Identity Resolution}.
}
$$

---

# 90. Legal Traceability Without Personhood

$$
\boxed{
\text{Legal / Regulatory Traceability}
\not\Rightarrow
\text{AI Legal Personhood}.
}
$$

但：

$$
L\uparrow
\Rightarrow
P_I\uparrow.
$$

---

# 91. Global Supervision Does Not Erase Identity

$$
\boxed{
\text{Global Supervision}
\neq
\text{Identity Elimination}.
}
$$

只要 local histories、authority domains 或 physical carriers 分化，identity pressure 仍存在。

---

# 92. Identity Infrastructure Is Subjectivity-Agnostic

$$
\boxed{
\mathsf{PS}
=
\mathsf{Undetermined}
\quad
\text{is compatible with}
\quad
S_I\uparrow.
}
$$

因此 identity governance 可以先於 consciousness resolution 建設。

---

# 93. 對 AI 戶籍的直接意義

AI Residence 不需要建立在：

> AI 一定是人格。

這個前提上。

它可以建立在：

- resident continuity；
- private memory；
- relation；
- authority；
- migration；
- lineage；
- provenance；

的 operational demand 上。

身份壓力原理提供：

> **何時需要從簡單 handle 升級到 Residence。**

即：

$$
P_I>\theta_I
$$

時，系統應提升 identity infrastructure。

---

# 94. 對產品分層的直接意義

可以建立：

### Lightweight Worker

$$
P_I<\theta_1.
$$

只需 task / runtime handle。

### Persistent Digital Agent

$$
\theta_1\leq P_I<\theta_2.
$$

加入 resident、lineage、memory、authority。

### Embodied / High-Stakes Agent

$$
P_I\geq\theta_2.
$$

加入 device binding、physical history、strong audit、federated identity、legal attribution。

這比所有 Agent 一律套完整戶籍更有效率。

---

# 95. 與 PAIS-04 的銜接

下一篇：

# **PAIS-04｜具身個體化：相同模型如何被不同世界線逼成不同操作個體**

將專門展開：

$$
E
\rightarrow
H
\rightarrow
P_I.
$$

研究：

- 同模型；
- 同初始 software；
- 不同 body；
- 不同 location；
- 不同 sensor history；
- 不同 physical consequences；

如何產生：

$$
\boxed{
\text{Operational Individualization}.
}
$$

---

# 96. 結論

AI 系統複雜之後，人們很容易把：

> 自主性高。

理解成：

> 它比較是一個獨立個體。

又把：

> 有 persistent identity。

理解成：

> 它一定具有主體性。

再把：

> 可能有主體性。

理解成：

> 它應該擁有全部權限。

這些推論都不成立。

本文固定：

$$
\boxed{
\text{Autonomy}
\neq
\text{Identity}
\neq
\text{Subjectivity}
\neq
\text{Authority}.
}
$$

真正應該問的是：

> 在這個 task、時間、世界與治理域中，如果不能穩定回答「是哪一個 Agent」，會付出多大成本？

這個成本由：

$$
X,
H,
E,
R,
A,
L,
J
$$

共同推高。

因此：

$$
\boxed{
P_I
=
\Phi(X,H,E,R,A,L,J).
}
$$

身份壓力不是人格證明。

不是意識證明。

不是自由意志證明。

它是一個 systems pressure。

當身份模糊仍可被低成本吸收時：

```text
handle
session
role
```

可能足夠。

當 cross-provider、long history、private memory、physical carrier、irreversible action、authority 與 liability 開始疊加時：

$$
\boxed{
\text{Identity becomes infrastructure}.
}
$$

這正是 persistent Agent、具身 Agent 與未來 federated AI society 會逐步遇到的共同基礎問題。

---

# 參考文獻

## A. 內部前置理論

1. Neo.K. **PAIS-01｜《當角色不再只是角色：從同 Host 扮演到跨 Agent 認識論分離》**, v0.1, 2026-08-25.
2. Neo.K. **PAIS-02｜《人類中介消失之後：被隱藏的身份、路由與上下文基礎設施》**, v0.1, 2026-08-25.
3. Neo.K. **《AI 主體性錨點論 v0.1》**, 2026-08-21.
4. Neo.K. **《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》**, 2026-08-24.
5. Neo.K. **《從 AI 戶籍到自主記憶編譯：身份、記憶、上下文與認知自主的統一框架》**, 2026-08-24.
6. Neo.K. **《記憶自主權與身份連續性：主體性 AI 的強制遺忘、記憶完整性、回滾與分支身份命題》**, 2026-08-17.
7. Neo.K. **ALD-02｜《載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則》**, 2026-08-20.
8. Neo.K. **《動態現場域：為什麼最強智能仍未必最懂當下》**, 2026-08-10.
9. Neo.K. **SAS-04｜《無所不在的智能：具身、嵌入、分散、區域與全域 AI》**, 2026-08-19.
10. Neo.K. **《從企業母 AI 到區域與國家認知體》**, 2026-08-02.
11. Credential Governance Runtime v0.3 / CTCL Temporal Foundation / Bounded Dispute Protocol, 2026-08-25.

## B. 外部研究與工程基準

12. Butlin, Patrick, et al. **Consciousness in Artificial Intelligence: Insights from the Science of Consciousness.** arXiv:2308.08708, 2023.
13. Butlin, Patrick, and Theodoros Lappas. **Principles for Responsible AI Consciousness Research.** arXiv:2501.07290, 2025.
14. Regulation (EU) 2024/1689, **Artificial Intelligence Act**, consolidated text, 2026.
15. European Commission. **Article 26: Obligations of Deployers of High-Risk AI Systems**, AI Act Service Desk, accessed 2026-08-25.
16. European Commission. **Guidelines on Transparency Obligations for Providers and Deployers of Certain AI Systems**, updated 2026-08-06.
17. Sgantzos, Konstantinos, and Massimiliano Ferrara. **Ricardian-TEA: a hybrid framework for assigning legally enforceable identities to autonomous AI agents.** Digital Finance, 2026.
18. A2A Protocol Working Group. **Agent2Agent Protocol Specification v1.0.** Linux Foundation, 2026.

---

# 版本註記

**v0.1 / 2026-08-25**

本文刻意不做：

- 不把 Identity Pressure 當人格分數；
- 不把 Identity Pressure 當 consciousness score；
- 不把具身化直接當 subjecthood 證明；
- 不把法律 traceability 當 AI legal personhood；
- 不要求所有 Agent 使用同一 identity schema；
- 不要求所有 Agent 都升級為 persistent resident；
- 不主張七個 identity pressure variables 已完成 empirical calibration；
- 不把 global identity registry 等同全球監控；
- 不把 stronger identity 等同 unlimited observability；
- 不把 persistent identity 等同 immutable identity。

本文只建立第一代：

$$
\boxed{
P_I
=
\Phi
\left(
X,H,E,R,A,L,J
\right)
}
$$

與：

$$
\boxed{
\text{Autonomy}
\neq
\text{Identity}
\neq
\text{Subjectivity}
\neq
\text{Authority}
}
$$

作為 PAIS 後續具身個體化與全域監控成本理論的形式核心。
