import time
from abc import ABC, abstractmethod
from random import random

#
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#
#
# class Car(Vehicle):
#     def go(self):
#         print("You Drive the car")
#
#
# class MotorCycle(Vehicle):
#     def go(self):
#         print("You drive the motorcycle")
#
#
# v1 = Car()
# m1 = MotorCycle()
#
# v1.go()
# m1.go()

import random


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self):
        ...

    @abstractmethod
    def call_target(self, name: str):
        ...


class android(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        rdn = random.randint(1, 100)
        return f'battery {rdn}% remaining!'

    def call_target(self, name: str):
        print(f"Calling {name}. . .")
        time.sleep(3)
        print(f"{name} called!")


andr = android("Ipineapple")

andr.call_target("Luigi")
print(andr.power)