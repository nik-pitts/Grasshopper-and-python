hill = rs.coercecurve(x)
# reparametrize hill crv 0 to 1.
hill.Domain = rh.Geometry.Interval(0.00,1.00)

eval1 = rs.EvaluateCurve(hill, param)
eval2 = rs.EvaluateCurve(hill, param + wheel_distance)

a = eval1
b = eval2
