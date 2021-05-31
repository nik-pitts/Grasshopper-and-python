import rhinoscriptsyntax as rs
import math

power_pts = []
log_pts = []

for i in range(min, max):
    x=i*scale
    y=math.pow(base,x)
    power_p = rs.AddPoint((x+x_pm,y+y_pm,0))
    log_p = rs.AddPoint((y+x_pm,x+y_pm,0))
    power_pts.append(power_p)
    log_pts.append(log_p)
    
a = power_pts
b = log_pts
