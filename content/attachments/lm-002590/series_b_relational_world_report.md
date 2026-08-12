# Series B Relational World Simulator — Report

## Hidden world
- nodes on cycle: 5
- state dimension: 3
- loop holonomy strength ||H-I||₂ = 0.935954611913
- consecutive order defects = [0.18539877601106014, 0.31164308541459373, 0.135965795169183, 0.08936670445960243, 0.14967684743214493]
- Q(v)=||v||² max residual across 1000 random states = 3.5527136788e-15

## Observer covariance
- observers: ['O0', 'O1', 'O2', 'O3']
- max exact covariance defect = 6.66901527567e-16
- deliberately blind O2 projection: ||P H - P|| = 4.99600361081e-16
- full O0 visibility: ||H-I|| = 0.935954611913

## Observer network coherence
- exact triangle ||K-I|| = 1.3766598184e-16
- injected bad triangle ||K-I|| = 0.00167154075085

## H1-style observer nerve
- nontrivial cycle c=(1, 0, 0, 0): coboundary? False
- trivial cycle c=(1, 1, 0, 0): coboundary? True

## Bad local observer model
Underlying hidden world remains orthogonal and Q-conserving.
- bad observer covariance defect = 0.000905538513814
- same observer's quadratic conservation residual = 0.00128554821725

This is important: a local observer model can report apparent non-conservation even when the hidden/global transport used to generate the world still exactly conserves Q.

## Strict vs balance
- Q before = 5.69
- Q after  = 4.25
- strict change = -1.44
- accounted exchange Phi = -1.44
- balance residual = 0

## Monte Carlo stress (200 random relational worlds)
- max exact observer covariance defect = 7.59541496523e-16
- max observer-frame Q residual = 1.54534373607e-15
- max holonomy spectrum difference under frame conjugacy = 2.23772604566e-15

## Verdict
Passed 17/17 high-level checks.
