import rhinoscriptsyntax as rs
import math

#min&max: making x coordinates
#scale: scaler multiplied to x coordinates
#x_pm: x direction parallel movement
#y_pm: y direction parallel moverment
#r: radius

plus_y_pt = []
minus_y_pt = []

for i in range(min, max):
    x=i*scale
    plus_y_raw=math.pow(r,2)-math.pow(x,2)
    plus_y=math.sqrt(plus_y_raw)
    minus_y=-plus_y
    plus_p=rs.AddPoint((x+x_pm, plus_y+y_pm,0))
    minus_p=rs.AddPoint((x+x_pm, minus_y+y_pm,0))
    plus_y_pt.append(plus_p)
    minus_y_pt.append(minus_p)
    
a = plus_y_pt
b = minus_y_pt
