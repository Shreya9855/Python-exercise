#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius**2*22/7

c = Circle(7)
print(c.area())