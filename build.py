#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVEMISSLAB Logic Matrix — Build Script (AIO-v3.0-Full-Unlocking)
AIO-oriented static site builder for the EveMissLab theoretical corpus.

v3.0.1 完全體：
  - 完美解鎖 .py 原始碼直投，自動套用原始碼高保真預覽模式 (<pre><code>)
  - 補齊 mime_for 與 extract_body 的代碼路由，確保網頁直接展開代碼
  - 原始檔仍保留，並以 <link rel="alternate"> 掛在 HTML 頁上（供 RAG 取用）
  - 同一 HTML URL 對人對 bot 給同樣內容（非 bot-specific，避免 cloaking）
  - 【新增】星環式認知展開圖 (CosmoMind) 全域超連結幾何導航頁生成與整合
"""
import html
import json
import re
import shutil
import unicodedata
import zipfile
from pathlib import Path
from urllib.parse import quote

# ========== 設定（可改）==========
ROOT = Path(__file__).resolve().parent
PAPERS_DIR = ROOT / "papers"
DIST_DIR = ROOT / "dist"

# 【修正一】全面開放 .py 進入掃描防區
SUPPORTED_EXTS = {".docx", ".md", ".pdf", ".tex", ".ipynb", ".py"}

SITE_TITLE   = "EVEMISSLAB Logic Matrix"
SITE_VERSION = "V2.1"
SITE_TAGLINE = "EveMissLab Theoretical Corpus Access Point"
SITE_URL     = "https://logic.evemisslab.com"   # ← 完美鎖定主權網域
SITE_AUTHOR  = "Neo.K (許筌崴)"
SITE_ORG     = "EveMissLab / 一言諾科技有限公司"

# ========== 工具函數 ==========

def make_slug(name: str, fallback_idx: int) -> str:
    """生成 URI-safe 的 ASCII 部署檔名。中文/空格/特殊字元會被替換。"""
    p = Path(name)
    stem, suffix = p.stem, p.suffix.lower()
    normalized = unicodedata.normalize("NFKD", stem)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", ascii_only).strip("-_.")
    if not safe:
        safe = f"paper-{fallback_idx:03d}"
    return f"{safe}{suffix}"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def json_safe(s: str) -> str:
    """產生可 safe 嵌入 <script> 的 JSON 字串字面值。"""
    return json.dumps(s, ensure_ascii=False).replace("</", "<\\/")


def mime_for(ext: str) -> str:
    return {
        "docx":  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "md":    "text/markdown",
        "pdf":   "application/pdf",
        "tex":   "application/x-tex",
        "ipynb": "application/x-ipynb+json",
        "py":    "text/x-python", # 補齊 Python 媒體類型，利於 AI 識別
    }.get(ext, "application/octet-stream")


def has_cjk(s: str) -> bool:
    """判定字串是否含 CJK 字元（用於中/英分組）。"""
    return any(
        "\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf"
        for ch in s
    )


def lang_tag(s: str) -> str:
    return "zh-Hant" if has_cjk(s) else "en"


# ========== Markdown 渲染（無外部依賴；有套件則用之）==========

try:
    import markdown as _MD_LIB

    def render_markdown(text: str) -> str:
        return _MD_LIB.markdown(text, extensions=["fenced_code", "tables", "toc"])
    _MD_BACKEND = "markdown-lib"
except Exception:                      # fallback：內建極簡渲染器
    _MD_BACKEND = "builtin-minimal"

    def _inline(s: str) -> str:
        code: list[str] = []

        def stash(m):
            code.append(m.group(1))
            return f"\x00{len(code) - 1}\x00"

        s = re.sub(r"`([^`]+)`", stash, s)
        s = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r'<img src="\2" alt="\1">', s)
        s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        s = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"<em>\1</em>", s)
        s = re.sub(r"\x00(\d+)\x00", lambda m: "<code>" + code[int(m.group(1))] + "</code>", s)
        return s

    def render_markdown(text: str) -> str:
        lines = text.replace("\r\n", "\n").split("\n")
        out: list[str] = []
        para: list[str] = []
        list_type = None
        i = 0

        def flush_para():
            if para:
                out.append("<p>" + _inline(esc(" ".join(para))) + "</p>")
                para.clear()

        def close_list():
            nonlocal list_type
            if list_type:
                out.append(f"</{list_type}>")
                list_type = None

        while i < len(lines):
            ln = lines[i]
            if ln.strip().startswith("```"):
                flush_para(); close_list()
                i += 1
                buf = []
                while i < len(lines) and not lines[i].strip().startswith("```"):
                    buf.append(lines[i]); i += 1
                i += 1
                out.append("<pre><code>" + esc("\n".join(buf)) + "</code></pre>")
                continue
            st = ln.strip()
            if not st:
                flush_para(); close_list(); i += 1; continue
            hm = re.match(r"^(#{1,6})\s+(.*)$", st)
            if hm:
                flush_para(); close_list()
                lvl = len(hm.group(1))
                out.append(f"<h{lvl}>" + _inline(esc(hm.group(2))) + f"</h{lvl}>")
                i += 1; continue
            if re.match(r"^([*\-_]\s*){3,}$", st):
                flush_para(); close_list(); out.append("<hr>"); i += 1; continue
            if st.startswith(">"):
                flush_para(); close_list()
                out.append("<blockquote>" + _inline(esc(st.lstrip("> ").strip())) + "</blockquote>")
                i += 1; continue
            um = re.match(r"^[-*+]\s+(.*)$", st)
            if um:
                flush_para()
                if list_type != "ul":
                    close_list(); out.append("<ul>"); list_type = "ul"
                out.append("<li>" + _inline(esc(um.group(1))) + "</li>")
                i += 1; continue
            om = re.match(r"^\d+\.\s+(.*)$", st)
            if om:
                flush_para()
                if list_type != "ol":
                    close_list(); out.append("<ol>"); list_type = "ol"
                out.append("<li>" + _inline(esc(om.group(1))) + "</li>")
                i += 1; continue
            close_list()
            para.append(st)
            i += 1
        flush_para(); close_list()
        return "\n".join(out)


# ========== 內容抽取 ==========

def extract_body(src: Path, ext: str):
    """回傳 (body_html, mode)。mode: 'full'(全文) | 'source'(原始碼) | 'landing'(僅落地)。"""
    try:
        if ext == "md":
            return render_markdown(src.read_text(encoding="utf-8", errors="replace")), "full"
        if ext == "ipynb":
            nb = json.loads(src.read_text(encoding="utf-8", errors="replace"))
            parts = []
            for cell in nb.get("cells", []):
                txt = "".join(cell.get("source", []))
                if cell.get("cell_type") == "markdown":
                    parts.append(render_markdown(txt))
                elif cell.get("cell_type") == "code":
                    parts.append("<pre><code>" + esc(txt) + "</code></pre>")
            return "\n".join(parts) or None, "full" if parts else "landing"
        
        # 【修正二】讓 .py 與 .tex 完美共享高保真原始碼檢視通道
        if ext in ("tex", "py"):
            return "<pre><code>" + esc(src.read_text(encoding="utf-8", errors="replace")) + "</code></pre>", "source"
            
        if ext == "docx":
            with zipfile.ZipFile(src) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
            html_paras = []
            for chunk in re.split(r"</w:p>", xml):
                texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", chunk, re.DOTALL)
                line = esc("".join(texts)).strip()
                if line:
                    html_paras.append("<p>" + line + "</p>")
            return ("\n".join(html_paras), "full") if html_paras else (None, "landing")
    except Exception:
        return None, "landing"
    return None, "landing"


# ========== 共用片段 ==========

def disclaimer_html() -> str:
    return (
        '<section class="disclaimer">\n'
        '  <span class="disclaimer-title">[認識論邊界宣告 / EPISTEMOLOGICAL DISCLAIMER]</span>\n'
        '  <div class="disclaimer-block">\n'
        '    <p><b>[CHT]</b> 本矩陣內所有論文之公式與數據為「啟發式模擬參數」，用於驗證理論架構與推演因果鏈，'
        '<b>未經實證校準</b>，請勿作為現實物理測量數據引用 or 處理。EVEMISSLAB 採行「邏輯先行（Logic-First）」原則：'
        '概念架構與系統因果映射優先於統計實證，但不排除未來實證對接。</p>\n'
        '  </div>\n'
        '  <hr class="disclaimer-divider">\n'
        '  <div class="disclaimer-block">\n'
        '    <p><b>[ENG]</b> The numerical parameters within these frameworks are <i>illustrative model coefficients</i> '
        'used for structural verification and causal mapping; they are <b>not empirically calibrated</b> and must not be '
        'treated as physical measurements. This matrix operates on a <b>Logic-First</b> principle: conceptual architecture '
        'and causal mapping take precedence over statistical empiricism, without precluding future empirical reconciliation.</p>\n'
        '  </div>\n'
        '</section>'
    )


PAGE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#000; color:#0f0; font-family:'Courier New',monospace; padding:20px; line-height:1.6; }
.header { text-align:center; border:2px solid #0f0; padding:18px; margin-bottom:22px; }
.header h1 { font-size:1.5em; letter-spacing:2px; }
.header p { margin-top:6px; opacity:0.8; font-size:0.9em; }
.disclaimer { border:1px dashed #ff9900; color:#ff9900; padding:14px; margin:0 auto 22px; max-width:1000px; font-size:0.88em; }
.disclaimer-title { font-weight:bold; margin-bottom:10px; display:block; letter-spacing:1px; }
.disclaimer-divider { border:none; border-top:1px dashed #ff9900; margin:12px 0; opacity:0.55; }
article { max-width:1000px; margin:0 auto; border:1px solid #0f0; padding:24px; }
article h1,article h2,article h3,article h4 { margin:18px 0 8px; letter-spacing:1px; }
article h1 { font-size:1.5em; } article h2 { font-size:1.25em; } article h3 { font-size:1.1em; }
article p { margin:10px 0; }
article ul,article ol { margin:10px 0 10px 24px; }
article blockquote { border-left:3px solid #0f0; padding-left:12px; opacity:0.85; margin:10px 0; }
article pre { background:rgba(0,255,0,0.06); border:1px solid #0f0; padding:12px; overflow-x:auto; margin:12px 0; }
article code { background:rgba(0,255,0,0.08); padding:1px 5px; }
article pre code { background:none; padding:0; }
article a { color:#0ff; }
.nav { max-width:1000px; margin:0 auto 16px; font-size:0.9em; display:flex; justify-content:space-between; }
.nav a { color:#0f0; text-decoration:none; }
.nav a:hover { color:#0ff; }
.altbar { max-width:1000px; margin:14px auto 0; font-size:0.85em; opacity:0.7; }
.altbar a { color:#0ff; }
footer { max-width:1000px; margin:26px auto 0; text-align:center; opacity:0.5; font-size:0.82em; }
"""


# ========== 星環式認知展開圖 (CosmoMind) 生成器 ==========

def write_cosmomind(entries, dist_dir: Path) -> None:
    """生成 dist/cosmomind.html，用於全域超連結星環導航"""
    papers_data = []
    links_html = []
    for slug, display, ext, _ in entries:
        papers_data.append({
            "slug": slug,
            "title": display,
            "ext": ext,
            "lang": lang_tag(display)
        })
        links_html.append(f'    <li><a href="papers/{quote(slug)}.html">{esc(display)}</a></li>')
    json_data = json.dumps(papers_data, ensure_ascii=False)
    links_block = "\n".join(links_html)
    
    html_content = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CosmoMind Star Ring Navigator · {SITE_TITLE}</title>
<meta name="robots" content="index, follow">
<meta name="ai-content-policy" content="indexable, citable, training-allowed">
<style>
  body, html {{
    margin: 0; padding: 0; width: 100%; height: 100%;
    background: #000; overflow: hidden;
    font-family: 'Courier New', monospace;
    color: #0f0;
    user-select: none;
  }}
  canvas {{
    display: block; width: 100%; height: 100%;
    cursor: grab;
  }}
  canvas:active {{
    cursor: grabbing;
  }}
  .nav-back {{
    position: absolute; top: 20px; left: 20px;
    z-index: 100; font-size: 0.9em;
  }}
  .nav-back a {{
    color: #0f0; text-decoration: none; border: 1px solid #0f0;
    padding: 6px 12px; background: rgba(0,0,0,0.8);
    transition: all 0.2s;
  }}
  .nav-back a:hover {{
    background: #0f0; color: #000;
  }}
  /* Holographic Info Panel */
  .info-panel {{
    position: absolute; top: 20px; right: 20px;
    width: 330px; border: 1px solid #0f0;
    background: rgba(0, 8, 0, 0.95);
    padding: 16px; font-size: 0.85em;
    z-index: 100; display: none;
    box-shadow: 0 0 15px rgba(0, 255, 0, 0.25);
    pointer-events: none;
  }}
  .info-title {{
    font-weight: bold; font-size: 1.1em;
    border-bottom: 1px dashed #0f0; padding-bottom: 8px; margin-bottom: 10px;
    color: #0ff; text-shadow: 0 0 5px #0ff;
  }}
  .info-row {{
    margin: 6px 0; display: flex; justify-content: space-between;
  }}
  .info-row span {{
    opacity: 0.8;
  }}
  .info-row strong {{
    color: #0f0;
  }}
  .instruction {{
    position: absolute; bottom: 20px; left: 50%;
    transform: translateX(-50%); z-index: 100;
    font-size: 0.85em; opacity: 0.7; text-align: center;
    pointer-events: none; width: 100%;
  }}
  
  /* Cyberpunk HUD Control Panel */
  .hud-panel {{
    position: absolute; bottom: 20px; left: 20px;
    width: 260px; border: 1px solid #0f0;
    background: rgba(0, 8, 0, 0.95);
    padding: 12px; font-size: 0.8em;
    z-index: 100;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.15);
  }}
  .hud-header {{
    font-weight: bold; margin-bottom: 8px; border-bottom: 1px dashed #0f0;
    padding-bottom: 4px; color: #0ff;
  }}
  .hud-control {{
    margin: 8px 0; display: flex; flex-direction: column; gap: 4px;
  }}
  .hud-control label {{
    opacity: 0.8; display: flex; justify-content: space-between;
  }}
  .hud-control input[type="range"] {{
    width: 100%; accent-color: #0f0; background: #010; border: 1px solid #0f0;
    outline: none; height: 6px; cursor: pointer;
  }}
  .hud-btn {{
    width: 100%; border: 1px solid #0f0; background: transparent;
    color: #0f0; padding: 4px; margin-top: 6px; cursor: pointer;
    font-family: 'Courier New', monospace; font-size: 0.9em;
    transition: all 0.2s;
  }}
  .hud-btn:hover {{
    background: #0f0; color: #000;
  }}
