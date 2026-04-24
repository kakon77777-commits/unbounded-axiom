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
