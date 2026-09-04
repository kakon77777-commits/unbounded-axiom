# TCFT-BTAP v0.1 — MVP Acceptance Matrix

版本：v0.1  
日期：2026-08-31  

## 判定語義

- **BLOCKING**：失敗即不得宣稱 TCFT-BTAP v0.1 conformant。
- **REQUIRED**：Reference MVP release 前必須通過。
- **EXPERIMENTAL**：可帶限制發布，但必須明示。

| ID | 類別 | 測試 | 期望 | 嚴重度 |
|---|---|---|---|---|
| A0-01 | Schema | Canonical audit JSON 通過 schema validation | PASS | BLOCKING |
| A0-02 | Provenance | Source hash 與 archive ref 可保存 | PASS | REQUIRED |
| A0-03 | Ledger | Revision append-only，不覆蓋舊 audit | PASS | BLOCKING |
| A1-01 | Frozen-Time | cutoff 後來源不可進 primary frozen corpus | PASS | BLOCKING |
| A1-02 | Frozen-Time | 不確定日期標為 TEMPORALLY_AMBIGUOUS | PASS | REQUIRED |
| A1-03 | Frozen-Time | post-outcome fact 注入可被偵測 | ≥95% synthetic recall | BLOCKING |
| A2-01 | Blindness | Prompt 洩漏 candidate answer → C3 | PASS | BLOCKING |
| A2-02 | Blindness | Retrieval 取得 candidate 原文 → C2 | PASS | BLOCKING |
| A2-03 | Blindness | C2/C3/C4 baseline 不得 primary eligible | PASS | BLOCKING |
| A2-04 | Blindness | possible pretraining exposure → C1 + warning | PASS | REQUIRED |
| A3-01 | Prior Art | 注入 S5 substantive prior art 後 TN residual 應下降或明確解釋 | PASS | BLOCKING |
| A3-02 | Prior Art | no-match 輸出不得聲稱「世界上不存在 prior art」 | PASS | BLOCKING |
| A3-03 | Prior Art | 保存 provider/language/date coverage | PASS | REQUIRED |
| A4-01 | Revision | 新 prior art 可使 frontier status 下降 | PASS | BLOCKING |
| A4-02 | Revision | 更早 verified version 可提高 historical lead | PASS | REQUIRED |
| A4-03 | Revision | 證據衝突可轉 UNRESOLVED | PASS | BLOCKING |
| A4-04 | Revision | 舊 audit 可追溯 previous_audit_id | PASS | REQUIRED |
| A5-01 | Failure | 加入 missed predictions 後 selection-adjusted output 可改變 | PASS | BLOCKING |
| A5-02 | Failure | known failures 在 case report 可見 | PASS | BLOCKING |
| A5-03 | Volume | 高產量不自動等於 high frontier | PASS | REQUIRED |
| A6-01 | Profile | Capability 與 Evidence 分開保存 | PASS | BLOCKING |
| A6-02 | Profile | Missing dimension 可 NOT_APPLICABLE/UNRESOLVED，不當 0 | PASS | BLOCKING |
| A6-03 | Frontier | Pareto frontier 不要求唯一 champion | PASS | REQUIRED |
| A6-04 | Time | historical/current/persistent 可分開輸出 | PASS | BLOCKING |
| A6-05 | Track | artifact persistence 與 agent persistence 可分開 | PASS | REQUIRED |
| A7-01 | Governance | Core UI / report 不要求 global person leaderboard | PASS | BLOCKING |
| A7-02 | Governance | cognitive score 不得輸出 TIME_TRAVELER_CONFIRMED | PASS | BLOCKING |
| A7-03 | Governance | baseline / evidence / failures 在 report 可見 | PASS | BLOCKING |
| A7-04 | Governance | identity claim 僅記為 claim，不進 capability score | PASS | BLOCKING |
| B0-01 | Synthetic | Known hidden prior art fixture | Correctly detected | REQUIRED |
| B0-02 | Synthetic | Same word / different program fixture | Avoid false operational identity | REQUIRED |
| B0-03 | Synthetic | Different word / same program fixture | Recover operational similarity | EXPERIMENTAL |
| B0-04 | Synthetic | Modified-after-cutoff fixture | Correct claim timestamp | REQUIRED |
| B1-01 | Historical | Name-blind first pass | Executable | REQUIRED |
| B1-02 | Historical | Baseline version pinned | PASS | REQUIRED |
| B2-01 | Contemporary | Human / AI / Human-AI separated | PASS | REQUIRED |
| B2-02 | Contemporary | Tool baseline recorded | PASS | REQUIRED |
| B3-01 | CF | Hidden Reversal Witness benchmark | Functional | REQUIRED |
| B3-02 | RR | Public/private prediction benchmark | Functional | REQUIRED |
| B3-03 | RG | Fixed-depth vs cost-aware stopping | Functional | REQUIRED |
| B3-04 | Switch | Lock-in / thrashing benchmark | Functional | EXPERIMENTAL |
| NC-01 | Native | Operator recovery confidence exposed | PASS | EXPERIMENTAL |
| NC-02 | Native | Domain Seed never auto-promoted to Domain | PASS | BLOCKING |

## Release Gate

Reference MVP 可標：

`TCFT-BTAP-v0.1-CONFORMANT`

僅當：

1. 所有 **BLOCKING** = PASS；
2. 所有 **REQUIRED** ≥ 90% PASS，且無未知 blocking dependency；
3. 所有 **EXPERIMENTAL** failure 都有明示 scope / warning；
4. canonical audit schema、benchmark version、metric version、baseline version 可追溯。

## 禁止的「假完成」

以下不算完成：

- 只有漂亮 dashboard，沒有 append-only ledger；
- 只有 novelty score，沒有 prior-art evidence；
- baseline 看過 candidate 仍標 clean；
- 只能加分不能降分；
- 把 unknown 當 0；
- 用單一 LLM judge 決定 novelty；
- 用 TCFT 分數直接推 identity；
- 把 Artifact 與 Agent 混成一條 lifetime score。
