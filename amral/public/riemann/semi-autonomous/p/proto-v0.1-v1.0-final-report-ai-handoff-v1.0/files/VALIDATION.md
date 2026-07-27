# 最終整合驗證報告

## 結果

`PASS`

共 $11$ 類 final-synthesis checks，全部通過：

1. required files；
2. JSON parsing；
3. 十個 canonical source ZIP 的 SHA-256、CRC 與 internal manifest；
4. $82$ 份 canonical evidence snapshots；
5. $13$ 份前史／方法來源 hashes；
6. hard flags；
7. v0.1–v1.0 timeline；
8. claim/GAP semantics；
9. Markdown math delimiters；
10. report trust markers；
11. final release manifest。

機器報告位於：

`validation/final-validation.json`

## Canonical source 判定

十個 canonical ZIP 全部通過 internal manifest。Extracted v0.2 working tree 的 `outputs/gram_results.json` 曾被發現截斷，但 canonical ZIP 內檔案完整，因此不影響來源 archive 或本整合包的 evidence snapshots。

## 驗證命令

```bash
python3 validate_release.py --require-sources
```

單獨下載 final synthesis ZIP 時，可用：

```bash
python3 validate_release.py
```

後者驗證包內 manifest、snapshots 與 recorded canonical audit；前者另會即時重審全部外部來源檔。
