import math
from base.geometry_base.shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle : radius {self.radius}"