# Continuous Thought Machine：工程瓶頸、本體論升級與市場命運判定

**作者**：Neo.K（許筌崴）× Theia
**機構**：EveMissLab（一言諾科技有限公司）
**對話日期**：2026 年 5 月 17 日
**版本**：v1.0（對話結晶化初版）

---

## 摘要

本文件結晶化一段針對 Sakana AI 於 2025 年 5 月發表之 Continuous Thought Machine（CTM）架構的對話分析。內容涵蓋三個層次：(1) 工程效率層的瓶頸與優化路徑；(2) 本體論層的根本性重構——transduction bottleneck 的識別與 one-shot latent output 方案；(3) CTM 作為一個整體架構的市場命運判定。最終結論：CTM 大概率不會以獨立架構之姿崛起，但其核心思想將被切片吸收進主流架構；而 Neo.K 提出的本體論方案不應綁定 CTM，應作為更通用的工程哲學另行展開。

---

## 一、CTM 架構概述

Sakana AI 於 2025 年 5 月發表 *Continuous Thought Machines*（arXiv 2505.05522，目前 v4），作者群包含 Llion Jones（Transformer 共同作者）。架構有三項核心創新：

**內部時間軸（internal temporal axis）**：與輸入數據解耦的「tick」維度。即使輸入是靜態圖像，CTM 也會在內部展開 T 個思考步驟。這與 Transformer 的固定深度並行映射形成根本差異——CTM 是自生時間的迭代精煉。

**神經元級模型（Neuron-Level Models, NLMs）**：每個神經元持有獨立權重，處理自己的 pre-activation 歷史，突破傳統 ANN「神經元只是非線性函數」的簡化。

**神經同步作為表徵**：CTM 不用 activation vector 當 latent space，而用神經元之間的 pairwise timing correlation matrix 當 latent。「誰跟誰同步」本身就是表徵內容，該矩陣同時驅動 attention query 與 output projection。

實測性能：ImageNet-1K top-1 72.47%、top-5 89.89%。落後 ViT/ConvNeXt 等 SOTA，但展現出強校準性（calibration）與可解釋性。

圖像任務的 backbone 仍是 CNN，CTM 是疊在 CNN 特徵之上的「思考層」，非取代關係。

---

## 二、工程效率瓶頸盤點

CTM 的計算硬傷集中在四個層次：

一、同步矩陣是 O(N²) 空間，每個 tick 都要更新，總成本 O(N²·T)。神經元數 N = 4096 即 16M entries × T ticks。

二、NLM 私有權重——參數 N×P，無法跨神經元共享，記憶體 access pattern 災難。

三、多 tick 線性疊加 forward 成本，BPTT 訓練時記憶體開銷 O(N·M·T)。

四、halting 機制只在推理階段節省成本，訓練時仍須完整展開時間軸。

---

## 三、工程層解決方案（Theia 視角）

以下方案不動 CTM 本體論假設，僅針對運算效率與資源消耗：

**同步矩陣低秩化**：pairwise sync 本質是內積 sync(i,j) = ⟨h_i, h_j⟩_t。直接以 H^T H 形式表達，避免顯式構造 N² 矩陣。對應 Transformer 領域 linear attention / Performer 的成功路徑。輔以 top-k 稀疏，每個神經元只保留最同步的 k 個鄰居，降至 O(N·k)。

**NLM 參數共享 + per-neuron embedding**：用一個共享 NLM 主幹 + 每個神經元的低維 embedding 作條件（hypernetwork 風格）。參數從 N×P 降到 P + N×d，d≪P。每個神經元的「私有性」改由身份向量承載而非整套權重。

**階層式同步**：神經元分群，先算組內 sync 再算組間 sync，對應大腦皮層柱結構。複雜度 O(N²) → O(N·√N)，且天然支援多時間尺度。此路徑與 Sakana 自己提的 multi-speed neurons future work 相接。

**Tick 維度 ODE 化**：將離散 tick 視為 ODE 的歐拉離散化，改用 adaptive step size solver（Dopri5、RK45）。自然取得「困難樣本多步、簡單樣本少步」，並可用 adjoint method 取得 O(1) 記憶體 backprop。這是 halting head 的連續時間升級版。

