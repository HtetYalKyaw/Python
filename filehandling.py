# f = open("readme.txt")
# for x in f:
#  print(x)
# f.close()

# f = open("myfile.txt", "x")

f = open("myfile.txt", "a")
f.write("Hello, i m human")
f.close()

f = open("myfile.txt")
print(f.read())