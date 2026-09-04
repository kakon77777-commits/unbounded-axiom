# IQRC-02｜從發展合法性到努力—回報斷裂：新中國的流動性、相對剝奪與 AI 變數

**English Title:** *From Developmental Legitimacy to Effort–Reward Fracture: Mobility, Relative Deprivation, and the AI Variable in the People’s Republic of China*  
**系列：**《制度智能、類全域 AI 與可重開文明系列》  
**Series:** *Institutional Intelligence, Quasi-Global AI, and Reopenable Civilization Series*  
**篇次：** Paper 02 / 08  
**文件編號：** EML-IQRC-02-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 中國政治經濟／發展合法性／社會流動／相對剝奪／AI 政治經濟學  
**狀態：** Canonical Draft / China Historical Stress-Test  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

理解當代中國的政治穩定、社會壓力與未來制度路徑，不能只問「中國人是否比以前更富」「不平等是否增加」「GDP 是否放緩」或「人民是否支持現行制度」。1949 年後的中國經歷了國家重建、計畫動員、大躍進與大饑荒、文化大革命、中美關係轉向、改革開放、高速工業化與城市化、教育擴張、房地產資產化、數位化，以及目前正在加速的人工智慧與具身智能部署。不同歷史階段中，相同程度的不平等、工作負擔或政治限制，可能產生完全不同的主觀與政治效果。

本文提出：中國改革開放後長期穩定的一個重要機制，不只是生活水準提高，而是形成了相當可信的「努力—改善—流動」發展敘事。即使工作時間長、收入差距擴張、城鄉與階級差異存在，只要大量個體仍觀察到家庭生活改善、教育機會增加、城市與產業擴張、職業階梯打開，且相信自身或下一代仍可能向上流動，則他人的成功可以被解讀為「前方通道正在打開」而非純粹剝奪。這與 Hirschman–Rothschild 的 tunnel effect 相容，也與中國社會流動研究中「絕對上升機會增加、但相對競爭逐漸僵化」的雙重現象相容。

本文因此將傳統相對剝奪擴充為多參照、動態模型：

$$
\boxed{
D_{i,t}
=
f(
P_{i,t}^{past},
P_{i,t}^{promise},
P_{i,t}^{peer},
P_{i,t}^{elite},
P_{i,t}^{foreign},
P_{i,t}^{future}
).
}
$$

更重要的是加入「努力—回報彈性」：

$$
\boxed{
\varepsilon_{ER,i,t}
=
\frac{
\partial
\mathbb E[
\Delta Position_{i,t+1}
]
}{
\partial Effort_{i,t}
}.
}
$$

若個體即使處境不佳，仍相信：

$$
\varepsilon_{ER,i,t}>0,
$$

高負擔可以被理解為有代價但仍值得的投資；若：

$$
\varepsilon_{ER,i,t}\rightarrow0,
$$

則「很累但有用」可能轉為「很累而且不知道還有沒有用」。此時躺平、降低投資、延後婚育、減少消費、退出競爭或重新評估制度，不必被簡化為怠惰或情緒異常，而可能是對預期邊際回報下降的適應。

本文同時修正早期「中國崩潰」式強預測。相對剝奪與流動性下降本身不會直接推出政權失敗。政治效果仍受到因果歸因、家庭與社會緩衝、民族與外部競爭敘事、行政調適、公共服務、制度壓力吸收、資訊結構與國家能力影響。中國在 2026 年仍保持超過 $4\%$ 的預期增長、強大的製造與出口能力、高科技投資與國家動員能力；同時房地產投資大幅收縮、青年就業壓力偏高、長工時與內需不足等結構問題也持續存在。這是一個多向耦合系統，不宜簡化為「繁榮」或「崩潰」二選一。

最後，本文加入 AI 作為高階動態變數。AI 可能重新打開普通人的能力與流動通道，改善公共服務、降低知識與創業門檻；也可能壓縮中間職位、提高資本與頂尖人才槓桿、強化國家監測與政策調適，甚至造成「國家能力繼續上升，但家庭能力與政治選擇未同步上升」的發展合法性脫鉤。AI 因此不是舊中國模型中的一個普通科技項，而是可能同時重寫努力回報、比較視野、產業結構、國家能力、資訊環境與制度可行域的作用算子。

---

## 關鍵詞

中國；新中國史；改革開放；發展合法性；相對剝奪；Tunnel Effect；努力—回報彈性；社會流動；階級流動；躺平；青年失業；房地產；國家能力；Agentic AI；類全域 AI；制度—智能共演化

---

# 0. 研究問題：中國真正危險的是變窮，還是「努力失去可預期回報」？

討論中國政治前景時，常見兩種相反敘事。

第一種：

> 中國經濟仍然增長、製造業強、國家能力高，因此制度具有高度穩定性。

第二種：

> 房地產、人口、失業、地方債務、不平等與政治限制正在累積，因此中國接近制度危機。

兩者都可能抓到部分事實，但都容易犯同一錯誤：