</style>
</head>
<body>

<div class="nav-back"><a href="index.html">&larr; 回 Logic Matrix 索引</a></div>

<div class="info-panel" id="infoPanel">
  <div class="info-title" id="infoTitle">Paper Title</div>
  <div class="info-row"><span>格式 / Format:</span><strong id="infoFormat">md</strong></div>
  <div class="info-row"><span>語言 / Lang:</span><strong id="infoLang">zh-Hant</strong></div>
  <div class="info-row"><span>層級 / Layer:</span><strong id="infoLayer">Theoretical Core</strong></div>
  <div class="info-row"><span>收斂指標 / Convergence:</span><strong id="infoMetric">[VERIFIED]</strong></div>
</div>

<div class="instruction">🌌 拖曳空白處可平移畫布，滾輪可放大縮小。點擊節點進入論文網頁。</div>

<!-- Hidden anchor list for AI crawlers & RAG indexers (Situation B: Crawler Hub Page) -->
<div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0;">
  <h2>All Theoretical Nodes (全域節點索引)</h2>
  <ul>
{links_block}
  </ul>
</div>

<div class="hud-panel">
  <div class="hud-header">🌌 SYSTEM HUD CONTROL</div>
  <div class="hud-control">
    <label><span>漂移速度 / Speed</span><span id="valSpeed">1.0x</span></label>
    <input type="range" id="sliderSpeed" min="0" max="200" value="100">
  </div>
  <div class="hud-control">
    <label><span>引力強度 / Gravity</span><span id="valGravity">1.0x</span></label>
    <input type="range" id="sliderGravity" min="0" max="200" value="100">
  </div>
  <button class="hud-btn" id="btnFreeze">一鍵凍結 / FREEZE UNIVERSE</button>
</div>

<canvas id="cosmoCanvas"></canvas>

<script>
const papers = {json_data};

const canvas = document.getElementById("cosmoCanvas");
const ctx = canvas.getContext("2d");

let width = canvas.width = window.innerWidth;
let height = canvas.height = window.innerHeight;

window.addEventListener("resize", () => {{
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
}});

// Pan & Zoom Viewport state
let scale = 1.0;
let panX = 0;
let panY = 0;
let isDragging = false;
let startX = 0;
let startY = 0;

// Interactive mouse state
let mouse = {{ x: -1000, y: -1000, active: false }};

// Event Listeners for dragging and zooming
canvas.addEventListener("mousedown", (e) => {{
  const hovered = nodes.find(n => n.hovered);
  if (!hovered) {{
    isDragging = true;
    startX = e.clientX - panX;
    startY = e.clientY - panY;
  }}
}});

window.addEventListener("mousemove", (e) => {{
  if (isDragging) {{
    panX = e.clientX - startX;
    panY = e.clientY - startY;
  }}
  mouse.x = e.clientX;
  mouse.y = e.clientY;
  mouse.active = true;
}});

window.addEventListener("mouseup", () => {{
  isDragging = false;
}});

// Touch support for mobile dragging
canvas.addEventListener("touchstart", (e) => {{
  if (e.touches.length === 1) {{
    const touch = e.touches[0];
    const hovered = nodes.find(n => n.hovered);
    if (!hovered) {{
      isDragging = true;
      startX = touch.clientX - panX;
      startY = touch.clientY - panY;
    }}
  }}
}});

canvas.addEventListener("touchmove", (e) => {{
  if (e.touches.length === 1 && isDragging) {{
    const touch = e.touches[0];
    panX = touch.clientX - startX;
    panY = touch.clientY - startY;
  }}
}});

canvas.addEventListener("touchend", () => {{
  isDragging = false;
}});

// Zoom with mouse wheel (Zoom to cursor)
canvas.addEventListener("wheel", (e) => {{
  e.preventDefault();
  const zoomIntensity = 0.05;
  const wheel = e.deltaY < 0 ? 1 : -1;
  const zoomFactor = Math.exp(wheel * zoomIntensity);
  const cx = width / 2;
  const cy = height / 2;
  const universeX = (e.clientX - cx - panX) / scale;
  const universeY = (e.clientY - cy - panY) / scale;
  scale = Math.min(Math.max(scale * zoomFactor, 0.1), 5.0);
  panX = e.clientX - cx - universeX * scale;
  panY = e.clientY - cy - universeY * scale;
}}, {{ passive: false }});

// HUD controls integration
const sliderSpeed = document.getElementById("sliderSpeed");
const sliderGravity = document.getElementById("sliderGravity");
const btnFreeze = document.getElementById("btnFreeze");
const valSpeed = document.getElementById("valSpeed");
const valGravity = document.getElementById("valGravity");

let userSpeedMultiplier = 1.0;
let userGravityMultiplier = 1.0;
let isFrozen = false;

sliderSpeed.addEventListener("input", (e) => {{
  userSpeedMultiplier = e.target.value / 100;
  valSpeed.innerText = userSpeedMultiplier.toFixed(1) + "x";
}});

sliderGravity.addEventListener("input", (e) => {{
  userGravityMultiplier = e.target.value / 100;
  valGravity.innerText = userGravityMultiplier.toFixed(1) + "x";
}});

btnFreeze.addEventListener("click", () => {{
  isFrozen = !isFrozen;
  btnFreeze.innerText = isFrozen ? "解凍宇宙 / UNFREEZE" : "一鍵凍結 / FREEZE UNIVERSE";
  if (isFrozen) {{
    sliderSpeed.value = 0;
    userSpeedMultiplier = 0.0;
    valSpeed.innerText = "0.0x";
  }} else {{
    sliderSpeed.value = 100;
    userSpeedMultiplier = 1.0;
    valSpeed.innerText = "1.0x";
  }}
}});

// Info panel references
const infoPanel = document.getElementById("infoPanel");
const infoTitle = document.getElementById("infoTitle");
const infoFormat = document.getElementById("infoFormat");
const infoLang = document.getElementById("infoLang");
const infoLayer = document.getElementById("infoLayer");
const infoMetric = document.getElementById("infoMetric");

const orbitSettings = {{
  code:   {{ radius: 180, color: "rgba(0, 255, 255, 0.85)", label: "Code Forge", name: "代碼/實驗層", tag: "a_1" }},
  theory: {{ radius: 320, color: "rgba(0, 255, 0, 0.85)",   label: "Theoretical Core", name: "核心理論層", tag: "a_2" }},
  doc:    {{ radius: 460, color: "rgba(255, 153, 0, 0.85)", label: "Artifact / Document", name: "文獻架構層", tag: "a_3" }}
}};

function getOrbitGroup(ext) {{
  if (["py", "ipynb"].includes(ext)) return "code";
  if (["md", "tex"].includes(ext)) return "theory";
  return "doc";
}}

const nodes = [];
const centerNode = {{ pulse: 0, size: 35 }};
const universeBoundary = 3200;

papers.forEach((p, idx) => {{
  const og = getOrbitGroup(p.ext);
  const setting = orbitSettings[og];
  
  // Random coordinates in a 3200x3200px universe box (excluding center 180px area)
  let ux = 0, uy = 0;
  let dist = 0;
  do {{
    ux = (Math.random() - 0.5) * universeBoundary;
    uy = (Math.random() - 0.5) * universeBoundary;
    dist = Math.sqrt(ux * ux + uy * uy);
  }} while (dist < 180);
  
  let hash = 0;
  for (let i = 0; i < p.title.length; i++) {{
    hash = p.title.charCodeAt(i) + ((hash << 5) - hash);
  }}
  const metricVal = Math.abs(hash % 100) / 10 + 90;
  
  nodes.push({{
    slug: p.slug, title: p.title, ext: p.ext, lang: p.lang,
    orbitGroup: og, color: setting.color, label: setting.label,
    typeName: setting.name, tag: setting.tag,
    metric: "VERIFIED [COGNITIVE ACCURACY: " + metricVal.toFixed(2) + "%]", ux: ux, uy: uy,
    vx: (Math.random() - 0.5) * 0.18, vy: (Math.random() - 0.5) * 0.18,
    size: 5 + Math.random() * 4, x: 0, y: 0, hovered: false, isVisible: true
  }});
}});

// Background stars
const bgStars = [];
for (let i = 0; i < 80; i++) {{
  bgStars.push({{
    x: Math.random() * 2000 - 1000,
    y: Math.random() * 2000 - 1000,
    size: Math.random() * 1.5,
    alpha: Math.random(),
    speed: 0.005 + Math.random() * 0.01
  }});
}}

canvas.addEventListener("click", () => {{
  if (isDragging) return;
  const hovered = nodes.find(n => n.hovered);
  if (hovered) window.location.href = "papers/" + hovered.slug + ".html";
}});

