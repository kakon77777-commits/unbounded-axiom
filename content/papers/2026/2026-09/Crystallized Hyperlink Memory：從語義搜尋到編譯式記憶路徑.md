# Crystallized Hyperlink Memory：從語義搜尋到編譯式記憶路徑

**英文暫名：** Crystallized Hyperlink Memory: From Semantic Retrieval to Compiled Memory Paths  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 06  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

長期 AI 記憶系統若每次 recall 都從 raw transcript、向量資料庫、全文索引或整張語義圖重新搜尋，則即使「記憶已被保存」，AI 仍可能在每一次回想時重新支付接近完整研究成本。當具名 AI 具有大量 conversation lines、project memories、canonical records、Crystallized Semantic Graph、source provenance 與多 runtime projection 時，這種 cold retrieval 的重複成本將成為新的瓶頸。

本文提出 **Crystallized Hyperlink Memory（CHM）**。其核心主張是：一個成功的記憶搜尋結果不只可以被保存為內容，也可以把**成功的搜尋／推理／展開路徑本身**保存為可驗證、可失效、可回退、可重用的 typed hyperlink。

令一次 recall 的成功路徑為：

$$
P_{\mathrm{memory}}
=
(
q,
n_0,
n_1,
\ldots,
n_k,
v
),
$$

其中 $q$ 是 query class， $n_i$ 是中間 semantic / canonical / source nodes， $v$ 是 validation outcome。若此路徑在多次相似任務中保持高 reuse、低 cost、低 risk、穩定 provenance 與可接受 staleness，則可將其 crystallize / compile 為：

$$
\boxed{
P_{\mathrm{memory}}
\rightarrow
\widehat{\ell}_{\mathrm{memory}}.
}
$$

其中 $\widehat{\ell}_{\mathrm{memory}}$ 不是一般 URL，而是一個具有型別、前置條件、scope、source revision、validator、fallback、invalidation rule 與 provenance 的可執行認知地址。

本文將 recall 分為三態：

$$
\boxed{
\text{Cold Recall}
\rightarrow
\text{Warm Route}
\rightarrow
\text{Hot Compiled Path}.
}
$$

Cold Recall 允許較昂貴的 semantic search、graph traversal 與 source verification；Warm Route 累積路徑成功 evidence；Hot Path 則在條件成立時直接跳轉到高價值 semantic region 或 source target，但仍保留當下 authorization 與 revision 檢查。

本文進一步提出 **Navigation Crystal**，將「如何回想」本身作為 derived semantic memory：

$$
\boxed{
\text{Memory Content}
+
\text{Memory Navigation Knowledge}.
}
$$

因此具名 AI 不只記住「以前得到什麼結論」，也能逐步記住「遇到這一類問題時，通常應從哪個 crystal、哪個 project state、哪個 source span 開始找」。

為避免把所有路徑都編譯造成 Crystal Debt、Selection Congestion、Invalidation Storm 與 Maintenance Explosion，本文採用 **Selective Path Compilation**。令一條候選路徑的生命週期效用為：

$$
U(\ell)
=
B_{\mathrm{reuse}}
+
B_{\mathrm{latency}}
+
B_{\mathrm{context}}
+
B_{\mathrm{future}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{select}}
-
C_{\mathrm{risk}}.
$$

只有當：

$$
U(\ell)>0
$$

且滿足最低 reuse、validation、provenance、fallback 與 authority-stability 門檻時，才值得 persistent compilation。

本文同時強調，Path Compilation 不能成為 permission compilation：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

Hot path 可以縮短 semantic traversal，但不能省略 identity resolution、capability check、permission revision、source validity 與 revocation。更快的路徑只能在當下 Safe Reachable World 內執行。

本文最終把 CHM 定位為 CSG、MNEME、SOACR、LIMEN、Canonical Storage Architecture 與 UNPNP Path Compilation 之間的 acceleration layer，使長期具名 AI 從「每次重新搜尋記憶」進一步發展為「逐步編譯自己的記憶路徑」。

**關鍵詞：** Crystallized Hyperlink Memory、Path Compilation、Navigation Crystal、Semantic Retrieval、Named AI、CSG、UNPNP、Memory Routing、Hot Path、Cold Recall、MNEME、SOACR、LIMEN

---

# 1. 問題：有記憶，不代表會高效回想

假設 resident $R$ 的長期記憶世界為：

$$
\mathcal W_R^M.
$$

若每次 query $q$ 都重新執行：

$$
q
\rightarrow
\operatorname{Search}
\rightarrow
\operatorname{Rank}
\rightarrow
\operatorname{Traverse}
\rightarrow
\operatorname{Expand}
\rightarrow
\operatorname{Verify},
$$

則 recall cost：

$$
T_{\mathrm{recall}}(q)
$$

可能長期維持高值。

即使同一類問題：

$$
q_1\sim q_2\sim q_3,
$$

也可能每次重新做相似工作。

因此：

$$
\boxed{
\text{Stored Memory}
\not\Rightarrow
\text{Efficient Recall}.
}
$$

長期記憶系統還需要學會：

> 哪條路通常能最快、最可靠地找到這一類記憶？

---

# 2. Memory Content 與 Memory Navigation Knowledge

傳統 memory record 偏向：

$$
m=\text{What is remembered}.
$$

本文加入：

$$
r=\text{How to retrieve what is remembered}.
$$

因此 resident memory 可以分：

$$
\mathcal M_R
=
\mathcal M_R^{content}
\cup
\mathcal M_R^{navigation}.
$$

其中 navigation knowledge 不一定是 canonical truth，而可以是 derived operational knowledge。

因此：

$$
\boxed{
\text{AI can remember how to remember}.
}
$$

這是 CHM 的核心。

---

# 3. Retrieval Path

定義一次 recall path：

$$
P
=
(
q,
s_0,
a_1,
s_1,
a_2,
\ldots,
a_k,
s_k,
v
).
$$

其中：

- $q$：query / MemoryNeed class；
- $s_i$：memory state / node；
- $a_i$：retrieval action；
- $v$：validation result。

例如：

$$
Q_{\mathrm{SOACR}}
\rightarrow
C_{\mathrm{project}}
\rightarrow
C_{\mathrm{decision}}
\rightarrow
R_{\mathrm{source}}
\rightarrow
Validation.
$$

如果這條路徑成功：

$$
Success(P)=1.
$$

它本身就具有 future reuse value。

---

# 4. Cold Recall

第一次或不熟悉 query：

$$
q\in Q_{\mathrm{cold}}
$$

可採較廣搜尋：

