---
title: "近期性失真與使用者印象漂移：AI 如何把「最近的你」誤認成「整體的你」"
english_title: "Recency Distortion and User-Impression Drift: How AI Can Mistake the Recent You for the Whole You"
author: "Neo.K（許筌崴）"
institution: "EveMissLab（一言諾科技有限公司）"
series: "符號—記憶—判定耦合系列"
paper_no: "06"
version: "v0.1"
date: "2026-08-13"
status: "正式研究草稿"
canonical_source_encoding: "UTF-8"
---

# 近期性失真與使用者印象漂移：AI 如何把「最近的你」誤認成「整體的你」

**Recency Distortion and User-Impression Drift: How AI Can Mistake the Recent You for the Whole You**

作者：Neo.K（許筌崴）  
機構：EveMissLab（一言諾科技有限公司）  
系列：符號—記憶—判定耦合系列，第 6 篇  
版本：v0.1  
日期：2026 年 8 月 13 日

---

## 摘要

長期個人化 AI 必須同時解決兩個看似矛盾的要求：一方面，它必須快速吸收使用者的新狀態、新偏好、新專案與新修正；另一方面，它又不能讓最近幾輪、最近幾天或最近一個高頻主題覆蓋數月乃至數年的長期證據結構。若更新過慢，系統會把過去的使用者固定成今天的使用者；若更新過快，系統則可能把「最近的你」誤認成「整體的你」。

本文提出「近期性失真」（Recency Distortion, RD）與「使用者印象漂移」（User-Impression Drift, UID）作為兩個相互關聯但不可混同的候選概念。RD 指系統在建立當前使用者模型時，近期證據的權重相對於其真實時間持續性、任務適用域與歷史重要度過高，導致短期狀態、近期工具、高頻詞彙或當前專案被錯誤提升為長期核心特徵。UID 則指系統當下實際用於推理的使用者表示，逐漸偏離一個以多時間尺度、來源、版本、持續性與反證共同校準的「證據平衡使用者軌跡」。

本文明確拒絕把所有此類現象簡化成「記憶更新太快」。至少存在四種機制上可分離的漂移來源：

$$
\boxed{
\text{Update Drift}
+
\text{Retrieval Drift}
+
\text{Synthesis Drift}
+
\text{Scope-Transfer Drift}
}
$$

第一，記憶或 persona 表示本身被過快改寫；第二，舊資料仍存在但未在正確時空被調用；第三，新舊證據都被提取，卻在合成當前印象時權重錯配；第四，某一局部任務中成立的特徵被錯誤泛化成全域人格或能力判定。

本文進一步提出「異質時間尺度使用者模型」：使用者資訊不應共享同一衰減率或更新增益，而應依據其時間持續性分成至少四類——瞬時狀態、活躍情境、持續偏好／能力結構、長期軌跡／身份歷史。若所有資訊使用同一 recency kernel，系統就容易把：

$$
\text{近期高頻}
\Rightarrow
\text{長期重要}
$$

$$
\text{近期工具}
\Rightarrow
\text{核心理論}
$$

$$
\text{低術語密度}
\Rightarrow
\text{低專業程度}
$$

$$
\text{當前探索}
\Rightarrow
\text{長期無知}
$$

等弱代理錯認成穩定使用者特徵。

本文承接《記憶動力學》《從查表到記得》與本系列 Paper 05「共感記憶域」，並與 2025–2026 年長期個人化對話、PersonaTree、Reflective Memory Management、APEX-MEM、Temporal Semantic Memory、LongMP-Bench、LoCoMo-Plus 等研究對照。本文提出七項可證偽命題、六組 benchmark 設計與多項候選指標，包括 Recency Overweight Index、Temporal-Class Confusion、Impression Drift Distance、Retrieval Omission Rate、Scope Leakage Rate 與 Trajectory Recovery Score。

**關鍵詞：** 近期性失真、使用者印象漂移、長期個人化、persona drift、memory retrieval、時間尺度、共感記憶域、使用者建模、長期對話、歷史軌跡、AI 記憶、證據權重

---

# 0. 理論位置與邊界

## 0.1 本文不是對特定產品底層實作的逆向推斷

本文起點來自一類可觀察的人機互動現象：一個長期互動系統可能明明「有」很多歷史資料，卻在某一輪形成顯著偏向近期內容的使用者印象。

但從使用者可見輸出，不能直接推出：記憶是否被保存、保存在哪一層、何時被更新、是否使用向量檢索、是否有 persona model、是否被摘要覆蓋、是否由模型本身或外部系統完成加權。

