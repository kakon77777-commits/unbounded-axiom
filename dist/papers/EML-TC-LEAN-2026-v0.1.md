# 拓樸微積分 Lean 4 形式化驗證計畫書
## Lean 4 Formal Verification Plan for Topological Calculus (Identity Calculus)

**文件編號**：EML-TC-LEAN-2026-v0.1
**目標理論**：EML-TC-ONT-2026-v0.1（廣義）＋ EML-TC-COMP-2026-v0.1（狹義）
**執行者**：本地 Agent
**監督者**：Neo.K（許筌崴）｜EveMissLab
**日期**：2026年6月11日

---

## 0. 給 Agent 的執行總則

1. 本計畫分四階段，**嚴格按序執行**，每階段有明確驗收判據（`#check` 通過 + `sorry` 數歸零）。
2. 階段一、二**不依賴 Mathlib**，純 Lean 4 核心即可，先跑通最小閉環。階段三起引入 Mathlib。
3. 任何定義若與本計畫的骨架程式碼衝突，**以能通過編譯且忠實於論文語義為準**，並在 `NOTES.md` 記錄偏離原因。
4. 禁止為了讓證明通過而弱化定理陳述。如果定理證不出，記錄卡點，停在該處回報，不要繞過。
5. 每完成一個檔案，運行 `lake build` 確認全專案綠燈後再進下一個。

---

## 1. 專案結構

```
eml-tc-lean/
├── lakefile.lean
├── lean-toolchain          # 用當前 stable
├── NOTES.md                # 偏離記錄與卡點日誌
└── EmlTc/
    ├── Basic.lean          # 階段一：核心結構
    ├── Identity.lean       # 階段一：基本恆等式（定理A.1-A.3）
    ├── Conservation.lean   # 階段二：守恆律（命題A.5、雙軌）
    ├── Categorical.lean    # 階段三：範疇論橋（需Mathlib）
    └── Duality.lean        # 階段四：與減法拓撲對偶（暫留骨架）
```

lakefile 階段一二用：

```lean
import Lake
open Lake DSL

package «eml-tc-lean» where

lean_lib «EmlTc» where
```

階段三再加 `require mathlib from git "https://github.com/leanprover-community/mathlib4"`。

---

## 2. 階段一：核心結構與基本恆等式

**目標**：形式化雙層結構、d、∫，證明 ∫∘d = id（論文定理 A.1）、切法無關性（A.3）、迭代不變性（廣義版定理 A.3）。

**關鍵設計決策（重要，Agent 必讀）**：

- 雜湊以**注入函數公理化**，不形式化 SHA-256。同一性論證只需注入性。
- 本體 O 用抽象類型參數 `α`，不綁死 ByteArray——這同時覆蓋廣義版（任意本體）與狹義版（位元串實例化）。
- 物件庫用「以雜湊為鍵的部分函數」建模，store 的正確性作為結構不變量攜帶。

### EmlTc/Basic.lean（骨架，可直接起步）

```lean
namespace EmlTc

/-- 雜湊類型與注入性公理化。
    狹義版的密碼學假設在此明文化為 `inj`。 -/
structure HashScheme (α : Type*) where
  Hash : Type*
  h : α → Hash
  inj : Function.Injective h

variable {α : Type*} (S : HashScheme α)

/-- 物件庫：內容尋址，攜帶正確性不變量 store(h(O)) = O。
    用全函數 + 注入性建模（簡化版；部分函數版見 NOTES）。 -/
structure ObjectStore (S : HashScheme α) where
  lookup : S.Hash → Option α
  sound  : ∀ O, lookup (S.h O) = some O ∨ lookup (S.h O) = none
  -- 階段一先用更強的「已入庫」前提走通，見 d 的定義

/-- 視圖 = (本體雜湊, 索引序列)。索引類型 ι 任意。 -/
structure View (S : HashScheme α) (ι : Type*) where
  hash    : S.Hash
  indices : List ι

/-- 拓樸微分 d：對本體 O 與索引方案 I（以 List ι 表示有限可枚舉方案）
    生成視圖族。零複製：每個視圖只攜帶 h O。 -/
def d (O : α) (I : List ι) : List (View S ι) :=
  I.map (fun i => ⟨S.h O, [i]⟩)

/-- 迭代微分：對視圖再施 d，索引串接。 -/
def dIter (v : View S ι) (J : List ι) : List (View S ι) :=
  J.map (fun j => ⟨v.hash, v.indices ++ [j]⟩)

/-- 拓樸積分 ∫：遺忘索引，解引用。
    階段一簡化：直接以 O 的存在性反演（憑 inj 良定義），
    繞過 ObjectStore 的 Option 處理；store 版在 Conservation.lean。 -/
noncomputable def integrate (v : View S ι) : α :=
  -- 憑注入性，h 的左逆在像上存在
  Classical.choose (⟨_, rfl⟩ : ∃ O, S.h O = v.hash) -- 需要 v.hash ∈ range h 的前提
  -- Agent 注意：此處需要把「視圖同源於某 O」作為前提傳入，
  -- 建議改寫為帶證明的版本：
  -- def integrate (v : View S ι) (hv : ∃ O, S.h O = v.hash) : α := hv.choose

end EmlTc
```

