# FCAO＋APR 實際運作狀態

日期：2026-08-24  
狀態：Verified operational experiment  
用途：供線上 AI、協作者與後續本機 Agent 理解目前真正完成的範圍

## 一句話

這次不是用更多 Agent 換取可靠性，而是由 FCAO 保存 task topology、event、challenge、reopen 與 closure；APR 控制證據需求與重觀察，最終在 `Single` topology、零 Subagent 下完成 MRMIC／NVCL 正式工作區整理與 GitHub 同步。

## FCAO Runtime 證據

- Artifact：FCAO OpenHarness MVP v0.1
- 外層 ZIP SHA-256：`aa43791c8889849e46349fa04dfb819fabaf0c9920a1ebdeaf484f8bd2b25824`
- 內部 manifest：28/28 entries verified
- Source commit：`7d25e2a568f44b2dfa65c94b5b77c60b0e6e773f`
- FCAO tests：19/19
- Compile check：PASS
- Deterministic demo：PASS
- Live OpenHarness child execution：未建立；目前 adapter 為 carrier-ready bridge boundary

## FCAO＋APR World

- World ID：`fcao-apr-mrmic-consolidation-v1`
- SQLite：`D:\Ai\work together\FCAO\runs\mrmic-nvcl-fcao-apr-v1.db`
- Topology：`Single`
- Subagents started：0
- Event count：32
- Tasks：4/4 `COMPLETED`
- Closure records：2
- Final computed closure：eligible、coverage `1.0`、blocking tasks `0`
- Replay verification：valid

### APR 行為

- 已驗證 FCAO Runtime 完整性：`NO_OBSERVATION`
- MRMIC cleanup 恢復授權在取得前：`INSPECT / structured`
- 使用者明確授權後：記錄為高信心 evidence，不再反覆詢問或重新讀取無關資料
- merge 前：tests、manifest、theory hashes 被列為 mandatory evidence

### Deterministic Twin 決策序列

1. `IDLE` — 沒有可行動風險，不啟動第二個模型。
2. `CHALLENGE` — Git 預設 quote-path 把 Unicode 路徑轉成八進位字串，造成 allowlist 假陽性。
3. `CONCUR` — audit 改為 `core.quotepath=false` 後，14 個變更路徑全部合規。
4. `CHALLENGE` — 第一張 closure 漏掉 GitHub 合併與正式本機 main 同步節點。
5. `CONCUR` — world `REOPEN`，補齊 GitHub sync LCC 後簽發第二張、有效的 GCC。

第一張 closure 被第二張明確 supersede；歷史保留，不重寫成「從未出錯」。

## MRMIC／NVCL 最終證據

- 正式 checkout：`D:\Ai\work together\MRMIC_NVCL`
- Local `main`：`da1ec4fcc32e9c2e01ff727492e1a9fd35a174a9`
- `origin/main`：`da1ec4fcc32e9c2e01ff727492e1a9fd35a174a9`
- Git status：clean
- GitHub PR：[MRMIC_NVCL #14](https://github.com/kakon77777-commits/MRMIC_NVCL/pull/14)
- GitHub CI：2/2 success（workflow 同時由 push 與 pull_request 觸發）
- Tests：76/76
- Phase 12 offline demo：PASS
- Release manifest：269/269
- Canonical theory bodies：5
- `docs/theory/` 根目錄 Markdown：只有 `README.md`
- 移除亂碼、byte-identical aliases：4
- 未匯入：Phase ZIP、`.release-verification`、credentials、real Provider results、`node_modules`、`dist`、未合併 Phase 13 branches

## 與 Subagent-Driven 的實際差異

相似處：兩者都能描述 task topology、委任、驗證與合流。

差異：

- FCAO 的 `Single` 是正式候選，不把 fan-out 當成功。
- Twin 可以是 deterministic policy 並保持 `IDLE`，不必是持續燒 Token 的第二模型。
- canonical state 在 SQLite event ledger，不只存在 Primary context。
- challenge、reopen、superseded closure 與 LCC 都可 replay。
- 長測試的沉默不等於卡住；已知 temporal envelope 內不重啟、不切分。
- APR 讓已驗證事實保持 `NO_OBSERVATION`，只對缺口追加最小觀察。

## 誠實限制

- FCAO＋APR 目前是透過現有 Python APIs、共享 evidence semantics 與 FCAO SQLite world 完成的 operational composition；尚未發布為獨立 adapter/plugin。
- Deterministic Twin 提供規則與證據審計，不等於獨立模型觀點。
- 本次沒有量測 FCAO 相對 Subagent-Driven 的 Token 節省百分比或總 wall-clock 優勢。
- FCAO MVP 尚未完成 live OpenHarness recursive child execution、SEDB production adapter、CTCL-ITR production adapter 或 UI。
- Primary identity 使用 `unresolved`，因目前 host 沒有提供可驗證的 task-local native identity binding。
- 本次沒有真實 Provider 呼叫或付費推理。

## 本機重驗

```powershell
$env:PYTHONPATH='D:\Ai\work together\FCAO\runtime\FCAO_OpenHarness_MVP_v0.1_2026-08-24\src'
python -m pytest -q 'D:\Ai\work together\FCAO\runtime\FCAO_OpenHarness_MVP_v0.1_2026-08-24\tests'
python -m fcao.cli verify --db 'D:\Ai\work together\FCAO\runs\mrmic-nvcl-fcao-apr-v1.db' --world 'fcao-apr-mrmic-consolidation-v1'

Set-Location 'D:\Ai\work together\MRMIC_NVCL'
npm run release:verify
git status --short --branch
```