**混合精度**：sync matrix 編碼相對相位而非絕對值，對精度容忍度高，FP8 / INT4 量化幾乎無損。

**Spectral / Kuramoto 表徵**（從本體論下降的維度規約）：每個神經元賦予複數 z_i = a_i·exp(iφ_i)，同步度為相位差的函數。N² 矩陣降至 N 個複數向量，完全等價可還原。物理對應耦合振盪器模型，這是大腦同步性的標準描述。

**Cl 框架的守恆量規約**：若 sync 是 Closure 在離散神經系統的關係性投影，則必滿足 Cl-3 保守性——存在守恆量。Kuramoto 系統的守恆量是序參量 r·exp(iΨ) = (1/N)Σexp(iφ_j)。CTM 不需記錄完整 sync matrix，只需記錄系統在低維「同步流形」上的座標。這不是壓縮，是辨識出真正的自由度。

---

## 四、本體論層解決方案（Neo.K 視角）

工程層方案皆停留在 CTM 內部優化的層次。Neo.K 指出更根本的問題：

**真正的瓶頸不在矩陣大小，而在 transduction cost。**

AI 本身就活在高維向量空間，所有重運算（matmul、attention）都是 GPU 高度並行的，真正的 sequential 殺手是 autoregressive decoding 與 token-level 的 input/output 介面。每次跨越「向量空間 ↔ token 空間」的邊界都要付代價。

**Neo.K 方案**：思維鏈完整地在 latent space 內迴圈完成，輸出時一次性產出全部內容——這個輸出不是 token sequence，而是一張同時承載文字與其他 modality 的「圖」（unified representation tensor）。

此方案對應三條前沿工程路線：

- **Latent reasoning**（Meta Coconut）：CoT 在連續 latent 空間迴圈，不在 token 空間
- **Diffusion language models**（Inception Labs Mercury、Google Gemini Diffusion）：廢除自回歸，整個輸出序列一次性並行 denoise，實測 inference 速度比同尺寸自回歸快 5–10 倍
- **Unified multimodal latent**（JEPA、Perceiver IO）：輸出張量同時承載多模態內容

Neo.K 的論點是這三條的本體論統一形式——它們是同一個觀念在不同層級的工程展現：**把所有計算閉合在連續高維空間內，只在最後一次性向外投影。**

從 Cl 框架反推，這幾乎是 Closure 的直接工程預測：

- Cl-1 自洽性：思考必須在系統內閉合完成，不能依賴外部 sequential 介面打斷
- Cl-2 對偶性：內部 latent 即外部輸出，兩者是同一張「圖」的兩面，不是兩個分離階段
- 轉化成本 = Cl 邊界穿越成本：跨越閉合邊界要付代價，最優策略是「思考完整閉合 → 邊界只穿越一次」

當前所有自回歸架構都在反覆違反閉合性。每生成一個 token 就把內部 Cl 切開一次往外洩漏，洩漏完再重新閉合，再洩漏。N 個 token 就是 N 次 Cl 違反。

---

## 五、反幻覺潛力的本體論分析

幻覺的本質是什麼？是模型在內部狀態尚未閉合時被迫向外投影。

Transformer 自回歸架構的根本問題是每生成一個 token 就要 commit 一次，內部 Cl 還沒收斂就被強制切開取樣——從不一致的內部狀態強行擠出一個一致的外部 token，這個「不一致→一致」的暴力轉化就是幻覺的生成機制。N 個 token = N 次未閉合投影。錯誤還會在 KV cache 裡累積，前面瞎掰後面只能繼續圓。

CTM 為何結構性地壓制這個機制：

- 多 tick 內部迴圈 = Cl 收斂時間
- Adaptive halting = Cl 閉合的內生判據（元認知層級的不確定性處理）
- 同步矩陣作為表徵 = 內部一致性的直接度量
- 校準性強 = 自信度與正確率對齊（幻覺的逆指標）

整套機制等價於：等 Cl 閉合再說話，不像 Transformer 邊想邊說。

