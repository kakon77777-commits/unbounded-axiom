# 當差分忘記出身

### 質數 Gilbreath 三角的 mod-$m$ 殘差轉移，與一個模數無關性閾值

**一篇教學向短札（expository note, math.HO）**

作者：Neo.K  
版本：草稿 v0.1　·　分類：math.HO（History and Overview）／math.NT

---

> **聲明（請先讀）。** 本文**不主張任何新定理**。文中三個數學事實——Gilbreath 邊緣恆一、Odlyzko 的 $\{0,2\}$ 飽和機制、Lemke Oliver–Soundararajan 的二階偏差——**全部屬於被引用的原作者**。本文唯一做的事，是把這三塊現成的磚按在同一張桌上，用一個初等的視角（殘差轉移矩陣沿三角下降）觀察它們的接縫，並指出一個容易陳述、容易復現的小現象。所有啟發歸於他人；若本札有任何用處，那用處也只是「整理」，不是「發現」。

---

## 摘要

設 $p_1=2,p_2=3,\dots$ 為質數列。對其反覆取相鄰絕對差，得到 Gilbreath 差分三角。本文把每一列的元素按 $\bmod\,m$ 取殘差，建立該列的**整數值殘差轉移計數矩陣** $T_k^{(m)}$，並追蹤它沿三角下降時的變化。觀察到的現象可以一句話說完：

> 第 $1$ 列（質數間隙）攜帶**與 $m$ 有關、且質數專屬**的二階結構；而一旦某列被 Odlyzko 機制飽和進字母表 $\{0,1,2\}$，它的轉移矩陣對**所有 $m\ge 3$ 完全相同**，僅在 $m=2$ 時退化。$m$-依賴性消失的深度，恰好就是這一列「忘記自己曾是質數」的深度。

整個構造停留在整數環內，沒有小數點；小數點只在兩個明確的接縫出現——正規化與取極限——文末對此作一認識論附記。

---

## 1. 引言：平均的規律，逐點的混沌

質數在**平均**意義上極其規律：質數定理給出密度 $\sim 1/\ln x$，黎曼假設不過是在問這條平滑曲線的誤差項能壓多小。但在**逐點**意義上，質數近乎混沌：相鄰間隙可以任意大（$n!+2,\dots,n!+n$ 是連續 $n-1$ 個合數），卻又被猜測存在無窮多對僅差 $2$ 的孿生質數。

1958 年，N. L. Gilbreath 在一個關於這種「逐點結構」的玩法裡注意到一個頑強的圖樣 [Guy1994]。把質數列反覆做相鄰絕對差：

$$
\begin{aligned}
R_0:&\quad 2,\;3,\;5,\;7,\;11,\;13,\;17,\;19,\;23,\dots\\
R_1:&\quad 1,\;2,\;2,\;4,\;2,\;4,\;2,\;4,\dots\\
R_2:&\quad 1,\;0,\;2,\;2,\;2,\;2,\;2,\dots\\
R_3:&\quad 1,\;2,\;0,\;0,\;0,\;0,\dots\\
&\quad\vdots
\end{aligned}
$$

形式地，$R_0=(p_n)_{n\ge1}$，且 $R_{k+1}(i)=\bigl|R_k(i+1)-R_k(i)\bigr|$。**Gilbreath 猜想**斷言：除第 $0$ 列外，每一列最左邊那一項恆為 $1$（OEIS **A036262** 收錄此三角 [OEIS-A036262]）。

這個圖樣其實更早被 F. Proth 在 1878 年觀察到 [Proth1878]；多數文獻稱 Proth 自稱有證明而證明有誤，但 Chase 考證認為並無證據顯示 Proth 發表過任何（即使錯誤的）證明 [Chase2020]。猜想至今**仍是開放問題**，只有不斷推進的數值驗證：Killgrove 與 Ralston 1959 年驗到前 $63{,}419$ 列 [KR1959]；Odlyzko 1993 年推進到質數 $\le 10^{13}$，需 $G(\pi(10^{13}))=635$ 列即達飽和 [Odlyzko1993]。此紀錄於 2025 年被打破：J.-F. Colonna（2025/10/05）與 S. Plouffe（2025/10/07）各自以不同方法獨立驗到 $10^{14}$，皆得 $G(\pi(10^{14}))=693$ [Plouffe2025][Colonna2026]；Colonna 隨後（與 J.-P. Delahaye 合作）於 2026 年初推進到 $10^{15}$（$G=800$），並驗證至 $1.5\times10^{15}$（2026/03/18）[Colonna2026]。猜想仍未獲證。

