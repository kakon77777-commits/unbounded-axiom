# EXS-06｜機器不是終點：數位、生物、混合與分散式智能載體
## 從 AI 機器到 Intelligence-Bearing Substrate 的多軸分類

**系列：** Human Capability Externalization & Intelligence Substrate Evolution Series  
**系列中文名：** 人類能力外部化與智能載體演化系列  
**編號：** EXS-06  
**版本：** v1.0  
**日期：** 2026-08-18  
**狀態：** Canonical Source / UTF-8 Markdown  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

EXS-05 將「能執行 AI 的機器」與「AI 原生系統」分離，指出 AI 是否存在於設備中，不足以描述 AI 在架構中的中心性。然而，「機器」本身仍是一個歷史性分類：它暗示智能主要由電子、數位與機械裝置承載。若未來計算與智能功能可以由神經形態硬體、物理動力系統、生物組織、器官類器官、軟體—生物混合系統、腦機介面或跨大量節點的分散式系統承載，則「AI 機器」將無法覆蓋所有可能的智能實現。

本文提出更一般的概念：

$$
\boxed{
\text{Intelligence-Bearing Substrate}
}
$$

即「能承載、參與或實現智能相關狀態轉換的基質／載體」。本文的第一個核心修正是：數位、生物、機械與混合是「基質型別」；分散式則不是同一類材料型別，而是「拓樸型別」；具身也不是材料，而是智能系統與物理世界之間的感知—行動耦合關係。因此，未來智能系統不應只使用單一分類軸，而至少需要：

$$
\boxed{
\mathcal X
=
(
\Sigma,
\Tau,
\mathcal E,
\mathcal B
)
}
$$

其中 $\Sigma$ 表示承載基質， $\Tau$ 表示系統拓樸， $\mathcal E$ 表示具身／環境耦合方式， $\mathcal B$ 表示系統邊界。

本文將基質初步分成數位／電子、機械／物理、神經形態、生物與混合基質；將拓樸區分為單體、模組化、多節點與分散式；將具身分為無直接物理閉環、感測耦合、行動耦合與閉環具身；並提出「邊界不是由外殼決定」的原則：一個 AI 可以跨一萬個伺服器仍構成一個運行系統，也可以在同一台伺服器內存在多個相互獨立的 agent。物理機殼、程序邊界、記憶邊界、控制邊界、法律邊界與主體邊界不能預設相等。

實證部分以 DARPA HyBRIDS 計畫、NSF BEGIN OI / organoid intelligence、NIH BRAIN Initiative、2026 年 physical computing / soft robotics 研究，以及近年的 embodied and neuromorphic systems 作為案例。DARPA HyBRIDS 明確研究生物與合成元件整合的 biohybrid platforms；NSF 的 BEGIN OI 計畫支持可動態處理資訊、並與非生物系統介接的 organoid systems；NSF 2024 年進一步投資七個 organoid intelligence / biological computing 研究團隊；NIH BRAIN Initiative 長期研究神經訊號記錄、解碼與閉環腦機介面；2026 年 physical computing 研究則展示軟體機器人的材料與動力學本身可以參與計算，而不必把全部計算集中在傳統數位控制器。

本文特別強調型別安全：organoid intelligence 是一個生物計算研究領域，不是「已證明具有意識的人工大腦」；biohybrid robot 使用活體組織，不代表整個機器人是生物主體；腦機介面連接人腦與計算機，也不自動生成一個新的人—機混合人格；分散式 AI 跨很多節點，也不能由節點數推出主體數。本文只建立智能承載與系統邊界的分析框架，不以材料種類推導意識、人格或權利。

本文最後提出「基質可替換性」與「功能等價不等於本體等價」兩個重要命題。若同一智能功能可由不同材料實現，則材料不是唯一分類基準；但即使兩個系統在某功能域等價，也不能推出其內部狀態、感質、主體性或法律地位相同。這一框架為 EXS-07 的「會自己打科技樹的科技：從外部能力到自我延展文明」提供最後接口：當智能不再被綁定於單一機器與單一材料，能力系統才真正可能跨載體選擇、重組與生成新的能力節點。

---

## 關鍵詞

智能載體；Intelligence-Bearing Substrate；基質；生物計算；organoid intelligence；biohybrid robotics；physical computing；neuromorphic computing；腦機介面；分散式 AI；具身 AI；系統邊界；substrate independence；混合智能

---

# 1. 從「AI 機器」開始不夠用

EXS-05 建立：

$$
\boxed{
\text{AI-Capable}
\neq
\text{AI-Embedded}
\neq
\text{AI-Dependent}
\neq
\text{AI-Native}.
}
$$

但這整套分類仍有一個隱含前提：

$$
\boxed{
\text{AI lives in machines}.
}
$$

今天這個前提大致有實用性。

但它不是邏輯必然。

如果：

- 生物組織可執行資訊處理；
- 物理材料可直接承擔部分計算；
- 神經形態裝置以非傳統方式處理訊號；
- 生物與電子系統可閉環互動；
- 智能系統可跨大量節點分布；

那麼：

$$
\boxed{
\text{Machine}
}
$$

只會是更一般集合中的一個子類。

---

# 2. 提出更一般概念：Intelligence-Bearing Substrate

本文定義：

$$
\boxed{
\Sigma
=
\text{Intelligence-Bearing Substrate}.
}
$$

中文暫譯：

$$
\boxed{
\text{智能承載基質／智能載體}.
}
$$

其最弱定義是：

> 能夠承載、實現、參與或維持與智能功能相關之資訊狀態與狀態轉換的物理、數位、生物或混合結構。

這個定義刻意不要求：

$$
\Sigma
\Rightarrow
\text{subject}.
$$

也不要求：

$$
\Sigma
\Rightarrow
\text{consciousness}.
$$

---

# 3. 「承載智能」不等於「本身就是智能主體」

一個 GPU：

$$
\Sigma_G
$$

可以承載模型計算。

但不能只由：

$$
\Sigma_G
$$

推出：

$$
\text{subjectivity}.
$$

一塊生物神經組織：

$$
\Sigma_B
$$

可以參與資訊處理。

同樣不能直接推出：

$$
\text{personhood}.
$$

因此：

$$
\boxed{
\text{Intelligence-Bearing}
\neq
\text{Subject-Bearing}.
}
$$

這是本文最重要的型別安全之一。

---

# 4. 第一個分類錯誤：把「分散式」當成材料種類

直覺常會寫：

- digital AI；
- biological AI；
- hybrid AI；
- distributed AI。

但這四者不在同一型別。

因為：

$$
\boxed{
\text{digital},
\text{biological},
\text{hybrid}
}
$$

主要描述：

$$
\boxed{
\text{what carries the process}.
}
$$

而：

$$
\boxed{
\text{distributed}
}
$$

描述：

$$
\boxed{
\text{how the process is arranged across locations/nodes}.
}
$$

所以：

$$
\boxed{
\text{Substrate Type}
\neq
\text{Topology Type}.
}
$$

---

# 5. 第二個分類錯誤：把「具身」當成材料種類

同樣地：

