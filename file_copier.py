import shutil
import os

origin = 'C:\\Users\\bbria\\Downloads\\keras training set\\banana'
target = 'C:\\Users\\bbria\\Downloads\\training2\\banana'

# counter = 0
# for root, dirs, files in os.walk(origin):
#     for file in files:
#         counter += 1
#         if counter == 10:
#             path_file = os.path.join(root, file)
#             shutil.copy2(path_file, target)
#             counter = 0



for root, dirs, files in os.walk(origin):  # replace the . with your starting directory
   for file in files:
      path_file = os.path.join(root,file)
      shutil.copy2(path_file,target) # change you destination dir