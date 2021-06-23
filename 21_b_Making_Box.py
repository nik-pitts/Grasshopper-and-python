# Making box also in minus direction of coordinates.
# Point range: -x< <x, -y< <y, -z< <z

import rhinoscriptsyntax as rs
import Rhino as rh

start_p = -(size*n)/2
points = []

x = [start_p, start_p+size]
y = [start_p,start_p+size]
z = [start_p,start_p+size]

for u in x:
    for v in y:
        for w in z:
            cor = (u,v,w)
            points.append(cor)

points = sorted(points, key=lambda x : (x[2],x[1]))
points[2], points[3] = points[3], points[2]
points[6], points[7] = points[7], points[6]

box = rs.AddBox(points)

# copy boxes in x direction

boxes = []
gp = rs.coerce3dpoint((start_p,0,0))

for i in range(n):
    xn = rs.coerce3dpoint((start_p+i*size,0,0))
    vector = xn - gp
    copy_box = rs.CopyObject(box, vector)
    boxes.append(copy_box)

a = boxes
