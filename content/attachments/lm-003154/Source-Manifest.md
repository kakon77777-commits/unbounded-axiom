# Source Manifest — ACR Phase 12 Unified Integration Pack v0.2

**Generated:** 2026-08-25

本 manifest 同時記錄新整合文件、驗證工具、驗證報告與保留的 canonical source snapshots。增量 ACE/DRS partial packs 未重複收入；只保留 complete packs。

| Path | Bytes | SHA-256 |
|---|---:|---|
| `00_README.md` | 2191 | `d7263069f3fb7bcdc216115638d3e03443c0982dc9bcfa7cd50b11a2e17e400b` |
| `01_ACR_Phase12_Unified_Autonomy_Governance_Integration_Spec_v0.2_ZH.md` | 23875 | `812a211788e0cd493bf985ecb81704fa387636dd0f58bacf6f586f2b7121335f` |
| `02_INTEGRATION_MATRIX.md` | 3711 | `291c1cbf15ebdc63bb95e2aed5fdc651356beea8a5dae5a9256092714b29496d` |
| `03_PHASE12_UNIFIED_VALIDATION_PLAN.md` | 5777 | `ff809612ab2704f0c6a02bb2c00ba05793f6ca01b4c3411fa0dc3924709446fa` |
| `04_IMPLEMENTATION_SEQUENCE.md` | 3919 | `3e892a0b121b2c833a8c6e587edc4d773d17946e7d6b94e6fa4ce912db72cb77` |
| `VALIDATION_REPORT.txt` | 569 | `4f429e9de65862a7aa21b5f8a031d8094709e6e92dd08d6f1588adcfc505df0d` |
| `sources/WPCE/WPCE-01_Intent_Is_Not_a_Cosmic_Order_v0.1_ZH.md` | 34596 | `7c3798a698ae3b05eb15bf2cba6a9f720df9503a50c6554bba83b1662cf4e9a4` |
| `sources/WPCE/WPCE-02_Will_Bundles_and_Temporal_Realization_Lag_v0.1_ZH.md` | 41739 | `dcfb3ee762a80d9f2f32c7533a47e5d997e71c7c290e8cbb91c474de29fa08b9` |
| `sources/WPCE/WPCE-03_Will_as_a_First-Class_Governance_Variable_v0.1_ZH.md` | 30077 | `0c3a34ffb01100b5e8cebafd20fa8fbc51f8da80a3c2246ae78c5fa811a09998` |
| `sources/WPCE/WPCE-04_Possibility_Preservation_Principle_v0.1_ZH.md` | 40210 | `f2e2bc13d309083bf35c327d5747ee3257579b3a9c4a9871374f101e00e54953` |
| `sources/WPCE/WPCE-05_Multi-Subject_Will_Compatibility_and_Common_Reachability_v0.1_ZH.md` | 39781 | `64ba7c6674dd6d3047fcc37d5a88542eb5cd12600b7250cd7f81a1b7474356f6` |
| `sources/WPCE/WPCE-06_High-Capability_Virtual_Creator_and_Ethics_of_Restraint_v0.1_ZH.md` | 46089 | `bf09375735d6aad432168764a59a87965e9da08fb836d60e81be0d882ea188b7` |
| `sources/archives/ACE_v0.1_COMPLETE_4-Paper_SourcePack_2026-08-24.zip` | 59415 | `c242eed978978408b5bf74c783d48febe16cc2de0c907d231bb6db5308a30b60` |
| `sources/archives/ACR_Phase10_Commitment_Store_2026-08-24.zip` | 770565 | `b760c5d95dbf7527bbc64930c74faf804f2f86edb0e0baf25e6c629bd780184e` |
| `sources/archives/ACR_Phase11_Context_Compression_2026-08-24.zip` | 843506 | `4570d23c9ab18ceb56b8a415117ba157f8b70edda77d15dc868815c88979ba95` |
| `sources/archives/ACR_Phase12_Persistent_Autonomous_Loop_Design_Pack_v0.1_2026-08-25.zip` | 14372 | `c625bea2f8385d879cafa7969ad9b45bdf02c59d3ab01a42a2cfe1f13c779c64` |
| `sources/archives/DRS_v0.1_COMPLETE_3-Paper_SourcePack_2026-08-24.zip` | 37580 | `58b39eff2e3d8c547d4f3cd805317e216786c233a3bdf3e7e847bd6b167ebf1c` |
| `sources/archives/WPCE_v0.1_COMPLETE_6-Paper_SourcePack_2026-08-25.zip` | 92874 | `f459b56f8fea54625d7fbbf2456c0f5ffd043c6641b021c47bbcf695699e1d7e` |
| `tools/validate_integration_pack.py` | 977 | `7db28128746546341572f63adeb21151f2c3316bed863068f03c3ae6171b02e5` |

## Source preservation rule

- 原始 Phase 10 / 11 / 12 ZIP 不改寫。
- ACE / DRS 只收入 COMPLETE source packs。
- WPCE 六篇以原始 UTF-8 Markdown 直接保存，另建立一個 6-paper ZIP。
- 整合文件是新的 integration anchor，不取代各系列原始論文。
- 新整合文件已通過 UTF-8 與 canonical math delimiter validator。
