import rhinoscriptsyntax as rs
import Rhino as rh
from itertools import product

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

combination_list = []

for i in range(n):
    point = start_p + size*i
    combination_list.append(point)

combination_result = product(combination_list,repeat=3)

#making copying vector

cubes = []

for i in combination_result:
    coerce_point = rs.coerce3dpoint(i)
    vector = coerce_point - gp
    copy_box = rs.CopyObject(box, vector)
    cubes.append(copy_box)

#Making bounding box and finding centroid of bounding box
    
bounding_box = rs.BoundingBox(cubes)

a = bounding_box
