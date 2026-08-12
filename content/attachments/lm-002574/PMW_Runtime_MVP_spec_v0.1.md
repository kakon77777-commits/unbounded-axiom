# PMW Runtime MVP 工程規格 v0.1

## 1. 目標

建立一個單機、可測試的 Persistent Multi-Agent Workspace Runtime，驗證：

$$
\boxed{
Conversation \neq ContinuityCarrier
}
$$

以及：

$$
\boxed{
SharedWorld
+
Wake/Handoff
+
ScopedMemory
+
VersionedState
}
$$

是否足以讓不同 Agent 執行實例持續協作。

---

## 2. 非目標

v0.1 不處理：

- 分散式共識；
- 大規模水平擴展；
- 自動 RL topology controller；
- 自動語義衝突解決；
- 端到端 OAuth；
- 多租戶 production isolation；
- 現象意識／主體性。

---

## 3. 儲存

- SQLite：runtime metadata。
- Filesystem：artifacts。
- JSON：結構化 payload。

---

## 4. 核心表

- `agents`
- `events`
- `shared_state`
- `tasks`
- `memory`
- `wake_events`
- `handoffs`
- `decision_receipts`
- `topology_edges`

---

## 5. 核心 invariant

### I1 State CAS

所有 shared state update 使用 expected version。

### I2 Wake Idempotency

同一 idempotency key 只能建立一個 wake。

### I3 Scope Preservation

PRIVATE memory 不可被其他 Agent retrieve。

### I4 Authority Separation

message / memory / handoff 不自動傳遞 effect permission。

### I5 Append Events

Event Log 不 in-place 改歷史事件。

### I6 Explicit Receipt

重要 wake 必須留下 ACK / NO_ACTION / ACTION / ERROR receipt。

---

## 6. Runtime 狀態

```text
SLEEPING
WAKING
OBSERVING
ACTING
WAITING
BLOCKED
TERMINATED
```

---

## 7. 最小協作算子

```text
ISOLATE
SHARE
JOIN
HANDOFF
```

---

## 8. API

```python
register_agent()
append_event()
get_state()
compare_and_set_state()
create_task()
store_memory()
list_memories()
enqueue_wake()
claim_wake()
ack_wake()
create_handoff()
write_receipt()
set_topology_edge()
get_topology()
```

---

## 9. Smoke Test

1. 建 Agent A、B。
2. 建 Task T1。
3. A 寫 shared state `phase=research` v1。
4. A 寫 private memory。
5. B 無法讀 A private memory。
6. A 建 handoff 給 B。
7. B 依 task/shared state 接手。
8. 重複送同一 wake idempotency key，不得新增第二個 wake。
9. A 以舊版 state CAS 更新時必須失敗。
10. 寫 Decision Receipt。
11. 驗證 event history 可追溯。

---

## 10. v0.2

- Room lifecycle。
- shared-memory candidate / promotion。
- conflict object。
- artifact registry。
- snapshot / restore。

## 11. v0.3

- REST API。
- MCP adapter。
- event stream。
- role / permission matrix。

## 12. v0.4

- rule-based ACTC。
- Isolate/Share/Join transition。
- hysteresis / dwell time。

## 13. v1.0

- production auth。
- durable remote queues。
- conflict policies。
- observability dashboard。
- benchmark suite。
