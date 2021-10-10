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


#Function 1: use compressonator to decomp to tga
def decomp(sourcedir,destdir):
    cmdstring = 'compressonatorcli -UseGPUDecompress -ff DDS -fd ARGB_8888 -log -fx TGA ' +sourcedir+' '+destdir+'/holder/'
    print('running: '+cmdstring)
    subprocess.run(cmdstring)
    scrubnames(destdir,'_dds_ARGB_8888')
    scrubnames(destdir,'_dds_Unknown')

#decomp('D:/ResolutionOfHector/Modding/Freespace/BPCExtractQ/data/maps','D:/ModDev/Shineup/01-oldtga-convert')
decomp('D:/ModDev/Shineup/00-oldraw','D:/ModDev/Shineup/01-oldtga-convert')