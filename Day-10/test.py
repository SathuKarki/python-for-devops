import os

#number = input("please give numbers")
#print(number)

folders = input("plese share the folder with spaces").split()

print(folders)

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide valid folder name. This folder doesnot exists" + folder)
        continue

    print("****Listing the files of folder " + folder )
        #print(files)
    for file in files:
        print(file)