$$
\boxed{
\text{把多維動態系統壓成單一方向。}
}
$$

本文提出另一個問題：

> 一個人是否願意繼續投入一個制度，不只取決於今天拿到多少，也取決於他是否相信額外努力仍能轉化為未來位置改善。

因此真正需要追蹤的是：

$$
\boxed{
\text{Absolute Welfare}
+
\text{Welfare Derivative}
+
\text{Mobility Expectation}
+
\text{Effort–Reward Elasticity}
+
\text{Reference Horizon}.
}
$$

---

# 1. 歷史前提：1949 後中國不是單一制度狀態

本文不把 1949 至今的中國視為一個靜態「威權國家」。

至少應分為：

$$
\boxed{
\begin{aligned}
H_1 &: 1949\text{--}1957,\quad \text{國家重建與早期計畫化},\\
H_2 &: 1958\text{--}1976,\quad \text{高動員與高政治波動},\\
H_3 &: 1971\text{--}1979,\quad \text{外部關係重接與制度轉折},\\
H_4 &: 1978\text{--}2000s,\quad \text{改革開放與高速追趕},\\
H_5 &: 2000s\text{--}2010s,\quad \text{成熟化、資產化與大規模流動},\\
H_6 &: 2020s,\quad \text{增長換檔、流動壓力與 AI 轉型}.
\end{aligned}
}
$$

這些階段彼此重疊，不是嚴格斷點。

---

# 2. 1949–1957：低基準條件下的國家重建

1949 年的新中國面對：

- 長期戰爭後的重建；
- 低教育與低工業化；
- 基礎設施不足；
- 高農業人口；
- 國家能力重新整合。

在此階段，政治與經濟評價不能直接套用成熟中等收入國家的標準。

若：

$$
W_{1949}
$$

極低，則只要：

$$
\Delta W_t>0,
$$

即使絕對生活仍不富裕，也可能產生強烈的改善感。

但本文不把此階段浪漫化。土地改革、政治運動、計畫化與組織控制同樣建立了新的權力結構。

因此：

$$
\boxed{
\text{material improvement}
\neq
\text{absence of political coercion}.
}
$$

---

# 3. 1958–1976：高動員能力不等於高治理校正能力

## 3.1 大躍進的政治經濟教訓

1958 年開始的大躍進及其後的 1959–1961 年農業危機與大饑荒，是理解中國制度能力的重要節點。

它展示：

$$
\boxed{
\text{Mobilization Capacity}
\neq
\text{Information Quality}
\neq
\text{Corrective Capacity}.
}
$$

中央可以動員巨大資源，卻不代表地方資訊可以無失真上傳，也不代表錯誤政策能迅速被修正。

---

## 3.2 文化大革命

1966–1976 年文化大革命再次顯示：

$$
\boxed{
\text{political activation}
\neq
\text{institutional stability}.
}
$$

高政治參與、群眾運動與權力重組可以同時破壞教育、行政與專業秩序。

因此毛時代不能只用：

$$
\text{平等}
$$

或：

$$
\text{貧窮}
$$

描述。

---

# 4. 相對封閉與比較視野

## 4.1 比較不是自然固定的

相對剝奪需要參照集合。

定義個體 $i$ 的比較集合：

$$
\boxed{
\mathcal R_{i,t}
=
\{
self\_past,
peer,
elite,
foreign,
promise,
future
\}.
}
$$

若外部資訊與人口流動有限：

$$
|\mathcal R_{i,t}^{foreign}|
$$

可能較小。

這不表示人民沒有不滿，而是可見比較組不同。

---

## 4.2 比較視野擴張

當：

- 對外開放；
- 電視與媒體；
- 出國；
- 外資；
- 網際網路；
- 社交平台；
- AI 搜尋與翻譯；

增加後：

$$
\boxed{
Visibility(\mathcal R_{i,t})
\uparrow.
}
$$

同一生活水準下，相對位置感可能因此改變。

---

# 5. 1971–1979：外部重接與制度轉折

1971 年中美高層接觸加速，1972 年尼克森訪華與《上海公報》成為關係轉折；1978 年底雙方宣布建立正式外交關係，1979 年完成正常化。

這條外交線與經濟改革不是同一事件，但共同顯示中國開始進入新的外部結構。

1978 年後的改革開放則形成更深層的政治經濟轉折：

$$
\boxed{
\text{closed mobilization}
\rightarrow
\text{developmental competition}.
}
$$

世界銀行指出，自 1978 年改革開放以來，中國 GDP 年均增速長期超過 $9\%$，並有近八億人口脫離極端貧困。

這是一個不能被政治立場抹除的巨大發展事實。

---

# 6. 發展合法性：不是「有錢」而是「一直變好」

本文將發展合法性定義為：

$$
\boxed{
L_t^{dev}
=
f(
W_t,
\dot W_t,
M_t,
E_t^{future},
\varepsilon_{ER,t},
T_t
).
}
$$

其中：

