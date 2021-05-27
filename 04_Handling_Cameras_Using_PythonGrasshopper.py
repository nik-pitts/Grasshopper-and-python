import rhinoscriptsyntax as rs
import scriptcontext as sc

sc.doc = ghdoc
loc = rs.coerce3dpoint(location)
tar = rs.coerce3dpoint(target)

vp = sc.doc.Views.ActiveView.ActiveViewport
vp.SetCameraLocation(loc, False)
vp.SetCameraDirection(tar-loc, True)