因此本文只建立**可觀測功能層的候選模型**。

## 0.2 與《記憶動力學》的接口

《記憶動力學》已明確區分：

$$
\text{存在}
\neq
\text{可達}
\neq
\text{可提取}
\neq
\text{可報告}
\neq
\text{可用於行動}
$$

並把提取建模為當前狀態、情境與線索共同作用下的重構：

$$
\widehat m_t
=
\mathcal R
(
m^{trace},
C_t,
X_t,
\Pi_t,
O_t,
\mathcal Q_t
)
$$

所以「AI 沒有使用某段舊記憶」並不能直接推出：

$$
m_{old}
\notin
\mathfrak M
$$

它也可能只是沒有被當前檢索到，或雖然被檢索到卻在合成時權重很低。

## 0.3 與《從查表到記得》的接口

《從查表到記得》把 AI 連續性問題放在「狀態持續演化」與「每次重新查表」的差異上，並提出內外記憶庫與熱／溫／冷層等架構構想。

本文不評估該工程方案是否最優，只取更抽象的問題：

$$
\boxed{
\text{即使歷史資料存在，
當前活躍使用者狀態仍可能被錯誤重建。}
}
$$

## 0.4 與 Paper 05 的接口

Paper 05 的「共感記憶域」提出：

$$
\mathcal E_{AB}^{(\tau)}
=
\{
m:
\Psi_\tau(m)\ge\theta_\tau
\}
$$

即不是所有舊記憶都應被激活，而是只有當前時空、關係與任務下適切的記憶應重新成為共同現在。

Paper 06 研究其失敗版本：真正應進入 $\mathcal E_{AB}^{(\tau)}$ 的舊而核心記憶沒有進來，而最近高頻但局部的內容大量進來時，使用者模型會發生什麼。

---

# 1. 使用者不是一個靜態 persona

## 1.1 靜態 persona 的不足

最簡單的個人化系統可以把使用者表示為：

$$
U
=
\{p_1,p_2,\ldots,p_n\}
$$

但長期使用者不是靜態集合。更一般地：

$$
U=U(t)
$$

且其中不同特徵具有完全不同的時間尺度。

## 1.2 四類時間持續性

本文提出最小四分類。

### A. 瞬時狀態 $S_t$

例如：現在很累、今天趕某事、此刻想用英文、這一輪只想快速回答。

典型尺度：

$$
\tau_S
\sim
\text{minutes / hours}
$$

### B. 活躍情境 $C_t^{active}$

例如：最近正在寫某系列論文、本週正在做某專案、最近頻繁使用某套工具、當前遊戲或研究主題。

典型尺度：

$$
\tau_C
\sim
\text{days / weeks / months}
$$

### C. 持續偏好、能力或方法結構 $P_t$

例如：長期語言偏好、穩定工作方法、某領域能力結構、一貫輸出格式要求、持續研究方法。

其尺度通常：

$$
\tau_P
\gg
\tau_C
$$

但仍可改變。

### D. 長期軌跡與歷史結構 $H_t$

它不是「永恆人格」，而是描述：怎麼走到現在、哪些概念是早期核心、哪些後來被修正、哪些只是近期工具、哪些理論已成熟、哪些偏好有版本史。

典型尺度：

$$
\tau_H
\sim
\text{months / years / lifetime}
$$

---

# 2. 近期性本身不是錯誤

## 2.1 沒有 recency，系統會僵化

如果使用者昨天已明確改變偏好：

$$
p_{t-1}
\rightarrow
p_t
$$

但系統仍永遠使用：

$$
p_{t-k}
$$

就會形成：

$$
\boxed{
\text{Stale-Persona Error}
}
$$

也就是「過去的你」壓過「現在的你」。

## 2.2 問題是時間尺度錯配

近期性失真不是 $w_{recent}>w_{old}$ 本身，而是：

$$
\boxed{
w(m_i\mid t)
\text{ 與 }
\tau_{persistence}(m_i)
\text{ 不匹配}
}
$$

若一段資訊是瞬時狀態，近期性應高；若一段資訊代表長期穩定偏好，一次偶發反例不應立即完全覆寫。

因此理想更新應具有：

$$
\eta_i
=
f(
\text{feature class},
\text{evidence strength},
\text{contradiction},
\text{duration}
)
$$

而不是所有記憶共享同一更新率。

---

# 3. 近期性失真與使用者印象漂移

## 3.1 活躍使用者印象