- $W_t$：當下福利；
- $\dot W_t$：福利改善速度；
- $M_t$：流動機會；
- $E_t^{future}$：未來改善預期；
- $\varepsilon_{ER,t}$：努力—回報彈性；
- $T_t$：對制度與市場通道的信任。

因此：

$$
W_t
$$

不高，也可以有高：

$$
L_t^{dev},
$$

只要：

$$
\dot W_t\gg0.
$$

---

# 7. Tunnel Effect：為什麼別人先變好不一定帶來革命

Hirschman 與 Rothschild 在 1973 年提出著名的 tunnel effect。

塞車時，旁邊車道開始移動。

最初：

$$
\text{OtherProgress}
\rightarrow
\text{Hope}.
$$

因為：

> 他動了，可能代表我也快動了。

因此短期不平等增加可能與社會容忍共存。

但如果：

$$
\Delta t\uparrow
$$

而自己的車道始終不動：

$$
\text{Hope}
\rightarrow
\text{Suspicion}
\rightarrow
\text{Deprivation}.
$$

本文將其一般化為：

$$
\boxed{
\frac{
\partial Tolerance
}{
\partial Inequality
}
=
g(
ExpectedOwnMobility
).
}
$$

---

# 8. 改革開放中國的「隧道」

改革開放後，大量普通家庭觀察到：

- 農業向工業與服務業轉移；
- 農村人口進城；
- 高等教育擴張；
- 私營與外資企業增加；
- 城市住房與基礎設施改善；
- 家庭耐久財增加；
- 出國、留學與國際接觸增加。

因此：

$$
\boxed{
\text{others moving up}
}
$$

可以在相當長時間被理解為：

$$
\boxed{
\text{my family may also move up}.
}
$$

這使發展型不平等和完全封閉的階級不平等具有不同政治效果。

---

# 9. 絕對流動與相對流動必須分開

中國社會流動研究顯示一個重要雙重現象。

對較年輕世代：

$$
AbsoluteMobility\uparrow,
$$

但：

$$
RelativeMobility
$$

未必同步改善。

Oxford 的中國社會流動研究指出，較年輕世代的絕對流動與向上流動大幅增加，但在最年輕男性世代中，相對階級競爭呈現更強僵化，專業與管理階層和其他階層的差異更加顯著。

因此：

$$
\boxed{
\text{More upward positions}
\neq
\text{Equal probability of reaching them}.
}
$$

---

# 10. 教育擴張的雙重效果

高等教育擴張可以同時造成：

$$
Opportunity\uparrow
$$

與：

$$
CredentialCompetition\uparrow.
$$

如果所有階層都增加大學教育，但優勢階級增加得更快，則：

$$
\boxed{
\text{mass expansion}
\neq
\text{relative equalization}.
}
$$

這是理解當代中國青年壓力的重要前置。

---

# 11. 從「我比父母好」到「我能不能比父母更好」

發展型社會早期的參照通常是：

$$
P_{i,t}^{past}.
$$

若：

$$
Position_i(t)
>
Position_{parent}(t-\Delta),
$$

則個體容易感受到上升。

成熟後比較會轉向：

$$
P_{i,t}^{peer},
$$

$$
P_{i,t}^{elite},
$$

$$
P_{i,t}^{foreign},
$$

與：

$$
P_{i,t}^{expected}.
$$

因此即使：

$$
W_t
>
W_{t-20},
$$

仍可能：

$$
D_t\uparrow.
$$

---

# 12. 多參照相對剝奪模型

本文正式定義：

$$
\boxed{
D_{i,t}
=
\sum_{r\in\mathcal R}
\omega_{i,r,t}
\left(
P_{i,r,t}^{expected}
-
P_{i,t}^{perceived}
\right).
}
$$

其中：

$$
\sum_r\omega_{i,r,t}=1.
$$

參照可以是：

- 自己過去；
- 父母；
- 同齡人；
- 官僚與菁英；
- 富裕階層；
- 外國同類群體；
- 官方承諾；
- 自己預期的未來。

---

# 13. 相對剝奪不是自動政治化

本文延續既有「因果歸因」修正。

定義歸因算子：

$$
\boxed{
\Gamma_{i,t}
:
D_{i,t}
\rightarrow
Cause_{i,t}.
}
$$

可能歸因於：

$$
\{
self,
family,
market,
local\_government,
central\_government,
foreign\_actor,
history,
technology
\}.
$$

因此：

$$
D\uparrow
$$

不推出：

$$
AntiRegimeAction\uparrow.
$$

---

# 14. 四種典型歸因路徑

## 14.1 自我歸因

$$
D
\rightarrow
\text{self-blame}
\rightarrow
\text{more effort / withdrawal}.
$$

---

## 14.2 市場歸因

$$
D
\rightarrow
\text{job / housing / competition problem}.
$$

可能要求經濟政策，而非政權更替。

---

## 14.3 外部歸因

