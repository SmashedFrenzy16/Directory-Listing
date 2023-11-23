from os import *

direc = input("Enter in the path of the directory: ")

contents = scandir(direc)

for i in contents:

    if i.is_file():

        print(i.name)

    elif i.is_dir():

        print(f"/{i.name}")



