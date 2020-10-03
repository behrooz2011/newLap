import shutil
import os
dest="C:/My tutorials/python coursera/6 Projects/1"
for file in os.listdir('C:/My tutorials/python coursera/practice/pipe'):
    print(type(file))
    file='C:/My tutorials/python coursera/practice/pipe/'+file
    shutil.move(file,dest)