$$
ColdRecall(q)
=
Search
+
Reveal
+
Traverse
+
Expand
+
Verify.
$$

Cold Recall 的主要任務不是最快，而是：

- 找到正確記憶；
- 建立 provenance；
- 發現結構；
- 保存成功 route evidence。

因此：

$$
\boxed{
\text{Cold Recall explores}.
}
$$

---

# 5. Warm Route

同類 query 重複後，可以觀察：

$$
P_1,P_2,\ldots,P_n.
$$

若路徑存在穩定交集：

$$
CommonRoute(P_1,\ldots,P_n)
=
\widetilde{P},
$$

則可建立 warm route。

Warm Route 不是完全編譯，而是：

- preferred start node；
- recommended semantic region；
- likely source；
- validation rule；
- fallback route。

因此：

$$
\boxed{
\text{Warm Route remembers a likely way}.
}
$$

---

# 6. Hot Compiled Path

若 warm route 經過足夠 reuse 與 validation，可形成：

$$
\widehat{\ell}.
$$

定義：

$$
\widehat{\ell}
=
(
q_c,
target,
type,
preconditions,
scope,
validator,
provenance,
revision,
fallback,
invalidation
).
$$

其中：

- $q_c$：query class；
- `target`：logical ArtifactAddress / semantic node；
- `type`：hyperlink type；
- `preconditions`：身份、scope、version 等前置條件；
- `validator`：使用前後驗證；
- `provenance`：來源；
- `revision`：依賴版本；
- `fallback`：slow path；
- `invalidation`：失效條件。

因此：

$$
\boxed{
\text{Hot Path is a typed executable memory address}.
}
$$

---

# 7. Hyperlink 不等於 URL

一般 URL 主要回答：

> 要去哪裡？

CHM hyperlink 還要回答：

> 誰可以走？在什麼條件下走？走到的是哪個 revision？如果失效怎麼辦？如何驗證？

因此：

$$
\boxed{
\text{Hyperlink}
=
\text{Address}
+
\text{Semantics}
+
\text{Guard}
+
\text{Validation}
+
\text{Fallback}.
}
$$

這更接近認知 runtime primitive，而不是單純 navigation string。

---

# 8. Logical Target

Paper 05 已提出：

$$
ArtifactAddress
=
(
objectId,
kind,
schema,
revision,
digest,
scope,
representation
).
$$

CHM 應優先把：

$$
ArtifactAddress
$$

作為 hyperlink target。

所以：

$$
\widehat{\ell}
\rightarrow
ObjectRef
\rightarrow
Resolver
\rightarrow
PhysicalArtifact.
$$

而不是：

$$
\widehat{\ell}
\rightarrow
D:\backslash path.
$$

因此：

$$
\boxed{
\text{Compile logical route, not physical path}.
}
$$

---

# 9. Query Class

Hot path 不應綁單一句自然語言。

應建立 query class：

$$
q_c.
$$

例如：

```text
recall_current_soacr_architecture
verify_named_ai_identity_rule
find_latest_project_decision
retrieve_exact_source_for_crystal
```

query class 可以由：

- explicit intent；
- MemoryNeed；
- semantic pattern；
- structured task；

決定。

但不能只靠 embedding similarity 自動升級 authority。

---

# 10. Navigation Crystal

可定義：

$$
C_{\mathrm{nav}}
=
(
q_c,
preferredRoute,
fallback,
evidence,
successRate,
costEstimate,
validity
).
$$

它是 derived semantic object。

Navigation Crystal 不一定立即成為 hot compiled path。

因此：

$$
\boxed{
\text{Navigation Crystal}
\neq
\text{Compiled Hyperlink}.
}
$$

前者是可理解的路由知識。

後者是 runtime 可直接執行的優化。

---

# 11. Route Observation

每次 recall 可以產生 route receipt：

```text
query_class
resident_id
line_id
route_nodes[]
route_edges[]
source_reads
latency
token_cost
validation_result
fallback_used
final_confidence
```

這些 receipts 提供 path compilation evidence。

但 receipt 本身不應塞進 working context，除非需要 audit。

---

# 12. Route Similarity

若：

$$
P_a,P_b
$$

共享：

- same query class；
- same semantic start；
- same target；
- same validation；
- similar scope；

則：

$$
Sim(P_a,P_b)
$$

高。

可聚類：

$$
\mathcal P_c
=
\{
P_i
\mid
class(P_i)=q_c
\}.
$$

再抽取 candidate route。

---

# 13. Path Compilation

Path Compilation 可表示：

$$
Compile:
\mathcal P_c
\rightarrow
\widehat{\ell}_c.
$$

但不是所有：

$$
\mathcal P_c
$$

都值得 compile。

需要：

$$
Gate_{\mathrm{compile}}.
$$

---

# 14. Compilation Gate

第一代至少檢查：

```text
reuse_count
success_rate
validation_rate
source_stability
scope_stability
authority_stability
fallback_available
maintenance_cost
risk_class
```

若任一 critical condition 不足：

$$
RemainWarm.
$$

因此：

$$
\boxed{
\text{Observed Route}
\not\Rightarrow
\text{Compiled Route}.
}
$$

---

# 15. Path Utility

定義：

$$
U(\ell)
=
B_{\mathrm{reuse}}
+
B_{\mathrm{latency}}
+
B_{\mathrm{context}}
+
B_{\mathrm{future}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{select}}
-
C_{\mathrm{risk}}.
$$

## 15.1 Reuse Benefit

$$
B_{\mathrm{reuse}}
$$

表示未來重複使用次數。

## 15.2 Latency Benefit

$$
B_{\mathrm{latency}}
$$

表示少走 search / traversal 所節省時間。

## 15.3 Context Benefit

$$
B_{\mathrm{context}}
$$

表示減少 materialized context。

## 15.4 Future Benefit

$$
B_{\mathrm{future}}
$$

表示 path 本身對未來 navigation learning 的價值。

---

# 16. Compilation Cost

$$
C_{\mathrm{compile}}
$$

包括：

- route normalization；
- schema generation；
- guard creation；
- validation；
- storage；
- indexing。

如果路徑只會用一次：

$$
C_{\mathrm{compile}}
>
B_{\mathrm{reuse}}.
$$

就不值得。

---

# 17. Verification Cost

Hot path 仍需要：

$$
C_{\mathrm{verify}}.
$$

如果每次 verification 比 cold search 還貴：

$$
U(\ell)<0.
$$

因此 path compiler 必須考慮安全成本，而不是只看 hop count。

---

# 18. Maintenance Cost

路徑依賴：

$$
D(\ell)
=
\{
x_1,\ldots,x_n
\}.
$$

