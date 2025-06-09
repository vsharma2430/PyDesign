from typing import List, Optional
from base.geometry_base.point import Point3D
from base.geometry_base.line import Line3D
from base.load.conc_load import ConcentratedLoad, LoadCase
from base.load.uniform_load import UniformLoad

class Pipe:
    """A pipe element in 3D space with structural properties and load handling, composed of Line3D segments."""
    
    def __init__(self, 
                 lines: List[Line3D], 
                 diameter: float,
                 thickness: float,
                 material_density: float = 7850,  # kg/m³, default steel
                 name: Optional[str] = None):
        """
        Initialize a pipe with a list of Line3D segments and material properties.
        
        Args:
            lines: List of Line3D objects representing the pipe's segments
            diameter: Outer diameter of the pipe (m)
            thickness: Wall thickness of the pipe (m)
            material_density: Material density (kg/m³)
            name: Optional identifier for the pipe
        """
        if not lines:
            raise ValueError("Pipe must contain at least one Line3D segment")
        self.lines = lines  # List of Line3D objects
        self.diameter = diameter
        self.thickness = thickness
        self.material_density = material_density
        self.name = name
        self.loads: List[ConcentratedLoad | UniformLoad] = []
        
        if diameter <= 0:
            raise ValueError("Diameter must be positive")
        if thickness <= 0 or thickness > diameter/2:
            raise ValueError("Invalid thickness value")
    
    @property
    def cross_sectional_area(self) -> float:
        """Calculate the cross-sectional area of the pipe (m²)."""
        outer_radius = self.diameter / 2
        inner_radius = outer_radius - self.thickness
        return 3.14159 * (outer_radius**2 - inner_radius**2)
    
    @property
    def weight_per_unit_length(self) -> float:
        """Calculate the weight per unit length (N/m)."""
        return self.cross_sectional_area * self.material_density * 9.81
    
    def add_concentrated_load(self, load: ConcentratedLoad) -> None:
        """Add a concentrated load to the pipe."""
        if isinstance(load, ConcentratedLoad):
            self.loads.append(load)
    
    def add_uniform_load(self, load: UniformLoad) -> None:
        """Add a uniform load to the pipe."""
        if isinstance(load, UniformLoad):
            self.loads.append(load)
    
    def get_total_load(self, load_case: LoadCase) -> float:
        """Calculate total load magnitude for a specific load case across all segments."""
        total = 0.0
        for load in self.loads:
            if load.load_case == load_case:
                if isinstance(load, ConcentratedLoad):
                    total += abs(load.force_value)
                elif isinstance(load, UniformLoad):
                    # Use the segment length if d1_value and d2_value are not specified
                    length = abs(load.d2_value - load.d1_value) or self.length
                    total += abs(load.force_value) * length
        return total
    
    @property
    def length(self) -> float:
        """Calculate the total length of the pipe by summing segment lengths (m)."""
        return sum(line.start.distance_to(line.end) for line in self.lines)