# 當手工看起來像 AI：同質化創作的反直覺問題

**系列：** AI 時代的創作、選擇與人類復古系列  
**篇次：** 第 3 篇  
**版本：** v0.1  
**性質：** 理論論文／創作同質化模型／公開版

---

## 摘要

AI 生成內容經常被批評具有模板化、平均化、同質化與「一眼 AI」的特徵。然而，本篇提出一個反直覺但 increasingly important 的命題：

$$
\boxed{
\text{Human-Made}
\not\Rightarrow
\text{Human-Distinctive}
}
$$

人類創作者同樣可能在高產量壓力、固定工作流、局部審美最優、長期自我模仿、缺乏外部審核與有限資源下，逐步收斂到高度模板化的創作吸引子。當這種收斂足夠強時，人類作品甚至可能在視覺、敘事、角色設計、程式結構或產品體驗上呈現與 AI 平均化輸出極為相似的特徵。

因此，「看起來像 AI」不能可靠推出「由 AI 生成」；同樣地，「由人類完成」也不能可靠推出「具有高度作者性」。

本篇建立 **Homogenization Attractor Model（同質化吸引子模型）**，區分 AI 統計平均化、人類自我模板化、產量驅動收斂、工具驅動收斂與市場驅動收斂，並提出「來源—風格脫鉤」命題：

$$
\boxed{
\text{Provenance}
\perp
\text{Aesthetic Distinctiveness}
}
$$

在 AI 時代，真正值得追求的不是「證明作品不是 AI」，而是提升 **Identity Density（身份密度）**、**Selection Density（選擇密度）** 與 **Directional Coherence（方向一致性）**，使作品即使使用大量 AI 工具，仍能呈現明確、持續、可辨識的作者性。

---

## 關鍵詞

AI 同質化、人類模板化、作者性、審美吸引子、風格收斂、Identity Density、Selection Density、AI 創作、人類復古、來源與風格脫鉤

---

# 1. 「像 AI」到底在說什麼

當人們說：

> 這張圖很像 AI。

通常不是在做來源鑑識。

更多時候是在描述某些感知特徵：

- 臉部結構相似；
- 五官比例平均；
- 光影過度平滑；
- 細節密度均勻；
- 缺乏局部怪癖；
- 角色間辨識度不足；
- 敘事語氣平均；
- 設計像在同一個模板上換配件。

所以：

$$
\boxed{
\text{AI-like}
}
$$

其實常常是在描述：

$$
\boxed{
\text{Homogenized Output}
}
$$

而不是：

$$
\text{Verified AI Provenance}
$$

---

# 2. 因此必須分開兩件事

第一件：

$$
P=
\text{Provenance}
$$

即：

> 作品由誰、用什麼工具做出來。

第二件：

$$
D=
\text{Distinctiveness}
$$

即：

> 作品本身有沒有明確差異、人格與辨識度。

兩者不是同一件事。

因此：

$$
\boxed{
P
\not\Rightarrow
D
}
$$

更進一步：

$$
\boxed{
\text{Human Provenance}
\not\Rightarrow
\text{High Distinctiveness}
}
$$

同樣：

$$
\boxed{
\text{AI Assistance}
\not\Rightarrow
\text{Low Distinctiveness}
}
$$

---

# 3. 來源與風格正在脫鉤

過去很多人直覺認為：

$$
\text{Human}
\rightarrow
\text{Unique}
$$

$$
\text{AI}
\rightarrow
\text{Generic}
$$

但這個對應在快速失效。

未來更合理的是：

$$
\boxed{
\text{Provenance}
\perp
\text{Style}
}
$$

也就是：

- 人類可以做得很模板；
- AI 可以做得很怪；
- 人類可以高度同質；
- AI 可以在強限制下非常一致且獨特；
- Hybrid pipeline 也可以具有極強作者性。

所以來源不能再被當成風格代理變數。

---

# 4. AI 為什麼容易同質化

AI 生成的同質化可以粗略理解為：

$$
\boxed{
\text{Statistical Attractor}
}
$$

模型在大量資料分布中學到：

$$
P(x)
$$

在沒有強約束時，生成結果容易朝：

$$
\arg\max_x P(x)
$$

附近收斂。

也就是：

$$
\boxed{
\text{高概率、低風險、平均可接受}
}
$$

的區域。

所以常見結果會出現：

- 相似臉型；
- 相似打光；
- 相似構圖；
- 相似文句節奏；
- 相似角色 archetype；
- 相似產品 wording。

---

# 5. 但人類也有自己的「統計吸引子」

人類不是沒有分布。

一個創作者長期工作後，也會形成自己的：