每個 source revision 變更都可能觸發：

$$
Revalidate(\ell).
$$

所以：

$$
C_{\mathrm{maintain}}
$$

隨 dependency volatility 增加。

高變動資料不適合 aggressive compilation。

---

# 19. Selection Cost

如果 compiled routes 太多：

$$
|\widehat{\mathcal L}|
\rightarrow
large,
$$

則 query 到 path 的 selection 本身會變慢。

因此：

$$
C_{\mathrm{select}}
$$

不能忽略。

這形成：

$$
\boxed{
\text{Hyperlink Congestion}.
}
$$

---

# 20. Risk Cost

某些 memory path 涉及：

- private memory；
- identity context；
- legal source；
- security record；
- project authority；
- external data。

即使速度收益高，也可能：

$$
C_{\mathrm{risk}}
$$

過高。

因此：

$$
\boxed{
\text{Fast}
\neq
\text{Worth Compiling}.
}
$$

---

# 21. Break-Even Reuse

設：

$$
C_0
$$

為 compilation fixed cost，

每次 cold recall cost：

$$
C_c,
$$

每次 hot recall cost：

$$
C_h.
$$

若：

$$
C_h<C_c,
$$

break-even 次數：

$$
n^\*
=
\left\lceil
\frac{C_0}
{C_c-C_h}
\right\rceil.
$$

只有預估 reuse：

$$
n\ge n^\*
$$

才有純成本上的 compile 理由。

---

# 22. Semantic Break-Even

除了成本，也可加入 quality：

$$
Q_h
$$

與：

$$
Q_c.
$$

若 hot path 雖快但：

$$
Q_h\ll Q_c,
$$

也不值得。

所以可定義：

$$
U_Q(\ell)
=
U(\ell)
+
\lambda
(
Q_h-Q_{\min}
).
$$

---

# 23. Cold / Warm / Hot State Machine

可定義 route state：

$$
state(\ell)
\in
\{
cold,
warm,
candidate,
hot,
stale,
revoked,
retired
\}.
$$

典型流程：

$$
cold
\rightarrow
warm
\rightarrow
candidate
\rightarrow
hot.
$$

若 source 改變：

$$
hot
\rightarrow
stale.
$$

若 permission revoke：

$$
hot
\rightarrow
revoked.
$$

若長期不再使用：

$$
hot
\rightarrow
retired.
$$

---

# 24. Promotion Rule

從 warm 到 candidate：

$$
reuse\ge r_{\min}
$$

且：

$$
success\ge s_{\min}.
$$

從 candidate 到 hot：

$$
validation\ge v_{\min}
$$

且：

$$
U(\ell)>0.
$$

第一代 threshold 可以保守。

---

# 25. Demotion Rule

若：

$$
failureRate>\theta_f,
$$

或：

$$
staleRate>\theta_s,
$$

則：

$$
hot
\rightarrow
warm/stale.
$$

因此 route 不是一旦 compile 就永久存在。

---

# 26. Route Scope

compiled path 必須有 scope：

$$
Scope(\ell)
\in
\{
line,
project,
resident,
shared
\}.
$$

如果 path 只在 Project A 有效：

$$
Scope(\ell)=project:A.
$$

不能因為同一 resident 就自動在 Project B 使用。

---

# 27. Line-Local Route

一些 path 只適合某條 experiment line。

例如：

$$
L_{\mathrm{debug}}
$$

使用特殊 source ordering。

可以保持：

$$
Scope(\ell)=line.
$$

不必提升 global。

---

# 28. Project Route

如果多條 project lines 都反覆用同一路徑：

$$
L_1,L_2,L_3
\rightarrow
\ell_P,
$$

可 promotion：

$$
line
\rightarrow
project.
$$

但 promotion 需要重新檢查：

- scope；
- source；
- authority；
- semantic stability。

---

# 29. Resident-Global Route

只有非常穩定的 recall pattern 才適合：

$$
Scope(\ell)=resident.
$$

例如：

- stable identity explanation；
- recurring collaboration convention；
- long-lived project registry access。

但 resident-global route 仍不能跨 private/project ACL。

---

# 30. Cross-Resident Route

未來 multi-resident Agent 可能存在：

$$
R_A
\rightarrow
SharedObject
\leftarrow
R_B.
$$

compiled route 只能指向 explicit shared scope。

不能把：

$$
Private(R_A)
$$

編成：

$$
Route(R_B).
$$

因此：

$$
\boxed{
\text{Cross-Resident Route Requires Explicit Shared Authority}.
}
$$

---

# 31. Path Compilation 與 Permission Compilation 的分離

最重要的安全不變式之一：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

Hot path 可以保存：

> 若被授權，這是最快路。

不能保存：

> 上次可以，所以這次永遠可以。

所以每次：

$$
Use(\widehat{\ell})
$$

都需重新驗：

$$
Authorize(
currentIdentity,
currentScope,
currentPermissionRevision
).
$$

---

# 32. Identity Gate

若：

$$
Resident=unresolved,
$$

所有 private CHM path：

$$
Deny.
$$

不能因為 hyperlink target 指向 resident memory 就反推：

$$
Resident=R.
$$

因此：

$$
\boxed{
\text{Hot Memory Path}
\text{ assumes resolved identity; it does not prove identity}.
}
$$

---

# 33. Capability Gate

若 compiled route 需要：

```text
filesystem.read
graph.traverse
source.expand
```

而 runtime profile 缺：

```text
filesystem.read
```

則：

$$
FastPath=Unavailable.
$$

可以：

$$
Fallback.
$$

不能模型自行假裝有 capability。

---

# 34. Revision Binding

Route cache key 可綁：

$$
K_\ell
=
(
residentId,
queryClass,
scope,
capabilityRevision,
permissionRevision,
sourceRevision,
semanticRevision
).
$$

若任一變化：

$$
K_{\ell}^{old}
\neq
K_{\ell}^{current},
$$

則重新驗證。

---

# 35. Source Revision

如果 target crystal：

$$
C_{42}
$$

被：

$$
C_{43}
$$

supersede，舊 path 不一定完全 invalid。

可以：

- redirect；
- revalidate；
- fallback；
- retire。

但不能默默把舊 target 當 current。

---

# 36. Semantic Revision

CSG relation 也可能變。

若：

$$
C_A
\xrightarrow{supports}
C_B
$$

改成：

$$
C_A
\xrightarrow{contradicts}
C_B,
$$

任何依賴舊 relation 的 compiled route 必須 revalidate。

---

# 37. Fallback

每條 hot path 必須有 fallback：

$$
Fallback(\widehat{\ell}).
$$