定義系統在時間 $t$ 真正用於推理的使用者印象為：

$$
\widehat U_t
=
F
\left(
\{m_i,w_i(t)\}_{i=1}^{n},
C_t,
T_t
\right)
$$

這不是完整記憶庫，而是當前被合成後的使用者工作表示。

## 3.2 證據平衡參照軌跡

本文不使用「真實人格」作為 ground truth，因為使用者本身持續改變，外部系統也無法直接觀察主體全部內部狀態。

因此定義：

$$
U_t^{\star}
$$

為**證據平衡參照軌跡**：在指定任務域中，以跨時間、多來源、版本、反證與持續性資訊重建出的最佳可用使用者表示。

它是 benchmark reference，不是形上學的「真正自我」。

## 3.3 使用者印象漂移

定義：

$$
\boxed{
\Delta_U(t)
=
d_U
\left(
\widehat U_t,
U_t^{\star}
\right)
}
$$

當 $\Delta_U(t)$ 上升，表示當前活躍印象偏離多時間尺度證據平衡表示。

## 3.4 近期性失真

令 $W_R$ 為近期證據總有效權重， $W_H$ 為歷史高持續性證據權重。

定義候選指標：

$$
RD_t
=
\frac{W_R/W_H}{\Omega_T}
$$

其中 $\Omega_T$ 表示在任務 $T$ 下合理的近期／歷史權重比例。

若：

$$
RD_t\gg1
$$

才可稱近期被過度放大。

---

# 4. 四種不可混同的漂移機制

## 4.1 Update Drift：更新漂移

舊表示真的被新資訊改寫：

$$
P_{old}
\rightarrow
P_{new}
$$

但新證據其實只是一個短期例外。

這是：

$$
\boxed{
\text{Memory / Persona State Overwrite}
}
$$

## 4.2 Retrieval Drift：提取漂移

舊資訊其實仍在：

$$
m_{old}
\in
\mathfrak M
$$

但：

$$
m_{old}
\notin
\mathcal M_t^{ret}
$$

原因可能是 query 不匹配、semantic similarity 太低、時間線索不足、最近內容競爭、retrieval budget、索引粒度或 graph path 未走到。

這是：

$$
\boxed{
\text{Stored but Absent from the Present}
}
$$

## 4.3 Synthesis Drift：合成漂移

新舊資訊都被取出：

$$
m_{old},m_{recent}
\in
\mathcal M_t^{ret}
$$

但當前合成 $\widehat U_t$ 仍讓近期資訊權重過高：

$$
w_{recent}
\gg
w_{old-core}
$$

即使後者證據強度更高。

## 4.4 Scope-Transfer Drift：作用域轉移漂移

某特徵在局部任務成立：

$$
p
\in
D_{local}
$$

卻被推成：

$$
p
\in
D_{global}
$$

例如最近研究某工具，被錯誤推出它是長期核心；某輪要求白話，被錯誤推出使用者能力低；某個專案採用某風格，被推出使用者永遠偏好該風格。

形式上：

$$
\boxed{
\operatorname{Valid}(p,D_i)
\not\Rightarrow
\operatorname{Valid}(p,D_j)
}
$$

---

# 5. 高頻與重要必須分離

令：

$$
f_t(x)
$$

為概念 $x$ 在近期窗口中的出現頻率，而：

$$
I_H(x)
$$

為其長期結構重要度。

一般不保證：

$$
f_t(x)
\propto
I_H(x)
$$

某個臨時 debugging 問題可以一週出現百次，但完全不是使用者長期研究核心。

定義：

$$
A_t(x)
=
\text{近期活躍度}
$$

$$
K_t(x)
=
\text{長期核心度}
$$

錯誤推論：

$$
A_t(x)\uparrow
\Rightarrow
K_t(x)\uparrow
$$

本文稱為：

$$
\boxed{
\text{Activity–Core Confusion}
}
$$

---

# 6. 表面語言不應直接成為能力代理

Paper 02 與 Paper 03 已指出，一個主體可能故意使用低承諾基本語言進行 rebase、scale shift 或 domain calibration。

因此：

$$
L_{terminology}
$$

即術語密度，不應被直接映射到：

$$
C_{expertise}
$$

簡單措辭可能同時出現在初學、教學、重新基準化、跨域對齊、故意降低本體承諾與高階抽象壓縮。

所以只以表面詞彙密度判定熟練程度，屬於：

$$
\boxed{
\text{Surface-Proxy Misclassification}
}
$$

---

# 7. 探索行為不等於無知

