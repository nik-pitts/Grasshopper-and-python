import rhinoscriptsyntax as rs
import Rhino as rh
from itertools import product, permutations

#Guide point will be imported from Rhino to GH
#Size will be a parametric variable imported from Rhino to GH 
#More simpler script making box will be further developed.

gp = rs.coerce3dpoint(guide_point)

#x-axis array
#copy guide point based on size.
#user can decide how much they want to array in x direction.

copy_points = []

repeat = 0

while repeat<n:
    raw_copy_gp = rs.CopyObject(gp, [repeat*size,0,0])
    copy_gp = rs.coerce3dpoint(raw_copy_gp)
    copy_points.append(copy_gp)
    repeat = repeat+1

print copy_points[2][0]
print len(copy_points)

box_list = []

#making all possible rectangle box points

indicator = 0

while indicator<len(copy_points):
    points = []
    if indicator == 0:
        vec_list = [copy_points[indicator][0], size]
        indicator = indicator + 1
        for vec in product(vec_list, repeat=3):
            points.append(vec)
    else:
        vec_list = [copy_points[indicator][0], size*(indicator+1),0]
        indicator = indicator + 1
        for vec in product(vec_list, repeat=3): 
            #considering how points are made, especially now boxes are only arrayed in x-aixs.
            points.append(vec)

    print points
    box = rs.AddBox(points)
    points = [] #making points list as default
    box_list.append(box)

a = box_list
