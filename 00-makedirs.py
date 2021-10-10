import os

def checkdest(destroot):
    if not os.path.isdir(destroot):
        os.mkdir(destroot)
checkdest('D:/ModDev/Shineup/00-oldraw')
checkdest('D:/ModDev/Shineup/01-altsource')
checkdest('D:/ModDev/Shineup/01-oldtga-convert')
checkdest('D:/ModDev/Shineup/02-oldtga-fromsource')
checkdest('D:/ModDev/Shineup/03-forconvert')
checkdest('D:/ModDev/Shineup/04-sorted')
checkdest('D:/ModDev/Shineup/04-sorted')
checkdest('D:/ModDev/Shineup/05-gameready')
checkdest('D:/ModDev/Shineup/09-archive')