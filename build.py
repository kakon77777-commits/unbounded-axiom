import os
from pathlib import Path
import shutil

# 扫描 papers 文件夹
papers_dir = Path("papers")
if not papers_dir.exists():
    print("Warning: papers folder not found. Creating empty one.")
    papers_dir.mkdir()

# 收集所有文档
files = []
for ext in ["*.docx", "*.md"]:
    files.extend(papers_dir.glob(ext))

# 生成文件链接列表
links_html = ""
if files:
    for f in sorted(files):
        links_html += f'<div class="link"><a href="papers/{f.name}" target="_blank">{f.stem}</a></div>\n'
else:
    links_html = '<div class="link">No papers found. Upload .docx or .md files to papers/ folder.</div>'

# HTML 模板（加入认识论边界宣告）
html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EVEMISSLAB LOGIC MATRIX</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: #000;
            color: #0f0;
            font-family: 'Courier New', monospace;
            padding: 20px;
            line-height: 1.6;
        }}
        .header {{
            text-align: center;
            border: 2px solid #0f0;
            padding: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            font-size: 2em;
            letter-spacing: 3px;
        }}
        .disclaimer {{
            border: 1px dashed #ff9900;
            color: #ff9900;
            padding: 15px;
            margin-bottom: 30px;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }}
        .disclaimer-title {{
            font-weight: bold;
            margin-bottom: 10px;
            display: block;
        }}
        .matrix {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .link {{
            padding: 8px 0;
            border-bottom: 1px solid #0f0;
        }}
        .link a {{
            color: #0f0;
            text-decoration: none;
            display: block;
            transition: all 0.2s;
        }}
        .link a:hover {{
            background: #0f0;
            color: #000;
            padding-left: 10px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>EVEMISSLAB_LOGIC_MATRIX_V2.0</h1>
        <p>EveMissLab Theoretical Corpus Access Point | NODES: {len(files)}</p>
    </div>
    
    <div class="disclaimer">
        <span class="disclaimer-title">[SYSTEM EPISTEMOLOGICAL DISCLAIMER]</span>
        <b>[ENG]</b> The numerical data within these frameworks are <i>heuristically simulated</i> for structural verification. Do not treat them as empirical or physical measurements. This matrix operates strictly on a <b>Logic-First</b> principle, prioritizing conceptual architecture and causal mapping over statistical empiricism.<br><br>
        <b>[CHT]</b> 認識論邊界宣告：本矩陣內所有論文之公式數據均為「啟發式模擬數據」,僅用於驗證理論架構與推演因果鏈。請勿作為現實物理實證數據引用。EVEMISSLAB 奉行「邏輯先行」原則,本站理論全面以概念啟發與底層系統架構為主。
    </div>
    
    <div class="matrix">
        {links_html}
    </div>
</body>
</html>
"""

# 输出到 dist 文件夹
dist_dir = Path("dist")
dist_dir.mkdir(exist_ok=True)
(dist_dir / "index.html").write_text(html, encoding="utf-8")

# 复制 papers 文件夹到 dist
if papers_dir.exists() and any(papers_dir.iterdir()):
    shutil.copytree(papers_dir, dist_dir / "papers", dirs_exist_ok=True)

print("Success: Build completed")
