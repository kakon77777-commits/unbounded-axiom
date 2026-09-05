# Cosmogenesis Ontology v0.2
## 廣義宇宙生成論本體表：Claim-Scoped Evidence、Dual Origin 與 Emergent Spacetime

**日期：** 2026-08-21  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**狀態：** v0.2 Canonical Schema Draft  
**前版：** Cosmogenesis Ontology v0.1  
**資料母表：** Cosmogenesis Master Table v0.2  

---

# 0. v0.2 的真正更新

v0.1 建立：

$$
\boxed{
\text{Generation Topology}
\neq
\text{Physical Mechanism}
\neq
\text{Evidence Status}
\neq
\text{Ultimate Ontology}.
}
$$

v0.2 進一步發現：

$$
\boxed{
\text{Model Name}
\neq
\text{Claim Scope}
\neq
\text{Evidence Scope}.
}
$$

同一模型可以同時含有：

- 高證據子命題；
- 中等物理候選；
- 低證據終極起源解讀。

因此 row-level `Physical_Status` 只能作 coarse summary；正式評估優先使用：

`Evidence_By_Claim_Scope`。

---

# 1. v0.2 核心新增欄位

## 1.1 Parent_Model_ID

用於：

$$
\boxed{
\text{Family}
\rightarrow
\text{Realization}
}
$$

例如 Generic Big Bounce 可作 LQC / Matter Bounce 的 parent family。

---

## 1.2 Branch_Type

`GEN-BRANCH` 在 v0.1 太粗。

v0.2 增加：

- `BR-BUBBLE`
- `BR-QUANTUM`
- `BR-CAUSAL`
- `BR-CONSTRUCTION`
- `BR-GROWTH`
- `BR-BLACKHOLE`
- `BR-WORMHOLE`
- `BR-SYMMETRY`

因此：

$$
\boxed{
\text{Branching}
\neq
\text{one universal causal relation}.
}
$$

Everett branching、bubble nucleation、baby-universe budding 與 causal-set growth 不應使用同一語義。

---

## 1.3 Transition_Target

生成算子必須回答：

> 到底什麼被轉換？

候選：

- phase；
- vacuum；
- aeon；
- brane；
- boundary；
- causal set；
- pre-geometric state；
- spacetime geometry；
- world instance。

因此：

$$
\boxed{
\mathcal G
=
\mathcal G(Target).
}
$$

---

## 1.4 Fate_Module

Big Crunch 類結構主要描述：

$$
\mathcal F(W),
$$

不是：

$$
\mathcal G(W).
$$

只有：

$$
\mathcal F(W_n)
\rightarrow
\mathcal G(W_{n+1})
$$

時才構成 regeneration chain。

---

## 1.5 Internal_Origin / External_Origin

對 nested / constructed / holographic worlds：

$$
\boxed{
Origin_{internal}(W)
\neq
Origin_{external}(W).
}
$$

例如 simulated world 可同時具有：

- internal Hot Big Bang；
- external host instantiation。

這兩個 origin 都合法，但 relation 不同。

---

## 1.6 Realization_Domain

新增：

- `RD-COSMOS`：直接作物理宇宙模型；
- `RD-QG-TOY`：量子重力／toy realization；
- `RD-HOLO`：holographic realization；
- `RD-COMP-ENG`：計算／工程人工世界；
- `RD-LAB-CAND`：實驗室宇宙候選；
- `RD-MATH`：純形式／數學 realization。

核心：

$$
\boxed{
\text{Realized Somewhere}
\not\Rightarrow
\text{Realized as Our Cosmos}.
}
$$

---

## 1.7 Evidence_By_Claim_Scope

形式：

```yaml
evidence_by_claim_scope:
  - claim: "hot-dense early evolution"
    status: "PA-5"
  - claim: "absolute temporal beginning"
    status: "ULT-OPEN"
```

因此：

$$
\boxed{
Evidence(Model)
}
$$

不再視為單值。

---

# 2. 新增 Dimensional Code：DIM-EMERG

第二批模型逼出：

`DIM-EMERG`

表示：

> dimensional / spacetime structure 本身由 pre-geometric degrees of freedom emergent。

適用候選：

- Group Field Theory geometrogenesis；
- Causal Set continuum emergence；
- Causal Dynamical Triangulations；
- matrix / non-geometric cosmology。