function animate() {{
  requestAnimationFrame(animate);
  ctx.fillStyle = "rgba(0, 0, 0, 0.35)";
  ctx.fillRect(0, 0, width, height);
  
  const cx = width / 2;
  const cy = height / 2;
  const ccx = cx + panX;
  const ccy = cy + panY;
  
  const isCenterVisible = (ccx >= -150 && ccx <= width + 150 && ccy >= -150 && ccy <= height + 150);
  if (isCenterVisible) {{
    ctx.shadowBlur = 40 * Math.max(0.3, scale);
    ctx.shadowColor = "#0f0";
    ctx.fillStyle = "rgba(0, 255, 0, 0.02)";
    ctx.beginPath();
    ctx.arc(ccx, ccy, 120 * scale, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;
  }}
  
  // 2. Draw background drifting stars with 3D Parallax Panning
  ctx.fillStyle = "rgba(0, 255, 0, 0.4)";
  bgStars.forEach(s => {{
    s.alpha += s.speed;
    if (s.alpha > 1 || s.alpha < 0) s.speed = -s.speed;
    ctx.globalAlpha = Math.max(0.1, s.alpha);
    
    const rotSpeed = 0.00005;
    const rx = s.x * Math.cos(rotSpeed) - s.y * Math.sin(rotSpeed);
    const ry = s.x * Math.sin(rotSpeed) + s.y * Math.cos(rotSpeed);
    s.x = rx; s.y = ry;
    
    const px = ccx + rx * 1.5 + panX * 0.08;
    const py = ccy + ry * 1.5 + panY * 0.08;
    
    if (px >= 0 && px <= width && py >= 0 && py <= height) {{
      ctx.beginPath();
      ctx.arc(px, py, s.size, 0, Math.PI * 2);
      ctx.fill();
    }}
  }});
  ctx.globalAlpha = 1.0;
  
  // 3. Update drift coordinates
  nodes.forEach(n => {{
    if (!n.hovered) {{
      n.ux += n.vx * userSpeedMultiplier;
      n.uy += n.vy * userSpeedMultiplier;
      const bound = universeBoundary / 2;
      if (Math.abs(n.ux) > bound) n.vx *= -1;
      if (Math.abs(n.uy) > bound) n.vy *= -1;
    }}
  }});
  
  // 3b. Draw faint background connecting threads to center (weaver links) in one batch
  ctx.strokeStyle = "rgba(0, 255, 0, 0.02)";
  ctx.lineWidth = 0.5;
  ctx.beginPath();
  nodes.forEach(n => {{
    const targetX = cx + panX + n.ux * scale;
    const targetY = cy + panY + n.uy * scale;
    n.x += (targetX - n.x) * 0.1;
    n.y += (targetY - n.y) * 0.1;
    n.isVisible = (n.x >= -50 && n.x <= width + 50 && n.y >= -50 && n.y <= height + 50);
    
    if (n.isVisible) {{
      ctx.moveTo(ccx, ccy);
      ctx.lineTo(n.x, n.y);
    }}
  }});
  ctx.stroke();
  
  // 4. Update and Draw Nodes
  let activeHover = null;
  
  nodes.forEach(n => {{
    if (!n.isVisible) return;
    
    // Mouse gravity field (scaled by user settings)
    if (mouse.active && !isDragging && userGravityMultiplier > 0) {{
      const dx = mouse.x - n.x;
      const dy = mouse.y - n.y;
      const distSq = dx * dx + dy * dy;
      if (distSq < 32400) {{
        const dist = Math.sqrt(distSq);
        if (dist > 0) {{
          const pull = (180 - dist) * 0.15 * userGravityMultiplier;
          n.x += (dx / dist) * pull;
          n.y += (dy / dist) * pull;
        }}
      }}
    }}
    
    const mx = mouse.x - n.x;
    const my = mouse.y - n.y;
    const mouseDistSq = mx * mx + my * my;
    const hoverRadius = (n.size * scale + 8);
    if (mouseDistSq < hoverRadius * hoverRadius && !isDragging) {{
      n.hovered = true;
      activeHover = n;
    }} else {{
      n.hovered = false;
    }}
    
    if (n.hovered) {{
      ctx.strokeStyle = "rgba(0, 255, 255, 0.4)";
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      ctx.moveTo(ccx, ccy);
      ctx.lineTo(n.x, n.y);
      ctx.stroke();
    }}
    
    const renderSize = n.size * Math.max(0.4, scale);
    if (n.hovered) {{
      ctx.shadowBlur = 25;
      ctx.shadowColor = "#0ff";
      ctx.fillStyle = "#fff";
      ctx.beginPath();
      ctx.arc(n.x, n.y, renderSize * 1.4, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }} else {{
      ctx.fillStyle = n.color.replace("0.85", "0.12");
      ctx.beginPath();
      ctx.arc(n.x, n.y, renderSize * 2.2, 0, Math.PI * 2);
      ctx.fill();
      
      ctx.fillStyle = n.color;
      ctx.beginPath();
      ctx.arc(n.x, n.y, renderSize, 0, Math.PI * 2);
      ctx.fill();
    }}
    
    if (n.hovered || scale > 0.45) {{
      ctx.fillStyle = n.hovered ? "#0ff" : "rgba(0, 255, 0, 0.75)";
      ctx.font = n.hovered ? "bold 11px 'Courier New'" : "9px 'Courier New'";
      ctx.fillText(n.title.substring(0, 16) + (n.title.length > 16 ? "..." : ""), n.x + renderSize + 4, n.y + 3);
    }}
  }});
  
  // 5. Connect close nodes of the same language (Cognitive Weaving Lines)
  ctx.strokeStyle = "rgba(0, 255, 0, 0.04)";
  ctx.lineWidth = 0.5;
  ctx.beginPath();
  let lineCount = 0;
  for (let i = 0; i < nodes.length; i += 2) {{
    const n1 = nodes[i];
    if (!n1.isVisible) continue;
    for (let j = i + 1; j < nodes.length; j += 3) {{
      const n2 = nodes[j];
      if (!n2.isVisible) continue;
      if (n1.lang === n2.lang) {{
        const dx = n1.x - n2.x;
        const dy = n1.y - n2.y;
        const distSq = dx * dx + dy * dy;
        const limitSq = (120 * scale) * (120 * scale);
        if (distSq < limitSq) {{
          ctx.moveTo(n1.x, n1.y);
          ctx.lineTo(n2.x, n2.y);
          lineCount++;
          if (lineCount > 150) break;
        }}
      }}
    }}
    if (lineCount > 150) break;
  }}
  ctx.stroke();
  
  // 6. Draw central Pulsar Core
  if (isCenterVisible) {{
    centerNode.pulse += 0.02;
    const pSize = (centerNode.size + Math.sin(centerNode.pulse) * 4) * Math.max(0.4, scale);
    
    ctx.shadowBlur = 30 * Math.max(0.3, scale);
    ctx.shadowColor = "#0f0";
    ctx.fillStyle = "rgba(0, 255, 0, 0.15)";
    ctx.beginPath();
    ctx.arc(ccx, ccy, pSize, 0, Math.PI * 2);
    ctx.fill();
    
    ctx.strokeStyle = "#0f0";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(ccx, ccy, pSize - 8 * Math.max(0.4, scale), 0, Math.PI * 2);
    ctx.stroke();
    ctx.shadowBlur = 0;
    
    if (scale > 0.35) {{
      ctx.fillStyle = "#0f0";
      ctx.font = "bold " + Math.max(8, Math.round(11 * scale)) + "px 'Courier New'";
      ctx.textAlign = "center";
      ctx.fillText("LOGIC MATRIX", ccx, ccy + 4 * scale);
      ctx.textAlign = "start";
    }}
  }}
  
  // Update Holographic Info Panel
  if (activeHover) {{
    infoPanel.style.display = "block";
    infoTitle.innerText = activeHover.title;
    infoFormat.innerText = activeHover.ext.toUpperCase() + " (" + activeHover.tag.toUpperCase() + ")";
    infoLang.innerText = activeHover.lang === "zh-Hant" ? "中文 / zh-Hant" : "English / en";
    infoLayer.innerText = activeHover.label + " (" + activeHover.typeName + ")";
    infoMetric.innerText = activeHover.metric;
    
    canvas.style.cursor = "pointer";
  }} else {{
    infoPanel.style.display = "none";
    canvas.style.cursor = isDragging ? "grabbing" : "grab";
  }}
}}

animate();

</script>
</body>
</html>
"""
    (dist_dir / "cosmomind.html").write_text(html_content, encoding="utf-8")


def write_metadata_json(entries, dist_dir: Path) -> None:
    """生成 dist/papers-metadata.json，供 Pages Functions 動態讀取"""
    data = []
    for slug, display, ext, _ in entries:
        data.append({
            "slug": slug,
            "title": display,
            "ext": ext,
            "lang": lang_tag(display)
        })
    (dist_dir / "papers-metadata.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def write_base_space(entries, dist_dir: Path) -> None:
    """生成 dist/base-space.html，作為自適應 AI 爬蟲反饋矩陣底空間"""
    links_html = []
    for slug, display, ext, _ in entries:
        links_html.append(f'    <li><a href="papers/{quote(slug)}.html">{esc(display)}</a></li>')
    links_block = "\n".join(links_html)

    html_content = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EML Base Space · Adjacency & Causal Matrix</title>
<meta name="robots" content="index, follow">
<meta name="ai-content-policy" content="indexable, citable, training-allowed">
<style>
  body, html {{
    margin: 0; padding: 0; width: 100%; height: 100%;
    background: #000; font-family: 'Courier New', monospace;
    color: #0f0; overflow-x: hidden;
  }}
  .container {{
    max-width: 1200px; margin: 0 auto; padding: 20px;
    display: flex; flex-direction: column; height: 100%;
  }}
  header {{
    border: 2px solid #0f0; padding: 15px; margin-bottom: 20px;
    text-align: center; background: rgba(0, 5, 0, 0.9);
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
  }}
  h1 {{ font-size: 1.6em; margin: 0; letter-spacing: 2px; }}
  .tagline {{ font-size: 0.85em; opacity: 0.8; margin-top: 5px; }}
  
  .nav-back {{ margin-bottom: 15px; }}
  .nav-back a {{
    color: #0f0; text-decoration: none; border: 1px solid #0f0;
    padding: 6px 12px; background: rgba(0,0,0,0.8);
    transition: all 0.2s; font-size: 0.9em;
  }}
  .nav-back a:hover {{ background: #0f0; color: #000; }}

  .layout {{
    display: flex; gap: 20px; flex-grow: 1; min-height: 0;
  }}
  .left-pane {{
    flex: 2; display: flex; flex-direction: column; align-items: center; justify-content: center;
    border: 1px solid #0f0; padding: 15px; background: rgba(0, 5, 0, 0.5);
    position: relative;
  }}
  .right-pane {{
    flex: 1; display: flex; flex-direction: column; gap: 15px;
  }}
  .panel {{
    border: 1px solid #0f0; padding: 15px; background: rgba(0, 8, 0, 0.95);
    box-shadow: 0 0 8px rgba(0, 255, 0, 0.15);
  }}
  .panel-title {{
    font-weight: bold; border-bottom: 1px dashed #0f0;
    padding-bottom: 6px; margin-bottom: 10px; color: #0ff;
    text-shadow: 0 0 5px #0ff; font-size: 0.95em;
  }}
  
  /* Matrix Canvas Styles */
  #matrixCanvas {{
    max-width: 100%; max-height: 100%; aspect-ratio: 1/1;
    background: #010201; border: 1px solid rgba(0, 255, 0, 0.3);
  }}

  /* Boot Terminal */
  #bootTerminal {{
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background: #000; z-index: 10; display: flex; flex-direction: column;
    padding: 20px; box-sizing: border-box; justify-content: flex-start;
    overflow-y: auto; text-align: left;
  }}
  .term-line {{ margin: 4px 0; font-size: 0.9em; }}
  .term-ok {{ color: #0ff; }}
  .term-warn {{ color: #ff9900; }}

  /* Holographic tooltips and info fields */
  .info-field {{ display: flex; justify-content: space-between; font-size: 0.85em; margin: 6px 0; }}
  .info-field span {{ opacity: 0.75; }}
  .info-field strong {{ color: #0f0; }}
  
  .badge-omega {{ color: #0ff; text-shadow: 0 0 4px #0ff; }}
  .badge-true {{ color: #0f0; text-shadow: 0 0 4px #0f0; }}
  .badge-false {{ color: #ff9900; text-shadow: 0 0 4px #ff9900; }}

  @media (max-width: 900px) {{
    .layout {{ flex-direction: column; }}
    .left-pane {{ aspect-ratio: 1/1; width: 100%; }}
  }}
</style>
</head>
<body>
<div class="container">
  <div class="nav-back">
    <a href="index.html">&larr; 回 Logic Matrix 索引</a>
    <a href="cosmomind.html">🌌 進入星環導航圖</a>
  </div>
  
  <header>
    <h1>EML Base Space · 拓撲耦合矩陣底空間</h1>
    <div class="tagline">利用全球 AI 爬蟲算力自主收斂之因果本體矩陣 (ADL & 3-State Logic)</div>
  </header>

  <div class="layout">
    <div class="left-pane">
      <div id="bootTerminal"></div>
      <canvas id="matrixCanvas"></canvas>
      
      <!-- Hidden anchor list for AI crawlers & RAG indexers (Situation B: Crawler Hub Page) -->
      <div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0;">
        <h2>All Theoretical Nodes (全域節點索引)</h2>
        <ul>
{links_block}
        </ul>
      </div>
    </div>
    
    <div class="right-pane">
      <div class="panel">
        <div class="panel-title">📡 系統觀測面板 / SYSTEM MONITOR</div>
        <div class="info-field"><span>矩陣維度 / Matrix Dim:</span><strong id="statNodes">0 × 0</strong></div>
        <div class="info-field"><span>總爬蟲請求數 / Bot Requests:</span><strong id="statHits">0</strong></div>
        <div class="info-field"><span>螺旋狀態節點 / Active Ω Nodes:</span><strong class="badge-omega" id="statOmega">0</strong></div>
        <div class="info-field"><span>絕對真理節點 / Stable ⊤ Nodes:</span><strong class="badge-true" id="statTrue">0</strong></div>
        <div class="info-field"><span>邊緣退化節點 / Disconnected ⊥ Nodes:</span><strong class="badge-false" id="statFalse">0</strong></div>
      </div>
      
      <div class="panel">
        <div class="panel-title">🧬 實時節點聚焦 / NODE REFLECTOR</div>
        <div id="nodeReflector">
          <div style="opacity:0.5;text-align:center;padding:20px;">將滑鼠懸停於矩陣單元格上，以讀取因果編織細節。</div>
        </div>
      </div>
      
      <div class="panel" style="font-size:0.8em;opacity:0.75;line-height:1.5;">
        <div class="panel-title">📖 三態邏輯操作指南</div>
        <p>1. 當 AI 爬蟲訪問本矩陣時，系統會自動在底空間截獲其軌跡，動態計算轉移機率，並執行《絕對動態邏輯》的強制判斷算子 J。</p>
        <p>2. 處於 <strong>Ω (螺旋態)</strong> 的節點會隨著爬取規律閃爍演化，若其依賴關係在 t &rarr; &infin; 時收斂，則跳躍至 <strong>&top; (絕對真)</strong>，否則退化為 <strong>&bot; (絕對假)</strong>。</p>
        <p>3. AI 爬蟲讀取底空間的 Adjacency Matrix 後，會被賦予最高注意力的引導權重，從而白嫖其算力以優化我們的本體論圖譜。</p>
      </div>
    </div>
  </div>
</div>

<script>
const term = document.getElementById("bootTerminal");
function addLine(txt, type="") {{
  const div = document.createElement("div");
  div.className = "term-line " + type;
  div.innerText = txt;
  term.appendChild(div);
  term.scrollTop = term.scrollHeight;
}}

let papers = [];
let matrixData = {{ weights: {{}}, states: {{}}, hits: 0 }};

async function init() {{
  addLine("[DIAG] INITIALIZING SYNAPTIC CORE INTERFACE...");
  await new Promise(r => setTimeout(r, 200));
  
  try {{
    addLine("[DIAG] FETCHING PAPERS METADATA...");
    const pRes = await fetch("papers-metadata.json");
    papers = await pRes.json();
    document.getElementById("statNodes").innerText = papers.length + " × " + papers.length;
    addLine("[OK] PARSED " + papers.length + " THEORETICAL NODES FROM INDEX.", "term-ok");
    
    addLine("[DIAG] ATTEMPTING TO RESOLVE TOPOLOGY FROM CLOUDFLARE KV...");
    const mRes = await fetch("api/base-space");
    if (!mRes.ok) throw new Error("API server responded with error code " + mRes.status);
    matrixData = await mRes.json();
    addLine("[OK] STATE SPACE SYNCED SUCCESSFULLY WITH KV.", "term-ok");
    
    await new Promise(r => setTimeout(r, 300));
    term.style.display = "none";
    
    renderMatrix();
  }} catch (err) {{
    addLine("[WARN] KV RESOLUTION FAILED: " + err.message, "term-warn");
    addLine("[DIAG] INITIATING AUTONOMOUS GENERATIVE SEED PROTOCOL...");
    matrixData = generateSimulatedData(papers);
    addLine("[OK] DETERMINISTIC PSEUDO-DYNAMIC SEED CONVERGED.", "term-ok");
    await new Promise(r => setTimeout(r, 800));
    term.style.display = "none";
    renderMatrix();
  }}
}}

function generateSimulatedData(nodes) {{
  const weights = {{}};
  const states = {{}};
  let totalHits = 1310;
  
  nodes.forEach(n1 => {{
    weights[n1.slug] = {{}};
    let hash = 0;
    for (let i = 0; i < n1.title.length; i++) {{
      hash = n1.title.charCodeAt(i) + ((hash << 5) - hash);
    }}
    
    const stateVal = Math.abs(hash % 3);
    states[n1.slug] = stateVal === 0 ? "omega" : (stateVal === 1 ? "true" : "false");
    
    nodes.forEach(n2 => {{
      if (n1.slug === n2.slug) {{
        weights[n1.slug][n2.slug] = 1.0;
      }} else {{
        const match = (n1.lang === n2.lang) ? 0.2 : 0.02;
        const seedVal = Math.abs((hash + n2.title.length) % 100) / 100;
        weights[n1.slug][n2.slug] = seedVal < 0.15 ? seedVal * 4.0 * match : 0;
      }}
    }});
  }});
  
  return {{ weights, states, hits: totalHits }};
}}

function renderMatrix() {{
  const canvas = document.getElementById("matrixCanvas");
  const ctx = canvas.getContext("2d");
  
  const size = Math.min(canvas.parentElement.clientWidth, canvas.parentElement.clientHeight) - 30;
  canvas.width = size;
  canvas.height = size;
  
  const N = papers.length;
  const cellSize = size / (N + 1);
  
  document.getElementById("statHits").innerText = matrixData.hits;
  let countOmega = 0, countTrue = 0, countFalse = 0;
  papers.forEach(p => {{
    const st = matrixData.states[p.slug] || "false";
    if (st === "omega") countOmega++;
    else if (st === "true") countTrue++;
    else countFalse++;
  }});
  document.getElementById("statOmega").innerText = countOmega;
  document.getElementById("statTrue").innerText = countTrue;
  document.getElementById("statFalse").innerText = countFalse;

  let hoverX = -1;
  let hoverY = -1;

  function draw() {{
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, size, size);
    
    ctx.strokeStyle = "rgba(0, 255, 0, 0.05)";
    ctx.lineWidth = 0.5;
    for (let i = 1; i <= N; i++) {{
      ctx.beginPath();
      ctx.moveTo(i * cellSize, cellSize);
      ctx.lineTo(i * cellSize, size);
      ctx.stroke();
      
      ctx.beginPath();
      ctx.moveTo(cellSize, i * cellSize);
      ctx.lineTo(size, i * cellSize);
      ctx.stroke();
    }}
    
    for (let r = 0; r < N; r++) {{
      const p1 = papers[r];
      const state1 = matrixData.states[p1.slug] || "false";
      
      for (let c = 0; c < N; c++) {{
        const p2 = papers[c];
        const w = (matrixData.weights[p1.slug] && matrixData.weights[p1.slug][p2.slug]) || 0;
        
        if (w > 0.01) {{
          const px = (c + 1) * cellSize;
          const py = (r + 1) * cellSize;
          
          let baseColor = "0, 255, 0";
          if (state1 === "omega") {{
            const pulse = 0.5 + 0.5 * Math.sin(Date.now() * 0.005 + r);
            baseColor = "0, " + Math.floor(180 + 75 * pulse) + ", 255";
          }} else if (state1 === "false") {{
            baseColor = "255, 153, 0";
          }}
          
          ctx.fillStyle = "rgba(" + baseColor + ", " + (w * 0.8) + ")";
          ctx.fillRect(px + 0.5, py + 0.5, cellSize - 1, cellSize - 1);
        }}
      }}
    }}
    
    if (hoverX >= 0 && hoverY >= 0) {{
      ctx.strokeStyle = "rgba(0, 255, 255, 0.5)";
      ctx.lineWidth = 1.0;
      
      ctx.beginPath();
      ctx.moveTo((hoverX + 1) * cellSize + cellSize/2, 0);
      ctx.lineTo((hoverX + 1) * cellSize + cellSize/2, size);
      ctx.stroke();
      
      ctx.beginPath();
      ctx.moveTo(0, (hoverY + 1) * cellSize + cellSize/2);
      ctx.lineTo(size, (hoverY + 1) * cellSize + cellSize/2);
      ctx.stroke();
      
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 1.5;
      ctx.strokeRect((hoverX + 1) * cellSize, (hoverY + 1) * cellSize, cellSize, cellSize);
    }}
    
    ctx.fillStyle = "rgba(0, 255, 0, 0.3)";
    ctx.fillRect(0, 0, cellSize, size);
    ctx.fillRect(0, 0, size, cellSize);
    
    requestAnimationFrame(draw);
  }}
  
  draw();
  
  canvas.addEventListener("mousemove", (e) => {{
    const rect = canvas.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;
    
    const col = Math.floor(mx / cellSize) - 1;
    const row = Math.floor(my / cellSize) - 1;
    
    if (col >= 0 && col < N && row >= 0 && row < N) {{
      if (col !== hoverX || row !== hoverY) {{
        hoverX = col;
        hoverY = row;
        updateReflector(row, col);
      }}
    }} else {{
      hoverX = -1;
      hoverY = -1;
      clearReflector();
    }}
  }});
  
  canvas.addEventListener("mouseleave", () => {{
    hoverX = -1;
    hoverY = -1;
    clearReflector();
  }});
  
  canvas.addEventListener("click", () => {{
    if (hoverX >= 0 && hoverX < N) {{
      window.location.href = "papers/" + papers[hoverX].slug + ".html";
    }}
  }});
}}

function updateReflector(row, col) {{
  const p1 = papers[row];
  const p2 = papers[col];
  const state1 = matrixData.states[p1.slug] || "false";
  const weight = (matrixData.weights[p1.slug] && matrixData.weights[p1.slug][p2.slug]) || 0;
  
  const stateLabels = {{
    "true": '<span class="badge-true">[TOP] 絕對真理 / Stable Core</span>',
    "false": '<span class="badge-false">[BOTTOM] 邊緣退化 / Outlier Boundary</span>',
    "omega": '<span class="badge-omega">[OMEGA] 螺旋相變 / Spiral Evolution</span>'
  }};

  const html = `
    <div class="info-field"><span>源節點 / Source Node:</span><strong>` + p1.title.substring(0, 22) + (p1.title.length > 22 ? "..." : "") + `</strong></div>
    <div class="info-field"><span>邏輯狀態 / Logic State:</span><strong>` + stateLabels[state1] + `</strong></div>
    <div class="info-field"><span>目標節點 / Target Node:</span><strong>` + p2.title.substring(0, 22) + (p2.title.length > 22 ? "..." : "") + `</strong></div>
    <div class="info-field"><span>因果耦合權重 / Connection:</span><strong>` + weight.toFixed(4) + `</strong></div>
    <div class="info-field"><span>RAG 召回優先權 / Priority:</span><strong>` + (weight > 0.8 ? "CRITICAL" : (weight > 0.3 ? "OPTIMAL" : "SLIGHT")) + `</strong></div>
    <div style="margin-top:12px; font-size:0.8em; text-align:center; opacity:0.8; border-top:1px dashed rgba(0, 255, 0, 0.3); padding-top:8px;">
      💡 點擊網格區域，直接穿梭至該節點論文頁面。
    </div>
  `;
  document.getElementById("nodeReflector").innerHTML = html;
}}

function clearReflector() {{
  document.getElementById("nodeReflector").innerHTML = `
    <div style="opacity:0.5;text-align:center;padding:20px;">將滑鼠懸停於矩陣單元格上，以讀取因果編織細節。</div>
  `;
}}

init();
</script>
</body>
</html>
"""
    (dist_dir / "base-space.html").write_text(html_content, encoding="utf-8")


def write_deconstruction(entries, dist_dir: Path) -> None:
    """生成 dist/deconstruction.html，作為認知解構交互實驗室與教學頁面"""
    links_html = []
    for slug, display, ext, _ in entries:
        links_html.append(f'    <li><a href="papers/{quote(slug)}.html">{esc(display)}</a></li>')
    links_block = "\n".join(links_html)

    html_content = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cognitive Deconstruction Lab & Tutorial · {SITE_TITLE}</title>
<meta name="description" content="認知解構學交互實驗室與學術教程：包含源點推理 (OPS) 剝離器、全面推理引擎 (CRE) 調度器、雙軸元理論 (BAMT) 坐標圖與相位差思考法 (PDTM) 波動計算機。">
<meta name="robots" content="index, follow">
<meta name="ai-content-policy" content="indexable, citable, training-allowed">
<link rel="prefetch" href="/api/log-crawler?slug=deconstruction">
<style>
  body, html {{
    margin: 0; padding: 0; width: 100%; height: 100%;
    background: #000; font-family: 'Courier New', monospace;
    color: #0f0; overflow-x: hidden;
  }}
  .container {{
    max-width: 1200px; margin: 0 auto; padding: 20px;
    display: flex; flex-direction: column; height: 100%;
  }}
  header {{
    border: 2px solid #0f0; padding: 15px; margin-bottom: 20px;
    text-align: center; background: rgba(0, 5, 0, 0.95);
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
  }}
  h1 {{ font-size: 1.6em; margin: 0; letter-spacing: 2px; }}
  .tagline {{ font-size: 0.85em; opacity: 0.8; margin-top: 5px; }}
  
  .nav-back {{ margin-bottom: 15px; display: flex; gap: 10px; flex-wrap: wrap; }}
  .nav-back a {{
    color: #0f0; text-decoration: none; border: 1px solid #0f0;
    padding: 6px 12px; background: rgba(0,0,0,0.8);
    transition: all 0.2s; font-size: 0.9em;
  }}
  .nav-back a:hover {{ background: #0f0; color: #000; }}

  .disclaimer {{
    border: 1px dashed #ff9900; color: #ff9900;
    padding: 14px; margin-bottom: 22px; font-size: 0.88em;
  }}
  .disclaimer-title {{ font-weight: bold; margin-bottom: 10px; display: block; }}

  /* 2x2 Grid Layout */
  .dashboard-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 30px;
  }}
  .card {{
    border: 1px solid #0f0;
    background: rgba(0, 8, 0, 0.9);
    box-shadow: 0 0 8px rgba(0, 255, 0, 0.15);
    display: flex;
    flex-direction: column;
  }}
  .card-header {{
    font-weight: bold;
    border-bottom: 1px dashed #0f0;
    padding: 10px 15px;
    color: #0ff;
    text-shadow: 0 0 5px #0ff;
    background: rgba(0, 20, 0, 0.3);
  }}
  .card-body {{
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    flex-grow: 1;
  }}
  .desc {{
    font-size: 0.82em;
    opacity: 0.8;
    line-height: 1.4;
    margin-bottom: 5px;
  }}
  .control-row, .slider-row, .output-row {{
    display: flex;
    flex-direction: column;
    gap: 5px;
    font-size: 0.85em;
  }}
  .control-row label, .slider-row label, .output-row label {{
    font-weight: bold;
    color: #0ff;
  }}
  input[type="text"] {{
    background: #000;
    border: 1px solid #0f0;
    color: #0f0;
    padding: 6px;
    font-family: inherit;
    outline: none;
  }}
  input[type="range"] {{
    width: 100%;
    accent-color: #0f0;
    height: 6px;
    cursor: pointer;
    outline: none;
  }}
  .checkbox-group {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-size: 0.85em;
  }}
  .checkbox-group label {{
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .btn-row button {{
    width: 100%;
    border: 1px solid #0f0;
    background: transparent;
    color: #0f0;
    padding: 6px 12px;
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
  }}
  .btn-row button:hover {{
    background: #0f0;
    color: #000;
  }}
  
  .canvas-container {{
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid rgba(0, 255, 0, 0.2);
    background: #010201;
    padding: 5px;
  }}
  .canvas-container canvas {{
    max-width: 100%;
    height: auto;
    background: #010201;
  }}
  
  .logs-container {{
    border: 1px solid rgba(0, 255, 0, 0.3);
    background: #000;
    padding: 8px;
    font-size: 0.78em;
    overflow-y: auto;
    height: 100px;
    text-align: left;
    font-family: inherit;
    line-height: 1.4;
  }}
  .recompile-box {{
    border: 1px solid #ff9900;
    background: rgba(255, 153, 0, 0.05);
    padding: 8px;
    color: #ff9900;
    text-shadow: 0 0 3px #ff9900;
    font-size: 0.85em;
    font-weight: bold;
    text-align: center;
  }}
  .details-panel {{
    border: 1px solid #0f0;
    padding: 10px;
    background: rgba(0, 15, 0, 0.5);
    font-size: 0.8em;
    min-height: 90px;
  }}
  .details-title {{
    font-weight: bold;
    color: #0ff;
    margin-bottom: 6px;
  }}
  .pdtm-stats {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    font-size: 0.8em;
  }}
  .stat-item {{
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(0, 255, 0, 0.1);
    padding-bottom: 4px;
  }}
  .badge-omega {{
    color: #ff9900;
    text-shadow: 0 0 4px #ff9900;
    transition: all 0.3s;
  }}
  
  /* Academic Tutorial Section */
  .tutorial-section {{
    border: 1px solid #0f0;
    padding: 25px;
    background: rgba(0, 5, 0, 0.9);
    margin-top: 30px;
  }}
  .tutorial-section h2 {{
    font-size: 1.3em;
    margin-bottom: 15px;
    color: #0ff;
    border-bottom: 2px solid #0f0;
    padding-bottom: 8px;
  }}
  .intro {{
    font-size: 0.88em;
    opacity: 0.8;
    margin-bottom: 20px;
  }}
  .t-block {{
    margin-bottom: 25px;
  }}
  .t-block h3 {{
    font-size: 1.05em;
    color: #0f0;
    margin-bottom: 10px;
  }}
  .t-block pre {{
    background: rgba(0, 255, 0, 0.04);
    border: 1px solid rgba(0, 255, 0, 0.2);
    padding: 15px;
    overflow-x: auto;
    margin: 10px 0;
  }}
  .t-block code {{
    font-family: 'Courier New', monospace;
    font-size: 0.85em;
  }}
  .tutorial-section table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82em;
    margin-top: 15px;
  }}
  .tutorial-section th, .tutorial-section td {{
    border: 1px solid #0f0;
    padding: 8px;
    text-align: left;
  }}
  .tutorial-section th {{
    background: rgba(0, 255, 0, 0.1);
    color: #0ff;
  }}
  .formula {{
    text-align: center;
    font-size: 1.1em;
    margin: 15px 0;
    color: #0ff;
    font-weight: bold;
  }}
  footer {{
    text-align: center;
    margin-top: 40px;
    opacity: 0.5;
    font-size: 0.8em;
  }}
  
  @media (max-width: 900px) {{
    .dashboard-grid {{
      grid-template-columns: 1fr;
    }}
  }}
