#!/usr/bin/env python3
# from PIL import Image
# import os

# dir ='/home/student-03-0427a38b784e/opt/icons/'
# for file in os.listdir('/home/student-03-0427a38b784e/images'):
#  if file.endswith('tiff'):
#   im=Image.open(file).rotate(90).resize((128,128))
#   file = file[:-4]+'jpg'
#   if not os.path.exists(dir):
#     os.makedirs(dir)
#     print('success')
#   new_file=dir+file
#   im.save(new_file)

######### move ########
import subprocess
src ="C:/My tutorials/python coursera/practice/pipe"
dest="C:/My tutorials/python coursera/6 Projects/1"
subprocess.call(["rsync", "-arq", src, dest])
