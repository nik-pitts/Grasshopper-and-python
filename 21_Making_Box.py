import rhinoscriptsyntax as rs
import Rhino as rh

#Guide point will be imported from Rhino to GH
#Size will be a parametric variable imported from Rhino to GH 
#A simpler script making box will be further developed.

point = rs.coerce3dpoint(guide_point)

mo1 = rs.CopyObject(guide_point, [0,0,0])
mo2 = rs.CopyObject(guide_point, [0,size,0])
mo3 = rs.CopyObject(guide_point, [size,size,0])
mo4 = rs.CopyObject(guide_point, [size,0,0])
mo5 = rs.CopyObject(guide_point, [0,0,size])
mo6 = rs.CopyObject(guide_point, [0,size,size])
mo7 = rs.CopyObject(guide_point, [size,size,size])
mo8 = rs.CopyObject(guide_point, [size,0,size])

corners = [mo1, mo2, mo3, mo4, mo5, mo6, mo7, mo8]

box = rs.AddBox(corners)

a = box