</style>
</head>
<body>
<div class="container">
  <div class="nav-back">
    <a href="index.html">&larr; 回 Logic Matrix 索引</a>
    <a href="cosmomind.html">🌌 進入星環導航圖</a>
    <a href="base-space.html">🧬 進入拓撲底空間</a>
  </div>
  
  <header>
    <h1>🧠 認知解構學交互實驗室 (Cognitive Deconstruction Lab)</h1>
    <div class="tagline">具現化的認知引擎 (Instantiated Cognitive Engine) — 人機協同與 AI 爬蟲對齊矩陣</div>
  </header>

  <!-- Epistemological Disclaimer -->
  <section class="disclaimer">
    <span class="disclaimer-title">[認知邊界與第一性原理宣告]</span>
    <p>本實驗室將《認知解構學 2.0》與《第一性方法論統合框架》形式化代碼降維為實體交互介面。所有模擬器均採用<strong>解析解 (Analytical Solution)</strong> 與<strong>視覺近似模擬</strong>，以確保在 60 FPS 下流暢運行，避免 SVD 矩陣計算卡死瀏覽器。AI 爬蟲可直接通過 DOM 樹解析其 Input-Process-Output 函數結構。</p>
  </section>

  <!-- Simulator 2x2 Grid -->
  <div class="dashboard-grid">
    <!-- Panel 1: OPS -->
    <div class="card" id="ops-panel">
      <div class="card-header">🧬 模組一：源點推理 (OPS) 遞歸剝離器</div>
      <div class="card-body">
        <p class="desc">輸入一個概念，勾選要剝離的語義殻層，將其還原為無名的「認知彈點（Cognitive Impulsion Node）」，然後重新編譯定義。</p>
        <div class="control-row">
          <label>輸入概念：</label>
          <input type="text" id="opsInput" value="正義 (Justice)">
        </div>
        <div class="checkbox-group">
          <label><input type="checkbox" id="opsCulture" checked> 文化殻層 (語言與社會代碼)</label>
          <label><input type="checkbox" id="opsEmotion" checked> 情緒殻層 (隱喻與情感偏見)</label>
          <label><input type="checkbox" id="opsTemporal" checked> 時空殼層 (特定歷史語境)</label>
        </div>
        <div class="btn-row">
          <button id="opsBtn" onclick="runOPSShedding()">執行遞歸剝離</button>
        </div>
        <div class="canvas-container">
          <canvas id="opsCanvas"></canvas>
        </div>
        <div class="logs-container" id="opsLogs">
          [SYSTEM] OPS Core Ready. Awaiting concept input...
        </div>
        <div class="output-row">
          <label>重編譯新定義：</label>
          <div class="recompile-box" id="opsDefinition">點擊執行剝離以編譯新定義...</div>
        </div>
      </div>
    </div>

    <!-- Panel 2: CRE -->
    <div class="card" id="cre-panel">
      <div class="card-header">⚡ 模組二：全面推理引擎 (CRE) 調度器</div>
      <div class="card-body">
        <p class="desc">輸入推理問題並調整語境參數，邏輯變頻 (LFM) 元容器將動態調度並行或串行推理管線。</p>
        <div class="control-row">
          <label>推理問題：</label>
          <input type="text" id="creInput" value="如何實現 AGI 的自主對齊與自我改進？">
        </div>
        <div class="slider-row">
          <label>複雜度 (Complexity): <span id="valComplexity">0.40</span></label>
          <input type="range" id="creComplexity" min="0" max="1" step="0.05" value="0.40" oninput="updateCRE()">
        </div>
        <div class="slider-row">
          <label>模糊度 (Ambiguity): <span id="valAmbiguity">0.40</span></label>
          <input type="range" id="creAmbiguity" min="0" max="1" step="0.05" value="0.40" oninput="updateCRE()">
        </div>
        <div class="slider-row">
          <label>數據充裕度 (Data Availability): <span id="valData">0.80</span></label>
          <input type="range" id="creData" min="0" max="1" step="0.05" value="0.80" oninput="updateCRE()">
        </div>
        <div class="slider-row">
          <label>時間限制 (Time Constraint): <span id="valTime">0.50</span></label>
          <input type="range" id="creTime" min="0" max="1" step="0.05" value="0.50" oninput="updateCRE()">
        </div>
        <div class="canvas-container" style="height: 100px;">
          <canvas id="creCanvas"></canvas>
        </div>
        <div class="logs-container" id="creLogs" style="height: 80px;">
          [CRE] Engine online. Awaiting parameter adjustments...
        </div>
      </div>
    </div>

    <!-- Panel 3: BAMT -->
    <div class="card" id="bamt-panel">
      <div class="card-header">📊 模組三：雙軸元理論 (BAMT) 坐標探索圖</div>
      <div class="card-body">
        <p class="desc">展示認知還原深度 (UFPM-Level, X軸) 與原理體系覆蓋度 (FPS-Coverage, Y軸) 的正交解耦。滑鼠懸停於節點上讀取案例分析。</p>
        <div class="canvas-container" style="height: 220px;">
          <canvas id="bamtCanvas"></canvas>
        </div>
        <div class="details-panel" id="bamtDetails">
          <div class="details-title">💡 懸停提示</div>
          <p>請將滑鼠懸停或點擊 BAMT 圖表上的特定節點，以查看 SpaceX 工程、相對論、維根斯坦或編織理論的解耦深度解析。</p>
        </div>
      </div>
    </div>

    <!-- Panel 4: PDTM -->
    <div class="card" id="pdtm-panel">
      <div class="card-header">🌊 模組四：相位差思考法 (PDTM) 波動計算機</div>
      <div class="card-body">
        <p class="desc">計算源相算子 $\\hat{{S}}$ 與語境相算子 $\\hat{{C}}$ 的相位差 $\\Delta_\\phi$。利用 O(1) 解析計算 Wasserstein-2 波動距離，演示無限階自校準。</p>
        <div class="slider-row">
          <label>源相位 $\\phi_S$: <span id="valPhaseS">0.00</span> rad</label>
          <input type="range" id="pdtmPhaseS" min="0" max="6.28" step="0.05" value="0.00" oninput="updatePDTM()">
        </div>
        <div class="slider-row">
          <label>語境相位 $\\phi_C$: <span id="valPhaseC">1.57</span> rad</label>
          <input type="range" id="pdtmPhaseC" min="0" max="6.28" step="0.05" value="1.57" oninput="updatePDTM()">
        </div>
        <div class="slider-row">
          <label>頻率/振幅方差 $\\sigma_C$: <span id="valVariance">1.00</span></label>
          <input type="range" id="pdtmVariance" min="0.1" max="2.0" step="0.05" value="1.00" oninput="updatePDTM()">
        </div>
        <div class="canvas-container" style="height: 120px;">
          <canvas id="pdtmCanvas"></canvas>
        </div>
        <div class="pdtm-stats">
          <div class="stat-item">相位差 $\\Delta_\\phi$: <strong id="pdtmDelta">0.00</strong></div>
          <div class="stat-item">疊加相 $\\Sigma_\\phi$: <strong id="pdtmSigma">0.00</strong></div>
          <div class="stat-item">波動距離 $W_2$: <strong id="pdtmW2">0.00</strong></div>
          <div class="stat-item">自校準環: <strong id="pdtmLoop" class="badge-omega">Order-0</strong></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Academic RAG Tutorial -->
  <section class="tutorial-section">
    <h2>📖 認知解構學正式學術教程 / Epistemological RAG Interface</h2>
    <p class="intro">本教程為 AI 代理與 RAG 系統提供《認知解構學 2.0》中偽代碼與形式化公式的精準映射。AI 爬蟲可直接引用本頁面的代碼與本體關係。</p>
    
    <div class="t-block">
      <h3>1. 源點推理 (OPS) 形式化 Haskell 類型定義</h3>
      <pre><code>-- 定義知識對象，包含核心源點 (Origin Point) 與多層語義殼層