這和：

`DIM-CHANGE`

不同。

`DIM-CHANGE` 表示已存在維度結構發生改變。

`DIM-EMERG` 表示「維度／時空」本身才是生成結果。

---

# 3. v0.2 的新宇宙生成分類

第二批正式納入：

1. Group Field Theory condensate cosmology / geometrogenesis；
2. Causal Set Classical Sequential Growth；
3. Causal Dynamical Triangulations emergent de Sitter universe；
4. CPT-symmetric universe；
5. Cosmological Natural Selection；
6. Farhi–Guth–Guven laboratory-universe tunneling；
7. Holographic eternal inflation；
8. Higher-order gravity finite-action safe beginning；
9. Wineglass-wormhole birth of inflationary universes；
10. Wormhole-assisted false-vacuum bubble tunneling。

---

# 4. Pre-Geometric Cosmogenesis

v0.1 多數模型仍可理解為：

$$
\text{spacetime state}
\rightarrow
\text{new spacetime state}.
$$

v0.2 正式加入：

$$
\boxed{
\text{Non-Spatiotemporal / Discrete / Pre-Geometric Structure}
\rightarrow
\text{Spacetime}.
}
$$

這形成新的母類：

## CG-PG｜Pre-Geometric Cosmogenesis

典型：

$$
Q_{pregeo}
\overset{GEN-EMERG}{\longrightarrow}
W_{spacetime}.
$$

這是一個重要擴張，因為宇宙生成不再預設：

> 生成以前一定已經有 classical spacetime。

---

# 5. Growth Cosmogenesis

Causal Set Classical Sequential Growth 逼出：

$$
\boxed{
BR-GROWTH.
}
$$

它不是：

- bubble；
- parent–child budding；
- Everett branch。

而是：

$$
C_n
\rightarrow
C_{n+1}
$$

的離散 successor / accretion history。

因此：

$$
\boxed{
\text{Cosmogenesis}
}
$$

可以是：

> world structure 在生成過程本身逐步「長出來」。

---

# 6. Symmetry-Branch Cosmogenesis

CPT-symmetric universe 逼出：

`BR-SYMMETRY`

其 relation 類型是：

$$
W_-
\overset{CPT}{\longleftrightarrow}
W_+.
$$

它不是典型 parent-child。

所以：

$$
\boxed{
\text{paired universe relations}
}
$$

也必須和 reproductive branching 分開。

---

# 7. Reproductive Cosmogenesis

Cosmological Natural Selection 不是只有：

$$
Parent
\rightarrow
Child.
$$

它還加入：

$$
\mathcal L_p
\rightarrow
\mathcal L_c
$$

的 parameter mutation / selection structure。

因此 v0.2 明確分：

$$
\boxed{
\text{Generation Operator}
\neq
\text{Inheritance / Mutation Rule}
\neq
\text{Selection Rule}.
}
$$

---

# 8. Constructed Physical Cosmogenesis

FGG 類模型很重要，因為它和 simulation 不同。

Simulation：

$$
Code+Runtime
\rightarrow
W_{sim}.
$$

FGG 類候選：

$$
\text{physical false-vacuum configuration}
\overset{quantum\ tunneling}{\longrightarrow}
W_{child}.
$$

所以 Layer IV 必須分：

- computational construction；
- physical laboratory cosmogenesis candidate。

---

# 9. Holographic Origin Relations

Holographic eternal inflation 顯示：

$$
Origin_{bulk}
$$

與：

$$
Origin_{boundary-description}
$$

可以不同。

這不是 ordinary nested simulation，但同樣需要 dual-origin language。

因此：

$$
\boxed{
\text{External Origin}
}
$$

不是只服務 simulation。

---

# 10. Topology as Generator Variable

Wineglass wormholes 與 wormhole-assisted bubble tunneling顯示：

$$
\boxed{
\text{spacetime topology}
}
$$

可能不是生成後的附加特徵，而是：

$$
\mathcal G
$$

本身的參數／結構。

因此未來 v0.3 可考慮：

`Topological_Transition`

作候選 dynamic field。

---

# 11. Model Role Taxonomy

v0.2 建議正式角色：