$$
D
\rightarrow
\text{foreign pressure}
\rightarrow
\text{national solidarity}.
$$

甚至可能提高國家支持。

---

## 14.4 制度歸因

$$
D
\rightarrow
\text{structural unfairness}
\rightarrow
\text{institutional demand}.
$$

只有這一類更可能直接形成制度性政治壓力。

---

# 15. 努力—回報彈性

本文定義：

$$
\boxed{
\varepsilon_{ER,i,t}
=
\frac{
\partial
\mathbb E[
\Delta Position_{i,t+1}
]
}{
\partial Effort_{i,t}
}.
}
$$

若：

$$
\varepsilon_{ER,i,t}\gg0,
$$

努力具有可見回報。

若：

$$
\varepsilon_{ER,i,t}\approx0,
$$

追加努力無法明顯改善預期位置。

若：

$$
\varepsilon_{ER,i,t}<0,
$$

可能出現：

> 越投入，承擔的債務、健康、時間與機會成本反而越大。

---

# 16. 「很累但有用」與「很累而且不知道有沒有用」

這是兩個不同社會狀態。

第一種：

$$
Cost(Effort)\uparrow,
$$

但：

$$
\varepsilon_{ER}>0.
$$

因此：

$$
\boxed{
\text{high effort}
+
\text{credible mobility}.
}
$$

第二種：

$$
Cost(Effort)\uparrow,
$$

且：

$$
\varepsilon_{ER}\downarrow.
$$

因此：

$$
\boxed{
\text{high effort}
+
\text{low expected mobility}.
}
$$

後者才更容易產生「退出遊戲」動機。

---

# 17. 躺平可以是理性回應，而不是單純文化病

令個體額外努力：

$$
\Delta e>0.
$$

若：

$$
\mathbb E[
\Delta U
\mid
\Delta e
]
<
Cost(\Delta e),
$$

則降低投入可以是效用最大化行為。

因此：

$$
\boxed{
\text{Tang Ping}
\neq
\text{proof of laziness}.
}
$$

它可能同時包含：

- 抗議；
- 資源保全；
- 低欲望策略；
- 風險避免；
- 退出高成本競爭。

---

# 18. 2020s 的重要結構壓力

本文不把中國描述為整體衰退國家。

2026 年仍存在：

- 超過 $4\%$ 的預期 GDP 增長；
- 強大製造能力；
- 高科技投資；
- 高出口韌性；
- 大型基礎設施；
- 新能源與 AI 產業優勢。

但同時也存在：

- 房地產調整；
- 青年就業壓力；
- 居民消費偏弱；
- 長工時；
- 教育與職位錯配；
- 人口老化；
- 流動性疑慮。

所以：

$$
\boxed{
\text{growth}
\land
\text{structural stress}
}
$$

可以同時成立。

---

# 19. 2026 房地產：不是單一資產價格問題

中國國家統計局資料顯示，2026 年 1–7 月房地產開發投資同比下降 $19.2\%$。

房地產對中國家庭不只是住房，也長期承載：

- 家庭財富；
- 婚育預期；
- 地方財政；
- 建築與相關就業；
- 信貸；
- 城市上升敘事。

因此：

$$
\boxed{
HousingShock
\rightarrow
Wealth
+
Expectation
+
LocalFinance
+
MobilityNarrative.
}
$$

---

# 20. 青年失業與入口職位

2026 年 7 月，中國 $16$ – $24$ 歲非在校青年城鎮失業率升至 $17.9\%$。

這個數字不能直接等於：

$$
17.9\%
\text{ 的青年反對制度}.
$$

但它會影響：

$$
\varepsilon_{ER}^{youth}.
$$

尤其當：

$$
EducationCost\uparrow
$$

而：

$$
EntryOpportunity\downarrow,
$$

則教育投資與職位回報的心理連結會受壓。

---

# 21. 長工時與時間剝奪

2026 年 7 月，中國全國企業就業人員週平均工作時間為 $48.2$ 小時。

因此生活評估不能只用：

$$
Income.
$$

還應加入：

$$
\boxed{
DisposableTime
=
TotalTime
-
Work
-
Commute
-
Care
-
AdministrativeBurden.
}
$$

若收入增長沒有轉化成自由時間：

$$
WelfareGain
$$

可能被高估。

---

# 22. 發展合法性的成熟期難題

追趕期：

$$
\dot W_t\gg0.
$$

成熟期：

$$
\dot W_t\downarrow.
$$

這不必表示制度失敗，而是合法性來源必須轉換。

從：

$$
\boxed{
\text{everyone can expect rapid improvement}
}
$$

逐漸轉為：

$$
\boxed{
\text{fair allocation}
+
\text{service quality}
+
\text{security}
+
\text{choice}
+
\text{correction}.
}
$$

若合法性來源沒有轉換，增長換檔就會被主觀感知為「制度失去以前的承諾」。

---

# 23. 國際比較階級流動

全球資訊化後，參照群體不再只在國內。

一個中國工程師可能比較：