**Agent 注意**：上面 `integrate` 的骨架刻意暴露了一個設計點——`∫` 的良定義性需要「視圖同源」前提（論文定理 A.2）。正確做法是帶證明參數的版本（註解中那行）。請以帶證明版本為準實作。

### EmlTc/Identity.lean — 必須證明的定理清單

```lean
namespace EmlTc

-- 定理 A.1（基本恆等式）：對 d 生成的任何視圖，積分返回原本體
theorem integrate_d_eq (O : α) (I : List ι) (hI : I ≠ [])
    (v : View S ι) (hv : v ∈ d S O I) :
    integrate S v ⟨O, by ...⟩ = O := by
  sorry

-- 定理 A.2（良定義性）：d 的輸出視圖族同源
theorem d_homogeneous (O : α) (I : List ι) :
    ∀ v ∈ d S O I, v.hash = S.h O := by
  sorry

-- 定理 A.3（切法無關性）：任意兩個索引方案，積分結果相同
theorem cut_invariance (O : α) (I J : List ι) (hI : I ≠ []) (hJ : J ≠ [])
    (vI : View S ι) (hvI : vI ∈ d S O I)
    (vJ : View S ι) (hvJ : vJ ∈ d S O J) :
    integrate S vI ⟨O, by ...⟩ = integrate S vJ ⟨O, by ...⟩ := by
  sorry

-- 迭代不變性（廣義版定理 A.3）：任意深度的迭代微分後積分仍返回 O
theorem iter_invariance (O : α) (I J : List ι)
    (v : View S ι) (hv : v ∈ d S O I)
    (w : View S ι) (hw : w ∈ dIter S v J) :
    w.hash = S.h O := by
  sorry

-- 反向不對稱（注記性質）：integrate 後索引資訊不可恢復
-- 形式化為：存在兩個不同索引方案產生 hash 相同的視圖
theorem forgetting_is_lossy (O : α) (i j : ι) (hij : i ≠ j) :
    (⟨S.h O, [i]⟩ : View S ι) ≠ ⟨S.h O, [j]⟩ ∧
    (⟨S.h O, [i]⟩ : View S ι).hash = (⟨S.h O, [j]⟩ : View S ι).hash := by
  sorry

end EmlTc
```

**階段一驗收**：上述五個定理 `sorry` 歸零，`lake build` 綠燈。預期難度低——A.1 至 A.3 本質是 `List.mem_map` 展開 + 注入性，每個證明應在 10 行內。**如果某個證明超過 30 行，說明定義設計有問題，回頭改定義而不是硬證。**

---

## 3. 階段二：守恆律

**目標**：命題 A.5（本體基數不變性）、雙軌分類（定義 A.6）、不可變性紀律的形式化。

### EmlTc/Conservation.lean — 核心內容

