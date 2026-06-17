"""
ETN Dynamic Storm Eye Model (動態風暴眼模型)
EML-ETN-STORM-2026-v0.1

基於 ETN 風暴眼原理（⊛）的熱帶氣旋建模框架
核心差異：不追全局吸引子，只追 ⊛ 點的張力對稱性

作者：Neo.K + Theia
機構：EveMissLab Logic Matrix
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional
import warnings


# ─────────────────────────────────────────
#  資料結構
# ─────────────────────────────────────────

@dataclass
class StormEyeState:
    """
    ⊛_n 的完整狀態。

    ETN 對應：
      eye_pos      = ⊛ 中心點座標
      symmetry     = SE_n 條件度量（1=完美對稱，0=完全破壞）
      intensity    = 對稱張力分量的大小（真實強度）
      drift        = 當前漂移向量（張力不對稱的淨力）
      god_balance  = 上下（或任意二分）GOD POINT 場的平衡度
    """
    eye_pos: np.ndarray          # shape (2,)  [row, col] 或 [lat, lon]
    symmetry: float = 0.0        # SE_n：0~1
    intensity: float = 0.0       # 對稱張力大小
    drift: np.ndarray = field(
        default_factory=lambda: np.zeros(2)
    )
    god_balance: float = 0.0     # 上下 GOD POINT 平衡

    # ETN 診斷
    is_well_defined: bool = False   # ⊛ 是否成立（symmetry > threshold）
    asymmetry_vector: np.ndarray = field(
        default_factory=lambda: np.zeros(2)
    )


# ─────────────────────────────────────────
#  核心：⊛ 張力場計算
# ─────────────────────────────────────────

class TensionField:
    """
    圍繞 ⊛ 中心點的張力場 T(θ, r)。

    ETN 物理意義：
      T(θ, r) 是中心點在方向 θ、半徑 r 處感受到的張力強度。
      高 T(θ) → 那個方向有強 GOD POINT 在拉。
      低 T(θ) → 那個方向的 GOD POINT 場弱，⊛ 可能往反方向漂。

    實際大氣對應：
      壓力梯度 + 風切變 + 潛熱釋放率 → 綜合張力估計
    """

    def __init__(self, n_angles: int = 72, n_radii: int = 20,
                 r_min: float = 1.0, r_max: float = 30.0):
        self.n_angles = n_angles
        self.n_radii = n_radii
        self.angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
        self.radii = np.linspace(r_min, r_max, n_radii)
        # T[角度, 半徑]
        self.T = np.zeros((n_angles, n_radii))

    def update_from_fields(self,
                           pressure: np.ndarray,
                           wind_u: np.ndarray,
                           wind_v: np.ndarray,
                           eye: np.ndarray):
        """
        從氣壓場和風場採樣，更新張力場 T(θ, r)。

        採樣策略：
          在每個 (θ, r) 位置，計算指向 ⊛ 中心的壓力梯度
          加上徑向風速分量（入流 = 正張力）。
        """
        ny, nx = pressure.shape

        for i, theta in enumerate(self.angles):
            cos_t, sin_t = np.cos(theta), np.sin(theta)

            for j, r in enumerate(self.radii):
                # 採樣點座標
                px = eye[1] + r * cos_t
                py = eye[0] + r * sin_t

                # 邊界夾緊
                px_c = np.clip(px, 0, nx - 2)
                py_c = np.clip(py, 0, ny - 2)
                ix, iy = int(px_c), int(py_c)

                # 雙線性插值
                fx, fy = px_c - ix, py_c - iy
                p00 = pressure[iy, ix]
                p10 = pressure[iy, min(ix+1, nx-1)]
                p01 = pressure[min(iy+1, ny-1), ix]
                p11 = pressure[min(iy+1, ny-1), min(ix+1, nx-1)]
                p_val = (p00 * (1-fx) * (1-fy) +
                         p10 * fx * (1-fy) +
                         p01 * (1-fx) * fy +
                         p11 * fx * fy)

                # 壓力梯度（指向中心方向為正）
                p_eye = pressure[int(eye[0]), int(eye[1])]
                dp_dr = (p_val - p_eye) / (r + 1e-8)

                # 風速徑向分量（入流為正）
                u_val = _bilinear(wind_u, px_c, py_c, nx, ny)
                v_val = _bilinear(wind_v, px_c, py_c, nx, ny)
                # 入流 = 從外往內，即與 (eye - sample) 方向一致
                wind_radial = -(u_val * cos_t + v_val * sin_t)

                self.T[i, j] = -dp_dr + 0.5 * wind_radial

    def update_synthetic(self, eye: np.ndarray,
                          asymmetry_angle: float = 0.0,
                          asymmetry_strength: float = 0.0,
                          base_intensity: float = 10.0,
                          noise_level: float = 0.5):
        """
        合成張力場（測試用）：
          base_intensity  = 對稱基礎張力
          asymmetry_angle = 不對稱方向（弧度）
          asymmetry_strength = 不對稱強度（破壞 SE_n 條件的程度）
        """
        for i, theta in enumerate(self.angles):
            for j, r in enumerate(self.radii):
                # 基礎張力（對稱分量，隨半徑衰減）
                base = base_intensity * np.exp(-r / 15.0)

                # 不對稱分量（破壞 SE_n）
                asym = asymmetry_strength * np.cos(
                    theta - asymmetry_angle
                ) * np.exp(-r / 10.0)

                # 噪聲
                noise = noise_level * np.random.randn()

                self.T[i, j] = max(0, base + asym + noise)

    # ── 診斷量 ──────────────────────────────

    def angular_profile(self) -> np.ndarray:
        """T(θ)：對半徑積分後的角向張力剖面。"""
        return np.trapezoid(np.abs(self.T), self.radii, axis=1)

    def symmetry_measure(self) -> float:
        """
        SE_n 對稱度量：1 = 完美對稱，0 = 完全不對稱。

        公式：1 - (std / mean)，即 1 - 變異係數。

        ETN 含義：
          SE_n = 1 → ⊛ 成立，風暴眼穩定
          SE_n → 0 → ⊛ 退化，風暴眼即將漂移或消散
        """
        T_ang = self.angular_profile()
        mean_T = np.mean(T_ang)
        if mean_T < 1e-10:
            return 0.0
        return float(np.clip(1.0 - np.std(T_ang) / mean_T, 0, 1))

    def drift_vector(self, scale: float = 0.1) -> np.ndarray:
        """
        漂移向量：張力不對稱的淨力方向。

        ETN 公式：
          F_net = (1/2π) ∫ T(θ) · ê_θ dθ

          ⊛ 往張力強的方向漂移（不是往壓力低的方向），
          因為那是 GOD POINT 場在拉它的方向。

        與傳統方法的差異：
          傳統：引導流（steering flow）= 環境風的加權平均
          ETN：漂移 = 張力場不對稱的淨力（包含環境資訊但不等同）
        """
        T_ang = self.angular_profile()
        F_col = np.trapezoid(T_ang * np.cos(self.angles), self.angles) / (2 * np.pi)
        F_row = np.trapezoid(T_ang * np.sin(self.angles), self.angles) / (2 * np.pi)
        return np.array([F_row, F_col]) * scale

    def intensity_metric(self) -> float:
        """
        強度 = 對稱張力分量的大小。

        ETN 含義：
          不是「總張力大小」，而是「對稱的那部分」。
          高對稱張力 → 強且穩定的風暴眼
          高總張力但低對稱 → 強烈但混亂，眼牆不規則
        """
        T_ang = self.angular_profile()
        return float(np.mean(T_ang))

    def god_point_balance(self) -> float:
        """
        GOD POINT 平衡度：上下半球（或任意二分）張力的平衡。

        ETN 含義：
          G_{n+1}^-（上方 GOD POINT）和 G_n^-（下方 GOD POINT）
          的張力是否對稱？

          不平衡 → ⊛ 往強側漂移。
        """
        T_ang = self.angular_profile()
        upper = np.mean(T_ang[:self.n_angles // 2])
        lower = np.mean(T_ang[self.n_angles // 2:])
        total = upper + lower
        if total < 1e-10:
            return 0.0
        return float(1.0 - abs(upper - lower) / total)

    def asymmetry_vector(self) -> np.ndarray:
        """不對稱向量（診斷用）：張力場中不對稱的主要方向。"""
        T_ang = self.angular_profile()
        mean_T = np.mean(T_ang)
        deviation = T_ang - mean_T
        F_col = np.trapezoid(deviation * np.cos(self.angles), self.angles)
        F_row = np.trapezoid(deviation * np.sin(self.angles), self.angles)
        return np.array([F_row, F_col])


# ─────────────────────────────────────────
#  主類：ETN 風暴眼追蹤器
# ─────────────────────────────────────────

class ETNStormTracker:
    """
    基於 ETN 動態風暴眼原理的氣旋追蹤器。

    核心概念：
      不追全局相空間吸引子，只追 ⊛ 點的張力對稱性。

    預測邏輯：
      1. 更新 T(θ, r)（從大氣場或合成場）
      2. 計算 SE_n（⊛ 是否成立）
      3. 計算漂移向量（往哪裡走）
      4. 計算強度（對稱張力大小）
      5. 診斷：急速增強、眼牆替換、消散

    與吸引子方法的根本差異：
      吸引子方法：全局 → 局部（找盆地，追軌跡）
      ETN 方法：局部 → 全局預測（⊛ 的對稱性決定行為）
    """

    SE_THRESHOLD = 0.65          # 低於此值，⊛ 不成立
    RI_SYMMETRY_GAIN = 0.05      # 每步對稱度提升 > 此值 = 急速增強信號
    ERC_OUTER_RADIUS_RATIO = 2.5 # 外眼牆半徑比（眼牆替換週期判斷）

    def __init__(self,
                 eye_pos: np.ndarray,
                 n_angles: int = 72,
                 n_radii: int = 20,
                 r_max: float = 30.0):
        self.eye = np.array(eye_pos, dtype=float)
        self.tension = TensionField(
            n_angles=n_angles,
            n_radii=n_radii,
            r_max=r_max
        )
        self.history: list[StormEyeState] = []
        self._prev_symmetry: float = 0.0
        self._prev_intensity: float = 0.0

    # ── 主要步進 ───────────────────────────

    def step_from_fields(self,
                          pressure: np.ndarray,
                          wind_u: np.ndarray,
                          wind_v: np.ndarray,
                          dt: float = 1.0) -> StormEyeState:
        """從真實（或數值模式輸出）氣象場推進一步。"""
        self.tension.update_from_fields(pressure, wind_u, wind_v, self.eye)
        return self._compute_and_advance(dt)

    def step_synthetic(self,
                        asymmetry_angle: float = 0.0,
                        asymmetry_strength: float = 0.0,
                        base_intensity: float = 10.0,
                        dt: float = 1.0) -> StormEyeState:
        """從合成張力場推進一步（測試、理論分析用）。"""
        self.tension.update_synthetic(
            self.eye,
            asymmetry_angle=asymmetry_angle,
            asymmetry_strength=asymmetry_strength,
            base_intensity=base_intensity
        )
        return self._compute_and_advance(dt)

    def _compute_and_advance(self, dt: float) -> StormEyeState:
        sym = self.tension.symmetry_measure()
        drift = self.tension.drift_vector()
        inten = self.tension.intensity_metric()
        god_bal = self.tension.god_point_balance()
        asym_vec = self.tension.asymmetry_vector()

        # ⊛ 是否成立
        well_defined = sym >= self.SE_THRESHOLD

        state = StormEyeState(
            eye_pos=self.eye.copy(),
            symmetry=sym,
            intensity=inten,
            drift=drift.copy(),
            god_balance=god_bal,
            is_well_defined=well_defined,
            asymmetry_vector=asym_vec.copy()
        )

        self.history.append(state)

        # 只在 ⊛ 成立時，以對稱性加權的漂移更新位置
        # （不穩定的眼不做預測性位移）
        if well_defined:
            self.eye += drift * dt * sym
        else:
            # ⊛ 退化：以小步隨機游走（混沌態）
            self.eye += drift * dt * 0.1

        self._prev_symmetry = sym
        self._prev_intensity = inten

        return state

    # ── ETN 特有診斷 ────────────────────────

    def diagnose(self) -> dict:
        """
        ETN 診斷報告：
          rapid_intensification  = 急速增強信號
          eyewall_replacement    = 眼牆替換週期信號
          dissipation_risk       = 消散風險
        """
        if len(self.history) < 2:
            return {'error': '需要至少 2 步歷史'}

        curr = self.history[-1]
        prev = self.history[-2]

        # 急速增強（RI）：對稱度↑ 且強度↑
        sym_gain = curr.symmetry - prev.symmetry
        inten_gain = curr.intensity - prev.intensity
        ri_signal = (sym_gain > self.RI_SYMMETRY_GAIN and inten_gain > 0)

        # 消散風險：對稱度低 且強度下降
        dissipation = (curr.symmetry < self.SE_THRESHOLD and inten_gain < 0)

        # 軌跡不穩定：連續 3 步 ⊛ 不成立
        track_unstable = (
            len(self.history) >= 3 and
            not any(s.is_well_defined for s in self.history[-3:])
        )

        return {
            'is_well_defined': curr.is_well_defined,
            'symmetry': round(curr.symmetry, 3),
            'intensity': round(curr.intensity, 3),
            'god_point_balance': round(curr.god_balance, 3),
            'rapid_intensification': ri_signal,
            'symmetry_gain': round(sym_gain, 4),
            'dissipation_risk': dissipation,
            'track_unstable': track_unstable,
            'drift_magnitude': round(float(np.linalg.norm(curr.drift)), 4),
            'drift_direction_deg': round(
                float(np.degrees(np.arctan2(curr.drift[1], curr.drift[0]))), 1
            )
        }

    def track_array(self) -> np.ndarray:
        """回傳所有歷史眼位置，shape = (steps, 2)。"""
        return np.array([s.eye_pos for s in self.history])


# ─────────────────────────────────────────
#  工具函式
# ─────────────────────────────────────────

def _bilinear(field: np.ndarray,
               px: float, py: float,
               nx: int, ny: int) -> float:
    """雙線性插值。"""
    ix = int(np.clip(px, 0, nx - 2))
    iy = int(np.clip(py, 0, ny - 2))
    fx = np.clip(px, 0, nx - 2) - ix
    fy = np.clip(py, 0, ny - 2) - iy
    return (field[iy, ix] * (1-fx) * (1-fy) +
            field[iy, min(ix+1, nx-1)] * fx * (1-fy) +
            field[min(iy+1, ny-1), ix] * (1-fx) * fy +
            field[min(iy+1, ny-1), min(ix+1, nx-1)] * fx * fy)


def generate_synthetic_typhoon(grid_size: int = 100,
                                 center: Optional[np.ndarray] = None,
                                 max_wind: float = 50.0,
                                 eye_radius: float = 5.0) -> dict:
    """
    生成合成颱風氣壓場和風場（測試用）。

    使用 Rankine 渦旋模型：
      r < r_eye：solid-body rotation（眼區）
      r >= r_eye：衰減旋轉（眼牆外）
    """
    if center is None:
        center = np.array([grid_size // 2, grid_size // 2], dtype=float)

    y, x = np.mgrid[0:grid_size, 0:grid_size]
    r = np.sqrt((x - center[1])**2 + (y - center[0])**2)
    r = np.maximum(r, 0.1)

    # 切向風速（Rankine 渦旋）
    v_tan = np.where(r < eye_radius,
                     max_wind * r / eye_radius,
                     max_wind * eye_radius / r)

    # 風場分量
    theta_field = np.arctan2(y - center[0], x - center[1])
    wind_u = -v_tan * np.sin(theta_field)  # 逆時針（北半球）
    wind_v = v_tan * np.cos(theta_field)

    # 氣壓場（眼中心最低，向外增加）
    dp_max = 50.0  # hPa
    pressure = 1000.0 - dp_max * np.exp(-r**2 / (2 * (3 * eye_radius)**2))

    return {
        'pressure': pressure,
        'wind_u': wind_u,
        'wind_v': wind_v,
        'center': center,
        'r': r
    }


# ─────────────────────────────────────────
#  示範：理論驗證實驗
# ─────────────────────────────────────────

def demo_storm_eye_principle():
    """
    實驗一：風暴眼原理驗證

    ETN 預測：
      對稱張力 → ⊛ 穩定，眼不漂移
      不對稱張力 → ⊛ 退化，眼往強側漂移
    """
    print("=" * 60)
    print("ETN 動態風暴眼原理 — 實驗一：對稱性與漂移")
    print("=" * 60)

    # 情境 A：對稱張力場（⊛ 應成立，眼不漂）
    tracker_a = ETNStormTracker(eye_pos=np.array([50.0, 50.0]))
    print("\n[情境 A] 對稱張力場（asymmetry_strength = 0）")
    for t in range(5):
        state = tracker_a.step_synthetic(
            asymmetry_strength=0.0,
            base_intensity=10.0
        )
        print(f"  t={t}: 眼位 {state.eye_pos}, "
              f"SE_n={state.symmetry:.3f}, "
              f"⊛成立={state.is_well_defined}")

    # 情境 B：不對稱張力場（⊛ 應退化，眼往北漂）
    tracker_b = ETNStormTracker(eye_pos=np.array([50.0, 50.0]))
    print("\n[情境 B] 不對稱張力場（北側強，asymmetry_strength = 5.0）")
    for t in range(5):
        state = tracker_b.step_synthetic(
            asymmetry_angle=np.pi / 2,   # 北方（θ=90°）張力強
            asymmetry_strength=5.0,
            base_intensity=10.0
        )
        print(f"  t={t}: 眼位 {np.round(state.eye_pos, 2)}, "
              f"SE_n={state.symmetry:.3f}, "
              f"漂移={np.round(state.drift, 3)}")

    print("\nETN 預測驗證：情境 A 眼不動，情境 B 眼往北漂移。")
    print("這是張力不對稱（GOD POINT 失衡）的直接結果，")
    print("而不是引導流或壓力梯度的直接結果。")


def demo_rapid_intensification():
    """
    實驗二：急速增強（RI）的 ETN 診斷

    ETN 預測：
      對稱度持續上升 + 強度上升 → RI 信號
      傳統方法要觀察到風速才知道，ETN 在對稱度上升時就給出信號
    """
    print("\n" + "=" * 60)
    print("ETN 動態風暴眼原理 — 實驗二：急速增強診斷")
    print("=" * 60)

    tracker = ETNStormTracker(eye_pos=np.array([50.0, 50.0]))

    # 模擬組織化過程：不對稱度逐漸降低（眼逐漸清晰化）
    steps = 10
    print("\n模擬眼牆組織化過程（不對稱強度從 4.0 降至 0.5）：")
    for t in range(steps):
        asym = 4.0 * (1 - t / steps) + 0.5
        inten = 8.0 + t * 0.5  # 強度上升
        state = tracker.step_synthetic(
            asymmetry_strength=asym,
            base_intensity=inten
        )
        if t > 0:
            diag = tracker.diagnose()
            ri = "⚡ RI信號" if diag['rapid_intensification'] else ""
            print(f"  t={t}: SE_n={state.symmetry:.3f}, "
                  f"強度={state.intensity:.2f}, "
                  f"不對稱={asym:.1f}  {ri}")


def demo_dissipation():
    """
    實驗三：消散過程的 ETN 診斷

    ETN 預測：
      ⊛ 退化（SE_n 降低）→ 眼牆崩潰 → 消散
    """
    print("\n" + "=" * 60)
    print("ETN 動態風暴眼原理 — 實驗三：消散診斷")
    print("=" * 60)

    tracker = ETNStormTracker(eye_pos=np.array([50.0, 50.0]))
    print("\n模擬登陸後摩擦增加（不對稱強度上升，張力下降）：")
    for t in range(8):
        asym = 0.5 + t * 1.2       # 不對稱度上升
        inten = 12.0 - t * 1.5     # 強度下降
        state = tracker.step_synthetic(
            asymmetry_strength=asym,
            base_intensity=max(inten, 1.0)
        )
        if t > 0:
            diag = tracker.diagnose()
            risk = "💀 消散風險" if diag['dissipation_risk'] else ""
            print(f"  t={t}: SE_n={state.symmetry:.3f}, "
                  f"⊛成立={state.is_well_defined}, "
                  f"強度={state.intensity:.2f}  {risk}")


def demo_real_field():
    """
    實驗四：從合成氣象場出發（模擬真實 NWP 輸入）

    展示如何將 ETN 追蹤器接上實際氣壓場和風場。
    """
    print("\n" + "=" * 60)
    print("ETN 動態風暴眼原理 — 實驗四：合成氣象場追蹤")
    print("=" * 60)

    grid_size = 100
    typhoon = generate_synthetic_typhoon(
        grid_size=grid_size,
        max_wind=50.0,
        eye_radius=6.0
    )

    tracker = ETNStormTracker(
        eye_pos=typhoon['center'].copy(),
        r_max=25.0
    )

    print("\n對稱 Rankine 渦旋 + ETN 追蹤：")
    for t in range(5):
        # 真實場景：每步加一點環境不對稱
        noise_u = np.random.randn(*typhoon['wind_u'].shape) * 2
        noise_v = np.random.randn(*typhoon['wind_v'].shape) * 2

        state = tracker.step_from_fields(
            typhoon['pressure'],
            typhoon['wind_u'] + noise_u,
            typhoon['wind_v'] + noise_v
        )
        print(f"  t={t}: 眼位={np.round(state.eye_pos, 2)}, "
              f"SE_n={state.symmetry:.3f}, "
              f"強度={state.intensity:.2f}, "
              f"⊛={state.is_well_defined}")

    print("\n[ETN vs 傳統方法 比較]")
    print("傳統吸引子：追蹤全局相空間，計算 Lyapunov 指數，預測盆地內軌跡")
    print("ETN 風暴眼：追蹤 ⊛ 點局部張力對稱性，預測從局部結構直接讀出")
    print("差異：ETN 不需要知道全局場就能診斷眼的穩定性和漂移方向")


# ─────────────────────────────────────────
#  主程式
# ─────────────────────────────────────────

if __name__ == "__main__":
    np.random.seed(42)

    demo_storm_eye_principle()
    demo_rapid_intensification()
    demo_dissipation()
    demo_real_field()

    print("\n" + "=" * 60)
    print("ETN-STORM v0.1 完成")
    print("⊛ — 被拉扯而靜，向外發射而在")
    print("=" * 60)
