# TCUE-SNS v0.1 Release Notes

## 封頂內容
- 11 篇 canonical Markdown 論文
- 每篇獨立 release artifacts
- 系列索引
- 理論依賴圖
- 主張強度分類
- 系列級驗證與 checksums

## 系列級重新驗證
Paper 01–11 已使用同一嚴格標準重新驗證：
- UTF-8 decode
- replacement character = 0
- canonical math delimiters
- display-math balance
- odd inline `$` scan
- Pandoc MathML parse
- **Pandoc stderr 必須為空**
- SHA-256 source fingerprint

## Canonical policy
單篇 canonical source 仍是各自的 `paper.md`。系列包只是 release container，不改寫各篇 source。
