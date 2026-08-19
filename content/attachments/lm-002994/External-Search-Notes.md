# External Search Notes — EML-ONTO-CORE-06

A fresh external literature search was run immediately before drafting Paper 06.

Primary research papers / author manuscripts are used for technical comparison.

## 1. Closure operators on dcpos

France Dacar.
`Closure operators on dcpos`.
arXiv:1709.06170.

Relevance:
- studies closure/preclosure maps on dcpos;
- proves complete-lattice structure for closure operators in the stated setting;
- provides a precise mathematical example where closure has explicit domain/order structure.

Use:
- boundary comparison for typed Closure and fixed-point relations.
- not treated as a proof of the EveMissLab DCO Closure ontology.

## 2. Lattice of algebraic closure operators

Martha Lee Hollist Kilpack.
`The lattice of algebraic closure operators`.
arXiv:1411.6497.

Relevance:
- closure operators themselves form a structured lattice in the investigated setting.

Use:
- supports the methodological rule that closure must specify its mathematical domain and operator conditions.

## 3. egg / equality saturation

Max Willsey et al.
`egg: Fast and Extensible Equality Saturation`.
arXiv:2004.03082.

Relevance:
- e-graphs compactly represent congruence/equivalence classes over many expressions;
- equality-saturation systems commonly require domain-specific analyses and extraction choices.

Use:
- comparison for CRL equivalence clusters versus selection/extraction.

## 4. Rewrite rule inference using equality saturation

Chandrakana Nandi et al.
`Rewrite Rule Inference Using Equality Saturation`.
arXiv:2108.10436.

Relevance:
- large rewrite spaces contain redundancy;
- equality saturation can compactly represent very large enumerated term spaces.

Use:
- comparison for branch explosion and certified-equivalence compression.

## 5. Confluence / normal-form properties

Takahito Aoto, Yoshihito Toyama.
`Automated Proofs of Unique Normal Forms w.r.t. Conversion for Term Rewriting Systems`.
arXiv:1807.00940.

Bertram Felgenhauer.
`Deciding Confluence and Normal Form Properties of Ground Term Rewrite Systems Efficiently`.
arXiv:1710.10991.

Cyrille Chenavier.
`Reduction Operators and Completion of Rewriting Systems`.
arXiv:1605.00174.

Relevance:
- confluence, unique normal forms, and completion are distinct properties;
- legal rewrite paths do not automatically imply a unique terminal representation.

Use:
- comparison for convergence/fixed-point/closure separation.

## 6. Sheaf-based local/global alignment

Gabriele D'Acunto et al.
`Sheaf-Based Federated Representation Learning`.
arXiv:2608.10016.

Relevance:
- heterogeneous local representations are aligned with learnable restriction maps;
- global consistency is treated through local alignment/gluing structure rather than assuming one shared global latent space.

Use:
- recent comparison for typed local-to-global gluing.

## 7. Equivalence Hypergraphs

Dan R. Ghica, Chris Barrett, Aleksei Tiurin.
`Equivalence Hypergraphs: E-Graphs for Monoidal Theories`.
arXiv:2406.15882.

Relevance:
- extends equivalence-graph ideas beyond ordinary term settings using categorical/monoidal structure.

Use:
- comparison for higher-order equivalence representation.

## Boundary rule

External closure operators, term-rewriting systems, e-graphs and sheaves are comparison structures. They do not prove:
- DCO Closure axioms;
- CRL derivability from Closure;
- CRE minimality or universality;
- an absolute global-closure theorem for reality.