本文不碰猜想本身。我們只問一個更小、更可玩的問題：**如果用 $\bmod\,m$ 的眼睛去看這座三角，會看見什麼？**

---

## 2. 三塊現成的磚

下面三節的內容**全部是已知結果**，逐一註明原作者。本文後續的視角完全建立在它們之上。

### 2.1 邊緣恆一（Gilbreath / Proth）

如上所述：每一列首項恆為 $1$。一個基本卻關鍵的初等事實是，由於 $2$ 是唯一的偶質數，$R_1$ 之後每一列的首項必為**奇數**——這是因為「奇數－偶數＝奇數、偶數－奇數＝奇數」沿左緣傳遞 [t5k-Gilbreath]。**但要強調：奇 $\ne 1$。** 首項為奇只是必要條件，遠不足以推出首項為 $1$；任何僅憑奇偶性「證明」邊緣為 $1$ 的論證都是不成立的。真正的機制見 §2.2。

Croft 進一步猜測（經 Gardner 1980 傳播）：此性質不限於質數，凡「以 $2$ 開頭、其後為間隙又小又隨機的遞增奇數列」皆應成立 [Gardner1980]。Chase 2020 的隨機類比把這個直覺做成了定理 [Chase2020]。換言之，邊緣恆一很可能**不依賴質數的深層算術，只依賴間隙的統計溫順**。

### 2.2 $\{0,2\}$ 飽和機制（Odlyzko 1993）

Odlyzko 驗證猜想的方法本身揭示了真正的機制 [Odlyzko1993]：往下降幾列之後，每一列迅速呈現「一個 $1$，後面只剩 $0$ 與 $2$」的形態。關鍵在於字母表 $\{0,2\}$ 在絕對差下**封閉**：

$$
|0-0|=0,\quad |2-0|=2,\quad |2-2|=0,
$$

而「首項 $1$ 後面接 $0$ 或 $2$」永遠再生出 $1$（$|0-1|=|2-1|=1$）。因此一旦某列達到「$1+$ 全 $\{0,2\}$」的形態，往下所有列的首項就被鎖死為 $1$。Odlyzko 正是驗到第 $635$ 列以 $1$ 開頭、其後在足夠長範圍內只有 $0$ 與 $2$，從而推出後續所有列皆以 $1$ 起始。

每一列從左數到「第一個大於 $2$ 的項」之前有多少項，由 OEIS **A000232**（$3,8,14,14,25,23,22,25,\dots$）量度 [OEIS-A000232]；它刻畫了 $\{0,2\}$ 飽和從左邊推進的速度。

一個與本文更貼近的量是 $G(\pi(x))$：使「第 $G$ 列起以 $1$ 開頭、其後僅有 $0$ 與 $2$」成立所需的列深。它正是 Odlyzko、Plouffe、Colonna 在大規模驗證中追蹤的數——$G(\pi(10^{13}))=635$、$G(\pi(10^{14}))=693$、$G(\pi(10^{15}))=800$ [Odlyzko1993][Plouffe2025][Colonna2026]。下文 §4 的閾值深度正與此量同源。

### 2.3 二階分布偏差（Lemke Oliver–Soundararajan 2016）

對固定模 $q$，質數在各個互質剩餘類中是**均勻**分布的（Dirichlet）——這是「一階」或「邊際」規律。Lemke Oliver 與 Soundararajan 2016 年發現，**相鄰**質數的剩餘類**聯合**分布卻出人意料地不均勻：質數傾向於「避免重複」自己的剩餘 [LOS2016]。以個位數（$\bmod 10$）為例，若一質數以 $1$ 結尾，下一個質數以 $1$ 結尾的機率約 $18\%$，以 $3$ 約 $30\%$、以 $7$ 約 $30\%$、以 $9$ 約 $22\%$——而非天真期望的各 $25\%$ [LOS2016]。他們基於 Hardy–Littlewood 猜想給出一個帶大型二階項的啟發式模型，與數據吻合極佳。

這是「二階 $\bmod$ 規律」最清楚的範例：**規律不在一階（一階均勻得像白噪音），規律藏在二階的轉移結構裡。**

