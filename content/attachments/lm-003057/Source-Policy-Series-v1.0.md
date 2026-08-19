# SOURCE_POLICY

1. 正式論文原稿以本 release 中 UTF-8 Markdown 為 canonical source。
2. 數學 delimiter 僅允許 `$...$` 與 `$$...$$`。
3. 不使用 LaTeX 的 parenthesis-style 或 bracket-style math delimiters 作為 canonical delimiter。
4. 不進行 unicode_escape round-trip。
5. 不把 Unicode 數學字元重新當成 LaTeX source。
6. Derived graph、embedding、摘要、HTML render 不得取代原始 source。
7. 所有正式輸出先 validate，再生成 checksum。
8. 任何 NS、P vs NP 或其他未解問題的內容，除非另有完整形式證明，不得由 corpus saturation 推論其真值、錯置或不可判定性。
