import os
import platform

def main():
    if str(platform.system()) == "Linux" or str(platform.system()) == "Darwin":
        if str(platform.system()) == "Darwin":
            print("Not tested on MacOS, but i don't se why it shouldn't work, proceed with caution")
        sortDownloads(myInput("Enter absolute target directory (e.g. /home/user/Downloads) :"), myInput("Enter absolute destination directory (e.g. /home/user/Downloads_Sorted) :"))
    else:
        print("This Script is UNIX only at the moment! Start using a good OS!")
        exit(1)

def sortDownloads(targetDir, destDir):
    if not os.path.exists(targetDir):
        print("Specified target directory "+ targetDir +" does not exsist! Try again!")
        sortDownloads(myInput("Enter absolute target directory (e.g. /home/user/Downloads) :"), myInput("Enter absolute destination directory (e.g. /home/user/Downloads_Sorted) :"))
    if not destDir.endswith("/"):
        destDir = destDir + "/"
    createDir(destDir)
    createSubDirs(destDir)
    if not targetDir.endswith("/"):
        targetDir = targetDir + "/"
    targetDirEncoded = os.fsencode(targetDir)
    for file in os.listdir(targetDirEncoded):
        filename = os.fsdecode(file)
        if filename.endswith(".apng") or filename.endswith(".avif") or filename.endswith(".gif") or filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".jfif") or filename.endswith(".pjpeg") or filename.endswith(".pjp") or  filename.endswith(".png") or filename.endswith(".svg") or filename.endswith(".webp") or filename.endswith(".bmp") or filename.endswith(".ico") or filename.endswith(".cur") or filename.endswith(".tif") or filename.endswith(".tiff"):
            directory, name  = os.path.split(filename)
            os.rename(os.path.join(targetDir, name), os.path.join(destDir, "Images", name))
        elif filename.endswith(".doc") or filename.endswith(".docx") or filename.endswith(".odt") or filename.endswith(".pdf") or filename.endswith(".xls") or filename.endswith(".xlsx") or filename.endswith(".ppt") or filename.endswith(".pptx") or filename.endswith(".txt") or filename.endswith(".md"):
            directory, name  = os.path.split(filename)
            os.rename(os.path.join(targetDir, name), os.path.join(destDir, "Documents", name))
        elif filename.endswith(".7z") or filename.endswith(".bz2") or filename.endswith(".gz") or filename.endswith(".rar") or filename.endswith(".zip") or filename.endswith(".zipx"):
            directory, name  = os.path.split(filename)
            os.rename(os.path.join(targetDir, name), os.path.join(destDir, "Archives", name))
        elif filename.endswith(".iso"):
            directory, name  = os.path.split(filename)
            os.rename(os.path.join(targetDir, name), os.path.join(destDir, "ISOs", name))
        else:
            directory, name  = os.path.split(filename)
            os.rename(os.path.join(targetDir, name), os.path.join(destDir, "Other", name))
    print("Everything sorted!")
    exit(0)

    
    
def createDir(dir):
    try:
        print("Creating directory " + str(dir))
        os.mkdir(dir)
    except FileExistsError:
        print("Using existing directory: " + dir)

def createSubDirs(dir):
    createDir(str(dir) + "Images/")
    createDir(str(dir) + "Documents/")
    createDir(str(dir) + "Archives/")
    createDir(str(dir) + "ISOs/")
    createDir(str(dir) + "Other/")


def myInput(string):
    return str(input(string)).strip()

def yes_no(string):
    ask = str(input(string+' (y/N): ')).lower().strip()
    if ask[0] == 'y':
        return True
    else:
        return False


#call_main####################
main()
##############################
