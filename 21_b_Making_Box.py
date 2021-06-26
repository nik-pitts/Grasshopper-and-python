import rhinoscriptsyntax as rs
import Rhino as rh
from itertools import product

start_p0 = 0
start_p = -(size*n)/2
points = []

x = [start_p0, start_p0+size]
y = [start_p0,start_p0+size]
z = [start_p0,start_p0+size]

for u in x:
    for v in y:
        for w in z:
            cor = (u,v,w)
            points.append(cor)

points = sorted(points, key=lambda x : (x[2],x[1]))
points[2], points[3] = points[3], points[2]
points[6], points[7] = points[7], points[6]

box = rs.AddBox(points)

gp = rs.coerce3dpoint((0,0,0))

combination_list = []

for i in range(n):
    point = start_p + size*i
    combination_list.append(point)

print combination_list

combination_result = product(combination_list,repeat=3)

#making copying vector

cubes = []

for i in combination_result:
    coerce_point = rs.coerce3dpoint(i)
    vector = coerce_point - gp
    copy_box = rs.CopyObject(box, vector)
    cubes.append(copy_box)

a = cubes
