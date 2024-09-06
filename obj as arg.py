class Car:
    color = None


class Motorcycle:
    color = None


def change_color(car, color):
    car.color = color
    print(color)


c1 = Car()
c2 = Car()
b1 = Motorcycle()
b2 = Motorcycle()

change_color(c1, "blue")
change_color(c2, "red")
change_color(b1, "Lavender ")
change_color(b2, "black")
