hill_raw = rs.coercecurve(x)
dom = rh.Geometry.Interval(0.00,1.00)
hill = hill_raw.set
sp = rs.CurveLength(hill, 0)
print sp

a=sp
