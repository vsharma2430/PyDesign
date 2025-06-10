from typing import List, Optional
from base.geometry_base.point import Point3D
from base.geometry_base.line import Line3D
from base.load.conc_load import ConcentratedLoad, LoadCase
from base.load.uniform_load import UniformLoad
from base.piping_elements.pipe import Pipe  # Importing the updated Pipe class
from base.structural_elements.beam import Beam3D

class Flare(Pipe):
    """A flare pipe element in 3D space with flare-specific properties."""
    
    def __init__(self, 
                 lines: List[Line3D], 
                 diameter: float = 0.5,  # Default: 0.5 m (500 mm)
                 thickness: float = 0.01,  # Default: 10 mm
                 design_load: float = 1.0,  # in T/m (tonnes per meter)
                 material_density: float = 7850,  # kg/m³, default steel
                 name: Optional[str] = None,
                 support_member: bool = False,
                 members: List[Beam3D] = []
                 ):
        """
        Initialize a flare pipe with a list of Line3D segments and flare-specific properties.
        
        Args:
            lines: List of Line3D objects representing the flare pipe's segments
            diameter: Outer diameter of the pipe (m)
            thickness: Wall thickness of the pipe (m)
            design_load: Design load per unit length (T/m)
            material_density: Material density (kg/m³)
            name: Optional identifier for the flare
            support_member: Indicates if the flare acts as a support member
            members: List of Beam3D objects representing structural members
        """
        super().__init__(lines, diameter, thickness, design_load, material_density, name)
        self.support_member = support_member
        if members and not all(isinstance(m, Beam3D) for m in members):
            raise TypeError("All members must be Beam3D instances")
        self.members = members if members else []

    def add_member(self, member: Beam3D) -> None:
        """Add a single Beam3D member to the flare."""
        if not isinstance(member, Beam3D):
            raise TypeError("Member must be a Beam3D instance")
        self.members.append(member)

    def add_members(self, members: List[Beam3D]) -> None:
        """Add multiple Beam3D members to the flare."""
        if not all(isinstance(m, Beam3D) for m in members):
            raise TypeError("All members must be Beam3D instances")
        self.members.extend(members)