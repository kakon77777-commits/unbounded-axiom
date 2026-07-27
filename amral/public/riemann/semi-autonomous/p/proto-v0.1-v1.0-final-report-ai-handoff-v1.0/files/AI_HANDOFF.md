# 後續 AI 研究交接

## 一句話狀態

v0.1–v1.0 已把局部函數工程推進到嚴格的抽象 $58$ 維位置覆蓋，但尚未建立 hypothetical off-axis $\zeta$ zero 到 occupancy cell 的合法條件式介面，也尚未完成顯式公式 admissibility、係數方向與 prime-side cone。

下一節點不要再以「放大 local radius」作主要目標。

## 不可改寫的旗標

```json
{
  "rh_proved": false,
  "rh_disproved": false,
  "actual_zeta_occupancy_family": false,
  "zeta_facing_count_and_tail_coefficients_certified": false,
  "explicit_formula_transfer_certified": false,
  "global_rh_certificate": false,
  "v0_7_abstract_continuous_interval_certificate": true,
  "v1_0_abstract_58_location_cover_certificate": true
}
```

前六個 `false` 與後兩個 `true` 必須同時保留。這正是目前研究狀態，不是矛盾。

## 建議下一節點

`RH-ConditionalOffAxisCell-ZetaTransfer-2026Q3-v1.1`

核心問題：

> 若假設存在偏軸 $\zeta$ 零點，能否不用任何實際偏軸零點表，就把它合法隔離為 source-locked rational occupancy cell，並將該 cell 接到方向正確的顯式公式 operator inequality？

## 執行順序

### 1. Source lock

建立 theorem registry，至少含：

- 零點計數／argument-principle 或 Turing-style 來源；
- multiplicity 與 endpoint convention；
- tail bounds；
- 使用版本的 explicit formula；
- validity ranges；
- 所有 constants 的 exact source；
- source file 或 URL hash。

不允許從摘要文字自行補常數。

### 2. Conditional occupancy

證明一個條件式介面：

$$
\exists\ \rho\ \text{偏軸零點}
\Longrightarrow
\exists\ \text{有理 cell }C
$$

且 $C$ 具有可供 operator transfer 使用的 presence、multiplicity、boundary 與 symmetry data。

零點位置仍是 quantified variable。不要把 v0.7 的 $58$ 個 dual atoms 或 height-$20.4$ prototype 稱為 actual zeros。

### 3. Explicit-formula transfer

對同一個 clamped test-function object 完成：

- analytic admissibility；
- density 與 limit exchange；
- zero/tail convergence；
- 五帶與 tail coefficients 的 legal orientation；
- directed interval bounds；
- prime-side expression。

如果 legally oriented coefficients 使 v0.7 witness 失效，應重做 optimization；不得恢復已知錯誤的 upper-to-lower 轉移。

### 4. Compose one parameterized cell

將 conditional occupancy 與 interval Green family 合成。成功輸出只能是：

- 一個 machine-checkable parameterized conditional cell theorem；或
- 一個 formal robust-failure/no-go record。

單純把 $h$ 從 $1.78\times10^{-6}$ 再放大，不算主 GAP 閉合。

### 5. 才考慮 global scaling

只有前述 cell theorem 成立後，才處理全高度、全偏軸區域、unknown leakage、tail 與 prime-side exhaustion。

## 強制停止規則

- 不在 height-$20.4$ prototype 上尋找 unresolved off-axis target；
- 不把 scalar count 變成 arbitrary operator measure；
- 不把 synthetic occupancy 叫作 zeta presence；
- 不以 sampled grid 取代位置全稱量詞；
- 不把 failed interval enclosure 稱為 point counterexample；
- 不重啟 unguided dictionary/rank/support scaling；
- 不在 support 與 admissibility 未凍結前做大規模 prime enumeration；
- 不把有限函數類失敗寫成全部 admissible functions 的不可能定理；
- 不使用「已接近 RH 證明」等模糊升格。

## 最低接手機器程序

```bash
python3 validate_release.py --require-sources
```

若只取得本 final synthesis ZIP、未取得全部 canonical source archives，則執行：

```bash
python3 validate_release.py
```

接著讀取：

1. `metadata/claim-register.json`；
2. `metadata/gap-ledger.json`；
3. `metadata/failure-correction-map.json`；
4. `metadata/dependency-graph.json`；
5. v0.7、v0.8、v0.9、v1.0 的 `evidence_snapshots/`。

## 每一個新節點必須交付

- `README.md`
- 主研究稿
- `RESULTS.md`
- `TRUST_BOUNDARY.md`
- `REPLAY.md`
- `metadata/research_node.json`
- `metadata/claim_register.json`
- `metadata/gap_ledger.json`
- `metadata/dependency_graph.json`
- `metadata/handoff.json`
- source lineage 與 hashes
- machine-checkable outputs
- release manifest

如果只得到負結果，也要精確標記它淘汰的函數類、量詞範圍與未被淘汰的更大空間。