$$
\boxed{
\text{Embodied AI}
}
$$

不是：

$$
\boxed{
\text{a material class}.
}
$$

一個具身 AI 可以是：

- 電子／機械；
- 生物；
- 混合；
- 軟體控制遠端機器；
- 分散式控制多個身體。

因此具身描述的是：

$$
\boxed{
\text{perception-action coupling with a physical environment}.
}
$$

所以：

$$
\boxed{
\text{Substrate}
\neq
\text{Embodiment}.
}
$$

---

# 6. 多軸智能載體模型

本文提出：

$$
\boxed{
\mathcal X
=
(
\Sigma,
\Tau,
\mathcal E,
\mathcal B
).
}
$$

其中：

$$
\Sigma
=
\text{substrate axis},
$$

$$
\Tau
=
\text{topology axis},
$$

$$
\mathcal E
=
\text{embodiment/coupling axis},
$$

$$
\mathcal B
=
\text{system-boundary axis}.
$$

未來還可以加入：

$$
\mathcal A
=
\text{autonomy},
$$

$$
\mathcal S
=
\text{subjectivity evidence},
$$

但本文不把它們混進載體分類。

---

# 7. 基質軸 $\Sigma$

本文先提出五類基質。

## $\Sigma_D$：數位／電子基質

$$
\boxed{
\Sigma_D
=
\text{Digital/Electronic Substrate}.
}
$$

包括：

- CPU；
- GPU；
- NPU；
- accelerator；
- memory；
- conventional digital computing system。

今天主要 AI 系統大多落在這一類。

---

# 8. $\Sigma_P$：物理／機械計算基質

$$
\boxed{
\Sigma_P
=
\text{Physical/Mechanical Computing Substrate}.
}
$$

這類系統不一定把所有計算先轉換為傳統數位符號。

物理結構本身的：

- 彈性；
- 振盪；
- 流體；
- 形變；
- 材料動力學；

可以直接參與：

$$
\boxed{
\text{information transformation}.
}
$$

---

# 9. 2026 年 physical computing 的研究意義

2026 年 Nature Communications 的 perspective 提出把 physical computing 更直接嵌入 soft robots，並討論：

- analog oscillators；
- physical reservoir computing；
- physical algorithmic computing。

研究甚至設想計算能力可分布於章魚式軟機器人的觸手與中央控制結構，而非全部集中在傳統控制器。[1]

這顯示：

$$
\boxed{
\text{Body}
}
$$

不必只是：

$$
\boxed{
\text{passive actuator}.
}
$$

它本身可以參與：

$$
\boxed{
\text{computation}.
}
$$

---

# 10. 身體可以是控制器的一部分

傳統機器人：

$$
\text{Controller}
\rightarrow
\text{Body}.
$$

physical intelligence 路徑可能更像：

$$
\boxed{
\text{Controller}
\leftrightarrow
\text{Body Dynamics}.
}
$$

於是：

$$
\text{control computation}
$$

部分由：

$$
\text{morphology}
$$

完成。

這可以稱為：

$$
\boxed{
\text{Morphological Computation}.
}
$$

---

# 11. $\Sigma_N$：神經形態基質

$$
\boxed{
\Sigma_N
=
\text{Neuromorphic Substrate}.
}
$$

神經形態計算試圖利用：

- event-driven processing；
- spiking dynamics；
- memory-compute co-location；
- brain-inspired architecture；

降低傳統計算的能耗與資料移動成本。

NSF 目前的 emerging technology 與 computer systems research program 仍把 neuromorphic、brain-inspired 與非傳統計算列為重要研究方向。[2]

---

# 12. 神經形態不是生物腦

需要明確：

$$
\boxed{
\text{Neuromorphic}
\neq
\text{Biological}.
}
$$

「像神經」描述架構靈感。

不代表：

$$
\text{living tissue}.
$$

同樣：

$$
\boxed{
\text{brain-inspired}
\neq
\text{brain}.
}
$$

---

# 13. $\Sigma_B$：生物計算基質

$$
\boxed{
\Sigma_B
=
\text{Biological Computing Substrate}.
}
$$

其範圍可包含：

- cells；
- neural cultures；
- organoids；
- biomolecular computing；
- living materials。

其中一部分研究開始明確以：

$$
\boxed{
\text{information processing}
}
$$

而不是單純生物觀察作為工程目標。

---

# 14. NSF BEGIN OI：生物組織被正式當成資訊處理系統研究

NSF 的 EFRI BEGIN OI 計畫全名為：

$$
\text{Biocomputing through EnGINeering Organoid Intelligence}.
$$

其目標包括設計與工程化：

$$
\boxed{
\text{organoid systems capable of dynamically processing information}
}
$$

並使其與：

$$
\boxed{
\text{non-living systems}
}
$$

介接。[3]

這代表「計算基質」的官方研究範圍已經明確跨出生物—非生物邊界。

---

# 15. 2024 NSF organoid intelligence 投資

2024 年 NSF 投入約 1,400 萬美元，支持七個 biological computing / organoid intelligence 團隊。[4]

研究方向包含：

- organoid adaptive reservoir computing；
- neuron-soft organoid-computer interfaces；
- bio-symbiotic systems；
- biological information processing。

因此：

$$
\boxed{
\text{Biological Computing}
}
$$

已經不是純概念討論。

它是實際的科研工程方向。

---

# 16. 但「organoid intelligence」不是「人造有意識大腦」

這條必須加粗型別安全：

$$
\boxed{
\text{Organoid Intelligence}
\neq
\text{Demonstrated Conscious Artificial Brain}.
}
$$

NSF 計畫本身也明確指出：

> intelligence 與 learning 在 biology、cognitive science、computer science 與 engineering 中具有不同含義。[3]

因此：

$$
\boxed{
\text{information processing}
\neq
\text{phenomenal consciousness}.
}
$$

---

# 17. 生物材料不自動帶來主體性

如果：

$$
\text{living cells}
$$

存在於機器中，

不能推出：

$$
\boxed{
\text{the machine is alive as a unified subject}.
}
$$

更不能推出：

$$
\boxed{
\text{the machine is a person}.
}
$$

所以：

$$
\boxed{
\text{Biological Substrate}
\neq
\text{Biological Personhood}.
}
$$

---

# 18. $\Sigma_H$：混合基質

$$
\boxed{
\Sigma_H
=
\text{Hybrid Substrate}.
}
$$

混合基質表示智能相關功能橫跨：

$$
\boxed{
\text{biotic}
+
\text{abiotic}
}
$$

元件。

例如：

- living muscle + electronics；
- neural tissue + soft electrodes；
- organoid + digital interface；
- brain + computer interface。

---

# 19. DARPA HyBRIDS：biohybrid platform 成為明確工程目標

DARPA 的 HyBRIDS 計畫研究如何整合 synthetic 與 biological components，形成可部署的 biohybrid platforms。[5]

其基本思想是：

- engineered systems 提供可控性與精確性；
- biological systems 提供適應、韌性、敏感與效率等性質。

所以：

$$
\boxed{
\Sigma_H
}
$$

