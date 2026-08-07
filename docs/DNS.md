# DNS — unboundedaxiom.org / unboundedaxiom.com

狀態記於 2026-08-07。

## 已完成（在 repo 裡，`wrangler deploy` 帶上去的）

五個主機名都由 `unbounded-axiom` Worker 服務。Worker 自訂網域**會自己建立 DNS
記錄**，所以這些不需要手動設 DNS：

| 主機名 | 行為 |
|---|---|
| `unboundedaxiom.org` | 正式站，200 |
| `unboundedaxiom.com` | 301 → `.org`，一跳，路徑保留 |
| `www.unboundedaxiom.org` | 301 → apex |
| `www.unboundedaxiom.com` | 301 → apex |
| `logic.evemisslab.com` | 301 → `.org`，**永久保留**，承載 2051 個已被引用的網址 |

要改就改 `wrangler.jsonc` 的 `routes`，不要在儀表板上動這些記錄 —— routes 區塊
在部署時是唯一真相，儀表板上有而這裡沒有的網域會被拔掉。

## 未完成：郵件冒用防護（需要 DNS 寫入權，部署用的權杖只有 `zone (read)`）

2026-08-07 掃過九個網域，**沒有一個有 DMARC**，七個連 SPF 都沒有。

一個沒有 SPF/DMARC 的網域可以被任何人冒名寄信。對一個「存在的目的就是成為
可歸屬、可引用的記錄」的網域來說，一封看起來來自它自己的偽造信，正好攻擊在
它要建立的那件事上。

### 不收發信的網域 — 可以直接設到最嚴，沒有風險

`unboundedaxiom.org`、`unboundedaxiom.com`、`evemiss.com`、
`efficientnewlanguage.org`、`commoninstant.org`、`thisoneisneok.com`、
`evemisstechnology.com`

```
類型   名稱      內容
TXT    @         v=spf1 -all
TXT    _dmarc    v=DMARC1; p=reject; rua=mailto:kakon77777@evemisslab.com; aspf=s; adkim=s
MX     @         0 .          ← RFC 7505 null MX：明確宣告「這裡不收信」
```

這三筆的意思分別是：沒有任何主機獲授權代表本網域寄信；違反者一律拒收；本網域
不接受郵件。三筆都不會影響網站。

### 已經在收信的網域 — 不要直接設 `p=reject`

| 網域 | 郵件 | 現有 SPF |
|---|---|---|
| `evemisslab.com` | Google Workspace | `v=spf1 include:_spf.google.com -all` |
| `agiright.org` | Cloudflare Email Routing | `v=spf1 include:_spf.mx.cloudflare.net ~all` |

SPF 保持不動，只加 DMARC，而且**先用 `p=none`**：

```
TXT    _dmarc    v=DMARC1; p=none; rua=mailto:kakon77777@evemisslab.com
```

`p=none` 只回報不攔截。收兩三週報告，確認沒有正當寄件被判為不合格（例如某個
服務代你寄信而不在 SPF 裡），再改成 `p=quarantine`，最後 `p=reject`。直接跳到
`reject` 會讓那些信**安靜地消失**，而你不會知道。

### CAA — 建議不要設

憑證目前由 Google Trust Services 簽發，但 Cloudflare 的 Universal SSL 會在不同
CA 之間輪替。一筆寫窄了的 CAA 會讓憑證**續簽失敗**，而失敗是安靜的，直到網站
某天憑證過期。這個情境下 CAA 的好處很小，壞掉的代價很大。
