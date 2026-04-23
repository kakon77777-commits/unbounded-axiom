import os
from pathlib import Path

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

# HTML 模板
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
            margin-bottom: 40px;
        }}
        .header h1 {{
            font-size: 2em;
            letter-spacing: 3px;
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
        <p>EveMissLab Theoretical Corpus Access Point</p>
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
import shutil
if papers_dir.exists():
    shutil.copytree(papers_dir, dist_dir / "papers", dirs_exist_ok=True)

print("Success: Build completed")