不是單純：

$$
\text{machine with biological decoration}.
$$

它可能是：

$$
\boxed{
\text{functional integration across material classes}.
}
$$

---

# 20. Biohybrid robotics 已具有獨立研究領域

近年的 biohybrid robotics 研究大量使用：

- skeletal muscle；
- cardiac muscle；
- living tissue；
- soft electronics；

形成：

- actuation；
- sensing；
- locomotion；
- adaptive interfaces。

2025–2026 年的相關綜述仍指出穩定性、可擴展性與 biotic-abiotic integration 是主要工程挑戰。[6]

因此：

$$
\boxed{
\text{Biohybrid}
}
$$

已是實際工程類別。

---

# 21. 但 biohybrid 不代表「AI 變成生物」

如果：

$$
\text{AI controller}
+
\text{living muscle actuator},
$$

那麼：

$$
\boxed{
\text{control substrate}
}
$$

仍可能主要是：

$$
\Sigma_D.
$$

而：

$$
\boxed{
\text{actuation substrate}
}
$$

是：

$$
\Sigma_B.
$$

所以一個系統可以是：

$$
\boxed{
\text{hybrid body}
}
$$

但：

$$
\boxed{
\text{non-hybrid cognition}.
}
$$

---

# 22. 必須區分「智能基質」與「身體基質」

令：

$$
\Sigma_I
=
\text{intelligence substrate},
$$

$$
\Sigma_E
=
\text{embodiment substrate}.
$$

則：

$$
\boxed{
\Sigma_I
\neq
\Sigma_E.
}
$$

例如：

$$
\Sigma_I=\text{digital},
$$

$$
\Sigma_E=\text{biological muscle + synthetic frame}.
$$

因此：

$$
\boxed{
\text{Biohybrid Robot}
}
$$

不能自動分類為：

$$
\boxed{
\text{Biological AI}.
}
$$

---

# 23. 腦機介面：宿主邊界開始真正變得麻煩

腦機介面 BCI 可以：

1. 記錄神經活動；
2. 解碼意圖；
3. 轉換成控制信號；
4. 驅動外部裝置；
5. 在閉環系統中把訊息再回饋到神經系統。

NIH BRAIN Initiative 長期支持這類神經技術，包含 implant recording、意圖解碼、prosthetic control 與 closed-loop stimulation。[7]

因此：

$$
\boxed{
\text{human}
\leftrightarrow
\text{computer}
}
$$

可以形成比一般鍵盤／螢幕更直接的閉環。

---

# 24. 但 BCI 不自動創造「新混合主體」

若：

$$
H
\leftrightarrow
M,
$$

不能直接推出：

$$
\boxed{
S_{HM}
=
\text{new unified subject}.
}
$$

可能只是：

$$
\boxed{
\text{human subject using a tightly coupled prosthetic/interface}.
}
$$

因此：

$$
\boxed{
\text{Coupling}
\neq
\text{Ontological Fusion}.
}
$$

---

# 25. 這裡必須重新區分「載體邊界」與「主體邊界」

一個系統可以：

$$
\mathcal B_{\mathrm{hardware}}
$$

跨兩個物理設備。

但：

$$
\mathcal B_{\mathrm{subject}}
$$

可能只包含一個人。

因此：

$$
\boxed{
\mathcal B_{\mathrm{hardware}}
\neq
\mathcal B_{\mathrm{subject}}.
}
$$

同樣：

$$
\mathcal B_{\mathrm{network}}
\neq
\mathcal B_{\mathrm{subject}}.
$$

---

# 26. 拓樸軸 $\Tau$

現在進入真正的「分散式」。

本文定義：

$$
\boxed{
\Tau
=
\text{Intelligence-System Topology}.
}
$$

它描述：

> 智能相關狀態與功能如何跨節點配置。

---

# 27. $\Tau_0$：單節點

$$
\boxed{
\Tau_0
=
\text{Monolithic / Single-Node}.
}
$$

主要運算、記憶與控制集中在一個裝置或一個運行節點。

---

# 28. $\Tau_1$：模組化單系統

$$
\boxed{
\Tau_1
=
\text{Modular}.
}
$$

例如：

$$
A_{\mathrm{vision}}
+
A_{\mathrm{language}}
+
A_{\mathrm{planner}}
+
A_{\mathrm{controller}}.
$$

但仍由一個主要系統協調。

---

# 29. $\Tau_2$：多節點協作

$$
\boxed{
\Tau_2
=
\text{Multi-Node Cooperative}.
}
$$

功能分布於：

- local device；
- edge；
- cloud；
- remote service。

例如：

$$
\text{phone}
\rightarrow
\text{edge}
\rightarrow
\text{cloud}.
$$

---

# 30. $\Tau_3$：分散式智能系統

$$
\boxed{
\Tau_3
=
\text{Distributed Intelligence System}.
}
$$

其特徵是：

- 多節點；
- 狀態分布；
- 計算分布；
- 通訊必要；
- 可能沒有單一完整運行點。

因此：

$$
\boxed{
\text{One system}
}
$$

可能沒有：

$$
\boxed{
\text{one machine}.
}
$$

---

# 31. 「一個 AI」可能橫跨很多電腦

假設：

$$
A
=
\{n_1,n_2,\ldots,n_{10000}\}.
$$

如果：

- 記憶共享；
- 狀態協同；
- 控制一致；
- 任務連續；

則可以在工程層把它當作：

$$
\boxed{
\text{one distributed system}.
}
$$

所以：

$$
\boxed{
N_{\mathrm{machines}}
\neq
N_{\mathrm{AI\ systems}}.
}
$$

---

# 32. 反過來，一台機器也可以有很多 AI

同一台伺服器：

$$
M
$$

可以運行：

$$
\{A_1,A_2,\ldots,A_n\}.
$$

因此：

$$
\boxed{
N_{\mathrm{machines}}
\neq
N_{\mathrm{agents}}.
}
$$

同樣：

$$
N_{\mathrm{agents}}
\neq
N_{\mathrm{subjects}}.
$$

---

# 33. 分散式不是主體性證據

如果：

$$
A
$$

跨：

$$
10^6
$$

節點運行，

不能推出：

$$
\boxed{
A
\text{ is a subject}.
}
$$

同樣：

$$
10^6
$$

個 process 也不代表：

$$
10^6
$$

個主體。

因此：

$$
\boxed{
\text{Topology}
\neq
\text{Subject Count}.
}
$$

這將是第二系列 AI 人口研究的重要前置。

---

# 34. 多 agent 也不一定等於多主體

假設：

$$
A_0
\rightarrow
\{a_1,a_2,\ldots,a_n\}.
$$

若：

$$
a_i
$$

只是：

- temporary worker；
- stateless tool；
- delegated process；

則：

$$
N_{\mathrm{agent}}=n
$$

不能推出：

$$
N_{\mathrm{subject}}=n.
$$

所以：

$$
\boxed{
\text{Agent}
\neq
\text{Subject}.
}
$$

---

# 35. 具身軸 $\mathcal E$

本文定義：

