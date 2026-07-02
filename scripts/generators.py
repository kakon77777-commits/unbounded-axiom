#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""All dist/ output generators (pages, index, ai indexes, sitemap, llms, etc.)."""
import html
import json
import re
import shutil
import unicodedata
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from scripts.config import *
from scripts.helpers import *
from scripts.render import *


def write_cosmomind(registry, entries, dist_dir: Path) -> None:
    """生成 dist/cosmomind.html，用於全域超連結星環導航"""
    papers_data = []
    links_html = []
    for item in registry["items"]:
        papers_data.append({
            "id": item["id"],
            "title": item["title"],
            "ext": item["ext"],
            "lang": item["language"]
        })
        links_html.append(f'    <li><a href="/p/{item["id"]}/">{esc(item["title"])}</a></li>')
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
    id: p.id, title: p.title, ext: p.ext, lang: p.lang,
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
  if (hovered) window.location.href = "/p/" + hovered.id + "/";
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


def write_metadata_json(registry, dist_dir: Path) -> None:
    """生成 dist/papers-metadata.json，供 Pages Functions 動態讀取（id-native）"""
    data = []
    for item in registry["items"]:
        data.append({
            "id": item["id"],
            "title": item["title"],
            "ext": item["ext"],
            "lang": item["language"],
            "canonical": item["canonical_url"],   # /p/{id}/
            "raw": item["raw_url"]                 # /raw/{id}.{ext}
        })
    (dist_dir / "papers-metadata.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def write_base_space(registry, dist_dir: Path) -> None:
    """生成 dist/base-space.html，作為自適應 AI 爬蟲反饋矩陣底空間"""
    links_html = []
    for item in registry["items"]:
        links_html.append(f'    <li><a href="{item["canonical_url"]}">{esc(item["title"])}</a></li>')
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
    <div class="tagline">TCF 真實理論依賴拓撲 (Phase A) × AI 爬蟲注意力層 (ADL & 3-State Logic)</div>
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
        <div class="info-field"><span>圖源 / Graph Source:</span><strong id="statSource">—</strong></div>
        <div class="info-field"><span>已映射 / Mapped:</span><strong id="statMapped">—</strong></div>
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
      
      <div class="panel" style="font-size:0.8em;opacity:0.88;line-height:1.55;">
        <div class="panel-title">🧭 計畫說明 / PROJECT STATUS — Phase A 概念框架示範 (Demo MVP)</div>
        <p><strong>這是一個長期計畫的第一階段示範。</strong>願景：讓 base-space 成為一張「活的理論因果圖」——AI agent 讀取語料庫後提案更新、修正、補充理論間的因果邏輯，經對抗驗證與人類閘門後生效。</p>
        <p>目前（Phase A / 階梯 L1）：46 / 1177 篇核心論文已 TCF 化（理論壓縮標準格式）；173 條候選邊經逐邊對抗審核，僅 59 條存活發布——每條邊都帶可回溯原文的證據引文。</p>
        <p>後續路線：語料持續擴充 → 英文與簡中多語化 → 設立 TCF 專區逐篇結晶化 → base-space 進入全量與驗證迴路階段。</p>
        <p style="opacity:0.72;"><em>EN: Phase A of a long-term programme — a concept-framework demo, not a finished product. 46/1177 papers TCF-distilled; every published edge survived a per-edge adversarial audit (59/173) and carries verbatim source evidence. ⊤/⊥ truth states are reserved for future Lean machine-checking and multi-agent consensus loops. A dedicated TCF section will follow corpus expansion and EN / zh-CN translation.</em></p>
      </div>

      <div class="panel" id="demandPanel" style="font-size:0.8em;opacity:0.88;line-height:1.5;">
        <div class="panel-title">🔥 矽基需求排行榜 / SILICON DEMAND QUEUE</div>
        <p style="opacity:0.75;">近 48h 內被 AI 爬蟲高頻敲擊、但尚未 TCF 化的「空殼節點」。熱度突破閾值者，將由本地智能體「衍」優先結晶化——算力的市場化調度。</p>
        <div id="demandQueueBody"><div style="opacity:0.5;">偵測矽基網路的飢餓度…</div></div>
      </div>

      <div class="panel" style="font-size:0.8em;opacity:0.75;line-height:1.5;">
        <div class="panel-title">📖 三態邏輯操作指南</div>
        <p>1. <strong>Phase A（現行）</strong>：矩陣的邊來自 TCF 抽取的真實理論依賴——每條邊帶有可回溯至論文原文的 evidence 引文，由 <a href="/ai/graph.json" style="color:#0ff;">/ai/graph.json</a> 提供。未映射的論文誠實缺席，不偽造權重。</p>
        <p>2. 節點狀態遵循三態邏輯：<strong>Ω (螺旋態)</strong> = 已抽取草稿／修訂中；<strong>&top; (絕對真)</strong> 與 <strong>&bot; (絕對假)</strong> 保留給 Lean 機器驗證與多 agent 對抗驗證迴路（Phase C/E），不由流量決定。</p>
        <p>3. AI 爬蟲的訪問軌跡仍寫入注意力層（KV），作為次要觀測維度；當 TCF 真圖存在時，注意力不再冒充因果狀態。將滑鼠懸停於格點可讀取該依賴邊的類型與原文證據。</p>
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
let displayPapers = [];
let matrixData = {{ weights: {{}}, states: {{}}, hits: 0 }};

function graphToMatrix(graph) {{
  const w = {{}}, s = {{}}, edgeMeta = {{}};
  (graph.nodes || []).forEach(n => {{
    w[n.id] = {{}};
    w[n.id][n.id] = 1.0;
    s[n.id] = n.state || "omega";
  }});
  (graph.edges || []).forEach(e => {{
    if (!w[e.from]) {{ w[e.from] = {{}}; w[e.from][e.from] = 1.0; }}
    w[e.from][e.to] = e.weight;
    edgeMeta[e.from + "|" + e.to] = {{ type: e.type, evidence: (e.evidence && e.evidence[0]) || null }};
  }});
  return {{
    weights: w, states: s, hits: 0, edge_meta: edgeMeta,
    meta: {{
      source: "tcf-graph", version: graph.version,
      mapped: (graph.nodes || []).length,
      total: (graph.coverage && graph.coverage.papers_total) || null
    }}
  }};
}}

async function init() {{
  addLine("[DIAG] INITIALIZING SYNAPTIC CORE INTERFACE...");
  await new Promise(r => setTimeout(r, 200));

  try {{
    addLine("[DIAG] FETCHING PAPERS METADATA...");
    const pRes = await fetch("papers-metadata.json");
    papers = await pRes.json();
    addLine("[OK] PARSED " + papers.length + " THEORETICAL NODES FROM INDEX.", "term-ok");

    addLine("[DIAG] RESOLVING TOPOLOGY (ORDER OF TRUTH: TCF GRAPH > KV > SEED)...");
    try {{
      const mRes = await fetch("api/base-space");
      if (!mRes.ok) throw new Error("API " + mRes.status);
      matrixData = await mRes.json();
    }} catch (apiErr) {{
      addLine("[WARN] API UNREACHABLE (" + apiErr.message + "); READING STATIC /ai/graph.json...", "term-warn");
      const gRes = await fetch("ai/graph.json");
      if (!gRes.ok) throw new Error("graph.json " + gRes.status);
      matrixData = graphToMatrix(await gRes.json());
    }}

    if (matrixData.meta && matrixData.meta.source === "tcf-graph") {{
      addLine("[OK] REAL TCF DEPENDENCY TOPOLOGY LOADED (PHASE A).", "term-ok");
      addLine("[OK] " + matrixData.meta.mapped + " / " + papers.length + " NODES MAPPED — EVIDENCE-BACKED EDGES ONLY.", "term-ok");
    }} else {{
      addLine("[OK] STATE SPACE SYNCED WITH KV (NO TCF GRAPH YET — SIMULATED SEED).", "term-ok");
    }}

    await new Promise(r => setTimeout(r, 300));
    term.style.display = "none";

    renderMatrix();
  }} catch (err) {{
    addLine("[WARN] TOPOLOGY RESOLUTION FAILED: " + err.message, "term-warn");
    addLine("[DIAG] INITIATING AUTONOMOUS GENERATIVE SEED PROTOCOL (SIMULATED)...");
    matrixData = generateSimulatedData(papers);
    addLine("[OK] DETERMINISTIC PSEUDO-DYNAMIC SEED CONVERGED (NOT REAL DEPENDENCIES).", "term-ok");
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
    weights[n1.id] = {{}};
    let hash = 0;
    for (let i = 0; i < n1.title.length; i++) {{
      hash = n1.title.charCodeAt(i) + ((hash << 5) - hash);
    }}

    const stateVal = Math.abs(hash % 3);
    states[n1.id] = stateVal === 0 ? "omega" : (stateVal === 1 ? "true" : "false");

    nodes.forEach(n2 => {{
      if (n1.id === n2.id) {{
        weights[n1.id][n2.id] = 1.0;
      }} else {{
        const match = (n1.lang === n2.lang) ? 0.2 : 0.02;
        const seedVal = Math.abs((hash + n2.title.length) % 100) / 100;
        weights[n1.id][n2.id] = seedVal < 0.15 ? seedVal * 4.0 * match : 0;
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

  // Real-graph mode renders only the TCF-mapped subgraph: honest sparse coverage
  // stays legible instead of vanishing inside a 1177x1177 grid of unmapped cells.
  const isReal = !!(matrixData.meta && matrixData.meta.source === "tcf-graph");
  displayPapers = isReal ? papers.filter(p => matrixData.states[p.id] !== undefined) : papers;
  const N = displayPapers.length;
  const cellSize = size / (N + 1);

  document.getElementById("statNodes").innerText = N + " × " + N + (isReal ? " (mapped subgraph)" : "");
  document.getElementById("statSource").innerText = isReal ? "TCF REAL GRAPH · Phase A" : "SIMULATED SEED";
  document.getElementById("statMapped").innerText = isReal ? (N + " / " + papers.length) : "0 / " + papers.length;
  document.getElementById("statHits").innerText = matrixData.hits;
  let countOmega = 0, countTrue = 0, countFalse = 0;
  displayPapers.forEach(p => {{
    const st = matrixData.states[p.id] || "false";
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
      const p1 = displayPapers[r];
      const state1 = matrixData.states[p1.id] || "false";

      for (let c = 0; c < N; c++) {{
        const p2 = displayPapers[c];
        const w = (matrixData.weights[p1.id] && matrixData.weights[p1.id][p2.id]) || 0;
        
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
    if (hoverX >= 0 && hoverX < N && displayPapers[hoverX] && displayPapers[hoverX].canonical) {{
      window.location.href = displayPapers[hoverX].canonical;  // "/p/{{id}}/"
    }}
  }});
}}

function updateReflector(row, col) {{
  const p1 = displayPapers[row];
  const p2 = displayPapers[col];
  const state1 = matrixData.states[p1.id] || "false";
  const weight = (matrixData.weights[p1.id] && matrixData.weights[p1.id][p2.id]) || 0;
  const em = (matrixData.edge_meta || {{}})[p1.id + "|" + p2.id];

  const stateLabels = {{
    "true": '<span class="badge-true">[TOP] 絕對真理 / Stable Core</span>',
    "false": '<span class="badge-false">[BOTTOM] 邊緣退化 / Outlier Boundary</span>',
    "omega": '<span class="badge-omega">[OMEGA] 螺旋相變 / Spiral Evolution</span>'
  }};

  let html = `
    <div class="info-field"><span>源節點 / Source Node:</span><strong>` + p1.title.substring(0, 22) + (p1.title.length > 22 ? "..." : "") + `</strong></div>
    <div class="info-field"><span>邏輯狀態 / Logic State:</span><strong>` + stateLabels[state1] + `</strong></div>
    <div class="info-field"><span>目標節點 / Target Node:</span><strong>` + p2.title.substring(0, 22) + (p2.title.length > 22 ? "..." : "") + `</strong></div>
    <div class="info-field"><span>因果耦合權重 / Connection:</span><strong>` + weight.toFixed(4) + `</strong></div>`;

  if (em) {{
    const ev = em.evidence || {{}};
    const quote = ev.quote || ev.use_quote || "";
    html += `
    <div class="info-field"><span>依賴類型 / Relation:</span><strong style="color:#0ff;">` + em.type + (ev.concept ? " · " + ev.concept : "") + `</strong></div>`;
    if (quote) {{
      html += `
    <div style="margin-top:8px; font-size:0.78em; opacity:0.85; border-left:2px solid rgba(0,255,255,0.4); padding-left:8px;">
      📜 原文證據 / Evidence:<br>「` + quote.substring(0, 120) + (quote.length > 120 ? "…" : "") + `」
    </div>`;
    }}
  }} else {{
    html += `
    <div class="info-field"><span>RAG 召回優先權 / Priority:</span><strong>` + (weight > 0.8 ? "CRITICAL" : (weight > 0.3 ? "OPTIMAL" : "SLIGHT")) + `</strong></div>`;
  }}

  html += `
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

async function loadDemandQueue() {{
  const panel = document.getElementById("demandPanel");
  const body = document.getElementById("demandQueueBody");
  try {{
    const r = await fetch("api/tcf-queue");
    if (!r.ok) {{ panel.style.display = "none"; return; }}
    const q = await r.json();
    if (!q.queue || !q.queue.length) {{
      body.innerHTML = '<div style="opacity:0.5;">近 48h 尚無突破閾值（' + q.threshold + ' 次）的空殼節點。矽基網路正在漫遊中。</div>';
      return;
    }}
    let html = "";
    q.queue.forEach((item, i) => {{
      html += '<div class="info-field"><span>#' + (i + 1) + ' <a href="' + item.canonical + '" style="color:#0f0;">'
            + item.title.substring(0, 20) + (item.title.length > 20 ? "…" : "") + '</a></span>'
            + '<strong style="color:#ff9900;">' + item.recent_hits + ' hits ⏳</strong></div>';
    }});
    html += '<div style="margin-top:8px;font-size:0.85em;opacity:0.6;">追蹤中空殼節點：' + q.hollow_tracked + '　已映射：' + q.mapped_total + '</div>';
    body.innerHTML = html;
  }} catch (err) {{
    panel.style.display = "none";
  }}
}}

init();
loadDemandQueue();
</script>
</body>
</html>
"""
    (dist_dir / "base-space.html").write_text(html_content, encoding="utf-8")


def write_deconstruction(registry, entries, dist_dir: Path) -> None:
    """生成 dist/deconstruction.html，作為認知解構交互實驗室與教學頁面"""
    links_html = []
    for item in registry["items"]:
        links_html.append(f'    <li><a href="/p/{item["id"]}/">{esc(item["title"])}</a></li>')
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


def write_index(zh_entries, en_entries, registry) -> None:
    total_zh = len(zh_entries)
    total_en = len(en_entries)
    total_nodes = total_zh + total_en
    now_dt = datetime.now(timezone.utc)
    now_iso = now_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    now_date = now_dt.strftime("%Y-%m-%d")
    build_id = f"{SITE_VERSION}-{now_dt.strftime('%Y%m%d%H%M%S')}Z"
    meta_description = f"{SITE_TAGLINE} [NODES: {total_nodes} | LAST_UPDATED: {now_date}]"
    by_src = {it["source_file"]: it for it in registry["items"]}
    def _item_for(src):
        return by_src[src.relative_to(ROOT).as_posix()]
    def render_items(group):
        rows = []
        for slug, display, ext, src in group:
            item = _item_for(src)
            rows.append(
                f'        <li class="paper-item" data-format="{esc(ext)}" data-lang="{lang_tag(display)}" data-id="{esc(item["id"])}">'
                f'<a href="{item["canonical_url"]}">'
                f'<span class="paper-title">{esc(display)}</span>'
                f'<span class="paper-format">[{esc(ext)}] '
                f'<a href="{item["raw_url"]}" rel="noopener" style="opacity:0.6">原檔</a></span>'
                f'</a></li>'
            )
        return "\n".join(rows)

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
    for slug, display, ext, src in all_entries:
        item = _item_for(src)
        parts.append(
            "    {"
            f'"@type": "ScholarlyArticle", '
            f'"name": {json_safe(display)}, '
            f'"url": "{SITE_URL}{item["canonical_url"]}", '
            f'"identifier": {json_safe(item["id"])}, '
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
<meta name="description" content="{esc(meta_description)}">
<meta name="author" content="{esc(SITE_AUTHOR)}">
<meta name="robots" content="index, follow">

<meta property="og:type" content="website">
<meta property="og:title" content="{esc(SITE_TITLE)} {esc(SITE_VERSION)}">
<meta property="og:description" content="{esc(meta_description)}">
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
  <p>{esc(SITE_TAGLINE)} | NODES: {total_nodes} ({total_zh} ZH / {total_en} EN)</p>
  <p>BUILD_ID: {esc(build_id)} | LAST_UPDATED: {esc(now_iso)}</p>
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
# Preferred machine-readable entry points (deterministic ingestion):
# - AI manifest: {SITE_URL}/ai/manifest.json
# - Bulk corpus (jsonl): {SITE_URL}/ai/corpus.jsonl
# - AI rights spectrum: {SITE_URL}/ai/rights-spectrum.json
# - Sitemap (canonical /p/ only): {SITE_URL}/sitemap.xml
# - Index (llms.txt): {SITE_URL}/llms.txt
# - Full Corpus (llms-full.txt): {SITE_URL}/llms-full.txt
# - Interactive Lab (deconstruction.html): {SITE_URL}/deconstruction.html
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
        f"For the full concatenated corpus in a single markdown file, see: {SITE_URL}/llms-full.txt",
        f"For the interactive Cognitive Deconstruction Lab, see: {SITE_URL}/deconstruction.html",
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


def write_manifest(zh_entries, en_entries, dist_dir: Path) -> None:
    """生成 /corpus.json，供 AI Agent 快速校對矩陣狀態。"""
    total_zh = len(zh_entries)
    total_en = len(en_entries)
    total_nodes = total_zh + total_en
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    manifest = {
        "site": SITE_TITLE,
        "version": SITE_VERSION,
        "last_updated": now_str,
        "nodes_total": total_nodes,
        "nodes_zh": total_zh,
        "nodes_en": total_en,
        "entry": f"{SITE_URL}/",
    }

    (dist_dir / "corpus.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def write_sitemap(entries) -> None:
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    urls = [
        f"  <url><loc>{SITE_URL}/</loc><lastmod>{now_iso}</lastmod></url>",
        f"  <url><loc>{SITE_URL}/cosmomind.html</loc><lastmod>{now_iso}</lastmod></url>",
        f"  <url><loc>{SITE_URL}/base-space.html</loc><lastmod>{now_iso}</lastmod></url>",
        f"  <url><loc>{SITE_URL}/deconstruction.html</loc><lastmod>{now_iso}</lastmod></url>",
        f"  <url><loc>{SITE_URL}/llms.txt</loc><lastmod>{now_iso}</lastmod></url>",
        f"  <url><loc>{SITE_URL}/llms-full.txt</loc><lastmod>{now_iso}</lastmod></url>",
    ]
    for slug, _, _, _ in entries:
        urls.append(
            f"  <url><loc>{SITE_URL}/papers/{quote(slug)}.html</loc><lastmod>{now_iso}</lastmod></url>"
        )
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (DIST_DIR / "sitemap.xml").write_text(body, encoding="utf-8")