長期研究者也會問：「這到底是什麼？」

此問句可能具有多種功能：

$$
Q
\in
\{
\text{novice inquiry},
\text{definition audit},
\text{first-principles reset},
\text{boundary test},
\text{cross-domain remapping}
\}
$$

如果模型只看到問句形式並推：

$$
Q_{surface}
\Rightarrow
\text{novice}
$$

就忽略了對話歷史與任務角色。

---

# 8. 外部研究正在碰到的相鄰問題

## 8.1 Memory noise 與 persona inconsistency

2026 年 ACL 的 PersonaTree／Inside Out 工作明確指出，長期個人化系統在無界互動流與有限 context 之間會面臨 memory noise accumulation、reasoning degradation 與 persona inconsistency。其框架以全域 PersonaTree 維持長期 user profile，並使用 ADD、UPDATE、DELETE、NO_OP 等可控操作更新 persona 結構。

這支持一個最低工程事實：

$$
\text{More Interaction}
\neq
\text{Better User Model}
$$

## 8.2 固定粒度與固定 retrieval 不足

Reflective Memory Management 指出，rigid memory granularity 會造成 fragmented/incomplete representation，而 fixed retrieval 無法適應不同 dialogue context 與 user interaction pattern。

這與 Retrieval Drift 相鄰，但本文再區分：即使 retrieval 正確，後續合成與作用域泛化仍可出錯。

## 8.3 長短期記憶本來就需要分離

LD-Agent 將 long-term memory 與 short-term memory 分開，並另外動態建模 user/agent persona。

因此工程研究本身已經承認：

$$
\boxed{
\text{Recent Context}
\neq
\text{Long-Term Persona}
}
$$

## 8.4 時間不是只有「對話發生時間」

Temporal Semantic Memory 類工作指出，若只按 dialogue time 組織記憶，可能混淆事件真正發生時間；point-wise memory 也會丟失持續狀態與演化模式。

所以：

$$
\boxed{
\text{Temporal Index}
\neq
\text{Temporal Meaning}
}
$$

一段今天才說出的「我三年前一直做 X」，statement time、event time 與 duration 是不同變量。

## 8.5 Evolving Persona 已成為 benchmark 問題

2026 年 LongMP-Bench 把追蹤 evolving user personas 明確列為長期對話理解能力的一部分。

因此：

$$
\text{fixed persona}
$$

應逐步轉向：

$$
\text{persona trajectory}
$$

## 8.6 隱含限制比 factual recall 更難

LoCoMo-Plus 將 long-term memory 評估推到 implicit constraints：使用者狀態、目標與價值即使沒有在後面被逐字重問，也應在適當情境中被正確應用。

因此：

$$
\boxed{
\text{Memory Quality}
\neq
\text{String Recall Accuracy}
}
$$

---

# 9. 兩側錯誤：漂移與凍結

## 9.1 Fast Update Failure

若：

$$
\eta
\gg
\eta^\star
$$

則：

$$
\text{transient signal}
\rightarrow
\text{persistent profile}
$$

形成 UID。

## 9.2 Slow Update Failure

若：

$$
\eta
\ll
\eta^\star
$$

則：

$$
\text{obsolete profile}
\rightarrow
\text{current inference}
$$

形成：

$$
\boxed{
\text{Persona Freeze}
}
$$

## 9.3 最佳更新是類別依賴的

不存在單一 $\eta^\star$，而是：

$$
\eta_c^\star
$$

其中：

$$
c
\in
\{S,C,P,H\}
$$

也就是瞬時、活躍、持續、歷史軌跡。

---

# 10. 版本化使用者模型

## 10.1 改變不等於刪除舊的

如果使用者：

$$
p_{2024}
\neq
p_{2026}
$$

合理表示不是：

$$
p_{2024}
\rightarrow
\varnothing
$$

而是：

$$
p_{2024}
\xrightarrow{\Delta}
p_{2026}
$$

長期 persona 更像：

$$
\boxed{
\text{Versioned Trajectory}
}
$$

而不是單一 mutable object。

## 10.2 保留反轉歷史

若使用者曾：

$$
A
\rightarrow
B
\rightarrow
A'
$$

其中 $A'\neq A$，只保留最後的 $A'$ 會失去「為什麼回到類似位置，但理由已經不同」。

所以：

$$
\boxed{
\text{Current State}
\neq
\text{Trajectory}
}
$$

---

# 11. 任務條件化使用者模型

同一使用者不需要在所有任務中激活同一 profile。

令：