可分：

```text
warm_route
semantic_reveal
project_search
source_search
full_cold_recall
```

因此：

$$
\boxed{
\text{Fast Path Without Fallback}
\text{ 不適合長期記憶。}
}
$$

---

# 38. Fail-Open 與 Fail-Closed

如果 hot path 失效：

$$
FastPathFail.
$$

一般應：

$$
FallbackToSlow.
$$

但如果失效原因是：

$$
Unauthorized
$$

則不能 fallback 到「更廣搜索」繞過權限。

應：

$$
Deny.
$$

因此：

$$
\boxed{
\text{Technical Miss}
\rightarrow
\text{Fallback};
}
$$

$$
\boxed{
\text{Authority Fail}
\rightarrow
\text{Fail Closed}.
}
$$

---

# 39. Invalidations

可定義 dependency closure：

$$
Dep(\ell).
$$

若：

$$
Invalidate(x),
$$

則：

$$
\forall \ell:
x\in Dep(\ell)
\Rightarrow
Revalidate(\ell).
$$

這是 Paper 07 安全篇的直接前置。

---

# 40. Invalidation Graph

可以建立：

$$
\mathcal D_{\mathrm{route}}.
$$

edge：

```text
compiled_from
depends_on
validated_by
authorized_by_revision
resolves_to
```

這不是 CSG。

它是 operational dependency graph。

---

# 41. Invalidation Storm

若一個高階 source 被大量 routes 依賴：

$$
degree(x)\gg1,
$$

修改 $x$ 可能造成：

$$
O(degree(x))
$$

revalidation。

這就是：

$$
\boxed{
\text{Invalidation Storm}.
}
$$

因此不能過度編譯所有下游 path。

---

# 42. Effective Hyperlink Path Encoding

CHM 不要求保存完整原始 search trace。

可以把 path 壓縮成：

$$
EHP(\ell)
=
(
queryClass,
anchor,
target,
guards,
validator,
fallback
).
$$

這保留 runtime 必要資訊，而不是整段 reasoning transcript。

因此：

$$
\boxed{
\text{Compiled Path}
\neq
\text{Stored Chain of Thought}.
}
$$

只需保存可驗證的外部路由結構與 evidence。

---

# 43. Path Evidence

route evidence 可以包含：

- node IDs；
- source IDs；
- validation receipts；
- success counters；
- latency；
- error classes。

不需要保存 hidden model reasoning。

這有利於跨模型 reuse。

---

# 44. Cross-Model Navigation

若：

$$
Model_A
$$

找到成功 route，

$$
Model_B
$$

只要理解 standardized hyperlink schema，也可以使用。

因此：

$$
\boxed{
\text{Navigation Knowledge Can Be Model-Portable}.
}
$$

這也是 AI-native interlingua / protocol 的實際用途之一。

---

# 45. Query Normalization

不同 query：

```text
我們之前 SOACR 最後定案什麼？
SOACR architecture current decision?
找 SOACR 目前 accepted architecture
```

可以 normalize 到：

$$
q_c=
recall\_soacr\_accepted\_architecture.
$$

這降低 path duplication。

---

# 46. Query Over-Generalization

若 normalization 太寬：

$$
q_a,q_b
\rightarrow
q_c
$$

但實際需求不同，hot path 會錯。

因此 query class 應保留：

- purpose；
- fidelity；
- scope；
- current/historical；
- exact/semantic。

不能只用 topic。

---

# 47. Purpose-Aware Path

可定義：

$$
q_c
=
(topic,purpose,fidelity,scope).
$$

例如：

$$
(
SOACR,
verify,
exact,
project
).
$$

與：

$$
(
SOACR,
recall,
overview,
project
)
$$

應是不同 route class。

---

# 48. MemoryNeed Integration

SOACR 產生：

$$
N_t.
$$

CHM path selector 接：

$$
SelectPath(
N_t,
Profile,
Authority,
State
).
$$

因此：

$$
\boxed{
\text{Path Selection}
\text{ 應由 MemoryNeed 驅動，而不是字面 query 驅動。}
}
$$

---

# 49. CSG Integration

CSG 提供：

$$
V_C,\mathcal E_C.
$$

Hot path 可以直接跳到：

$$
C_{\mathrm{anchor}}.
$$

再：

$$
RevealNeighborhood.
$$

這比每次全圖搜尋便宜。

因此 CHM 是 CSG 的 acceleration overlay。

---

# 50. MNEME Integration

若 query 需要 canonical truth：

$$
\widehat{\ell}
\rightarrow
mneme:record/X.
$$

route 可以縮短定位，但 canonical read 仍由 MNEME 控制。

因此：

$$
\boxed{
\text{CHM locates;}
}
$$

$$
\boxed{
\text{MNEME authorizes and materializes canonical memory}.
}
$$

---

# 51. LIMEN Integration

LIMEN 在 path 前：

$$
ResolveIdentity.
$$

CHM 不能：

$$
ResolveByRememberedPath.
$$

也就是：

> 我記得上次我是 A，所以直接走 A 的 path。

不允許。

---

# 52. Canonical Storage Integration

Paper 05 的 `ArtifactAddress` 提供：

- stable ID；
- schema；
- revision；
- digest；
- scope；
- representation。

CHM target 以此為基礎。

因此 physical relocation 不會破壞 logical route。

---

# 53. Runtime Profile Integration

Paper 04 的：

$$
\mathcal C_\rho
$$

決定 route 是否 executable。

如果 route requirements：

$$
Req(\ell)
\subseteq
\mathcal C_\rho,
$$

才可執行。

否則：

$$
Fallback.
$$

---

# 54. Web CHM Profile

Web 第一代可先只支援：

```text
crystal_anchor
project_route
decision_route
source_on_demand
read_only_fast_path
```

暫不支援：

- cross-resident path；
- executable action path；
- registrar mutation path。

---

# 55. Agent CHM Profile

Agent 可增加：

- filesystem source route；
- repo route；
- local DB route；
- MCP resource route；
- delegated project route。

但 action path 應另行分級。

---

# 56. Memory Hyperlink 與 Action Hyperlink 分離

本文只聚焦：

$$
\widehat{\ell}_{memory}.
$$

未來：

$$
\widehat{\ell}_{action}
$$

具有 external side effect，風險更高。

因此：

$$
\boxed{
\text{Memory Hyperlink}
\neq
\text{Action Hyperlink}.
}
$$

不能因 memory path 技術成熟就直接推到 destructive automation。

---

# 57. Read-Only First

CHM 第一代應優先：

$$
ReadOnly.
$$

即：

