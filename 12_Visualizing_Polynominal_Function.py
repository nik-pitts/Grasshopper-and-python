import rhinoscriptsyntax as rs
import math

pts = []

for i in range(min, max):
    x=i*scale
    y=math.pow(x,int(power))
    p = rs.AddPoint((x+x_pm,y+y_pm,0))
    pts.append(p)
    
a = pts
