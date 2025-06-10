import math
from copy import deepcopy
from base.structural_elements.member import Member
from base.geometry_base.point import Point3D
from base.geometry_base.line import Line3D

class Beam3D(Member):
    def __init__(self,start: Point3D = Point3D(), end: Point3D = Point3D(1,0,0), id:int =-1, 
                profile:str = '', cross_sectional_area: float = 0.0, youngs_modulus: float = 210e9,weight_per_meter : float = 0):
        """
        Initialize a 3D Beam with start and end points, cross-sectional area, and Young's modulus.
        """
        self.id = id
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
        return Line3D(self.start,self.end).length()
    
    def get_line(self):
        """
        Calculate the direction vector of the 3D beam.
        Returns a tuple (dx, dy, dz) representing the direction.
        """
        return Line3D(self.start,self.end)

    def direction_vector(self):
        """
        Calculate the direction vector of the 3D beam.
        Returns a tuple (dx, dy, dz) representing the direction.
        """
        return Line3D(self.start,self.end).direction_vector()

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
        beam = deepcopy(self)
        beam.start = self.start.__add__(point)
        beam.end = self.end.__add__(point)
        return beam
    
    def shift_to_y(self,y):
        self.start.y = y
        self.end.y = y
        return self
    
    def shift_to_x(self,x):
        self.start.x = x
        self.end.x = x
        return self
        
    def mid(self) -> Point3D:
        return self.start.mid(self.end)

    def __str__(self):
        """
        Return a string representation of the 3D Beam.
        """
        return (f"Beam(start={self.start}, end={self.end},")

    def __repr__(self):
        """
        Return a formal string representation of the 3D Beam.
        """
        return (f"Beam(start={self.start}, end={self.end}, "
                f"Profile={self.profile}, ")
        
beams_sorted_yzx = lambda beams : sorted(beams, key=lambda beam: (beam.start.y, beam.start.z, beam.start.x))
beams_sorted_yxz = lambda beams : sorted(beams, key=lambda beam: (beam.start.y, beam.start.x, beam.start.z))

def group_beams_by_y(beams):
    groups = {}
    for beam in beams:
        y = beam.start.y
        if y not in groups:
            groups[y] = []
        groups[y].append(beam)
    return groups