$$
P_H(x)
$$

也就是：

- 慣用臉型；
- 慣用配色；
- 慣用構圖；
- 慣用角色性格；
- 慣用劇情節奏；
- 慣用 UI；
- 慣用系統解法；
- 慣用程式架構。

所以：

$$
\boxed{
\text{Human Creator}
}
$$

本身也會形成：

$$
\boxed{
\text{Personal Attractor Basin}
}
$$

---

# 6. 人類同質化不是 Bug，而是效率策略的自然結果

當創作者需要大量產出：

$$
N\uparrow
$$

且時間：

$$
T
$$

固定，

則每個作品可投入的探索時間：

$$
E
\approx
\frac{T}{N}
$$

因此：

$$
N\uparrow
\Rightarrow
E\downarrow
$$

探索越少：

$$
\boxed{
\text{Reuse Existing Solution}
}
$$

就越合理。

所以：

$$
\boxed{
\text{高產量}
\rightarrow
\text{模板化}
}
$$

不是 AI 專屬問題。

它是任何受限創作者都可能出現的資源配置結果。

---

# 7. 同質化吸引子模型

定義：

$$
H_t
=
\text{Homogenization Level at time }t
$$

則可寫：

$$
H_{t+1}
=
H_t
+
\alpha R
+
\beta P
+
\gamma C
+
\delta M
-
\epsilon X
$$

其中：

- $R$：Reuse Pressure，重用壓力；
- $P$：Production Pressure，產量壓力；
- $C$：Constraint Narrowness，限制狹窄程度；
- $M$：Market Convergence，市場收斂；
- $X$：Exploration，探索強度。

所以若：

$$
R,P,C,M\uparrow
$$

而：

$$
X\downarrow
$$

則：

$$
\boxed{
H\uparrow
}
$$

無論創作者是：

$$
\text{Human}
$$

或：

$$
\text{AI}
$$

都可能成立。

---

# 8. 人類自我模仿是最容易被忽略的來源

創作者會自然形成：

$$
\boxed{
\text{Self-Imitation}
}
$$

因為：

- 過去這樣成功；
- 這種畫法最快；
- 這種角色最好畫；
- 這種故事最熟；
- 這種系統自己最會寫。

所以：

$$
\text{PastSuccess}
\rightarrow
\text{Reuse}
$$

長期後：

$$
\boxed{
\text{Personal Style}
}
$$

可能逐步退化為：

$$
\boxed{
\text{Personal Template}
}
$$

這兩者很像，但不一樣。

---

# 9. Style 與 Template 的差異

Style 是：

$$
\boxed{
\text{可辨識的一致性}
}
$$

Template 是：

$$
\boxed{
\text{缺乏必要差異的重複}
}
$$

所以：

$$
\text{Consistency}
\neq
\text{Homogeneity}
$$

真正成熟的創作者需要：

$$
\boxed{
\text{Stable Identity}
+
\text{Internal Variation}
}
$$

而不是：

$$
\text{Same Face}
+
\text{Different Hair}
$$

或：

$$
\text{Same Plot}
+
\text{Different Names}
$$

---

# 10. 同一張臉換髮型，是最典型的低差異生成

可以把角色設計寫成：

$$
C_i
=
F_i
+
H_i
+
B_i
+
K_i
+
S_i
$$

其中：

- $F$：Face；
- $H$：Hair；
- $B$：Body；
- $K$：Costume；
- $S$：Silhouette。

若大量角色只改：

$$
H_i,K_i
$$

而：

$$
F_i,S_i
$$

高度固定，

玩家就會感覺：

$$
\boxed{
\text{Characters are different in data, but not different in perception.}
}
$$

這正是很多「像 AI」感的來源。

---

# 11. 「人類畫的」不能免除辨識度責任

假設創作者證明：

$$
\text{AIUsage}=0
$$

這只能回答：

> 來源是人類。

它不能回答：

> 為什麼角色彼此太像？

所以：

$$
\boxed{
\text{Provenance Defense}
}
$$

不能直接解決：

$$
\boxed{
\text{Design Homogeneity}
}
$$

如果問題是：

> 所有角色都很像。

回答：

> 但都是我手畫的。

其實沒有處理原問題。

---

# 12. AI 可以被用來反同質化

這又是一個反直覺點。

很多人認為：

$$
\text{AI}
\rightarrow
\text{Homogenization}
$$

但 AI 也可以被用來：

$$
\boxed{
\text{Increase Search Space}
}
$$

例如一次探索：

- 20 種臉型；
- 30 種 silhouette；
- 15 種服裝語法；
- 不同年齡；
- 不同文化；
- 不同體態；
- 不同角色氣質。

