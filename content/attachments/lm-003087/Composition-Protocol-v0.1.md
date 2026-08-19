# COMPOSITION_PROTOCOL — GCORF-02 v0.1

候選組合進入 canonical library 前：

1. TypeCheck
2. DomainCheck
3. LicenseCheck
4. InterfaceCheck
5. ExecutionTest
6. FailureAudit
7. SpectrumMeasurement
8. CostAudit
9. ReproducibilityTest
10. Admit / Provisional / Reject / Undefined

新增 atomic operator 前另需判斷：

- NewAtomic?
- ExistingOperator + NewImplementationMode?
- ExistingCluster?
- CompositeOnly?

Coupling 產生的新 operator candidate 必須重新回到 GCORF-01 的 CandidateOperator / Atomicization pipeline。
