import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d
import random

random.seed(randomSeed)

def boxMaker(firstpoint, recursion):
    a.append(firstpoint)
    
    moveX=random.uniform(-size*moveFactor,size*moveFactor)
    moveY=random.uniform(-size*moveFactor,size*moveFactor)
    
    if recursion < 10 :
        movedpoint1 = firstpoint + Point3d(moveX, moveY, size)
        boxMaker(movedpoint1, recursion +1)
        
        if abs(moveX) > size * 0.5 and abs(moveY) > size * 0.5:
            movedpoint2 = firstpoint + Point3d(-moveX, -moveY, size)
            boxMaker(movedpoint2, recursion +1)


firstpoint = rs.coerce3dpoint(startpoint)

a = []

boxMaker(firstpoint, 0)