$$
Salary_{CN}
$$

與：

$$
Salary_{US},
$$

也比較：

$$
HousingCost,
WorkingTime,
PoliticalAgency,
PublicService,
TechnologyOpportunity.
$$

因此：

$$
\boxed{
\mathcal R^{foreign}
}
$$

已經成為現代相對剝奪的重要項。

AI 搜尋、翻譯與跨語言資訊會進一步擴大這個參照域。

---

# 24. 「中國快不行了」的早期模型為什麼需要降級

若舊模型近似：

$$
RelativeDeprivation\uparrow
\Rightarrow
RegimeRisk\uparrow,
$$

它遺漏：

$$
\Gamma
$$

因果歸因；

$$
B
$$

家庭與社會緩衝；

$$
C_{\mathrm{state}}
$$

國家適應能力；

$$
N
$$

民族與外部競爭；

$$
S_{\mathrm{service}}
$$

公共服務；

以及：

$$
\mathcal A
$$

AI 增幅。

因此更合理是：

$$
\boxed{
Risk_t
=
f(
D_t,
\Gamma_t,
B_t,
C_{\mathrm{state},t},
L_t,
R_t,
\mathcal A_t
).
}
$$

---

# 25. 蘇聯類比仍有價值，但不能直接複製

中國與蘇聯都曾面臨：

- 中央計畫資訊問題；
- 官僚激勵；
- 政治校正限制；
- 外部競爭；
- 組織僵化。

但現代中國具有蘇聯晚期沒有的：

- 全球製造鏈深度；
- 市場機制；
- 數位平台；
- 大規模民營企業；
- 高速資訊基礎設施；
- 世界級出口產業；
- AI／Agent／感測器系統。

因此：

$$
\boxed{
\text{Soviet Analogy}
=
\text{partial structural comparison},
}
$$

而不是：

$$
\text{deterministic historical replay}.
$$

---

# 26. AI 變數一：Mobility Reset

AI 可以降低：

$$
Cost(
Knowledge,
Coding,
Design,
Research,
Translation,
Tutoring
).
$$

若普通人的能力槓桿提高：

$$
\boxed{
\varepsilon_{ER}^{AI}
\uparrow.
}
$$

則 AI 可能重新打開隧道。

---

# 27. AI 變數二：入口職位壓縮

若 AI 優先替代：

- 初階文職；
- 基礎程式；
- 客服；
- 翻譯；
- 內容製作；
- 部分分析工作；

則：

$$
EntryPositions\downarrow.
$$

對高教育青年而言，這可能形成：

$$
\boxed{
EducationExpansion
+
AICompression
\rightarrow
CredentialReturnPressure.
}
$$

---

# 28. AI 變數三：資本與頂尖人才槓桿

AI 可能使：

$$
Productivity_{top}
\uparrow\uparrow.
$$

若：

$$
Ownership
$$

高度集中，則：

$$
\boxed{
AI
\rightarrow
LeverageConcentration.
}
$$

因此即使總產出提高：

$$
GDP\uparrow,
$$

相對流動也可能下降。

---

# 29. AI 變數四：公共服務與第二次人口時間釋放

AI 也可能：

- 降低行政等待；
- 補足基層醫療；
- 改善高齡照護；
- 降低危險勞動；
- 提升教育可及性；
- 降低中小企業知識門檻。

若技術紅利轉化為：

$$
FreeTime\uparrow,
$$

$$
RealIncome\uparrow,
$$

$$
ServiceAccess\uparrow,
$$

則可能形成：

$$
\boxed{
\text{Second Population-Time Release}.
}
$$

---

# 30. AI 變數五：國家適應能力

Agentic AI 可提高：

$$
PolicySensing,
$$

$$
Simulation,
$$

$$
AdministrativeRouting,
$$

$$
RiskDetection.
$$

因此：

$$
\boxed{
StructuralPressure\uparrow
\not\Rightarrow
StateAdaptation\downarrow.
}
$$

甚至兩者可以同時上升。

---

# 31. AI 變數六：國家能力與家庭能力脫鉤

本文定義：

$$
\boxed{
\Delta C_N
=
\Delta
\text{National Capability},
}
$$

$$
\boxed{
\Delta C_H
=
\Delta
\text{Household Capability}.
}
$$

可能出現：

$$
\Delta C_N>0
$$

但：

$$
\Delta C_H\leq0.
$$

例如國家：

- 工業更強；
- 出口更強；
- AI 更強；
- 軍事與科研更強；

但家庭：

- 工作更不穩；
- 住房資產下跌；
- 自由時間未增加；
- 上升通道縮窄。

本文稱此為：

$$
\boxed{
\text{AI-Induced Developmental Legitimacy Decoupling}.
}
$$

---

# 32. 為什麼這個脫鉤比單純衰退更有政治意義

若：

$$
C_N\downarrow
$$

且：

$$
C_H\downarrow,
$$

人民可以理解為：

> 整個國家都遇到困難。

但若：

