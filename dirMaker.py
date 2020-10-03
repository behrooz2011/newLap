
#!/usr/bin/env python3
# from PIL import Image
import os
# print(os.getcwd())

# dir = 'C:/My tutorials/python coursera/practice/nested/1'
# if not os.path.exists(dir):
#     os.makedirs(dir)
#     print('success')
ndir=os.getcwd()
for file in os.listdir(ndir):
 if file.endswith('txt'):
     print(file[:-3]+'jpg')
#   im=Image.open(file).rotate(90).resize((128,128))
#   file = file[:-4]+'jpg'

#   dir ='/home/student-03-0427a38b784e/opt/icons/'
#   if not os.path.exists(dir):
#     os.makedirs(dir)
#     print('success')
#   file= dir+file
#   im.save(file)

