"""Round-14 model definitions.

Double-peak model:
    curvature density = (1-a) rho(c1,e1) + a rho(c2,e2)
where rho is a normalized sech^2 layer.

Single peak is recovered at:
    c1=c2 and e1=e2.

Asymmetric model:
    left local center  = c + eta_c
    right local center = 1 - c + eta_c
    left width         = e exp(eta_e)
    right width        = e exp(-eta_e)

Under reflection, the tested chirality parameters change sign.  The objective
uses the weaker of the original and reflected branches.