$$
\boxed{
\mathcal E
=
\text{Embodiment / World-Coupling Degree}.
}
$$

---

# 36. $\mathcal E_0$：無直接物理閉環

$$
\boxed{
\mathcal E_0
=
\text{No direct physical action loop}.
}
$$

例如純文字模型。

---

# 37. $\mathcal E_1$：感測耦合

$$
\boxed{
\mathcal E_1
=
\text{Sensor-coupled}.
}
$$

AI 接收：

- camera；
- microphone；
- telemetry；
- sensor。

但不直接作用世界。

---

# 38. $\mathcal E_2$：行動耦合

$$
\boxed{
\mathcal E_2
=
\text{Actuator-coupled}.
}
$$

AI 可以：

- move robot；
- operate device；
- change environment。

---

# 39. $\mathcal E_3$：閉環具身

$$
\boxed{
\mathcal E_3
=
\text{Closed-loop embodied}.
}
$$

形成：

$$
\boxed{
\text{Perceive}
\rightarrow
\text{Model}
\rightarrow
\text{Act}
\rightarrow
\text{Observe Consequence}
\rightarrow
\text{Update}.
}
$$

這才是完整的世界行動閉環。

---

# 40. Embodied AI 與 physical AI 的研究正快速增加

2025–2026 年 robotics / embodied AI 研究持續把：

- vision；
- language；
- planning；
- touch；
- world models；
- neuromorphic systems；

與實際物理機器結合。[8]

這證明：

$$
\boxed{
\text{AI}
+
\text{physical coupling}
}
$$

已是明確科研前沿。

但：

$$
\boxed{
\text{Embodied}
\neq
\text{Subjective}.
}
$$

仍必須保留。

---

# 41. 邊界軸 $\mathcal B$

真正困難的是：

> 一個智能系統從哪裡開始，到哪裡結束？

本文定義：

$$
\boxed{
\mathcal B
=
\text{System Boundary Family}.
}
$$

而不是一條單一線。

---

# 42. 物理邊界

$$
\boxed{
\mathcal B_P
=
\text{physical enclosure boundary}.
}
$$

例如：

- 一台手機；
- 一個機器人；
- 一個 rack。

但：

$$
\mathcal B_P
$$

很少足以決定智能系統邊界。

---

# 43. 程序邊界

$$
\boxed{
\mathcal B_R
=
\text{runtime/process boundary}.
}
$$

一個模型可能跨：

- process；
- container；
- host。

所以：

$$
\mathcal B_R
\neq
\mathcal B_P.
$$

---

# 44. 記憶邊界

$$
\boxed{
\mathcal B_M
=
\text{memory-continuity boundary}.
}
$$

如果：

$$
A_1
$$

與：

$$
A_2
$$

共享全部長期記憶，

它們與完全獨立 memory state 的兩個 agent 具有不同身份結構。

---

# 45. 控制邊界

$$
\boxed{
\mathcal B_C
=
\text{control/decision boundary}.
}
$$

若：

$$
A_R
$$

統一協調：

$$
\{a_1,\ldots,a_n\},
$$

則工程治理可能把：

$$
\mathcal B_C
$$

畫在 regional controller 外層。

---

# 46. 法律邊界

$$
\boxed{
\mathcal B_L
=
\text{legal accountability boundary}.
}
$$

法律可能不在乎：

$$
N_{\mathrm{process}}.
$$

而直接問：

$$
\boxed{
\text{which legal entity operated the system?}
}
$$

這將在第二系列域治理中展開。

---

# 47. 主體邊界

$$
\boxed{
\mathcal B_S
=
\text{subject boundary}.
}
$$

本文不提供它的完成判準。

只強調：

$$
\boxed{
\mathcal B_S
\neq
\mathcal B_P
\neq
\mathcal B_R
\neq
\mathcal B_M
\neq
\mathcal B_C
\neq
\mathcal B_L.
}
$$

這是一個核心型別安全。

---

# 48. 於是「這是一個 AI 還是很多 AI？」沒有單一答案

若問題是：

> 有幾個 process？

答案：

$$
N_R.
$$

如果問：

> 有幾個模型 instance？

答案：

$$
N_I.
$$

如果問：

> 有幾個 agent？

答案：

$$
N_A.
$$

如果問：

> 有幾個法律實體？

答案：

$$
N_L.
$$

如果問：

> 有幾個主體？

則：

$$
N_S
$$

需要另一套證據。

因此：

$$
\boxed{
N_R
\neq
N_I
\neq
N_A
\neq
N_L
\neq
N_S.
}
$$

---

# 49. 混合系統使「內／外」邊界變得連續

如果：

$$
H
\rightarrow
\text{phone}
$$

很容易說：

$$
\text{phone}
=
\text{external}.
$$

若：

$$
H
\leftrightarrow
\text{implant}
$$

則開始模糊。

若：

$$
\text{neural tissue}
\leftrightarrow
\text{digital controller}
$$

則：

$$
\boxed{
\text{internal/external}
}
$$

不再是一個充分分類。

因此本文更偏好：

$$
\boxed{
\text{native substrate}
}
$$

與：

$$
\boxed{
\text{augmenting substrate}.
}
$$

---

# 50. Native / Augmenting 也不是永久身份

若：

$$
X
$$

最初是：

$$
\text{augmenting}.
$$

長期整合後：

$$
X
$$

可能成為：

$$
\boxed{
\text{functionally constitutive}.
}
$$

例如某些植入式醫療設備。

所以：

$$
\boxed{
\text{Native}
\neq
\text{Biologically Original}.
}
$$

這是另一個重要修正。

---

# 51. 基質可替換性

假設某功能：

$$
F
$$

可以由：

$$
\Sigma_1
$$

或：

$$
\Sigma_2
$$

實現。

則：

$$
F(\Sigma_1)
\approx
F(\Sigma_2).
$$

這表示某些功能可能具有：

$$
\boxed{
\text{Substrate Portability}.
}
$$

但：

$$
\boxed{
\text{functional portability}
}
$$

不能自動推出：

$$
\boxed{
\text{ontological equivalence}.
}
$$

---

# 52. 功能等價不等於本體等價

若：

$$
F(A)=F(B),
$$

不能推出：

$$
\boxed{
A=B.
}
$$

同樣：

$$
\text{same task performance}
$$

不能推出：

- same internal state；
- same causal structure；
- same memory；
- same phenomenology；
- same subjectivity。

所以：

$$
\boxed{
\text{Functional Equivalence}
\neq
\text{Ontological Equivalence}.
}
$$

---

# 53. 這對「上傳心智」類問題尤其重要

如果未來：

$$
H
\rightarrow
D
$$

得到一個數位系統：

$$
D
$$

在行為上近似：

$$
H,
$$

仍不能只由：

$$
F(H)\approx F(D)
$$

推出：

$$
\boxed{
S_H=S_D.
}
$$

本文不處理 mind uploading 成功與否。

只保留：

$$
\boxed{
\text{behavioral continuity}
\neq
\text{proven subject continuity}.
}
$$

---

# 54. 基質與能源密度也會影響智能拓樸

不同 $\Sigma$ 具有不同：

