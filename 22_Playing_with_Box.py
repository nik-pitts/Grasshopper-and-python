import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th

#This code is to explode original cube boxes.

#1. Turning box into Rhino object
raw_bb_base = th.tree_to_list(b,retrieve_base=None)
bb_base = rs.coercebrep(raw_bb_base)

#2. Finding cetroid of Boxes

#3. Scale every centroid points

#4. Move original geometries to centroid points
