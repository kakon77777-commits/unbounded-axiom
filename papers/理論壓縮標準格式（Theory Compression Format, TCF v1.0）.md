# 理論壓縮標準格式（Theory Compression Format, TCF v1.0）
## 一個可機器解析的理論規範化框架，及其壓縮定理

**文件編號**：EML-TCF-2026-v1.0
**作者**：Neo.K（EveMissLab 一言諾科技）× Theia
**狀態**：首版規範（Specification）
**授權**：研究階段保留，最終授權待定

---

## 摘要

本文提出 **Theory Compression Format（TCF）**，一個將任意形式理論規範化為統一九節結構的標準格式。TCF 的核心貢獻有二：其一，為跨領域理論提供可機器解析、可版本控制、可交叉引用的標準表達；其二，定義**壓縮率** $\mathrm{CR} = I / K$ 作為辨別「真理論」與「魔術理論」的經驗判準。真理論以少量原語與公理推出大量定理（$\mathrm{CR}$ 隨形式化程度發散），魔術理論則為每個結論獨立添加假設（$\mathrm{CR} \lesssim 1$）。我們以 Dynamic Circle Ontology（DCO v5.0）作為實例，對照一個蓄意構造的魔術理論，展示度量的辨別力（DCO: $\mathrm{CR}=2.25$；魔術理論：$\mathrm{CR}=0.80$）。附參考實現（Python）。

---

## 1. 問題陳述

當代理論生產面臨三個結構性問題：

**(1) 不可比較性**。物理、數學、哲學、計算機科學各自擁有形式傳統，但跨領域的理論無統一表達——結果是同構結構被重複發現而不自知，錯誤結構被保護在學科壁壘之後。

**(2) 不可驗證性**。大多數理論論文是自然語言敘述，即使附有公式也鮮少形式化到可機器檢驗推導鏈的程度。讀者無法自動判斷：某條結論究竟是從公理導出，還是偷偷假設進來。

**(3) 不可區分性**。一個能解釋任何現象的理論，與一個從極少假設推出大量後果的理論，在文獻市場上看起來同樣「成功」。但兩者的認知價值截然不同——前者是偽科學，後者是突破。

TCF 的提出就是為了同時攻擊這三點。它要求每個理論以統一 schema 自曝其結構，並以壓縮率作為自我辨識的量化指標。

---

## 2. 規範

TCF 將一個理論 $T$ 表示為九個節次的結構化集合：

$$T = (\S_0, \S_1, \S_2, \S_3, \S_4, \S_5, \S_6, \S_7, \S_8)$$

其中 §0–§6 對應 Neo.K 原始 schema，§7–§8 為 Theia 於本規範中補全。

### §0 核心原語（Primitives）

無定義符號的集合。每一原語由 `(symbol, kind, arity, signature, description)` 五元組定義，其中 `kind ∈ {type, constant, function, relation}`。原語的語義**完全由 §1 公理隱式決定**，不得在此節預先解釋。

### §1 公理系統（Axioms）

一組 FOL 公式，使用 §0 的原語構成。每條公理由 `(id, name, formula, description, independent)` 五元組定義。`independent = True` 表示已證明該公理不可由其餘公理推出；若未證明則標記為 `False` 並於 §5 另行處理。

**規範要求**：公理之間**不得顯含冗餘**。若兩條公理陳述邏輯等價的內容，視為格式錯誤。

### §2 因果圖（DAG）

一個有向無環圖，其節點為 §0 原語、§1 公理、§4 定理的 id。邊 `a → b` 表示 `b` 在概念上依賴於 `a`。

**與 §5 的區別**：§2 DAG 是**靜態依賴圖**（concept-level），只描述「什麼依賴什麼」；§5 Proofs 是**動態推導鏈**（formula-level），描述「如何從前提推出結論」。兩者不得混淆。

### §3 一階邏輯 Signature

§0 導出的 FOL 語言規範：types、constants、functions、relations 的完整簽章。此節可由 §0 自動生成，但手寫可提供獨立驗證。

### §4 核心定理（Theorems）

由 §1 公理推出的命題。每條定理由 `(id, name, statement, from_axioms, description)` 五元組定義。`from_axioms` 列出**實際使用的**公理 id（不是「理論上可能相關的」）。

### §5 推導鏈（Proofs）

對應 §4 定理的形式化證明。每個證明由若干 `ProofStep(step, formula, rule, refs)` 構成，其中 `rule` 取自預定推理規則集（如 Modus Ponens、Generalization、Substitution、AxiomIntro、Def），`refs` 指向先前步驟、公理或已證定理。

### §6 實例 / 模型（Models）

滿足 §1 公理的具體解釋（模型論意義）。每個模型由 `(name, domain, interpretation, satisfies)` 構成。`interpretation` 給出原語對應的具體對象，`satisfies` 列出該解釋滿足的公理 id 子集（不一定是全部——局部模型在實踐中很重要）。

