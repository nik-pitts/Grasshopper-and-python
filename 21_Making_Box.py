import rhinoscriptsyntax as rs
import Rhino as rh

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
    raw_copy_gp = rs.CopyObject(gp,[repeat*size,0,0])
    copy_gp = rs.coerce3dpoint(raw_copy_gp)
    copy_points.append(copy_gp)
    repeat = repeat+1

print copy_points[2][0]
print len(copy_points)

box_list = []
y_box_list = []

#making all possible rectangle box points

indicator = 0

while indicator<len(copy_points):
    points = []
    starting_x=copy_points[indicator][0]
    starting_y=copy_points[indicator][1]
    x = [starting_x, starting_x+size]
    y = [size,0.0]
    z = [size,0.0]
    
    for u in x:
        for v in y:
            for w in z:
                cor = (u,v,w)
                points.append(cor)

    print points
    box = rs.AddBox(points)
    points = [] #making points list as default
    box_list.append(box)
    
    #making vectors & copy to y direction
    
    y_guide = 1
    
    while y_guide<n:
        y_vec = [0,size*y_guide,0]
        y_copy_box = rs.CopyObject(box, y_vec)
        y_box_list.append(y_copy_box)
        y_guide = y_guide+1
    
    indicator = indicator + 1

a = box_list
b= y_box_list
