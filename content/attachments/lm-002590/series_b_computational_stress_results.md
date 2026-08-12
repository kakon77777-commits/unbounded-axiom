# Series B computational stress test

## Test 1 — local order defect
delta(A,B;x) = ||A(Bx)-B(Ax)|| = 1.38924439894
A(Bx) = [ 0.2 -0.5]
B(Ax) = [-0.5 -1.7]
noncommutative? True

## Test 2 — adjacent-swap propagation bound
final path difference = 1.83806963959
||S||_2 * delta       = 2.80979707034
bound holds? True

random cases = 2000, violations = 0, max(lhs/rhs) = 0.999296324388

## Test 3 — finite Z2 gluing obstruction
all coboundaries = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
c=(1,1,1) is coboundary? False
c=(1,1,0) is coboundary? True
loop parity of (1,1,1) = 1

## Test 4 — two kinds of non-globality
parity-model global sections = []
global section exists there? False
projection observer preimages = {0: [(0, 0), (0, 1)], 1: [(1, 0), (1, 1)]}
observer map injective? False

## Test 5 — closed-loop holonomy
K = ABA^-1B^-1 =
[[ 3. -1.]
 [ 1.  0.]]
||K-I||_2 = 2.61803398875
K v = [3. 1.], v = [1. 0.]
relational memory nontrivial? True

## Test 6 — holonomy without breaking an invariant
H = 90-degree rotation, ||H-I||_2 = 1.41421356237
v -> Hv: [3. 4.] -> [-4.  3.]
Q(v)=||v||^2: before=25, after=25
state changed? True
Q conserved? True

## Test 7 — observer covariance and relative holonomy
||F T_O - T_P F||_2 = 0
trace(H_O), trace(H_P) = 1.51672375198, 1.51672375198
eigenvalues(H_O) = [0.75836188-0.65183377j 0.75836188+0.65183377j]
eigenvalues(H_P) = [0.75836188-0.65183377j 0.75836188+0.65183377j]
||R_OP-I||_2 = 1.42007017897e-16

after perturbing P's transport: defect = 0.0005

## Test 8 — coarse-graining can hide relational memory
H_hidden != I? True
||F H_hidden - F||_2 = 0
holonomy invisible to projected observer? True

## Test 9 — observer-network triple coherence
all three pairwise maps invertible? True
K_123 = F31 F23 F12 =
[[ 0.5       -0.8660254]
 [ 0.8660254  0.5      ]]
||K_123-I||_2 = 1
pairwise maps exist but network closes? False

coherent triangle built from global frames: ||K-I||_2 = 2.39159492507e-16

## Test 10 — observer-covariant conservation
Q_O before/after = 2.18, 2.18
Q_P before/after = 2.18, 2.18
cross-observer compatibility |Q_P(Fv)-Q_O(v)| = 0
conserved in O? True
conserved in P? True

## Test 11 — strict conservation vs balance law
Q0=10.0, Q1=7.0, strict defect ΔQ=-3.0
accounted flux/source term Φ=-3.0
balance residual ΔQ-Φ = 0.0
strict conservation? False
balance law satisfied? True

## Summary
- T1_noncommutative_defect_detected: PASS
- T2_lipschitz_bound: PASS
- T3_z2_obstruction: PASS
- T4_nonexistence_vs_inaccessibility: PASS
- T5_nontrivial_holonomy: PASS
- T6_invariant_survives_holonomy: PASS
- T7_exact_covariance: PASS
- T8_hidden_holonomy: PASS
- T9_network_coherence_test: PASS
- T10_observer_covariant_conservation: PASS
- T11_balance_not_strict: PASS

**Passed 11/11 checks.**