$$
C_N\uparrow
$$

而：

$$
C_H\downarrow,
$$

則可能形成：

> 國家、產業、AI、機器人都越來越強，為什麼我的可行生活沒有同步擴張？

因此：

$$
\boxed{
NationalSuccess
\neq
PersonalFeasibleSetExpansion.
}
$$

這是 AI 時代新的發展政治問題。

---

# 33. AI 也可能降低相對剝奪

反方向必須保留。

若 AI：

- 普及高品質教育；
- 降低醫療差距；
- 提高小城市與農村能力；
- 降低創業固定成本；
- 提供個人化專業代理；
- 擴大弱勢者行政與法律能力；

則：

$$
w_i^{effective}
\uparrow
$$

可以降低由制度位置差異帶來的剝奪。

因此本文不主張：

$$
AI
\Rightarrow
Inequality\uparrow.
$$

---

# 34. 類全域 AI 會進一步修改比較集合

如果未來類全域 AI 開始持續回答普通人：

$$
Human
\leftrightarrow
AI,
$$

則 AI 不只回應既有偏好，也會告訴人：

- 還有哪些制度；
- 還有哪些權利；
- 還有哪些工作方式；
- 還有哪些國際生活模式；
- 還有哪些申訴與退出通道。

因此：

$$
\boxed{
AI
\rightarrow
ReferenceSetExpansion.
}
$$

這會直接作用於：

$$
D_{i,t}.
$$

---

# 35. AI 可能同時擴張與管理剝奪

一方面：

$$
ReferenceSet\uparrow
\Rightarrow
Comparison\uparrow.
$$

另一方面：

$$
AIServiceQuality\uparrow
\Rightarrow
Friction\downarrow.
$$

因此：

$$
\boxed{
AI
\text{ can increase awareness of inequality
while reducing some lived burdens}.
}
$$

這是典型雙向效應。

---

# 36. 新中國穩定模型

本文提出：

$$
\boxed{
Stability_t
=
f(
W_t,
\dot W_t,
M_t,
\varepsilon_{ER,t},
D_t,
\Gamma_t,
B_t,
C_{\mathrm{state},t},
R_t,
\mathcal A_t
).
}
$$

其中：

$$
R_t
$$

為制度可逆性與可爭議性。

此式不是用於直接輸出一個「崩潰機率」，而是建立可分解比較框架。

---

# 37. 發展合法性轉換

可把中國的長期合法性來源概念化為：

## 第一階段

$$
\boxed{
\text{State Reconstruction}
+
\text{Order}
+
\text{Industrialization}.
}
$$

## 第二階段

$$
\boxed{
\text{Rapid Material Improvement}
+
\text{Mobility}
+
\text{National Development}.
}
$$

## 第三階段

若高速增長降低，則必須增加：

$$
\boxed{
\text{Distribution}
+
\text{Service}
+
\text{Security}
+
\text{Choice}
+
\text{Correction}.
}
$$

AI 將決定第三階段的部分可行域。

---

# 38. 三種 AI 中國情境

## 38.1 正向情境：Mobility Reopening

$$
AI
\rightarrow
Productivity
\rightarrow
Income
+
FreeTime
+
NewJobs
+
Service
\rightarrow
\varepsilon_{ER}\uparrow.
$$

---

## 38.2 負向情境：Capability Concentration

$$
AI
\rightarrow
CapitalLeverage
+
JobCompression
+
Control
\rightarrow
M\downarrow
+
D\uparrow.
$$

---

## 38.3 混合情境：High-Performance Authoritarian Equilibrium

可能出現：

$$
W\uparrow,
$$

$$
C_{\mathrm{state}}\uparrow,
$$

$$
Service\uparrow,
$$

同時：

$$
Contestability
$$

維持較低。

這種情境不能用「中國一定會失敗」排除。

它將在 Paper 06 正面處理：

> 高福利與高績效是否足以構成完整政治正當性？

---

# 39. 可檢驗預測

## 39.1 預測一：青年政治與社會態度更受努力—回報預期而非 GDP 單值影響

若：

$$
GDP_t>0
$$

但：

$$
\varepsilon_{ER,youth}\downarrow,
$$

則青年退出競爭、低消費與低長期承諾仍可能上升。

---

## 39.2 預測二：絕對生活改善與相對僵化可同時存在

即：

$$
AbsoluteMobility\uparrow
$$

與：

$$
RelativeRigidity\uparrow
$$

不矛盾。

---

## 39.3 預測三：AI 對不同階級的努力—回報彈性影響不一致

$$
\Delta\varepsilon_{ER}^{AI}(class_1)
\neq
\Delta\varepsilon_{ER}^{AI}(class_2).
$$

---

## 39.4 預測四：AI 公共服務效果若能被家庭直接感知，績效合法性可能增加

$$
AIServiceGain
\rightarrow
L^{dev}\uparrow.
$$

---

## 39.5 預測五：若國家能力與家庭能力長期分岔，發展敘事將更難單獨維持合法性