然後人類再選：

$$
\boxed{
\text{Which Difference Matters?}
}
$$

所以：

$$
\text{AI}
$$

既可以：

$$
\text{Compress Diversity}
$$

也可以：

$$
\text{Expand Diversity Search}
$$

取決於：

$$
\boxed{
\text{How It Is Used}
}
$$

---

# 13. AI 的真正問題可能不是生成，而是缺乏選擇

如果流程是：

$$
\text{Prompt}
\rightarrow
\text{Image}
\rightarrow
\text{Use}
$$

那很容易得到平均化內容。

但如果流程是：

$$
\text{Prompt}
\rightarrow
\text{50Variants}
\rightarrow
\text{Critique}
\rightarrow
\text{Recombine}
\rightarrow
\text{Reject}
\rightarrow
\text{Refine}
\rightarrow
\text{Use}
$$

則：

$$
\boxed{
\text{Selection Density}
}
$$

大幅提升。

因此真正重要的變量不是：

$$
\text{AIUsage}
$$

而是：

$$
\boxed{
\text{SelectionDensity}
}
$$

---

# 14. Selection Density

定義：

$$
D_S
=
\frac{
\text{Meaningful Selection Decisions}
}{
\text{Final Output Units}
}
$$

如果一張圖：

> 生一張就用。

則：

$$
D_S
$$

低。

如果一張圖經過：

- 20 個概念；
- 6 個方向；
- 3 次重組；
- 4 次否決；
- 2 次局部重畫；
- 最後人工整合；

那：

$$
D_S
$$

高。

所以：

$$
\boxed{
\text{High AI Usage}
+
\text{High Selection Density}
}
$$

完全可能比：

$$
\text{Human Only}
+
\text{Low Selection Density}
$$

更有作者性。

---

# 15. Identity Density

定義：

$$
D_I
=
\frac{
\text{Distinctive Identity Decisions}
}{
\text{Content Volume}
}
$$

一個作品如果：

- 角色很多；
- 圖很多；
- 任務很多；
- 系統很多；

但真正有辨識度的選擇很少，

那：

$$
D_I\downarrow
$$

所以：

$$
\boxed{
\text{Content Count}
\neq
\text{Identity Density}
}
$$

這在 AI 時代會變得尤其重要。

---

# 16. 高產量可能稀釋身份密度

假設：

$$
I
=
\text{Identity Decisions}
$$

$$
N
=
\text{Content Units}
$$

則：

$$
D_I
=
\frac{I}{N}
$$

如果創作者只增加：

$$
N\uparrow
$$

但：

$$
I
$$

沒有同比例增加，

則：

$$
\boxed{
D_I\downarrow
}
$$

結果就是：

> 內容很多，但都像。

---

# 17. 人類創作也會有「平均化模型」

一個成熟但沒有自我挑戰的創作者，腦中也會形成：

$$
\boxed{
\text{Internal Predictive Model}
}
$$

例如：

> 玩家喜歡這種。

> 這種角色最安全。

> 這種 UI 最穩。

> 這種故事最容易。

久而久之：

$$
\text{Human Decision}
$$

也會變成：

$$
\boxed{
\arg\max P_H(x)
}
$$

也就是：

> 選自己最熟、最可能成功的局部最優。

這和 AI 的高概率生成，結構上其實很像。

---

# 18. 所以「AI 平均化」其實是一個更一般的優化問題

更廣義地說：

$$
\boxed{
\text{Homogenization}
=
\text{Repeated Optimization Toward Local Safe Optima}
}
$$

只要系統一直選：

- 最安全；
- 最熟悉；
- 最快；
- 最便宜；
- 最可接受；

最後就會：

$$
\boxed{
\text{Converge}
}
$$

這和執行者是：

- AI；
- 人類；
- 公司；
- 編輯；
- 市場；

沒有本質必然關係。

---

# 19. 市場也會製造同質化

即使創作者想創新，市場可能給：

$$
Reward(x)
$$

當某種內容成功：

$$
Reward(x^*)\uparrow
$$

其他創作者會模仿：

$$
x_i\rightarrow x^*
$$

結果：

$$
\boxed{
\text{Market Attractor}
}
$$

形成。

所以：

$$
\boxed{
\text{同質化不只是生成模型問題，也是市場選擇問題。}
}
$$

---

# 20. 平台演算法也會塑造吸引子

平台推薦：

$$
R(x)
$$

會偏好：

- 點擊率；
- 停留；
- 完播；
- 轉化。

創作者於是學習：

$$
\arg\max_x R(x)
$$

結果：