---

## 3. 一個視角：沿三角下降的殘差轉移算子

把 §2.3 的「相鄰剩餘聯合分布」這個算子，不只施加在第 $0$ 列（質數本身），而是施加在**每一列**上。對第 $k$ 列 $R_k$ 與模 $m$，定義整數值矩陣

$$
T_k^{(m)}[a][b]\;=\;\#\bigl\{\,i:\;R_k(i)\equiv a,\;R_k(i+1)\equiv b \pmod m\,\bigr\},
\qquad a,b\in\{0,\dots,m-1\}.
$$

$T_k^{(m)}$ 是純整數計數矩陣（這一點在 §5 很重要）。$T_0^{(m)}$ 正是 Lemke Oliver–Soundararajan 研究的對象。本文的全部內容，就是看 $T_k^{(m)}$ 隨 $k$ 增大如何演化。

下表是 $m=3$、質數 $<5000$（$669$ 個質數、$669$ 列）時，$T_k^{(3)}$ 在幾個深度的快照（行列順序為剩餘 $0,1,2$）：

| 列 $k$ | 列長 | $T_k^{(3)}$ |
|---|---|---|
| $1$ | $668$ | $\begin{smallmatrix}74&79&83\\83&0&132\\80&135&1\end{smallmatrix}$ |
| $30$ | $639$ | $\begin{smallmatrix}149&0&171\\1&0&0\\170&0&147\end{smallmatrix}$ |
| $100$ | $569$ | $\begin{smallmatrix}124&0&145\\0&0&1\\145&0&153\end{smallmatrix}$ |
| $600$ | $69$ | $\begin{smallmatrix}20&0&16\\1&0&0\\16&0&15\end{smallmatrix}$ |

讀法：第 $1$ 列三類俱在、結構豐富（質數指紋）；越往下，與剩餘 $1$ 有關的整行整列塌成零，只剩一個游離的 $1$——那正是 Gilbreath 的左邊緣本人——主體則沉進 $\{0,2\}$ 構成的 $2\times2$ 塊。

---

## 4. 觀察：模數無關性閾值

把上表的現象說成一句可陳述的話。記某列 $R_k$ **已飽和**，意指 $R_k$ 的所有項都落在 $\{0,1,2\}$（除最多有限例外）——這正是 §2.2 Odlyzko 機制描述的形態。

**觀察。** 對已飽和的列 $R_k$：

1. **$m=2$ 是特殊的。** 此時 $|a-b|\equiv a+b\pmod 2$，整座三角 $\bmod 2$ 是一台異或（XOR）元胞自動機；字母 $0$ 與 $2$ 被合併為「偶」，字母表塌成 $\{0,1\}$，左邊緣恆 $1$ 是該自動機的不動點。

