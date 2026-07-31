# 第 15 輪候選與分支開啟審計

## 最終候選

```json
{
  "multiplier": 3.2275,
  "coefficient_norm": 0.1291,
  "parameters": [
    0.3361039495856486,
    1.4054231629110312,
    0.051972968077192816,
    0.5802095527303379,
    0.036983383487424734
  ],
  "coefficients": {
    "translation_like_P1": 0.000636097039547498,
    "width_split_P2": 0.01763543356796946,
    "skew_P3": 0.004755842498620271,
    "shoulder_P4": -0.0752235430432821,
    "tail_skew_P5": 0.010666503454247333,
    "triple_peak_P6": 0.057547527232882936,
    "wave_P7": -0.019001897723771536,
    "wave_P8": -0.08299176521743751
  },
  "resolution_audit": [
    {
      "u_count": 6001,
      "four_branch_values": [
        0.9989144811220076,
        0.9989144817396812,
        0.9989144807169635,
        0.9989144807169643
      ],
      "four_branch_phases": [
        0.1550437940451888,
        0.12361061090488029,
        2.0943951023931953,
        4.71238898038469
      ],
      "control_scale": 0.9989144807169635,
      "control_spread": 1.0227176883148559e-09,
      "latent_phase": 0.1384248020095228,
      "latent_scale": 0.9989144837215295,
      "latent_minus_control": 3.0045659293875815e-09,
      "global_scale": 0.9989144807169635,
      "gain_over_round15_base": 1.3747448013301522e-07,
      "gain_over_stored_round13": 1.3741947846312996e-07,
      "rho_min": 9.41950903438551e-13,
      "rho_max": 13.705712630270922
    },
    {
      "u_count": 12001,
      "four_branch_values": [
        0.9989144811208411,
        0.9989144817391554,
        0.998914480716965,
        0.9989144807169653
      ],
      "four_branch_phases": [
        0.15504376882869256,
        0.1236108260351185,
        2.0943951023931953,
        4.71238898038469
      ],
      "control_scale": 0.998914480716965,
      "control_spread": 1.0221904434004614e-09,
      "latent_phase": 0.13842464183156328,
      "latent_scale": 0.9989144837215915,
      "latent_minus_control": 3.004626547564726e-09,
      "global_scale": 0.998914480716965,
      "gain_over_round15_base": 1.3747448157630515e-07,
      "gain_over_stored_round13": 1.374194799064199e-07,
      "rho_min": 9.419509034385502e-13,
      "rho_max": 13.706037778467712
    },
    {
      "u_count": 24001,
      "four_branch_values": [
        0.9989144811208791,
        0.9989144817392616,
        0.9989144807169715,
        0.9989144807169712
      ],
      "four_branch_phases": [
        0.15504372142464304,
        0.12361080498982033,
        2.0943951023931953,
        4.71238898038469
      ],
      "control_scale": 0.9989144807169712,
      "control_spread": 1.0222903634726777e-09,
      "latent_phase": 0.13842466727521352,
      "latent_scale": 0.998914483721559,
      "latent_minus_control": 3.0045878007811666e-09,
      "global_scale": 0.9989144807169712,
      "gain_over_round15_base": 1.374744877935541e-07,
      "gain_over_stored_round13": 1.3741948612366883e-07,
      "rho_min": 9.419509034385504e-13,
      "rho_max": 13.706037778467708
    },
    {
      "u_count": 48001,
      "four_branch_values": [
        0.9989144811208676,
        0.9989144817392726,
        0.9989144807169661,
        0.9989144807169661
      ],
      "four_branch_phases": [
        0.15504370744868684,
        0.12361080367136806,
        2.0943951023931953,
        4.71238898038469
      ],
      "control_scale": 0.9989144807169661,
      "control_spread": 1.0223064617065347e-09,
      "latent_phase": 0.13842469825295847,
      "latent_scale": 0.9989144837215526,
      "latent_minus_control": 3.004586468513537e-09,
      "global_scale": 0.9989144807169661,
      "gain_over_round15_base": 1.3747448268652818e-07,
      "gain_over_stored_round13": 1.3741948101664292e-07,
      "rho_min": 9.419509034385504e-13,
      "rho_max": 13.706037778467712
    },
    {
      "u_count": 96001,
      "four_branch_values": [
        0.9989144811208602,
        0.9989144817392649,
        0.9989144807169461,
        0.9989144807169489
      ],
      "four_branch_phases": [
        0.15504372158465476,
        0.12361081163961733,
        2.0943951023931953,
        4.71238898038469
      ],
      "control_scale": 0.9989144807169461,
      "control_spread": 1.022318785182108e-09,
      "latent_phase": 0.13842463331396365,
      "latent_scale": 0.9989144837215472,
      "latent_minus_control": 3.004601123457462e-09,
      "global_scale": 0.9989144807169461,
      "gain_over_round15_base": 1.3747446270251373e-07,
      "gain_over_stored_round13": 1.3741946103262848e-07,
      "rho_min": 9.419509034385502e-13,
      "rho_max": 13.706037778467708
    }
  ],
  "highest_resolution_global_scale": 0.9989144807169461,
  "highest_resolution_gain_over_round13": 1.3741946103262848e-07,
  "highest_resolution_latent_margin": 3.004601123457462e-09,
  "full_phase": {
    "u_count": 96001,
    "phase_count": 262144,
    "contact_change_count": 18,
    "distinct_signature_count": 18,
    "sampled_local_minimum_count": 9,
    "local_minima": [
      {
        "phase": 2.0943951023931953,
        "scale": 0.9989144807169461,
        "signature": "120deg"
      },
      {
        "phase": 4.71238898038469,
        "scale": 0.9989144807169489,
        "signature": "p3|p3|p1"
      },
      {
        "phase": 0.15504370523813515,
        "scale": 0.9989144811208601,
        "signature": "L|p0|p2"
      },
      {
        "phase": 0.123610811812937,
        "scale": 0.9989144817392648,
        "signature": "L|p0|p2"
      },
      {
        "phase": 0.1384246484932264,
        "scale": 0.9989144837215471,
        "signature": "L|p0|p2"
      },
      {
        "phase": 1.7361485087542565,
        "scale": 1.029348172727573,
        "signature": "p2|L|p3"
      },
      {
        "phase": 5.235987755982968,
        "scale": 1.0814270889115383,
        "signature": "p0|p3|p1"
      },
      {
        "phase": 3.028192453799176,
        "scale": 1.0998062298940177,
        "signature": "p3|p1|p0"
      },
      {
        "phase": 3.778900491652884,
        "scale": 1.1275841851852073,
        "signature": "p3|p2|L"
      }
    ],
    "global_minimum": {
      "phase": 2.0943951023931953,
      "scale": 0.9989144807169461,
      "signature": "120deg"
    },
    "second_minimum": {
      "phase": 4.71238898038469,
      "scale": 0.9989144807169489,
      "signature": "p3|p3|p1"
    },
    "margin_to_second": 2.7755575615628914e-15
  }
}
```

## 被排除的四分支候選

```text
four-branch scale = 9.9891469224730511e-01
full-phase hidden branch = 9.9891155002465470e-01
hidden phase = 1.3908150396590241e-01
```

## 關鍵判定

- 四分支候選已排除；
- Newton 線存在真上升窗；
- 幾何重整後選定 m=3.2275；
- m=3.228 附近第五分支開始接管；
- 最終第五分支餘量約 3.0e-9；
- 尚未有區間證書。
