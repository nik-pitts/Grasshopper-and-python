import rhinoscriptsyntax as rs

pointList = []
refPosition = rs.PointCoordinates(p)

for j in range(y):
    for i in range(x):
        p = rs.AddPoint(i,j,0)
        dis = rs.Distance(refPosition,p)
        rs.MoveObject(p,[0,0,dis])
        pointList.append(p)

a=pointList
