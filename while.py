# method 1
# name = ""
#
# while len(name) == 0:
#     name = input("Enter Your Name :")
#
# print ("Hello " + name )

# method 2
name = None

while not name:
    name = input("Enter Your Name : ")

print("Hello " + name)