import os
import shutil

# 設定目錄
SOURCE_DIR = 'papers'
DIST_DIR = 'dist'

def build_site():
    # 建立或清空輸出目錄
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)
    
    # 複製論文檔案到輸出目錄
    shutil.copytree(SOURCE_DIR, os.path.join(DIST_DIR, 'papers'))
    
    links = []
    files = sorted(os.listdir(SOURCE_DIR))
    
    for i, filename in enumerate(files, 1):
        if filename.endswith('.md'):
            filepath = os.path.join(SOURCE_DIR, filename)
            
            # 讀取標題 (讀取第一行)
            title = filename
            with open(filepath, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                if first_line.startswith('#'):
                    title = first_line.replace('#', '').strip()
            
            # 生成超連結 (數字 + 標題)
            link = f'<div>{i}. <a href="papers/{filename}">{title}</a></div>'
            links.append(link)

    # 寫入最終的 index.html
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="robots" content="noindex">
        <title>EveMissLab Logic Matrix</title>
        <style>
            body {{ font-family: monospace; background: #000; color: #0f0; padding: 20px; }}
            a {{ color: #0f0; text-decoration: none; }}
            a:hover {{ background: #0f0; color: #000; }}
            div {{ margin-bottom: 5px; }}
        </style>
    </head>
    <body>
        <pre>EVEMISSLAB_LOGIC_MATRIX_V2.0</pre>
        <hr>
        {''.join(links)}
    </body>
    </html>
    """
    
    with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    build_site()