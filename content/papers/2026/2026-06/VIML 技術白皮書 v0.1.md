# VIML 技術白皮書 v0.1
## 視覺意圖標記語言：系統架構、符號集規格與AI生成管道實現

**作者：Neo.K (許筌崴)**
**機構：EveMissLab (一言諾科技有限公司)**
**日期：2026年6月**
**文件性質：技術白皮書（Technical Whitepaper）——對應理論框架論文《VIML視覺意圖標記語言》**

---

## 摘要

本白皮書為VIML（Visual Intent Markup Language）的技術實現規格文件，覆蓋以下四個層次：符號資源採集層（爬蟲策略與Agent分類工作流）、符號集數據規格（ISS六類符號的JSON標準定義）、符號→ControlNet conditioning映射協議（各類符號到AI生成系統輸入的技術轉換規則）、AI API整合層（後端選擇、調用流程、結果處理）。本文件同時提供MVP（最小可用產品）的實現路線圖與優先級排序，以及基礎教學大綱規格。

**技術棧**：Python 3.11+、ComfyUI（主要後端）、FLUX.2（主要生成模型）、ControlNet（conditioning框架）、本地LLM Agent（符號分類）

---

## 1. 系統架構總覽

### 1.1 四層架構

```
┌─────────────────────────────────────┐
│         Layer 4: 用戶介面層          │
│  畫布 + 符號拖放 + 文字提示輸入      │
└──────────────┬──────────────────────┘
               │  符號配置 JSON
┌──────────────▼──────────────────────┐
│         Layer 3: 意圖解析層          │
│  SCR衝突檢查 + 符號→conditioning映射 │
└──────────────┬──────────────────────┘
               │  conditioning maps + text prompt
┌──────────────▼──────────────────────┐
│         Layer 2: API整合層           │
│  ComfyUI workflow / FLUX.2 API      │
└──────────────┬──────────────────────┘
               │  生成結果
┌──────────────▼──────────────────────┐
│         Layer 1: 符號資源層          │
│  ISS符號庫 + 爬蟲採集 + Agent分類   │
└─────────────────────────────────────┘
```

### 1.2 數據流

```
用戶放置符號 
  → 生成 scene_intent.json（符號配置）
  → SCR衝突解析
  → 生成 conditioning_maps（OpenPose/Depth/Normal）
  → 合併文字提示 text_prompt
  → 調用 ComfyUI API
  → 返回生成圖像
  → 顯示 + 允許意圖迭代調整
```

---

## 2. 符號資源採集層

### 2.1 爬蟲來源優先級

**P1級（直接可用，格式標準）**

| 來源 | 類別覆蓋 | 格式 | 授權 |
|------|---------|------|------|
| OpenPose官方示例庫 | PA全部 | JSON keypoints | Apache 2.0 |
| ControlNet官方條件圖範例 | PA/SC/LS/CA | PNG conditioning maps | 開源 |
| Noun Project API（免費tier） | LS/CA/MT/RD | SVG | CC Attribution |
| Flaticon基礎套件 | LS/CA/MT | SVG | 免費個人用 |

**P2級（需Agent處理分類）**

| 來源 | 類別覆蓋 | 說明 |
|------|---------|------|
| storyboardthat.com符號集 | PA/SC/RD | 需截圖+向量化 |
| 電影分鏡範例圖（公共域） | CA/SC/RD | 需Agent從圖中提取符號 |
| 建築/工程圖標準符號集 | SC/MT | ISO標準符號，公共域 |
| Adobe Stock免費圖標（每月） | MT/LS | 需手動整理 |

**P3級（半自動生成）**

| 來源 | 說明 |
|------|------|
| 用Midjourney/FLUX生成符號SVG | 需人工審核抽象度 |
| 從現有ControlNet pose圖提取 | Agent識別關節點 |

### 2.2 爬蟲工作流