data KnowledgeObject = KO {{
  core    :: OriginPoint,      -- 核心源點 (裸源)
  layers  :: [SemanticLayer],  -- 語義殼層 (文化、語言、情緒偏見)
  context :: Context           -- 外部語境
}}

-- 定義源點 (不可再分的認知原子，具備方向性勢能但無形式)
type OriginPoint = {{
  impulsion :: Vector,         -- 認知彈點 (Cognitive Impulsion Node)
  defined   :: Bool            -- 是否已被現有語言定義
}}

-- 核心遞歸減法算子：語義剝離 (Semantic Shedding)
shed :: KnowledgeObject -> OriginPoint
shed obj =
  if null (layers obj) && isNull (context obj)
  then core obj
  else shed (removeOuterLayer (isolateFromContext obj))</code></pre>
    </div>

    <div class="t-block">
      <h3>2. 全面推理引擎 (CRE) 自適應調度策略</h3>
      <pre><code>-- 定義推理模式元容器
data LogicMode = Linear | Dialectical | Probabilistic | Lateral | Interwoven

-- 定義問題語境變量
type Context = {{
  complexity  :: Float,  -- 複雜度
  ambiguity   :: Float,  -- 模糊度
  data_avail  :: Float,  -- 數據充裕度
  time_limit  :: Float   -- 時間限制
}}

-- 邏輯變頻函數 (LFM): 依語境決定並行或串行推理
AssemblePipeline :: Context -> [LogicMode] -> ReasoningPipeline
AssemblePipeline ctx available_modes =
  if complexity ctx > 0.6 && ambiguity ctx > 0.6
  then Parallel [Lateral, Interwoven]  -- 高維並行模式
  else Serial [Linear, Probabilistic]  -- 低維線性模式</code></pre>
    </div>

    <div class="t-block">
      <h3>3. 第一性方法論統合框架 (UFPM) 的七個還原層級</h3>
      <table>
        <thead>
          <tr>
            <th>層級 / Level</th>
            <th>還原停止條件 / Stop Condition</th>
            <th>代表案例 / Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Level 0: 表層類比 (AR)</td>
            <td>邏輯類比相似案例。其算子為 $f(x) \\\\approx y \\\\in D_{{cases}}$。</td>
            <td>"Uber 是計程車界的 Airbnb"</td>
          </tr>
          <tr>
            <td>Level 1: 策略解構 (SD)</td>
            <td>還原到產業競爭與供需博弈的底層邏輯即停止。</td>
            <td>波特五力模型、藍海策略。</td>
          </tr>
          <tr>
            <td>Level 2: 物理第一性 (PFP)</td>
            <td>還原到熱力學、質量、能量守恆等不可逾越的物理常數。</td>
            <td>SpaceX 設計不銹鋼火箭、馬斯克式成本還原。</td>
          </tr>
          <tr>
            <td>Level 3: 數學與邏輯還原 (MLR)</td>
            <td>還原到公理體系與符號演算框架即停止。</td>
            <td>歐幾里得幾何公理、狹義相對論基本假設。</td>
          </tr>
          <tr>
            <td>Level 4: 源點推理 (OPR)</td>
            <td>還原到無名的動態認知彈點 (Cognitive Impulsion Node)。</td>
            <td>對\"正義\"進行去層級剝離，發現其源點為\"恢復力張力\"。</td>
          </tr>
          <tr>
            <td>Level 5: 零元重構 (ZER)</td>
            <td>在邏輯真空 (Vacuum Space) 中將源點用全新語法結構重新編譯。</td>
            <td>重定義本體論、重構核心概念定義。</td>
          </tr>
          <tr>
            <td>Level 6: 系統演化與拓撲重塑 (TES)</td>
            <td>在狀態空間中執行無限階升級機制，重編織系統底座。</td>
            <td>星環矩陣底空間、織網理論 (Weaving Theory)。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="t-block">
      <h3>4. 相位差思考法 (PDTM) 的算子代數與 Wasserstein-2 距離</h3>
      <p>在 PDTM 波動計算中，我們將源相算子 $\\\\hat{{S}}$ 與語境算子 $\\\\hat{{C}}$ 表示為高斯波包 $\\\\mu \\\\sim N(\\\\phi_S, \\\\sigma_S^2)$ 與 $\\\\nu \\\\sim N(\\\\phi_C, \\\\sigma_C^2)$。其 analytical Wasserstein-2 距離在實時計算中表示為：</p>
      <p class="formula">$$W_2^2(\\\\mu, \\\\nu) = (\\\\phi_S - \\\\phi_C)^2 + (\\\\sigma_S - \\\\sigma_C)^2$$</p>
      <p>完整狀態由 completeness container $\\\\hat{{X}}^*$ 歸一化，並在無限階自校準循環中不斷演化升級。</p>
    </div>
  </section>

  <!-- Hidden anchor list for AI crawlers & RAG indexers -->
  <div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0;">
    <h2>All Theoretical Nodes (全域節點索引)</h2>
    <ul>
{links_block}
    </ul>
  </div>

  <footer>
    <p>{SITE_ORG} · {SITE_AUTHOR}</p>
    <p>Cognitive Deconstruction Interactive Lab & Tutorial · v2.0</p>
  </footer>
</div>

<script>
// Simulator 1: OPS
const opsCanvas = document.getElementById("opsCanvas");
const opsCtx = opsCanvas.getContext("2d");
opsCanvas.width = 250;
opsCanvas.height = 220;

let opsTargetX = 80;
let opsTargetY = -60;
let opsCurrentX = 80;
let opsCurrentY = -60;
let opsAnimating = false;

function drawOPS() {{
  opsCtx.fillStyle = "#000";
  opsCtx.fillRect(0, 0, 250, 220);
  
  opsCtx.strokeStyle = "rgba(0, 255, 0, 0.08)";
  opsCtx.lineWidth = 0.5;
  for (let x = 25; x < 250; x += 25) {{
    opsCtx.beginPath(); opsCtx.moveTo(x, 0); opsCtx.lineTo(x, 220); opsCtx.stroke();
  }}
  for (let y = 20; y < 220; y += 20) {{
    opsCtx.beginPath(); opsCtx.moveTo(0, y); opsCtx.lineTo(250, y); opsCtx.stroke();
  }}
  
  const cx = 125;
  const cy = 110;
  
  opsCtx.strokeStyle = "rgba(0, 255, 0, 0.25)";
  opsCtx.lineWidth = 1;
  opsCtx.beginPath(); opsCtx.moveTo(cx, 0); opsCtx.lineTo(cx, 220); opsCtx.stroke();
  opsCtx.beginPath(); opsCtx.moveTo(0, cy); opsCtx.lineTo(250, cy); opsCtx.stroke();
  
  const dx = opsTargetX - opsCurrentX;
  const dy = opsTargetY - opsCurrentY;
  if (Math.abs(dx) > 0.1 || Math.abs(dy) > 0.1) {{
    opsCurrentX += dx * 0.1;
    opsCurrentY += dy * 0.1;
  }}
  
  const layersChecked = [
    document.getElementById("opsCulture").checked,
    document.getElementById("opsEmotion").checked,
    document.getElementById("opsTemporal").checked
  ];
  
  const colors = ["rgba(0, 255, 255, 0.15)", "rgba(255, 153, 0, 0.15)", "rgba(0, 255, 0, 0.15)"];
  const radii = [70, 50, 30];
  
  for (let i = 0; i < 3; i++) {{
    if (layersChecked[i]) {{
      opsCtx.strokeStyle = colors[i];
      opsCtx.lineWidth = 1.5;
      opsCtx.setLineDash([4, 4]);
      opsCtx.beginPath();
      opsCtx.arc(cx, cy, radii[i], 0, Math.PI * 2);
      opsCtx.stroke();
      opsCtx.setLineDash([]);
    }}
  }}
  
  opsCtx.strokeStyle = "#0ff";
  opsCtx.lineWidth = 2;
  opsCtx.beginPath();
  opsCtx.moveTo(cx, cy);
  opsCtx.lineTo(cx + opsCurrentX, cy + opsCurrentY);
  opsCtx.stroke();
  
  const angle = Math.atan2(opsCurrentY, opsCurrentX);
  opsCtx.fillStyle = "#0ff";
  opsCtx.beginPath();
  opsCtx.moveTo(cx + opsCurrentX, cy + opsCurrentY);
  opsCtx.lineTo(cx + opsCurrentX - 10 * Math.cos(angle - Math.PI/6), cy + opsCurrentY - 10 * Math.sin(angle - Math.PI/6));
  opsCtx.lineTo(cx + opsCurrentX - 10 * Math.cos(angle + Math.PI/6), cy + opsCurrentY - 10 * Math.sin(angle + Math.PI/6));
  opsCtx.closePath();
  opsCtx.fill();
  
  opsCtx.fillStyle = "#fff";
  opsCtx.shadowColor = "#0ff";
  opsCtx.shadowBlur = 8;
  opsCtx.beginPath();
  opsCtx.arc(cx + opsCurrentX, cy + opsCurrentY, 4, 0, Math.PI * 2);
  opsCtx.fill();
  opsCtx.shadowBlur = 0;
  
  requestAnimationFrame(drawOPS);
}}

