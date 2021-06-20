import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
import Rhino

#This code is to explode original cube boxes into bigger scale.

input_tree = th.tree_to_list(x,retrieve_base=None)

#1. Turning box into Rhino object

geo_list = []

for list_list in input_tree:
    for list in list_list:
        for i in list:
            geo = rs.coercesurface(i)
            geo_list.append(i)

print len(geo_list)

#2. Finding cetroid of Boxes

centroid_list = []

for i in geo_list:
    geo_analysis = Rhino.Geometry.AreaMassProperties.Compute(i)
    centroid = geo_analysis.Centroid
    centroid_list.append(centroid)