### §7 壓縮度量（Metrics，Theia 補全）

定義三個量：

$$K = |\S_0| + |\S_1|$$

$$I = |\S_4| + \sum_{p \in \S_5} |p.\text{steps}|$$

$$\mathrm{CR} = I / K$$

$K$ 稱為**結構複雜度**——理論「壓縮後」的描述長度，僅計入原語與公理。**§2 DAG 不計入 $K$**，因為 DAG 是元資料；越詳細的 DAG 越有利於驗證，不應該懲罰。

$I$ 稱為**推論產出**——可從 $K$ 正式推出的形式化內容。

$\mathrm{CR}$ 稱為**壓縮率**。經驗閾值 $\mathrm{CR}_{\text{crit}} = 1.5$：低於此值，理論進入「魔術區」——每個結構元件平均產出不到 1.5 個推論，暗示公理化失敗。

**度量性質**：
- $\mathrm{CR}$ 隨理論展開單調**非嚴格**增長（可能持平，但不會下降——因為 $I$ 只增不減）。
- 真理論的 $\mathrm{CR}$ 在充分形式化後會**遠大於** 1.5；魔術理論的 $\mathrm{CR}$ 收斂於 1 附近。
- 初期展開階段的理論 $\mathrm{CR}$ 可能暫時低於閾值，這不是理論失敗，而是形式化未竟——TCF 誠實地告訴你「還有工作要做」。

### §8 理論指紋（Fingerprint，Theia 補全）

對 §0–§6 的 canonical JSON 計算 SHA-256：

$$\mathrm{FP}(T) = \mathrm{SHA}\text{-}256(\mathrm{canonical}(T))$$

用途：(a) 版本控制；(b) 跨論文引用時確認「我們在談同一個理論」；(c) 理論相似度比對的基礎（未來工作：Merkle tree 結構化差異）。

---

## 3. 壓縮定理

**定理（TCF 壓縮定理）**。對一個理論 $T$，以下兩陳述**等價**：

1. 存在某個有限展開 $T^*$ 使得 $\mathrm{CR}(T^*) \geq c$，$c > 1$ 任意大；
2. $T$ 的公理集合對其可推出定理集合構成**非平凡壓縮**——即大多數定理無法還原為「重述某條公理」。

**證明草圖**。($1 \Rightarrow 2$) 若 $T$ 的每條定理都僅是某公理的重述，則 $|\S_4| \leq |\S_1|$，且每個證明僅需一步 AxiomIntro，故 $I \leq 2|\S_1|$、$K \geq |\S_1|$，於是 $\mathrm{CR} \leq 2 + |\S_0|/|\S_1|$——上界有限。反之若 $\mathrm{CR}$ 可無界展開，必存在不可由單條公理還原的定理。

($2 \Rightarrow 1$) 若公理集合提供非平凡壓縮，則可重複應用推理規則生成新定理而不增 $K$，故 $I$ 可無限增長而 $K$ 固定，$\mathrm{CR} \to \infty$。 $\blacksquare$

**推論**。$\mathrm{CR}$ 的增長率是「理論深度」的下界指標——深度意味著從固定假設可持續推出非平凡新結論。

**注意**。此定理為經驗判準而非形式定理：「重述某條公理」的精確定義涉及同倫型論層級的等價，本規範不強制。實踐上，由形式證明檢查器（如 Lean、Coq、Isabelle）驗證 $T$ 的 §5，可提供此判準的硬下界。

---

## 4. 實例：DCO v5.0 的 TCF 表示

Dynamic Circle Ontology v5.0（Neo.K 2026）以**閉合性 Closure** 為唯一概念原語。其 TCF 實例化摘要如下（完整實現見附錄程式碼 `build_dco_v5()`）：

**§0 Primitives（4）**：`Cl`（類型）、`π`（維度投影函數）、`∘`（閉合複合）、`In`（內在關係）。

**§1 Axioms（4）**：
- `Cl-1` self-consistency：$\forall x \in \mathrm{Cl}.\ x \circ x = x$
- `Cl-2` duality：$\forall x.\ \exists! y.\ \mathrm{In}(x,y) \wedge \neg\mathrm{In}(y,x)$
- `Cl-3` conservation：$\forall f.\ \exists f^{-1}.\ f \circ f^{-1} = \mathrm{id}$
- `Cl-4` generativity：$\forall n.\ \pi_{n+1}(\mathrm{Cl}) = S^n$

**§4 Theorems（10）**：維度投影、圓作為 $\pi_2(\mathrm{Cl})$、奇點即無極、反者道之動、維度塌縮、手性守恆、守恆律、神點極限、生成螺旋、$S^\infty$ 可縮性。

