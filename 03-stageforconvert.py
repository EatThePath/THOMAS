import os
import shutil

def sort(sourcedir,destroot):
    sortcheckdest(destroot)
    sortrename(sourcedir)
    sortcopy(sourcedir,destroot)

def sortcheckdest(destroot):
    if not os.path.isdir(destroot):
        os.mkdir(destroot)

    for item in ['reflect','misc']:
        item_full = destroot+'/'+item
        if not os.path.isdir(item_full):
            os.mkdir(item_full)

def copyreplace(src,dest):
    if os.path.isfile(src):
        if os.path.isfile(dest):
            os.remove(dest)
        shutil.copy(src,dest)

def movereplace(src,dest):
    if os.path.isfile(src):
        if os.path.isfile(dest):
            os.remove(dest)
        shutil.copy(src,dest)

#move things into named subcategories so that conversion can act on useful sets
def sortcopy(sourcedir,destroot):
    with os.scandir(sourcedir) as contents:
        for item in contents:
            old= item.name
            if old.endswith('~'):
                continue
            new = old
            subdir = 'misc'
            if '-reflect.' in old:
                subdir = 'reflect'
            old = sourcedir+'/'+old
            new = destroot+'/'+subdir+'/'+new
            copyreplace(old,new)

#take the names krita output sticks on things and make them good names
def sortrename(sourcedir):
    with os.scandir(sourcedir) as contents:
        for item in contents:
            old= item.name
            new = old

            if '_Diffuse.' in old and os.path.isfile(old):
                new = old.replace('_Diffuse.','.')

            elif '_reflect.' in old and os.path.isfile(old):
                new = old.replace('_reflect.','-reflect')

            if new != old:
                movereplace(sourcedir+'/'+old,sourcedir+'/'+new)

sort('D:/ModDev/Shineup/03-forconvert','d:/moddev/shineup/04-sorted')