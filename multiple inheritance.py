class prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class rabbit(prey):
    pass

class hawk(Predator):
    pass

class fish(prey, Predator):
    pass

p1 = rabbit()
p1.flee()

p2 = hawk()
p2.hunt()

p3 = fish()
p3.flee()
p3.hunt()
