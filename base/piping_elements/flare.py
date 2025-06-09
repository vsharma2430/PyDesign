from typing import List, Optional
from base.geometry_base.point import Point3D
from base.geometry_base.line import Line3D
from base.load.conc_load import ConcentratedLoad, LoadCase
from base.load.uniform_load import UniformLoad
from base.piping_elements.pipe import Pipe  # Importing the updated Pipe class

class Flare(Pipe):
    """A flare pipe element in 3D space with flare-specific properties."""
    
    def __init__(self, 
                 lines: List[Line3D], 
                 diameter: float = 50,
                 thickness: float = 10,
                 material_density: float = 7850,  # kg/m³, default steel
                 name: Optional[str] = None,
                 support_member: bool = False):
        """
        Initialize a flare pipe with a list of Line3D segments and flare-specific properties.
        
        Args:
            lines: List of Line3D objects representing the flare pipe's segments
            diameter: Outer diameter of the pipe (m)
            thickness: Wall thickness of the pipe (m)
            material_density: Material density (kg/m³)
            name: Optional identifier for the flare
            support_member: Indicates if the flare acts as a support member
        """
        super().__init__(lines, diameter, thickness, material_density, name)
        self.support_member = support_member