# SOURCE_NOTES — Global Computation Methodology Series v0.1

日期：2026-08-23

本文件只記錄本輪正式撰寫前進行的 fresh literature search，用於區分：
1. 使用者既有理論與本輪統合形式；
2. 既有外部研究；
3. 本系列的新組合與重新定位。

## A. Heterogeneous Computing / Runtime Scheduling

- Fang, J., Huang, C., Tang, T., & Wang, Z. **Parallel Programming Models for Heterogeneous Many-Cores: A Survey** (2020).
- **Towards an Optimized Heterogeneous Distributed Task Scheduler in OpenMP Cluster** (SC24-W / IEEE, 2024).
- Boné, A. et al. **A task-based data-flow methodology for programming heterogeneous systems with multiple accelerator APIs** (2026).
- De Matteis, T., Gianinazzi, L., de Fine Licht, J., & Hoefler, T. **Streaming Task Graph Scheduling for Dataflow Architectures** (2023).
- **CaRCS: Joint Optimization of Computing-Aware Routing and Collaborative Scheduling in Computing Power Networks** (IEEE Network, 2025).
- **Cloud-Edge System for Scheduling Unpredictable LLM Requests With Combinatorial Bandit** (IEEE TSC, 2025).

## B. Hybrid / Continuous–Discrete Systems

- Taha, W. M., Taha, A.-E. M., & Thunberg, J. **Hybrid Systems** (2020).
- Stauner, T. **Properties of Hybrid Systems—A Computer Science Perspective** (2004).
- Goncharov, S., Neves, R., & Proença, J. **Implementing Hybrid Semantics: From Functional to Imperative** (2020).

## C. Partial Observability / Observer Projection

- Atkinson, E. & Carbin, M. **Programming and Reasoning with Partial Observability** (2021).
- Norman, G., Parker, D., & Zou, X. **Verification and control of partially observable probabilistic systems** (2017).
- Zhang, R., Cai, K., & Wonham, W. M. **Supervisor Localization of Discrete-Event Systems under Partial Observation** (2015).
- **A survey on compositional algorithms for verification and synthesis in supervisory control** (2023).

## D. Materialization / Adaptive Resolution / Active Support

- Liang, X., Elmore, A. J., & Krishnan, S. **Opportunistic View Materialization with Deep Reinforcement Learning** (2019).
- Xia, L. et al. **Story of Your Lazy Function's Life: A Bidirectional Demand Semantics for Mechanized Cost Analysis of Lazy Programs** (2024).
- Adaptive mesh refinement / adaptive wavelet collocation literature.
- **From adaptive resolution to molecular dynamics of open systems** (2021).
- Chen, D., Wang, S., & Guo, Q. **ACGraph: An Efficient Asynchronous Out-of-Core Graph Processing Framework** (2025).
- Zhao, C. et al. **Kaleido: An Efficient Out-of-core Graph Mining System on A Single Machine** (2019).

## E. Concurrency / History / Partial-Order Semantics

- Mazurkiewicz trace theory.
- Diekert, V. **Combinatorics on Traces** (1990).
- **Optimal Dynamic Partial Order Reduction with Observers** (TACAS, 2018).
- **Quasi-Optimal Partial Order Reduction** (CAV, 2018).
- **Parsimonious Optimal Dynamic Partial Order Reduction** (2024).
- **Extracting safe thread schedules from incomplete model checking results** (2020).

## F. 本系列與外部研究的分界

本系列不主張：
- 異質硬體調度由本系列首創；
- continuous/discrete hybrid semantics 由本系列首創；
- partial observability / projection 由本系列首創；
- adaptive resolution、lazy evaluation、materialized views 由本系列首創；
- partial-order traces / DPOR 由本系列首創。

本系列的主要新組合與重新定位是：

$$
\boxed{
\text{Computational Taxonomy}
\to
\text{Addressable Configuration Space}
\to
\text{Dynamic Runtime Routing}
\to
\text{Global Computation Methodology}
}
$$

以及把：
- computational form；
- transition law；
- domain；
- resolution / materialization；
- observer projection；
- active support；
- history / provenance

放進同一個可路由、可組合的 Runtime 方法論框架。
