"""Core LP formulation for Moser Skew Lab v0.2.

For fixed rotation phi:
minimize scale s over translation (tx,ty), subject to
h_gamma(theta_j-phi)+tx*cos(theta_j)+ty*sin(theta_j)
    <= s*h_container(theta_j).

The negative HiGHS inequality marginals are nonnegative contact weights.
"""