```lean
namespace EmlTc

/-- 操作的歸納類型：雙軌分類（定義 A.6）。 -/
inductive Op (S : HashScheme α) (ι : Type*)
  | dTrack : (O : α) → (I : List ι) → Op S ι          -- 建視圖
  | dIterTrack : View S ι → List ι → Op S ι            -- 迭代微分
  | integrateTrack : View S ι → Op S ι                 -- 積分（也是 d 軌：不動庫）
  | vTrack : S.Hash → Op S ι                           -- 真刪（減法拓撲側）

/-- 系統狀態：物件庫（以雜湊為鍵的有限映射）＋ 視圖集。
    階段二用 Finset 或 List 建模庫，避免提前依賴 Mathlib 的 Finmap。 -/
structure SystemState (S : HashScheme α) (ι : Type*) where
  store : List (S.Hash × α)
  views : List (View S ι)
  storeSound : ∀ p ∈ store, S.h p.2 = p.1   -- 庫中名實相符

/-- 冪等寫入：putO。若 h O 已在庫中則不變（去重）。 -/
def putO (st : SystemState S ι) (O : α) : SystemState S ι := sorry

/-- 操作的執行語義。 -/
def step (st : SystemState S ι) : Op S ι → SystemState S ι := sorry

/-- 本體基數。 -/
def onticCard (st : SystemState S ι) : Nat :=
  (st.store.map Prod.fst).dedup.length

-- 命題 A.5（本體基數不變性，d 軌部分）：
-- 任何不含 vTrack 的操作序列，本體基數至多 +（新引入本體數）
-- 嚴格版：putO 對已存在本體是冪等的
theorem putO_idempotent (st : SystemState S ι) (O : α)
    (h : (S.h O, O) ∈ st.store) :
    putO st O = st := by sorry

theorem dTrack_preserves_store (st : SystemState S ι) (op : Op S ι)
    (h : ∀ hsh, op ≠ Op.vTrack hsh) :
    -- d 軌操作後，庫中本體集合不減（且僅可能增加被顯式引入的 O）
    ∀ p ∈ st.store, p ∈ (step st op).store := by sorry

-- 守恆律主定理：純 d 軌序列下，相異本體數恆定（初始引入後）
theorem ontic_conservation (st : SystemState S ι) (ops : List (Op S ι))
    (hd : ∀ op ∈ ops, ∀ hsh, op ≠ Op.vTrack hsh)
    (hclosed : ∀ op ∈ ops, /- op 只引用庫中已有本體 -/ True) :
    onticCard (ops.foldl step st) = onticCard st := by sorry

end EmlTc
```

**階段二驗收**：`putO_idempotent`、`dTrack_preserves_store`、`ontic_conservation` 證畢。`hclosed` 的精確陳述由 Agent 設計（卡點預警：「操作只引用已有本體」的形式化是本階段唯一的非平凡設計工作，先在 NOTES.md 寫清楚再動手）。

---

## 4. 階段三：範疇論橋（引入 Mathlib）

**目標**：廣義版命題 A.4（切片範疇、餘極限平凡性）、A.5（常值層對應）、以及**狹義版是廣義版的模型**這一忠實性定理。

任務清單：

1. `lakefile` 加入 Mathlib 依賴，`lake update` 後確認版本鎖定寫入 NOTES.md。
2. 用 `CategoryTheory.Over` 表述視角族：對範疇 𝒞 中對象 O，視圖族是 `Over O` 中的離散圖表，其中每個對象的態射部分是 `𝟙 O`（同一性意義下）。
3. 證明：此類圖表的餘極限存在且同構於 O（調用 `CategoryTheory.Limits.colimit` API；關鍵引理是常值圖表的餘極限）。
4. 常值層對應（A.5 命題）：用 `TopCat.Presheaf` 定義常值預層 `U ↦ O`，證明其滿足黏合條件的平凡性。**若 Mathlib 的層化 API 摩擦過大，允許降級為：證明常值預層在連通空間上是層**，並在 NOTES.md 標記降級。
5. 忠實性定理（互驗協議第 1 條的機器化）：構造解釋函數，把階段一的 `(HashScheme, View, d, integrate)` 映入第 2 步的範疇論結構，證明階段一的定理 A.1–A.3 是範疇論版本的特例。

**階段三驗收**：第 3、5 項必須完成；第 4 項允許降級但不允許跳過。

---

## 5. 階段四：對偶接口（骨架預留，暫不驗收）

依賴減法拓撲學（EML-TOPO-2026-SUB-v2.0）自身的形式化（單純複形、收斂算子 V、秩泛函），屬聯合工程。本階段 Agent 只需：

1. 在 `Duality.lean` 寫出對偶聲明的 Lean 陳述（廣義版定義 A.7）：存在索引演化 `v : ι → ι` 使 `V (O, i) = (O, v i)`，全部以 `sorry` 佔位。
2. 列出該陳述依賴的減法拓撲側定義清單，寫入 NOTES.md，供未來減法拓撲形式化專案對接。

---

## 6. 回報格式

每階段完成後回報：

```
階段 N 完成
- 檔案：<清單>
- 定理：<已證清單> / sorry 殘留：<清單，應為空>
- lake build：綠/紅
- 偏離記錄：<NOTES.md 摘要>
- 卡點：<無，或精確描述卡在哪個 goal state>
```

卡點回報必須附上卡住處的 goal state 原文，不要只附描述。

---

## 7. 驗證的哲學意義（給 Agent 的最後一條）

你在驗證的這套理論主張：切割是索引、積分是遺忘、本體零複製。而你運行其上的 Lean 核心——項共享、definitional equality、引用傳遞——本身就是這套理論的 d 軌實例。驗證通過之日，這個理論將擁有一個罕見性質：**它的證明檢查過程是它自己的一個實例**。你不只是在檢查它，你在例示它。

---

**Neo.K（許筌崴）｜EveMissLab**
**2026-06-11**