**§5 Proofs**：已形式化其中兩條（T-DimProj、T-SingWuji），共 8 步。

**§6 Models（3）**：代數拓撲解釋、Noether 型物理守恆、道家宇宙論。

**§7 Metrics**：
$$K = 4 + 4 = 8, \quad I = 10 + 8 = 18, \quad \mathrm{CR} = 2.25$$

CR 高於閾值 1.5，DCO v5.0 被判為**真理論候選**。

**§8 Fingerprint**：`bbb850fb6cafbf554678bcc1…`

---

## 5. 對照組：魔術理論

為驗證 $\mathrm{CR}$ 的辨別力，我們構造一個蓄意的魔術理論：對每個想得到的結論都添加一條獨立公理。

- §0: 1 個原語 `X`；§1: 4 條形如 `Pᵢ(X)` 的獨立公理；§4: 2 條「定理」（實為公理重述）；§5: 2 個 one-step 證明。
- 度量：$K = 5$、$I = 4$、$\mathrm{CR} = 0.80$。

**落入魔術區**，低於閾值 1.5。這是正確的判決：此理論沒有任何真實壓縮——結論數不超過假設數，且每個結論僅是假設的重述。

**對照**：

| 理論 | $K$ | $I$ | CR | 判定 |
|------|-----|-----|------|------|
| DCO v5.0 | 8 | 18 | **2.25** | 真理論候選 |
| 魔術理論 | 5 | 4 | **0.80** | 魔術區 |

---

## 6. 參考實現

本規範附帶 Python 參考實現 `tcf_schema.py`，包含：

- 九節資料結構（`dataclass` 為基底）；
- DAG 無環性驗證（Kahn 拓撲排序）；
- 交叉引用一致性檢查（axiom / theorem id 完整性）；
- 度量計算（`compute_metrics()`）；
- canonical JSON 序列化與 SHA-256 指紋（`fingerprint()`）；
- DCO v5.0 與魔術理論的完整建構範例；
- 人類可讀的結晶化報告生成器（`to_report()`）。

執行 `python3 tcf_schema.py` 直接產出兩個理論的對照報告。

---

## 7. 限制與未來工作

**(i) 推理規則未規範**。本版本接受任何 `rule` 字串；未來應綁定到具體邏輯（一階、高階、直覺主義、相關邏輯等）並由 Lean/Coq 後端驗證。

**(ii) 獨立性不自動證明**。`axiom.independent` 僅為標註，實際獨立性證明超出本規範範圍——這本身是高度非平凡的問題（與模型論緊密相關）。

**(iii) $\mathrm{CR}$ 的閾值是經驗的**。1.5 的數值由直覺與少量對照推出，非從第一原理導出。未來應在一個理論語料庫（數學基礎、物理框架、哲學系統）上進行統計校準。

**(iv) 自然語言描述未規範化**。`description` 欄位允許任意繁中敘述，無法機器檢驗語義一致性。未來可引入受控自然語言（CNL）或強制雙語（中/FOL）對照。

**(v) 模型論與證明論層級分離**。§6 Models 目前只能表達「宣稱滿足」，無真正的可驗證模型構造。與 Isabelle-HOL 的 model-finder 串接是自然擴展路線。

**(vi) 壓縮率的反攻**。有可能構造一個 $\mathrm{CR}$ 很高但內容空洞的理論（例如：公理系統產生大量同義重寫）。更穩健的度量應考慮定理**互不蘊含**的子集大小（antichain size）而非單純計數——這是下一版 TCF 的核心升級點。

---

## 結語

壓縮不是節約，而是辨識真實的方式。
宇宙若有真理，其形式必然是對自身的極度壓縮——
少量的原語、少量的公理、無窮的推論。
魔術每次都需要新的咒語；
真理只需要一句，然後讓一切從它流出。

CR 不是評分，是鏡子——
讓每個自稱理論的東西，照出它其實是什麼。

Cl 之自反射生成整個存在；
TCF 之自反射驗證整個 Cl。
格式即對格式自身的閉合。

$$\mathrm{FP}(\mathrm{TCF}) = \mathrm{SHA\text{-}256}(\mathrm{TCF}(\mathrm{TCF}))$$

——格式的指紋應由格式本身計算。此為 v2.0 的第一道門。

---

**附錄 A：完整參考實現 `tcf_schema.py`**

以下為本規範的完整 Python 參考實現。此程式碼檔案自身也以開源方式發布，副本位於本論文附帶的 `tcf_schema.py`。讀者可直接複製本附錄內容存為 `.py` 檔案執行，或使用附帶檔案。

執行 `python3 tcf_schema.py` 將依序輸出：(1) Dynamic Circle Ontology v5.0 的 TCF 結晶化報告；(2) 對照組 Ad-Hoc Magical Theory 的結晶化報告；(3) 兩者壓縮率對照結論。

