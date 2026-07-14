(*
   KneserFiniteKernel.v

   A Coq/Rocq port of the finite Lean kernel.  It uses only the standard
   list, boolean, and natural-number libraries.  The executable claims are
   deliberately finite: K_3 at n = 9, and the n = 10 finite-core check.
*)

From Coq Require Import List Bool Arith.PeanoNat.
Import ListNotations.

Record triple : Type := {
  ta : nat;
  tb : nat;
  tc : nat
}.

Definition allTriples (n : nat) : list triple :=
  flat_map
    (fun a =>
      flat_map
        (fun b =>
          map
            (fun c => {| ta := a; tb := b; tc := c |})
            (skipn (S b) (seq 0 n)))
        (skipn (S a) (seq 0 n)))
    (seq 0 n).

Definition absDiff (a b : nat) : nat :=
  if a <=? b then b - a else a - b.

Definition cyclicDistance (n a b : nat) : nat :=
  let d := absDiff a b in Nat.min d (n - d).

Definition atLeast (bound value : nat) : bool := bound <=? value.

Definition stable3 (n : nat) (t : triple) : bool :=
  atLeast 3 (cyclicDistance n (ta t) (tb t)) &&
  atLeast 3 (cyclicDistance n (ta t) (tc t)) &&
  atLeast 3 (cyclicDistance n (tb t) (tc t)).

Definition stableTriples (n : nat) : list triple :=
  filter (stable3 n) (allTriples n).

Definition members (t : triple) : list nat := [ta t; tb t; tc t].

Definition sharePoint (left right : triple) : bool :=
  existsb
    (fun x => existsb (Nat.eqb x) (members right))
    (members left).

Definition disjoint (left right : triple) : bool := negb (sharePoint left right).

Fixpoint allPairs {A : Type} (p : A -> A -> bool) (xs : list A) : bool :=
  match xs with
  | [] => true
  | x :: rest => forallb (p x) rest && allPairs p rest
  end.

Definition intersecting (family : list triple) : bool := allPairs sharePoint family.

Definition containsPoint (x : nat) (t : triple) : bool :=
  existsb (Nat.eqb x) (members t).

Definition starAt (x : nat) (family : list triple) : bool :=
  forallb (containsPoint x) family.

Definition isStar (n : nat) (family : list triple) : bool :=
  existsb (fun x => starAt x family) (seq 0 n).

Fixpoint powerset {A : Type} (xs : list A) : list (list A) :=
  match xs with
  | [] => [[]]
  | x :: rest =>
      let tail := powerset rest in
      tail ++ map (fun subset => x :: subset) tail
  end.

Definition everyIntersectingFamilyIsStar (n : nat) : bool :=
  forallb
    (fun family => negb (intersecting family) || isStar n family)
    (powerset (stableTriples n)).

Fixpoint colorings (q vertices : nat) : list (list nat) :=
  match vertices with
  | 0 => [[]]
  | S priorCount =>
      flat_map
        (fun prior => map (fun color => color :: prior) (seq 0 q))
        (colorings q priorCount)
  end.

Definition properForVertices (vertices : list triple) (colors : list nat) : bool :=
  let labelled := combine vertices colors in
  (length colors =? length vertices) &&
  allPairs
    (fun left right =>
      negb (disjoint (fst left) (fst right) && Nat.eqb (snd left) (snd right)))
    labelled.

Definition properColorings (n q : nat) : list (list nat) :=
  let vertices := stableTriples n in
  filter (properForVertices vertices) (colorings q (length vertices)).

Definition expectedStableTriples9 : list triple :=
  [{| ta := 0; tb := 3; tc := 6 |};
   {| ta := 1; tb := 4; tc := 7 |};
   {| ta := 2; tb := 5; tc := 8 |}].

Example stableTriples9_exact :
  stableTriples 9 = expectedStableTriples9.
Proof. vm_compute. reflexivity. Qed.

Example stableTriples9_pairwise_disjoint :
  allPairs disjoint (stableTriples 9) = true.
Proof. vm_compute. reflexivity. Qed.

Example k3_has_no_two_coloring :
  properColorings 9 2 = [].
Proof. vm_compute. reflexivity. Qed.

Example stableTriples10_count :
  length (stableTriples 10) = 10.
Proof. vm_compute. reflexivity. Qed.

Example n10_every_intersecting_color_class_is_star :
  everyIntersectingFamilyIsStar 10 = true.
Proof. vm_compute. reflexivity. Qed.

Example n10_has_no_three_coloring :
  properColorings 10 3 = [].
Proof. vm_compute. reflexivity. Qed.
