import math
from base.geometry_base.shape import Shape
from base.geometry_base.point import Point,Point3D

class Line(Shape):
    def __init__(self, start: Point, end: Point):
        """
        Initialize a Line with a start point and an end point.
        """
        self.start = start
        self.end = end

    def length(self):
        """
        Calculate the length of the line using the Euclidean distance formula.
        """
        return math.sqrt((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)

    def slope(self):
        """
        Calculate the slope of the line.
        Returns None if the line is vertical (infinite slope).
        """
        if self.end.x == self.start.x:
            return None  # Vertical line, slope is undefined
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    def __str__(self):
        """
        Return a string representation of the Line.
        """
        return f"Line(start={self.start}, end={self.end})"

    def __repr__(self):
        """
        Return a formal string representation of the Line.
        """
        return f"Line(start={self.start}, end={self.end})"
    
class Line3D(Shape):
    def __init__(self, start: Point3D, end: Point3D):
        """
        Initialize a 3D Line with a start point and an end point.
        """
        self.start = start
        self.end = end

    def length(self):
        """
        Calculate the length of the 3D line using the Euclidean distance formula.
        """
        return math.sqrt(
            (self.end.x - self.start.x)**2 +
            (self.end.y - self.start.y)**2 +
            (self.end.z - self.start.z)**2
        )

    def direction_vector(self):
        """
        Calculate the direction vector of the 3D line.
        Returns a tuple (dx, dy, dz) representing the direction.
        """
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        dz = self.end.z - self.start.z
        return (dx, dy, dz)

    def __str__(self):
        """
        Return a string representation of the 3D Line.
        """
        return f"Line3D(start={self.start}, end={self.end})"

    def __repr__(self):
        """
        Return a formal string representation of the 3D Line.
        """
        return f"Line3D(start={self.start}, end={self.end})"