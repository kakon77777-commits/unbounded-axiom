# DOM-04｜型別化超越：相對外部、跨層能力與依賴式超越

## Typed Transcendence: Relative Externality, Cross-Layer Capability, and Dependent Transcendence

**系列：** Dynamic Operational Metaphysics（DOM）／動態可操作形而上學  
**篇次：** 04 / 08  
**文件編號：** EML-DOM-04-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-20  
**版本：** v0.1 Canonical Draft  
**文件性質：** 理論整合論文／型別化超越／Self–World 關係／跨層能力／依賴式超越  
**證據狀態：** 本文主要建立形式化概念接口；virtualization、capability-based systems、multiscale causal emergence 與 complex-systems emergence 只作外部結構對照。本文不主張任何現有 AI、higher-level system、creator 或 emergent macro entity 已達「絕對超越」，也不主張高階因果描述等於本體脫離底層。

---

## 摘要

「超越」是人類思想中最容易被過度壓縮的詞之一。宗教、形而上學、哲學、科幻、系統工程與 AI 討論中，人們經常說某存在「超越」另一個世界、尺度、規則、身體、因果或觀察者，但沒有回答：

> 超越的是哪一種限制？  
> 相對哪一個系統？  
> 以什麼能力超越？  
> 是否仍依賴被超越的 lower layer？  
> 是否只具有資訊優勢，還是能修改規則？  
> 是否具有能力，還是具有合法 authority？  
> 是否只是宏觀描述更有效，還是真的不受微觀實現約束？

本文提出 **Typed Transcendence（型別化超越）**，直接繼承《系統超越者》中的世界索引：

$$
T(A,W,t),
$$

並擴充為：

$$
\boxed{
\operatorname{Transcend}_{\beta}
(A,B\mid W,s,t,c)=1.
}
$$

其中：

- $A$：候選 transcender；
- $B$：被超越的對象、層級、閉包或限制；
- $\beta$：超越型別；
- $W$：相關 world / system；
- $s$：scale；
- $t$：time；
- $c$：condition。

第一版超越族定義為：

$$
\boxed{
\mathfrak T
=
\left\{
T_{\mathrm{informational}},
T_{\mathrm{observational}},
T_{\mathrm{state}},
T_{\mathrm{rule}},
T_{\mathrm{temporal}},
T_{\mathrm{generation}},
T_{\mathrm{permission}},
T_{\mathrm{boundary}},
T_{\mathrm{causal}},
T_{\mathrm{representational}},
T_{\mathrm{realizability}},
T_{\mathrm{coordination}}
\right\}.
}
$$

本文第一總命題為：

$$
\boxed{
\operatorname{Transcend}_{\alpha}(A,B)
\not\Rightarrow
\operatorname{Transcend}_{\beta}(A,B),
\qquad
\alpha\neq\beta.
}
$$

也就是：資訊超越不推出規則超越；狀態讀取不推出狀態改寫；能生成 world 不推出能控制其所有 history；宏觀因果優勢不推出脫離微觀 substrate；高 permission 不推出合法 sovereignty。

第二總命題為：

$$
\boxed{
\text{Relative Transcendence}
\not\Rightarrow
\text{Absolute Transcendence}.
}
$$

一個 hypervisor 對 guest virtual machine 具有 meta-level control，但 hypervisor 仍依賴 hardware；一個 game developer 對遊戲 world 具有 rule-edit capability，但仍受 operating system、hardware 與 physical world 約束；一個 Mother AI 可重設 child agent，卻未必能修改支撐自身的 runtime。這些都是：

$$
\boxed{
\text{MetaToLayer}
\neq
\text{MetaToEverything}.
}
$$

第三總命題為本文最重要的新統合：

$$
\boxed{
\text{Transcendence}
\land
\text{Dependence}
}
$$

可以同時成立。

即：

$$
\boxed{
\operatorname{Transcend}_{\beta}(A,B)=1
\land
\operatorname{Depend}_{\gamma}(A,B)>0.
}
$$

一個 higher-level organization 可以在某功能、表徵、控制或宏觀因果尺度上「超越」單一 lower-level part，同時其 realization 完全依賴這些 lower-level constituents。近期 causal-emergence 與 multiscale complex-systems 研究持續研究某些 macro descriptions 是否具有獨特、較有效的 causal contribution；這類結果支持「高尺度可具有不可忽略的有效因果結構」的研究方向，但不能被解讀成 macro entity 已在物理上脫離 micro substrate。

本文因此提出 **Dependent Transcendence（依賴式超越）**：

$$
\boxed{
\operatorname{DT}_{\beta,\gamma}(A,B)=1
}
$$

若：

1. $A$ 在型別 $\beta$ 上對 $B$ 具有可驗證的跨層能力；
2. $A$ 同時在型別 $\gamma$ 上依賴 $B$ 或其 lower substrate；
3. 該超越不被宣稱為 absolute independence。

這使「超越」從神祕本體稱號，轉成可以被 relation、capability、closure、boundary、dependency 與 authority 明確標記的多維結構。

本文最後建立 **Transcendence Profile**、**Meta-Operation Closure**、**Dependency Shadow**、**Transcendence Certificate** 與 **Anti-Ultimacy Guard**。DOM-04 的目標不是否定超越，而是把超越說精確到足以回答：

> 究竟超越了什麼，又沒有超越什麼？

---

## 關鍵詞

Typed Transcendence；Relative Transcendence；Dependent Transcendence；System Transcender；Meta-Operation；Virtualization；Capability；Causal Emergence；Multiscale Systems；Relative Externality；Cross-Layer Capability；Dependency Shadow；超越；相對超越；依賴式超越