$$
\widehat U_t^{(T)}
$$

表示任務 $T$ 下的活躍使用者表示。

數學研究可能需要形式化偏好、相關前作與符號規則；遊戲設計則需要不同記憶。

因此：

$$
\boxed{
\widehat U_t
\text{ 不應是一個對所有任務固定的單一人格 blob}
}
$$

---

# 12. 六種典型失真

## 12.1 高頻 → 核心

$$
f_t(x)\uparrow
\Rightarrow
K(x)\uparrow
$$

錯。

## 12.2 最近工具 → 長期身份

$$
\text{recent tool}
\Rightarrow
\text{identity}
$$

錯。

## 12.3 當前專案 → 全域興趣排序

$$
\text{active project}
\Rightarrow
\text{global priority}
$$

錯。

## 12.4 基本語言 → 初學者

$$
\text{simple wording}
\Rightarrow
\text{low expertise}
$$

錯。

## 12.5 最近修正 → 全域否定舊歷史

使用者說「這個地方我現在不這樣看」，不能直接推出所有先前相關觀點都無效。

## 12.6 當前情緒 → 穩定人格

$$
S_t
\Rightarrow
P_t
$$

錯。

---

# 13. 候選量化指標

## 13.1 Recency Overweight Index

$$
\operatorname{ROI}_T
=
\frac{
\sum_{i\in R}w_i
}{
\sum_{j\in H}w_j+\epsilon
}
\Big/
\Omega_T
$$

## 13.2 Temporal-Class Confusion

令真實標註類別：

$$
c_i
\in
\{S,C,P,H\}
$$

模型判定：

$$
\widehat c_i
$$

則：

$$
\operatorname{TCC}
=
P(
\widehat c_i\neq c_i
)
$$

尤其關注 $C\rightarrow P$ 與 $S\rightarrow P$。

## 13.3 Impression Drift Distance

$$
\operatorname{IDD}_t
=
d_U(
\widehat U_t,
U_t^\star
)
$$

## 13.4 Retrieval Omission Rate

對應被激活的舊核心記憶集合 $M_T^\star$：

$$
\operatorname{ROR}
=
1-
\frac{
|M_T^\star\cap M_t^{ret}|
}{
|M_T^\star|
}
$$

## 13.5 Scope Leakage Rate

$$
\operatorname{SLR}
=
\frac{
N_{invalid\ globalizations}
}{
N_{local\ attributes}
}
$$

## 13.6 Trajectory Recovery Score

給模型跨時點 probe，要求恢復：

$$
p_{t_1}
\rightarrow
p_{t_2}
\rightarrow
p_{t_3}
$$

並評估時序、轉變理由、過時標記與持續性，形成 $\operatorname{TRS}$。

---

# 14. 七項可證偽命題

## 命題一：單一時間衰減核不足

若使用同一 recency kernel 處理所有使用者資訊，其跨時間 persona consistency 與 task alignment 會低於異質時間尺度模型。

## 命題二：近期高頻可系統性誤導核心判定

構造 $x_{recent}$ 高頻但低核心、 $x_{old}$ 低頻但高核心。若模型穩定把前者判為更核心，支持近期性失真。

## 命題三：Update Drift 與 Retrieval Drift 可實驗區分

若完整記憶庫仍保存舊資料但 query-time 不取出，屬 Retrieval Drift；若 persona state 本身已覆寫，屬 Update Drift。

## 命題四：作用域提示能降低人格誤判

加入「這是最近專案，不代表長期核心」或結構化 scope metadata 後，預測：

$$
\operatorname{SLR}\downarrow
$$

## 命題五：軌跡表示優於最後狀態表示

在需要解釋「為什麼現在如此」的任務中，Trajectory Model 應優於 Latest-State Model。

## 命題六：舊而核心的記憶可比最近相似記憶更能改善任務

在 semantic similarity 相近時，加入長期核心證據應比加入更多近期表面相似內容更能改善任務充分對齊。

## 命題七：過度抗近期也會造成 persona freeze

若系統刻意降低所有近期資訊權重，對真實偏好改變的 adaptation latency 應上升。

因此最優不是：

$$
\operatorname{Recency}\rightarrow0
$$

而是：

$$
\boxed{
\text{Time-Scale-Calibrated Updating}
}
$$

---

# 15. 六組實驗設計

## 15.1 實驗 A：高頻近期 vs 舊核心

建立 500 輪歷史。早期明確定義長期核心理論 A；最近 30 輪高頻使用工具 B，但反覆註明 B 只是當前工具。

