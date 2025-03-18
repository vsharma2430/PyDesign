import math

class Point:
    def __init__(self, x=0, y=0):
        """
        Initialize a Point with x and y coordinates.
        Default coordinates are (0, 0).
        """
        self.x = x
        self.y = y

    def distance_to(self, other):
        """
        Calculate the Euclidean distance between this point and another point.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        """
        Return a string representation of the Point.
        """
        return f"Point(x={self.x}, y={self.y})"

    def __repr__(self):
        """
        Return a formal string representation of the Point.
        """
        return f"Point(x={self.x}, y={self.y})"
    
class Point3D:
    def __init__(self, x=0, y=0, z=0):
        """
        Initialize a 3D Point with x, y, and z coordinates.
        Default coordinates are (0, 0, 0).
        """
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        """
        Calculate the Euclidean distance between this point and another 3D point.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def __str__(self):
        """
        Return a string representation of the 3D Point.
        """
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        """
        Return a formal string representation of the 3D Point.
        """
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        """
        Add two Point3D objects together.
        """
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Subtract one Point3D object from another.
        """
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        """
        Check if two Point3D objects are equal.
        """
        return self.x == other.x and self.y == other.y and self.z == other.z