2. **所有 $m\ge 3$ 給出同一個矩陣。** 因為 $0,1,2$ 在任何 $m\ge 3$ 下都是三個**不同**的剩餘類，取 $\bmod\,m$ 對一個已落在 $\{0,1,2\}$ 的列**毫無作用**。於是
$$
T_k^{(m)}=T_k^{(m')}\quad\text{對一切 } m,m'\ge 3,\ \text{只要 } R_k \text{ 已飽和。}
$$
此共同矩陣的非零結構僅由 $\{0,2\}$ 上的 $2\times2$ 塊，加上邊緣貢獻的孤立 $1$ 構成。

**推論（語意層面）。** $T_k^{(m)}$ 對 $m$ 的依賴性，正是「這一列還記得自己源於質數」的度量：淺層列裡 $T_k^{(m)}$ 隨 $m$ 變動、編碼質數間隙的算術（$k=1$ 即 Lemke Oliver–Soundararajan）；一旦飽和，依賴性蒸發，剩下的只是與質數無關的 $\{0,1,2\}$ 小字母動力學。存在一個**閾值深度** $d^*(N)$，在其下方 $m$-依賴性消失。由 §2.2，$d^*(N)$ 受控於 $\{0,2\}$ 飽和速度——其全域上界正是被 Odlyzko–Plouffe–Colonna 釘出的 $G(\pi(N))$（$635,693,800,\dots$）：使整列達「$1+\{0,2\}$」所需的列深 [Odlyzko1993][Plouffe2025][Colonna2026]。

**誠實的限定。** 「飽和列 $\subset\{0,1,2\}$」這一前提，正處於 Gilbreath/Odlyzko 「已大量數值驗證、但未獲證明」的範圍內。因此「$d^*(N)$ 對一切 $N$ 存在」這件事，其開放程度與 Gilbreath 猜想本身**等價**。本文只主張：**在飽和成立的範圍內**，上述模數無關性是 $\bmod$ 運算的初等後果，並提供一個清楚的復現對象。這不是定理，是一個整理過的觀察。

---

## 5. 認識論附記：小數點的位置

以上每一個對象都是整數：三角是整數，殘差是整數，$T_k^{(m)}$ 是整數計數矩陣。「質數避免重複殘差」這個二階規律，可以**完全不用小數點**陳述——上表 $T_1^{(3)}$ 中 $135>0$、$132>0$ 而對角的 $0$ 與 $1$ 極小，兩個整數一比即見偏差。

小數點只在兩個明確的接縫出現：

- **正規化。** 把計數除以總數去問「佔幾成」，$41.8\%$ 才冒出來。但這是顯示選擇——真值是精確有理數（如 $16394/39231$）。小數是為了和「均勻」這把尺對齊而手動製造的；不除，它就不在。
- **取極限。** 一階邊際密度是乾淨有理數 $1/\varphi(m)$；真正逼出實數（甚至涉及解析常數）的，只有 Lemke Oliver–Soundararajan 那個「隨 $x\to\infty$ 緩慢趨零的二階項」[LOS2016]。

換言之，離散側全程整數、精確；小數點是「有限離散 → 無限連續」這道接縫的感測器，而這道接縫在本構造裡**位置完全確定**——它就在計數被除開、或被推向無窮的那一刻。其餘地方乾淨得像沒人來過。

---

## 6. 代碼

> 以下程式可復現 §3 的下降表與 §4 的觀察（含 $m=2$ 的退化與 $m\ge3$ 的重合）。讀者可自行調整模數與質數上界。**（代碼區，作者後補。）**

```JavaScript

# ── 代碼區（待貼上）──────────────────────────────────────────
import React, { useEffect, useMemo, useRef, useState } from "react";

// ─────────────────────────────────────────────────────────────────────────────
//  GILBREATH ⋈ MOD-m  —  二階MOD規律觀測台
//  整數精確：三角全為整數，殘差全為整數，轉移計數全為整數。
//  小數點只在你按下「正規化」時出現。
// ─────────────────────────────────────────────────────────────────────────────

const INK = "#0a0b0f";
const PANEL = "#11131a";
const LINE = "#22262f";
const PAPER = "#e9e3d3";
const MUTE = "#8a8d97";
const ONE = "#ffb454"; // 殘差 1 = Gilbreath 邊緣
const COOL = "#3aa6b9";

function sieve(n) {
  const s = new Uint8Array(n + 1);
  const ps = [];
  for (let i = 2; i <= n; i++) {
    if (!s[i]) {
      ps.push(i);
      for (let j = i * i; j <= n; j += i) s[j] = 1;
    }
  }
  return ps;
}

function buildTriangle(primes) {
  const tri = [Int32Array.from(primes)];
  let cur = tri[0];
  while (cur.length > 1) {
    const nxt = new Int32Array(cur.length - 1);
    for (let i = 1; i < cur.length; i++) nxt[i - 1] = Math.abs(cur[i] - cur[i - 1]);
    tri.push(nxt);
    cur = nxt;
  }
  return tri;
}

function resColor(r, m) {
  if (r === 1) return ONE;
  if (r === 0) return "#191f2b";
  const t = (r - 1) / Math.max(1, m - 1);
  const hue = 195 - 30 * t;
  const light = 28 + 34 * t;
  return `hsl(${hue} 42% ${light}%)`;
}

export default function App() {
  const [bound, setBound] = useState(2000);
  const [m, setM] = useState(3);
  const [row, setRow] = useState(1);
  const [norm, setNorm] = useState(false);
  const [playing, setPlaying] = useState(false);
  const canvasRef = useRef(null);

  const primes = useMemo(() => sieve(bound), [bound]);
  const tri = useMemo(() => buildTriangle(primes), [primes]);
  const maxRow = tri.length - 1;

  useEffect(() => { if (row > maxRow) setRow(Math.max(1, maxRow)); }, [maxRow, row]);

  // ── auto-descend ──
  useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => {
      setRow((r) => {
        if (r >= maxRow) { setPlaying(false); return r; }
        return r + 1;
      });
    }, 90);
    return () => clearInterval(id);
  }, [playing, maxRow]);

  // ── draw residue triangle ──
  useEffect(() => {
    const cv = canvasRef.current;
    if (!cv) return;
    const N = tri[0].length;
    const cs = Math.max(1, Math.floor(560 / N));
    const W = N * cs, H = tri.length * cs;
    cv.width = W; cv.height = H;
    const ctx = cv.getContext("2d");
    ctx.fillStyle = INK; ctx.fillRect(0, 0, W, H);
    for (let r = 0; r < tri.length; r++) {
      const arr = tri[r];
      for (let c = 0; c < arr.length; c++) {
        ctx.fillStyle = resColor(arr[c] % m, m);
        ctx.fillRect(c * cs, r * cs, cs, cs);
      }
    }
    // mark current row
    ctx.strokeStyle = "rgba(255,180,84,0.9)";
    ctx.lineWidth = Math.max(1, cs);
    ctx.beginPath();
    ctx.moveTo(0, row * cs + cs / 2);
    ctx.lineTo(tri[row].length * cs, row * cs + cs / 2);
    ctx.stroke();
  }, [tri, m, row]);

  // ── transition matrix + histogram of selected row, mod m ──
  const { T, total, hist, ones, edge } = useMemo(() => {
    const arr = tri[row] || new Int32Array();
    const T = Array.from({ length: m }, () => new Array(m).fill(0));
    const hist = new Array(m).fill(0);
    for (let i = 0; i < arr.length; i++) hist[arr[i] % m]++;
    let tot = 0;
    for (let i = 1; i < arr.length; i++) { T[arr[i - 1] % m][arr[i] % m]++; tot++; }
    return { T, total: tot, hist, ones: hist[1] || 0, edge: arr.length ? arr[0] : "-" };
  }, [tri, row, m]);

  const maxHist = Math.max(1, ...hist);

  const fmt = (x) => {
    if (!norm) return x;
    if (total === 0) return "0";
    return ((100 * x) / total).toFixed(1) + "%";
  };
  const cellMax = Math.max(1, ...T.flat());

  return (
    <div style={{ background: INK, color: PAPER, minHeight: "100%", padding: "22px 20px 40px",
      fontFamily: "'Spectral', Georgia, serif" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Spectral:wght@300;400;600&family=JetBrains+Mono:wght@400;600&display=swap');
        * { box-sizing: border-box; }
        .mono { font-family: 'JetBrains Mono', monospace; }
        .disp { font-family: 'Fraunces', serif; }
        input[type=range]{ -webkit-appearance:none; appearance:none; height:3px; background:${LINE}; border-radius:2px; outline:none; }
        input[type=range]::-webkit-slider-thumb{ -webkit-appearance:none; width:15px; height:15px; border-radius:50%; background:${ONE}; cursor:pointer; box-shadow:0 0 0 4px rgba(255,180,84,0.15); }
        input[type=range]::-moz-range-thumb{ width:15px;height:15px;border:none;border-radius:50%;background:${ONE};cursor:pointer; }
        .chip{ cursor:pointer; user-select:none; transition:all .12s; }
        .chip:hover{ border-color:${ONE}!important; color:${PAPER}!important; }
        @keyframes glow { 0%,100%{opacity:.55} 50%{opacity:1} }
      `}</style>

      <div style={{ maxWidth: 1080, margin: "0 auto" }}>
        {/* header */}
        <div style={{ display: "flex", alignItems: "baseline", gap: 14, flexWrap: "wrap", marginBottom: 4 }}>
          <h1 className="disp" style={{ margin: 0, fontSize: 30, fontWeight: 600, letterSpacing: "-0.01em" }}>
            Gilbreath <span style={{ color: COOL }}>⋈</span> mod-<span style={{ color: ONE }}>{m}</span>
          </h1>
          <span className="mono" style={{ fontSize: 12, color: MUTE }}>二階MOD規律觀測台</span>
        </div>
        <p style={{ margin: "0 0 20px", color: MUTE, fontSize: 14, maxWidth: 760, lineHeight: 1.5 }}>
          每個格子是質數絕對差三角的一項，依 <span style={{ color: PAPER }}>殘差 mod {m}</span> 著色。
          <span style={{ color: ONE }}> 琥珀色 = 殘差 1</span>（Gilbreath 邊緣）。往下拉行游標，看 1 如何退成左邊一條孤線、主體塌進 {"{0,2}"} 的冷色塊。全程整數。
        </p>

        {/* controls */}
        <div style={{ display: "flex", gap: 18, flexWrap: "wrap", alignItems: "center", marginBottom: 18,
          padding: "12px 14px", background: PANEL, border: `1px solid ${LINE}`, borderRadius: 10 }}>
          <Ctl label="模數 m">
            <div style={{ display: "flex", gap: 5 }}>
              {[2, 3, 4, 5, 6, 7, 9].map((v) => (
                <span key={v} className="chip mono" onClick={() => setM(v)}
                  style={{ padding: "3px 9px", fontSize: 13, borderRadius: 6,
                    border: `1px solid ${m === v ? ONE : LINE}`,
                    color: m === v ? INK : MUTE, background: m === v ? ONE : "transparent", fontWeight: 600 }}>
                  {v}
                </span>
              ))}
            </div>
          </Ctl>
          <Ctl label="質數上界">
            <div style={{ display: "flex", gap: 5 }}>
              {[1000, 2000, 5000, 10000].map((v) => (
                <span key={v} className="chip mono" onClick={() => setBound(v)}
                  style={{ padding: "3px 9px", fontSize: 13, borderRadius: 6,
                    border: `1px solid ${bound === v ? COOL : LINE}`,
                    color: bound === v ? INK : MUTE, background: bound === v ? COOL : "transparent", fontWeight: 600 }}>
                  {v >= 1000 ? v / 1000 + "k" : v}
                </span>
              ))}
            </div>
          </Ctl>
          <div className="mono" style={{ fontSize: 12, color: MUTE }}>
            {primes.length} 個質數 · {tri.length} 列
          </div>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "minmax(0,1.15fr) minmax(0,1fr)", gap: 20, alignItems: "start" }}>
          {/* triangle */}
          <div style={{ background: PANEL, border: `1px solid ${LINE}`, borderRadius: 10, padding: 12 }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
              <span className="mono" style={{ fontSize: 12, color: MUTE }}>殘差三角 (mod {m})</span>
              <span className="mono" style={{ fontSize: 12, color: ONE }}>← 邊緣恆 1</span>
            </div>
            <div style={{ overflow: "hidden", borderRadius: 4, lineHeight: 0 }}>
              <canvas ref={canvasRef} style={{ width: "100%", height: "auto", imageRendering: "pixelated", display: "block" }} />
            </div>
            <div style={{ marginTop: 14 }}>
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                <span className="mono" style={{ fontSize: 12, color: MUTE }}>行游標</span>
                <span className="mono" style={{ fontSize: 12, color: PAPER }}>row {row} / {maxRow}</span>
              </div>
              <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
                <span className="chip mono" onClick={() => setPlaying((p) => !p)}
                  style={{ padding: "4px 11px", fontSize: 12, borderRadius: 6, border: `1px solid ${LINE}`,
                    color: playing ? INK : PAPER, background: playing ? ONE : "transparent", fontWeight: 600 }}>
                  {playing ? "■ 停" : "▶ 下降"}
                </span>
                <input type="range" min={1} max={Math.max(1, maxRow)} value={row}
                  onChange={(e) => { setPlaying(false); setRow(+e.target.value); }} style={{ flex: 1 }} />
              </div>
            </div>
          </div>

          {/* analytics */}
          <div style={{ display: "flex", flexDirection: "column", gap: 16 }}>
            {/* stat strip */}
            <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 10 }}>
              <Stat k="此列長度" v={tri[row] ? tri[row].length : 0} />
              <Stat k="左邊緣值" v={edge} hot={edge === 1} />
              <Stat k="殘差1出現" v={ones} hot={ones <= 2} />
            </div>

            {/* transition matrix */}
            <div style={{ background: PANEL, border: `1px solid ${LINE}`, borderRadius: 10, padding: 14 }}>
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 10 }}>
                <span className="mono" style={{ fontSize: 12, color: MUTE }}>轉移{norm ? "頻率" : "計數"}矩陣 T[from→to]</span>
                <span className="chip mono" onClick={() => setNorm((n) => !n)}
                  style={{ padding: "2px 8px", fontSize: 11, borderRadius: 5, border: `1px solid ${norm ? ONE : LINE}`,
                    color: norm ? ONE : MUTE }}>
                  {norm ? "小數 ⏿" : "整數 ⏾"}
                </span>
              </div>
              <div style={{ display: "grid", gridTemplateColumns: `28px repeat(${m}, 1fr)`, gap: 3 }}>
                <div />
                {Array.from({ length: m }).map((_, j) => (
                  <div key={j} className="mono" style={{ textAlign: "center", fontSize: 11,
                    color: j === 1 ? ONE : MUTE }}>{j}</div>
                ))}
                {T.map((rw, i) => (
                  <React.Fragment key={i}>
                    <div className="mono" style={{ fontSize: 11, color: i === 1 ? ONE : MUTE,
                      display: "flex", alignItems: "center" }}>{i}</div>
                    {rw.map((x, j) => {
                      const isOne = i === 1 || j === 1;
                      const a = x === 0 ? 0 : 0.12 + 0.6 * (x / cellMax);
                      return (
                        <div key={j} className="mono" style={{ textAlign: "center", padding: "7px 2px",
                          fontSize: 12, borderRadius: 5,
                          background: x === 0 ? "#0d0f15" : `rgba(58,166,185,${a})`,
                          color: x === 0 ? "#363b46" : PAPER,
                          border: isOne ? `1px solid rgba(255,180,84,${x === 0 ? 0.25 : 0.7})` : "1px solid transparent",
                          fontWeight: x === cellMax ? 600 : 400 }}>
                          {fmt(x)}
                        </div>
                      );
                    })}
                  </React.Fragment>
                ))}
              </div>
              <p style={{ margin: "10px 0 0", fontSize: 12, color: MUTE, lineHeight: 1.45 }}>
                琥珀框 = 牽涉殘差 1 的轉移。下降時這圈會空成零，只剩邊緣那一個 1 撐著。
              </p>
            </div>

            {/* residue histogram */}
            <div style={{ background: PANEL, border: `1px solid ${LINE}`, borderRadius: 10, padding: 14 }}>
              <span className="mono" style={{ fontSize: 12, color: MUTE }}>此列殘差分布</span>
              <div style={{ display: "flex", alignItems: "flex-end", gap: 6, height: 84, marginTop: 10 }}>
                {hist.map((h, r) => (
                  <div key={r} style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", gap: 4 }}>
                    <span className="mono" style={{ fontSize: 10, color: MUTE }}>{h}</span>
                    <div style={{ width: "100%", height: `${(h / maxHist) * 60}px`,
                      background: resColor(r, m), borderRadius: "3px 3px 0 0",
                      animation: r === 1 ? "glow 2.2s ease-in-out infinite" : "none" }} />
                    <span className="mono" style={{ fontSize: 11, color: r === 1 ? ONE : MUTE }}>{r}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <p style={{ marginTop: 22, fontSize: 12.5, color: MUTE, lineHeight: 1.55, maxWidth: 900 }}>
          <span style={{ color: PAPER }}>讀法。</span> 第 1 列是質數間隙——二階MOD的指紋在這裡最濃（Lemke-Oliver 的反重複）。越往下，列被 Odlyzko 的 {"{0,2}"} 閉包吞沒，
          轉移矩陣收斂成一個只支撐在 {"{0,2}"} 上的固定塊，殘差 1 退化為左邊緣那條孤線。
          那是「二階MOD × Gilbreath」的核心現象：<span style={{ color: ONE }}>質數的個性只活在最上面幾列，深層是與質數無關的小字母動力學。</span>
        </p>
      </div>
    </div>
  );
}

function Ctl({ label, children }) {
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
      <span className="mono" style={{ fontSize: 11, color: "#6f727b", textTransform: "uppercase", letterSpacing: "0.05em" }}>{label}</span>
      {children}
    </div>
  );
}

