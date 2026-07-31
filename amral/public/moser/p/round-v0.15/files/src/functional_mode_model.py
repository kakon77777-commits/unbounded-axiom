"""Round-15 functional curvature model.

Use the base curvature CDF t(u)=2F0(u)-1 and bounded Legendre modes
psi_n(u)=sqrt(2n+1) P_n(t(u)), n=1,...,8.

The deformed density is rho_p(u) exp(sum a_n psi_n(u)), normalized to unit mass.

A larger four-branch candidate was rejected after a ninth local minimum appeared
near phi=0.13908. Replays must audit the full phase circle.
