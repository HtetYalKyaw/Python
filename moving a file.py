import os

source = "test.txt"
destination = "C:\\Users\\Dell\\Desktop\\SITE\\test.txt"

try:
    if os.path.exists(destination):
        print("The path already exists.")
    else:
        os.replace(source, destination)
        print(source+" was moved.")
except FileNotFoundError:
    print(source+" not found.")