# Symbol Table — EML-ONTO-CORE-04 v0.1

| Symbol | Meaning | Note |
|---|---|---|
| $\mathcal X$ | source state space | typed domain |
| $\mathcal Y$ | transformed representation space | target |
| $\mathcal J$ | typed information query family | canonical relevance contract |
| $j_\alpha$ | information query/invariant | $X\to Z_\alpha$ |
| $\mathbf I_{\mathcal J}(X)$ | typed information profile | not necessarily numeric vector |
| $T$ | transformation | compression/projection/transport/etc. |
| $\widehat j$ | query decoder | recovers $j$ from $T(x)$ |
| $F_y^T$ | transformation fiber | $T^{-1}(y)$ |
| $P_j(T)$ | exact preservation indicator | 0/1 |
| $\mathbf P_{\mathcal J}(T)$ | preservation profile | typed exact status |
| $D_j^\ast(T)$ | optimal expected reconstruction distortion | requires distribution/metric |
| $D_{j,\infty}^\ast(T)$ | optimal worst-case distortion | distribution-free variant |
| $\boldsymbol\Delta_{\mathcal J}(T)$ | typed distortion spectrum | canonical quantitative loss object |
| $R$ | restoration map | must state allowed inputs |
| $\mathcal S_{\mathrm{side}}$ | side information | provenance/key/history/etc. |
| $\equiv_{\mathcal J}$ | task-relative equivalence | same answers for all $j\in J$ |
| $q_{\mathcal J}$ | quotient projection | to $X/\equiv_J$ |
| $\mathfrak C_I(T)$ | Information Preservation Contract | J, distortion, side info, tolerance, context |
| $\mathrm{TICDR}(T;q)$ | full transformation information status | canonical Paper 04 object |