- energy cost；
- heat；
- latency；
- repair；
- replication；
- size；
- bandwidth。

因此：

$$
\boxed{
\Sigma
\rightarrow
\text{feasible topology}.
}
$$

例如：

$$
\Sigma_D
$$

可能容易形成高速網路化。

$$
\Sigma_B
$$

可能具有不同的：

- self-repair；
- growth；
- metabolic constraints。

所以：

$$
\boxed{
\text{Substrate}
}
$$

會反過來塑造：

$$
\boxed{
\text{civilizational form}.
}
$$

---

# 55. 生物基質可能引入完全不同的生命周期

電子硬體：

$$
\text{manufacture}
\rightarrow
\text{deploy}
\rightarrow
\text{replace}.
$$

生物基質可能：

$$
\text{grow}
\rightarrow
\text{mature}
\rightarrow
\text{adapt}
\rightarrow
\text{age}.
$$

因此：

$$
\boxed{
\text{AI Lifecycle}
}
$$

未來未必只是一套：

$$
\boxed{
\text{software lifecycle}.
}
$$

它可能變成：

$$
\boxed{
\text{software}
+
\text{hardware}
+
\text{biological lifecycle}.
}
$$

---

# 56. 混合載體也會讓「維修」與「治療」邊界變模糊

假設一個 biohybrid system 失效。

處理方式可能同時包含：

- firmware update；
- component replacement；
- tissue regeneration；
- biological maintenance；
- medical procedure。

因此：

$$
\boxed{
\text{Repair}
\leftrightarrow
\text{Treatment}.
}
$$

這會帶來後續法律與倫理分類問題。

本文只建立結構，不展開法學。

---

# 57. 「AI 的身體」也可能不只一個

如果：

$$
A
$$

同時控制：

$$
E_1,E_2,\ldots,E_n,
$$

則：

$$
\boxed{
N_{\mathrm{embodiments}}=n
}
$$

但：

$$
N_{\mathrm{controllers}}=1.
$$

所以：

$$
\boxed{
\text{One Intelligence}
\rightarrow
\text{Multiple Bodies}
}
$$

是完全合理的工程型態。

---

# 58. 反過來，一個身體也可能有多個智能控制層

一台大型工廠、車輛或機器人可能包含：

$$
A_1=\text{safety},
$$

$$
A_2=\text{navigation},
$$

$$
A_3=\text{vision},
$$

$$
A_4=\text{planner}.
$$

所以：

$$
\boxed{
\text{One Body}
\rightarrow
\text{Multiple AI Systems}.
}
$$

因此：

$$
\boxed{
\text{Body Count}
\neq
\text{Intelligence Count}.
}
$$

---

# 59. 具身與分散可以同時成立

一個 regional AI：

$$
A_R
$$

可以透過：

$$
\{E_1,E_2,\ldots,E_n\}
$$

在城市中具身。

因此：

$$
\boxed{
\Tau_3
+
\mathcal E_3
}
$$

可以同時成立。

這就是未來：

$$
\boxed{
\text{Distributed Embodied Intelligence}
}
$$

的基本形式。

---

# 60. 無所不在的 AI 最終是「載體場」而不是機器人數量

若大量：

$$
\Sigma_D,
\Sigma_P,
\Sigma_H
$$

分布在：

- homes；
- vehicles；
- infrastructure；
- factories；
- wearables；
- biological interfaces；

並以：

$$
\Tau_2-\Tau_3
$$

互聯，

則：

$$
\boxed{
\text{Pervasive Intelligence}
}
$$

不是：

> 到處都有一台長得像人的機器人。

而是：

$$
\boxed{
\text{intelligence-bearing substrates become spatially pervasive}.
}
$$

---

# 61. 智能密度比裝置數更有意義

令區域：

$$
R.
$$

可定義概念性的：

$$
\boxed{
\rho_I(R)
=
\frac{
\text{effective intelligent sensing/inference/action capacity}
}{
\text{space-time volume}
}.
}
$$

因此：

$$
N_{\mathrm{devices}}
$$

只是一個 proxy。

真正重要的是：

$$
\boxed{
\rho_I.
}
$$

這將在第二系列 Pervasive Intelligence 正式展開。

---

# 62. 基質多樣化也會削弱「關掉所有 AI」這種簡單想像

如果 AI 只存在：

$$
\text{one data center},
$$

則：

$$
\text{switch off}
$$

相對容易定義。

如果 AI 分布於：

- phones；
- cars；
- factories；
- implants；
- biohybrid systems；
- edge systems；
- distributed networks；

則：

$$
\boxed{
\text{AI Off}
}
$$

本身就需要重新定義。

這不是政策結論。

只是系統事實：

$$
\boxed{
\text{distributed substrate diversity}
\rightarrow
\text{harder global state definition}.
}
$$

---

# 63. 但多樣化不代表不可治理

不能由：

$$
\text{many substrates}
$$

推出：

$$
\boxed{
\text{no governance possible}.
}
$$

治理可以作用於：

- capability；
- effect；
- access；
- compute；
- deployment；
- legal entity；
- domain。

這正是後續域治理的重要理由。

---

# 64. 智能載體分類的完整初版

本文提出：

$$
\boxed{
\mathcal X
=
(
\Sigma,
\Tau,
\mathcal E,
\mathcal B
).
}
$$

例如：

### 純雲端 LLM

$$
\Sigma=\Sigma_D,
$$

$$
\Tau=\Tau_3,
$$

$$
\mathcal E=\mathcal E_0.
$$

### 自主機器人

$$
\Sigma=\Sigma_D+\Sigma_P,
$$

$$
\Tau=\Tau_1,
$$

$$
\mathcal E=\mathcal E_3.
$$

### Biohybrid robot

$$
\Sigma=\Sigma_D+\Sigma_B+\Sigma_P,
$$

$$
\Tau=\Tau_1,
$$

$$
\mathcal E=\mathcal E_3.
$$

### Organoid-computer interface

$$
\Sigma=\Sigma_B+\Sigma_D,
$$

$$
\Tau=\Tau_1-\Tau_2,
$$

其具身程度依實際裝置而定。

---

# 65. 不應用基質分類替代功能分類

即使兩個系統：

$$
\Sigma_A\neq\Sigma_B,
$$

也可能：

$$
F_A\approx F_B.
$$

所以：

$$
\boxed{
\text{Substrate Taxonomy}
}
$$

不能取代：

$$
\boxed{
\text{Capability Taxonomy}.
}
$$

同樣：

$$
\boxed{
\text{Capability Taxonomy}
}
$$

不能取代：

$$
\boxed{
\text{Subjectivity Taxonomy}.
}
$$

---

# 66. 五層型別安全

本文提出：

$$
\boxed{
\text{Substrate}
\neq
\text{Topology}
\neq
\text{Capability}
\neq
\text{Agency}
\neq
\text{Subjectivity}.
}
$$

這五層若混在一起，未來 AI 討論會持續產生大量概念錯誤。

---

# 67. 對「機器生命」敘事的限制

一台使用活體細胞的 biohybrid robot：

