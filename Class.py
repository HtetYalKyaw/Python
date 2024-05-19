class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, My Name is "+ self.name)

    # def __str__(self):
        # return f"{self.name}({self.age})"


p1 = Myclass("Htet Yal Kyaw", 25)
p1.myfunc()

# class Human:
#     pass

# del p1 (delete object properties)



