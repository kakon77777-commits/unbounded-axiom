#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corpus Engine configuration constants."""
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "content" / "papers"
DIST_DIR = ROOT / "dist"

# 【修正一】全面開放 .py 進入掃描防區
SUPPORTED_EXTS = {".docx", ".md", ".pdf", ".tex", ".ipynb", ".py", ".lean", ".ts", ".jsx"}

SITE_TITLE   = "EVEMISSLAB Logic Matrix"
SITE_VERSION = "V2.1"
SITE_TAGLINE = "EveMissLab Theoretical Corpus Access Point"
SITE_URL     = "https://logic.evemisslab.com"   # ← 完美鎖定主權網域
SITE_AUTHOR  = "Neo.K (許筌崴)"
SITE_ORG     = "EveMissLab / 一言諾科技有限公司"


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
