# RH-W-18：GAP 更新與 Batch 01 進度

## 本輪封閉的工作節點

- 統一歷史證書狀態詞彙。
- 建立單一 manifest 與 dependency graph。
- 建立 SHA-256 artifact identity 層。
- 建立 native verifier adapter 層。
- 建立 claim normalization 與 RH claim firewall。
- 建立 hash、語義參數與 claim escalation 的 red-team。
- 公開記錄 W-06 legacy incomplete 與 W-14 supersession。

## 尚未封閉

- W-06 缺失的原始 2×2 prime-active artifact 尚未恢復。
- 後端尚未做到 Lean／Coq 層的 proof object 驗證。
- 歷史 transcendentals 仍依各輪 documented software contract，而不是共同形式化核心。
- schema migration 目前由 adapter 完成，尚未將所有舊 JSON 原地轉換成 canonical payload。

## Batch 01

$$
\boxed{\texttt{RH-W-18}/\texttt{RH-W-20}}
$$

目前完成 $18/20$，剩下兩輪。

下一節點：

$$
\boxed{\texttt{RH-W-19-REPRODUCIBILITY-AND-ADVERSARIAL-AUDIT}}
$$

W-19 將不只測後端本身，而會建立一組可公開的錯誤證書動物園：漏 prime power、錯誤 knot piece、$M/G$ 參數錯配、非 outward interval、浮點假負、尾界截斷與 witness 版本錯配，並要求後端給出可分類的拒絕理由。
