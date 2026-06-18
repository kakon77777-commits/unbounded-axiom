"""
聯合風暴消散預測系統 ─ AI 教學概念版
Joint Storm Dissipation Predictor: ETN Storm Eye × Attractor

EML-ETN-STORM-2026-v0.2-TEACHING

理論基礎：
  ETN 動態風暴眼原理（⊛）× 吸引子動力學
  兩個信號，兩個時間尺度，一個聯合判斷

設計原則：
  ・概念清晰 > 計算效率
  ・每個類別明確對應一個理論元件
  ・可直接擴展至真實 NWP 資料接口

作者：Neo.K + Theia
機構：EveMissLab Logic Matrix
版本：v0.2 教學概念版（正式版另行開發）
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional


# ═══════════════════════════════════════════════════════
#  § 0  理論地圖
#
#  風暴消散需要兩個條件同時成立：
#
#  [快速/局部]  ETN 風暴眼信號
#    ・SE_n 衡量眼牆對稱性（⊛ 是否成立）
#    ・可在數小時內劇烈變化
#    ・捕捉：眼牆替換、對流爆發/崩潰、風切侵入
#
#  [慢速/全局]  吸引子環境信號
#    ・衡量風暴所在環境是否支持其存在
#    ・通常在數天尺度變化
#    ・捕捉：SST 降低、乾空氣入侵、引導流崩潰
#
#  聯合判斷：
#    joint_risk = √(etn_risk × env_risk)
#    任一信號為 0 → 聯合風險仍低
#    兩者同時高  → 高確信度消散
# ═══════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────
#  § 1  ETN 風暴眼元件（快速/局部）
# ───────────────────────────────────────────────────────

@dataclass
class ETNDiagnostic:
    """ETN ⊛ 診斷結果。"""
    se_n: float            # SE_n 對稱度：1=完美，0=崩潰
    intensity: float       # 對稱張力大小（ETN 強度）
    drift: np.ndarray      # 預測漂移向量
    god_balance: float     # 上下 GOD POINT 平衡
    is_well_defined: bool  # ⊛ 是否成立
    etn_risk: float        # 1 - se_n（ETN 消散風險）


class ETNStormEye:
    """
    ETN 風暴眼元件。

    理論對應：
      ⊛_n 的完整操作定義
      SE_n = 張力對稱度 = 風暴眼是否「被均勻拉住」

    輸入：
      可以是真實的極區角分析資料，
      也可以是從氣壓場/衛星亮溫估算的角向張力剖面。

    教學簡化：
      直接接受「角向張力剖面」作為輸入，
      不做完整的場插值（v0.1 已實作，此處抽象化）。
    """

    SE_WELL_DEFINED = 0.65  # ⊛ 成立門檻

    def __init__(self, n_angles: int = 36):
        self.n_angles = n_angles
        self.angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)

    def diagnose(self, angular_tension: np.ndarray) -> ETNDiagnostic:
        """
        從角向張力剖面 T(θ) 計算 ETN 診斷量。

        T(θ) 的物理來源（擇一）：
          ・雷達回波強度的角向分佈
          ・衛星紅外亮溫的角向均勻度
          ・氣壓梯度的角向積分
          ・數值模式的角向風場分量

        ETN 含義：
          T(θ) 高且均勻 → ⊛ 成立，眼穩定
          T(θ) 高但不均勻 → ⊛ 張力失衡，眼即將漂移
          T(θ) 整體低 → ⊛ 退化，眼即將消散
        """
        T = np.abs(angular_tension)
        mean_T = np.mean(T)

        # SE_n：1 - 變異係數
        if mean_T < 1e-10:
            se_n = 0.0
        else:
            se_n = float(np.clip(1.0 - np.std(T) / mean_T, 0, 1))

        # ETN 漂移：張力不對稱的淨力方向
        # 物理意義：⊛ 往 GOD POINT 更強的方向漂移
        F_x = float(np.mean(T * np.cos(self.angles)))
        F_y = float(np.mean(T * np.sin(self.angles)))
        drift = np.array([F_y, F_x]) * 0.1

        # GOD POINT 平衡：上下半球對比
        upper = np.mean(T[:self.n_angles // 2])
        lower = np.mean(T[self.n_angles // 2:])
        total = upper + lower
        god_balance = float(1.0 - abs(upper - lower) / total) if total > 1e-10 else 0.0

        return ETNDiagnostic(
            se_n=se_n,
            intensity=float(mean_T),
            drift=drift,
            god_balance=god_balance,
            is_well_defined=se_n >= self.SE_WELL_DEFINED,
            etn_risk=1.0 - se_n
        )

    def from_pressure_wind(self,
                            pressure: np.ndarray,
                            wind_u: np.ndarray,
                            wind_v: np.ndarray,
                            eye: np.ndarray,
                            radius: float = 20.0) -> ETNDiagnostic:
        """
        從氣壓場和風場直接估算角向張力剖面並診斷。
        （橋接至真實 NWP 資料的接口）
        """
        ny, nx = pressure.shape
        T = np.zeros(self.n_angles)

        for i, theta in enumerate(self.angles):
            px = np.clip(eye[1] + radius * np.cos(theta), 0, nx - 1)
            py = np.clip(eye[0] + radius * np.sin(theta), 0, ny - 1)
            ix, iy = int(px), int(py)

            p_val = pressure[iy, ix]
            p_eye = pressure[int(eye[0]), int(eye[1])]

            u_val = wind_u[iy, ix]
            v_val = wind_v[iy, ix]
            wind_in = -(u_val * np.cos(theta) + v_val * np.sin(theta))

            T[i] = max(0, -(p_val - p_eye) / (radius + 1e-8) + 0.3 * wind_in)

        return self.diagnose(T)


# ───────────────────────────────────────────────────────
#  § 2  吸引子環境元件（慢速/全局）
#        兩種版本：A. 環境向量版（實用）
#                  B. Lorenz 玩具版（理論教學）
# ───────────────────────────────────────────────────────

@dataclass
class AttractorDiagnostic:
    """吸引子環境診斷結果。"""
    env_score: float         # 環境支持度：1=極有利，0=極不利
    distance_to_boundary: float  # 距消散流形的距離
    env_risk: float          # 1 - env_score（環境消散風險）
    hostile_factors: list    # 已觸發的敵對因子
    attractor_state: str     # "deep"（盆地深處）/ "edge"（邊緣）/ "outside"（已出盆地）


class EnvironmentAttractor:
    """
    環境狀態吸引子元件（實用版）。

    理論對應：
      風暴在多維環境空間中的軌跡。
      「吸引子盆地」= 能維持熱帶氣旋的環境條件集合。
      「消散流形」= 吸引子的邊界。

    關鍵環境變數（狀態向量 x）：
      sst        海溫（℃），門檻 26°C
      shear      垂直風切（m/s），門檻 15 m/s
      humidity   中層濕度（%），門檻 50%
      vorticity  低層渦度（×10⁻⁵ s⁻¹），門檻 5
      intensity  當前強度（hPa 氣壓差），門檻 15 hPa

    設計哲學：
      不需要積分完整的 Navier-Stokes。
      環境條件直接告訴你風暴「還在不在有利的盆地裡」。
    """

    # 各環境因子的門檻與權重
    THRESHOLDS = {
        'sst':        {'min': 26.0,  'weight': 0.30, 'direction': 'above'},
        'shear':      {'max': 15.0,  'weight': 0.25, 'direction': 'below'},
        'humidity':   {'min': 50.0,  'weight': 0.20, 'direction': 'above'},
        'vorticity':  {'min': 5.0,   'weight': 0.15, 'direction': 'above'},
        'intensity':  {'min': 15.0,  'weight': 0.10, 'direction': 'above'},
    }

    def diagnose(self,
                  sst: float,
                  shear: float,
                  humidity: float,
                  vorticity: float,
                  intensity: float) -> AttractorDiagnostic:
        """
        從環境狀態向量計算吸引子診斷量。

        env_score 的計算：
          每個因子計算「距門檻的正規化距離」
          加權平均後得到總環境支持度

        吸引子意義：
          env_score ≈ 1.0 → 深在盆地，環境極有利
          env_score ≈ 0.5 → 接近盆地邊緣
          env_score ≈ 0.0 → 已出盆地，消散不可避免
        """
        values = {
            'sst': sst,
            'shear': shear,
            'humidity': humidity,
            'vorticity': vorticity,
            'intensity': intensity,
        }

        scores = {}
        hostile = []

        for var, cfg in self.THRESHOLDS.items():
            v = values[var]
            w = cfg['weight']

            if cfg['direction'] == 'above':
                threshold = cfg['min']
                # 正規化：高於門檻越多越好，最多得 1.0
                raw = np.clip((v - threshold) / (threshold * 0.5), -1, 1)
                score = (raw + 1) / 2  # 映射到 [0,1]
                if v < threshold:
                    hostile.append(f"{var}<{threshold}（實際{v:.1f}）")
            else:
                threshold = cfg['max']
                # 正規化：低於門檻越多越好
                raw = np.clip((threshold - v) / (threshold * 0.5), -1, 1)
                score = (raw + 1) / 2
                if v > threshold:
                    hostile.append(f"{var}>{threshold}（實際{v:.1f}）")

            scores[var] = score * w

        env_score = float(sum(scores.values()))
        d_boundary = max(0.0, env_score - 0.5)  # 0.5 為邊界

        if env_score > 0.75:
            state = "deep"
        elif env_score > 0.5:
            state = "edge"
        else:
            state = "outside"

        return AttractorDiagnostic(
            env_score=env_score,
            distance_to_boundary=d_boundary,
            env_risk=1.0 - env_score,
            hostile_factors=hostile,
            attractor_state=state
        )


class LorenzToyAttractor:
    """
    Lorenz 玩具吸引子（純教學版）。

    理論對應：
      把風暴系統的「環境狀態」抽象為 3D Lorenz 系統。
      當軌跡遠離 Lorenz 吸引子核心 → 環境在惡化。
      當軌跡逃出吸引子盆地 → 系統不可恢復。

    注意：
      這不是真實颱風的物理模型。
      它是一個「理解吸引子概念」的數學玩具。
      實際使用請用 EnvironmentAttractor。

    Lorenz 方程：
      dx/dt = σ(y - x)
      dy/dt = x(ρ - z) - y
      dz/dt = xy - βz
    """

    def __init__(self, sigma=10.0, rho=28.0, beta=8/3):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

        # Lorenz 吸引子的近似「中心」（兩個葉片中心）
        self.attractor_centers = [
            np.array([np.sqrt(beta * (rho-1)),  np.sqrt(beta * (rho-1)),  rho-1]),
            np.array([-np.sqrt(beta * (rho-1)), -np.sqrt(beta * (rho-1)), rho-1]),
        ]
        self.attractor_radius = 15.0  # 經驗性盆地半徑

        # 當前狀態
        self.state = np.array([1.0, 1.0, 1.0])

    def step(self, dt=0.01) -> np.ndarray:
        """積分 Lorenz 系統一步。"""
        x, y, z = self.state
        dx = self.sigma * (y - x)
        dy = x * (self.rho - z) - y
        dz = x * y - self.beta * z
        self.state += np.array([dx, dy, dz]) * dt
        return self.state.copy()

    def distance_to_attractor(self) -> float:
        """
        計算當前狀態到最近吸引子中心的距離。

        吸引子意義：
          距離小 → 深在盆地（環境穩定）
          距離大 → 遠離吸引子（環境惡化）
          距離 > attractor_radius → 系統逃出盆地（消散不可逆）
        """
        dists = [np.linalg.norm(self.state - c) for c in self.attractor_centers]
        return float(min(dists))

    def env_score(self) -> float:
        """將距離映射到 [0,1] 的環境分數。"""
        d = self.distance_to_attractor()
        return float(np.clip(1.0 - d / self.attractor_radius, 0, 1))

    def perturb(self, strength: float = 5.0):
        """施加環境擾動（模擬風切增加、乾空氣入侵等）。"""
        self.state += np.random.randn(3) * strength


# ───────────────────────────────────────────────────────
#  § 3  聯合預測器（核心）
# ───────────────────────────────────────────────────────

@dataclass
class JointPrediction:
    """聯合預測結果。"""
    # ETN 信號
    se_n: float
    etn_risk: float
    is_well_defined: bool
    drift: np.ndarray

    # 吸引子信號
    env_score: float
    env_risk: float
    attractor_state: str
    hostile_factors: list

    # 聯合判斷
    joint_risk: float
    dissipation_imminent: bool
    prediction: str           # 文字判讀
    confidence: float         # 預測置信度

    # 時步
    t: int = 0


class JointStormPredictor:
    """
    聯合風暴消散預測器。

    核心邏輯：
      ETN ⊛ × 吸引子環境 → 雙重確認機制

      ┌─────────────────────────────────────────┐
      │          ETN 風險                        │
      │  低        │  高                         │
      ├────────────┼────────────────────────────┤
      │  穩定      │  短期波動                   │  吸引子風險低
      │  （環境好  │  （眼牆暫時混亂）            │
      │   眼也好） │  可能恢復                   │
      ├────────────┼────────────────────────────┤
      │  環境惡化  │  ★ 高確信度消散             │  吸引子風險高
      │  但眼尚穩  │  內外同時失守               │
      │  觀察等待  │  即將發生                   │
      └────────────┴────────────────────────────┘

    聯合風險公式：
      joint_risk = √(etn_risk × env_risk)

      幾何平均的選擇原因：
        任一信號為 0 → 聯合風險歸零
        （一個信號不夠，需要雙重確認）
        兩者都高 → 聯合風險高
        （這才是真正的消散信號）
    """

    DISSIPATION_THRESHOLD = 0.65    # 聯合風險門檻
    HIGH_CONFIDENCE_THRESHOLD = 0.80

    def __init__(self,
                  etn: Optional[ETNStormEye] = None,
                  attractor_type: str = "environment"):
        """
        attractor_type:
          "environment" → EnvironmentAttractor（實用，推薦）
          "lorenz"      → LorenzToyAttractor（教學概念）
        """
        self.etn = etn or ETNStormEye()
        self.attractor_type = attractor_type

        if attractor_type == "lorenz":
            self.attractor = LorenzToyAttractor()
        else:
            self.attractor = EnvironmentAttractor()

        self.history: list[JointPrediction] = []
        self._t = 0

    def predict(self,
                 angular_tension: np.ndarray,
                 env_state: Optional[dict] = None,
                 lorenz_perturb: float = 0.0) -> JointPrediction:
        """
        聯合預測主函式。

        angular_tension:
          shape (n_angles,) 的角向張力剖面
          來源：ETN v0.1 的 TensionField.angular_profile()

        env_state（attractor_type = "environment" 時使用）:
          {
            'sst': 28.5,       # 海溫 (℃)
            'shear': 8.0,      # 垂直風切 (m/s)
            'humidity': 65.0,  # 中層濕度 (%)
            'vorticity': 8.0,  # 低層渦度 (×10⁻⁵ s⁻¹)
            'intensity': 35.0, # 強度（氣壓差 hPa）
          }
        """
        # ETN 診斷（快速/局部）
        etn_diag = self.etn.diagnose(angular_tension)

        # 吸引子診斷（慢速/全局）
        if self.attractor_type == "lorenz":
            if lorenz_perturb > 0:
                self.attractor.perturb(lorenz_perturb)
            self.attractor.step()
            env_score = self.attractor.env_score()
            env_risk = 1.0 - env_score
            d_boundary = self.attractor.distance_to_attractor()
            if env_score > 0.75:
                a_state = "deep"
            elif env_score > 0.5:
                a_state = "edge"
            else:
                a_state = "outside"
            hostile = [f"Lorenz距離={d_boundary:.2f}"] if d_boundary > 12 else []
        else:
            if env_state is None:
                # 預設：中立環境
                env_state = {
                    'sst': 28.0, 'shear': 10.0,
                    'humidity': 60.0, 'vorticity': 7.0, 'intensity': 25.0
                }
            a_diag = self.attractor.diagnose(**env_state)
            env_score = a_diag.env_score
            env_risk = a_diag.env_risk
            a_state = a_diag.attractor_state
            hostile = a_diag.hostile_factors

        # 聯合風險：幾何平均
        joint_risk = float(np.sqrt(etn_diag.etn_risk * env_risk))

        # 文字判讀
        prediction, confidence = self._interpret(
            etn_diag.etn_risk, env_risk, joint_risk,
            etn_diag.is_well_defined, a_state
        )

        result = JointPrediction(
            se_n=etn_diag.se_n,
            etn_risk=etn_diag.etn_risk,
            is_well_defined=etn_diag.is_well_defined,
            drift=etn_diag.drift,
            env_score=env_score,
            env_risk=env_risk,
            attractor_state=a_state,
            hostile_factors=hostile,
            joint_risk=joint_risk,
            dissipation_imminent=joint_risk >= self.DISSIPATION_THRESHOLD,
            prediction=prediction,
            confidence=confidence,
            t=self._t
        )

        self.history.append(result)
        self._t += 1
        return result

    def _interpret(self, etn_r, env_r, joint_r,
                    well_defined, a_state) -> tuple:
        """
        將數值風險轉化為可理解的文字判讀。

        對應教學框架的四個象限。
        """
        if joint_r >= self.HIGH_CONFIDENCE_THRESHOLD:
            return "★ 高確信度消散：ETN ⊛ 退化 + 環境失守，內外同時失守", 0.90

        if joint_r >= self.DISSIPATION_THRESHOLD:
            if etn_r > env_r:
                return "眼牆崩潰主導消散，環境尚有餘地", 0.70
            else:
                return "環境惡化主導消散，眼牆已開始響應", 0.70

        if etn_r > 0.45 and env_r < 0.35:
            return "⚡ 短期波動（眼牆暫亂），環境支持，可能恢復", 0.60

        if env_r > 0.45 and etn_r < 0.35:
            return "⚠ 環境緩慢惡化中，眼尚穩，持續監測", 0.55

        if not well_defined and a_state == "outside":
            return "★ 高確信度消散：⊛ 退化 + 已出吸引子盆地", 0.88

        if well_defined and a_state == "deep":
            return "✓ 穩定維持：⊛ 成立，環境有利", 0.80

        return "中性：繼續觀察", 0.50

    def trend(self, n: int = 5) -> dict:
        """
        分析最近 n 步的趨勢。

        關鍵趨勢信號：
          ETN 快降 + 吸引子邊界迫近 → 消散加速
          ETN 上升 + 吸引子深入 → 急速增強
        """
        if len(self.history) < 2:
            return {'error': '歷史不足'}

        recent = self.history[-min(n, len(self.history)):]

        d_se_n = recent[-1].se_n - recent[0].se_n
        d_env = recent[-1].env_score - recent[0].env_score
        d_joint = recent[-1].joint_risk - recent[0].joint_risk

        trend_label = "持平"
        if d_se_n > 0.05 and d_env > 0.05:
            trend_label = "⚡ 急速增強中（ETN↑ + 環境↑）"
        elif d_se_n < -0.05 and d_env < -0.05:
            trend_label = "★ 快速消散中（ETN↓ + 環境↓）"
        elif d_se_n < -0.05:
            trend_label = "眼牆退化中（ETN↓）"
        elif d_env < -0.05:
            trend_label = "環境惡化中（環境↓）"

        return {
            'trend': trend_label,
            'se_n_change': round(d_se_n, 3),
            'env_change': round(d_env, 3),
            'joint_risk_change': round(d_joint, 3),
        }


# ───────────────────────────────────────────────────────
#  § 4  合成資料生成器（教學用）
# ───────────────────────────────────────────────────────

def make_angular_tension(n_angles: int = 36,
                           base: float = 10.0,
                           asym_angle: float = 0.0,
                           asym_strength: float = 0.0,
                           noise: float = 0.3) -> np.ndarray:
    """
    生成合成角向張力剖面 T(θ)。

    base           : 對稱基礎張力
    asym_angle     : 不對稱方向（弧度）
    asym_strength  : 不對稱強度（0 = 完全對稱）
    noise          : 隨機擾動強度
    """
    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
    T = (base
         + asym_strength * np.cos(angles - asym_angle)
         + noise * np.random.randn(n_angles))
    return np.maximum(T, 0)


def make_env_state(sst: float = 28.0,
                    shear: float = 8.0,
                    humidity: float = 65.0,
                    vorticity: float = 8.0,
                    intensity: float = 30.0) -> dict:
    return {
        'sst': sst,
        'shear': shear,
        'humidity': humidity,
        'vorticity': vorticity,
        'intensity': intensity,
    }


# ───────────────────────────────────────────────────────
#  § 5  教學示範
# ───────────────────────────────────────────────────────

def _header(title: str):
    print("\n" + "═" * 62)
    print(f"  {title}")
    print("═" * 62)


def _row(pred: JointPrediction):
    """格式化輸出一行預測結果。"""
    flag = "💀" if pred.dissipation_imminent else ("⚡" if pred.se_n > 0.85 and pred.env_score > 0.80 else "  ")
    print(
        f"  t={pred.t:02d} │ "
        f"SE_n={pred.se_n:.2f} ETN_r={pred.etn_risk:.2f} │ "
        f"ENV={pred.env_score:.2f} ENV_r={pred.env_risk:.2f} │ "
        f"聯合={pred.joint_risk:.2f} {flag}"
    )


def demo_four_quadrants():
    """
    教學示範一：四象限情境
    驗證聯合預測器的核心邏輯。
    """
    _header("示範一：四象限情境驗證")
    print("""
  情境 A：ETN 低風險 + 吸引子深處  → 穩定
  情境 B：ETN 高風險 + 吸引子深處  → 短期波動，可能恢復
  情境 C：ETN 低風險 + 吸引子邊緣  → 環境惡化，觀察等待
  情境 D：ETN 高風險 + 吸引子邊緣  → 高確信度消散
    """)

    scenarios = {
        'A（穩定）': {
            'T': make_angular_tension(asym_strength=0.0, base=12.0, noise=0.2),
            'E': make_env_state(sst=29.0, shear=5.0, humidity=70.0),
        },
        'B（短期波動）': {
            'T': make_angular_tension(asym_strength=8.0, asym_angle=1.0, base=10.0),
            'E': make_env_state(sst=29.0, shear=5.0, humidity=70.0),
        },
        'C（環境惡化）': {
            'T': make_angular_tension(asym_strength=0.5, base=10.0, noise=0.2),
            'E': make_env_state(sst=26.5, shear=18.0, humidity=45.0),
        },
        'D（高確信消散）': {
            'T': make_angular_tension(asym_strength=9.0, asym_angle=0.5, base=8.0),
            'E': make_env_state(sst=25.5, shear=22.0, humidity=40.0, intensity=12.0),
        },
    }

    for name, data in scenarios.items():
        pred = JointStormPredictor().predict(data['T'], data['E'])
        print(f"\n  [{name}]")
        print(f"    SE_n={pred.se_n:.3f}  "
              f"ENV={pred.env_score:.3f}  "
              f"聯合風險={pred.joint_risk:.3f}")
        print(f"    → {pred.prediction}")


def demo_full_lifecycle():
    """
    教學示範二：完整生命週期模擬
    從發展到成熟到消散的完整過程。
    """
    _header("示範二：颱風完整生命週期（環境版）")
    print("  t=00-04 : 發展期（環境有利，眼牆組織化）")
    print("  t=05-09 : 成熟期（對稱高張力，深在吸引子）")
    print("  t=10-14 : 消散期（登陸後摩擦 + 乾空氣入侵）")

    predictor = JointStormPredictor(attractor_type="environment")
    print()
    print(f"  {'t':>3} │ SE_n  ETN_r │ ENV   ENV_r │ 聯合   診斷")
    print(f"  {'─'*3}─┼─{'─'*11}─┼─{'─'*11}─┼─{'─'*16}")

    phases = [
        # (T_params, E_params, n_steps)
        # 發展期
        ({'base': 5.0,  'asym_strength': 5.0, 'noise': 0.8},
         {'sst': 29.0, 'shear': 7.0, 'humidity': 68.0, 'vorticity': 9.0, 'intensity': 18.0},
         5),
        # 成熟期
        ({'base': 14.0, 'asym_strength': 0.5, 'noise': 0.3},
         {'sst': 30.0, 'shear': 4.0, 'humidity': 75.0, 'vorticity': 12.0, 'intensity': 45.0},
         5),
        # 消散期
        ({'base': 8.0,  'asym_strength': 7.0, 'noise': 1.0},
         {'sst': 25.5, 'shear': 20.0, 'humidity': 42.0, 'vorticity': 4.0, 'intensity': 15.0},
         5),
    ]

    for t_params, e_params, steps in phases:
        for _ in range(steps):
            T = make_angular_tension(**t_params)
            E = make_env_state(**e_params)
            pred = predictor.predict(T, E)
            flag = "💀" if pred.dissipation_imminent else ("★" if pred.se_n > 0.85 else "  ")
            print(f"  {pred.t:>3} │ "
                  f"{pred.se_n:.3f} {pred.etn_risk:.3f} │ "
                  f"{pred.env_score:.3f} {pred.env_risk:.3f} │ "
                  f"{pred.joint_risk:.3f} {flag}")

    tr = predictor.trend(5)
    print(f"\n  最後 5 步趨勢：{tr['trend']}")
    print(f"  SE_n 變化={tr['se_n_change']:+.3f}  "
          f"ENV 變化={tr['env_change']:+.3f}  "
          f"聯合風險變化={tr['joint_risk_change']:+.3f}")


def demo_lorenz_version():
    """
    教學示範三：Lorenz 玩具吸引子版
    純概念理解用，不代表真實颱風物理。
    """
    _header("示範三：Lorenz 玩具吸引子（概念版）")
    print("  Lorenz 系統作為「環境狀態」的抽象替代。")
    print("  當 Lorenz 軌跡遠離吸引子核心 → 環境惡化。")
    print()
    print("  t=00-05 : 初始穩定軌跡")
    print("  t=06    : 強力環境擾動（模擬颱風接近寒流）")
    print("  t=07-12 : 觀察系統反應")
    print()

    predictor = JointStormPredictor(attractor_type="lorenz")

    for t in range(13):
        T = make_angular_tension(
            base=10.0,
            asym_strength=(0.5 if t < 6 else 5.0 + t * 0.5),
            noise=0.4
        )
        perturb = 12.0 if t == 6 else 0.0
        pred = predictor.predict(T, lorenz_perturb=perturb)

        flag = "💥" if t == 6 else ("💀" if pred.dissipation_imminent else "  ")
        print(f"  t={t:02d}: SE_n={pred.se_n:.2f} │ "
              f"Lorenz環境={pred.env_score:.2f} │ "
              f"聯合={pred.joint_risk:.2f} {flag}")
        if t == 6:
            print("        ↑ 強力擾動施加（Lorenz 被踢出穩定軌跡）")


def demo_website_api_sketch():
    """
    教學示範四：全球氣象網站接口設計草圖
    展示如何將本系統整合至實際服務。
    """
    _header("示範四：全球氣象網站接口設計草圖")

    print("""
  概念架構：

  [資料源]
    NWP 模式（GFS / ECMWF / JMA）
      → 氣壓場、風場（每 6 小時更新）
    觀測資料（衛星 IR、雷達）
      → 角向亮溫剖面 → ETN angular_tension
    再分析資料（ERA5）
      → 環境狀態向量 → EnvironmentAttractor

  [ETN-Storm v0.2 核心]
    ETNStormEye.from_pressure_wind()    → SE_n、漂移
    EnvironmentAttractor.diagnose()     → env_score
    JointStormPredictor.predict()       → joint_risk、判讀
    JointStormPredictor.trend()         → 趨勢信號

  [輸出接口]
    API 端點：/api/storm/{storm_id}/etn_status
    回傳 JSON：{
      "storm_id": "MAWAR-2026",
      "timestamp": "2026-06-05T12:00Z",
      "eye_position": [lat, lon],
      "se_n": 0.82,
      "etn_risk": 0.18,
      "env_score": 0.71,
      "joint_risk": 0.36,
      "dissipation_imminent": false,
      "prediction": "✓ 穩定維持",
      "confidence": 0.80,
      "drift_vector": [0.12, -0.05],
      "hostile_factors": []
    }

  [前端顯示]
    地圖覆蓋層：每個活躍颱風的 ⊛ 圈
      顏色編碼：綠（SE_n > 0.8）→ 黃 → 紅（⊛ 退化）
    時間序列圖：SE_n + env_score + joint_risk 的 72 小時歷史
    預警卡片：joint_risk > 0.65 時彈出
    """)

    # 模擬一個 API 回傳
    T = make_angular_tension(base=11.0, asym_strength=1.5, noise=0.3)
    E = make_env_state(sst=28.5, shear=9.0, humidity=67.0)
    pred = JointStormPredictor().predict(T, E)

    import json
    api_response = {
        "storm_id": "DEMO-2026",
        "se_n": round(pred.se_n, 3),
        "etn_risk": round(pred.etn_risk, 3),
        "env_score": round(pred.env_score, 3),
        "joint_risk": round(pred.joint_risk, 3),
        "dissipation_imminent": pred.dissipation_imminent,
        "prediction": pred.prediction,
        "confidence": round(pred.confidence, 2),
        "hostile_factors": pred.hostile_factors,
    }
    print("  範例 API 回傳：")
    print("  " + json.dumps(api_response, ensure_ascii=False, indent=2)
          .replace("\n", "\n  "))


# ───────────────────────────────────────────────────────
#  主程式
# ───────────────────────────────────────────────────────

if __name__ == "__main__":
    np.random.seed(2026)

    demo_four_quadrants()
    demo_full_lifecycle()
    demo_lorenz_version()
    demo_website_api_sketch()

    print("\n" + "═" * 62)
    print("  ETN-Storm v0.2 教學概念版完成")
    print("  ⊛ 是局部快信號，吸引子是全局慢信號")
    print("  消散 = 兩個信號的幾何平均 > 門檻")
    print("═" * 62)