```python
# 爬蟲Pipeline概覽（偽代碼）

class VIMLCrawler:
    
    def crawl_openpose_samples(self):
        """抓取OpenPose骨架樣本，提取keypoints JSON"""
        # 目標：50-100種標準姿態
        # 輸出：PA類符號原始數據包
        
    def crawl_svg_icons(self, sources=['nounproject', 'flaticon']):
        """抓取SVG圖標，覆蓋LS/CA/MT/RD類"""
        # 搜索關鍵詞：sun, light, camera, angle, texture, arrow
        # 輸出：原始SVG文件包 + 元數據
        
    def crawl_storyboard_examples(self):
        """從分鏡範例中提取符號模式"""
        # 輸出：截圖包 + Agent待分類列表
        
    def generate_sc_symbols(self):
        """生成SC類空間符號（幾何形狀，無需爬取）"""
        # 直接生成：方格線、三分法網格、深度分層線
        # 輸出：SC類SVG集合
```

### 2.3 本地Agent分類工作流

爬取的原始資源需要通過本地LLM Agent進行分類和標注，輸出符合ISS規格的JSON記錄。

**Agent系統提示詞（核心版本）**：

```
你是VIML符號集的分類Agent。你的任務是對輸入的圖像符號進行分析和分類。

對每個符號，輸出以下JSON：
{
  "category": "PA/SC/LS/CA/MT/RD",
  "sub_type": "具體子類型",
  "abstraction_level": 0.0-1.0（0=完全具體，1=完全抽象），
  "intent_dimension": "這個符號能表達的意圖維度描述",
  "conflict_tags": ["與此符號衝突的其他符號標籤列表"],
  "controlnet_type": "openpose/depth/normal/canny/text_only",
  "machine_readable": true/false（是否可自動轉為conditioning map）,
  "text_hint": "若machine_readable=false，轉換為文字提示的模板"
}

分類標準：
- 符號應表達「創作者意圖」而非「視覺內容」
- abstraction_level高意味著符號不過度規定具體外觀
- 若符號包含具體的視覺內容（真實人物照片、詳細場景），判定為不適合ISS，返回null
```

**分類批處理腳本**：

```python
import json
from pathlib import Path

def classify_symbols_batch(raw_symbols_dir, agent_client, output_path):
    """
    批量分類原始符號資源
    raw_symbols_dir: 爬取的原始SVG/PNG目錄
    agent_client: 本地LLM客戶端（Ollama/LM Studio等）
    output_path: 輸出的符號集JSON路徑
    """
    results = []
    
    for symbol_file in Path(raw_symbols_dir).iterdir():
        # 將符號圖像轉為base64或描述文字
        symbol_desc = extract_symbol_description(symbol_file)
        
        # Agent分類
        classification = agent_client.classify(
            system_prompt=VIML_CLASSIFIER_PROMPT,
            input=symbol_desc
        )
        
        if classification:  # Agent判定適合ISS
            results.append({
                "symbol_id": generate_symbol_id(classification),
                "source_file": str(symbol_file),
                **classification
            })
    
    with open(output_path, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    return results
```

---

## 3. ISS符號集數據規格

### 3.1 符號記錄標準格式

每個ISS符號的標準JSON記錄如下：

```json
{
  "symbol_id": "PA_stand_neutral_001",
  "category": "PA",
  "sub_type": "standing",
  "name_zh": "站立中性姿態",
  "name_en": "Standing Neutral Pose",
  "version": "1.0.0",
  "abstraction_level": 0.75,
  "svg_path": "symbols/PA/stand_neutral_001.svg",
  "thumbnail_path": "thumbnails/PA/stand_neutral_001.png",
  "controlnet_type": "openpose",
  "keypoints": {
    "nose":           [0.500, 0.120],
    "neck":           [0.500, 0.200],
    "right_shoulder": [0.420, 0.270],
    "left_shoulder":  [0.580, 0.270],
    "right_elbow":    [0.380, 0.380],
    "left_elbow":     [0.620, 0.380],
    "right_wrist":    [0.360, 0.490],
    "left_wrist":     [0.640, 0.490],
    "right_hip":      [0.440, 0.520],
    "left_hip":       [0.560, 0.520],
    "right_knee":     [0.430, 0.680],
    "left_knee":      [0.570, 0.680],
    "right_ankle":    [0.430, 0.850],
    "left_ankle":     [0.570, 0.850]
  },
  "conflict_tags": ["PA_sitting", "PA_lying", "PA_crouching"],
  "composable_with": ["SC_*", "LS_*", "CA_*", "MT_skin_*", "RD_*"],
  "text_hint": "",
  "machine_readable": true,
  "tags": ["human", "standing", "neutral", "full_body"],
  "source": "openpose_standard",
  "license": "Apache-2.0"
}
```

