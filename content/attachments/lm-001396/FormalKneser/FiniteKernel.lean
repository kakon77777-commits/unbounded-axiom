import Std

/-!
  FiniteKernel.lean

  A kernel-checked finite formalization of the smallest stable-Kneser
  instances used by the research record.  It intentionally does not claim the
  asymptotic theorem.  The target is the exact finite base of the star-peeling
  route: the 3-stable triples on the 9-cycle form K₃, and the 10-cycle admits
  no 3-colouring of its 3-stable Kneser graph.
-/

namespace FormalKneser

structure Triple where
  a : Nat
  b : Nat
  c : Nat
  deriving Repr, DecidableEq, BEq

def allTriples (n : Nat) : List Triple :=
  (List.range n).flatMap fun a =>
    ((List.range n).drop (a + 1)).flatMap fun b =>
      ((List.range n).drop (b + 1)).map fun c => ⟨a, b, c⟩

def absDiff (a b : Nat) : Nat :=
  if a ≤ b then b - a else a - b

def cyclicDistance (n a b : Nat) : Nat :=
  let d := absDiff a b
  min d (n - d)

def atLeast (bound value : Nat) : Bool :=
  decide (bound ≤ value)

def stable3 (n : Nat) (t : Triple) : Bool :=
  atLeast 3 (cyclicDistance n t.a t.b) &&
  atLeast 3 (cyclicDistance n t.a t.c) &&
  atLeast 3 (cyclicDistance n t.b t.c)

def stableTriples (n : Nat) : List Triple :=
  (allTriples n).filter (stable3 n)

def members (t : Triple) : List Nat := [t.a, t.b, t.c]

def sharePoint (left right : Triple) : Bool :=
  (members left).any fun x =>
    (members right).any fun y => x == y

def disjoint (left right : Triple) : Bool :=
  !sharePoint left right

def allPairs {α : Type} (p : α → α → Bool) : List α → Bool
  | [] => true
  | x :: xs => xs.all (p x) && allPairs p xs

def intersecting (family : List Triple) : Bool :=
  allPairs sharePoint family

def containsPoint (x : Nat) (t : Triple) : Bool :=
  (members t).any fun y => x == y

def starAt (x : Nat) (family : List Triple) : Bool :=
  family.all (containsPoint x)

def isStar (n : Nat) (family : List Triple) : Bool :=
  (List.range n).any fun x => starAt x family

def powerset {α : Type} : List α → List (List α)
  | [] => [[]]
  | x :: xs =>
      let tail := powerset xs
      tail ++ tail.map fun subset => x :: subset

def everyIntersectingFamilyIsStar (n : Nat) : Bool :=
  (powerset (stableTriples n)).all fun family =>
    !intersecting family || isStar n family

def colorings (q : Nat) : Nat → List (List Nat)
  | 0 => [[]]
  | v + 1 =>
      (colorings q v).flatMap fun prior =>
        (List.range q).map fun color => color :: prior

def properForVertices (vertices : List Triple) (colors : List Nat) : Bool :=
  let labelled := List.zip vertices colors
  (colors.length == vertices.length) &&
  allPairs
    (fun left right => !(disjoint left.1 right.1 && left.2 == right.2))
    labelled

def properColorings (n q : Nat) : List (List Nat) :=
  let vertices := stableTriples n
  (colorings q vertices.length).filter (properForVertices vertices)

def compatibleWithAssigned
    (vertex : Triple)
    (color : Nat)
    (assignedVertices : List Triple)
    (assignedColors : List Nat) : Bool :=
  (List.zip assignedVertices assignedColors).all fun assigned =>
    !(disjoint vertex assigned.1 && color == assigned.2)

def searchColoring
    (remaining : List Triple)
    (assignedVertices : List Triple)
    (assignedColors : List Nat)
    (q : Nat) : Bool :=
  match remaining with
  | [] => true
  | vertex :: tail =>
      (List.range q).any fun color =>
        compatibleWithAssigned vertex color assignedVertices assignedColors &&
        searchColoring tail (assignedVertices ++ [vertex]) (assignedColors ++ [color]) q

def colorable (n q : Nat) : Bool :=
  searchColoring (stableTriples n) [] [] q

def starCoveredBy (n : Nat) (centres : List Nat) : Bool :=
  (stableTriples n).all fun triple =>
    centres.any fun centre => containsPoint centre triple

def anyStarCover (n centerCount : Nat) : Bool :=
  (colorings n centerCount).any (starCoveredBy n)

def expectedStableTriples9 : List Triple :=
  [⟨0, 3, 6⟩, ⟨1, 4, 7⟩, ⟨2, 5, 8⟩]

/-! ## Exact finite base -/

theorem stableTriples9_exact :
    stableTriples 9 = expectedStableTriples9 := by
  decide

theorem stableTriples9_pairwise_disjoint :
    allPairs disjoint (stableTriples 9) = true := by
  decide

theorem k3_has_no_two_coloring :
    properColorings 9 2 = [] := by
  decide

/-! ## First finite-core step -/

theorem stableTriples10_count :
    (stableTriples 10).length = 10 := by
  decide

set_option maxRecDepth 20000 in
theorem n10_every_intersecting_color_class_is_star :
    everyIntersectingFamilyIsStar 10 = true := by
  decide +kernel

set_option maxRecDepth 20000 in
theorem n10_has_no_three_coloring :
    colorable 10 3 = false := by
  decide +kernel

set_option maxRecDepth 20000 in
theorem n10_has_no_three_center_star_cover :
    anyStarCover 10 3 = false := by
  decide +kernel

end FormalKneser
