# DNS — unboundedaxiom.org / unboundedaxiom.com

狀態記於 2026-08-07。

## 主機名（在 repo 裡，`wrangler deploy` 帶上去的）

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

## 郵件冒用防護 — 2026-08-07 完成，14 個 zone 全部

之前的狀態是：**十四個 zone 沒有一個有 DMARC，十二個連 SPF 都沒有。** 一個
沒有 SPF/DMARC 的網域可以被任何人冒名寄信，而對一個「存在的目的就是成為可歸屬、
可引用的記錄」的網域來說，一封看起來來自它自己的偽造信，正好攻擊在它要建立的
那件事上。

**清單是從帳號掃出來的，不是手打的。** 手打的那一版是九個，帳號裡實際有十四個。

### 十二個不收信的 zone

`asiright.org`、`commoninstant.org`、`efficientnewlanguage.org`、
`emlphosphor.com`、`eveglypheditor.com`、`evemiss.com`、`evemisstechnology.com`、
`httpefficientnewlanguage.org`、`thisoneisneok.com`、`unboundedaxiom.com`、
`unboundedaxiom.org`、`一言諾科技有限公司.tw`

```
TXT  @         v=spf1 -all
TXT  _dmarc    v=DMARC1; p=reject; rua=mailto:kakon77777@evemisslab.com; aspf=s; adkim=s; fo=1
MX   @   0 .   ← RFC 7505 null MX：明確宣告「這裡不收信」
```

### 兩個在收信的 zone — 只加 DMARC，SPF 與 MX 一個字沒動

| zone | 郵件 | SPF（保持不動） | DMARC |
|---|---|---|---|
| `evemisslab.com` | Google Workspace，5 筆 MX | `v=spf1 include:_spf.google.com -all` | `p=none` |
| `agiright.org` | Cloudflare Email Routing，3 筆 MX | `v=spf1 include:_spf.mx.cloudflare.net ~all` | `p=none` |

**`p=none` 是刻意的，不是偷懶。** 直接跳到 `p=reject`，任何不在 SPF 裡的正當
寄件會在收件端**安靜消失** —— 那是你不會發現的失敗。`p=none` 什麼都不擋，只
產生報告。收兩三週，確認沒有正當寄件被判不合格，再依序改成 `p=quarantine`、
`p=reject`。

### 跨網域報告授權（否則 `rua=` 是裝飾品）

DMARC 報告要寄到**別的網域**的信箱，需要接收端明示同意。所以
`evemisslab.com` 上另外建了 13 筆：

```
TXT  <zone>._report._dmarc.evemisslab.com    v=DMARC1
```

沒有這些，上面每一個 `rua=mailto:kakon77777@evemisslab.com` 都不會有報告寄出。

### 驗證方式

寫入後**用公開 DNS（DoH）重驗，不是用剛才寫入的那個 API**。API 只能確認「送出
了什麼」；解析才能確認「世界看到什麼」—— 寫入可能落在不是正在應答的那個 zone 上，
記錄也可能還沒傳播。

最要緊的一項：**null MX 對一個真的在收信的網域會讓投遞停掉。** 所以
`dns_apply.py` 在寫入前會**當場重讀該 zone 的 MX**（不信任稽核當時的快照），
有任何真實 MX 就跳過；`dns_verify.py` 則另外斷言那兩個郵件網域仍有 3 筆與 5 筆
真實 MX、且**沒有**多出 null MX。

## CAA — 建議不要設

憑證目前由 Google Trust Services 簽發，但 Cloudflare 的 Universal SSL 會在不同
CA 之間輪替。一筆寫窄了的 CAA 會讓憑證**續簽失敗**，而失敗是安靜的，直到網站
某天憑證過期。這個情境下 CAA 的好處很小，壞掉的代價很大。

## 之後要做的

`p=none` 的那兩個 zone 收兩三週報告後收緊。除此之外沒有待辦。
