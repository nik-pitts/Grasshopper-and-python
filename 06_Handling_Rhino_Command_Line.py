import rhinoscriptsyntax as rs

if active:
    rs.Command("_Render")
    savedLocation = filePath + str(int(current)).zfill(4) + ".png"
    rs.Command("_-SaveRenderWindowAs \n\"" + savedLocation + "\"\n")
    rs.Command("_-CloseRenderWindow")
    C = True
else:
    C = False
