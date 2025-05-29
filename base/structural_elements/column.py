from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D

class Column3D(Beam3D):
    """
    A Column3D is a special type of Beam3D that is vertical.
    """
    def __init__(self, base: Point3D = Point3D(0,0,0), height: float = 1, cross_sectional_area: float = 0, youngs_modulus: float = 210e9):
        """
        Initialize a 3D Column with a base point, height, cross-sectional area, and Young's modulus.
        """
        end = Point3D(base.x, base.y + height, base.z )
        super().__init__(base, end, cross_sectional_area, youngs_modulus)