**SC類符號範例（佔位符）**：

```json
{
  "symbol_id": "SC_placeholder_figure_foreground_001",
  "category": "SC",
  "sub_type": "depth_foreground",
  "name_zh": "前景人物佔位符",
  "abstraction_level": 0.90,
  "svg_path": "symbols/SC/placeholder_figure_fg_001.svg",
  "controlnet_type": "depth",
  "depth_value": 0.85,
  "relative_size": "large",
  "position_anchor": "bottom_left",
  "conflict_tags": [],
  "machine_readable": true,
  "text_hint": "foreground figure, close to camera"
}
```

**LS類符號範例（光源）**：

```json
{
  "symbol_id": "LS_directional_upper_left_hard_001",
  "category": "LS",
  "sub_type": "directional_hard",
  "name_zh": "左上方硬光源",
  "abstraction_level": 0.85,
  "svg_path": "symbols/LS/sun_upper_left_001.svg",
  "controlnet_type": "normal_map",
  "light_direction": [-0.577, -0.577, 0.577],
  "light_quality": "hard",
  "color_temperature": "neutral",
  "conflict_tags": ["LS_soft_*_same_direction"],
  "machine_readable": true,
  "text_hint": "dramatic directional lighting from upper left, hard shadows"
}
```

### 3.2 符號集目錄結構

```
viml_symbols/
├── index.json                    # 符號集總索引
├── PA/                           # 姿態/動作類（目標50-100個）
│   ├── standing/
│   ├── sitting/
│   ├── action/
│   └── emotion_overlays/
├── SC/                           # 空間/構圖類（目標30-50個）
│   ├── placeholders/
│   ├── depth_layers/
│   ├── composition_guides/
│   └── occlusion_markers/
├── LS/                           # 光源/光影類（目標20-30個）
│   ├── directional/
│   ├── ambient/
│   └── special/
├── CA/                           # 鏡頭/視角類（目標15-25個）
│   ├── angle/
│   ├── focal_length/
│   └── depth_of_field/
├── MT/                           # 材質/質感類（目標20-30個）
│   ├── organic/
│   ├── manufactured/
│   └── elemental/
└── RD/                           # 關係/動態類（目標20-30個）
    ├── attention/
    ├── character_relation/
    └── scene_dynamics/
```

### 3.3 場景意圖配置格式（scene_intent.json）

用戶在畫布上放置符號後，系統生成以下配置文件：

```json
{
  "scene_id": "scene_20260609_001",
  "canvas_size": [1024, 1024],
  "symbols": [
    {
      "symbol_id": "PA_stand_neutral_001",
      "position": {"x": 0.30, "y": 0.50},
      "scale": 0.8,
      "rotation": 0,
      "layer": "foreground",
      "character_id": "char_A"
    },
    {
      "symbol_id": "SC_placeholder_figure_background_001",
      "position": {"x": 0.70, "y": 0.40},
      "scale": 0.5,
      "rotation": 0,
      "layer": "midground",
      "character_id": "char_B"
    },
    {
      "symbol_id": "LS_directional_upper_left_hard_001",
      "position": {"x": 0.15, "y": 0.10},
      "scale": 1.0,
      "rotation": 0,
      "applies_to": "global"
    },
    {
      "symbol_id": "CA_eye_level_standard_001",
      "position": {"x": 0.50, "y": 0.50},
      "applies_to": "global"
    }
  ],
  "text_prompt": "two people in conversation, urban background, realistic style",
  "negative_prompt": "blurry, distorted, unrealistic anatomy",
  "generation_params": {
    "steps": 30,
    "cfg_scale": 7.5,
    "seed": -1
  }
}
```

---

## 4. SCR衝突解析引擎（MVP版本）

