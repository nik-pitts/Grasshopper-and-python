import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

if active:
    sc.doc = Rhino.RhinoDoc.ActiveDoc
    objs = rs.ObjectsByLayer(layer)
    rs.DeleteObjects(objs)
