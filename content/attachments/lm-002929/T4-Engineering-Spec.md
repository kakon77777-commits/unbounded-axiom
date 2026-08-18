# T4：Dynamic Logic Visual Renderer
## 讓判斷真正「在畫面上發生」的視覺與互動規格

**版本：** v0.1  
**日期：** 2026-08-16  
**目標：** 把動態邏輯從文字說明轉成可直接觀察的運行介面。

---

# 1. 最核心要求

這個 renderer 不是：

> 把公式加動畫。

它是：

$$
\boxed{
\text{Render actual state transitions}.
}
$$

如果 runtime 沒有新事件，renderer 不應假裝「判斷一直在變」。

---

# 2. 三個主要 View

## Paper View

人類熟悉的線性論文。

## Live Logic View

目前正在運行的：

- claim；
- evidence；
- formula；
- judgment；
- causal relation。

## Replay View

重播歷史：

$$
S_0\rightarrow S_1\rightarrow\cdots\rightarrow S_n.
$$

---

# 3. Paper View

保持：

- 標題；
- 段落；
- 公式；
- 圖表；
- 引文。

Dynamic block 以低干擾方式顯示 current state。

例如：

```text
[Ω 仍在生成]
```

---

# 4. Live Logic View

主要畫面建議：

```text
┌──────────────────────────────────────────┐
│ Claim                                    │
│ H: ...                                   │
├─────────────┬──────────────┬─────────────┤
│ Evidence    │ Judgment     │ Next Action │
│ stream      │ Ω            │ Search ...  │
│             │ 68% support  │             │
├─────────────┴──────────────┴─────────────┤
│ Live Formula / Graph                     │
└──────────────────────────────────────────┘
```

---

# 5. Judgment Badge

狀態：

```text
Ω Generating
✓ Provisionally True
✕ Provisionally False
⚡ Conflicted
⏸ Blocked
! Runtime Error
```

注意：

$$
\boxed{
\mathrm{Error}
}
$$

必須使用與 $\Omega$ 完全不同的視覺語義。

---

# 6. Motion Semantics

動畫只能表示：

$$
\text{real transition}.
$$

例如：

$$
\Omega
\rightarrow
\top_p
$$

發生時：

- badge transition；
- timeline 新 event；
- formula value diff；
- evidence reason highlight。

不得無事件時持續閃爍來假裝「AI 正在思考」。

---

# 7. Heartbeat

可以顯示：

```text
Runtime connected
Last event: 12s ago
```

但 heartbeat 是：

$$
\text{liveness}
$$

不是：

$$
\text{epistemic change}.
$$

兩者必須分離。

---

# 8. Evidence Stream

每筆 evidence：

```text
[+ support] Study A
[- oppose] Study B
[? unresolved] Source C
[× invalidated] Source D
```

點擊可查看：

- 原始來源；
- quote；
- timestamp；
- independence；
- model analysis。

---

# 9. Evidence Independence

如果：

$$
d_1,d_2,d_3
$$

都抄自同一 source：

$$
s,
$$

UI 應把它們群組：

```text
1 independent source
3 derivative reports
```

避免視覺灌水。

---

# 10. Formula Live View

現有：

$$
P(H\mid E_t)=0.68.
$$

新 evidence 後：

$$
P(H\mid E_{t+1})=0.74.
$$

Renderer 應短暫標示：

```text
0.68 → 0.74
```

並能點擊：

> Why changed?

---

# 11. Formula Structure Change

若：

$$
f_t
\rightarrow
f_{t+1},
$$

不能只換畫面。

需要 diff：

```text
- f(E)
+ f(E, O, Γ)
```

以及：

```text
Reason: observer bias added to model
```

---

# 12. Claim Split

若：

$$
H
\rightarrow
H_1,H_2,
$$

視覺上應真正分叉。

不是把 $H$ 原地改名。

這是生成判斷最直觀的展示。

---

# 13. Timeline

```text
t0 Claim created
t1 Evidence A added
t2 Ω → provisional true
t3 Counterevidence B
t4 reopened
t5 hypothesis split
```

每個 event 可定位到：

