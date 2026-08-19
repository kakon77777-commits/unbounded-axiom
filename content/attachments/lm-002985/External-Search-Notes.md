# External Search Notes — EML-ONTO-CORE-04

A fresh literature search was run immediately before drafting Paper 04.

Technical comparison relies on primary papers / author manuscripts.

## 1. Information Bottleneck

Naftali Tishby, Fernando C. Pereira, William Bialek.
`The Information Bottleneck Method`.
arXiv:physics/0004057.

Key comparison:
- compress source representation while retaining relevant information about a target;
- relevance is explicit rather than identical to preserving all source detail.

Use in TICDR:
- precedent for task-relative information preservation.

## 2. Invertibility and full-detail preservation

Yang Liu et al.
`Are Deep Neural Architectures Losing Information? Invertibility Is Indispensable`.
arXiv:2009.03173.

Key comparison:
- studies the condition for preserving full input information;
- emphasizes invertibility when full-detail restoration is required.

Use:
- comparison for exact state restoration versus task-relative sufficiency.

## 3. Semantic rate-distortion with side information

Tao Guo et al.
`Semantic Compression with Side Information: A Rate-Distortion Perspective`.
arXiv:2208.06094.

Use:
- precedent for explicit distortion constraints;
- source reconstruction and semantic inference can be different objectives;
- side information changes the achievable reconstruction problem.

## 4. Semantic-preserved communication

Tianxiao Han et al.
`Semantic-preserved Communication System for Highly Efficient Speech Transmission`.
arXiv:2205.12727.

Use:
- direct engineering example where semantic-relevant information can be transmitted separately from additional information needed for source reconstruction.

## 5. Rate-Distortion-Perception

Jingxuan Chai et al.
`Rate-Distortion-Perception Theory for Semantic Communication`.
arXiv:2312.05437.

Use:
- reconstruction quality depends on which distortion/perception constraints are declared.

## 6. Sufficient-statistic reduction of Information Bottleneck

Joss Armstrong.
`A Sufficient-Statistic Reduction of the Information Bottleneck to a Low-Dimensional Problem`.
arXiv:2604.26744.

Use:
- recent formal comparison point for loss-free reduction when target dependence factors through a sufficient statistic.

## 7. Deductive closure fidelity

Jianfeng Xu.
`Semantic Rate-Distortion Theory: Deductive Compression and Closure Fidelity`.
arXiv:2604.11204.

Use:
- recent example of defining fidelity by preservation of deductive closure rather than verbatim source;
- relevant to later Closure/CRL work.

Boundary:
- treated as a recent research comparison, not as an established universal standard.

## 8. Landauer / reversible computation

Charles H. Bennett.
`Notes on Landauer's principle, Reversible Computation and Maxwell's Demon`.
arXiv:physics/0210005.

Use:
- boundary comparison between logical irreversibility and physical thermodynamic claims.

## Canonical boundary

No external paper is treated as proof that the EveMissLab typed ontology is universal. The external literature is used to constrain terminology and identify established mathematical precedents.
