import FormalKneser.FiniteKernel

/-!
  Run this module after `lake build` to inspect the trusted axioms of the
  finite theorems.  All finite proofs in `FiniteKernel.lean` use `decide
  +kernel`, not native evaluation.
-/

#print axioms FormalKneser.stableTriples9_exact
#print axioms FormalKneser.k3_has_no_two_coloring
#print axioms FormalKneser.n10_every_intersecting_color_class_is_star
#print axioms FormalKneser.n10_has_no_three_center_star_cover
#print axioms FormalKneser.n10_has_no_three_coloring