$$
S_t.
$$

---

# 14. Replay Slider

```text
|----●----------------|
t0                  now
```

拖動：

$$
t_k
$$

時，整個畫面投影：

$$
\operatorname{Render}(S_k).
$$

---

# 15. Replay 不是重新運算

預設 replay 應讀歷史 state/event。

不是拿今天的新模型重新算昨天。

若使用：

```text
Re-evaluate historical state with current model
```

必須明確另開模式。

---

# 16. Compare Mode

可以比較：

$$
J_{\text{2026 model}}(P,t)
$$

與：

$$
J_{\text{2030 model}}(P,t).
$$

這對長期 AI 研究非常重要。

---

# 17. Bayesian Projection

科普模式：

```text
Support        ███████░░░ 68%
Counterpressure████░░░░░░ 31%
Completeness   █████░░░░░ 52%
```

但不要用單一紅綠色判決取代文字。

---

# 18. Color 不應是唯一編碼

Accessibility 要求：

- icon；
- text；
- pattern；
- label；

共同表達狀態。

因使用者可能：

- 色弱；
- dark mode；
- 黑白列印。

---

# 19. Reduced Motion

支援：

```text
prefers-reduced-motion
```

若開啟：

- 不做流動動畫；
- 只做狀態瞬時更新；
- timeline 仍完整。

---

# 20. Formula Accessibility

Live formula 更新時不得讓 screen reader 每幀重讀整頁。

應：

- aria-live localized；
- announce only significant transition；
- 提供 change summary。

---

# 21. 動態不等於 60 FPS

Runtime 是 event-driven。

$$
\boxed{
\text{Dynamic Logic}
\neq
\text{continuous animation loop}.
}
$$

只有 simulation 類 block 才需要固定 tick。

---

# 22. Simulation Mode

若某公式本身描述：

$$
x(t),
$$

則可設定：

```text
tick: 100ms
```

但 tick 是 model time。

要顯示：

```text
Simulation time
Wall-clock time
```

兩者分開。

---

# 23. Causal Graph

節點：

- claim；
- evidence；
- hypothesis；
- outcome。

邊：

```text
supports
opposes
causes
derived_from
invalidates
depends_on
```

---

# 24. 可不可 Overlay

對選中的 action 顯示：

```text
Logical        可
Physical       可
Technical      可
Epistemic      未定
Normative      不可
Authority      不可
Generative     可
```

這會是《可不可論》最好的科普畫面之一。

---

# 25. Dynamic Fixed Point Overlay

顯示：

```text
Content changed: 17 fields
Invariants preserved: 6/6
```

使用者直接看到：

> 內容變了，但某些東西沒變。

---

# 26. Responsibility Ledger View

```text
Action
→ Outcome
→ Harm/Cost
→ Repair
→ Remaining debt
```

避免「論文更新後過去消失」。

---

# 27. Export

Paper View：

```text
PDF snapshot
Static HTML
Snapshot MD
```

Replay View：

```text
JSON event package
Optional video capture
```

但 video 不是 canonical history。

---

# 28. Monitor

需監控：

```text
runtime errors
stale dependencies
unverified source
model mismatch
snapshot lag
```

不能把這些混到 judgment state。

---

# 29. 最小 Demo

Demo 只要一個命題：

$$
H.
$$

初始：

$$
\Omega.
$$

event 1：

支持證據。

event 2：

達到 closure：

$$
\Omega\rightarrow\top_p.
$$

event 3：

重大反證：

$$
\top_p\rightarrow\Omega.
$$

event 4：

重新閉合：

$$
\Omega\rightarrow\bot_p.
$$

使用者可 replay。

---

# 30. 成功標準

如果普通使用者不用先讀 ADL，也能從畫面理解：

> 「喔，原來判斷不是固定標籤，而是一段有原因、有歷史、可以重開的過程。」

則 renderer 達成第一階段目的。

---

# 31. 最終定義

$$
\boxed{
\text{Dynamic Logic Visual Renderer}
=
\text{State Projection}
+
\text{Transition Visualization}
+
\text{Historical Replay}
+
\text{Provenance Access}.
}
$$