- navigate；
- reveal；
- materialize；
- verify。

不直接：

- mutate；
- delete；
- deploy；
- send；
- transfer。

這能隔離 path correctness 與 action safety。

---

# 58. Route Confidence

可定義：

$$
Conf(\ell)
=
f(
success,
validation,
freshness,
stability,
scopeMatch
).
$$

只有：

$$
Conf(\ell)\ge\theta
$$

才進 hot path。

---

# 59. Route Freshness

定義：

$$
Fresh(\ell,t).
$$

如果：

$$
t-t_{\mathrm{validated}}
>
\Delta_{\max},
$$

則：

$$
stale.
$$

不同 query class 可以有不同 freshness threshold。

---

# 60. Route Failure Classes

可分：

```text
not_found
stale
unauthorized
capability_missing
schema_changed
target_superseded
validation_failed
scope_mismatch
resolver_error
```

不同 failure 對應不同 fallback。

---

# 61. Resolver Error

如果只是 physical backend 暫時不可用：

$$
resolver\_error,
$$

可以 retry / alternate representation。

但不能改用無權限的其他 source。

---

# 62. Target Superseded

如果：

$$
target\_superseded,
$$

可沿：

$$
supersedes
$$

edge 找新 target。

這可以形成：

$$
RouteRepair.
$$

---

# 63. Route Repair

當：

$$
\ell
$$

部分失效，不一定全部重建。

可以：

$$
Repair(
\ell,
changedDependency
).
$$

例如更新：

- target revision；
- source digest；
- validator。

這降低 maintenance cost。

---

# 64. Route Regeneration

如果 route structure 已完全不適用：

$$
Retire(\ell)
$$

再：

$$
ColdRecall
\rightarrow
NewRoute.
$$

---

# 65. Route Lifetime

可定義：

$$
TTL(\ell).
$$

低 volatility route 可以長 TTL。

高 volatility route 短 TTL。

但 TTL 到期不是刪除，而是：

$$
RequireRevalidation.
$$

---

# 66. Path Metrics

每條 route 可記：

```text
uses
successes
failures
avg_latency
avg_materialized_bytes
avg_token_cost
last_validated
last_used
fallback_rate
```

這支援 EHPE / selective optimization。

---

# 67. Crystal Debt

如果 persistent crystals / routes 太多：

$$
Debt_{\mathrm{crystal}}
\uparrow.
$$

表現為：

- stale objects；
- duplicate routes；
- maintenance burden；
- route selection noise；
- invalidation graph explosion。

因此需要 retirement。

---

# 68. Route Retirement

如果：

$$
lastUsed
\gg
TTL_{retire}
$$

且：

$$
reuse\approx0,
$$

可以：

$$
hot
\rightarrow
retired.
$$

retired path 仍可保留歷史 evidence，但退出 default selection。

---

# 69. Route Deduplication

兩條 compiled routes：

$$
\ell_a,\ell_b
$$

若 query class、scope、target、guard 高度一致，可 merge operational metadata。

但 merge route metadata 不等於 merge source crystals。

---

# 70. Route Competition

若同 query class 有：

$$
\ell_1,\ell_2,\ell_3,
$$

selector 可用：

$$
Score(\ell_i)
=
\alpha Success
-
\beta Latency
-
\gamma Risk
-
\delta Staleness.
$$

選最佳。

但也可保留 alternate route 做 robustness。

---

# 71. Single Shortest Path 並非永遠最好

若只有一條 hot path：

$$
\ell^\*,
$$

一旦失效容易脆弱。

因此某些重要 memory class 可保留：

$$
k\text{-best routes}.
$$

這與 redundancy / resilience 相關。

---

# 72. Source Diversity

若多條 route 都指向同一 derived crystal，但沒有獨立 source，robustness 不一定真的提高。

所以 critical memory 可以要求：

$$
SourceDiversity\ge d_{\min}.
$$

---

# 73. Verification Route

某些 query 可以有專門：

$$
\ell_{\mathrm{verify}}.
$$

例如：

$$
DecisionCrystal
\rightarrow
SourceRecord
\rightarrow
ValidationReceipt.
$$

它可能比 recall route 慢，但更可信。

因此：

$$
\boxed{
\text{Recall Path}
\neq
\text{Verification Path}.
}
$$

---

# 74. Overview Route

另一條：

$$
\ell_{\mathrm{overview}}
$$

只去 higher-order crystal。

所以同 topic 可以多 path：

- overview；
- exact；
- verify；
- historical；
- current。

---

# 75. Path Type

可定義：

```text
overview
current_state
exact_source
verification
historical
open_loop
decision
navigation
```

type 是 path semantics 的一部分。

---

# 76. Hyperlink Chain

一條 compiled path 不一定只有單 hop。

可為：

$$
\ell
=
\ell_1\circ\ell_2\circ\cdots\circ\ell_k.
$$

但 path compiler 可以把穩定子鏈壓成 composite link。

---

# 77. Composite Link

如果：

$$
A\rightarrow B\rightarrow C
$$

長期穩定，可建立：

$$
A\Rightarrow C.
$$

但 composite link 必須保存：

$$
Prov(A\Rightarrow C)
=
\{A\rightarrow B,B\rightarrow C\}.
$$

不能把中間 provenance 消失。

---

# 78. Decompression

任何 composite hyperlink 都應能：

$$
Decompress(\ell^\*)
\rightarrow
UnderlyingRoute.
$$

因此：

$$
\boxed{
\text{Compiled Path Remains Auditable}.
}
$$

---

# 79. Hyperlink as Crystallized Computation

Path Compilation 的更一般形式是：

$$
\text{Repeated Computation}
\rightarrow
\text{Compiled Transition}.
$$

對 memory：

$$
\text{Repeated Recall Computation}
\rightarrow
\text{Crystallized Hyperlink}.
$$

因此 CHM 是 Crystallized Computation 在 memory domain 的一個具體實作。

---

# 80. Complexity Transfer

Hot path 把成本從 online recall 移到：

- route observation；
- compilation；
- maintenance；
- invalidation。

因此：

$$
\boxed{
\text{Complexity Is Transferred, Not Destroyed}.
}
$$

這與 UNPNP 的核心直覺一致。

---

# 81. Online / Offline Cost

可寫：

$$
C_{\mathrm{total}}
=
C_{\mathrm{offline}}
+
\sum_t C_{\mathrm{online},t}.
$$

如果 route reuse 高，增加：

$$
C_{\mathrm{offline}}
$$

可能降低總成本。

但低 reuse 則相反。

---

# 82. Compile Budget

系統可以限制：

$$
B_{\mathrm{compile}}.
$$

