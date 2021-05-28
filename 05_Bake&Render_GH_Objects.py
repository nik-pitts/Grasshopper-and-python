import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

if active:
    for i in range(len(geo)):
        geo_id=geo[i]
        sc.doc=ghdoc
        doc_object=rs.coercerhinoobject(geo_id)
        geometry=doc_object.Geometry
        
        attributes=doc_object.Attributes
        sc.doc = Rhino.RhinoDoc.ActiveDoc
        rhino_ref = sc.doc.Objects.Add(geometry, attributes)
        
        rs.ObjectLayer(rhino_ref, layer)