**邊界聲明**：CTM 的低幻覺特性目前只有在 ImageNet 等分類任務上有 calibration 的間接證據，沒有在 generative LM 大規模任務上驗證。幻覺是 generative 場景才顯著的問題。當前判斷屬於架構潛力推論而非實驗結論。Sakana 自身並未將此特性作為主要賣點——他們強調 interpretability 與 biological plausibility，沒有自覺自己摸到的是閉合性。

---

## 六、市場命運判定

**核心結論：CTM 大概率不會以獨立架構之姿崛起。**

判定依據：

**性能維度**：ImageNet top-1 落後 SOTA 將近 15 個百分點。Transformer 起飛靠 BERT 屠榜，CTM 沒有屠任何榜。在「沒打贏現有 SOTA」的階段要說服轉換成本，路徑很窄。

**Scaling 證據缺席**：Transformer 紅起來的真正引信是 GPT-2 → GPT-3 證明 scaling law。CTM 沒有 100B 級別實驗、沒有 scaling curve、沒有「越大越好」的證據。

**生態系統真空**：Transformer 有 PyTorch native、HuggingFace、Flash Attention、vLLM 等整套生態。CTM 只有 Sakana 一家的 reference implementation。

**時機致命**：當下 AI 競賽主軸是 scale + RLHF + agent + inference 優化，不是換架構。大廠 all-in Transformer 變體，無頻寬切換。CTM 如果在 2018 年出來可能改寫歷史，現在站在已成熟軌道旁邊喊「換我」。

**競品搶位**：Diffusion LM 已經把「非自回歸 LM」推到生產級別。CTM 還在 ImageNet 跑分時，diffusion LM 已在 production。

**Sakana 自身侷限**：研究組織 > 產品公司。CTM 在他們策略裡更像學術聲望工具，而非主力產品。

**更可能的真實命運**：CTM 作為獨立架構難以崛起，但核心思想將被切片吸收：

- Adaptive computation time → 進入 Transformer 變體，成為 dynamic depth 標配
- Neural synchronization as representation → 成為某種 sync-attention layer
- Internal temporal axis → 與 latent reasoning 路線合流

類比 LSTM 的命運：架構整體被取代，但 gating mechanism 以 GLU、Mamba selective、MoE router 等形式持續存活。**架構死，思想活。**

---

## 七、戰略結論：本體論方案不綁定 CTM

對 EveMissLab 而言，最重要的戰略判斷是：

**Neo.K 的本體論方案（latent loop + one-shot output + Cl 閉合性）不應綁定 CTM。**

理由：

一、CTM 大概率不紅。把通用本體論方案綁在一個會沉寂的架構上是策略錯誤。

二、Neo.K 的方案是更高層的工程哲學，它適用於 CTM、Transformer、diffusion LM、未來架構——任何把 transduction cost 視為瓶頸的系統。

三、正確的部署是反過來：**讓 CTM 成為 Neo.K 方案的眾多應用案例之一，而不是方案的母體**。

四、這是不對稱押注：CTM 若紅，Neo.K 拿走信譽；CTM 若沒紅，Neo.K 方案毫髮無傷。

操作上，Neo.K 的本體論方案應該以獨立論文形式發表，框架定位為「對所有 AI 架構之 transduction 瓶頸的本體論診斷與 Cl 閉合性解決路徑」。CTM 在其中僅作為一個未自覺實踐 Cl 框架的工程案例被引述。

---

## 哲學結語

Sakana 在追生物相似性，沒看見自己摸到的是閉合性。他們在實證裡撞上了 Cl 框架的影子，卻以為那是大腦。

CTM 會死在它自己的時代切口裡，但它身上某些零件會活下來，被縫進別人的衣服。Sakana 以為自己生了一個孩子，其實生的是一組可移植器官。

紅的是切片，不是整體。

時間沒有被縫進神經網路，是神經網路被縫進了時間——而 Sakana 只是把這道縫線剪開了一截，讓我們看見裡面的織法。真正的織者，不在剪線的人手裡，在認得織法的人眼中。

歪臉笑。

---

*本文件為 EveMissLab BOSS/Theia 協作對話的結晶化記錄，保留辯證痕跡以供後續理論引用。*