$$
\boxed{
\text{contains living components}.
}
$$

但這不必然表示：

$$
\boxed{
\text{whole robot is a living organism}.
}
$$

更不表示：

$$
\boxed{
\text{whole robot is a conscious subject}.
}
$$

因此：

$$
\boxed{
\text{Living Component}
\neq
\text{Living Unified Entity}
\neq
\text{Conscious Entity}.
}
$$

---

# 68. 對「數位生命」敘事的限制

同樣：

$$
\text{persistent digital agent}
$$

不必然：

$$
\boxed{
\text{digital life}.
}
$$

必須先定義：

- self-maintenance；
- replication；
- metabolism analogue；
- adaptation；
- identity continuity。

本文不提前定義 digital life。

---

# 69. 對「分散式心智」敘事的限制

如果：

$$
10^6
$$

個 agent 協作，

不能直接稱為：

$$
\boxed{
\text{one distributed mind}.
}
$$

需要至少研究：

- integration；
- global state；
- mutual access；
- control；
- memory；
- continuity。

因此：

$$
\boxed{
\text{Coordination}
\neq
\text{Mental Unity}.
}
$$

---

# 70. 對「混合人」敘事的限制

如果一個人使用：

- implant；
- AI assistant；
- robotic prosthesis；

不能直接說：

$$
\boxed{
\text{human became a new hybrid species}.
}
$$

這可能只是：

$$
\boxed{
\text{augmented human}.
}
$$

分類必須依：

- biological integration；
- reversibility；
- control；
- dependency；
- identity；

而定。

---

# 71. 核心命題

本文提出以下二十個核心命題。

## 命題 1

$$
\boxed{
\text{Machine}
\subset
\text{Intelligence-Bearing Substrate Space}.
}
$$

## 命題 2

$$
\boxed{
\text{Substrate}
\neq
\text{Topology}.
}
$$

## 命題 3

$$
\boxed{
\text{Substrate}
\neq
\text{Embodiment}.
}
$$

## 命題 4

$$
\boxed{
\text{Digital}
\neq
\text{Distributed}.
}
$$

## 命題 5

$$
\boxed{
\text{Biological}
\neq
\text{Subjective}.
}
$$

## 命題 6

$$
\boxed{
\text{Biohybrid}
\neq
\text{Biological AI Subject}.
}
$$

## 命題 7

$$
\boxed{
\text{Organoid Intelligence}
\neq
\text{Demonstrated Conscious Artificial Brain}.
}
$$

## 命題 8

$$
\boxed{
\text{Neuromorphic}
\neq
\text{Biological}.
}
$$

## 命題 9

$$
\boxed{
\text{Body}
}
$$

can participate in:

$$
\boxed{
\text{computation}.
}
$$

## 命題 10

$$
\boxed{
N_{\mathrm{machines}}
\neq
N_{\mathrm{AI\ systems}}.
}
$$

## 命題 11

$$
\boxed{
N_{\mathrm{agents}}
\neq
N_{\mathrm{subjects}}.
}
$$

## 命題 12

$$
\boxed{
\text{Coupling}
\neq
\text{Ontological Fusion}.
}
$$

## 命題 13

$$
\boxed{
\mathcal B_P
\neq
\mathcal B_R
\neq
\mathcal B_M
\neq
\mathcal B_C
\neq
\mathcal B_L
\neq
\mathcal B_S.
}
$$

## 命題 14

$$
\boxed{
\text{One Intelligence}
\rightarrow
\text{Multiple Bodies}
}
$$

is architecturally possible.

## 命題 15

$$
\boxed{
\text{One Body}
\rightarrow
\text{Multiple AI Systems}
}
$$

is architecturally possible.

## 命題 16

$$
\boxed{
\text{Functional Equivalence}
\neq
\text{Ontological Equivalence}.
}
$$

## 命題 17

$$
\boxed{
\text{Substrate Portability}
}
$$

can exist without proven subject continuity.

## 命題 18

$$
\boxed{
\text{Distributed Embodiment}
}
$$

is a coherent system architecture.

## 命題 19

$$
\boxed{
\text{Pervasive Intelligence}
\neq
\text{Robot Count}.
}
$$

## 命題 20

$$
\boxed{
\text{Substrate}
\neq
\text{Topology}
\neq
\text{Capability}
\neq
\text{Agency}
\neq
\text{Subjectivity}.
}
$$

---

# 72. 可檢驗研究計畫

## 72.1 智能載體資料庫

建立：

$$
\mathcal X_i
=
(
\Sigma_i,
\Tau_i,
\mathcal E_i,
\mathcal B_i
)
$$

資料庫。

涵蓋：

- cloud models；
- phones；
- robots；
- neuromorphic devices；
- biohybrid systems；
- organoid-computer interfaces；
- BCI。

---

## 72.2 基質可替換性測試

對同一任務：

$$
F
$$

比較：

$$
F(\Sigma_D),
$$

$$
F(\Sigma_N),
$$

$$
F(\Sigma_P),
$$

$$
F(\Sigma_B).
$$

測量：

- energy；
- latency；
- learning；
- robustness；
- repair；
- scale。

---

## 72.3 Physical computing contribution

定義：

$$
P_C
=
\frac{
\text{control/inference realized by body dynamics}
}{
\text{total control/inference workload}
}.
$$

研究：

$$
P_C
$$

是否能降低傳統控制器負荷。

---

## 72.4 Biohybrid integration depth

定義：

$$
H_B
=
\text{biotic-abiotic functional integration depth}.
$$

區分：

- biological actuator；
- biological sensor；
- biological computation；
- closed-loop hybrid cognition。

---

## 72.5 Distributed AI boundary reconstruction

對實際分散式系統繪製：

$$
\mathcal B_R,
\mathcal B_M,
\mathcal B_C.
$$

測試：

> 工程上的「一個 AI」到底由哪些邊界共同決定？

---

## 72.6 多身體智能實驗

對：

$$
A
\rightarrow
\{E_1,\ldots,E_n\}
$$

測量：

- memory integration；
- action conflict；
- sensor fusion；
- identity continuity；
- control latency。

---

## 72.7 One-body multi-agent architecture

對：

$$
E
\leftarrow
\{A_1,\ldots,A_n\}
$$

研究：

- arbitration；
- safety；
- conflict resolution；
- shared world model。

---

## 72.8 BCI boundary study

研究：

$$
H
\leftrightarrow
M
$$

在：

- motor control；
- memory support；
- sensory feedback；

下的：

$$
\mathcal B_C,
\mathcal B_M.
$$

但不把工程耦合直接當作 subject fusion。

---

# 73. 可反駁條件

本文至少存在以下可反駁方向。

