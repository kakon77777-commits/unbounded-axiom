# Paper 02｜看不見的權力：鎌倉政治作為多層關係場
## Invisible Power: Early Kamakura Politics as a Multilayer Relational Field

**系列**：人物—權力認知觀察系列  
**編號**：Paper 02  
**版本**：v0.1  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-09-01  
**狀態**：Completed Public Draft  
**方法承接**：Series 00、Paper 01  
**核心時段**：1199–1203  
**案例中心**：源賴家政權與鎌倉幕府草創世代  
**研究性質**：政治關係圖模型／歷史觀察命題／制度—網絡分析  
**非定位**：人物善惡排名、固定「十三人合議政府」模型、精確量化史實重建

---

## 摘要

源賴家繼承源賴朝之後的鎌倉政治，若只以官職、將軍位與「十三人」名單觀察，容易產生一個靜態印象：年輕的鎌倉殿位居中央，十三名宿老共同限制其權力，各家圍繞最高權位競逐。然而，這種表示法會遮蔽真正決定政權穩定性的多層關係。

本文提出：1199–1203年的鎌倉不應被表示為單一階層樹，而應表示為一個隨時間快速變化的多層關係圖：

$$
\mathcal{G}_t
=
\left(
V,
E_t^{(K)},
E_t^{(M)},
E_t^{(A)},
E_t^{(J)},
E_t^{(P)},
E_t^{(I)},
E_t^{(R)}
\right),
$$

其中分別表示血緣婚姻、軍事動員、行政文書、司法訴訟、近身通道、資訊中介與聲望／敵對等不同關係層。

在此模型中，「權力」不是一項單一資產，而是：

$$
P_i(t)
=
\Phi
\left(
L_i,
M_i,
A_i,
J_i,
B_i,
C_i,
O_i
\mid
\mathcal{G}_t
\right),
$$

其中包括合法性、軍事動員、行政能力、司法程序、橋接位置、聯盟協調與未來選項。

本文依此重建源賴家、北條時政與義時、比企能員、梶原景時、三浦義澄、和田義盛、大江廣元、三善康信、中原親能等角色所掌握的不同類型權力，並指出「十三人」從來不是十三份相等權力，也不是一個穩定不變的統一集團。梶原景時失腳、三浦義澄與安達盛長去世等事件，在極短時間內已使原始結構重新配線。

本文核心命題是：

$$
\boxed{
\text{Political power in early Kamakura was topological before it was hierarchical.}
}
$$

也就是：在幕府制度尚未完全固化、武裝御家人仍具有高度自主性的草創期，**一個人位階多高，不足以決定他真正有多少權力；更重要的是他位於哪些關係之間、能動員哪些節點、能切斷哪些通道，以及其他玩家是否需要他存在。**

這也使 Paper 01 的「顯性權力偏向假說」獲得更具體的環境模型：若源賴家主要管理的是自己節點上的正式權限，而北條、比企、三浦、大江廣元等玩家逐步管理的是邊、路徑與聯盟，那麼賴家即使名義上仍位於圖中心，也可能在拓樸上逐漸失去中心性。

---

## 關鍵詞

源賴家、鎌倉幕府、十三人、北條時政、比企能員、梶原景時、三浦氏、和田義盛、大江廣元、政治網絡、權力場、圖論、聯盟政治

---

# 1. 問題：為什麼「誰官最大」不足以解釋鎌倉政治？

若使用最簡單的封建階層模型，1199年的鎌倉可以畫成：

$$
\text{源賴家}
\rightarrow
\text{宿老}
\rightarrow
\text{御家人}.
$$

這個模型在形式上沒有錯。

但它無法解釋幾個問題：

1. 為何沒有將軍血統的北條氏可以逐步成為政權核心？
2. 為何梶原景時失去一個職位與政治支持後，整個政局會迅速改變？
3. 為何比企氏可以憑乳母、婚姻與繼承關係快速形成巨大威脅？
4. 為何大江廣元沒有大型東國武士集團，卻可以長期位居中樞？
5. 為何和田義盛的侍所別當具有不同於一般宿老的權力？
6. 為何同為「十三人」，彼此功能與可動員資源如此不同？

因為真正的政治不是單一樹狀結構。

至少要寫成：

$$
\text{Hierarchy}
+
\text{Kinship}
+
\text{Military}
+
\text{Administration}
+
\text{Judiciary}
+
\text{Information}
+
\text{Coalition}.
$$

因此：

$$
\text{Rank}
\neq
\text{Power}.
$$

位階只是權力的一個維度。

---

# 2. 從階層樹轉成多層圖

本文將1199–1203年的鎌倉表示為多層圖：

$$
\mathcal{G}_t
=
\left(
V,
\{E_t^{(k)}\}_{k=1}^{m}
\right).
$$

其中節點：

$$
V
=
\{
\text{個人},
\text{家族},
\text{職司},
\text{地方勢力}
\}.
$$

關係層至少包括：

$$
E^{(K)}
=
\text{Kinship / Marriage},
$$

$$
E^{(M)}
=
\text{Military Mobilization},
$$

$$
E^{(A)}
=
\text{Administration},
$$