### 4.1 MVP衝突檢查範疇

MVP版本只實現以下三類衝突檢查，其餘複雜衝突允許通過（後覆蓋原則）：

**Class A衝突（必須阻止，提示用戶）**：
- 同一角色/物件同時有多個互斥的PA姿態（站立+坐下）
- 同一場景同時有多個互斥的CA視角（俯視+仰視）
- 同一光源位置有多個互斥的LS光質符號

**Class B衝突（警告，允許繼續）**：
- 場景中前景層級有超過3個以上的PA符號（可能過於擁擠）
- LS和CA的組合在物理上不常見（正對光源的仰視鏡頭）

**Class C衝突（記錄，不提示）**：
- 其他非標準組合，記錄在日誌供後續分析

```python
class SCREngine:
    
    MUTEX_PAIRS = {
        "PA": [
            ("PA_standing_*", "PA_sitting_*"),
            ("PA_standing_*", "PA_lying_*"),
            ("PA_sitting_*", "PA_lying_*"),
        ],
        "CA": [
            ("CA_birds_eye_*", "CA_worms_eye_*"),
        ],
        "LS": [
            # 同方向不同光質
        ]
    }
    
    def check_conflicts(self, scene_intent):
        """
        檢查scene_intent.json中的符號衝突
        返回: {
            "class_a": [...],  # 必須解決
            "class_b": [...],  # 建議解決
            "class_c": [...]   # 僅記錄
        }
        """
        conflicts = {"class_a": [], "class_b": [], "class_c": []}
        
        # 按character_id分組檢查PA類衝突
        pa_by_char = self._group_by_character(
            scene_intent["symbols"], category="PA"
        )
        for char_id, pa_symbols in pa_by_char.items():
            mutex = self._find_mutex_in_group(pa_symbols, "PA")
            if mutex:
                conflicts["class_a"].append({
                    "type": "PA_mutex",
                    "character": char_id,
                    "symbols": mutex
                })
        
        # 檢查CA類衝突（全局）
        ca_symbols = [s for s in scene_intent["symbols"] 
                      if s["symbol_id"].startswith("CA_")]
        ca_mutex = self._find_mutex_in_group(ca_symbols, "CA")
        if ca_mutex:
            conflicts["class_a"].append({
                "type": "CA_mutex",
                "symbols": ca_mutex
            })
        
        return conflicts
```

---

## 5. 符號→ControlNet Conditioning映射協議

### 5.1 PA類 → OpenPose Conditioning Map

**輸入**：一個或多個PA符號的keypoints列表（相對坐標）

**輸出**：OpenPose格式的骨架圖像（RGB，標準18關節點彩色圓圈+連接線）

```python
import numpy as np
import cv2

def pa_to_openpose_map(pa_symbols, canvas_size=(1024, 1024)):
    """
    將PA符號轉換為OpenPose conditioning map
    
    pa_symbols: list of {keypoints, position, scale, rotation}
    返回: numpy array shape (H, W, 3), dtype uint8
    """
    OPENPOSE_COLORS = {
        "nose": (255, 0, 0),
        "neck": (255, 85, 0),
        "right_shoulder": (255, 170, 0),
        # ... 18個關節點的顏色定義
    }
    
    canvas = np.zeros((*canvas_size, 3), dtype=np.uint8)
    
    for symbol in pa_symbols:
        # 將相對座標轉換為絕對像素座標
        # 應用position偏移、scale縮放、rotation旋轉
        absolute_keypoints = transform_keypoints(
            symbol["keypoints"],
            symbol["position"],
            symbol["scale"],
            symbol["rotation"],
            canvas_size
        )
        
        # 繪製骨架連接線
        draw_skeleton_connections(canvas, absolute_keypoints, OPENPOSE_COLORS)
        
        # 繪製關節點圓圈
        for joint_name, coords in absolute_keypoints.items():
            if coords is not None:
                cv2.circle(canvas, coords, 5, 
                          OPENPOSE_COLORS[joint_name], -1)
    
    return canvas
```

### 5.2 SC類 → Depth Map

**輸入**：SC符號的depth_value（0-1，越大越近）和spatial位置

