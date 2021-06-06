import rhinoscriptsyntax as rs
import Rhino as rh
from itertools import product

#Guide point will be imported from Rhino
#Size will be a parametric variable imported from GH 
#A simpler script making a box is developed, using itertools moudle in python.

gp = rs.coerce3dpoint(guide_point)

vec_list = [0, size]
points = []

#making all possible rectangle box points

for vec in product(vec_list, repeat=3):
    points.append(vec)

print points # All possible rectangle box points
print len(points) # Should be 8

box = rs.AddBox(points)

a = box

#x-axis array
#copy guide point based on size.
#user can decide how much they want to array in x direction.
#n is a parameter given by grasshopper.

copy_points = []
repeat = 1

while repeat<n:
    raw_copy_gp = rs.CopyObject(gp, [repeat*size,0,0])
    copy_gp = rs.coerce3dpoint(raw_copy_gp)
    copy_points.append(copy_gp)
    repeat = repeat+1

print copy_points
