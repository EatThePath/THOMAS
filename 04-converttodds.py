import os
import subprocess

def scrubnames(targetdir,targetstring):
    contents = os.scandir(targetdir)
    with  os.scandir(targetdir) as contents:
        for item in contents:
            if targetstring in item.name:
                old=item.name
                new = old.replace(targetstring,'')
                old = targetdir+'/'+old
                new = targetdir+'/'+new
                if os.path.isfile(new):
                    os.remove(new)
                os.rename(old,new)

def checkdest(destroot):
    if not os.path.isdir(destroot):
        os.mkdir(destroot)

def recomp(sourcedir,destdir):
    checkdest(destdir)
    recompdir(sourcedir,destdir,'reflect','-fd BC7')
    recompdir(sourcedir,destdir,'misc','-fd BC7')
    scrubnames(destdir,'_png_BC7')
    scrubnames(destdir,'_tga_BC7')

def recompdir(sourcedir,destdir,dirname,flags):
    s = sourcedir+'/'+dirname
    d = destdir
    cmdstring = 'compressonatorcli -mipsize 128  -EncodeWith GPU  '+flags+' ' +s+' '+d+'/hold/'
    print('running: '+cmdstring)
    subprocess.run(cmdstring)



recomp('D:/ModDev/Shineup/04-sorted','d:/moddev/shineup/05-gameready')