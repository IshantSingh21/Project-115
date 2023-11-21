import os
import shutil

fromdir="c:/Users/MICROSOFT/Downloads"
todir= "c:/Users/MICROSOFT/Downloads"
listofFiles= os.listdir(fromdir)
print(listofFiles)

for file in listofFiles:
    name,extension= os.path.splitext(file)
    print(extension)
    if extension== "":
        continue
    if extension in ['.txt','.pdf','.doc','.docx']:
                     path1= fromdir + '/'+ file
                     path2= todir + '/' + "Document_Files"
                     path3= todir + '/' + "Document_Files" + '/' + file

                     if os.path.exists(path2):
                       print("Moving" + file + '.....')
                       shutil.move(path1,path3)
                     else:
                      os.mkdir(path2)
                      print("Moving"+ file + "....")
                      shutil.move(path1,path3)
             
                     