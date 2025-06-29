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
    def __init__(self, x=0, y=0, z=0,tuple_pt=None):
        """
        Initialize a 3D Point with x, y, and z coordinates.
        Default coordinates are (0, 0, 0).
        """
        self.x = x
        self.y = y
        self.z = z

        if(tuple_pt):
            self.x = tuple_pt[0]
            self.y = tuple_pt[1]
            self.z = tuple_pt[2]
            
    def __round__(self, n_digits=3):
        return Point3D(round(self.x,ndigits=n_digits),round(self.y,ndigits=n_digits),round(self.z,ndigits=n_digits))

    def distance_to(self, other,n_digits=3):
        """
        Calculate the Euclidean distance between this point and another 3D point.
        """
        return round(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2),ndigits=n_digits)
    
    def shift_y(self, y,n_digits=3):
        """
        Calculate the Euclidean distance between this point and another 3D point.
        """
        return Point3D(round(self.x,ndigits=n_digits),round(y,ndigits=n_digits),round(self.z,ndigits=n_digits))
    
    def shift_x(self, x,n_digits=3):
        """
        Calculate the Euclidean distance between this point and another 3D point.
        """
        return Point3D(round(x,ndigits=n_digits),round(self.y,ndigits=n_digits),round(self.z,ndigits=n_digits))
    
    def shift_z(self, z,n_digits=3):
        """
        Calculate the Euclidean distance between this point and another 3D point.
        """
        return Point3D(round(self.x,ndigits=n_digits),round(self.y,ndigits=n_digits),round(z,ndigits=n_digits))

    def __str__(self):
        """
        Return a string representation of the 3D Point.
        """
        return f"{self.x} , {self.y} , {self.z}"

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
    
    def mid(self, other):
        """
        Mid of two Point3D objects.
        """
        return Point3D((self.x + other.x)/2, (self.y + other.y)/2, (self.z + other.z)/2)

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
    
    def eq_x(self, other):
        """
        Check if two Point3D objects are equal x.
        """
        if(isinstance(other,Point3D)):
            return self.x == other.x
        else:
            return self.x == other
    
    def eq_y(self, other):
        """
        Check if two Point3D objects are equal.
        """
        if(isinstance(other,Point3D)):
            return round(self.y,3) == round(other.y,3)
        else:
            return self.y == other
    
    def eq_z(self, other):
        """
        Check if two Point3D objects are equal.
        """
        if(isinstance(other,Point3D)):
            return self.z == other.z
        else:
            return self.z == other
        
    def tuple_ref(self):
        return (self.x,self.y,self.z)