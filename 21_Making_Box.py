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

boxes = []
square_boxes = []
cube_boxes = []

#making all possible rectangle box points

x_guide = 0

while x_guide<len(copy_points):
    points = []
    starting_x=copy_points[x_guide][0]
    x = [starting_x, starting_x+size]
    y = [size,0.0]
    z = [size,0.0]
    
    for u in x:
        for v in y:
            for w in z:
                cor = (u,v,w)
                points.append(cor)

    points = sorted(points, key=lambda x : (x[2],x[1]))
    points[2], points[3] = points[3], points[2]
    points[6], points[7] = points[7], points[6]
    print points

    box = rs.AddBox(points)
    points = [] #making points list as default
    boxes.append(box)
    
    #making vectors & copy to y direction
    
    y_guide = 0
    
    while y_guide<n:
        y_vec = [0,size*y_guide,0]
        y_copy_box = rs.CopyObject(box, y_vec)
        square_boxes.append(y_copy_box)
        y_guide = y_guide+1

        #making vectors & copy to z direction
        
        z_guide = 1
        
        while z_guide<n:
            z_vec = [0,0,size*z_guide]
            z_copy_box = rs.CopyObject(y_copy_box, z_vec)
            cube_boxes.append(z_copy_box)
            z_guide = z_guide+1
    
    x_guide = x_guide + 1
    boxes = []

a = square_boxes + cube_boxes
