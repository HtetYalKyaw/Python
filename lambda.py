# def double (x):
#     return x*2
#
# print(double(5))

double = lambda x : x* 2
multiple = lambda x,y : x*2 + y*2
name = lambda fname, lname : fname + lname

check = lambda age :True if age > 18 else False


print(double(5))
print(multiple(5,10))
print(name("Bro","Code"))
print(check(5))
