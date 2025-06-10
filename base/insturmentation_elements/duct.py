from typing import List, Optional
from base.geometry_base.point import Point3D
from base.geometry_base.line import Line3D
from base.staad_base.load_enum import MemberDirection
from base.load.conc_load import ConcentratedLoad, LoadCase
from base.load.uniform_load import UniformLoad
from base.structural_elements.beam import Beam3D

class Cable:
    def __init__(self, name: str, diameter: float, length: float):
        """
        Represents a cable or wire.
        - name: Name/identifier of the cable.
        - diameter: Diameter of the cable in millimeters.
        - length: Length of the cable in meters.
        """
        self.name = name
        self.diameter = diameter
        self.length = length

    def __str__(self):
        return f"Cable(name={self.name}, diameter={self.diameter}mm, length={self.length}m)"

    def __repr__(self):
        return f"Cable(name={self.name}, diameter={self.diameter}mm, length={self.length}m)"


class InstrumentationDuct:
    # Weight lookup table based on provided data (width x height -> T/m)
    WEIGHT_TABLE = {
        (1.2, 0.4): 0.800,
        (1.0, 0.4): 0.650,
        (0.8, 0.3): 0.400,
        (0.6, 0.3): 0.320,
        (0.4, 0.2): 0.130
    }

    def __init__(
        self,
        width: float,
        height: float,
        material: str = "steel",
        edge_line: Optional[Line3D] = None,
        members: List[Beam3D] = []
    ):
        """
        Represents an instrumentation duct with loads and edge line.
        - width: Width of the duct in millimeters.
        - height: Height of the duct in millimeters.
        - material: Material of the duct (e.g., 'steel', 'aluminum').
        - edge_line: Line3D object representing the duct's centerline.
        """
        self.width = width  # mm
        self.height = height  # mm
        self.material = material
        self.cables: List[Cable] = []
        self.loads: List[UniformLoad] = []  # Store UniformLoad objects
        # Initialize edge_line; default to a 1-meter line along z-axis if None
        self.edge_line = edge_line if edge_line else Line3D(
            Point3D(0, 0, 0),
            Point3D(0, 0, 1000)  # Default 1 meter (1000 mm)
        )
        self.members = members

    def get_weight(self) -> float:
        """Retrieve weight (kg/m) for the duct size from the weight table."""
        size = (self.width, self.height)
        if size in self.WEIGHT_TABLE:
            return self.WEIGHT_TABLE[size]
        raise ValueError(f"No weight data available for duct size {size}")

    def get_uniform_load(self):
        return UniformLoad(direction= MemberDirection.GY,force_value=-1*self.get_weight()*0.5,load_case=LoadCase.LiveLoad)
    
    def calculate_length(self) -> float:
        """
        Calculate the length of the duct's centerline in meters.
        """
        return self.edge_line.length() / 1000  # Convert mm to meters

    def add_cable(self, cable: Cable):
        """
        Add a cable to the duct and create a corresponding UniformLoad.
        - cable: Cable object with diameter and weight_per_meter.
        """
        self.cables.append(cable)
        # Calculate cable weight per meter (N/m) = weight_per_meter (kg/m) * g (9.81 m/s²)
        cable_force = cable.weight_per_meter * 9.81
        # Assume cable weight acts downward (Y-direction) as a uniform load
        cable_load = UniformLoad(
            direction=MemberDirection.Y,
            force_value=-cable_force,  # Negative for downward force
            load_case=LoadCase.DeadLoad
        )
        self.loads.append(cable_load)

    def add_external_load(self, load: UniformLoad):
        """
        Add an external uniform load to the duct.
        - load: UniformLoad object representing the load.
        """
        self.loads.append(load)

    def total_load(self) -> float:
        """
        Calculate the total load on the duct in Newtons over its length.
        Sums force_value (N/m) * length (m) for all loads.
        """
        return sum(load.get_force() * self.calculate_length() for load in self.loads)

    def set_edge_line(self, edge_line: Line3D):
        """
        Update the duct's centerline.
        - edge_line: Line3D object representing the new centerline.
        """
        self.edge_line = edge_line

    def get_member_lines(self) -> List[Line3D]:
        return [self.edge_line,self.edge_line.shift(Point3D(self.width,0,0))]
    
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