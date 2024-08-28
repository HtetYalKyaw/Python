# super() = function used to give access to the methods of a parent class .
#             return temporary object of a parent class when used.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square1 = square(3, 4)
p2 = Cube(5, 6, 5)

square1.area()
p2.volume()

print(square1.area())
print(p2.volume())
