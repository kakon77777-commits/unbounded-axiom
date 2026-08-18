---
type: live-paper
status: demo
runtime: dynamic-logic
runtime_schema: "0.1"
---

# Live Judgment Demo

這份 Demo 只展示一件事：

$$
\boxed{
\text{判斷具有歷史。}
}
$$

## Claim

::: aimd-claim {id="weather-claim"}
statement: "Tomorrow afternoon will be rainy."
:::

## Evidence

::: aimd-evidence {id="forecast-a" claim="@weather-claim" direction="support"}
weight: 0.9
verified: true
:::

::: aimd-evidence {id="forecast-b" claim="@weather-claim" direction="support"}
weight: 0.8
verified: true
:::

## Judgment

::: aimd-judgment {id="weather-judge" claim="@weather-claim"}
policy: demo-default
projection: triadic
:::

目前判斷：**{{ weather-judge.state }}**

目前支持度：**{{ weather-judge.support }}**

::: aimd-view {source="@weather-judge.support" renderer="formula"}
S_t
:::

## History

::: aimd-history {claim="@weather-claim"}
mode: timeline
:::

## Expected Replay

事件序列應展示：

$$
\Omega
\rightarrow
\top_p
\rightarrow
\Omega
\rightarrow
\bot_p.
$$

注意：

- $\Omega$ 不是 runtime error；
- $\top_p$ 不是永恆真理；
- replay 不重新呼叫 AI；
- 靜態 PDF 只是一個 snapshot。