$$
\boxed{
\text{Algorithmic Selection}
\rightarrow
\text{Creative Convergence}
}
$$

所以即使完全不用 AI：

$$
\boxed{
\text{平台演算法仍然可以把人類創作推向模板化。}
}
$$

---

# 21. 來源鑑識會越來越困難

當：

$$
\text{HumanOutput}
\rightarrow
\text{AILike}
$$

且：

$$
\text{AIOutput}
\rightarrow
\text{HumanLike}
$$

兩者分布：

$$
P_H(x)
$$

與：

$$
P_A(x)
$$

會逐步重疊。

即：

$$
\boxed{
D_{KL}(P_H\parallel P_A)
\downarrow
}
$$

粗略表示：

> 光看作品本身，來源越來越難判斷。

因此未來：

$$
\boxed{
\text{Style Detection}
}
$$

很難取代：

$$
\boxed{
\text{Provenance Verification}
}
$$

---

# 22. 「AI 味」最後可能變成時代風格，而不是來源證據

就像某些年代有：

- 網頁 2.0 味；
- 手遊味；
- Unity Indie 味；
- 90 年代 CGI 味。

未來：

$$
\boxed{
\text{AI-like}
}
$$

可能只是描述：

> 某一時代的平均美學。

而不是：

> 這就是 AI 做的。

因此：

$$
\boxed{
\text{AI-like Aesthetic}
\neq
\text{AI Provenance}
}
$$

---

# 23. 真正的反同質化不是「禁止 AI」

如果人類本身也會模板化，

那：

$$
\text{AI}=0
$$

並不能保證：

$$
\text{Homogeneity}=0
$$

所以更有效的策略是：

$$
\boxed{
\text{Increase Exploration}
+
\text{Increase Critique}
+
\text{Increase Selection}
+
\text{Increase Identity Constraints}
}
$$

也就是：

$$
\boxed{
\text{反同質化是一個設計流程問題。}
}
$$

---

# 24. Art Direction 才是真正的核心

Art Direction 不只是：

> 選顏色。

而是：

$$
\boxed{
\text{Define What Must Differ}
+
\text{Define What Must Stay Coherent}
}
$$

例如：

- 哪些角色臉型一定要拉開；
- 哪些派系輪廓必須不同；
- 哪些配色可以共享；
- 哪些技術語言不能混；
- 哪些場景要保留共同世界感。

所以：

$$
\boxed{
\text{Good Art Direction}
=
\text{Controlled Diversity}
}
$$

---

# 25. 敘事也有同樣問題

AI 文本容易：

- 語氣平均；
- 太完整；
- 太順；
- 缺少怪癖。

但人類大量寫作也可能：

- 每個角色都像作者本人；
- 每場對話節奏一樣；
- 每個反派都同一種邏輯；
- 每個笑點都同一套路。

因此：

$$
\boxed{
\text{Character Voice Diversity}
}
$$

同樣不能靠：

> 人類寫的。

自動保證。

---

# 26. 程式與系統設計也會同質化

同質化不是只有美術。

程式設計者也可能：

> 每次都用同一種架構。

遊戲設計者也可能：

> 每次都加 Level、Skill、Currency、Quest。

所以：

$$
\boxed{
\text{Design Homogeneity}
}
$$

也是一種吸引子。

甚至：

$$
\boxed{
\text{Feature-Oriented Development}
}
$$

本身就可能是一種個人模板。

---

# 27. 人類作者性真正來自「哪些地方不跟平均值走」

可以把作者性寫成：

$$
A
=
\sum_i
w_i
\cdot
\Delta_i
$$

其中：

$$
\Delta_i
=
\text{Deviation from Expected Default}
$$

但不是所有偏離都好。

真正有價值的是：

$$
\boxed{
\text{Intentional, Coherent Deviation}
}
$$

即：

> 我知道平均答案是什麼，但我選擇不那樣做，而且這個偏離與整體作品一致。

---

# 28. 這就是「選擇密度」的核心

作者性不是：

> 我每一步都親手做。

而是：

$$
\boxed{
\text{我在哪些關鍵地方做出了不可替代的選擇。}
}
$$

所以：

$$
\boxed{
\text{Manual Action Density}
\neq
\text{Authorial Selection Density}
}
$$

這兩者未來必須分開。

---

# 29. 高作者性 AI 作品是可能的

若流程：

$$
\text{Human}
\rightarrow
\text{Define Constraints}
\rightarrow
\text{AI}
\rightarrow
\text{Explore}
\rightarrow
\text{Human}
\rightarrow
\text{Select}
\rightarrow
\text{AI}
\rightarrow
\text{Refine}
\rightarrow
\text{Human}
\rightarrow
\text{Integrate}
$$

