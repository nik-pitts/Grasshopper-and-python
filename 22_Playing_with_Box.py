import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
import Rhino


input_tree = th.tree_to_list(x,retrieve_base=None)

geo_list = []

for list_list in input_tree:
    for list in list_list:
        for i in list:
            coerce_ob = rs.coercebrep(i)
            geo_list.append(coerce_ob)

centroid_list = []

for i in geo_list:
    geo_analysis = Rhino.Geometry.AreaMassProperties.Compute(i)
    centroid = geo_analysis.Centroid
    centroid_list.append(centroid)

centroid_scaled = []

for i in centroid_list:
    centroid_scaled.append(i*y) #y is a variable given by users.

a = centroid_list
b = centroid_scaled
