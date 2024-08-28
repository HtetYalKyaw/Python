class Car:
    def start(self):
        print("You start the car !")
        return self

    def drive(self):
        print("You drive the car ")
        return self

    def brake(self):
        print("You step on the brake ")
        return self

    def stop(self):
        print("You stop the car")
        return self


car = Car()

car.start().drive().brake().brake()