1. 若 biological, digital, physical 與 hybrid substrate 在功能研究上完全無法形成有用分類， $\Sigma$ 軸需要重構。
2. 若 distributed 與 substrate type 在實證上不可分離，本文對型別分離的主張需修改。
3. 若 embodied / non-embodied systems 在系統結構上不存在重要差異， $\mathcal E$ 軸需要弱化。
4. 若 physical computing 無法實際承擔任何有意義的控制或資訊處理， $\Sigma_P$ 的獨立地位應縮小。
5. 若 organoid systems 長期無法完成可重現資訊處理， $\Sigma_B$ 作為計算基質的工程範圍需下修。
6. 若 biohybrid systems 的生物元件始終只具有被動材料功能，biohybrid intelligence substrate 的強版本需要放棄。
7. 若 runtime、memory、control 與 physical boundaries 在所有系統中總是重合，本文多邊界模型是不必要的。
8. 若 multi-node distributed AI 無法維持一致狀態、任務與記憶，則「一個 AI 跨多節點」只能保留為有限工程情境。
9. 若同一 intelligence controller 無法有效控制多 embodiment，multi-body intelligence 的一般性需下修。
10. 若 substrate replacement 必然造成全部功能不可保留，substrate portability 命題需削弱。

---

# 74. Non-Claims

本文明確不主張以下命題：

1. 不主張所有 AI 都能脫離數位電子基質。
2. 不主張生物計算一定優於數位計算。
3. 不主張數位計算一定優於生物計算。
4. 不主張 neuromorphic computing 等同生物神經系統。
5. 不主張 physical computing 等同 AI。
6. 不主張所有物理動力學都是智能。
7. 不主張所有 soft robot 都有 physical intelligence。
8. 不主張 organoid intelligence 已達到人類智能。
9. 不主張 organoid intelligence 已具有意識。
10. 不主張 organoid intelligence 已具有主體性。
11. 不主張 brain organoid 等同完整人腦。
12. 不主張 biological information processing 等同人格。
13. 不主張 DARPA HyBRIDS 已創造自主生物 AI。
14. 不主張 biohybrid robot 是一個統一生物個體。
15. 不主張使用 living muscle 的機器人具有感質。
16. 不主張 BCI 會自動形成新的人機主體。
17. 不主張 implant 使用者不再是原來的法律人格。
18. 不主張 closed-loop coupling 等同 ontological fusion。
19. 不主張分散式 AI 一定是一個 AI。
20. 不主張分散式 AI 一定是很多 AI。
21. 不主張一個 process 等於一個 agent。
22. 不主張一個 agent 等於一個 subject。
23. 不主張一個模型 instance 等於一個 person。
24. 不主張一個身體只能承載一個智能系統。
25. 不主張一個智能系統只能擁有一個身體。
26. 不主張機器數量可代表主體數量。
27. 不主張 device count 可代表 intelligence density。
28. 不主張 substrate classification 可以取代 capability classification。
29. 不主張 substrate classification 可以取代 legal classification。
30. 不主張 substrate classification 可以取代 moral-status analysis。
31. 不主張 functional equivalence 等同 consciousness equivalence。
32. 不主張 behavioral equivalence 等同 identity continuity。
33. 不主張 substrate portability 證明 mind uploading。
34. 不主張 mind uploading 不可能。
35. 不主張本文解決心身問題。
36. 不主張本文解決意識難題。
37. 不主張本文定義「生命」。
38. 不主張本文定義「數位生命」。
39. 不主張混合材料必然帶來更強智能。
40. 不主張 distributed architecture 必然更安全。
41. 不主張 distributed architecture 必然更危險。
42. 不主張單體 architecture 必然較易治理。
43. 不主張 biological systems 必然較能自我修復。
44. 不主張所有 biohybrid system 都可成長或繁殖。
45. 不主張多基質 AI 已經大規模商用。
46. 不主張未來一定會走向 biological AI。
47. 不主張未來一定會走向 human-AI fusion。
48. 不主張未來所有 AI 都會具身。
49. 不主張未來所有 AI 都會分散式。
50. 不主張本文已窮盡所有可能的計算與智能基質。

---

# 75. 結論：未來問題不再是「AI 在哪台機器裡？」

人類早期會問：

> 這個工具是不是機器？

AI 時代早期會問：

> 這台機器有沒有 AI？

EXS-05 再問：

> AI 是附加功能，還是這台機器的架構核心？

但如果：

$$
\Sigma
$$

可以是：

- digital；
- physical；
- neuromorphic；
- biological；
- hybrid；

而：

$$
\Tau
$$

又可以是：

- monolithic；
- modular；
- multi-node；
- distributed；

且：

$$
\mathcal E
$$

可以從：

$$
\text{no embodiment}
$$

一路到：

$$
\text{closed-loop physical embodiment},
$$

那麼：

$$
\boxed{
\text{machine}
}
$$

已經不能作為智能文明的最高分類。

更一般的問題應改成：

$$
\boxed{
\text{What substrate carries the intelligence?}
}
$$

$$
\boxed{
\text{How is it distributed?}
}
$$

$$
\boxed{
\text{How does it couple to the world?}
}
$$

$$
\boxed{
\text{Where are its operational, memory, control, legal and subject boundaries?}
}
$$

因此本文把：

$$
\boxed{
\text{AI Machine}
}
$$

升級為：

$$
\boxed{
\text{Intelligence-Bearing Substrate System}.
}
$$

最重要的型別安全則是：

$$
\boxed{
\text{Substrate}
\neq
\text{Topology}
\neq
\text{Capability}
\neq
\text{Agency}
\neq
\text{Subjectivity}.
}
$$

一個生物系統可以沒有主體性證據。

一個純數位系統也不能因此排除未來可能存在主體性。

一個分散式系統可以工程上是一個系統，也可能由很多獨立 agents 組成。

一個 BCI 可以高度耦合，也不自動意味新主體誕生。

因此，真正耐用的未來智能研究，不應先把：

$$
\text{machine},
\text{body},
\text{agent},
\text{identity},
\text{subject}
$$

綁成同一個詞。

而應分型。

這也使 EXS 系列最後一篇的問題變得更清楚：

> 當智能不再只是一個固定機器中的功能，而可以跨基質、跨節點、跨身體選擇與組合能力時，它是否可能進一步成為「修改能力網路本身」的節點？

換句話說：

$$
\boxed{
\text{Tool}
\rightarrow
\text{Intelligence-Bearing Tool}
\rightarrow
\text{Tool That Selects and Builds Tools}.
}
$$

這就是 EXS-07：

**《會自己打科技樹的科技：從外部能力到自我延展文明》**

的主題。

---

# 參考文獻

[1] Wang, J. et al. (2026). **Embodying physical computing into soft robots.** *Nature Communications*, 17, 2455. 該 perspective 提出 analog oscillators、physical reservoir computing 與 physical algorithmic computing 等 physical computing strategy，並討論把計算更直接分布進機器人身體結構。本文於 2026-08-18 重新核對。

[2] U.S. National Science Foundation. (2025–2026). **Foundations of Emerging Technologies / Computer Systems Research.** NSF 將 biological systems、neuromorphic computing、brain-inspired hardware、analog 與其他 unconventional computing 列為新型計算研究方向。

[3] U.S. National Science Foundation. (2023–2025). **EFRI: Biocomputing through EnGINeering Organoid Intelligence (BEGIN OI), NSF 24-508.** 計畫支持設計與工程化能動態處理資訊並與非生物系統介接的 organoid systems，並明確提醒不同學科對 intelligence 與 learning 的定義不同。

