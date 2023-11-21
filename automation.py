import os
import shutil
import random
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir="c:/Users/MICROSOFT/Downloads"
todir= "c:/Users/MICROSOFT/Desktop"
dirTree= {
      "ImageFiles":['.gif','.png','.jpg','.jpeg','.jfif'],
      "DocumentFiles":['.txt','.pdf','.doc','.docx'],
      "VideoFiles":['.mpg','.mp2','.mpeg','.mp4','.m4p','.mpe','.m4v'],
      "SetupFiles":['.exe','.cmd','.bin','dmg']



}
class File_Movement_Handler(FileSystemEventHandler):
      def on_created(self, event):
            name,extension=os.path.splitext(event.src_path)
            time.sleep(1)
            for key,value in dirTree.items():
                  time.sleep(1)
    
                  if extension in value:
                     file=os.path.basename(event.src_path)
                     path1= fromdir + '/'+ file
                     path2= todir + '/' + key
                     path3= todir + '/' + key + '/' + file

                     if os.path.exists(path2):
                       print("Directory exist")
                       time.sleep(1)
                       if os.path.exists(path3):
                           print("File already exist")
                           print("Renaming")
                           new_file_name = os.path.splitext(file)[0] + str(random.randint(0, 999)) + os.path.splitext(file)[1]
                           path4 = todir + '/' + key + '/' + new_file_name
                           print("Moving")
                           shutil.move(path1, path4)
                           time.sleep(1)
                       else:
                           
                          print("Moving" + file + '.....')
                          shutil.move(path1,path3)
                     else:
                      print("Making Directory")
                      os.makedirs(path2)
                      print("Moving"+ file + "....")
                      shutil.move(path1,path3)
event_handler= File_Movement_Handler()
observer= Observer()
observer.schedule(event_handler, fromdir, recursive=True)
observer.start()
try:
    while True: 
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()

