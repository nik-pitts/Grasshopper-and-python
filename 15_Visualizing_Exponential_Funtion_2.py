import rhinoscriptsyntax as rs
import math

#visualizing f(x) = 2^x + 2^(-x) and g(x) = 2^x - 2^(-x)
#As predicted, the shape of funtion is like as below.
#f(x) is even funtion, symmetric to axis Y
#g(x) is odd function, symmetric to origin (0,0)

plus_pts = []
minus_pts = []

for i in range(min, max):
    x=i*scale
    y1=math.pow(base,x)
    y2=math.pow(base,-x)
    plus_p = rs.AddPoint((x+x_pm,y1+y2+y_pm,0))
    minus_p = rs.AddPoint((x+x_pm,y1-y2+y_pm,0))
    plus_pts.append(plus_p)
    minus_pts.append(minus_p)
    
a = plus_pts
b = minus_pts