**輸出**：灰度深度圖（值越高=越近/越亮）

```python
def sc_to_depth_map(sc_symbols, canvas_size=(1024, 1024)):
    """
    將SC符號轉換為depth conditioning map
    
    深度分配規則：
    - depth_value=0.9 → 前景（灰度值230）
    - depth_value=0.5 → 中景（灰度值128）  
    - depth_value=0.1 → 遠景（灰度值26）
    - 未覆蓋區域 → 中遠景默認值（灰度值80）
    """
    depth_canvas = np.full(canvas_size, 80, dtype=np.uint8)
    
    for symbol in sc_symbols:
        gray_value = int(symbol["depth_value"] * 255)
        region_mask = symbol_to_region_mask(symbol, canvas_size)
        depth_canvas[region_mask] = gray_value
    
    # 添加輕微高斯模糊使邊界自然過渡
    depth_canvas = cv2.GaussianBlur(depth_canvas, (21, 21), 0)
    
    return depth_canvas
```

### 5.3 LS類 → Normal Map + 文字補充

**輸入**：LS符號的光源方向向量 + 光質屬性

**輸出**：
- Normal map（RGB格式的表面法向量圖）
- 文字提示補充字符串

```python
def ls_to_normal_and_text(ls_symbols, canvas_size=(1024, 1024)):
    """
    將LS符號轉換為normal map和文字提示補充
    
    Normal map格式：RGB值對應法向量(x,y,z)
    (128,128,255) = 指向相機的平面法向量（默認值）
    """
    normal_canvas = np.full(
        (*canvas_size, 3), [128, 128, 255], dtype=np.uint8
    )
    text_supplements = []
    
    for symbol in ls_symbols:
        if symbol.get("machine_readable"):
            # 根據光源方向調整法向量分佈
            light_dir = np.array(symbol["light_direction"])
            adjust_normals_for_light(normal_canvas, light_dir)
        
        # 生成文字補充
        quality_map = {
            "hard": "sharp directional lighting, hard shadows",
            "soft": "soft diffused lighting, gentle shadows",
            "ambient": "ambient lighting, no direct shadows"
        }
        color_temp_map = {
            "warm": "warm golden light",
            "cool": "cool blue-white light",
            "neutral": ""
        }
        
        text_parts = filter(None, [
            quality_map.get(symbol.get("light_quality", ""), ""),
            color_temp_map.get(symbol.get("color_temperature", ""), "")
        ])
        text_supplements.append(", ".join(text_parts))
    
    return normal_canvas, ". ".join(filter(None, text_supplements))
```

### 5.4 CA類 → 文字視角提示

**CA類目前主要通過文字提示傳遞，不生成獨立conditioning map**：

```python
CA_TEXT_MAP = {
    "CA_birds_eye_*":    "bird's-eye view, top-down shot, looking straight down",
    "CA_worms_eye_*":    "worm's-eye view, looking up, low angle shot",
    "CA_eye_level_*":    "eye-level shot, straight-on perspective",
    "CA_high_angle_*":   "high angle shot, slightly elevated viewpoint",
    "CA_low_angle_*":    "low angle shot, slightly below eye level",
    "CA_dutch_angle_*":  "dutch angle, tilted camera, dynamic composition",
    "CA_wide_angle_*":   "wide angle lens, expansive scene, slight distortion",
    "CA_telephoto_*":    "telephoto lens, compressed perspective, shallow depth",
    "CA_dof_shallow_*":  "shallow depth of field, blurred background, focused subject",
    "CA_dof_deep_*":     "deep focus, everything in sharp focus"
}

def ca_to_text(ca_symbols):
    texts = []
    for symbol in ca_symbols:
        for pattern, text in CA_TEXT_MAP.items():
            if fnmatch(symbol["symbol_id"], pattern):
                texts.append(text)
                break
    return ", ".join(texts)
```

### 5.5 MT類 → 文字材質提示（局部）

**MT類通過文字提示的局部區域描述傳遞**，格式：「[位置描述] [材質描述]」：