$$
E^{(J)}
=
\text{Judicial Process},
$$

$$
E^{(P)}
=
\text{Personal Access / Proximity},
$$

$$
E^{(I)}
=
\text{Information / Brokerage},
$$

$$
E^{(R)}
=
\text{Reputation / Rivalry / Trust}.
$$

同兩個人物之間可以同時存在多條不同性質的邊。

例如北條時政與賴家之間至少存在：

$$
E^{(K)}:
\text{外祖父—外孫},
$$

同時又存在：

$$
E^{(R)}:
\text{可能的政治競爭與利益分歧}.
$$

因此血緣不是天然同盟。

同樣地，比企能員與賴家的關係同時具有：

$$
\text{乳母家關係}
+
\text{岳父關係}
+
\text{繼承利益}.
$$

單一「臣下」標籤完全不足以描述。

---

# 3. 七種不能混在一起的權力

本文把早期鎌倉的權力暫分為七個維度。

## 3.1 合法性權力 $L$

例如：

- 源氏嫡流；
- 鎌倉殿身分；
- 朝廷官位；
- 對御家人主從關係的象徵中心。

源賴家在這一層具有天然優勢：

$$
L_{\mathrm{Yoriie}}
\gg
L_i
$$

對多數宿老成立。

但合法性不能自動轉化為軍事與行政服從。

---

## 3.2 軍事動員權力 $M$

指：

$$
\text{Who can actually bring armed men?}
$$

包括：

- 自家武士；
- 地方宗族；
- 長期軍事主從；
- 侍所與御家人統制；
- 臨時聯軍協調。

三浦、和田、比企、北條等東國武士家族在此層具有不同程度的實力。

這是最不能被將軍名位完全替代的權力。

---

## 3.3 行政權力 $A$

指：

- 文書生成；
- 命令制度化；
- 財政與政務程序；
- 京都交涉；
- 幕府機構的持續運作。

大江廣元、二階堂行政、中原親能等人的力量大量存在於這一層。

其特點是：

$$
A_i
\text{ 可在沒有大型私人軍隊時仍然很高}.
$$

---

## 3.4 司法／程序權力 $J$

問注所與訴訟取次所控制的不是「最終主權」本身，而是：

$$
\text{Which claims reach the ruler?}
$$

$$
\text{How are claims formatted?}
$$

$$
\text{What counts as evidence?}
$$

$$
\text{When does a dispute become a decision?}
$$

這類權力極容易被低估。

因為最終裁判者可能仍是將軍，但如果其他人控制：

$$
\text{input pipeline},
$$

那麼他們已經在控制決策空間。

---

## 3.5 近身權力 $P$

誰能直接接近鎌倉殿？

誰能先說話？

誰能在正式程序以前塑造問題？

這些都屬於：

$$
P_{\mathrm{proximity}}.
$$

賴家建立近習圈，本質上是在增加這一層的私人控制。

---

## 3.6 橋接／資訊權力 $B$

政治網絡中非常重要的一種節點，不一定擁有最大自身資源，但控制兩個群體之間的通道。

若移除節點 $v_i$ 後，大量最短政治路徑中斷，則：

$$
B_i
=
\operatorname{Betweenness}(v_i)
$$

可能很高。

中原親能對京都、大江廣元對行政與朝廷、梶原景時對將軍意志與御家人監督，都具有不同形式的橋接功能。

---

## 3.7 聯盟與選項權力 $C,O$

最高階的權力之一是：

$$
C_i
=
\text{ability to coordinate otherwise separate actors}.
$$

另一種是：

$$
O_i
=
\text{number and quality of future political options}.
$$

例如一個玩家即使現在不動手，只要他同時能：

- 靠近將軍；
- 與幾個大族合作；
- 轉向另一繼承人；
- 透過婚姻改變下一代局勢；

他的：

$$
O_i
$$

就很高。

這是一種「尚未使用的權力」。

---

# 4. 源賴家：合法中心，不等於拓樸中心

賴家繼承鎌倉殿後，最清楚的優勢是：

$$
L_{\mathrm{Yoriie}}\uparrow.
$$

他有：

- 賴朝嫡長子身分；
- 鎌倉殿繼承；
- 後續征夷大將軍官位；
- 對御家人的最終象徵中心地位。

但若把權力向量寫成：

$$
\mathbf{P}_{\mathrm{Yoriie}}
=
(
L,M,A,J,P,B,C,O
),
$$

則不能假定所有分量都因繼承而同步最大。

尤其：

$$
L\uparrow
\not\Rightarrow
M\uparrow,
$$

$$
L\uparrow
\not\Rightarrow
A\uparrow,
$$

$$
L\uparrow
\not\Rightarrow
C\uparrow.
$$

賴朝留下的是一個已經運作的網絡。

賴家繼承的是這個網絡的最高節點名稱，但不是所有邊的私人控制權。

因此：

$$
\boxed{
\text{Central node by title}
\neq
\text{central node by dependence}.
}
$$

這是理解整個賴家政權的第一個關鍵。

---

# 5. 北條時政：血緣只是表面，更重要的是可轉移的聯盟位置

北條時政最顯眼的權力是：