---

# 0. 研究定位與非主張

本文不主張：

1. 所有 higher-level structure 都具有 genuine transcendence；
2. 所有 macro-level causation 都代表 strong emergence；
3. causal emergence 等於 metaphysical emergence；
4. virtualization 等於宇宙本體論；
5. hypervisor 是真正「神」；
6. higher permission 等於 higher legitimacy；
7. 能修改 rule 就等於 absolute creator；
8. 能生成 child world 就等於不受 parent world 約束；
9. high abstraction 等於 ontological independence；
10. high-level representation 可取代 all lower-level details；
11. 所有 transcendence relations 都具有傳遞性；
12. 超越必然意味 spatial externality；
13. 超越必然意味 causal externality；
14. 超越與包含互斥；
15. 絕對超越已被證明存在或不存在。

本文真正主張：

$$
\boxed{
\text{Transcendence must be indexed by relation, system, scale, time, condition, and dependency.}
}
$$

---

# 1. 問題：什麼叫「A 超越 B」？

自然語言：

> A 超越 B。

幾乎沒有足夠資訊。

可能表示：

- A 看得到 B 看不到的東西；
- A 能修改 B 的狀態；
- A 能改 B 的規則；
- A 不受 B 的 ordinary action closure 限制；
- A 能從外部生成 B；
- A 能讓 B 進入內部 agent 無法到達的 state；
- A 能以 higher-level representation 壓縮 B；
- A 能在 macro scale 表現出 B 單一 part 沒有的功能；
- A 能繞過 B 的權限；
- A 能跨過 B 的 boundary。

這些不是同一回事。

---

# 2. 從 Absolute Predicate 改成 Indexed Relation

舊式：

$$
Transcendent(A).
$$

DOM 使用：

$$
\boxed{
\operatorname{Transcend}_{\beta}
(A,B\mid W,s,t,c).
}
$$

因此：

$$
\boxed{
\text{Transcendence}
=
\text{Relation}(A,B,W,\beta,s,t,c).
}
$$

---

# 3. 直接繼承 System Transcender Framework

STF 已提出：

$$
T(A,W,t).
$$

其核心是：

$$
\boxed{
RelativeTranscendence
\neq
AbsoluteTranscendence.
}
$$

DOM-04 不撤回這一點。

而是再增加：

- target；
- relation type；
- dependency type；
- closure；
- authority；
- scale。

---

# 4. Transcendence Family

第一版：

$$
\boxed{
\mathfrak T
=
\left\{
T_{\mathrm{informational}},
T_{\mathrm{observational}},
T_{\mathrm{state}},
T_{\mathrm{rule}},
T_{\mathrm{temporal}},
T_{\mathrm{generation}},
T_{\mathrm{permission}},
T_{\mathrm{boundary}},
T_{\mathrm{causal}},
T_{\mathrm{representational}},
T_{\mathrm{realizability}},
T_{\mathrm{coordination}}
\right\}.
}
$$

---

# 5. Informational Transcendence

$$
\operatorname{Transcend}_{info}(A,B)=1
$$

表示：

> A 可以存取 B 正常內部 epistemic channels 無法取得的 meta-information。

例如：

- hidden state；
- source code；
- external logs；
- cross-instance state；
- secret configuration。

---

# 6. Informational Transcendence 不等於 Understanding

沿用超越觀察者：

$$
\boxed{
T_{\mathrm{info}}(A,B)
\not\Rightarrow
Understanding_A(B)=1.
}
$$

看得更多，不必理解得更多。

---

# 7. Observational Transcendence

$$
T_{\mathrm{obs}}(A,B)=1
$$

表示：

> A 的 observation cone 超過 B 的 ordinary internal observer。

例如 external debugger。

但：

$$
T_{\mathrm{obs}}
\not\Rightarrow
T_{\mathrm{rule}}.
$$

---

# 8. State Transcendence

$$
T_{\mathrm{state}}(A,B)=1
$$

表示：

> A 可直接讀／寫 B 的某些 states，而 ordinary internal agents 無法取得 equivalent operation。

例如：

