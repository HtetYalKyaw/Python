import os

path = ("C:\\Users\\Dell\\Desktop\\SITE\\folder")

if os.path.exists(path):
    print("Yes, it exists")
    if os.path.isfile(path):
        print("It is a file.")
    elif os.path.isdir(path):
        print("It is a directory.")

else:
    print("No, it doesnt")