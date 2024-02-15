import math


class shape:
    def calculate_area(self):
        pass
class Rectangle(shape):
    def __init__(self, width, height):
            self.width = width
            self.height = height

    def calculate_area(self):
            return self.width*self.height

class circles (shape):
    def __init__(self,radius):
         self.radius=radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)


    def calculate_totalarea (shapes):
         totalarea =  0
         for shape in shapes:
            totalarea += shape.calculate_area()
            return totalarea

mycircle=circles(9)
myRectangle=Rectangle(7,6)
print(f"Area of circle is {mycircle.calculate_area()}")