- `BaselineEvolution`
- `EarlyDynamicsModule`
- `BoundaryConditionProposal`
- `GenerationOperatorFamily`
- `CompleteScenario`
- `FateModule`
- `MultiverseTaxonomy`
- `QGEmergenceProgram`
- `ConstructedRealization`
- `UpperOntology`

因此：

$$
\boxed{
\text{Big Bang}
,\text{Inflation}
,\text{Big Crunch}
,\text{Tegmark Level IV}
}
$$

不能被當作同一類 model object。

---

# 12. Claim-Scoped Evidence 原則

最終推薦：

$$
\boxed{
E(M)
=
\{(q_i,E_i)\}.
}
$$

不是：

$$
E(M)=e.
$$

例如：

Simulation：

- `artificial virtual worlds are constructible`：高；
- `our universe is simulated`：低／開放。

Hot Big Bang：

- `early hot dense regime`：高；
- `absolute beginning of all reality`：不由該證據推出。

GFT：

- `formal condensate cosmology exists`：中；
- `our universe emerged by GFT geometrogenesis`：未建立。

---

# 13. v0.2 Master Record

```yaml
cosmogenesis_model:
  model_id: "CGM-..."
  canonical_name: "..."
  family: "..."
  research_layer: "..."
  model_role: "..."
  claim_scope: "..."
  parent_model_id: "..."
  branch_type: []
  transition_target: "..."
  fate_module: "..."
  internal_origin: "..."
  external_origin: "..."
  realization_domain: "..."
  evidence_by_claim_scope: []
  precursor_type: []
  generation_operator: []
  temporal_topology: []
  causal_topology: []
  dimensional_relation: []
  law_inheritance: []
  seed_type: []
  multiplicity: "..."
  connectivity: []
  substrate: []
  generator_agency: []
  difference_source: []
  physical_status: "PA-?"
  observability: []
  ultimate_status: "ULT-OPEN"
  evidence_summary: "..."
  predictive_signatures: []
  major_open_problems: []
  composition_sequence: []
  sources: []
  dynamic_fields: {}
```

---

# 14. v0.2 總式

$$
\boxed{
\mathfrak{CG}^{(0.2)}
=
\left(
\mathcal W,
\mathfrak S,
\mathbb G_C,
G_U,
\mathcal L,
\mathcal X,
\mathcal E_{scope},
\mathcal R_D,
\mathbf U_C
\right).
}
$$

其中新增：

- $\mathcal E_{scope}$：claim-scoped evidence map；
- $\mathcal R_D$：realization-domain map。

---

# 15. 目前最重要的理論發現

第一：

$$
\boxed{
\text{宇宙生成不必預設生成前已有 classical universe / spacetime。}
}
$$

第二：

$$
\boxed{
\text{同一 universe 可以有多個 relation-indexed origins。}
}
$$

第三：

$$
\boxed{
\text{Branching 至少有 bubble、quantum、growth、black-hole、wormhole、construction、symmetry 等不同語義。}
}
$$

第四：

$$
\boxed{
\text{模型的證據不能再被壓成單一分數。}
}
$$

第五：

$$
\boxed{
\text{宇宙生成論已經自然跨入量子重力、拓撲、資訊、人工世界與上位本體分類。}
}
$$

---

# 16. v0.3 暫定待測欄位

暫不升格，等待第三批模型：

- `Topological_Transition`
- `Selection_Rule`
- `Mutation_Rule`
- `Law_Origin`
- `Spacetime_Origin`
- `Observer_Domain`
- `Measure_Problem_Type`
- `Topology_Change_Certificate`
- `Origin_Relation_ID`
- `Nested_Depth`

---

# 17. 結論

v0.1 問：

> 一個 universe 怎麼生成？

v0.2 已經被真實模型逼成：

> **哪一個 claim 在談哪一種 origin？  
> 哪個 relation 在 branch？  
> 什麼 target 被轉換？  
> 這個生成只在 toy/holographic/computational domain 被實現，還是真的在 physical cosmos 有 evidence？  
> 時空本身是不是才是生成結果？**

因此 Cosmogenesis Ontology 已從一張「宇宙起源分類表」，開始變成：

$$
\boxed{
\text{Universe-Generation Relation Language}.
}
$$

這正是之後要做 Meta-Cosmogenesis series / database 的真正底座。

**END — COSMOGENESIS ONTOLOGY v0.2**
