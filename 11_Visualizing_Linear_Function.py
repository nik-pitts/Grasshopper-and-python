import rhinoscriptsyntax as rs

pts = []

for i in range(min, max):
    x=i*scale
    y=inc*x + y_pm
    p = rs.AddPoint((x+x_pm,y,0))
    pts.append(p)
    
a = pts