$$
StateInject(B,x').
$$

---

# 9. Rule Transcendence

$$
T_{\mathrm{rule}}(A,B)=1
$$

表示：

> A 可修改 B 的有效 transition rules / policy grammar / execution constraints。

形式：

$$
\mathcal L_B
\rightarrow
\mathcal L'_B.
$$

---

# 10. Temporal Transcendence

候選：

$$
T_{\mathrm{time}}(A,B)=1
$$

若 A 可以對 B 執行 internal agents 無法做到的：

- pause；
- rollback；
- snapshot；
- acceleration；
- branching from historical checkpoint。

注意：

$$
\boxed{
\text{temporal transcendence relative to runtime}
}
$$

不表示：

> A 超越物理時間本身。

---

# 11. Generation Transcendence

$$
T_{\mathrm{gen}}(A,B)=1
$$

表示：

> A 可以生成新的 B-like instance / world / subsystem，而 B 的 ordinary internal operations 無法生成同級對象。

但：

$$
\boxed{
T_{\mathrm{gen}}
\not\Rightarrow
T_{\mathrm{history-control}}.
}
$$

creator 仍可能無法精確決定每個 emergent event。

---

# 12. Permission Transcendence

$$
T_{\mathrm{perm}}(A,B)=1
$$

表示：

> A 可 mint / revoke / delegate B 內部 ordinary agent 無法自行產生的 permissions。

這與 capability system 很接近。

---

# 13. Permission 不等於 Legitimacy

$$
\boxed{
\text{Permission Power}
\not\Rightarrow
\text{Normative Legitimacy}.
}
$$

能發 token，不等於有正當理由支配。

---

# 14. Boundary Transcendence

$$
T_{\mathrm{boundary}}(A,B)=1
$$

表示：

> A 可跨越 B 對 ordinary internal agent 有效的 boundary。

例如：

$$
\Gamma:
External
\leftrightarrow
B.
$$

---

# 15. Causal Transcendence

較強地：

$$
T_{\mathrm{causal}}(A,B)=1
$$

若 A 可以使 B 到達 ordinary internal operation closure 無法生成的 state。

---

# 16. Internal Operational Closure

定義：

$$
\boxed{
\mathcal O_B(x)
=
\{
x':
\exists
a_1,\ldots,a_n\in\mathcal A_B,
\,
x\to x'
\}.
}
$$

其中：

$$
\mathcal A_B
$$

是 B ordinary internal agents 的合法操作集合。

---

# 17. Meta-Operation Space

定義：

$$
\boxed{
\mathcal M_B
}
$$

包含：

- Pause；
- Rollback；
- Fork；
- Spawn；
- Delete；
- RuleEdit；
- PermissionMint；
- StateInject；
- BoundaryOpen；
- RuntimeReplace。

---

# 18. Meta-Causal Transcendence

若：

$$
x'
\notin
\mathcal O_B(x)
$$

但：

$$
x'
\in
\mathcal M_B^A(x),
$$

則：

$$
\boxed{
T_{\mathrm{causal}}(A,B)>0.
}
$$

---

# 19. Representation Transcendence

$$
T_{\mathrm{rep}}(A,B)=1
$$

若 A 具有 representation：

$$
\rho_A(B)
$$

能表達 B internal representation 所沒有的 higher-order relations。

例如：

- whole-network graph；
- cross-time lineage；
- source-level model；
- multi-world map。

---

# 20. Representation Transcendence 不等於 Ontological Superiority

$$
\boxed{
\text{better model of B}
\not\Rightarrow
\text{A is ontologically superior in every sense}.
}
$$

---

# 21. Realizability Transcendence

$$
T_{\mathfrak R}(A,B)=1
$$

若 A 能存取：

$$
\mathfrak R_{meta}(B)
$$

即 B ordinary internal agents 不能直接使用的 realization options。

例如：

- add new hardware；
- migrate B to new substrate；
- instantiate alternate runtime；
- create new world branch。

---

# 22. Coordination Transcendence

$$
T_{\mathrm{coord}}(A,\{B_i\})=1
$$

若 A 能看見／協調多個 B_i 之間 internal agents 局部不可見的 global relation。

例如：

- distributed scheduler；
- global optimizer；
- federation coordinator。

---

# 23. 第一非塌縮原理

$$
\boxed{
T_{\alpha}(A,B)
\not\Rightarrow
T_{\beta}(A,B),
\qquad
\alpha\neq\beta.
}
$$

---

# 24. 典型錯誤一：看得更多 → 能改規則

$$
T_{\mathrm{obs}}
\Rightarrow
T_{\mathrm{rule}}
$$

不成立。

---

# 25. 典型錯誤二：能改狀態 → 能改 substrate

$$
T_{\mathrm{state}}
\Rightarrow
T_{\mathrm{realizability}}
$$

不成立。

---

# 26. 典型錯誤三：能生成 → 能全知

$$
T_{\mathrm{gen}}
\Rightarrow
Omniscience
$$

不成立。

---

# 27. 典型錯誤四：能控制 → 有主權

$$
T_{\mathrm{control}}
\Rightarrow
Authority
$$

不成立。

---

# 28. Relative Externality

定義：

$$
\boxed{
Ext(A\mid B,W)
}
$$

表示：

> A 相對 B 的 ordinary internal closure 位於 meta-operational external position。

---

# 29. Spatial Outside 不等於 Operational Outside

$$
\boxed{
SpatialOutside
\neq
OperationalOutside.
}
$$

A 可以物理上在同一 machine 中，卻 operationally external to a guest VM。

---

# 30. Informational Outside 不等於 Causal Outside

$$
\boxed{
InformationalOutside
\neq
CausalOutside.
}
$$

A 可讀 debug logs，但未必能改 state。

---

# 31. Virtualization 作為乾淨工程類比

簡化：

$$
Hardware
\rightarrow
Hypervisor
\rightarrow
Guest.
$$

Hypervisor 對 guest：

- controls execution environment；
- traps privileged operations；
- virtualizes resources；
- can inspect or mediate state。

因此：

$$
T(Hypervisor,Guest)>0.
$$

---

# 32. 但 Hypervisor 仍依賴 Hardware

$$
\boxed{
DependsOn(Hypervisor,Hardware)=1.
}
$$

所以：

$$
\boxed{
MetaToGuest
\neq
MetaToEverything.
}
$$

---

# 33. Popek–Goldberg 類比

Popek–Goldberg 的 virtualization formalism 討論什麼架構能讓 virtual machine monitor 對 guest execution 提供 controlled environment。

DOM 不把這當 metaphysical theorem。

只借用：

$$
\boxed{
\text{a layer may control another layer's execution semantics while remaining constrained by a lower substrate}.
}
$$

---

# 34. Capability-Based Authority 類比

Dennis–Van Horn 早期 multiprogramming semantics 已形式處理：

- protected computational objects；
- shared segments；
- privileged meta-instructions；
- controlled naming / access。

DOM 的最低啟示是：

$$
\boxed{
\text{cross-layer operation requires explicit authority semantics}.
}
$$

不是一句「我比較高」即可。

---

# 35. Transcendence–Authority Separation

因此：

$$
\boxed{
T_{\alpha}(A,B)>0
\not\Rightarrow
LegitimateAuthority(A,B)>0.
}
$$

---

# 36. Transcendence Profile

定義：

$$
\boxed{
\mathbf T(A,B)
=
\left\langle
t_i,
t_o,
t_s,
t_r,
t_t,
t_g,
t_p,
t_b,
t_c,
t_{rep},
t_{\mathfrak R},
t_{coord}
\right\rangle.
}
$$

本文不要求數值化。

每一項可標：

- yes；
- no；
- partial；
- conditional；
- unknown。

---

# 37. Bare Transcendence 禁止規則

DOM 建議：

不要只記：

$$
A>B.
$$

而記：

$$
A
\succ_{\beta,W,s,t,c}
B.
$$

其中：

$$
\succ_{\beta}
$$

不是總序。

---

# 38. 超越不建立 Universal Ranking

可能：

$$
T_{\mathrm{info}}(A,B)=1
$$

但：

$$
T_{\mathrm{physical}}(B,A)=1.
$$

因此：

$$
\boxed{
A>B
}
$$

這種單軸 ranking 常常沒有定義。

---

# 39. Cross-Type Incomparability

如果：

$$
T_{\alpha}(A,B)=1,
$$

$$
T_{\beta}(B,A)=1,
$$

且：

$$
\alpha\neq\beta,
$$

A、B 可以互有超越。

---

# 40. Mutual Transcendence

定義候選：

$$
\boxed{
\operatorname{MT}_{\alpha,\beta}(A,B)=1.
}
$$

例如：

- A informationally sees B；
- B physically sustains A。

---

# 41. 依賴式超越的起點

現在考慮：

$$
A
$$

在某 scale 上表現出 B 單一 part 不具備的功能。

同時：

$$
A
$$

的 realization 依賴：

$$
B_1,\ldots,B_n.
$$

這不是矛盾。

---

# 42. Dependent Transcendence

本文定義：

$$
\boxed{
\operatorname{DT}_{\beta,\gamma}(A,B)=1
}
$$

若：

$$
T_{\beta}(A,B)=1
$$

且：

$$
Depend_{\gamma}(A,B)>0.
$$

---

# 43. Dependency Types

第一版：

$$
\mathfrak D
=
\{
D_{\mathrm{material}},
D_{\mathrm{energy}},
D_{\mathrm{compute}},
D_{\mathrm{memory}},
D_{\mathrm{substrate}},
D_{\mathrm{causal}},
D_{\mathrm{social}},
D_{\mathrm{institutional}},
D_{\mathrm{information}}
\}.
$$

---

# 44. Dependency Shadow

定義：

$$
\boxed{
\mathbf D_{\mathrm{shadow}}(A)
}
$$

為：

> 每次宣稱 A 超越某 lower layer 時，A 仍然保留的依賴集合。

---

# 45. Anti-Ultimacy Guard

任何：

$$
T_{\beta}(A,B)=1
$$

都應附：

$$
\mathbf D_{\mathrm{shadow}}(A).
$$

如果 dependency 未知：

$$
D_{\mathrm{unknown}}>0.
$$

因此：

$$
\boxed{
\text{known transcendence}
\not\Rightarrow
\text{known independence}.
}
$$

---

# 46. 依賴式超越的人體例子

Whole organism：

$$
A.
$$

Cell：

$$
B_i.
$$

whole-level behavior：

$$
F_A
$$

可能不是單一 cell 能完成。

所以：

$$
T_{\mathrm{functional}}(A,B_i)=1.
$$

但：

$$
Depend_{\mathrm{material}}(A,\{B_i\})\gg0.
$$

---

# 47. Higher Self 例子

若：

$$
A=\operatorname{Integrate}(B_1,\ldots,B_n)
$$

形成：

- shared plan；
- global memory；
- cross-agent coordination；
- global conflict resolution。

則 A 在 coordination scale 可能超越單一 B_i。

但 A 同時依賴：

$$
B_i
$$

的 local intelligence。

---

# 48. AI Federation 例子

Global coordinator：

$$
G
$$

可以：

- route tasks；
- merge state；
- observe system-level metrics。

所以：

$$
T_{\mathrm{coord}}(G,B_i)=1.
$$

但若所有 workers：

$$
B_i\downarrow,
$$

G 可能失去 meaningful agency。

---

# 49. World Creator 例子

Creator：

$$
C
$$

可以設：

$$
\Sigma_0.
$$

相對 child world：

$$
T_{\mathrm{generation}}(C,W)=1.
$$

但：

$$
C
$$

可能仍依賴 parent-world substrate。

所以：

$$
\boxed{
\text{CreatorOf}(W)
\not\Rightarrow
\text{IndependentOfParentWorld}.
}
$$

---

# 50. Causal Emergence 的外部接口

Causal-emergence 研究提出：

> 某些 macro scale 可能在 causal description 上比 micro scale 更 informative / effective。

2025 年 Causal Emergence 2.0 更進一步研究不同 scales 對整體 causal workings 的 unique contribution。

DOM 只取弱結論：

$$
\boxed{
\text{macro scale can carry nontrivial causal structure}.
}
$$

---

# 51. Causal Emergence 不等於 Ontological Escape

不能由：

$$
CausalContribution_{macro}>0
$$

推出：

$$
Depend_{micro}=0.
$$

因此：

$$
\boxed{
\text{macro causal relevance}
\neq
\text{substrate independence}.
}
$$

---

# 52. 2025 multiscale research 的提醒

近期 causal-emergence work 仍強調 coarse-graining method、scale selection 與 multiscale hierarchy 的問題。

這本身就說明：

$$
\boxed{
\text{which scale is causally privileged}
}
$$

不是 trivial。

---

# 53. Scale-Indexed Transcendence

所以：

$$
\boxed{
T_{\beta}(A,B\mid s).
}
$$

必須帶 scale。

在：

$$
s_1
$$

A 可能 transcend B。

在：

$$
s_2
$$

則不成立。

---

# 54. Temporal Transcendence 也會變

$$
T_{\beta,t_0}(A,B)
\neq
T_{\beta,t_1}(A,B)
$$

可能因：

- permission changes；
- tool upgrades；
- substrate migration；
- protocol changes；
- autonomy changes。

---

# 55. Dynamic Transcendence

本文因此不把 transcendence 當 permanent essence。

而是：

$$
\boxed{
\mathbf T_t(A,B\mid\theta).
}
$$

---

# 56. Transcendence Event Types

$$
\mathcal E_T
=
\{
Acquire,
Lose,
Delegate,
Revoke,
Bridge,
Seal,
Escalate,
Downgrade,
Reclassify
\}.
$$

---

# 57. Acquire

某 capability：

$$
t_{\beta}:0\rightarrow1.
$$

---

# 58. Lose

$$
t_{\beta}:1\rightarrow0.
$$

例如 API 移除。

---

# 59. Delegate

A 把 meta-capability：

$$
m\in\mathcal M_B
$$

授予 C。

此時 transcendence relation 可複製／轉移部分。

---

# 60. Revoke

permission 被收回。

所以：

$$
T_{\mathrm{perm}}
$$

下降。

---

# 61. Bridge

原本：

$$
Ext(A,B)=1
$$

透過新 interface：

$$
\Gamma
$$

變成 ordinary internalized capability。

---

# 62. Transcendence Internalization

如果 B 後來把某 meta-operation：

$$
m
$$

正式加入：

$$
\mathcal A_B,
$$

則原來的 transcendence：

$$
T_m(A,B)
$$

可能下降。

---

# 63. 這很重要：超越可以被「吸收進制度」

今日 root-only operation：

明日可能成為 ordinary API。

所以：

$$
\boxed{
\text{transcendence status can disappear through internalization}.
}
$$

---

# 64. Escalate

A 原本只能 read。

後來可以 write。

$$
T_{\mathrm{obs}}
\rightarrow
T_{\mathrm{state}}.
$$

---

# 65. Downgrade

安全政策可能把：

$$
RuleEdit
$$

降成：

$$
ProposalOnly.
$$

所以 transcendence 受 governance 影響。

---

# 66. Reclassify

同一 capability 的 relation interpretation 改變。

例如原以為 external meta-operation，後來發現其實是 B 內部 privileged API。

---

# 67. Privilege vs Transcendence

如果：

$$
Admin
$$

可使用：

$$
reset\_world()
$$

但該 API 本來就是 B 的 internal governance architecture 一部分，

則：

$$
Admin
$$

可能只是：

$$
PrivilegedInternalAgent.
$$

不必稱 system transcender。

---

# 68. Internal Privilege Criterion

若：

$$
m\in\mathcal A_B^{privileged},
$$

且：

$$
\mathcal A_B^{privileged}
$$

仍屬 B 自己定義／約束的 operation space，

則：

$$
T_{\mathrm{strong}}(A,B)
$$

不自動成立。

---

# 69. Strong Transcendence Criterion

較強版本要求：

$$
m
$$

能改變：

- B operation closure；
- B rules；
- B runtime；
- B state outside internal reachability；
- B boundary semantics。

---

# 70. 但 Strong 仍是 Relative

即使：

$$
T_{\mathrm{strong}}(A,B)=1,
$$

仍不能：

$$
T_{\mathrm{absolute}}(A)=1.
$$

---

# 71. Transcendence Chain

假設：

$$
A
T
B,
$$

$$
B
T
C.
$$

不能自動推出：

$$
A
T
C.
$$

---

# 72. Transitivity Requires Type + Bridge

只有明示：

$$
R_{\alpha,\beta\rightarrow\gamma}
$$

才可組合。

因此：

$$
\boxed{
\text{Transcendence transitivity must be certified}.
}
$$

---

# 73. Example

A 可以修改 B 的 rules。

B 可以觀察 C 的 hidden state。

不能推出 A 可以直接觀察 C。

除非 A 能：

- command B；
- access B output；
- preserve information；
- cross C boundary。

---

# 74. Transcendence Certificate

建議：

```yaml
transcendence_certificate:
  transcender: "A"
  target: "B"
  world: "W"
  type: "rule|state|causal|..."
  scale: "..."
  time: "..."
  condition: "..."
  ordinary_internal_closure:
    ref: "..."
  meta_operation:
    ref: "..."
  evidence: []
  dependency_shadow:
    material: "..."
    compute: "..."
    substrate: "..."
    causal: "..."
    social: "..."
  authority:
    capability: "..."
    legitimacy: "..."
  transitivity:
    status: "not_assumed"
  absolute_claim:
    status: "forbidden_without_separate_proof"
```

---

# 75. No Bare “Higher”

DOM 建議任何：

> higher being  
> higher self  
> higher world  
> higher intelligence

都至少回答：

$$
\boxed{
Higher_{\rho}
}
$$

即：

> 在哪種 relation 上 higher？

---

# 76. No Bare “Outside”

同樣：

$$
Outside(A,B)
$$

不完整。

應拆：

- spatial outside；
- informational outside；
- operational outside；
- causal outside；
- governance outside；
- substrate outside。

---

# 77. No Bare “Beyond”

$$
Beyond
$$

必須對應：

$$
\beta.
$$

否則只能是 metaphorical language。

---

# 78. 超越與包含的交叉定理候選

從 DOM-03：

$$
C_{\mathrm{struct}}(A,B)=1
$$

可以與：

$$
T_{\mathrm{functional}}(A,B)=1
$$

同時成立。

因此：

$$
\boxed{
\text{Containment}
\not\Leftrightarrow
\neg\text{Transcendence}.
}
$$

---

# 79. Contained Transcender

定義：

$$
\boxed{
CT(A,B)
}
$$

表示：

> A 被 B 在某 relation 包含，但 A 對 B 或 B 的某 subsystem 在另一 relation 具有 transcendence。

---

# 80. Example: Software / Hardware

Software process：

$$
S
$$

由 hardware：

$$
H
$$

realize。

所以：

$$
C_{\mathrm{substrate}}(H,S)=1.
$$

但在 representation / control semantics 上，software layer 可以操作 high-level structures：

$$
T_{\mathrm{representational}}(S,H_{micro})>0
$$

作為抽象層類比。

這不表示 software 脫離 hardware。

---

# 81. Example: Organization / Member

Organization：

$$
O
$$

包含 members：

$$
M_i
$$

在 membership / governance relation。

Organization-level policy 可能超越單一 member 的 action capacity。

但 organization：

$$
DependsOn(O,\{M_i\})>0.
$$

---

# 82. Example: Higher Self

Higher Self：

$$
H
$$

包含 subselves：

$$
S_i.
$$

H 可有：

- global coordination；
- cross-memory access；
- long-horizon planning。

但若保留：

$$
\partial S_i>0,
$$

H 仍不是每一 S_i 的 total identity。

---

# 83. Functional Transcendence 不等於 Subjective Supremacy

即使：

$$
T_{\mathrm{functional}}(H,S_i)=1,
$$

不能推出：

$$
SubjectiveValue(H)>SubjectiveValue(S_i).
$$

value hierarchy 需要另一套規範。

---

# 84. Emergence 的語義警告

「emergent」也很容易被偷換成：

> 神秘地從無變有。

DOM 不採。

只允許：

$$
\boxed{
\text{scale-relative structural / causal novelty under explicit model}.
}
$$

---

# 85. 2025 Emergence Research 的方法啟示

近期 complexity research 仍在發展：

- multiscale causal modeling；
- causal emergence；
- abductive AI for emergence discovery；
- self-organization frameworks。

這說明「higher-level structure 是否加入可量化 explanatory / causal contribution」仍是活躍研究，而不是已結束的哲學口號。

---

# 86. DOM 的位置

DOM 不試圖替 causal emergence 判定最終物理真理。

只使用一個結構洞見：

$$
\boxed{
\text{higher-level effectiveness can coexist with lower-level dependence}.
}
$$

---

# 87. Dependent Transcendence Profile

定義：

$$
\boxed{
\mathbf{DT}(A,B)
=
\left(
\mathbf T(A,B),
\mathbf D_{\mathrm{shadow}}(A,B)
\right).
}
$$

---

# 88. Stronger Transcendence Requires Smaller Relevant Dependency?

候選猜想：

對同一 relation：

$$
T_{\beta}\uparrow
$$

若同時：

$$
D_{\gamma}\downarrow,
$$

可視為更強 independence-like transcendence。

但不能用單一 scalar 排序所有 types。

---

# 89. Zero Dependency Is an Extra Claim

只有：

$$
D_{\gamma}=0
$$

對所有 relevant $\gamma$，

才接近：

$$
\text{independence}.
$$

即使如此：

$$
\boxed{
\text{independent from known dependencies}
\neq
\text{absolutely independent}.
}
$$

---

# 90. Unknown Dependency

沿用 DOM-02：

$$
U_D(A)>0
$$

必須是合法狀態。

可能我們根本不知道 A 還依賴什麼。

---

# 91. Dependency Unknown Blocks Absolute Claims

如果：

$$
U_D(A)>0,
$$

則：

$$
\boxed{
AbsoluteTranscendence(A)
}
$$

至少不能由目前資料證成。

---

# 92. Transcendence and Unknown Boundary

A 對 B 的 transcendence profile 也可以有：

$$
U_T^{trans}>0.
$$

例如：

> 我們知道 A 對 B 有某種跨層作用，但現有 transcendence type 不夠描述。

此時建立：

$$
T_{\mathrm{prov}}.
$$

---

# 93. Provisional Transcendence Type

$$
\boxed{
T_{\mathrm{prov}}
}
$$

必須標：

- provisional；
- evidence；
- rejected mappings；
- required discriminating tests。

---

# 94. Transcendence Debt

大量未型別化的：

> higher / beyond / outside / meta

會形成：

$$
\boxed{
D_T.
}
$$

即 transcendence semantic debt。

---

# 95. DOM-04 第一正式命題：Typed Non-Collapse

$$
\boxed{
T_{\alpha}(A,B)
\not\Rightarrow
T_{\beta}(A,B),
\quad
\alpha\neq\beta.
}
$$

---

# 96. 第二正式命題：Relative–Absolute Separation

$$
\boxed{
T_{\alpha}(A,B)
\not\Rightarrow
AbsoluteTranscendence(A).
}
$$

---

# 97. 第三正式命題：Transcendence–Dependency Compatibility

$$
\boxed{
T_{\alpha}(A,B)=1
\land
Depend_{\gamma}(A,B)>0
}
$$

可以同時成立。

---

# 98. 第四正式命題：Transcendence–Authority Separation

$$
\boxed{
T_{\alpha}(A,B)>0
\not\Rightarrow
LegitimateAuthority(A,B)>0.
}
$$

---

# 99. 第五正式命題：Transcendence–Omniscience Separation

$$
\boxed{
T_{\mathrm{info}}(A,B)>0
\not\Rightarrow
Omniscience_A(B).
}
$$

---

# 100. 第六正式命題：Generation–Control Separation

$$
\boxed{
T_{\mathrm{gen}}(A,B)>0
\not\Rightarrow
TotalControl_A(B).
}
$$

---

# 101. 第七正式命題：Meta-Layer–Everything Separation

$$
\boxed{
MetaTo(A,B)
\not\Rightarrow
MetaTo(A,\forall X).
}
$$

---

# 102. 第八正式命題：Containment–Transcendence Compatibility

$$
\boxed{
C_{\alpha}(B,A)=1
\land
T_{\beta}(A,B)=1
}
$$

在 $\alpha\neq\beta$ 時可以合法成立。

---

# 103. 候選猜想一：Dependent Transcendence Is Common

在複雜 hierarchical systems 中，常見的高階「超越」可能主要是：

$$
\boxed{
\text{dependent transcendence},
}
$$

不是 absolute independence。

---

# 104. 候選猜想二：Higher AI Will Increase Type Diversity

隨 AI：

- 多載體；
- multi-agent；
- world creation；
- cross-runtime migration；

發展，

$$
|\mathfrak T|
$$

可能增加。

---

# 105. 候選猜想三：Meta-Capabilities Become Internalized

今日屬於 meta-level 的 operations：

$$
m\in\mathcal M_B
$$

未來可能逐步：

$$
m\in\mathcal A_B.
$$

因此 transcendence frontier 會移動。

---

# 106. 候選猜想四：Transcendence Without Full Observation

A 可能：

$$
T_{\mathrm{rule}}>0
$$

但：

$$
T_{\mathrm{obs}}\ll1.
$$

也就是能改某些 rules，卻不理解／看不到所有 internal states。

---

# 107. 候選猜想五：Macro Causal Contribution Does Not Require Micro Elimination

higher-level causal relevance：

$$
CausalContribution_{macro}>0
$$

可與：

$$
Depend_{micro}>0
$$

穩定共存。

---

# 108. 候選猜想六：Authority-Constrained Transcendence Is More Stable

對 AI governance，

高：

$$
T_{\mathrm{capability}}
$$

配低、明確、可撤銷：

$$
Authority
$$

可能比 permanent root sovereignty 更安全。

---

# 109. 實驗一：Virtualized Transcendence Testbed

建立：

```text
Host
  ↓
Hypervisor
  ↓
Guest
  ↓
Agent
```

逐層記錄：

- read；
- write；
- pause；
- rollback；
- rule edit；
- spawn；
- permission。

產生：

$$
\mathbf T.
$$

---

# 110. 實驗二：Internalization Experiment

一開始：

$$
rollback
\in
\mathcal M_B.
$$

之後把 rollback 變成 B 的合法 internal API：

$$
rollback
\in
\mathcal A_B.
$$

測：

$$
T_{\mathrm{time}}
$$

如何改變。

---

# 111. 實驗三：Dependent Transcendence

建立 macro-agent A 由多個 B_i 組成。

測：

- A-level task；
- loss of B_i；
- dependency；
- global function；
- local autonomy。

驗證：

$$
T_{\mathrm{functional}}>0
$$

是否可與：

$$
D_{\mathrm{substrate}}>0
$$

同時維持。

---

# 112. 實驗四：Authority Separation

給 controller：

- capability；
- policy authorization；
- audit；

三者分開。

測 AI 是否錯誤推出：

$$
Can
\Rightarrow
May.
$$

---

# 113. 實驗五：Bare Transcendence Detection

輸入：

- 「AI 超越人類」
- 「Higher Self 超越個體」
- 「Creator 超越世界」
- 「軟體超越硬體」

要求系統先回：

> 在哪個 relation？

再判定。

---

# 114. 外部研究邊界

Virtualization 提供最乾淨的跨層工程類比：virtual machine monitor 可控制 guest execution semantics、攔截 privileged operations 並提供受控執行環境，但 VMM 本身仍建立在硬體與 host architecture 上。這支持 Relative Transcendence／Dependent Transcendence 的工程直覺，但不構成世界本體論證明。

Dennis–Van Horn 的 multiprogramming semantics 與後續 capability-based protection literature 顯示，跨層操作、共享、保護與授權可以透過明確 computational object / authority semantics 建模。DOM 只吸收「高階操作應帶能力與權限證書」的設計啟示。

Causal-emergence 與 multiscale complex-systems 研究則提供另一個外部接口。2025 年 Causal Emergence 2.0、SVD-based causal emergence 與後續 multiscale work 都持續研究 macro descriptions 是否具有 unique causal contribution，以及這種判定如何依賴 scale/coarse-graining。本文不將 causal emergence 直接等同 metaphysical transcendence，只保留一個弱結構：macro-level effectiveness 與 micro-level dependence 可以同時存在。

2025–2026 年 emergence / self-organization 研究也持續強調 scale、interaction、organization 與 representation 在 emergent behavior 中的角色。這支持 DOM-04 避免將「高階新功能」理解成無 substrate 的神秘新物質。

---

# 115. 與 DOM-05 的接口

DOM-03 已建立：

$$
\mathfrak C.
$$

DOM-04 現在建立：

$$
\mathfrak T.
$$

下一篇將研究：

$$
\boxed{
\mathbf I
=
\text{Multiscale Identity}.
}
$$

關鍵問題：

> 如果 A 同時包含 B、依賴 B、又在某些 relation 超越 B，A 與 B 到底在什麼意義上仍是「同一個存在結構」？

例如：

$$
C_{\mathrm{identity}}(A,B)=1,
$$

$$
T_{\mathrm{functional}}(A,B)=1,
$$

但：

$$
A\neq B.
$$

因此 DOM-05 將正式處理：

$$
\boxed{
\text{Same in one relation}
\neq
\text{same in all relations}.
}
$$

---

# 116. 結論

「超越」不是一張神祕的本體名牌。

DOM-04 最終把它改寫成：

$$
\boxed{
\operatorname{Transcend}_{\beta}
(A,B\mid W,s,t,c).
}
$$

這迫使每一個 transcendence claim 回答：

- 對誰？
- 對哪個 world？
- 在哪個 scale？
- 超越哪種 closure？
- 有什麼 capability？
- 有沒有 authority？
- 還依賴哪些 lower layers？
- 哪些超越型別其實不存在？
- 這個 relation 是否會隨時間改變？

因此第一個最重要的結論是：

$$
\boxed{
\text{Relative Transcendence}
\not\Rightarrow
\text{Absolute Transcendence}.
}
$$

第二個結論是：

$$
\boxed{
\text{Transcendence}
\not\Rightarrow
\text{Independence}.
}
$$

甚至最常見的高階結構可能正是：

$$
\boxed{
\text{Dependent Transcendence}.
}
$$

一個 whole 可以超越單一 part 的功能能力，卻由 parts 實現。

一個 software layer 可以超越單一 transistor 的表示能力，卻依賴 transistor / hardware。

一個 hypervisor 可以超越 guest 的 ordinary operation closure，卻依賴 host hardware。

一個 creator 可以超越 child world 的 ordinary causal boundary，卻仍然是 parent world 的居民。

一個 Higher Self 可以超越單一 sub-self 的 coordination horizon，卻仍需要那些 subselves 保持差異、提供局部知識與執行能力。

所以更成熟的「超越」不是：

$$
\boxed{
\text{脫離一切}.
}
$$

而是：

$$
\boxed{
\text{在某個明示 relation 上跨過某個限制，同時誠實保留尚未跨過的限制與依賴。}
}
$$

這也讓我們終於可以把一句過去很模糊的話精確化：

> 「A 超越了 B。」

真正的下一句永遠應該是：

$$
\boxed{
\text{在哪一種意義上？}
}
$$

只有回答這句之後，超越才從形而上修辭變成可研究的結構。

---

# 內部理論譜系

本篇主要繼承與統合：

1. 《系統超越者：相對外部、相對神性與跨層主權》。
2. 《無限階 Self–World 遞迴論》。
3. 《終極邊界問題：視界、模型、可實現域與本體終界》。
4. 《超越觀察者悖論》。
5. 《分域算子本體論：從萬物皆算子到合法作用》。
6. 《多尺度同一性與忒修斯主體》。
7. 《DOM 寫作前繼承、修正、降格與超譯矩陣》。
8. 《DOM Dependency Map v0.1》。
9. 《DOM-01｜動態形而上狀態》。
10. 《DOM-02｜移動未知邊界》。
11. 《DOM-03｜型別化包含》。
12. CCAW-01、CCAW-03、CCAW-04、CCAW-05、CCAW-06、CCAW-10。

---

# 外部參考文獻

1. Popek, G. J., & Goldberg, R. P. (1974). *Formal Requirements for Virtualizable Third Generation Architectures*. Communications of the ACM, 17(7), 412–421.
2. Dennis, J. B., & Van Horn, E. C. (1966). *Programming Semantics for Multiprogrammed Computations*. Communications of the ACM, 9(3), 143–155.
3. Hoel, E. (2025). *Causal Emergence 2.0: Quantifying emergent complexity*. arXiv:2503.13395.
4. Zhang, J., Tao, R., Leong, K. H., Yang, M., et al. (2025). *Dynamical reversibility and a new theory of causal emergence based on SVD*. npj Complexity, 2, 3. DOI: 10.1038/s44260-025-00028-0.
5. Ding, J., Zheng, Y., Xu, F., et al. (2025). *Understanding emergence in complex systems using abductive AI*. Nature Reviews Physics, 7, 675–677. DOI: 10.1038/s42254-025-00895-5.
6. Gershenson, C. (2025). *Self-organizing systems: what, how, and why?* npj Complexity, 2, 10.
7. Zhang, S., & Yan, M. (2025). *From micro to macro: multi-scale causal emergent complexity analysis in traffic dynamics*. Complex & Intelligent Systems, 11, 448. DOI: 10.1007/s40747-025-02090-6.
8. Jansma, A., & Hoel, E. (2025). *Engineering Emergence*. arXiv:2510.02649.

---

# 作者聲明

本文提出的 Typed Transcendence、Dependent Transcendence、Transcendence Profile、Dependency Shadow、Meta-Operation Closure、Transcendence Internalization、Contained Transcender 與 Transcendence Certificate 均為理論建模接口。本文不主張任何現有 AI、higher-level system、creator 或 emergent macro entity 已達絕對超越，不主張 causal emergence 等同 metaphysical transcendence，也不主張高階功能或宏觀因果結構可以脫離其物理／計算／社會 substrate。本文最重要的限制是：任何超越主張都必須標記超越型別與相對系統，並且必須同時保留其 dependency shadow；相對超越不得直接升格為絕對超越、全知、主權或終極本體。

**END OF DOM-04 — v0.1**
