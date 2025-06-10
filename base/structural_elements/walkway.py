from typing import List, Optional
from base.geometry_base.point import Point3D
from base.geometry_base.line import Line3D
from base.structural_elements.beam import Beam3D
from base.staad_base.load_enum import MemberDirection
from base.load.conc_load import ConcentratedLoad, LoadCase
from base.load.uniform_load import UniformLoad

class SteelWalkway:
    def __init__(self, edge_line: Line3D, width: float=0.8, thickness: float=0.25, material_type: str='steel', load_capacity: float=0.3):
        """
        Initialize a SteelWalkway.
        
        Args:
            edge_line (Line3D): The centerline of the walkway in 3D space.
            width (float): Width of the walkway in meters.
            thickness (float): Thickness of the walkway in meters.
            material_type (str): Type of steel (e.g., 'A36', 'Stainless').
            load_capacity (float): Maximum load capacity in T/m^2.
        """
        self.edge_line = edge_line
        self.width = width
        self.thickness = thickness
        self.material_type = material_type
        self.load_capacity = load_capacity
        self.members = []

    def length(self) -> float:
        """Return the length of the walkway based on the edge_line."""
        return self.edge_line.length()
    
    def get_member_lines(self) -> List[Line3D]:
        return [self.edge_line,self.edge_line.shift(Point3D(self.width,0,0))]
    
    def get_uniform_load(self):
        return UniformLoad(direction= MemberDirection.GY,force_value=-1*self.width*self.load_capacity*0.5,load_case=LoadCase.LiveLoad)
    
    def add_member(self,member):
        if(isinstance(member,Beam3D)):
            self.members.append(member)

    def add_members(self,members):
        self.members.extend(members)

    def __str__(self) -> str:
        """String representation of the SteelWalkway."""
        return (f"SteelWalkway(length={self.length():.2f}m, width={self.width:.2f}m")