則最終：

$$
\boxed{
\text{AI Usage High}
}
$$

但：

$$
\boxed{
\text{Human Authorial Control High}
}
$$

完全可能同時成立。

---

# 30. 低作者性純人類作品也可能存在

相反：

$$
\text{HumanOnly}
$$

但流程：

$$
\text{Reuse Old Template}
\rightarrow
\text{Repeat}
\rightarrow
\text{Ship}
$$

則：

$$
\boxed{
\text{Human Labor High}
}
$$

但：

$$
\boxed{
\text{Authorial Selection Density Low}
}
$$

所以純人類並不是作者性的充分條件。

---

# 31. 人類復古真正不能賣「來源純潔性」而已

如果未來 Human-Retro 市場只賣：

> 100% 沒用 AI。

但作品：

- 沒差異；
- 沒作者性；
- 沒更高品質；
- 沒文化意義；

那：

$$
\boxed{
\text{Human-Retro}
}
$$

很容易退化成：

$$
\boxed{
\text{Purity Branding}
}
$$

而不是：

$$
\text{Creative Value}
$$

---

# 32. Human-Retro 更合理的賣點

未來真正強的 Human-Retro 作品應該讓人感受到：

$$
\boxed{
\text{這不是「沒有 AI」，而是「有一個非常清楚的人在裡面」。}
}
$$

也就是：

$$
\boxed{
\text{Presence of Human Agency}
>
\text{Absence of AI}
}
$$

這一句是本篇最重要的結論之一。

---

# 33. 一個簡化的反同質化模型

定義：

$$
D
=
\text{Distinctiveness}
$$

可以粗略寫：

$$
D
=
E
+
S
+
I
+
C
-
H
$$

其中：

- $E$：Exploration；
- $S$：Selection Density；
- $I$：Identity Constraints；
- $C$：Critical Review；
- $H$：Homogenization Pressure。

因此：

$$
\boxed{
D\uparrow
}
$$

不需要：

$$
AI\downarrow
$$

只需要：

$$
E,S,I,C\uparrow
$$

並控制：

$$
H
$$

---

# 34. 對創作者的實務檢驗

可以定期問：

### Q1
如果把角色名字遮掉，我還分得出誰是誰嗎？

### Q2
如果全部轉灰階，silhouette 還能辨識嗎？

### Q3
如果拿掉來源標籤，作品仍然有作者性嗎？

### Q4
這十個設計裡，有多少其實是同一個模板？

### Q5
哪些地方是「因為我一直這樣做」，而不是「因為這次真的應該這樣做」？

### Q6
AI 是在增加探索空間，還是在複製平均答案？

### Q7
我有沒有真正拒絕過自己的第一個安全答案？

---

# 35. 本篇與系列後續的關係

第一篇處理：

$$
\text{Human-Made 變稀缺}
$$

第二篇處理：

$$
\text{稀缺不等於價值}
$$

第三篇進一步證明：

$$
\boxed{
\text{人類來源本身也不等於差異。}
}
$$

所以系列開始真正走向：

$$
\boxed{
\text{Value}
\rightarrow
\text{Selection}
\rightarrow
\text{Authorial Agency}
}
$$

下一篇將從市場端處理：

> 玩家、讀者、觀眾到底在買什麼？

也就是：

$$
\boxed{
\text{玩家買的是體驗，不是製程純潔性。}
}
$$

---

# 36. 結論

AI 時代最容易犯的錯誤之一，是把：

$$
\text{AI}
$$

與：

$$
\text{Homogeneity}
$$

直接畫上等號。

但：

$$
\boxed{
\text{同質化不是 AI 專屬現象。}
}
$$

它更一般地來自：

$$
\boxed{
\text{高產量}
+
\text{低探索}
+
\text{安全局部最優}
+
\text{市場收斂}
+
\text{缺乏外部審核}
}
$$

所以人類完全可能：

$$
\boxed{
\text{畫出「像 AI」的作品。}
}
$$

而 AI 也完全可能在強烈人類選擇、強 Art Direction、強世界約束下，產生高度有作者性的結果。

因此未來真正重要的，不是：

> 這到底是不是 AI 做的？

而是：

$$
\boxed{
\text{這個作品裡，到底有多少真正不可替代的選擇？}
}
$$

真正有價值的人類作者性，不是：

$$
\boxed{
\text{Absence of AI}
}
$$

而是：

$$
\boxed{
\text{Presence of Distinctive Human Agency}
}
$$

也就是：

> 即使不知道製程，我仍然能感受到——這不是平均答案。

這才是 Human-Retro 真正需要保存的東西。