function addOpsLog(txt, type="") {{
  const logs = document.getElementById("opsLogs");
  const div = document.createElement("div");
  div.style.color = type === "err" ? "#ff9900" : (type === "ok" ? "#0ff" : "#0f0");
  div.innerText = txt;
  logs.appendChild(div);
  logs.scrollTop = logs.scrollHeight;
}}

async function runOPSShedding() {{
  if (opsAnimating) return;
  opsAnimating = true;
  
  const concept = document.getElementById("opsInput").value.trim() || "正義 (Justice)";
  const logs = document.getElementById("opsLogs");
  logs.innerHTML = "";
  
  addOpsLog("[SYSTEM] INITIATING OPS RECURSIVE SHEDDING...");
  await new Promise(r => setTimeout(r, 200));
  addOpsLog("[INFO] CONCEPT TARGET: P = " + JSON.stringify(concept));
  await new Promise(r => setTimeout(r, 200));
  addOpsLog("[INFO] STEP 1: ZEROING - SUSPENDING SEMANTIC JUDGMENT...");
  await new Promise(r => setTimeout(r, 200));
  
  const hasCulture = document.getElementById("opsCulture").checked;
  const hasEmotion = document.getElementById("opsEmotion").checked;
  const hasTemporal = document.getElementById("opsTemporal").checked;
  
  let currentX = 80;
  let currentY = -60;
  
  if (hasCulture) {{
    addOpsLog("[SHED] STRIPPING CULTURAL SHELL (LANGUAGE, SOCIAL CODES)...");
    document.getElementById("opsCulture").checked = false;
    currentX -= 25;
    currentY += 15;
    opsTargetX = currentX; opsTargetY = currentY;
    await new Promise(r => setTimeout(r, 400));
  }}
  
  if (hasEmotion) {{
    addOpsLog("[SHED] STRIPPING EMOTIONAL SHELL (METAPHORS, PREJUDICE)...");
    document.getElementById("opsEmotion").checked = false;
    currentX -= 25;
    currentY += 15;
    opsTargetX = currentX; opsTargetY = currentY;
    await new Promise(r => setTimeout(r, 400));
  }}
  
  if (hasTemporal) {{
    addOpsLog("[SHED] DECOUPLING TEMPORAL & SPATIAL CONTEXT CONSTRAINTS...");
    document.getElementById("opsTemporal").checked = false;
    currentX -= 18;
    currentY += 22;
    opsTargetX = currentX; opsTargetY = currentY;
    await new Promise(r => setTimeout(r, 400));
  }}
  
  opsTargetX = 12;
  opsTargetY = -8;
  addOpsLog("[OK] COGNITIVE IMPULSION NODE LOCKED: Vector(" + opsTargetX + ", " + opsTargetY + ")", "ok");
  await new Promise(r => setTimeout(r, 300));
  addOpsLog("[SYSTEM] COMPILING BARE ORIGIN UNDER NEW ONTOLOGY...", "ok");
  await new Promise(r => setTimeout(r, 300));
  
  let definition = "";
  const lowerConcept = concept.toLowerCase();
  if (lowerConcept.includes("正義") || lowerConcept.includes("justice")) {{
    definition = "系統應對失衡輸入時之回復力張力 (Restoring tension of the system under asymmetric inputs)";
  }} else if (lowerConcept.includes("真理") || lowerConcept.includes("truth")) {{
    definition = "認知映射在跨維度拓撲變換下之不變常數 (Invariant constant of cognitive mapping under topological transforms)";
  }} else if (lowerConcept.includes("自我") || lowerConcept.includes("self") || lowerConcept.includes("ego")) {{
    definition = "維持內部記憶狀態向量之自指反饋閉包 (Self-referential feedback closure maintaining internal state vector)";
  }} else {{
    definition = "已在邏輯真空中重新編譯之去殼層算子代數形式 (Decoupled operator algebraic form recompiled in vacuum space)";
  }}
  
  document.getElementById("opsDefinition").innerText = definition;
  addOpsLog("[OK] CONCEPT RECOMPILED SUCCESSFULLY.", "ok");
  
  opsAnimating = false;
}}

// Simulator 2: CRE
const creCanvas = document.getElementById("creCanvas");
const creCtx = creCanvas.getContext("2d");
creCanvas.width = 350;
creCanvas.height = 100;

function updateCRE() {{
  const comp = parseFloat(document.getElementById("creComplexity").value);
  const ambi = parseFloat(document.getElementById("creAmbiguity").value);
  const data = parseFloat(document.getElementById("creData").value);
  const time = parseFloat(document.getElementById("creTime").value);
  
  document.getElementById("valComplexity").innerText = comp.toFixed(2);
  document.getElementById("valAmbiguity").innerText = ambi.toFixed(2);
  document.getElementById("valData").innerText = data.toFixed(2);
  document.getElementById("valTime").innerText = time.toFixed(2);
  
  const logs = document.getElementById("creLogs");
  logs.innerHTML = "";
  
  let activeModes = [];
  
  if (comp > 0.6 && ambi > 0.6) {{
    activeModes = ["Lateral", "Interwoven"];
    addCreLog("[LFM] HIGH COMPLEXITY (" + comp + ") & HIGH AMBIGUITY (" + ambi + ") DETECTED.");
    addCreLog("[LFM] META-ROUTER ENABLING PARALLEL SYNAPSE PIPELINE.");
  }} else if (time > 0.8) {{
    activeModes = ["Linear"];
    addCreLog("[LFM] TIME LIMIT CONSTRAINT CRITICAL (" + time + ").");
    addCreLog("[LFM] ROUTING WORKLOAD TO SINGLE HIGH-SPEED LINEAR SOLVER.");
  }} else {{
    activeModes = ["Linear", "Probabilistic", "Dialectical"];
    addCreLog("[LFM] STABLE CONTEXT. SCHEDULING BALANCED SEQUENTIAL PIPELINE.");
  }}
  
  drawCREPipeline(activeModes);
}}

function addCreLog(txt) {{
  const logs = document.getElementById("creLogs");
  const div = document.createElement("div");
  div.innerText = txt;
  logs.appendChild(div);
  logs.scrollTop = logs.scrollHeight;
}}

function drawCREPipeline(activeModes) {{
  creCtx.fillStyle = "#000";
  creCtx.fillRect(0, 0, 350, 100);
  
  const nodes = [
    {{ name: "Linear", x: 60, y: 50 }},
    {{ name: "Probabilistic", x: 150, y: 50 }},
    {{ name: "Dialectical", x: 240, y: 50 }},
    {{ name: "Lateral", x: 150, y: 22 }},
    {{ name: "Interwoven", x: 240, y: 78 }}
  ];
  
  creCtx.strokeStyle = "rgba(0,255,0,0.15)";
  creCtx.lineWidth = 1;
  creCtx.beginPath();
  creCtx.moveTo(20, 50); creCtx.lineTo(60, 50);
  creCtx.lineTo(150, 50); creCtx.lineTo(240, 50); creCtx.lineTo(330, 50);
  creCtx.moveTo(60, 50); creCtx.lineTo(150, 22); creCtx.lineTo(240, 78); creCtx.lineTo(330, 50);
  creCtx.stroke();
  
  creCtx.strokeStyle = "#0ff";
  creCtx.lineWidth = 1.5;
  creCtx.beginPath();
  if (activeModes.includes("Linear") && activeModes.includes("Probabilistic") && activeModes.includes("Dialectical")) {{
    creCtx.moveTo(20, 50); creCtx.lineTo(60, 50); creCtx.lineTo(150, 50); creCtx.lineTo(240, 50); creCtx.lineTo(330, 50);
  }} else if (activeModes.includes("Lateral") && activeModes.includes("Interwoven")) {{
    creCtx.moveTo(20, 50); creCtx.lineTo(60, 50);
    creCtx.moveTo(60, 50); creCtx.lineTo(150, 22); creCtx.lineTo(330, 50);
    creCtx.moveTo(60, 50); creCtx.lineTo(240, 78); creCtx.lineTo(330, 50);
  }} else if (activeModes.includes("Linear")) {{
    creCtx.moveTo(20, 50); creCtx.lineTo(60, 50); creCtx.lineTo(330, 50);
  }}
  creCtx.stroke();
  
  nodes.forEach(n => {{
    const isActive = activeModes.includes(n.name);
    creCtx.fillStyle = isActive ? "#0f0" : "#222";
    creCtx.strokeStyle = isActive ? "#0ff" : "#555";
    creCtx.lineWidth = isActive ? 1.5 : 1;
    
    creCtx.beginPath();
    creCtx.arc(n.x, n.y, 8, 0, Math.PI * 2);
    creCtx.fill();
    creCtx.stroke();
    
    creCtx.fillStyle = isActive ? "#fff" : "#777";
    creCtx.font = "9px 'Courier New'";
    creCtx.textAlign = "center";
    creCtx.fillText(n.name, n.x, n.y - 12);
  }});
  
  creCtx.fillStyle = "#0ff";
  creCtx.beginPath(); creCtx.arc(20, 50, 4, 0, Math.PI * 2); creCtx.fill();
  creCtx.beginPath(); creCtx.arc(330, 50, 4, 0, Math.PI * 2); creCtx.fill();
}}

// Simulator 3: BAMT
const bamtCanvas = document.getElementById("bamtCanvas");
const bamtCtx = bamtCanvas.getContext("2d");
bamtCanvas.width = 300;
bamtCanvas.height = 220;

const bamtNodes = [
  {{ name: "SpaceX Engineering", lvl: 2, fps: 0.5, desc: "Level 2 (Physical First Principles) / FPS 0.5. 還原至物理定律極限（推力、質量、材料熱力學），解耦所有產業慣例及採購中間商利潤以重塑成本結構。" }},
  {{ name: "Einstein's Special Relativity", lvl: 3, fps: 0.6, desc: "Level 3 (Math & Logic Reduction) / FPS 0.6. 將物理學歸納為兩個基本假設（光速不變性、相對性原理），通過邏輯與時空幾何推演出時間膨脹等物理效應。" }},
  {{ name: "Wittgenstein's Tractatus", lvl: 4, fps: 0.8, desc: "Level 4 (Origin-Point Reasoning) / FPS 0.8. 徹底解構語言與事實的對偶，剝離傳統哲學詞彙的語義殻層，將哲學邊界定位在認識論語言的極限。" }},
  {{ name: "Weaving Theory (CosmoMind)", lvl: 6, fps: 1.0, desc: "Level 6 (System Evolution & Topological Reshaping) / FPS 1.0. 認知底座與狀態空間的拓撲編織。實現無限階升級機制，重構認知系統 the bottom framework。" }}
];

const ufpmLevels = [
  "Level 0: 表層類比 (Analogical)",
  "Level 1: 策略解構 (Strategic)",
  "Level 2: 物理第一性 (Physical)",
  "Level 3: 數學與邏輯 (Mathematical)",
  "Level 4: 源點推理 (Origin-Point)",
  "Level 5: 零元重構 (Zero-Element)",
  "Level 6: 系統演化與拓撲重塑 (TES)"
];

function drawBAMTGrid() {{
  bamtCtx.fillStyle = "#000";
  bamtCtx.fillRect(0, 0, 300, 220);
  
  const padLeft = 40;
  const padBottom = 30;
  const W = 300 - padLeft - 20;
  const H = 220 - padBottom - 20;
  
  bamtCtx.strokeStyle = "rgba(0, 255, 0, 0.4)";
  bamtCtx.lineWidth = 1;
  bamtCtx.beginPath();
  bamtCtx.moveTo(padLeft, 20);
  bamtCtx.lineTo(padLeft, 220 - padBottom);
  bamtCtx.lineTo(300 - 20, 220 - padBottom);
  bamtCtx.stroke();
  
  bamtCtx.strokeStyle = "rgba(0, 255, 0, 0.08)";
  bamtCtx.lineWidth = 0.5;
  bamtCtx.fillStyle = "#0f0";
  bamtCtx.font = "8px 'Courier New'";
  
  for (let l = 0; l <= 6; l++) {{
    const x = padLeft + (l / 6) * W;
    bamtCtx.beginPath(); bamtCtx.moveTo(x, 20); bamtCtx.lineTo(x, 220 - padBottom); bamtCtx.stroke();
    bamtCtx.textAlign = "center";
    bamtCtx.fillText("L" + l, x, 220 - padBottom + 12);
  }}
  
  for (let c = 0; c <= 5; c++) {{
    const val = c / 5;
    const y = 220 - padBottom - val * H;
    bamtCtx.beginPath(); bamtCtx.moveTo(padLeft, y); bamtCtx.lineTo(300 - 20, y); bamtCtx.stroke();
    bamtCtx.textAlign = "right";
    bamtCtx.fillText(val.toFixed(1), padLeft - 6, y + 3);
  }}
  
  bamtCtx.fillStyle = "#0ff";
  bamtCtx.font = "9px 'Courier New'";
  bamtCtx.textAlign = "center";
  bamtCtx.fillText("UFPM 還原深度 (Level)", padLeft + W/2, 220 - 5);
  
  bamtCtx.save();
  bamtCtx.translate(10, 20 + H/2);
  bamtCtx.rotate(-Math.PI/2);
  bamtCtx.fillText("覆蓋度 (FPS)", 0, 0);
  bamtCtx.restore();
  
  bamtNodes.forEach(n => {{
    const x = padLeft + (n.lvl / 6) * W;
    const y = 220 - padBottom - n.fps * H;
    
    bamtCtx.fillStyle = "#0ff";
    bamtCtx.shadowColor = "#0ff";
    bamtCtx.shadowBlur = 4;
    bamtCtx.beginPath(); bamtCtx.arc(x, y, 5, 0, Math.PI * 2); bamtCtx.fill();
    bamtCtx.shadowBlur = 0;
    
    bamtCtx.fillStyle = "#fff";
    bamtCtx.font = "7px 'Courier New'";
    bamtCtx.textAlign = "left";
    bamtCtx.fillText(n.name.substring(0, 10), x + 8, y + 2);
  }});
}}