$$
E^{(K)}
:
\text{政子之父}
\rightarrow
\text{賴家外祖父}.
$$

但若只把他稱為「外祖父」，會低估真正的政治位置。

他的優勢包括：

1. 與源氏將軍家直接血緣連結；
2. 自身東國武士家族基礎；
3. 可以透過政子連接將軍家；
4. 可以與其他御家人形成臨時合作；
5. 在繼承危機中具有轉向另一將軍候選人的可能。

因此他的真正權力不只是：

$$
K_{\mathrm{Tokimasa}}.
$$

而是：

$$
O_{\mathrm{Tokimasa}}
+
C_{\mathrm{Tokimasa}}.
$$

也就是：

> 他不必永遠控制同一名鎌倉殿，只要北條氏仍能成為「新鎌倉殿不可缺少的節點」。

這就是一種高度可轉移權力。

---

# 6. 北條義時：早期不是最高權者，卻具備低可見度的累積路徑

後世看北條義時，很容易把後來的執權權力倒投回1199年。

這是錯誤的。

1199年的義時不能直接表示成後來的幕府最高實力者。

更合理的是：

$$
P_{\mathrm{Yoshitoki}}(1199)
<
P_{\mathrm{Yoshitoki}}(1221).
$$

但他具有一個重要結構條件：

$$
\frac{dP_{\mathrm{Yoshitoki}}}{dt}>0
$$

在後續相當長一段時間成立。

其成長並非單靠一次奪權，而是逐步累積：

- 北條家族位置；
- 宿老資格；
- 政務參與；
- 與大江廣元等行政人物協調；
- 對御家人衝突的介入；
- 後來對侍所等關鍵職司的掌握。

因此義時非常適合說明：

$$
\text{Power Growth}
\neq
\text{Immediate Office Capture}.
$$

真正危險的玩家不一定現在權力最大，而可能是：

$$
\operatorname{argmax}_i
\frac{dP_i}{dt}.
$$

---

# 7. 比企能員：乳母、婚姻與繼承形成的垂直捷徑

比企氏的權力結構與北條氏不同。

其歷史基礎包括比企尼與賴朝的長期關係；比企能員又與賴家的養育環境密切相連，能員之女若狹局成為賴家妻子，並生下一幡。

因此形成：

$$
\text{比企尼}
\rightarrow
\text{賴朝}
\rightarrow
\text{賴家養育關係},
$$

以及：

$$
\text{比企能員}
\rightarrow
\text{若狹局}
\rightarrow
\text{一幡}.
$$

這是一條直接通向下一代將軍繼承的路徑。

因此比企的力量不是單純：

$$
M_{\mathrm{Hiki}}.
$$

更重要的是：

$$
K_{\mathrm{Hiki}}
+
P_{\mathrm{Hiki}}
+
O_{\mathrm{succession}}.
$$

如果一幡完整繼承鎌倉殿位置，比企氏就可能從「賴家近親集團」變成：

