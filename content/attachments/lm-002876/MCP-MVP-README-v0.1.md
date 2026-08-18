# SSSP MCP MVP v0.1

Structured Scholarly Source Protocol 的最小可跑原型。

## 目前包含

- `docs/SSSP_技術白皮書_v0.1.md`
- 純 Python SSSP core
- MCP 2025-11-25 stdio server（不依賴第三方 MCP SDK）
- 七個 tool primitives
- L1 結構/字元 validator
- MathJax L2 TeX validator（使用系統已安裝的 `mathjax-full`）
- revision + SHA-256 checksum
- atomic write
- Markdown exporter
- immutable version snapshots
- MCP smoke test

## 啟動

```bash
python3 src/mcp_server.py
```

Server 只在 stdout 輸出 MCP JSON-RPC；log 走 stderr。

## 執行測試

```bash
python3 tests/test_core.py
python3 tests/test_mcp_smoke.py
```

若系統有全域 `mathjax-full`，L2 validation 會啟用；否則會回報 warning 而不假裝已完成 render validation。

## 資料根目錄

預設：`./data`

可設定：

```bash
export SSSP_ROOT=/path/to/data
```

## 注意

v0.1 是研究 MVP，不是 production server。遠端 HTTP、authentication、完整 JSON Schema、完整交易、semantic LLM diff 留待後續版本。