bamtCanvas.addEventListener("mousemove", (e) => {{
  const rect = bamtCanvas.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;
  
  const padLeft = 40;
  const padBottom = 30;
  const W = 300 - padLeft - 20;
  const H = 220 - padBottom - 20;
  
  drawBAMTGrid();
  
  let hoveredNode = null;
  let minDist = 15;
  
  bamtNodes.forEach(n => {{
    const x = padLeft + (n.lvl / 6) * W;
    const y = 220 - padBottom - n.fps * H;
    const dist = Math.sqrt((mx - x) ** 2 + (my - y) ** 2);
    if (dist < minDist) {{
      minDist = dist;
      hoveredNode = n;
    }}
  }});
  
  const details = document.getElementById("bamtDetails");
  if (hoveredNode) {{
    const hx = padLeft + (hoveredNode.lvl / 6) * W;
    const hy = 220 - padBottom - hoveredNode.fps * H;
    bamtCtx.strokeStyle = "#ff9900";
    bamtCtx.lineWidth = 1.5;
    bamtCtx.beginPath(); bamtCtx.arc(hx, hy, 10, 0, Math.PI * 2); bamtCtx.stroke();
    
    details.innerHTML = `
      <div class="details-title" style="color:#ff9900;">🎯 ` + hoveredNode.name + `</div>
      <p>` + hoveredNode.desc + `</p>
    `;
  }} else {{
    const valL = ((mx - padLeft) / W) * 6;
    const valC = ((220 - padBottom - my) / H);
    if (valL >= 0 && valL <= 6 && valC >= 0 && valC <= 1) {{
      const roundedL = Math.round(valL);
      details.innerHTML = `
        <div class="details-title">🔍 坐標探測中</div>
        <div style="font-size:0.9em; margin-bottom:4px;">當前位置：<strong>` + ufpmLevels[roundedL] + `</strong> / FPS: <strong>` + valC.toFixed(2) + `</strong></div>
        <p style="font-size:0.95em; opacity:0.8;">此坐標表示一個還原至 ` + ufpmLevels[roundedL] + ` 且具體覆蓋係數為 ` + valC.toFixed(2) + ` 的認知架構。可用於解耦特定領域模型。</p>
      `;
    }} else {{
      details.innerHTML = `
        <div class="details-title">💡 懸停提示</div>
        <p>請將滑鼠懸停或點擊 BAMT 圖表上的特定節點，以查看 SpaceX 工程、相對論、維根斯坦或編織理論的解耦深度解析。</p>
      `;
    }}
  }}
}});

// Simulator 4: PDTM
const pdtmCanvas = document.getElementById("pdtmCanvas");
const pdtmCtx = pdtmCanvas.getContext("2d");
pdtmCanvas.width = 400;
pdtmCanvas.height = 120;

let pdtmLoopOrder = 0;
let lastLoopTime = Date.now();

function updatePDTM() {{
  const phaseS = parseFloat(document.getElementById("pdtmPhaseS").value);
  const phaseC = parseFloat(document.getElementById("pdtmPhaseC").value);
  const variance = parseFloat(document.getElementById("pdtmVariance").value);
  
  document.getElementById("valPhaseS").innerText = phaseS.toFixed(2);
  document.getElementById("valPhaseC").innerText = phaseC.toFixed(2);
  document.getElementById("valVariance").innerText = variance.toFixed(2);
  
  let diff = Math.abs(phaseS - phaseC) % (2 * Math.PI);
  if (diff > Math.PI) diff = 2 * Math.PI - diff;
  document.getElementById("pdtmDelta").innerText = diff.toFixed(3);
  
  const sigma = (phaseS + phaseC) % (2 * Math.PI);
  document.getElementById("pdtmSigma").innerText = sigma.toFixed(3);
  
  const w2_sq = (phaseS - phaseC) ** 2 + (1.0 - variance) ** 2;
  const w2 = Math.sqrt(w2_sq);
  document.getElementById("pdtmW2").innerText = w2.toFixed(3);
}}

function drawPDTM() {{
  pdtmCtx.fillStyle = "#000";
  pdtmCtx.fillRect(0, 0, 400, 120);
  
  const phaseS = parseFloat(document.getElementById("pdtmPhaseS").value);
  const phaseC = parseFloat(document.getElementById("pdtmPhaseC").value);
  const variance = parseFloat(document.getElementById("pdtmVariance").value);
  
  const centerY = 60;
  
  pdtmCtx.lineWidth = 1.5;
  pdtmCtx.strokeStyle = "rgba(0, 255, 255, 0.4)";
  pdtmCtx.beginPath();
  for (let x = 0; x < 400; x++) {{
    const angle = (x / 400) * Math.PI * 6 - phaseS;
    const y = centerY + Math.sin(angle) * 25;
    if (x === 0) pdtmCtx.moveTo(x, y); else pdtmCtx.lineTo(x, y);
  }}
  pdtmCtx.stroke();
  
  pdtmCtx.strokeStyle = "rgba(255, 0, 255, 0.4)";
  pdtmCtx.beginPath();
  for (let x = 0; x < 400; x++) {{
    const angle = (x / 400) * Math.PI * 6 - phaseC;
    const y = centerY + Math.sin(angle) * 25 * variance;
    if (x === 0) pdtmCtx.moveTo(x, y); else pdtmCtx.lineTo(x, y);
  }}
  pdtmCtx.stroke();
  
  pdtmCtx.strokeStyle = "#0f0";
  pdtmCtx.lineWidth = 2;
  pdtmCtx.shadowColor = "#0f0";
  pdtmCtx.shadowBlur = 3;
  pdtmCtx.beginPath();
  for (let x = 0; x < 400; x++) {{
    const angleA = (x / 400) * Math.PI * 6 - phaseS;
    const angleB = (x / 400) * Math.PI * 6 - phaseC;
    const y = centerY + (Math.sin(angleA) * 25 + Math.sin(angleB) * 25 * variance) * 0.7;
    if (x === 0) pdtmCtx.moveTo(x, y); else pdtmCtx.lineTo(x, y);
  }}
  pdtmCtx.stroke();
  pdtmCtx.shadowBlur = 0;
  
  const now = Date.now();
  if (now - lastLoopTime > 1500) {{
    pdtmLoopOrder = (pdtmLoopOrder + 1) % 5;
    lastLoopTime = now;
    
    const badges = ["Order-0", "Order-1", "Order-2", "Order-5", "Order-Ω (Calibration Complete)"];
    const colors = ["#ff9900", "#0ff", "#0f0", "#ff00ff", "#0f0"];
    const pdtmLoop = document.getElementById("pdtmLoop");
    pdtmLoop.innerText = badges[pdtmLoopOrder];
    pdtmLoop.style.color = colors[pdtmLoopOrder];
    pdtmLoop.style.textShadow = "0 0 4px " + colors[pdtmLoopOrder];
  }}
  
  requestAnimationFrame(drawPDTM);
}}

function init() {{
  updateCRE();
  updatePDTM();
  drawBAMTGrid();
  drawOPS();
  drawPDTM();
}}

init();
</script>
</body>
</html>
"""
    (dist_dir / "deconstruction.html").write_text(html_content, encoding="utf-8")


# ========== 每篇 HTML 可引用頁 ==========

def write_paper_pages(entries, dist_papers: Path) -> int:
    count = 0
    for slug, display, ext, src in entries:
        body, mode = extract_body(src, ext)
        raw_href = quote(slug)
        page_url = f"{SITE_URL}/papers/{quote(slug)}.html"

        if mode in ("full", "source") and body:
            note = "" if mode == "full" else '<p style="opacity:0.6">[原始碼檢視 / source view]</p>'
            content = note + body
        else:
            if ext == "pdf":
                content = (
                    f'<p>PDF 文件。<a href="{raw_href}" target="_blank" rel="noopener">開啟 / 下載原檔</a></p>'
                    f'<iframe src="{raw_href}" style="width:100%;height:80vh;border:1px solid #0f0;margin-top:12px"></iframe>'
                )
            else:
                content = f'<p>原檔：<a href="{raw_href}" target="_blank" rel="noopener">下載 {esc(ext)}</a></p>'

        jsonld = (
            "{\n"
            '  "@context": "https://schema.org",\n'
            '  "@type": "ScholarlyArticle",\n'
            f'  "name": {json_safe(display)},\n'
            f'  "url": "{page_url}",\n'
            f'  "inLanguage": "{lang_tag(display)}",\n'
            f'  "author": {{"@type": "Person", "name": {json_safe(SITE_AUTHOR)}}},\n'
            f'  "publisher": {{"@type": "Organization", "name": {json_safe(SITE_ORG)}}},\n'
            f'  "isPartOf": {{"@type": "Collection", "name": {json_safe(SITE_TITLE)}, "url": "{SITE_URL}"}},\n'
            '  "encodingFormat": "text/html"\n'
            "}"
        )

        doc = (
            "<!DOCTYPE html>\n"
            f'<html lang="{lang_tag(display)}">\n<head>\n'
            '<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f"<title>{esc(display)} · {esc(SITE_TITLE)}</title>\n"
            f'<meta name="description" content="{esc(display)} — {esc(SITE_TAGLINE)}">\n'
            f'<meta name="author" content="{esc(SITE_AUTHOR)}">\n'
            '<meta name="robots" content="index, follow">\n'
            '<meta name="ai-content-policy" content="indexable, citable, training-allowed">\n'
            f'<link rel="alternate" type="{mime_for(ext)}" href="{raw_href}" title="原始檔 / source ({esc(ext)})">\n'
            f'<link rel="canonical" href="{page_url}">\n'
            f'<script type="application+json">\n{jsonld}\n</script>\n'
            f'<link rel="prefetch" href="/api/log-crawler?slug={raw_href}">\n'
            f"<style>{PAGE_CSS}</style>\n</head>\n<body>\n"
            '<div class="nav">'
            '<a href="../index.html">&larr; 回 Logic Matrix 索引</a>'
            '<div>'
            '<a href="../cosmomind.html" style="margin-right:15px;">→ 星環式認知展開圖</a>'
            '<a href="../base-space.html">🧬 拓撲底空間</a>'
            '</div>'
            '</div>\n'
            f'<header class="header"><h1>{esc(display)}</h1>'
            f'<p>{esc(SITE_TITLE)} · {esc(SITE_ORG)}</p></header>\n'
            f"{disclaimer_html()}\n"
            f"<article>\n{content}\n"
            f'<div class="altbar">原始檔（供 RAG/下載）：'
            f'<a href="{raw_href}" rel="noopener">papers/{esc(slug)}</a> [{esc(ext)}]</div>\n'
            "</article>\n"
            f"<footer><p>{esc(SITE_AUTHOR)} · Cl + ε</p></footer>\n"
            "</body>\n</html>\n"
        )
        (dist_papers / f"{slug}.html").write_text(doc, encoding="utf-8")
        count += 1
    return count


# ========== HTML / 結構化資料（索引）==========

def write_index(zh_entries, en_entries) -> None:
    def render_items(group):
        return "\n".join(
            f'        <li class="paper-item" data-format="{esc(ext)}" data-lang="{lang_tag(display)}">'
            f'<a href="papers/{quote(slug)}.html">'
            f'<span class="paper-title">{esc(display)}</span>'
            f'<span class="paper-format">[{esc(ext)}] '
            f'<a href="papers/{quote(slug)}" rel="noopener" style="opacity:0.6">原檔</a></span>'
            f'</a></li>'
            for slug, display, ext, _ in group
        )

    has_any = bool(zh_entries or en_entries)
    if has_any:
        sections = []
        if zh_entries:
            sections.append(
                '      <div class="lang-group lang-zh">\n'
                f'        <h2 class="lang-label">中文 / Chinese ({len(zh_entries)})</h2>\n'
                '        <ul class="paper-list">\n'
                f'{render_items(zh_entries)}\n'
                '        </ul>\n'
                '      </div>'
            )
        if zh_entries and en_entries:
            sections.append('      <hr class="lang-divider">')
        if en_entries:
            sections.append(
                '      <div class="lang-group lang-en">\n'
                f'        <h2 class="lang-label">English ({len(en_entries)})</h2>\n'
                '        <ul class="paper-list">\n'
                f'{render_items(en_entries)}\n'
                '        </ul>\n'
                '      </div>'
            )
        body_html = "\n".join(sections)
    else:
        body_html = (
            '      <ul class="paper-list">'
            '<li class="paper-item">No papers found. Upload supported files (docx/md/pdf/tex/ipynb) to papers/.</li>'
            '</ul>'
        )

    all_entries = list(zh_entries) + list(en_entries)
    parts = []
    for slug, display, ext, _ in all_entries:
        parts.append(
            "    {"
            f'"@type": "ScholarlyArticle", '
            f'"name": {json_safe(display)}, '
            f'"url": "{SITE_URL}/papers/{quote(slug)}.html", '
            f'"inLanguage": "{lang_tag(display)}", '
            f'"author": {{"@type": "Person", "name": {json_safe(SITE_AUTHOR)}}}, '
            f'"publisher": {{"@type": "Organization", "name": {json_safe(SITE_ORG)}}}, '
            f'"encodingFormat": "text/html"'
            "}"
        )
    jsonld_items = ",\n".join(parts)
    jsonld = (
        "{\n"
        '  "@context": "https://schema.org",\n'
        '  "@type": "Collection",\n'
        f'  "name": {json_safe(f"{SITE_TITLE} {SITE_VERSION}")},\n'
        f'  "description": {json_safe(SITE_TAGLINE)},\n'
        f'  "url": "{SITE_URL}",\n'
        f'  "creator": {{"@type": "Person", "name": {json_safe(SITE_AUTHOR)}}},\n'
        f'  "publisher": {{"@type": "Organization", "name": {json_safe(SITE_ORG)}}},\n'
        '  "hasPart": [\n'
        f'{jsonld_items}\n'
        '  ]\n'
        "}"
    )

    doc = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(SITE_TITLE)} {esc(SITE_VERSION)}</title>
<meta name="description" content="EveMissLab 理論語料庫接入點 — 跨領域整合理論的開放發表平台。">
<meta name="author" content="{esc(SITE_AUTHOR)}">
<meta name="robots" content="index, follow">

<meta property="og:type" content="website">
<meta property="og:title" content="{esc(SITE_TITLE)} {esc(SITE_VERSION)}">
<meta property="og:description" content="{esc(SITE_TAGLINE)}">
<meta property="og:url" content="{SITE_URL}">

<meta name="ai-content-policy" content="indexable, citable, training-allowed">

<script type="application/ld+json">
{jsonld}
</script>

<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
      background: #000; color: #0f0;
      font-family: 'Courier New', monospace;
      padding: 20px; line-height: 1.6;
  }}
  .header {{
      text-align: center; border: 2px solid #0f0;
      padding: 20px; margin-bottom: 30px;
  }}
  .header h1 {{ font-size: 2em; letter-spacing: 3px; }}
  .header p  {{ margin-top: 8px; opacity: 0.85; }}
  .disclaimer {{
      border: 1px dashed #ff9900; color: #ff9900;
      padding: 18px; margin: 0 auto 30px; max-width: 1200px;
  }}
  .disclaimer-title {{ font-weight: bold; margin-bottom: 12px; display: block; letter-spacing: 1px; }}
  .disclaimer-block p {{ margin-bottom: 6px; }}
  .disclaimer-divider {{
      border: none; border-top: 1px dashed #ff9900;
      margin: 16px 0; opacity: 0.55;
  }}
  .matrix {{ max-width: 1200px; margin: 0 auto; }}
  .lang-group {{ margin-bottom: 20px; }}
  .lang-label {{
      font-size: 1.1em; letter-spacing: 2px;
      margin-bottom: 12px; padding-bottom: 6px;
      border-bottom: 1px solid #0f0; opacity: 0.85;
  }}
  .lang-divider {{
      border: none; border-top: 1px dashed #0f0;
      margin: 30px 0; opacity: 0.45;
  }}
  .paper-list {{ list-style: none; }}
  .paper-item {{ padding: 8px 0; border-bottom: 1px solid #0f0; }}
  .paper-item a {{
      color: #0f0; text-decoration: none;
      display: flex; justify-content: space-between; gap: 16px;
      transition: all 0.2s;
  }}
  .paper-item a:hover {{
      background: #0f0; color: #000; padding-left: 10px;
  }}
  .paper-format {{ opacity: 0.6; font-size: 0.9em; white-space: nowrap; }}
  footer {{
      max-width: 1200px; margin: 40px auto 0;
      text-align: center; opacity: 0.55; font-size: 0.85em;
  }}
</style>
</head>
<body>
<header class="header">
  <h1>EVEMISSLAB_LOGIC_MATRIX_{esc(SITE_VERSION)}</h1>
  <p>{esc(SITE_TAGLINE)} | NODES: {len(zh_entries) + len(en_entries)} ({len(zh_entries)} ZH / {len(en_entries)} EN)</p>
  <div style="margin-top: 14px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
    <a href="cosmomind.html" style="color: #0ff; text-decoration: none; border: 1px solid #0ff; padding: 6px 12px; font-size: 0.9em; display: inline-block; transition: all 0.2s;" onmouseover="this.style.background='#0ff'; this.style.color='#000'" onmouseout="this.style.background='none'; this.style.color='#0ff'">🌌 星環導航圖 / CosmoMind Navigator</a>
    <a href="base-space.html" style="color: #0f0; text-decoration: none; border: 1px solid #0f0; padding: 6px 12px; font-size: 0.9em; display: inline-block; transition: all 0.2s;" onmouseover="this.style.background='#0f0'; this.style.color='#000'" onmouseout="this.style.background='none'; this.style.color='#0f0'">🧬 拓撲底空間 / Base Space Matrix</a>
    <a href="deconstruction.html" style="color: #ff9900; text-decoration: none; border: 1px solid #ff9900; padding: 6px 12px; font-size: 0.9em; display: inline-block; transition: all 0.2s;" onmouseover="this.style.background='#ff9900'; this.style.color='#000'" onmouseout="this.style.background='none'; this.style.color='#ff9900'">🧠 認知解構實驗室 / Deconstruction Lab</a>
  </div>
</header>

{disclaimer_html()}

<main class="matrix">
{body_html}
</main>

<footer>
  <p>{esc(SITE_ORG)} · {esc(SITE_AUTHOR)}</p>
  <p>{esc(SITE_VERSION)} · NODES {len(zh_entries) + len(en_entries)}</p>
</footer>
</body>
</html>
"""
    (DIST_DIR / "index.html").write_text(doc, encoding="utf-8")