只選 top candidate routes。

避免 background optimizer 吃掉所有資源。

---

# 83. Maintenance Budget

同樣：

$$
B_{\mathrm{maintain}}.
$$

若超過 budget，低價值 routes 先 demote。

因此 CHM 本身也需要 resource governance。

---

# 84. Priority

高優先 path：

- resident core；
- active project；
- current responsibility；
- frequently used decision；
- critical source.

低優先：

- old one-off exploration；
- rarely used historical thread。

---

# 85. Memory Path Ecology

長期系統會形成：

$$
\mathcal L_R
=
\{
\ell_1,\ldots,\ell_n
\}.
$$

其中 routes：

- 出生；
- 成熟；
- 使用；
- 修復；
- stale；
- retire。

因此 CHM 是動態 path ecology，而不是靜態 shortcut table。

---

# 86. Path Learning

可定義：

$$
LearnPath:
RecallReceipts
\rightarrow
NavigationCrystal
\rightarrow
CompiledCandidate.
$$

這形成：

$$
Experience
\rightarrow
MemoryNavigationKnowledge.
$$

---

# 87. No Hidden Autonomy Claim

Path learning 不等於 AI 產生自己的任務 agenda。

它只是：

$$
TaskGiven
\rightarrow
BetterRecallMethod.
$$

因此可以存在於 bounded cognitive autonomy 內。

---

# 88. Human Review

高風險 route promotion 可以要求：

$$
HumanReview.
$$

例如：

- identity-related；
- security-related；
- legal；
- cross-resident shared memory。

一般低風險 project recall 可自動 promotion。

---

# 89. AI Review

也可用 second-agent verifier：

$$
CandidateRoute
\rightarrow
Verifier.
$$

但 verifier 只提供 evidence，不自動擴權。

---

# 90. Route Provenance

每條 hot path 應能回答：

> 為什麼存在？

包含：

- originating recall receipts；
- source objects；
- validation；
- promotion decision；
- current dependencies。

---

# 91. Auditing

audit query：

$$
WhyDidYouRecall(X)?
$$

可回：

$$
QueryClass
\rightarrow
Route
\rightarrow
Target
\rightarrow
Source.
$$

這比黑箱 vector top-k 更可解釋。

---

# 92. Privacy

route metadata 本身可能洩漏：

> 某 resident 有某 private project。

因此 CHM route store 也必須有 ACL。

---

# 93. Metadata Minimization

public logs 不應寫完整 private query / target。

可只記 opaque IDs + status。

---

# 94. Cross-Line Reuse

同 resident 多 lines 可以共享 project-scoped hot path。

因此一條 line 發現成功 route，可以讓其他 line 未來直接受益。

這是 multi-conversation memory 的重要增益。

---

# 95. Cross-Project Reuse

只有語義穩定、scope 合法時，project route 才可 promotion 到 resident-level navigation.

不能因為 route technically works 就跨 project reuse。

---

# 96. Query Drift

同 query class 隨時間可能改變語義。

例如：

```text
current architecture
```

target 會變。

因此 current-state route 應指向：

$$
CurrentHeadResolver
$$

而不是固定舊 object revision。

---

# 97. Static vs Dynamic Target

可分：

$$
targetMode
\in
\{
static,
dynamic
\}.
$$

static：

$$
exact historical source.
$$

dynamic：

$$
current accepted decision.
$$

兩種 validation 不同。

---

# 98. Dynamic Resolver

dynamic route：

$$
\ell
\rightarrow
Resolver(current\_accepted\_decision).
$$

resolver 再取得 current object。

這避免 route 每次 head 更新都完全重寫。

---

# 99. Stable Semantic Alias

可有：

```text
project:SOACR/current-architecture
```

作 logical alias。

但 alias mapping 本身必須 canonical / versioned。

---

# 100. Alias 不等於自由字串搜尋

alias 是 registry entry。

不是：

> 猜一個看起來像 current architecture 的檔案。

因此：

$$
\boxed{
\text{Semantic Alias}
\neq
\text{Filename Heuristic}.
}
$$

---

# 101. Path Compression Levels

可定義：

## L0

raw recall trace。

## L1

navigation crystal。

## L2

typed route。

## L3

compiled hyperlink。

## L4

composite path。

越高層越快，但 maintenance burden 越高。

---

# 102. Promotion Across Levels

只有 evidence 足夠才：

$$
L0\rightarrow L1\rightarrow L2\rightarrow L3.
$$

不必所有 memory 都走到 L3。

---

# 103. Memory Path Compiler

第一代 compiler 可以很保守：

```text
input:
  route receipts
  query class
  scope
  source revisions

output:
  candidate hyperlink
  utility estimate
  validation report
  fallback
```

不需要 LLM 自由生成任意 shortcut。

---

# 104. Deterministic Compiler Core

安全相關部分應盡量 deterministic：

- schema；
- revision binding；
- scope；
- dependency；
- fallback；
- invalidation.

LLM 可以提出 candidate route，但 deterministic validator 決定是否可 compile。

---

# 105. Semantic Proposal / Deterministic Commit

可以：

$$
LLM
\rightarrow
RouteProposal.
$$

再：

$$
Validator
\rightarrow
CompiledRoute.
$$

因此：

$$
\boxed{
\text{Semantic Proposal}
\neq
\text{Runtime Commit}.
}
$$

---

# 106. Storage Schema Candidate

Compiled route 可存：

```text
route_id
route_kind
query_class
scope
anchor_ref
target_ref
required_capabilities
authority_mode
source_revision_refs
semantic_revision_refs
validator
fallback
state
metrics
created_at
last_validated
expires_at
```

這是 Paper 07 可直接擴充的基礎。

---

# 107. Route Receipt Candidate

```text
receipt_id
route_id
resident_id
line_id
task_id
used_at
result
latency_ms
materialized_bytes
fallback_used
validation_result
```

可供 optimizer 使用。

---

# 108. Compiled Route 不是 Canonical Memory Truth

即使 persistent：

$$
\widehat{\ell}
$$

仍只是 derived operational object。

所以：

$$
\boxed{
\widehat{\ell}
\neq
CanonicalMemory.
}
$$

刪除 route 只降低效能，不應刪除 memory truth。

---

# 109. Rebuildability

理想上：

$$
Delete(\mathcal L_R)
$$

後，系統仍可透過 cold recall 找到 memory。

因此：

$$
\boxed{
\text{CHM Is an Acceleration Layer, Not a Single Point of Truth}.
}
$$

---

# 110. Disaster Recovery

若 compiled routes 全毀：

