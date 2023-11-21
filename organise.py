import os
import shutil

fromdir= "c:/Users/MICROSOFT/Downloads"
todir="c:/Users/MICROSOFT/Downloads"
listofFiles= os.listdir(fromdir)
print(listofFiles)
for file in listofFiles:
    name,extension = os.path.splitext(file)
    if extension == "":
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1= fromdir + "/"+ file
        path2= todir + '/'+ 'imagefiles'
        path3= todir + "/"+ 'imagefiles' + "/"+ file
        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("Moving")
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)
            print("Moving")


     