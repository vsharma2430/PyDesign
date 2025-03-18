import math
from base.geometry_base.point import Point3D

class Beam3D:
    def __init__(self, start: Point3D = Point3D(), end: Point3D = Point3D(1,0,0), 
                profile:str = '', cross_sectional_area: float = 0.0, youngs_modulus: float = 210e9,weight_per_meter : float = 0):
        """
        Initialize a 3D Beam with start and end points, cross-sectional area, and Young's modulus.
        """
        self.start = start
        self.end = end
        self.profile = profile
        self.cross_sectional_area = cross_sectional_area
        self.youngs_modulus = youngs_modulus
        self.weight_per_meter = weight_per_meter

    def length(self):
        """
        Calculate the length of the 3D beam using the Euclidean distance formula.
        """
        return math.sqrt(
            (self.end.x - self.start.x)**2 +
            (self.end.y - self.start.y)**2 +
            (self.end.z - self.start.z)**2
        )

    def direction_vector(self):
        """
        Calculate the direction vector of the 3D beam.
        Returns a tuple (dx, dy, dz) representing the direction.
        """
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        dz = self.end.z - self.start.z
        return (dx, dy, dz)

    def stress(self, force: float):
        """
        Calculate the stress in the beam under a given axial force.
        Stress = Force / Cross-sectional area.
        """
        if self.cross_sectional_area == 0:
            raise ValueError("Cross-sectional area cannot be zero.")
        return force / self.cross_sectional_area

    def strain(self, force: float):
        """
        Calculate the strain in the beam under a given axial force.
        Strain = Stress / Young's modulus.
        """
        stress = self.stress(force)
        return stress / self.youngs_modulus

    def shift(self, point : Point3D):
        """
        Shift start and end point by point
        """
        self.start = self.start.__add__(point)
        self.end = self.end.__add__(point)
        return self

    def __str__(self):
        """
        Return a string representation of the 3D Beam.
        """
        return (f"Beam(start={self.start}, end={self.end}, "
                f"cross_sectional_area={self.cross_sectional_area}, "
                f"youngs_modulus={self.youngs_modulus})")

    def __repr__(self):
        """
        Return a formal string representation of the 3D Beam.
        """
        return (f"Beam(start={self.start}, end={self.end}, "
                f"Profile={self.profile}, "
                f"cross_sectional_area={self.cross_sectional_area}, "
                f"youngs_modulus={self.youngs_modulus})")