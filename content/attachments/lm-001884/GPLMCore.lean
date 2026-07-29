import Mathlib

/-!
# GPLM Core

Formal core of the non-axiomatic reconstruction.

The primary theorem is proved in additive logarithmic coordinates:
the minimax center of `[A,B]` is `(A+B)/2`.
-/

theorem max_gap_ge_half
    (A B X : ℝ) (hAB : A ≤ B) :
    (B - A) / 2 ≤ max (X - A) (B - X) := by
  by_cases h : X - A ≤ B - X
  · rw [max_eq_right h]
    linarith
  · have h' : B - X ≤ X - A := le_of_not_ge h
    rw [max_eq_left h']
    linarith

theorem max_gap_eq_half_iff
    (A B X : ℝ) (hAB : A ≤ B) :
    max (X - A) (B - X) = (B - A) / 2 ↔
      X = (A + B) / 2 := by
  constructor
  · intro hEq
    have h₁ : X - A ≤ (B - A) / 2 := by
      calc
        X - A ≤ max (X - A) (B - X) := le_max_left _ _
        _ = (B - A) / 2 := hEq
    have h₂ : B - X ≤ (B - A) / 2 := by
      calc
        B - X ≤ max (X - A) (B - X) := le_max_right _ _
        _ = (B - A) / 2 := hEq
    linarith
  · intro hX
    subst X
    have hleft : (A + B) / 2 - A = (B - A) / 2 := by ring
    have hright : B - (A + B) / 2 = (B - A) / 2 := by ring
    rw [hleft, hright, max_self]

theorem geometric_center_positive
    (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    0 < Real.sqrt (a * b) := by
  exact Real.sqrt_pos.2 (mul_pos ha hb)

theorem geometric_center_sq
    (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (Real.sqrt (a * b)) ^ 2 = a * b := by
  exact Real.sq_sqrt (mul_nonneg ha hb)

theorem geometric_center_balances
    (a b : ℝ) (ha : 0 < a) (hb : 0 < b) :
    let x := Real.sqrt (a * b)
    x / a = b / x := by
  dsimp
  have hx : Real.sqrt (a * b) ≠ 0 :=
    ne_of_gt (Real.sqrt_pos.2 (mul_pos ha hb))
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hs : (Real.sqrt (a * b)) ^ 2 = a * b :=
    Real.sq_sqrt (le_of_lt (mul_pos ha hb))
  field_simp
  nlinarith
