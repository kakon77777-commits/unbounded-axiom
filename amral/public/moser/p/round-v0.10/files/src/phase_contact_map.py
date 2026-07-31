"""Round-10 phase contact map.

The support labels are:
    p0, p1, p2, p3 -- curve endpoints/junctions
    L, R           -- interior stationary support point on a smooth wing

For each phase, the active signature is:
    (argmin rotated-x, argmin rotated-y, argmax diagonal support)

Within a fixed signature interval, the scale derivative uses the envelope
theorem:
    s' = n_d'·p_d - (n_x'·p_x)/A - (n_y'·p_y)/B.

The generated interval map is numerical.  A rigorous certificate still needs
interval enclosures for transition locations and derivative signs.