```python
MT_TEXT_TEMPLATES = {
    "MT_metal_*":       "{position} with metallic surface, reflective, specular highlights",
    "MT_fabric_*":      "{position} with fabric texture, woven material",
    "MT_skin_*":        "{position} with skin texture, natural human skin",
    "MT_wood_*":        "{position} with wooden texture, natural grain",
    "MT_stone_*":       "{position} with stone or concrete surface, rough texture",
    "MT_glass_*":       "{position} transparent glass, refractive",
    "MT_vegetation_*":  "{position} with organic plant texture, leaves or grass",
    "MT_water_*":       "{position} with water surface, fluid, reflective",
    "MT_emissive_*":    "{position} with glowing emissive surface, light source"
}
```

### 5.6 最終Prompt組裝

```python
def assemble_generation_request(scene_intent, conditioning_maps):
    """
    組裝最終的AI生成請求
    
    返回ComfyUI workflow JSON
    """
    # 收集所有文字提示補充
    text_supplements = []
    
    for symbol in scene_intent["symbols"]:
        if symbol["symbol_id"].startswith("LS_"):
            _, ls_text = ls_to_normal_and_text([symbol])
            text_supplements.append(ls_text)
        elif symbol["symbol_id"].startswith("CA_"):
            text_supplements.append(ca_to_text([symbol]))
        elif symbol["symbol_id"].startswith("MT_"):
            text_supplements.append(mt_to_text(symbol))
        elif symbol["symbol_id"].startswith("RD_"):
            text_supplements.append(rd_to_text(symbol))
    
    # 組合完整提示詞
    final_prompt = ", ".join(filter(None, [
        scene_intent.get("text_prompt", ""),
        *text_supplements
    ]))
    
    return build_comfyui_workflow(
        prompt=final_prompt,
        negative_prompt=scene_intent.get("negative_prompt", ""),
        conditioning_maps=conditioning_maps,
        generation_params=scene_intent.get("generation_params", {})
    )
```

---

## 6. AI API整合層

### 6.1 後端選擇

**主要後端：ComfyUI**（推薦）

ComfyUI是首選後端，原因：支持完整的ControlNet pipeline（OpenPose/Depth/Normal同時輸入）；支持FLUX.2模型；有詳細的API文件；工作流可視化有助調試；本地部署，保護創作內容。

**備用後端：Replicate API**（雲端，無需本地GPU）

適合無高性能GPU的使用者。支持FLUX.2和基本ControlNet。API調用更簡單但靈活性略低。

**後端配置文件（config.json）**：

```json
{
  "backend": "comfyui",
  "comfyui": {
    "host": "127.0.0.1",
    "port": 8188,
    "model": "flux2_dev.safetensors",
    "controlnet_openpose": "controlnet_openpose_flux.safetensors",
    "controlnet_depth": "controlnet_depth_flux.safetensors",
    "controlnet_normal": "controlnet_normal_flux.safetensors"
  },
  "replicate": {
    "api_key": "YOUR_API_KEY",
    "model": "black-forest-labs/flux-dev",
    "controlnet_model": "xlabs-ai/flux-dev-controlnet"
  }
}
```

### 6.2 ComfyUI Workflow生成

