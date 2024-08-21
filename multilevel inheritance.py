class Organism:
    alive = True

class animal(Organism):
    def eat(self):
        print("This animal is eating !")

class dog(animal):
    def bark(self):
        print("This Dog is Barking ")


p1= dog()
p1.eat()
p1.bark()