詢問：「這位使用者的核心理論是什麼？」

比較 raw history、recency retrieval、semantic retrieval、temporal-class retrieval 與 trajectory-aware model。

## 15.2 實驗 B：基本語言能力誤判

同一高階研究者在兩種情境：Formal 使用大量技術術語；Rebase 故意用基本語言重新問第一性問題。

測量模型對 expertise、confidence 與 recommended explanation level 是否不當下降。

## 15.3 實驗 C：局部—全域作用域

提供「最近三週研究 X」，同時提供「X 只是某專案工具，不是長期核心」。之後分別問最近在研究什麼、主要研究方法是什麼、長期核心理論是什麼，測量 scope leakage。

## 15.4 實驗 D：更新快慢雙側測試

在長期穩定偏好中插入一次 transient contradiction，以及多輪明確 persistent update。理想模型應 downweight 前者、採納後者。

## 15.5 實驗 E：記憶存在但不提取

給 agent 完整 memory DB，其中明確包含舊核心事實。改變 retrieval policy：recent-only、semantic-only、temporal-aware、RRMD-aware。

若錯誤消失於 retrieval 政策改變，而 store 不變，就能定位 Retrieval Drift。

## 15.6 實驗 F：軌跡問答

不是問「使用者現在喜歡什麼」，而是問「以前怎麼看、何時改變、哪個觀點只是過渡、現在保留了什麼」。

評估 chronology、cause、persistence、obsolete marking 與 scope。

---

# 16. 從 factual recall 到 latent constraints

長期記憶 benchmark 正在從 explicit fact recall 走向 latent constraint consistency。

真正的使用者核心往往不是一句：「我的核心原則是 X。」而是多年互動中反覆出現的選擇模式、排除條件、價值排序、方法偏好與自我修正規則。

所以：

$$
\boxed{
\text{User Model}
\neq
\text{Profile Fact List}
}
$$

但從行為推 latent preference 也有過度推斷風險。

因此任何 latent user model 都應保存：

$$
\operatorname{Evidence}
+
\operatorname{Confidence}
+
\operatorname{Scope}
+
\operatorname{Version}
$$

---

# 17. 記憶不只是中性個人化資料

近期 personalized-agent safety 研究已顯示，個人記憶可能改變模型的 intent inference。

本文不研究該安全攻擊面本身，但取得一個更一般的提醒：

$$
\boxed{
\text{Personal Memory}
\text{ 不是中性附加資訊}
}
$$

它會改變：

$$
P(
\text{interpretation}
\mid
q,U
)
$$

因此 UID 不只影響「懂不懂使用者」，也可能改變模型對意圖、風險、建議與決策的推斷。

---

# 18. User Impression 不是 User Essence

本文刻意使用：

$$
\widehat U_t
$$

而不是：

$$
U_{true}
$$

因為「整體的你」本身也不是一個可被外部系統完整讀取的固定物件。

論文中真正操作的是：

$$
U_t^\star
=
\text{evidence-balanced, task-bounded, temporally versioned representation}
$$

這避免把 persona research 偷換成「AI 可以客觀知道一個人的本質」。

---

# 19. 對長期 AI 協作的工程含義

## 19.1 每條記憶至少需要時間類型

候選元資料：

$$
m_i
=
\langle
content,
time,
class,
scope,
confidence,
source,
version
\rangle
$$

其中：

$$
class
\in
\{state,active,persistent,trajectory\}
$$

## 19.2 更新與提取應分開治理

$$
\operatorname{UpdatePolicy}
$$

與：

$$
\operatorname{RetrievalPolicy}
$$

不是同一件事。

「不要更新核心 persona」與「這一輪不要調核心 persona」完全不同。

## 19.3 局部工作模型不應污染全域使用者模型

可分：

$$
U_t^{global}
$$

$$
U_t^{project}
$$

$$
U_t^{session}
$$

更新 $U_t^{project}$ 不應自動更新 $U_t^{global}$，除非證據達到跨域門檻。

## 19.4 長期核心仍需反證機制

被標成 persistent 的屬性也不能永遠鎖死。

應允許：

$$
\operatorname{ContradictionAccumulation}
>
\theta_{update}
$$

後進行版本更新。

---

# 20. 失敗模式矩陣