function Stat({ k, v, hot }) {
  return (
    <div style={{ background: PANEL, border: `1px solid ${LINE}`, borderRadius: 9, padding: "10px 12px" }}>
      <div className="mono" style={{ fontSize: 10.5, color: "#6f727b", marginBottom: 4 }}>{k}</div>
      <div className="mono" style={{ fontSize: 19, fontWeight: 600, color: hot ? ONE : PAPER }}>{v}</div>
    </div>
  );
}

# ─────────────────────────────────────────────────────────────
```

---

## 7. 聲明與致謝

再次強調：**本文無任何新定理，全部數學實質歸於下列原作者。**

- Gilbreath 邊緣恆一的猜想：**N. L. Gilbreath**（1958），更早觀察：**F. Proth**（1878）。
- $\{0,2\}$ 飽和機制與大規模驗證：**A. M. Odlyzko**（1993）；早期驗證：**R. B. Killgrove 與 K. E. Ralston**（1959）。
- 「不限於質數」的推廣猜想：**H. Croft**，經 **M. Gardner**（1980）傳播。
- 隨機類比定理：**Z. Chase**（2020）。
- 相鄰質數剩餘的二階偏差：**R. J. Lemke Oliver 與 K. Soundararajan**（2016）。
- 整數序列編目：**OEIS Foundation**（A036262、A000232）。
- 近期數值延伸（$10^{14}$ 至 $1.5\times10^{15}$）：**S. Plouffe**（2025，arXiv:2510.06688）與 **J.-F. Colonna**（2025–2026，CMAP／École polytechnique），後者與 **J.-P. Delahaye** 合作。

本文僅將上述成果重新編排於同一視角下。任何錯誤歸於整理者，所有洞見歸於原作者。

---

## 參考文獻

[Proth1878] F. Proth, *Sur la série des nombres premiers*, Nouvelles Correspondances Mathématiques **4** (1878), 236–240.

[KR1959] R. B. Killgrove and K. E. Ralston, *On a conjecture concerning the primes*, Math. Comp. **13** (1959), 121–122.

[Gardner1980] M. Gardner, *Patterns in primes are a clue to the strong law of small numbers*, Scientific American **243** (Dec. 1980), 18–28.

[Odlyzko1993] A. M. Odlyzko, *Iterated absolute values of differences of consecutive primes*, Math. Comp. **61** (1993), no. 203, 373–380. DOI: 10.2307/2152962.

[Guy1994] R. K. Guy, *Unsolved Problems in Number Theory*, 2nd ed., §A10, Springer-Verlag, New York, 1994, pp. 25–26.

[LOS2016] R. J. Lemke Oliver and K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, Proc. Natl. Acad. Sci. USA **113** (2016), no. 31, E4446–E4454. DOI: 10.1073/pnas.1605366113. arXiv:1603.03720.

[Chase2020] Z. Chase, *A random analogue of Gilbreath's conjecture*, arXiv:2005.00530 (2020).

[Plouffe2025] S. Plouffe, *Verification of Gilbreath's conjecture up to $10^{14}$*, arXiv:2510.06688 (2025); 計算於 2025/10/07 完成，得 $G(\pi(10^{14}))=693$。

[Colonna2026] J.-F. Colonna（與 J.-P. Delahaye 合作）, *Proth–Gilbreath Conjecture*, Centre de Mathématiques Appliquées (CMAP), UMR CNRS 7641, École polytechnique（線上，頁面更新至 2026/05/08）。階段紀錄：$G(\pi(10^{14}))=693$（2025/10/05）、$G(\pi(10^{15}))=800$（2026/01/23），驗證至 $1.5\times10^{15}$（2026/03/18）。URL: http://www.lactamme.polytechnique.fr/descripteurs/GilbreathConjecture.01.Ang.html

[OEIS-A036262] N. J. A. Sloane (ed.), *The On-Line Encyclopedia of Integer Sequences*, sequence **A036262** (Gilbreath array).

[OEIS-A000232] N. J. A. Sloane (ed.), *The On-Line Encyclopedia of Integer Sequences*, sequence **A000232**.

[t5k-Gilbreath] C. K. Caldwell, *Gilbreath's conjecture*, The Prime Pages / Prime Glossary（線上）。

---

*草稿。Plouffe（arXiv:2510.06688）與 Colonna（lactamme.polytechnique.fr，更新至 2026/05/08）的近期數值驗證已核對一手來源；其餘引用（Odlyzko、Lemke Oliver–Soundararajan、Killgrove–Ralston、Proth、Guy、Gardner、Chase、OEIS）亦已核至一手。Proth 是否真曾發表（錯誤）證明，學界有分歧（見 Chase 2020），定稿措辭時可再斟酌。*
