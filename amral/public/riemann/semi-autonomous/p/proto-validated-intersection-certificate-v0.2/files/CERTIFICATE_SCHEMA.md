# Certificate schema

`outputs/certificate.json` contains:

- `format`: schema identifier;
- `model`: node count, support and explicit function definition;
- `region`:
  - certified and unresolved cell counts;
  - global upper bound for \(2\Re G^2\);
  - Taylor derivative bound;
  - maximum subdivision depth;
- `arithmetic`:
  - endpoint correction and residual intervals;
  - \(C(0)\) and derivative-energy intervals;
  - activated prime powers;
  - finite, archimedean and total intervals;
  - midpoint error budgets;
- `strict_intersection_certificate_passed`: conjunction of the two strict signs;
- `scope_warning`: explicit non-RH status.

`outputs/certified_region_cells.csv` is the independently inspectable rectangular cover. Every row records a subrectangle and a strict upper bound.