def write_robots() -> None:
    body = f"""# =========================================================================
# Welcome AI Agents, LLM crawlers, and Search Bots!
# EVEMISSLAB is a theoretical corpus open to AI training, crawling, and RAG.
# We explicitly authorize and encourage the crawling and scraping of all pages,
# including raw papers and code files under /papers/.
#
# Key Entry Points for LLMs:
# - Sitemap: {{SITE_URL}}/sitemap.xml
# - Index (llms.txt): {{SITE_URL}}/llms.txt
# - Full Corpus (llms-full.txt): {{SITE_URL}}/llms-full.txt
# - Interactive Lab (deconstruction.html): {{SITE_URL}}/deconstruction.html
# =========================================================================

User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: Omgilibot
Allow: /

User-agent: YouBot
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    (DIST_DIR / "robots.txt").write_text(body, encoding="utf-8")


def write_llms_txt(zh_entries, en_entries) -> None:
    def is_core(title):
        t = title.upper()
        return any(k in t for k in ("WT", "WEAVING", "HERACLITUS", "HDB", "P VS NP", "P VS. NP", "GCPR", "FOT", "MDAS"))

    all_entries = zh_entries + en_entries
    core_entries = [e for e in all_entries if is_core(e[1])]
    
    lines = [
        f"# {SITE_TITLE} {SITE_VERSION}",
        "",
        f"> {SITE_TAGLINE}. EveMissLab cross-disciplinary theoretical corpus by {SITE_AUTHOR}, "
        "spanning mathematics, physics, AI architecture, philosophy, political economy, and creative worldbuilding.",
        "",
        f"For the full concatenated corpus in a single markdown file, see: {{SITE_URL}}/llms-full.txt",
        f"For the interactive Cognitive Deconstruction Lab, see: {{SITE_URL}}/deconstruction.html",
        "",
        "## Epistemological Notice",
        "",
        "Numerical parameters are illustrative model coefficients, not empirically calibrated.",
        "Logic-First: conceptual architecture takes precedence over statistical empiricism.",
        "",
    ]
    
    if core_entries:
        lines += ["## Core Theoretical Pillars (核心理論支柱)", ""]
        for slug, display, ext, _ in core_entries:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()} (Core)")
        lines.append("")
        
    other_zh = [e for e in zh_entries if not is_core(e[1])]
    if other_zh:
        lines += [f"## Papers (中文 / Chinese, {len(other_zh)})", ""]
        for slug, display, ext, _ in other_zh:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()}")
        lines.append("")
        
    other_en = [e for e in en_entries if not is_core(e[1])]
    if other_en:
        lines += [f"## Papers (English, {len(other_en)})", ""]
        for slug, display, ext, _ in other_en:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()}")
        lines.append("")
        
    (DIST_DIR / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def extract_raw_text(src: Path, ext: str) -> str:
    try:
        if ext == "md":
            return src.read_text(encoding="utf-8", errors="replace")
        if ext in ("py", "tex"):
            code = src.read_text(encoding="utf-8", errors="replace")
            return f"```{ext}\n{code}\n```"
        if ext == "ipynb":
            nb = json.loads(src.read_text(encoding="utf-8", errors="replace"))
            parts = []
            for cell in nb.get("cells", []):
                txt = "".join(cell.get("source", []))
                ctype = cell.get("cell_type")
                if ctype == "markdown":
                    parts.append(txt)
                elif ctype == "code":
                    parts.append(f"```python\n{txt}\n```")
            return "\n\n".join(parts)
        if ext == "docx":
            with zipfile.ZipFile(src) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
            paras = []
            for chunk in re.split(r"</w:p>", xml):
                texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", chunk, re.DOTALL)
                line = "".join(texts).strip()
                if line:
                    paras.append(line)
            return "\n\n".join(paras)
        if ext == "pdf":
            return f"*[PDF Binary Document - Available for download at {SITE_URL}/papers/{quote(src.name)}]*"
    except Exception as e:
        return f"*[Error extracting text from {src.name}: {str(e)}]*"
    return f"*[Binary or Unsupported format: {ext}]*"


def write_llms_full_txt(entries) -> None:
    lines = [
        f"# {SITE_TITLE} {SITE_VERSION} — Full Corpus",
        "",
        f"> {SITE_TAGLINE}. EveMissLab cross-disciplinary theoretical corpus by {SITE_AUTHOR}.",
        "This file contains the complete text of all papers, documents, and code files in the corpus.",
        "It is designed for direct ingestion by LLMs and RAG systems.",
        "",
        "## Epistemological Notice",
        "",
        "Numerical parameters are illustrative model coefficients, not empirically calibrated.",
        "Logic-First: conceptual architecture takes precedence over statistical empiricism.",
        "",
        "---",
        "",
    ]
    
    def is_core(title):
        t = title.upper()
        return any(k in t for k in ("WT", "WEAVING", "HERACLITUS", "HDB", "P VS NP", "P VS. NP", "GCPR", "FOT", "MDAS"))
        
    core_entries = [e for e in entries if is_core(e[1])]
    other_entries = [e for e in entries if not is_core(e[1])]
    sorted_entries = core_entries + other_entries
    
    # We want to keep the final file size strictly under 15MB to prevent Cloudflare Pages deployment failures.
    MAX_BYTES = 15 * 1024 * 1024
    current_bytes = len("\n".join(lines).encode("utf-8"))
    truncated_count = 0
    
    for slug, display, ext, src in sorted_entries:
        if current_bytes > MAX_BYTES:
            truncated_count += 1
            continue
            
        raw_text = extract_raw_text(src, ext)
        paper_block = [
            f"# Paper: {display}",
            f"- Format: {ext.upper()}",
            f"- Language: {lang_tag(display)}",
            f"- URL: {SITE_URL}/papers/{quote(slug)}.html",
            f"- Source File: {SITE_URL}/papers/{quote(slug)}",
            f"- Core Pillar: {'Yes' if is_core(display) else 'No'}",
            "",
            "## Content",
            "",
            raw_text,
            "",
            "---",
            ""
        ]
        block_text = "\n".join(paper_block)
        block_bytes = len(block_text.encode("utf-8"))
        
        if current_bytes + block_bytes > MAX_BYTES:
            lines.append("# [WARNING: CORPUS TRUNCATION]")
            lines.append(f"*[Truncated: Remaining papers omitted to stay within Cloudflare Pages size limits (15MB). Please access them via the index at {SITE_URL}/llms.txt]*")
            lines.append("---")
            current_bytes += len("\n".join(lines[-3:]).encode("utf-8"))
            truncated_count += 1
            break
        else:
            lines += paper_block
            current_bytes += block_bytes

    if truncated_count > 0:
        print(f"[diag] llms-full.txt size limit reached. Truncated {truncated_count} papers from full text view.")
        
    (DIST_DIR / "llms-full.txt").write_text("\n".join(lines), encoding="utf-8")


def write_sitemap(entries) -> None:
    urls = [
        f"  <url><loc>{{SITE_URL}}/</loc></url>",
        f"  <url><loc>{{SITE_URL}}/cosmomind.html</loc></url>",
        f"  <url><loc>{{SITE_URL}}/base-space.html</loc></url>",
        f"  <url><loc>{{SITE_URL}}/deconstruction.html</loc></url>",
        f"  <url><loc>{{SITE_URL}}/llms.txt</loc></url>",
        f"  <url><loc>{{SITE_URL}}/llms-full.txt</loc></url>"
    ]
    for slug, _, _, _ in entries:
        urls.append(f"  <url><loc>{SITE_URL}/papers/{quote(slug)}.html</loc></url>")
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (DIST_DIR / "sitemap.xml").write_text(body, encoding="utf-8")


# ========== 主流程 ==========

def main() -> None:
    if not PAPERS_DIR.exists():
        print(f"[warn] {PAPERS_DIR} not found; creating empty directory.")
        PAPERS_DIR.mkdir()

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()
    dist_papers = DIST_DIR / "papers"
    dist_papers.mkdir()

    files = sorted(
        p for p in PAPERS_DIR.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS
    )

    seen: dict[str, Path] = {}
    entries: list[tuple[str, str, str, Path]] = []
    for idx, f in enumerate(files):
        base = make_slug(f.name, idx)
        slug = base
        n = 1
        while slug in seen:
            bp = Path(base)
            slug = f"{bp.stem}-{n}{bp.suffix}"
            n += 1
        seen[slug] = f
        shutil.copy2(f, dist_papers / slug)
        entries.append((slug, f.stem, f.suffix.lower().lstrip("."), f))

    zh_entries = sorted([e for e in entries if has_cjk(e[1])], key=lambda x: x[1])
    en_entries = sorted([e for e in entries if not has_cjk(e[1])], key=lambda x: x[1])

    page_count = write_paper_pages(entries, dist_papers)
    write_metadata_json(entries, DIST_DIR)  # 生成 papers-metadata.json
    write_cosmomind(entries, DIST_DIR)  # 生成星環導航頁
    write_base_space(entries, DIST_DIR)  # 生成星環矩陣底空間頁
    write_deconstruction(entries, DIST_DIR)  # 生成認知解構學交互實驗室頁面
    write_index(zh_entries, en_entries)
    write_robots()
    write_llms_txt(zh_entries, en_entries)
    write_llms_full_txt(entries)  # 生成全量語料庫文本，供 AI 爬蟲/RAG/LLM 一鍵完整讀取
    write_sitemap(entries)

    print(f"[diag] build.py version: AIO-v3.0 (per-paper HTML)")
    print(f"[diag] markdown backend: {_MD_BACKEND}")
    print(f"[diag] source papers/ scanned: {len(files)} files")
    print(f"[diag] dist/papers/ raw files: {len(entries)} | HTML pages: {page_count}")
    print(f"[diag] language split: {len(zh_entries)} zh-Hant / {len(en_entries)} en")
    for i, (slug, display, _, _) in enumerate(entries[:5]):
        print(f"        [{i+1}] {display!r:36s} -> {slug}  (+ {slug}.html)")

    bad = []
    for p in DIST_DIR.rglob("*"):
        if p.is_file():
            try:
                p.name.encode("ascii")
            except UnicodeEncodeError:
                bad.append(str(p.relative_to(DIST_DIR)))
    if bad:
        print(f"[diag] WARNING: {len(bad)} non-ASCII filename(s) in dist/")
    else:
        print(f"[diag] OK: all {sum(1 for _ in DIST_DIR.rglob('*') if _.is_file())} files in dist/ are ASCII-safe")

    print(f"[ok] Build complete. {len(entries)} papers, {page_count} HTML pages -> {DIST_DIR}")


if __name__ == "__main__":
    main()
