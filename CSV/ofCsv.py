import csv
import os

with open("csv_file.csv")as f:
    m=csv.reader(f)
    print(m)
    for x in m:
        name,phone,dep=x
        print("Name: {}, Phone Number: {}, Department: {}".format(name,phone,dep))

print(os.listdir())