# RH-W-19 工程包 v0.1

主題：可重現性、對抗性審計與錯誤證書動物園。

## 執行

```bash
python rhcert.py verify
python redteam_zoo.py
python rhcert.py verify --record RH-W-19
```

## 重要狀態

- 16 類錯誤預期被拒絕；
- 1 類 verifier／certificate 串通攻擊預期存活；
- 預期存活不是成功驗證，而是外部信任根缺口；
- `RH_CLAIM=False`。