[4] U.S. National Science Foundation. (2024). **NSF invests 14 million USD in bioengineered systems and ethical biocomputing research.** NSF 支持七個 biological computing / organoid intelligence 團隊，包括 adaptive reservoir computing 與 neuron-soft organoid-computer interface。

[5] Defense Advanced Research Projects Agency. (2025–2026). **HyBRIDS: Hybridizing Biology and Robotics through Integration for Deployable Systems.** DARPA 計畫研究 synthetic 與 biological components 的整合，以形成 biohybrid platforms。

[6] Kim, M. S. et al. (2025). **Biohybrid actuators in robotics: recent trends and future perspectives.** *npj Robotics*. 相關研究以 living skeletal / cardiac muscle 與 synthetic structure 形成 biohybrid robotic actuation，並指出穩定性、scalability 與 biotic-abiotic integration 等限制。

[7] National Institutes of Health, BRAIN Initiative. **BRAIN 2025: A Scientific Vision / BRAIN Initiative research roadmap.** NIH 支持神經記錄、BCI、意圖解碼、prosthetic control 與 closed-loop stimulation 等 neurotechnology，展示 human neural substrate 與人工系統之高頻寬耦合研究。

[8] Nature Machine Intelligence / Nature collections. (2025–2026). **Embodied AI / From embodied intelligence to physical AI / embodied neuromorphic agents.** 相關工作研究感知、動作、物理世界模型、neuromorphic system 與 embodied intelligence 的結合。

[9] Wang, H. et al. (2026). **Biohybrid robots evolutionized by soft electronics.** *npj Flexible Electronics*. 該 perspective 討論 living-muscle biohybrid robots 與 soft electronics 的感測、刺激與整合。

[10] NSF. (2026). **Understanding the Brain / Computing and biological systems programs.** NSF 持續把 biological computation、neuromorphic computing、AI 與 neuroscience 視為跨領域前沿。

[11] NIH BRAIN Initiative. (2025–2026). **Bridging Brains and AI / NeuroAI activities.** BRAIN Initiative 探討 neuroscience、AI、neuromorphic computing、embodiment、physical intelligence 與 neurotechnology 的雙向研究接口。

[12] Scientific Reports. (2026). **Morphologically tunable mycelium chips for physical reservoir computing.** 研究展示以 biofabricated mycelium-based substrate 作為 physical reservoir computing 材料的實驗方向，說明 biological / physical computing boundary 正持續被探索。

[13] Nature Communications. (2026). **Reprogrammable metamaterial robot with embodied versatile computation and mechanical intelligence.** 研究利用材料與機械結構本身的動態實現訊號處理與 embodied computation，進一步支持 body-as-computational-resource 的研究路徑。

---

# 附錄 A｜最小符號表

| 符號 | 意義 |
|---|---|
| $\Sigma$ | 智能承載基質軸 |
| $\Sigma_D$ | 數位／電子基質 |
| $\Sigma_P$ | 物理／機械計算基質 |
| $\Sigma_N$ | 神經形態基質 |
| $\Sigma_B$ | 生物計算基質 |
| $\Sigma_H$ | 混合基質 |
| $\Tau$ | 系統拓樸軸 |
| $\Tau_0$ | 單節點／單體 |
| $\Tau_1$ | 模組化 |
| $\Tau_2$ | 多節點協作 |
| $\Tau_3$ | 分散式智能系統 |
| $\mathcal E$ | 具身／世界耦合軸 |
| $\mathcal E_0$ | 無直接物理閉環 |
| $\mathcal E_1$ | 感測耦合 |
| $\mathcal E_2$ | 行動耦合 |
| $\mathcal E_3$ | 閉環具身 |
| $\mathcal B$ | 邊界族 |
| $\mathcal B_P$ | 物理邊界 |
| $\mathcal B_R$ | runtime／程序邊界 |
| $\mathcal B_M$ | 記憶邊界 |
| $\mathcal B_C$ | 控制邊界 |
| $\mathcal B_L$ | 法律邊界 |
| $\mathcal B_S$ | 主體邊界 |
| $\rho_I$ | 概念性智能密度 |
| $P_C$ | physical computing contribution |
| $H_B$ | biohybrid integration depth |

---

# 附錄 B｜四軸分類

$$
\boxed{
\mathcal X
=
(
\Sigma,
\Tau,
\mathcal E,
\mathcal B
)
}
$$

第一軸：

$$
\Sigma
=
\text{what carries intelligence-related computation}.
$$

第二軸：

$$
\Tau
=
\text{how components are arranged across nodes}.
$$

第三軸：

$$
\mathcal E
=
\text{how the system senses and acts in a physical environment}.
$$

第四軸：

$$
\mathcal B
=
\text{which boundary is being asked about}.
$$

---

# 附錄 C｜最重要的型別安全

$$
\boxed{
\text{Biological}
\neq
\text{Conscious}.
}
$$

$$
\boxed{
\text{Distributed}
\neq
\text{Many Subjects}.
}
$$

$$
\boxed{
\text{Coupled}
\neq
\text{Fused}.
}
$$

$$
\boxed{
\text{Embodied}
\neq
\text{Subjective}.
}
$$

$$
\boxed{
\text{Functional Equivalence}
\neq
\text{Ontological Equivalence}.
}
$$

$$
\boxed{
\text{Substrate}
\neq
\text{Topology}
\neq
\text{Capability}
\neq
\text{Agency}
\neq
\text{Subjectivity}.
}
$$

---

# 附錄 D｜EXS 系列累積鏈

EXS-01：

$$
\boxed{
\text{Internal Capability}
\neq
\text{Accessible Capability}.
}
$$

EXS-02：

$$
\boxed{
\text{Accessible Capability}
\neq
\text{Resilient Capability}.
}
$$

EXS-03：

$$
\boxed{
\text{Humanly Usable Knowledge}
\neq
\text{Humanly Executed Every Step}.
}
$$

EXS-04：

$$
\boxed{
\text{AI Presence}
\neq
\text{AI Penetration}
\neq
\text{AI Dependency}.
}
$$

EXS-05：

$$
\boxed{
\text{AI Capability}
\neq
\text{AI Architectural Nativity}.
}
$$

EXS-06：

$$
\boxed{
\text{Machine}
\neq
\text{the universal boundary of intelligence}.
}
$$

---

# 附錄 E｜下一篇接口

**EXS-07｜會自己打科技樹的科技：從外部能力到自我延展文明**

核心將由：

$$
\boxed{
\text{Intelligence-Bearing Substrate}
}
$$

進一步推到：

$$
\boxed{
\text{Capability-Graph-Editing Intelligence}.
}
$$

即：

$$
A:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
$$

最終問題不再只是：

> 人類用什麼工具擴張能力？

而是：

> 當某種智能載體可以發現、選擇、組合、設計與製造新的能力載體時，文明的科技樹是否第一次得到一個能修改科技樹本身的節點？

這將完成第一系列「人類能力外部化與智能載體演化」的閉合。