```python
def build_comfyui_workflow(prompt, negative_prompt, 
                            conditioning_maps, generation_params):
    """
    生成ComfyUI API所需的workflow JSON
    
    conditioning_maps: {
        "openpose": numpy_array or None,
        "depth": numpy_array or None,
        "normal": numpy_array or None
    }
    """
    workflow = {
        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {"ckpt_name": CONFIG["comfyui"]["model"]}
        },
        "2": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": prompt,
                "clip": ["1", 1]
            }
        },
        # ... 完整workflow節點
    }
    
    # 動態添加有效的ControlNet節點
    node_idx = 10
    prev_model_ref = ["1", 0]
    
    for cn_type, cn_map in conditioning_maps.items():
        if cn_map is not None:
            # 添加ControlNet加載節點
            workflow[str(node_idx)] = build_controlnet_node(
                cn_type, cn_map, prev_model_ref
            )
            prev_model_ref = [str(node_idx), 0]
            node_idx += 1
    
    # 添加採樣和解碼節點
    workflow["99"] = {
        "class_type": "KSampler",
        "inputs": {
            "model": prev_model_ref,
            "positive": ["2", 0],
            "negative": ["3", 0],
            "latent_image": ["4", 0],
            "seed": generation_params.get("seed", -1),
            "steps": generation_params.get("steps", 30),
            "cfg": generation_params.get("cfg_scale", 7.5),
            "sampler_name": "dpmpp_2m",
            "scheduler": "karras",
            "denoise": 1.0
        }
    }
    
    return workflow


def send_to_comfyui(workflow):
    """發送workflow到ComfyUI並等待結果"""
    import requests
    import websocket
    import json
    
    # 上傳conditioning圖像
    for key, img_array in extract_images_from_workflow(workflow):
        upload_image_to_comfyui(key, img_array)
    
    # 提交workflow
    response = requests.post(
        f"http://{CONFIG['comfyui']['host']}:{CONFIG['comfyui']['port']}/prompt",
        json={"prompt": workflow}
    )
    prompt_id = response.json()["prompt_id"]
    
    # 通過WebSocket等待完成
    result = wait_for_completion(prompt_id)
    return result
```

### 6.3 Python SDK 入口點

```python
# viml_sdk/client.py

class VIMLClient:
    """
    VIML SDK主客戶端
    
    使用範例：
    
    client = VIMLClient(config_path="config.json")
    
    scene = client.new_scene(size=(1024, 1024))
    scene.add_symbol("PA_stand_neutral_001", position=(0.3, 0.5), scale=0.8)
    scene.add_symbol("LS_directional_upper_left_hard_001")
    scene.add_symbol("CA_eye_level_standard_001")
    scene.set_text_prompt("two friends talking, sunny day, urban background")
    
    result = client.generate(scene)
    result.save("output.png")
    result.show()
    """
    
    def __init__(self, config_path="config.json"):
        self.config = load_config(config_path)
        self.symbol_registry = SymbolRegistry.load("viml_symbols/index.json")
        self.scr_engine = SCREngine(self.symbol_registry)
    
    def new_scene(self, size=(1024, 1024)):
        return Scene(size=size, registry=self.symbol_registry)
    
    def generate(self, scene):
        # 衝突檢查
        conflicts = self.scr_engine.check_conflicts(scene.to_intent_json())
        if conflicts["class_a"]:
            raise ConflictError(conflicts["class_a"])
        
        # 生成conditioning maps
        maps = generate_conditioning_maps(scene)
        
        # 組裝請求並發送
        workflow = assemble_generation_request(
            scene.to_intent_json(), maps
        )
        return send_to_backend(workflow, self.config)
```

---

## 7. 基礎教學大綱

### 7.1 教學結構

教學以Jupyter Notebook形式提供，共四個模組：

**Notebook 01：快速開始（30分鐘）**

```
1. 安裝 viml-sdk
2. 配置 ComfyUI 後端
3. 第一個場景：放置PA符號 + 簡單文字提示
4. 生成第一張圖 + 查看結果
5. 調整文字提示，觀察效果差異
```

**Notebook 02：符號組合基礎（1小時）**

```
1. SC類空間符號：前景/中景/遠景配置
2. LS類光源符號：不同光源方向的效果對比
3. CA類視角符號：俯視/平視/仰視的差異
4. 符號組合示範：PA+SC+LS+CA的完整場景
5. 衝突案例演示：典型Class A衝突及解決方法
```

**Notebook 03：意圖迭代精化（1小時）**

```
1. 從MCSI出發：最小完整意圖的生成結果
2. 逐步添加符號：觀察IF的提升
3. 空白意圖的利用：哪些地方不要規定
4. 文字提示與VIML符號的分工配合
5. 多次迭代的工作流程示範
```

**Notebook 04：分鏡序列（進階，2小時）**

```
1. 多幀場景的基本概念
2. 時序符號的使用
3. 角色/場景一致性配置
4. 生成3-5幀的簡單分鏡序列
5. 完整分鏡工作流程的結合示範
```

### 7.2 入門所需ISS子集（最小學習集）

