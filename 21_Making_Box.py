import rhinoscriptsyntax as rs
import Rhino as rh
from itertools import product

#Guide point will be imported from Rhino
#Size will be a parametric variable imported from GH 
#A simpler script making a box is developed, using itertools moudle in python.

point = rs.coerce3dpoint(guide_point)

vec_list = [0, size]
points = []

#making all possible rectangle box points

for vec in product(vec_list, repeat=3):
    points.append(vec)

print points # All possible rectangle box points
print len(points) # Should be 8

box = rs.AddBox(points)

a = box