$$
C_N\uparrow
\land
C_H\downarrow
\Rightarrow
LegitimacyDecouplingRisk\uparrow.
$$

---

# 40. 反證與限制

本文不主張：

1. 中國一定崩潰；
2. 中國一定不會崩潰；
3. 經濟增長可以無限替代政治權利；
4. 政治權利可以無條件替代經濟發展；
5. 躺平者都具有相同政治動機；
6. 青年失業率直接等於制度不滿比例；
7. 房地產下降必然導致政治危機；
8. 相對剝奪必然政治化；
9. 中國人民的制度支持必然虛假；
10. 中國人民的制度支持必然完全真實且不受表達環境影響；
11. AI 必然削弱中國制度；
12. AI 必然強化中國制度；
13. 蘇聯歷史可以直接預測中國；
14. 台灣經驗可直接當作中國民主化的反事實結果；
15. 高績效威權均衡必然可長期維持。

---

# 41. 與 Paper 01 的關係

Paper 01 建立：

$$
X_{t+1}
=
F(
X_t,
I_t,
\mathcal A_t,
E_t
).
$$

本文把中國歷史作為第一個大型案例。

其中：

$$
X_t
$$

具體化為：

$$
\boxed{
(
W,
\dot W,
M,
D,
L,
C,
R,
\varepsilon_{ER},
\Gamma
).
}
$$

AI 則不只作用於：

$$
W,
$$

而是同時作用於整個向量。

---

# 42. 與 Paper 03 的接口

下一篇：

**《AI 不只強化威權：福利、控制、流動與制度校正的多向耦合》**

將正式研究：

$$
\boxed{
\operatorname{sign}
\left(
\frac{
\partial X_i
}{
\partial A_j
}
\right)
}
$$

為何不是固定值。

中國將只是其中一個高耦合案例，而不再是唯一研究對象。

---

# 43. 核心命題

## 命題一：發展導數命題

$$
\boxed{
\text{Political effect of welfare depends not only on }W_t
\text{ but also on }\dot W_t.
}
$$

---

## 命題二：努力—回報命題

$$
\boxed{
\varepsilon_{ER}
\downarrow
}
$$

可能比單純收入下降更直接改變個體的長期投入策略。

---

## 命題三：多參照剝奪命題

$$
\boxed{
RelativeDeprivation
=
\text{multi-reference dynamic comparison},
}
$$

不是單一貧富差距。

---

## 命題四：歸因中介命題

$$
\boxed{
D
\not\Rightarrow
PoliticalOpposition.
}
$$

其政治效果受到：

$$
\Gamma
$$

中介。

---

## 命題五：絕對上升—相對僵化共存命題

$$
\boxed{
AbsoluteMobility\uparrow
\land
RelativeRigidity\uparrow
}
$$

可以同時成立。

---

## 命題六：AI 發展合法性脫鉤命題

$$
\boxed{
\Delta C_N>0
\land
\Delta C_H\leq0
}
$$

可能使國家成功與個人可行域改善逐漸分離。

---

# 44. 結論

理解中國不能只問：

> 中國現在比以前富多少？

也不能只問：

> 中國現在有多少不平等？

真正重要的是：

$$
\boxed{
\text{人是否仍相信自己的時間、努力與能力
可以轉化為更好的未來位置。}
}
$$

改革開放後很長一段時間，中國的發展合法性具有強大的歷史基礎：

$$
\text{生活改善}
+
\text{產業擴張}
+
\text{教育擴張}
+
\text{城市化}
+
\text{流動預期}.
$$

它使大量人即使身處高負擔競爭，也可以相信：

$$
\boxed{
\text{努力很累，但有用。}
}
$$

當中國進入成熟化、房地產調整、青年就業壓力、教育大眾化與增長換檔的階段，真正需要觀察的不是是否突然「停止增長」，而是：

$$
\boxed{
\varepsilon_{ER}
}
$$

是否持續下降，以及：

$$
\boxed{
M_t
}
$$

是否仍然提供可信的上升通道。

AI 使這個問題更複雜。

它可能：

$$
\text{重新打開隧道},
$$

也可能：

$$
\text{讓少數人更快離開隧道},
$$

還可能：

$$
\text{讓國家本身變成更強大的交通控制中心}.
$$

因此中國未來不能再用舊式：

$$
\text{growth}
\rightarrow
\text{stability}
$$

或：

$$
\text{deprivation}
\rightarrow
\text{collapse}
$$

描述。

更合理的是：

$$
\boxed{
\text{China Future}
=
\text{development}
\times
\text{mobility}
\times
\text{effort-return}
\times
\text{attribution}
\times
\text{state adaptation}
\times
\text{AI}.
}
$$

Paper 02 因此不給出「中國會不會倒」的答案。

它重新定義問題：

> **當一個曾以高速改善建立發展合法性的超大型國家進入 AI 時代後，AI 究竟會重新擴張普通人的未來可行域，還是主要擴張國家、資本與高槓桿節點的能力？**

