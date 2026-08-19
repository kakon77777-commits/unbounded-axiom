# VWDC-04 Handoff — Active Branch Design, Dependence-Aware World Experimentation, and Evidence Value

## Starting state

VWDC-03 establishes:

$$
n_{\mathrm{eff}}
=
\frac{
n
}{
1+(n-1)\rho
}
$$

for equicorrelated replication.

For paired counterfactual branches:

$$
\operatorname{Var}(Y_1-Y_0)
=
2\sigma^2(1-\rho).
$$

It distinguishes:

- REPLICATION;
- PAIRED_COUNTERFACTUAL;
- ROBUSTNESS_TEST;
- COUNTEREXAMPLE_SEARCH;
- SENSITIVITY_ANALYSIS;
- TRANSPORT_VALIDATION.

## Objective

Choose which branch/experiment/validation action deserves computation next.

## Main questions

1. When is another independent seed valuable?
2. When is an independent model/backend more valuable?
3. When should branches share noise?
4. How should covariance affect value of information?
5. How should counterexample probability be priced?
6. When is external validation more valuable than more simulation?
7. What is branch-design regret versus an oracle experimental policy?
8. How should the WDC Governor balance coverage, falsification, independence, and transport strength?

## Desired form

$$
\boxed{
\text{current claim}
+
\text{branch dependence model}
+
\text{uncertainty}
+
\text{cost}
+
\text{transport debt}
\Longrightarrow
\text{fork}
\vee
\text{change backend}
\vee
\text{couple noise}
\vee
\text{validate externally}
\vee
\text{stop}.
}
$$

## Prohibitions

- Do not optimize raw branch count.
- Do not use one dependence structure for all evidence purposes.
- Do not treat model diversity as proven independence.
- Do not spend unlimited simulation compute when transport error dominates.