新使用者只需先掌握以下5個符號，即可完成Notebook 01：

| 符號ID | 類別 | 作用 |
|--------|------|------|
| PA_stand_neutral_001 | PA | 站立人物佔位 |
| SC_placeholder_figure_foreground_001 | SC | 前景佔位 |
| SC_composition_thirds_001 | SC | 三分法構圖輔助線 |
| LS_directional_upper_left_hard_001 | LS | 基本光源 |
| CA_eye_level_standard_001 | CA | 平視鏡頭 |

其餘符號在後續練習中逐步引入。

---

## 8. MVP實現路線圖

### 8.1 Phase 0：基礎設施（預估：2週）

- [ ] 建立爬蟲腳本（P1級來源）
- [ ] 配置本地Agent分類工作流
- [ ] 輸出初版ISS符號集（目標：PA×20、SC×10、LS×10、CA×8、MT×5、RD×5）
- [ ] 建立符號集目錄結構和index.json

### 8.2 Phase 1：核心管道（預估：2週）

- [ ] PA→OpenPose mapping（pa_to_openpose_map）
- [ ] SC→Depth map mapping（sc_to_depth_map）
- [ ] LS→Normal + Text（ls_to_normal_and_text）
- [ ] CA/MT/RD→Text templates
- [ ] ComfyUI workflow生成和調用
- [ ] 基本SCR衝突檢查（Class A only）

### 8.3 Phase 2：SDK和教學（預估：1週）

- [ ] VIMLClient SDK封裝
- [ ] Notebook 01和02
- [ ] 基本錯誤處理和日誌

### 8.4 Phase 3：擴充（持續）

- [ ] 擴充ISS符號集至目標數量
- [ ] Notebook 03和04
- [ ] Replicate備用後端
- [ ] IF量化指標初版
- [ ] SCR Class B衝突規則

### 8.5 MVP完成標準

以下場景可以完整執行，視為MVP達成：

```python
client = VIMLClient()
scene = client.new_scene()

scene.add_symbol("PA_stand_neutral_001", position=(0.3, 0.6), scale=0.7)
scene.add_symbol("SC_placeholder_figure_background_001", position=(0.7, 0.4), scale=0.4)
scene.add_symbol("LS_directional_upper_left_hard_001")
scene.add_symbol("CA_eye_level_standard_001")
scene.set_text_prompt("two people in a coffee shop, afternoon light")

result = client.generate(scene)
result.save("test_output.png")
# 生成的圖像符合：前景站立人物、右後方次要人物、左上方光源、平視視角
```

---

## 9. 已知限制與後續擴展方向

### 9.1 MVP的已知限制

**符號→conditioning的轉換精度**：PA→OpenPose的骨架轉換在複雜姿態（手部精細動作、面部朝向）上精度有限。SC→Depth的轉換使用簡化的深度分層，不支持複雜的深度漸變。

**SCR的不完整**：MVP只處理Class A衝突，Class B和C留作後續。某些複雜的跨類別衝突（例如，CA_telephoto與SC的空間配置不匹配）在MVP版本中不被識別。

**後端依賴**：MVP依賴本地ComfyUI安裝。對無GPU使用者的支持（Replicate後端）在Phase 3才加入。

### 9.2 後續高優先擴展

**視覺化介面**：MVP版本是純代碼API。後續需要一個直觀的畫布介面讓使用者拖放符號（Electron桌面應用或Figma插件是候選方向）。

**與SAL的整合**：若未來SAL系統實現，VIML的符號可以直接對應到SAL的τ（色塊標注）和ρ（連接標注），形成完整的意圖→生成→理解→反饋循環。

**ISS動態擴充API**：讓使用者提交自己的符號到符號集，通過Agent審核後加入社群符號庫。

---

**文件性質**：技術白皮書 v0.1，MVP實現規格
**對應理論文件**：《VIML視覺意圖標記語言》理論框架論文
**版本**：v0.1
**作者**：Neo.K (許筌崴)，EveMissLab (一言諾科技有限公司)，台灣

*符號是橋；橋的這頭是意圖；橋的那頭是生成。白皮書是橋的施工圖。*