1. CSG 保留；
2. MNEME 保留；
3. cold recall 恢復；
4. route learning 重新累積。

這是健康架構。

---

# 111. Performance Metrics

至少測：

$$
T_{\mathrm{cold}},
T_{\mathrm{warm}},
T_{\mathrm{hot}}.
$$

以及：

$$
Bytes_{\mathrm{materialized}},
Tokens_{\mathrm{context}},
SearchCalls,
SourceReads.
$$

---

# 112. Correctness Metrics

測：

- target correctness；
- source fidelity；
- stale recall；
- scope correctness；
- fallback correctness；
- unauthorized route attempt。

---

# 113. Compilation Metrics

測：

- candidate count；
- promotion rate；
- break-even；
- maintenance cost；
- demotion rate；
- invalidation fanout。

---

# 114. Baseline Experiment

對一組重複 query：

$$
Q=\{q_1,\ldots,q_n\},
$$

比較：

## Baseline

每次 full semantic search。

## CHM

cold → warm → hot。

測 cumulative cost：

$$
C_{\mathrm{baseline}}(n)
$$

與：

$$
C_{\mathrm{CHM}}(n).
$$

---

# 115. Expected Curve

CHM 初期：

$$
C_{\mathrm{CHM}}
>
C_{\mathrm{baseline}}
$$

可能成立，因有 compilation overhead。

但若 reuse 高：

$$
n>n^\*
$$

後：

$$
C_{\mathrm{CHM}}
<
C_{\mathrm{baseline}}.
$$

---

# 116. Scalability

當 memory size：

$$
M\uparrow,
$$

cold search cost 可能上升。

但 hot path 若 target stable：

$$
T_{\mathrm{hot}}
$$

可保持近似 bounded。

因此 CHM 對超大 memory world 特別有價值。

---

# 117. Path Selection Scalability

但 route count：

$$
L\uparrow
$$

也會增加 selector cost。

所以需要：

- scope partition；
- query class；
- project partition；
- route retirement；
- hierarchical selector。

---

# 118. Hierarchical Route Selection

可先：

$$
Resident
\rightarrow
Project
\rightarrow
QueryClass
\rightarrow
Route.
$$

而不是在所有 routes 全域搜尋。

這本身又是一種 routing tree。

---

# 119. Recursive Compilation

若 path selector 本身反覆走穩定路徑，也可以編譯。

但 recursive optimization 要避免無限 meta-layer。

第一代只做一層即可。

---

# 120. Hyperlink as Externalized Computation

從更一般角度：

$$
\widehat{\ell}
$$

把部分曾經需要模型重新推理的 navigation decision 外部化。

所以：

$$
\boxed{
\text{Memory Hyperlink}
=
\text{Externalized Reusable Cognitive Transition}.
}
$$

這正是其 AI-native 計算意義。

---

# 121. 與 UNPNP 的連接

UNPNP 的核心直覺之一，是將高成本路徑搜尋與重複計算外移，並透過 hyperlink / path compilation 讓未來 execution 直接跨越已知結構。

CHM 在 memory domain 中對應：

$$
\text{Memory Search Space}
\rightarrow
\text{Validated Route}
\rightarrow
\text{Compiled Hyperlink}.
$$

因此：

$$
\boxed{
\text{CHM is a memory-domain instantiation of path crystallization}.
}
$$

---

# 122. 與 Crystallized Semantic Graph 的連接

CSG 讓：

$$
SemanticState
$$

變得可 address。

CHM 讓：

$$
TransitionBetweenSemanticStates
$$

也可以被 address / compile。

因此：

$$
\boxed{
\text{CSG crystallizes semantic states;}
}
$$

$$
\boxed{
\text{CHM crystallizes successful semantic transitions}.
}
$$

這是兩者最精確的分工。

---

# 123. 與 Named AI 的連接

同一 resident 的多 lines：

$$
L_1,\ldots,L_n
$$

可以共同累積 route evidence。

因此 resident 不只共享：

$$
\mathcal H_R,
$$

也可以共享：

$$
\mathcal L_R^{project/resident}.
$$

這讓一條 line 的成功 recall 經驗成為其他 lines 的未來 acceleration。

---

# 124. Responsibility Domain

如果 resident 長期負責某 project，project-scoped CHM 會逐漸成熟。

因此：

$$
Resp(R,P)
$$

越長期，

$$
NavigationKnowledge(R,P)
$$

也可能越豐富。

這使「負責域」不只是 task ownership，也逐漸形成專門 recall infrastructure。

---

# 125. Cognitive Specialization

不同 resident 甚至可能形成不同 navigation habits：

$$
\mathcal L_{R_A}
\neq
\mathcal L_{R_B}.
$$

即使共用同一 canonical source，也可能有不同合法 route preferences。

這是未來具名 AI specialization 的一種工程表現。

---

# 126. 但不應將 Route Preference 神格化為人格本體

route habit 只是 operational pattern。

不能：

$$
RoutePattern
\Rightarrow
Personhood.
$$

本文仍保持 engineering interpretation。

---

# 127. 第一代工程範圍

第一代 CHM 可只做：

```text
single resident
project-scoped routes
read-only memory hyperlinks
query classes
route receipts
navigation crystals
candidate promotion
revision binding
fallback
manual / deterministic invalidation
```

暫不做：

- cross-resident routes；
- executable action hyperlinks；
- autonomous registrar mutation；
- destructive writes；
- unrestricted recursive path compilation。

---

# 128. 第一代 Acceptance Tests

## H1 — Cold Recall Works Without CHM

刪除 compiled routes 後仍能找到正確 memory。

## H2 — Warm Evidence

重複 query 產生可比較 route receipts。

## H3 — Promotion

達 threshold 後形成 candidate / hot route。

## H4 — Hot Recall

hot route 比 cold baseline 少 search / source reads。

## H5 — Fallback

target stale 時成功回 cold/warm path。

## H6 — Scope Isolation

Project A route 不用於 Project B。

## H7 — Identity Gate

unresolved resident 無法走 private route。

## H8 — Capability Gate

缺 capability 時 route unavailable。

## H9 — Revision Invalidation

source revision 變更後 route revalidate。

## H10 — Permission Revision

permission change 不會因 hot path 被繞過。

## H11 — Decompression

composite route 可回溯 underlying route。

## H12 — Rebuildability

刪 route store 後 canonical memory 不受影響。

---

# 129. 可證偽研究問題

## Q1. CHM 是否真正降低重複 recall cost？

比較：

$$
T_{\mathrm{cold}}
$$

與：

$$
T_{\mathrm{hot}}.
$$

## Q2. Path Compilation 的 break-even 在哪？