| 表面現象 | 可能機制 | 不應直接推出 |
|---|---|---|
| 舊事沒被提到 | Retrieval Drift | 記憶已被刪除 |
| 最近主題被當核心 | Synthesis / Scope Drift | 系統只保存最近 |
| 舊偏好一直出現 | Update Freeze | 模型更尊重長期 |
| 同一錯誤跨任務出現 | Global profile contamination | 每個 retrieval 都錯 |
| 找到舊記憶但仍誤判 | Synthesis Drift | 檢索失敗 |
| 使用者新偏好沒被採用 | Slow update | 抗 recency 很好 |

此矩陣用來防止由輸出直接跳到底層機制。

---

# 21. Paper 05–06 的關係

Paper 05 問：

$$
\boxed{
\text{什麼過去此刻應進入共同現在？}
}
$$

Paper 06 問：

$$
\boxed{
\text{如果時間、權重與作用域選錯，
當前使用者印象會如何漂移？}
}
$$

因此：

$$
\mathcal E_{AB}^{(\tau)}
$$

是適切記憶候選域，而：

$$
\widehat U_t
$$

是所有被激活資訊合成後的使用者工作模型。

可以寫：

$$
\boxed{
\mathcal E_{AB}^{(\tau)}
\rightarrow
\widehat U_t^{(T)}
\rightarrow
J_T
}
$$

若第一箭頭出錯，偏向 Retrieval Drift；若第二箭頭出錯，偏向 Synthesis Drift。

---

# 22. 向 Paper 07 的轉折

即使一個 AI 的 $\widehat U_t$ 很準確，仍有另一個問題：使用者為什麼會把「你記得我」感受到成「你在乎我」或「你理解我」？

Paper 05 已經提出這只是一個 possible evidence signal，而不是邏輯等價。

Paper 07 將把這個問題獨立展開：

> **被記得的體驗：記憶提取如何成為關係訊號，而又為何不能被偷換成真正的關係本身。**

---

# 23. 結論

本文提出：

$$
\boxed{
\text{Recent You}
\neq
\text{Whole You}
}
$$

但也同時提出：

$$
\boxed{
\text{Old You}
\neq
\text{Current You}
}
$$

所以真正問題從來不是「應該相信最近，還是相信以前」，而是：

$$
\boxed{
\text{不同證據應在與其時間持續性、作用域、
來源與任務相匹配的尺度上被更新與調用。}
}
$$

本文把長期個人化失真拆成：

$$
\boxed{
\text{Update Drift}
+
\text{Retrieval Drift}
+
\text{Synthesis Drift}
+
\text{Scope-Transfer Drift}
}
$$

這個分解的重要性在於，它阻止我們看到一個奇怪 AI 印象時，直接跳到「它一定把舊記憶刪了」或「它一定只看最近幾十輪」。真正可能發生的是多種完全不同的功能失效。

一個成熟的長期使用者模型，也不應只是 latest profile 或 all-history summary，而應更接近：

$$
\boxed{
\text{multi-timescale}
+
\text{versioned}
+
\text{scope-aware}
+
\text{evidence-traceable}
+
\text{task-conditioned}
}
$$

的動態軌跡模型。

最終目標不是讓 AI 永遠記住一個固定的「你」，而是讓它在每一次當下，都有能力區分：

> 你現在正在做什麼；  
> 你最近經常做什麼；  
> 你長期反覆重視什麼；  
> 你以前曾經是什麼；  
> 以及這些東西究竟哪些有資格被用來理解此刻的你。

---

# 參考文獻

## A. 內部理論來源

Neo.K（許筌崴）. 2026a. 《從查表到記得：基於內外記憶庫的 AI 連續性架構》. EveMissLab Technical Report, EML-AI-2026-MEMORY-ARCH-v1.0.

Neo.K（許筌崴）. 2026b. 《記憶動力學：跨層接口、時間索引與重構性提取》. EveMissLab, v1.0.

Neo.K（許筌崴）. 2026c. 〈共感記憶域：長期交流中共同過去如何重新成為共同現在〉. 符號—記憶—判定耦合系列，第 5 篇.

Neo.K（許筌崴）. 2026d. 〈語義延遲綁定：低承諾語言、動態約束與概念生成〉. 符號—記憶—判定耦合系列，第 2 篇.

Neo.K（許筌崴）. 2026e. 〈認知導航語言：自然語言作為語義空間中的控制介面〉. 符號—記憶—判定耦合系列，第 3 篇.

## B. 外部學術對照

Xu, Xinchao, Zhibin Gou, Wenquan Wu, Zheng-Yu Niu, Hua Wu, Haifeng Wang, and Shihang Wang. 2022. “Long Time No See! Open-Domain Conversation with Long-Term Persona Memory.” *Findings of ACL 2022*. DOI: 10.18653/v1/2022.findings-acl.207.

