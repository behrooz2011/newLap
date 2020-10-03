#!/usr/bin/env python3
from PIL import Image
import os
import shutil

dir ='/home/student-03-0427a38b784e/opt/icons/'
if not os.path.exists(dir):
    os.makedirs(dir)
    print('success')

for file in os.listdir('#'):
 if file.endswith('tiff'):
  im=Image.open(file).rotate(90).resize((128,128))
  file = file[:-4]+'jpg'
  im.save(file)
  shutil.move('#'+file,dir)
  

######### move ########
# import subprocess
# src ="C:/My tutorials/python coursera/practice/pipe"
# dest="C:/My tutorials/python coursera/6 Projects/1"
# subprocess.call(["rsync", "-arq", src, dest])


import shutil
import os
dest="C:/My tutorials/python coursera/6 Projects/1"
for file in os.listdir('C:/My tutorials/python coursera/practice/pipe'):
    print(type(file))
    shutil.move(file,dest)

