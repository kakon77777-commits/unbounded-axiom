import Mathlib

open Metric

/-!
# Universal Circular Container

Formal skeleton for the exact radius `L/2`.
-/

theorem path_mem_midpoint_closedBall
    {X : Type*} [PseudoMetricSpace X]
    (γ : ℝ → X) (L : ℝ)
    (hL : 0 ≤ L)
    (hγ : LipschitzWith 1 γ)
    {t : ℝ} (ht0 : 0 ≤ t) (htL : t ≤ L) :
    γ t ∈ closedBall (γ (L / 2)) (L / 2) := by
  rw [mem_closedBall]
  calc
    dist (γ t) (γ (L / 2))
        ≤ (1 : ℝ) * dist t (L / 2) := hγ.dist_le_mul t (L / 2)
    _ = |t - L / 2| := by
      rw [one_mul, Real.dist_eq]
    _ ≤ L / 2 := by
      rw [abs_le]
      constructor <;> linarith

theorem two_points_force_radius
    {X : Type*} [PseudoMetricSpace X]
    {p q c : X} {R L : ℝ}
    (hp : p ∈ closedBall c R)
    (hq : q ∈ closedBall c R)
    (hL : dist p q = L) :
    L / 2 ≤ R := by
  rw [mem_closedBall] at hp hq
  have htri : dist p q ≤ dist p c + dist c q :=
    dist_triangle p c q
  rw [hL, dist_comm c q] at htri
  linarith
