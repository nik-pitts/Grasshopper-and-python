hill = rs.coercecurve(x)
# reparametrize hill crv 0 to 1.
hill.Domain = rh.Geometry.Interval(0.00,1.00)

eval = rs.EvaluateCurve(hill, param)

a = eval