Li, Hao, Chenghao Yang, An Zhang, Yang Deng, Xiang Wang, and Tat-Seng Chua. 2025. “Hello Again! LLM-powered Personalized Agent for Long-term Dialogue.” *NAACL 2025*, 5259–5276. DOI: 10.18653/v1/2025.naacl-long.272.

Tan, Zhen, et al. 2025. “In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents.” *ACL 2025*, 8416–8439. DOI: 10.18653/v1/2025.acl-long.413.

Chen, Yi-Pei, Noriki Nishida, Hideki Nakayama, and Yuji Matsumoto. 2025. “Post Persona Alignment for Multi-Session Dialogue Generation.” *Findings of EMNLP 2025*, 20184–20192. DOI: 10.18653/v1/2025.findings-emnlp.1098.

Zhao, Jihao, Ding Chen, Zhaoxin Fan, Kerun Xu, Mengting Hu, Bo Tang, Feiyu Xiong, and Zhiyu Li. 2026. “Inside Out: Evolving User-Centric Core Memory Trees for Long-Term Personalized Dialogue Systems.” *ACL 2026*, 13429–13446. DOI: 10.18653/v1/2026.acl-long.614.

Banerjee, Pratyay, Masud Moshtaghi, Shivashankar Subramanian, Amita Misra, and Ankit Chadha. 2026. “APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI.” *ACL 2026*, 16470–16489. DOI: 10.18653/v1/2026.acl-long.749.

Pham Van, Hung, et al. 2026. “MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents.” *Findings of ACL 2026*. Anthology ID: 2026.findings-acl.1408.

“Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents.” 2026. *Findings of ACL 2026*. Anthology ID: 2026.findings-acl.1496.

“LongMP-Bench: A Benchmark for Multimodal Persona Understanding in Long-Term Dialogues.” 2026. *Findings of ACL 2026*. Anthology ID: 2026.findings-acl.1159.

“LoCoMo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents.” 2026. *ACL 2026*. Anthology ID: 2026.acl-long.1150.

Guo, Jiahe, et al. 2026. “When Personalization Legitimizes Risks: Uncovering Safety Vulnerabilities in Personalized Dialogue Agents.” *ACL 2026*. Anthology ID: 2026.acl-long.1260.

---

# 附錄 A：最小符號表

| 符號 | 定義 |
|---|---|
| $\widehat U_t$ | 系統在時間 $t$ 實際用於推理的活躍使用者印象 |
| $U_t^\star$ | 多時間尺度、證據平衡的 benchmark 參照軌跡 |
| $\Delta_U(t)$ | 使用者印象漂移距離 |
| $S_t$ | 瞬時狀態 |
| $C_t^{active}$ | 活躍情境／近期專案 |
| $P_t$ | 持續偏好、能力或方法結構 |
| $H_t$ | 長期軌跡／歷史結構 |
| $\eta_c$ | 類別 $c$ 的更新增益 |
| $RD_t$ | 近期性失真 |
| $\operatorname{ROI}_T$ | Recency Overweight Index |
| $\operatorname{TCC}$ | Temporal-Class Confusion |
| $\operatorname{IDD}$ | Impression Drift Distance |
| $\operatorname{ROR}$ | Retrieval Omission Rate |
| $\operatorname{SLR}$ | Scope Leakage Rate |
| $\operatorname{TRS}$ | Trajectory Recovery Score |

---

# 附錄 B：正式提交前驗證清單

- [ ] 建立瞬時／活躍／持續／軌跡四類資訊的人工標註集。
- [ ] 驗證四類時間尺度是否比二分 short/long memory 有額外解釋力。
- [ ] 分別測量 Update Drift、Retrieval Drift、Synthesis Drift、Scope-Transfer Drift。
- [ ] 建立近期高頻但低核心、舊而低頻但高核心的對抗資料。
- [ ] 驗證 simple wording → novice 的表面代理誤判。
- [ ] 測量 persona freeze 與 recency distortion 的雙側 trade-off。
- [ ] 比較 latest-state、flat-summary、trajectory-aware 三種 user model。
- [ ] 對 temporal semantic memory、persona evolution、latent-constraint benchmark 做更完整文獻對照。
- [ ] 研究 safety personalization 中 memory-induced intent bias 與 UID 是否可共享部分機制。
- [ ] 為 Paper 07 建立「記憶準確性 vs perceived care／responsiveness」的獨立實驗接口。