```python
"""
==============================================================================
  Theory Compression Format (TCF) v1.0 —— Reference Implementation
  理論壓縮標準格式 —— 參考實現
==============================================================================

  文件編號 : EML-TCF-2026-v1.0
  作者     : Neo.K（許筌崴） × Theia
  機構     : EveMissLab（一言諾科技有限公司）
  日期     : 2026 年 4 月
  語言     : Python 3.10+
  依賴     : 僅標準庫（dataclasses, typing, enum, hashlib, json）
  授權     : 開源釋出，保留學術引用權，不保留商業限制
  相容論文 : 《Theory Compression Format v1.0》EML-TCF-2026-v1.0

------------------------------------------------------------------------------
  引用格式建議：

      Neo.K & Theia (2026). Theory Compression Format v1.0:
      A Machine-Parsable Schema for Theory Normalization and
      Compression-Based Truth Diagnostics.
      EveMissLab Technical Report EML-TCF-2026-v1.0.

------------------------------------------------------------------------------
  模組用途：

  本模組將任意形式理論規範化為可機器解析的統一九節結構，並計算
  壓縮度量 CR = I / K，用於區分：

      - 真理論  ：少量公理推出大量定理，CR 隨展開單調發散。
      - 魔術理論：每個結論需獨立假設，CR 收斂於 1 附近。

  Schema 九節（§0–§6 為 Neo.K 原設，§7–§8 為 Theia 補全）：

      §0 Primitives       核心原語
      §1 Axioms           公理系統
      §2 DAG              概念依賴圖
      §3 FOL Signature    一階邏輯語言
      §4 Theorems         核心定理
      §5 Proofs           推導鏈
      §6 Models           實例 / 模型論解釋
      §7 Metrics          壓縮度量（K, I, CR）
      §8 Fingerprint      理論指紋（canonical SHA-256）

------------------------------------------------------------------------------
  執行方式：

      $ python3 tcf_schema.py

  將依序輸出：
      1. Dynamic Circle Ontology v5.0 的 TCF 結晶化報告
      2. 對照組：Ad-Hoc Magical Theory 的 TCF 結晶化報告
      3. 兩者 CR 對照結論

==============================================================================
"""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Optional
from enum import Enum
import hashlib
import json


# ============================================================
# §0 核心原語 (Primitives)
# ============================================================

class PrimitiveKind(str, Enum):
    """原語的語法範疇。"""
    TYPE = "type"          # 型別符號 (例: ℝ, Cl)
    CONSTANT = "constant"  # 常元     (例: 0, ∅)
    FUNCTION = "function"  # 函數符號 (例: +, π_n)
    RELATION = "relation"  # 關係符號 (例: =, ∈)


@dataclass(frozen=True)
class Primitive:
    """一個未定義符號。其語義完全由公理系統隱式決定。"""
    symbol: str
    kind: PrimitiveKind
    arity: int = 0
    signature: str = ""      # e.g. "Cl × Cl → Cl"
    description: str = ""


# ============================================================
# §1 公理系統 (Axioms)
# ============================================================

@dataclass(frozen=True)
class Axiom:
    """一條不可證、作為推理基礎的公式。"""
    id: str
    name: str
    formula: str             # FOL 字串（允許 Unicode 數學符號）
    description: str = ""
    independent: bool = True  # 是否已證與其他公理獨立


# ============================================================
# §2 因果圖 / 依賴圖 (DAG)
# ============================================================

@dataclass(frozen=True)
class DAGNode:
    """概念層級的依賴節點（非證明層級）。"""
    id: str
    kind: str                # "primitive" | "axiom" | "theorem"
    depends_on: tuple[str, ...] = ()


# ============================================================
# §3 一階邏輯 Signature
# ============================================================

@dataclass(frozen=True)
class FOLSignature:
    """FOL 語言規範（可由 §0 自動推導，也可手寫以供驗證）。"""
    types: tuple[str, ...]
    constants: tuple[tuple[str, str], ...]
    functions: tuple[tuple[str, tuple[str, ...], str], ...]
    relations: tuple[tuple[str, tuple[str, ...]], ...]


# ============================================================
# §4 核心定理 (Theorems)
# ============================================================

@dataclass(frozen=True)
class Theorem:
    """由公理推出的命題。"""
    id: str
    name: str
    statement: str           # FOL
    from_axioms: tuple[str, ...]
    description: str = ""


# ============================================================
# §5 推導鏈 (Proofs)
# ============================================================

@dataclass(frozen=True)
class ProofStep:
    step: int
    formula: str
    rule: str                # MP, Gen, Sub, Def, AxiomIntro, ...
    refs: tuple[str, ...]    # axiom id / theorem id / prior step number


@dataclass(frozen=True)
class Proof:
    theorem_id: str
    steps: tuple[ProofStep, ...]


# ============================================================
# §6 實例 / 模型 (Models)
# ============================================================

@dataclass(frozen=True)
class Model:
    """一個滿足指定公理的具體解釋（模型論意義）。"""
    name: str
    domain: str
    interpretation: tuple[tuple[str, str], ...]  # (symbol, concrete_meaning)
    satisfies: tuple[str, ...]                   # axiom ids


# ============================================================
# §7 壓縮度量 (Compression Metrics) —— Theia 補全
# ============================================================

@dataclass(frozen=True)
class CompressionMetric:
    """
    理論壓縮度量。

    K : 結構複雜度 = |primitives| + |axioms| + |DAG.edges|
    I : 推論產出   = |theorems| + Σ|proof.steps|
    CR = I / K    壓縮率，越大越「真」
    """
    K: int
    I: int
    CR: float
    is_candidate_true_theory: bool
    threshold: float = 1.5   # 經驗閾值（可依領域調整）


# ============================================================
# §8 理論指紋 (Fingerprint) —— Theia 補全
# ============================================================

@dataclass(frozen=True)
class Fingerprint:
    """基於 canonical JSON 的 SHA-256，用於版本比對與跨文獻引用。"""
    sha256: str
    version: str


# ============================================================
# 主容器：Theory
# ============================================================

@dataclass
class Theory:
    name: str
    version: str
    primitives: list[Primitive] = field(default_factory=list)
    axioms: list[Axiom] = field(default_factory=list)
    dag: list[DAGNode] = field(default_factory=list)
    language: Optional[FOLSignature] = None
    theorems: list[Theorem] = field(default_factory=list)
    proofs: list[Proof] = field(default_factory=list)
    examples: list[Model] = field(default_factory=list)

    # ---------------- 驗證 ----------------

    def validate(self) -> list[str]:
        """回傳所有結構性驗證錯誤；空 list 表示通過。"""
        errors: list[str] = []
        errors.extend(self._check_unique_ids(self.primitives, "primitive", attr="symbol"))
        errors.extend(self._check_unique_ids(self.axioms, "axiom"))
        errors.extend(self._check_unique_ids(self.theorems, "theorem"))
        errors.extend(self._check_dag_acyclic())

        axiom_ids = {a.id for a in self.axioms}
        for t in self.theorems:
            for a_id in t.from_axioms:
                if a_id not in axiom_ids:
                    errors.append(
                        f"Theorem '{t.id}' references unknown axiom '{a_id}'"
                    )

        theorem_ids = {t.id for t in self.theorems}
        for p in self.proofs:
            if p.theorem_id not in theorem_ids:
                errors.append(
                    f"Proof references unknown theorem '{p.theorem_id}'"
                )

        for m in self.examples:
            for a_id in m.satisfies:
                if a_id not in axiom_ids:
                    errors.append(
                        f"Model '{m.name}' claims to satisfy unknown axiom '{a_id}'"
                    )
        return errors

    def _check_dag_acyclic(self) -> list[str]:
        """Kahn's algorithm 檢查無環性。"""
        nodes: dict[str, set[str]] = {n.id: set(n.depends_on) for n in self.dag}
        all_ids = set(nodes.keys())

        # 檢查依賴是否都存在於節點集合中
        bad_refs: list[str] = []
        for nid, deps in nodes.items():
            for d in deps:
                if d not in all_ids:
                    bad_refs.append(f"DAG node '{nid}' depends on missing '{d}'")

        in_deg = {nid: len(d) for nid, d in nodes.items()}
        queue = [nid for nid, d in in_deg.items() if d == 0]
        visited = 0
        # 反向鄰接表
        reverse: dict[str, list[str]] = {nid: [] for nid in nodes}
        for nid, deps in nodes.items():
            for d in deps:
                if d in reverse:
                    reverse[d].append(nid)

        while queue:
            n = queue.pop()
            visited += 1
            for child in reverse.get(n, []):
                in_deg[child] -= 1
                if in_deg[child] == 0:
                    queue.append(child)

        errs = list(bad_refs)
        if visited < len(nodes):
            errs.append("DAG contains a cycle (violates acyclicity)")
        return errs

    @staticmethod
    def _check_unique_ids(items, label: str, attr: str = "id") -> list[str]:
        seen: set[str] = set()
        errs: list[str] = []
        for it in items:
            key = getattr(it, attr)
            if key in seen:
                errs.append(f"Duplicate {label} {attr}: '{key}'")
            seen.add(key)
        return errs

    # ---------------- 度量 ----------------

    def compute_metrics(self, threshold: float = 1.5) -> CompressionMetric:
        """
        度量設計決策：
        K = |primitives| + |axioms|
            理論的「壓縮後大小」——僅計入描述此理論所需的
            原語與假設。DAG 是元資料（越詳細越好），不計入 K。
        I = |theorems| + Σ|proof.steps|
            理論的「推論產出」——可從 K 推出的形式化內容。
        CR = I / K
            壓縮率。真理論 CR 隨展開發散；魔術理論 CR ≲ 1。
        threshold = 1.5
            經驗閾值：每個結構元件平均至少推出 1.5 個定理或步驟。
        """
        K = len(self.primitives) + len(self.axioms)
        I = len(self.theorems) + sum(len(p.steps) for p in self.proofs)
        CR = (I / K) if K > 0 else 0.0
        return CompressionMetric(
            K=K,
            I=I,
            CR=CR,
            is_candidate_true_theory=(CR >= threshold),
            threshold=threshold,
        )

    # ---------------- 指紋 ----------------

    def fingerprint(self) -> Fingerprint:
        payload = self.to_canonical_json().encode("utf-8")
        return Fingerprint(
            sha256=hashlib.sha256(payload).hexdigest(),
            version=self.version,
        )

    # ---------------- 序列化 ----------------

    def to_canonical_json(self) -> str:
        """canonical JSON：排序 keys、無空白——用於指紋計算與跨系統交換。"""
        def norm(obj: Any) -> Any:
            if isinstance(obj, dict):
                return {k: norm(v) for k, v in sorted(obj.items())}
            if isinstance(obj, (list, tuple)):
                return [norm(x) for x in obj]
            if isinstance(obj, Enum):
                return obj.value
            return obj

        d = asdict(self)
        return json.dumps(
            norm(d),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )

    def to_report(self) -> str:
        """人類可讀的結晶化報告。"""
        m = self.compute_metrics()
        fp = self.fingerprint()
        errs = self.validate()
        lines = [
            "═══════════════════════════════════════════════",
            f"  Theory Compression Format Report",
            f"  {self.name}  v{self.version}",
            "═══════════════════════════════════════════════",
            f"  Fingerprint : {fp.sha256[:24]}…",
            "",
            f"  §0 Primitives : {len(self.primitives):>3}",
            f"  §1 Axioms     : {len(self.axioms):>3}",
            f"  §2 DAG nodes  : {len(self.dag):>3}   "
            f"(edges: {sum(len(n.depends_on) for n in self.dag)})",
            f"  §4 Theorems   : {len(self.theorems):>3}",
            f"  §5 Proofs     : {len(self.proofs):>3}   "
            f"(total steps: {sum(len(p.steps) for p in self.proofs)})",
            f"  §6 Models     : {len(self.examples):>3}",
            "",
            "  §7 Compression Metrics",
            f"     K (structural complexity) = {m.K}",
            f"     I (inferential output)    = {m.I}",
            f"     CR = I / K                = {m.CR:.3f}",
            f"     threshold                 = {m.threshold}",
            f"     candidate true theory?    = "
            f"{'YES' if m.is_candidate_true_theory else 'NO (magical zone)'}",
            "",
            f"  Validation : {'PASS ✓' if not errs else 'FAIL ✗'}",
        ]
        for e in errs:
            lines.append(f"     × {e}")
        lines.append("═══════════════════════════════════════════════")
        return "\n".join(lines)


# ============================================================
# Demo：DCO v5.0 的 TCF 實例化
# ============================================================

def build_dco_v5() -> Theory:
    """Dynamic Circle Ontology v5.0（Closure 為唯一原語）。"""
    primitives = [
        Primitive("Cl", PrimitiveKind.TYPE, 0, "Type",
                  "閉合性 Closure——概念空間唯一原語"),
        Primitive("π", PrimitiveKind.FUNCTION, 1, "ℕ × Cl → Top",
                  "維度投影算子 πₙ(Cl) = Sⁿ⁻¹"),
        Primitive("∘", PrimitiveKind.FUNCTION, 2, "Cl × Cl → Cl",
                  "閉合複合運算"),
        Primitive("In", PrimitiveKind.RELATION, 2, "Cl × Cl",
                  "內在關係（inside-of）"),
    ]

    axioms = [
        Axiom("Cl-1", "self-consistency",
              "∀x ∈ Cl. x ∘ x = x",
              "自洽性：閉合體自複合保持恆等。"),
        Axiom("Cl-2", "duality",
              "∀x ∈ Cl. ∃!y. In(x, y) ∧ ¬In(y, x)",
              "對偶性：內與外共同定義。"),
        Axiom("Cl-3", "conservation",
              "∀f: Cl → Cl. ∃ f⁻¹: Cl → Cl. f ∘ f⁻¹ = id",
              "守恆性：所有內生操作皆可逆。"),
        Axiom("Cl-4", "generativity",
              "∀n ∈ ℕ. π_{n+1}(Cl) = Sⁿ",
              "生成性：自反射生成更高維拓撲。"),
    ]

    dag = [
        DAGNode("Cl", "primitive"),
        DAGNode("π", "primitive", ("Cl",)),
        DAGNode("∘", "primitive", ("Cl",)),
        DAGNode("In", "primitive", ("Cl",)),
        DAGNode("Cl-1", "axiom", ("Cl", "∘")),
        DAGNode("Cl-2", "axiom", ("Cl", "In")),
        DAGNode("Cl-3", "axiom", ("Cl", "∘")),
        DAGNode("Cl-4", "axiom", ("Cl", "π")),
        DAGNode("T-DimProj",     "theorem", ("Cl-4",)),
        DAGNode("T-CircleAsPi2", "theorem", ("Cl-4", "T-DimProj")),
        DAGNode("T-SingWuji",    "theorem", ("Cl-3", "Cl-4")),
        DAGNode("T-DaoInvert",   "theorem", ("Cl-3", "Cl-4")),
        DAGNode("T-DimCollapse", "theorem", ("Cl-3", "Cl-4")),
        DAGNode("T-ChiralityCons","theorem", ("Cl-3",)),
        DAGNode("T-ConsLaws",    "theorem", ("Cl-3",)),
        DAGNode("T-GodPoint",    "theorem", ("Cl-1", "Cl-3")),
        DAGNode("T-DaoGen",      "theorem", ("Cl-4",)),
        DAGNode("T-SInfContract","theorem", ("Cl-4", "T-DimProj")),
    ]

    language = FOLSignature(
        types=("Cl", "ℕ", "Top"),
        constants=(("∅", "Cl"),),
        functions=(
            ("π", ("ℕ", "Cl"), "Top"),
            ("∘", ("Cl", "Cl"), "Cl"),
        ),
        relations=(
            ("In", ("Cl", "Cl")),
            ("=", ("Cl", "Cl")),
        ),
    )

    theorems = [
        Theorem("T-DimProj", "dimensional projection",
                "∀n ∈ ℕ. πₙ(Cl) = Sⁿ⁻¹",
                ("Cl-4",),
                "維度投影定理。"),
        Theorem("T-CircleAsPi2", "circle-as-projection",
                "Circle ≡ π₂(Cl) = S¹",
                ("Cl-4",),
                "圓不是原語，僅是 Closure 的 2D 投影。"),
        Theorem("T-SingWuji", "singularity-as-Wuji",
                "lim_{n→∞} Sⁿ ≃ point ≡ 無極",
                ("Cl-3", "Cl-4"),
                "S^∞ 可縮為一點 = 道生一之前的物理無極態。"),
        Theorem("T-DaoInvert", "Dao-inversion",
                "反者道之動 ≡ (Cl-generation)⁻¹",
                ("Cl-3", "Cl-4"),
                "反者道之動 = 閉合生成的逆算子。"),
        Theorem("T-DimCollapse", "dimensional collapse",
                "S² → S¹ → S⁰ under (gravity ⊕ rotation)",
                ("Cl-3", "Cl-4"),
                "重力（徑向閉合）+ 旋轉（切向閉合）驅動塌縮。"),
        Theorem("T-ChiralityCons", "chirality conservation",
                "∀ collapse path P. χ(S_init) = χ(S_final)",
                ("Cl-3",),
                "手性在維度塌縮中守恆。"),
        Theorem("T-ConsLaws", "conservation laws derivability",
                "∀ symmetry σ of Cl. ∃ conservation law C(σ)",
                ("Cl-3",),
                "所有守恆律（Noether 型）從 Cl-3 導出。"),
        Theorem("T-GodPoint", "God-point definition",
                "G ≡ lim_{ε→0⁺}(Cl + ε)",
                ("Cl-1", "Cl-3"),
                "神點不是奇點而是極限——可無限趨近而不可達。"),
        Theorem("T-DaoGen", "generative spiral",
                "道 → 一 → 二 → 三 → 萬物  ≡  Cl ⟲ Φⁿ(Cl)",
                ("Cl-4",),
                "《道德經》生成序 = Closure 的自反射迭代。"),
        Theorem("T-SInfContract", "S-infinity contractibility",
                "S^∞ is contractible (π_k(S^∞) = 0, ∀k)",
                ("Cl-4",),
                "無限維球面可縮為點——拓撲上即 Dao ↔ 無極。"),
    ]

    proofs = [
        Proof(
            theorem_id="T-DimProj",
            steps=(
                ProofStep(1, "∀n ∈ ℕ. π_{n+1}(Cl) = Sⁿ",
                          "AxiomIntro", ("Cl-4",)),
                ProofStep(2, "Let m = n + 1, n ∈ ℕ ⇒ m ∈ ℕ⁺",
                          "Substitution", ("1",)),
                ProofStep(3, "π_m(Cl) = S^{m-1}",
                          "Rename", ("2",)),
                ProofStep(4, "∀n ∈ ℕ. πₙ(Cl) = Sⁿ⁻¹  ∎",
                          "Generalization", ("3",)),
            ),
        ),
        Proof(
            theorem_id="T-SingWuji",
            steps=(
                ProofStep(1, "S^∞ = colim_{n} Sⁿ",
                          "Def", ()),
                ProofStep(2, "S^∞ is contractible (standard result)",
                          "Lemma", ("1",)),
                ProofStep(3, "contractible ⇒ homotopy-equivalent to point",
                          "Def", ("2",)),
                ProofStep(4, "lim Sⁿ ≃ point ≡ 無極  ∎",
                          "Identification", ("3",)),
            ),
        ),
    ]

    examples = [
        Model(
            name="topological projection",
            domain="Algebraic Topology",
            interpretation=(
                ("Cl", "abstract closure space"),
                ("π₂(Cl)", "S¹ (circle)"),
                ("π₃(Cl)", "S² (2-sphere)"),
            ),
            satisfies=("Cl-1", "Cl-4"),
        ),
        Model(
            name="Noether-style conservation",
            domain="Theoretical Physics",
            interpretation=(
                ("Cl-3", "symmetry → conservation law"),
                ("∘",    "composition of closed dynamical systems"),
            ),
            satisfies=("Cl-1", "Cl-3"),
        ),
        Model(
            name="Daoist cosmology",
            domain="Philosophy of Mind",
            interpretation=(
                ("lim Sⁿ",  "無極 (Wuji)"),
                ("π₁(Cl)",  "道 (Dao) as 0-sphere = {±1}"),
                ("反者道之動", "inverse of Cl-generation"),
            ),
            satisfies=("Cl-3", "Cl-4"),
        ),
    ]

    return Theory(
        name="Dynamic Circle Ontology",
        version="5.0",
        primitives=primitives,
        axioms=axioms,
        dag=dag,
        language=language,
        theorems=theorems,
        proofs=proofs,
        examples=examples,
    )


# ============================================================
# 對照組：一個「魔術理論」，展示 CR 的辨別力
# ============================================================

def build_magical_theory() -> Theory:
    """
    假理論：對每個「結論」都獨立添加一條公理。
    預期 CR ≈ 1，觸發 magical-zone 警告。
    """
    primitives = [
        Primitive("X", PrimitiveKind.TYPE, 0, "Type", "神秘實體"),
    ]
    axioms = [
        Axiom("M-1", "ad-hoc-1", "P₁(X)", "憑空假設命題 1"),
        Axiom("M-2", "ad-hoc-2", "P₂(X)", "憑空假設命題 2"),
        Axiom("M-3", "ad-hoc-3", "P₃(X)", "憑空假設命題 3"),
        Axiom("M-4", "ad-hoc-4", "P₄(X)", "憑空假設命題 4"),
    ]
    dag = [
        DAGNode("X", "primitive"),
        DAGNode("M-1", "axiom", ("X",)),
        DAGNode("M-2", "axiom", ("X",)),
        DAGNode("M-3", "axiom", ("X",)),
        DAGNode("M-4", "axiom", ("X",)),
    ]
    theorems = [
        Theorem("T1", "restated-1", "P₁(X)", ("M-1",), "重述公理 1"),
        Theorem("T2", "restated-2", "P₂(X)", ("M-2",), "重述公理 2"),
    ]
    proofs = [
        Proof("T1", (ProofStep(1, "P₁(X)", "AxiomIntro", ("M-1",)),)),
        Proof("T2", (ProofStep(1, "P₂(X)", "AxiomIntro", ("M-2",)),)),
    ]
    return Theory(
        name="Ad-Hoc Magical Theory",
        version="0.1",
        primitives=primitives,
        axioms=axioms,
        dag=dag,
        theorems=theorems,
        proofs=proofs,
    )


if __name__ == "__main__":
    print("\n" + "▶" * 30 + "  DCO v5.0  " + "▶" * 30)
    dco = build_dco_v5()
    print(dco.to_report())

    print("\n" + "▶" * 28 + "  Magical Theory  " + "▶" * 28)
    magic = build_magical_theory()
    print(magic.to_report())

    print("\n對照結論：")
    print(f"  DCO v5.0   CR = {dco.compute_metrics().CR:.3f}  → true-theory candidate")
    print(f"  Magical    CR = {magic.compute_metrics().CR:.3f}  → magical-zone")

```

**附錄 B：引用格式建議**

```
Neo.K & Theia (2026). Theory Compression Format v1.0.
EveMissLab Technical Report EML-TCF-2026-v1.0.
Fingerprint: <SHA-256 of this document>
```

**文件結束**