$$
\text{next shogun's maternal house}.
$$

所以北條與比企的衝突，不能只理解成兩個大臣爭寵。

它更接近：

$$
\boxed{
\text{competition over which network will reproduce itself through succession}.
}
$$

這是世代型權力。

---

# 8. 梶原景時：將軍權力的執行介面

梶原景時是理解「看不見權力」不可缺少的人物。

他曾任侍所所司，後任侍所別當。侍所本身具有御家人統制與鎌倉警備等功能。

因此景時不只是：

$$
\text{one warrior among many}.
$$

他更接近：

$$
\text{Shogunal Intent}
\rightarrow
\boxed{\text{Kagetoki}}
\rightarrow
\text{Warrior Enforcement}.
$$

他還具有：

- 對御家人行為的監督與報告；
- 文武能力；
- 與賴朝的高度信任；
- 將將軍意志轉換為具體執行的能力。

這使他的：

$$
B_{\mathrm{Kagetoki}}
$$

非常高。

但同樣的結構也使他累積大量敵意。

因為：

$$
\text{monitoring power}
\rightarrow
\text{resentment}.
$$

所以景時的政治位置具有典型悖論：

$$
\text{useful to the ruler}
\quad\land\quad
\text{disliked by many ruled actors}.
$$

賴朝可以吸收這個矛盾，是因為：

$$
P_{\mathrm{Yoritomo}}
$$

足以保護景時。

賴家時代則未必如此。

---

# 9. 梶原景時失腳不是「少一個人」，而是刪除一條高流量邊

1199年梶原景時遭大量御家人彈劾，之後失腳並於1200年死亡。

如果使用人物名單模型：

$$
13\rightarrow12.
$$

似乎只是十三人少了一人。

但在網絡模型中：

$$
\mathcal{G}_{1199}
\rightarrow
\mathcal{G}_{1200}
$$

可能發生更大變化。

移除景時同時削弱：

$$
\text{將軍}
\leftrightarrow
\text{侍所／御家人監督}
$$

的某種舊有橋接。

並改變：

$$
\text{Wada},
\text{Miura},
\text{Hojo},
\text{other gokenin}
$$

之間的相對位置。

因此：

$$
\Delta P_{\mathrm{system}}
\neq
\Delta P_{\mathrm{one\ node}}.
$$

更接近：

$$
\Delta P_{\mathrm{system}}
=
\Delta
\left(
\text{paths},
\text{coalitions},
\text{access},
\text{enforcement}
\right).
$$

這說明「刪除一個政治人物」真正重要的是他承載了多少路徑。

---

# 10. 三浦義澄與和田義盛：軍事網絡不是行政網絡

三浦義澄代表的是另一種權力。

三浦氏在相模具有深厚地方武士基礎，並自賴朝起兵初期就參與源氏政權形成。

因此：

$$
M_{\mathrm{Miura}}
$$

具有高度自主性。

和田義盛則與三浦一族相連，又曾任侍所別當。

於是其位置兼具：

$$
M_{\mathrm{Wada}}
+
A_{\mathrm{Samurai-dokoro}}.
$$

尤其侍所的意義在於：

$$
\text{warrior body}
\rightarrow
\text{institutional command channel}.
$$

因此，和田義盛不是單純「有兵的武士」。

他一度站在：

$$
\text{private military network}
\cap
\text{public warrior administration}
$$

的交界。

這是一個高價值交叉節點。

---

# 11. 為什麼三浦／和田不能簡化成「北條的敵人」？

後來歷史知道北條與和田最終發生衝突，很容易倒推：

$$
\text{Wada}
=
\text{anti-Hojo}.
$$

但動態政治不是固定陣營。

1203年比企氏事件中，和田義盛可以站到北條時政一側。

後來又可能與北條發生致命衝突。

因此聯盟應表示為：

$$
E_{ij}^{(C)}(t),
$$

而不是：

$$
E_{ij}^{(C)}
=
\text{constant}.
$$

也就是：

$$
\boxed{
\text{Alliance is a state variable, not an identity.}
}
$$

這一點非常重要。

因為賴家若把人物分類為：

$$
\text{我的人}
\quad vs.\quad
\text{不是我的人},
$$

就會錯過大量可以臨時重組的關係。

真正成熟的政治模型問的是：

$$
U_i(a,t)
$$

在此時此事下是什麼，而不是「這家永遠站哪邊」。

---

# 12. 大江廣元：沒有最大軍隊，仍可擁有巨大系統權力

大江廣元是最適合用來反駁：

$$
\text{power}=\text{military force}
$$

的人物之一。

他的核心能力包括：

- 京都實務官人經驗；
- 公文所、政所等行政機構；
- 文書與法令；
- 朝廷—鎌倉交涉；
- 幕府中樞政務的制度化。

因此：

$$
M_{\mathrm{Hiromoto}}
$$

未必突出，

但：

$$
A_{\mathrm{Hiromoto}}\gg0,
$$

$$
B_{\mathrm{Hiromoto}}\gg0.
$$

他控制的不是「誰今天拔刀」。

而是：

$$
\text{How a political decision becomes an administrable order}.
$$

這種權力平時可見度低。

但缺少它，政權就會從：

$$
\text{decision}
$$

無法穩定轉換成：

$$
\text{document}
\rightarrow
\text{procedure}
\rightarrow
\text{implementation}.
$$

因此大江廣元代表的是：

$$
\boxed{
\text{infrastructural power}.
}
$$

---

# 13. 三善康信與問注所：控制「問題如何進入系統」

三善康信與問注所所代表的權力尤其容易被忽視。

若最高裁判者是賴家，人們可能直覺認為：

$$
J_{\mathrm{Yoriie}}=1,
$$

其他人只是幕僚。

但實際決策鏈更像：

$$
\text{dispute}
\rightarrow
\text{petition}
\rightarrow
\text{screening}
\rightarrow
\text{evidence}
\rightarrow
\text{procedural framing}
\rightarrow
\text{decision}.
$$

如果某些人控制中間四步，那麼：

$$
\text{Final Decision Authority}
$$

並不是全部司法權力。

可以表示成：

$$
J_{\mathrm{total}}
=
J_{\mathrm{input}}
+
J_{\mathrm{process}}
+
J_{\mathrm{framing}}
+
J_{\mathrm{final}}.
$$

賴家可能擁有較多：

$$
J_{\mathrm{final}},
$$

而行政文士控制大量：

$$
J_{\mathrm{input}}
+
J_{\mathrm{process}}.
$$

這就是「看不見的制度權力」。

---

# 14. 中原親能：京都不是外部背景，而是另一張網

鎌倉政治並不是封閉系統。

朝廷仍然控制：

- 官位；
- 政治承認；
- 京都資訊；
- 公家社會；
- 西國關係。

中原親能長期扮演鎌倉與京都之間的聯絡角色。

因此他的價值可寫成：

$$
B_{\mathrm{Chikayoshi}}
=
\operatorname{Bridge}
(
G_{\mathrm{Kamakura}},
G_{\mathrm{Kyoto}}
).
$$

在多層網絡中，一個節點即使在鎌倉內部度數不最高，只要它連接兩張原本不完全重合的圖，就可能具有極高：

$$
\operatorname{Betweenness}.
$$

這種人不是「比將軍更有權」。

而是：

> 將軍若要影響某個外部系統，必須依賴這類橋接節點。

因此依賴本身就是權力來源。

---

# 15. 政子：不在「十三人」名單中，卻不能從權力圖中刪除

若把十三人名單當成全部政治中樞，最明顯的錯誤之一就是北條政子。

政子不是「十三人」之一。

但她同時是：

$$
\text{賴朝之妻}
+
\text{賴家之母}
+
\text{實朝之母}
+
\text{北條時政之女}.
$$

她位於：

$$
\text{Minamoto succession}
\cap
\text{Hojo kinship}
$$

的交界。

因此：

$$
B_{\mathrm{Masako}}
$$

天然很高。

這正好證明：

$$
\text{Council membership}
\neq
\text{political centrality}.
$$

真正的權力網必須納入未擁有正式「十三人」資格、但能改變繼承與聯盟的節點。

---

# 16. 「十三人」不是一個玩家

因此本文拒絕以下表示法：

$$
\text{Yoriie}
\leftrightarrow
\boxed{\text{Council of 13}}.
$$

它過度擬人化。

更合理的是：

$$
\text{Yoriie}
\leftrightarrow
\{
v_1,v_2,\ldots,v_{13}
\},
$$

且：

$$
U_1\neq U_2\neq\cdots\neq U_{13}.
$$

不同人物擁有不同：

- 家族利益；
- 年齡；
- 後繼者；
- 官職；
- 地方基礎；
- 與賴家的親疏；
- 與其他宿老的競合。

所以不存在天然的：

$$
U_{\mathrm{Council}}.
$$

只有在特定議題上，部分人的利益暫時對齊，才形成：

$$
C_t
\subseteq
V.
$$

這是一個 coalition，而不是固定 faction。

---

# 17. 1199年的十三人只是一張快照

1199年名單很容易製造穩定制度的錯覺。

但實際上極短時間內：

- 梶原景時失腳並死亡；
- 三浦義澄死亡；
- 安達盛長死亡；
- 其他人的政治參與程度也並不固定。

因此：

$$
G_{1199}
\neq
G_{1200}
\neq
G_{1201}
\neq
G_{1203}.
$$

真正需要研究的是：

$$
\frac{dG_t}{dt}.
$$

而不是：

$$
G_{1199}
$$

一張靜態名單。

這也意味著，賴家若能活用時間，其實存在大量重新接線機會。

因為舊宿老本身正在自然退出。

---

# 18. 權力空缺不會保持空白

當一個高中心性節點消失：

$$
v_k\rightarrow\varnothing,
$$

它原先承載的功能不會永久消失。

系統會進行：

$$
\text{Power Reallocation}.
$$

例如梶原景時退出後：

- 御家人統制功能需要重新安排；
- 將軍近身執行功能需要替代；
- 侍所權力重新分布；
- 原本反景時聯盟失去共同目標；
- 某些家族的相對地位上升。

因此：

$$
\text{remove rival}
$$

不等於：

$$
\text{my power increases}.
$$

真正結果取決於：

$$
\text{who captures the vacated edges}.
$$

如果賴家沒有捕捉那些邊，別人就會。

這是一個非常重要的「負空間權力」概念。

---

# 19. 權力的最小單位不是人物，而是依賴

本文因此提出：

$$
D_{ij}
=
\text{degree to which actor }i\text{ needs actor }j.
$$

政治權力可以部分理解為：

$$
P_j
\propto
\sum_i D_{ij}.
$$

但還要扣除：

$$
D_{ji},
$$

即 $j$ 對其他人的反向依賴。

若很多人需要你，而你有多個替代方案：

$$
P_j\uparrow.
$$

若你看似官位很高，但所有命令都需要同一群人合作：

$$
D_{j\rightarrow others}\uparrow,
$$

則你的實質自主性可能很低。

因此：

$$
\boxed{
\text{Power is asymmetric dependence.}
}
$$

比：

$$
\text{Power is rank.}
$$

更接近草創期鎌倉的實際政治。

---

# 20. 「讓所有人需要鎌倉殿」才是賴家的最優問題

如果使用這個模型，賴家的理想策略就不應只是：

$$
\max P_{\mathrm{Yoriie}}.
$$

而應是：

$$
\max
\sum_i
D_{i,\mathrm{Yoriie}}.
$$

也就是增加：

> 其他主要玩家對「賴家繼續存在」的依賴。

例如：

北條需要賴家才能保有某些地位；

比企需要賴家才能完成下一代繼承；

三浦需要賴家平衡北條；

和田需要賴家維持侍所位置；

大江廣元需要賴家提供政令合法中心；

各家二代需要賴家提供新的仕途。

如果做到：

$$
D_{\mathrm{Hojo},Y}>0,
$$

$$
D_{\mathrm{Hiki},Y}>0,
$$

$$
D_{\mathrm{Miura},Y}>0,
$$

$$
D_{\mathrm{Wada},Y}>0,
$$

且彼此無法輕易共同找到更好的替代方案，那麼：

$$
\operatorname{Cost}(\text{remove Yoriie})
\gg0.
$$

這才是將軍真正的安全。

---

# 21. 為什麼「只有比企支持我」反而危險？

如果賴家的網絡逐步變成：

$$
Y
\leftrightarrow
H_{\mathrm{Hiki}},
$$

而其他大族的依賴下降：

$$
D_{i,Y}\downarrow,
$$

那麼政治圖會發生兩件事。

第一，比企對賴家的議價能力增加：

$$
D_{Y,\mathrm{Hiki}}\uparrow.
$$

第二，其他大族更容易共同認為：

$$
U_i(\text{Yoriie-Hiki bloc removed})
>
U_i(\text{bloc survives}).
$$

於是：

$$
\text{personal support concentration}
$$

反而造成：

$$
\text{systemic coalition against the ruler}.
$$

這就是：

$$
\boxed{
\text{Concentrated loyalty can reduce systemic survivability.}
}
$$

也是 Paper 06「親信不等於聯盟」將正式展開的命題。

---

# 22. 制衡不是「讓兩邊一樣強」

政治中的制衡常被誤解成：

$$
P_A=P_B.
$$

但真正可操作的制衡更接近：

$$
U_A(\text{leader survives})
>
U_A(\text{leader removed}),
$$

同時：

$$
U_B(\text{leader survives})
>
U_B(\text{leader removed}),
$$

即使：

$$
U_A\neq U_B.
$$

所以賴家不必使北條與比企完全等強。

他真正需要的是：

$$
\text{Neither side can improve its position by removing him}.
$$

更高階則是：

$$
\text{Each side needs him to prevent the other side from dominating}.
$$

此時將軍變成：

$$
\boxed{
\text{indispensable balancing node}.
}
$$

這才是「看不見的權力」最高形態之一。

---

# 23. 最強的中心不是最大節點，而是不可替代節點

傳統權力直覺是：

$$
\max \operatorname{Size}(v_i).
$$

但網絡政治更重要的可能是：

$$
\max \operatorname{ReplacementCost}(v_i).
$$

如果一個人物消失後，所有玩家很快可以改接到另一個節點：

$$
\operatorname{ReplacementCost}(v_i)\approx0.
$$

那麼即使他的名位很高，其結構權力也有限。

反之，如果：

$$
\operatorname{ReplacementCost}(v_i)\gg0,
$$

則很多人即使不喜歡他，也會保護他。

這就是：

$$
\text{Indispensability Power}.
$$

賴朝在相當程度上曾是這種節點。

賴家最大的問題之一，可能正是沒有把自己的身分進一步轉化成：

$$
\text{systemic indispensability}.
$$

---

# 24. 一病倒就被重新分配，意味著什麼？

1203年賴家重病後，繼承安排迅速成為政治核心問題。

不論具體分配方案的形成責任應如何判定，有一件事在結構上非常重要：

$$
\text{Yoriie unavailable}
\rightarrow
\text{system begins succession reconfiguration}.
$$

任何政治系統在統治者病危時都會準備繼承。

因此這本身不能證明賴家無權。

真正值得觀察的是：

> 在賴家暫時退出決策後，是否存在足夠多的玩家願意以「維持賴家原有權力結構」作為自己的首要利益？

若答案偏弱，表示：

$$
D_{i,Y}
$$

在若干重要節點上並不足以保證賴家網絡自我維持。

這不是名位問題。

是系統依賴問題。

---

# 25. 從「權力中心」到「權力場控制器」

因此本文提出兩種統治模式。

## 模式 A：中心節點統治

$$
v_L
\rightarrow
V.
$$

核心問題：

> 我能不能直接控制大家？

## 模式 B：關係場統治

$$
v_L
\rightarrow
\frac{d\mathcal{G}}{dt}.
$$

核心問題：

> 我能不能使整張圖的變化方向持續有利於我的存在？

模式 B 的統治者不一定每天直接裁決最多事情。

他可能反而：

- 把行政交給廣元；
- 把訴訟程序交給康信；
- 把御家人統制交給侍所；
- 讓北條牽制比企；
- 讓比企牽制北條；
- 讓三浦／和田保有獨立利益；
- 自己控制最終合法性、恩賞與代際晉升。

於是：

$$
P_{\mathrm{direct}}\downarrow
$$

但：

$$
P_{\mathrm{systemic}}\uparrow.
$$

---

# 26. 源賴朝真正留下的是一張圖，不是一把椅子

這使我們可以重新理解「繼承」。

表面繼承：

$$
\text{Yoritomo}
\rightarrow
\text{Yoriie}
$$

表示：

$$
\text{office transferred}.
$$

但真正需要繼承的是：

$$
\mathcal{G}_{\mathrm{Yoritomo}}
\rightarrow
\mathcal{G}_{\mathrm{Yoriie}}.
$$

問題在於圖不能像官印一樣交接。

每一條邊都必須重新確認：

$$
E_{i,\mathrm{Yoritomo}}
\not\Rightarrow
E_{i,\mathrm{Yoriie}}.
$$

父親的恩情不是兒子的恩情。

父親的恐懼不是兒子的恐懼。

父親的私人信任不是兒子的私人信任。

因此：

$$
\boxed{
\text{Succession transfers the node faster than it transfers the edges.}
}
$$

這可能正是開國二代最危險的結構問題。

Paper 03 將以此為核心進一步分析。

---

# 27. 初步角色—權力層矩陣

以下矩陣只表示**功能型態**，不是精確量化或人物強弱排名。

| 角色 | 合法性 $L$ | 軍事 $M$ | 行政 $A$ | 司法 $J$ | 近身 $P$ | 橋接 $B$ | 聯盟／選項 $C,O$ |
|---|---|---|---|---|---|---|---|
| 源賴家 | 極高 | 間接 | 最終中心 | 最終裁決較高 | 可主動建立 | 中 | 未穩定 |
| 北條時政 | 血緣衍生 | 東國家族 | 漸增 | 間接 | 母族通道 | 高 | 高 |
| 北條義時 | 初期中低 | 家族衍生 | 漸增 | 間接 | 家族通道 | 漸增 | 高成長性 |
| 比企能員 | 繼承關係衍生 | 家族勢力 | 中 | 間接 | 高 | 高 | 對一幡繼承極高 |
| 梶原景時 | 低 | 高執行性 | 侍所 | 監督相關 | 高 | 極高 | 敵意成本高 |
| 三浦義澄 | 低 | 高 | 低 | 低 | 中 | 地方網高 | 高 |
| 和田義盛 | 低 | 高 | 侍所 | 低 | 中 | 軍事制度交界 | 高 |
| 大江廣元 | 低 | 低 | 極高 | 中 | 高 | 極高 | 高 |
| 三善康信 | 低 | 低 | 中 | 極高 | 中 | 程序高 | 中 |
| 中原親能 | 低 | 低 | 高 | 低 | 中 | 京都橋接極高 | 中 |
| 北條政子 | 血統中心 | 間接 | 非正式 | 非正式 | 極高 | 極高 | 繼承選項極高 |

此表真正想表達的是：

$$
\text{different actors own different dimensions}.
$$

因此「誰比較有權」本身就是錯問法。

更好的問題是：

> 在某一事件中，哪一種權力層成為瓶頸？

---

# 28. 事件會切換「最重要的權力維度」

設事件為：

$$
x_t.
$$

不同事件具有不同需求向量：

$$
\mathbf{q}(x_t)
=
(q_L,q_M,q_A,q_J,q_P,q_B,q_C).
$$

例如：

土地訴訟時：

$$
q_J,q_A\uparrow.
$$

軍事討伐時：

$$
q_M,q_C\uparrow.
$$

將軍繼承時：

$$
q_L,q_K,q_C,q_O\uparrow.
$$

京都交涉時：

$$
q_A,q_B\uparrow.
$$

因此人物的有效權力是：

$$
P_i(x_t)
=
\mathbf{P}_i
\cdot
\mathbf{q}(x_t).
$$

這解釋了為什麼同一個人不會在所有事件中都最重要。

權力是情境函數。

---

# 29. 看不見的權力甚至可以表現為「什麼都沒做」

如果某玩家因為存在，就使其他人不敢採取某行動，那也是權力。

定義：

$$
P_{\mathrm{deterrence}}
=
\text{actions others do not take because I exist}.
$$

這種權力最難在史料中直接觀察。

因為史料記錄：

$$
\text{what happened},
$$

卻很少記錄：

$$
\text{what rational actors decided not to attempt}.
$$

因此歷史權力分析天然容易高估顯性行動者，低估威懾、聲望與均衡本身。

這同樣提醒我們：不能只用「賴家做了多少事」判定他掌握多少政治。

---

# 30. 對 Paper 01 假說的回饋

Paper 01 提出：

$$
H_{\mathrm{VPB}}
:
\text{賴家可能高估顯性控制，低估關係權力}.
$$

本文沒有證明它。

但本文建立了其必要背景：

$$
P_{\mathrm{real}}
=
P(\mathcal{G}_t),
$$

而不是：

$$
P_{\mathrm{real}}
=
P(\text{office only}).
$$

因此若後續史料顯示賴家主要操作：

- 親裁；
- 近習；
- 直接分配；
- 顯性命令；

卻缺乏對：

- 跨派系依賴；
- 代際交換；
- 程序合法性；
- 節點替代成本；
- 聯盟重組；

的長期設計，那麼：

$$
P(H_{\mathrm{VPB}}\mid E)
\uparrow.
$$

---

# 31. 本文的核心理論：政治權力的拓樸優先性

本文最終提出：

$$
\boxed{
P_i(t)
=
\Phi
\left(
v_i,
\mathcal{N}_i,
\mathcal{B}_i,
\mathcal{D}_i,
\mathcal{O}_i
\right)
}
$$

其中：

- $v_i$：人物自身資源；
- $\mathcal{N}_i$：鄰接關係；
- $\mathcal{B}_i$：橋接路徑；
- $\mathcal{D}_i$：他人對其依賴；
- $\mathcal{O}_i$：未來可轉換選項。

因此：

$$
\text{formal hierarchy}
$$

只是：

$$
\mathcal{G}_t
$$

中的一個圖層。

在制度尚未完全固化的草創政權中：

$$
\boxed{
\text{topology may dominate hierarchy}.
}
$$

也就是：

> **真正重要的不是你坐在哪張椅子，而是多少重要道路必須經過你。**

---

# 32. 結論：賴家坐在中央，但中央可能正在移動

源賴家1199年繼承的是鎌倉殿。

從形式上看，他位於整個幕府最高點。

但本文指出，1199–1203年的真正政治結構不是一座靜態金字塔，而是一張高速重新接線的圖。

梶原景時消失。

三浦義澄死亡。

安達盛長死亡。

侍所位置重新分配。

比企氏透過婚姻與一幡繼承提高未來權重。

北條氏同樣握有將軍母族與另一繼承路徑。

大江廣元維持行政基礎設施。

三善康信控制重要訴訟程序。

和田、三浦等軍事集團具有自身動員能力。

政子甚至不在十三人名單內，卻位於源氏繼承與北條血緣的關鍵橋上。

因此：

$$
\text{Yoriie at the center of the hierarchy}
$$

並不能保證：

$$
\text{Yoriie at the center of the network}.
$$

如果他只試圖增加：

$$
P_{\mathrm{node}},
$$

而沒有管理：

$$
E_t,
$$

那麼就可能發生：

$$
P_{\mathrm{formal}}\text{ remains high}
$$

但：

$$
\operatorname{Centrality}_{\mathrm{real}}\downarrow.
$$

這就是本文最重要的歷史觀察命題：

$$
\boxed{
\text{The throne can remain in place while the center of power moves elsewhere.}
}
$$

一張椅子不會自己產生權力。

真正的權力存在於：

- 誰需要誰；
- 誰能聯絡誰；
- 誰能動員誰；
- 誰能讓命令成為制度；
- 誰能決定問題如何被提出；
- 誰能提供下一代的政治未來；
- 誰消失後會讓整個系統付出巨大代價。

如果源賴家沒有充分理解這一層，那麼他的問題就不是「被十三個人搶走權力」。

而是：

> **他仍坐在最高位置時，整張權力圖已開始重新尋找其他中心。**

下一篇將進一步處理為什麼開國二代特別容易發生這種錯位：

**Paper 03｜開國二代悖論：繼承終態而沒有繼承生成路徑。**

---

# 史料與研究支點

**S1｜藤本頼人，《源頼家とその時代：二代目鎌倉殿と宿老たち》，吉川弘文館，2023。**  
其章節直接處理「比企氏とそのネットワーク」「外戚北条氏の立場」「近習と宿老」「十三人の合議制」「頼家政権の方向性」等，是本文將賴家政權理解為網絡而非單一人物問題的重要近年研究支點。

**S2｜鎌倉市，〈鎌倉殿を支えた13人の宿老たち〉及相關「鎌倉殿通信」。**  
整理十三名宿老各自背景與職司，並指出近年研究不再把1199年制度簡化為十三人完全取代賴家親裁；同時可見侍所、政所、問注所等人物具有明顯不同的功能基礎。

**S3｜盛本昌広，〈鎌倉殿の13人と横浜〉，《Web版 有鄰》第578號，2022。**  
說明十三人制度的實際運作不宜理解為固定十三人全員合議，支持本文把「十三人」視為異質節點集合而非單一玩家。

**S4｜鎌倉市，大江廣元人物資料。**  
大江廣元具京都官人背景，任公文所／政所別當，負責行政、文書與朝廷交涉；頼朝死後仍居中樞，說明軍事資源並非早期幕府唯一權力來源。

**S5｜鎌倉市／東松山市，比企氏相關人物資料。**  
比企尼長期支援賴朝；比企能員成為賴家乳母父，其女若狹局又與賴家結合並生一幡，呈現養育、婚姻與繼承權力高度疊合。

**S6｜侍所相關辭典資料與梶原景時研究整理。**  
侍所自草創期即具有御家人統制與鎌倉警備功能；梶原景時曾任侍所所司、別當並充當賴朝重要執行者，其失腳不能只視為十三人名單減一。

**S7｜鎌倉市，三浦義澄、和田義盛人物資料。**  
三浦氏具有相模地方武士基礎；和田義盛與三浦氏相連且任侍所別當，呈現私人軍事網絡與幕府正式軍事機構交叉。

---

## 命題狀態

本文的網絡模型屬於：

$$
\text{Analytical Reconstruction},
$$

而非：

$$
\text{Numerically Measured Historical Network}.
$$

所有「高／低」「中心性」「橋接」目前都是功能性描述。若未來進行正式數位人文研究，可再將《吾妻鏡》、公家日記、系圖、官職與所領資料編碼，建立時間化多層圖並測試本文假說。

---

## Series Roadmap

Series 00｜從行為到世界模型：歷史人物政治認知的觀察命題方法  
Paper 01｜權力作為物：源賴家的顯性權力模型猜想  
Paper 02｜看不見的權力：鎌倉政治作為多層關係場  
Paper 03｜開國二代悖論：繼承終態而沒有繼承生成路徑  
Paper 04｜武士之外形與武家棟梁之實質  
Paper 05｜短期權力最大化與長期統治權耗散  
Paper 06｜親信不等於聯盟：近習政治與跨派系二代網絡  
Paper 07｜賴家真的「無能」嗎？史料偏差、替代解釋與模型比較