估計：

$$
n^\*.
$$

## Q3. Query class 是否會造成過度泛化？

測 wrong-target rate。

## Q4. Navigation crystal 是否跨模型可重用？

讓不同 model 執行同一 standardized route。

## Q5. Route maintenance 是否會抵消效益？

測 source volatility 不同時：

$$
C_{\mathrm{maintain}}.
$$

## Q6. Route count 增加是否造成 selector congestion？

測：

$$
L
\rightarrow large.
$$

## Q7. Project-scoped route 是否降低跨 line bootstrap cost？

比較不同 lines 首次接手 project 的 recall latency。

## Q8. Composite hyperlink 是否保持 auditability？

測 decompression completeness。

---

# 130. 最小不變式

## H-1 Stored Memory Is Not Efficient Recall

$$
\boxed{
\text{Stored}
\not\Rightarrow
\text{CheapToRecall}.
}
$$

## H-2 Navigation Knowledge Is Derived

$$
\boxed{
\text{Navigation Crystal}
\neq
\text{Canonical Memory Truth}.
}
$$

## H-3 Path Compilation Is Selective

$$
\boxed{
\text{Observed Route}
\not\Rightarrow
\text{Compiled Route}.
}
$$

## H-4 Compile Only When Utility Is Positive

$$
\boxed{
U(\ell)>0
}
$$

is required for promotion.

## H-5 Path Compilation Does Not Compile Permission

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

## H-6 Identity Before Private Hot Path

$$
\boxed{
ResolveIdentity
\prec
UsePrivateRoute.
}
$$

## H-7 Capability Before Execution

$$
\boxed{
Req(\ell)
\subseteq
\mathcal C_\rho.
}
$$

## H-8 Stale Route Must Revalidate

$$
\boxed{
DependencyChange
\Rightarrow
Revalidate.
}
$$

## H-9 Technical Failure May Fallback

$$
\boxed{
TechnicalMiss
\Rightarrow
SafeFallback.
}
$$

## H-10 Authority Failure Must Fail Closed

$$
\boxed{
AuthorityFail
\Rightarrow
Deny.
}
$$

## H-11 Fast Path Remains Auditable

$$
\boxed{
CompiledRoute
\rightarrow
UnderlyingProvenance.
}
$$

## H-12 CHM Is Rebuildable

$$
\boxed{
Delete(CHM)
\not\Rightarrow
Loss(CanonicalMemory).
}
$$

---

# 131. 系列位置

Paper 00：Resident-Centric Continuity。

Paper 01：Resident Conversation Graph。

Paper 02：Conversation Graph × CSG。

Paper 03：Shared Governed Memory World。

Paper 04：Runtime Profiles。

Paper 05：Canonical Storage Architecture。

本文 Paper 06 建立：

$$
\boxed{
\text{Retrieval Path}
\rightarrow
\text{Navigation Crystal}
\rightarrow
\text{Compiled Memory Hyperlink}.
}
$$

下一篇 Paper 07 將專門處理：

- Authorized Shortest Path；
- Safe Reachable World；
- capability envelope；
- revocation；
- permission propagation；
- prompt injection；
- risk-adjusted route cost；
- fail-closed security semantics。

因此 Paper 06 刻意只建立 performance / path crystallization 基礎，而不把安全模型壓縮成附註。

---

# 132. 結論

長期 AI 記憶的下一個瓶頸，不只是「如何保存更多內容」，而是：

> AI 每次回想時，是否仍要重新做一次昂貴的搜尋與推理？

本文提出 Crystallized Hyperlink Memory，讓成功 recall experience 本身成為可重用知識：

$$
\boxed{
\text{Remember what}
+
\text{Remember how to remember}.
}
$$

第一次 recall 可以昂貴：

$$
ColdRecall.
$$

多次成功後形成：

$$
WarmRoute.
$$

只有在 reuse、validation、stability、risk、maintenance 與 fallback 條件成立時，才進一步：

$$
\boxed{
P_{\mathrm{memory}}
\rightarrow
\widehat{\ell}_{\mathrm{memory}}.
}
$$

這條 hyperlink 不是單純 URL，而是一個具有 logical target、query class、scope、revision、validator、fallback 與 invalidation semantics 的 typed cognitive transition。

由此，Crystallized Semantic Graph 負責結晶：

$$
\text{Semantic State},
$$

而 CHM 負責結晶：

$$
\text{Successful Transition Between States}.
$$

兩者結合後，具名 AI 的共享記憶世界不只變得可檢索，也逐漸變得**可編譯**。

但本文同時保留最重要的界線：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

以及：

$$
\boxed{
\text{Faster Recall}
\not\Rightarrow
\text{Greater Authority}.
}
$$

因此 CHM 的角色不是繞過安全層，而是在安全、身份與 canonical memory 邊界內，將反覆成功的記憶搜尋工作外部化、結晶化並重用。

最終，本篇可以濃縮為四句：

$$
\boxed{
\text{Memory stores answers.}
}
$$

$$
\boxed{
\text{Navigation memory stores routes.}
}
$$

$$
\boxed{
\text{Path compilation turns stable routes into reusable transitions.}
}
$$

$$
\boxed{
\text{Complexity is transferred from repeated recall into governed compilation and maintenance.}
}
$$

這使具名 AI 從「擁有長期記憶」進一步邁向「擁有逐步成熟的回想基礎設施」。

---

## 內部理論與工程銜接

本文直接銜接：

- Paper 00：Resident-Centric Named-AI Continuity；
- Paper 01：Resident Conversation Graph；
- Paper 02：Conversation Graph × CSG；
- Paper 03：Shared Governed Memory World；
- Paper 04：Residence Runtime Profiles；
- Paper 05：Canonical Storage Architecture；
- Crystallized Semantic Graph：semantic state crystallization；
- SOACR：MemoryNeed / purpose-aware recall；
- MNEME：canonical memory / provenance；
- LIMEN：identity / authorization；
- UNPNP：Path Compilation / Hyperlink / Effective Path Encoding。

本文新增的核心抽象為：

$$
\boxed{
P_{\mathrm{memory}}
\rightarrow
C_{\mathrm{navigation}}
\rightarrow
\widehat{\ell}_{\mathrm{memory}}
}
$$

以及：

$$
\boxed{
U(\ell)
=
B_{\mathrm{reuse}}
+
B_{\mathrm{latency}}
+
B_{\mathrm{context}}
+
B_{\mathrm{future}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{select}}
-
C_{\mathrm{risk}}.
}
$$

作為後續 Authorized Hyperlink Runtime 的 path crystallization substrate。
