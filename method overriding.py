class prey:
    def eat(self):
        print("This animal is eating. ")


class rabbit(prey):
    def eat(self):
        print("This animal is eating carrot.")


p1 = rabbit()
p1.eat()