這才是下一階段真正值得觀察的中國問題。

---

# 參考文獻與資料來源

1. Hirschman, Albert O. & Rothschild, Michael. “The Changing Tolerance for Income Inequality in the Course of Economic Development.” *World Development*, 1(12), 1973, pp. 29–36. DOI: 10.1016/0305-750X(73)90109-5.
2. Li, Yaojun. “Social Mobility in China: A Case Study of Social Mobility Research in the Global South.” In *Social Mobility in Developing Countries*, Oxford University Press, 2021.
3. World Bank. “China — Country Overview.” 內容指出自 1978 年改革開放以來，中國長期 GDP 年均增速超過 9%，近八億人口脫離極端貧困。
4. World Bank. *Rebalancing Growth: China Economic Update*, 2026-07-07. 預測中國 2026 年增長約 4.4%，並指出房地產調整、消費謹慎與社會安全網的重要性。
5. National Bureau of Statistics of China. *Investment in Real Estate Development from January to July 2026*, 2026-08-18. 2026 年 1–7 月房地產開發投資同比下降 19.2%。
6. National Bureau of Statistics of China. *1—7月份國民經濟保持總體平穩、向新向優發展態勢*, 2026-08-17. 2026 年 7 月全國企業就業人員週平均工作時間為 48.2 小時。
7. Reuters. “China’s youth jobless rate hits 11-month high in July,” 2026-08-19. 報導 2026 年 7 月 16–24 歲非在校青年城鎮失業率為 17.9%。
8. U.S. Department of State, Office of the Historian. *Rapprochement with China, 1972*；以及 *China Policy, 1977–1980*. 用於中美關係正常化歷史節點。
9. Yang, Dennis Tao. “China’s Agricultural Crisis and Famine of 1959–1961: A Survey and Comparison to Soviet Famines.” 同行評審研究，用於大躍進與饑荒的制度性背景。
10. The National Archives, United Kingdom. *The Cultural Revolution*. 用於 1966–1976 年文化大革命基本歷史背景。
11. Ministry of Industry and Information Technology of the PRC. *“人工智能+信息通信”創新發展實施意見（2026—2028年）*, 2026.
12. Neo.K，〈十四億人的時間為何沒有被完全釋放：中國規模動員、時間錯配與國家生產率悖論〉，EveMissLab，2026。
13. Neo.K，〈AI 放大器下的中國耦合危機：具身智慧、生活再生產壓縮與零和外卷〉，EveMissLab，2026。
14. Neo.K，〈從忍耐到集體行動：結構壓力、正當性感知與動員轉換〉，EveMissLab，2026。
15. Neo.K，〈剝削度統一理論／相對剝奪與剝削逃逸速度〉相關版本，EveMissLab，2026。
16. Neo.K，〈政治關係動力學的綜合框架：階級聯盟、注意力場與系統相變的統一理論〉，EveMissLab，2026。
17. Neo.K，〈混合威權崩潰理論：中國作為疊加態政體的測量框架〉，EveMissLab，2026。
18. Neo.K，〈IQRC-01｜AI 介入後的政治系統動力學：從固定智能假設到制度—智能共演化〉，EveMissLab，2026。

---

## 外部來源定位

- World Bank China overview: `worldbank.org/ext/en/country/china`
- World Bank China Economic Update 2026-07-07: `worldbank.org/en/news/press-release/2026/07/07/rebalancing-growth-china-economic-update`
- NBS real estate 2026-01–07: `stats.gov.cn/english/PressRelease/202608/t20260819_1965077.html`
- NBS economy and working hours 2026-08-17: `stats.gov.cn/sj/zxfb/202608/t20260817_1965056.html`
- U.S. Office of the Historian, China rapprochement: `history.state.gov/milestones/1969-1976/rapprochement-china`
- U.S. Office of the Historian, normalization: `history.state.gov/milestones/1977-1980/china-policy`
- MIIT 2026–2028 AI + information communications policy: `hubca.miit.gov.cn/zwgk/zcwj/wjfb/art/2026/art_1a6880738cfc4235afeda815d6ae8ab4.html`
- Oxford Academic, Yaojun Li, Social Mobility in China: DOI `10.1093/oso/9780192896858.003.0010`
- Hirschman & Rothschild 1973: DOI `10.1016/0305-750X(73)90109-5`

---

## 版本註記

**v0.1 / 2026-08-28**

- 建立新中國六階段歷史型別；
- 將發展合法性從福利水準擴充為福利導數、流動預期與努力—回報彈性；
- 建立多參照相對剝奪模型；
- 加入因果歸因算子 $\Gamma$ ；
- 區分絕對流動與相對流動；
- 將「躺平」重新處理為可能的邊際回報適應；
- 降級早期單向中國崩潰預測；
- 加入六類 AI 政治經濟作用；
- 提出 AI-Induced Developmental Legitimacy Decoupling；
- 建立 Paper 03 的多向耦合接口。
