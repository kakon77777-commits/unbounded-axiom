# CCM Foundational Theory — Literature Positioning

Version: v1.0  
Primary-source verification date: 2026-08-15

## R1 — Experimental Mathematics

David H. Bailey and Jonathan M. Borwein.  
“Experimental Mathematics: Examples, Methods and Implications.”  
Notices of the American Mathematical Society, 52(5), 502--514, 2005.

Relevance to CCM: computation as an active research instrument rather than only a final verification device.

## R2 — Algorithm Selection

John R. Rice.  
“The Algorithm Selection Problem.”  
Advances in Computers, Volume 15, 65--118, 1976.

Relevance to CCM: feature-based selection among algorithms under a performance criterion.

## R3 — Algorithm Portfolios

Lin Xu, Frank Hutter, Holger H. Hoos, Kevin Leyton-Brown.  
“SATzilla: Portfolio-Based Algorithm Selection for SAT.”  
Journal of Artificial Intelligence Research, 32, 565--606, 2008.  
DOI: 10.1613/JAIR.2490.

Relevance to CCM: instance-aware portfolio routing among heterogeneous solvers.

## R4 — Online Algorithm Selection

Matteo Gagliolo and Jürgen Schmidhuber.  
“Algorithm Selection as a Bandit Problem with Unbounded Losses.”  
arXiv:0807.1494, 2008.

Relevance to CCM: online selection and exploration/exploitation when algorithm performance must be learned sequentially.

## R5 — Nonstationarity and Dynamic Regret

Wang Chi Cheung, David Simchi-Levi, Ruihao Zhu.  
“Hedging the Drift: Learning to Optimize under Non-Stationarity.”  
arXiv:1903.01461, 2019.

Relevance to CCM: dynamic regret and adaptation in changing environments.

## R6 — Proof Systems

Stephen A. Cook and Robert A. Reckhow.  
“The Relative Efficiency of Propositional Proof Systems.”  
The Journal of Symbolic Logic, 44(1), 36--50, 1979.  
DOI: 10.2307/2273702.

Relevance to CCM: proof languages as computational objects, proof verification, simulation, and efficiency.

## R7 — Foundational Proof Certificates

Zakaria Chihani, Dale Miller, Fabien Renaud.  
“Foundational Proof Certificates in First-Order Logic.”  
CADE-24, Lecture Notes in Computer Science 7898, 162--177, 2013.

Relevance to CCM: separation of proof evidence generation from a small general proof-checking architecture.

## R8 — Counterexample-Guided Refinement

Edmund Clarke, Orna Grumberg, Somesh Jha, Yuan Lu, Helmut Veith.  
“Counterexample-Guided Abstraction Refinement.”  
CAV 2000, Lecture Notes in Computer Science 1855, 154--169, 2000.  
DOI: 10.1007/10722167_15.

Relevance to CCM: failed abstractions and counterexamples become refinement information rather than terminal failure.

## R9 — SOS Certificates

Pablo A. Parrilo.  
“Semidefinite Programming Relaxations for Semialgebraic Problems.”  
Mathematical Programming, Series B, 96, 293--320, 2003.  
DOI: 10.1007/s10107-003-0387-5.

Relevance to CCM: checkable certificate languages for nonnegativity, semidefinite representations, and the distinction between a sufficient certificate class and the full truth domain.

## Positioning Statement

The foundational CCM claim is not that the components above are individually new.

CCM proposes to use the following joint object as the mathematical-methodology unit:

$$
\boxed{
\text{representation}
+
\text{certificate language}
+
\text{coverage domain}
+
\text{barrier}
+
\text{routing policy}
+
\text{cost state}
+
\text{history}.
}
$$

The resulting framework is intended as a research-control theory for mathematics rather than as a new single proof calculus.
