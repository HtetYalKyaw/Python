class Human:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print(self):
        print(self.firstname, self.lastname)


class student(Human):
    def __init__(self, fname, lname, year):
        # Human.__init__(self, fname, lname) child init function override the parent init function and no longer inheritance
        super().__init__( fname, lname) #super() inheritance all from parent class
        self.graduationyear = year
    def welcome(self):
        print("Welcome,", self.firstname,self.lastname ,"to the class of ",self.graduationyear)



p1 = student("HYK", "YMT", 2024)
p1.print()
print(p1.graduationyear)
p1.welcome()
