from base.load.load import Load
from base.staad_base.load_enum import *
from copy import deepcopy

class UniformLoad(Load):
    def __init__(self, direction: MemberDirection = MemberDirection.GY, force_value: float = -1, 
                 d1_value: float = 0, d2_value: float = 0, d3_value: float = 0, 
                 load_case: LoadCase = LoadCase.OperatingLoad):
        """
        Initialize a UniformLoad object representing a uniformly distributed force on a member.
        
        Args:
            direction (MemberDirection): The direction of the force (default: Y).
            force_value (float): The magnitude of the force per unit length (default: -1).
            d1_value (float): Start position or parameter 1 for load application (default: 0).
            d2_value (float): End position or parameter 2 for load application (default: 0).
            d3_value (float): Additional parameter for load application (default: 0).
            load_case (LoadCase): The load case for this load (default: OperatingLoad).
        """
        super().__init__(load_case=load_case)  # Pass load_case to base class
        self.direction = direction
        self.force_value = force_value
        self.d1_value = d1_value
        self.d2_value = d2_value
        self.d3_value = d3_value

    def set_force_value(self, force_value: float):
        load = deepcopy(self)
        load.force_value = force_value
        return load
    
    def factor_force_value(self, factor: float):
        load = deepcopy(self)
        load.force_value = self.force_value * factor
        return load
    
    def set_force_direction(self, direction: MemberDirection):
        load = deepcopy(self)
        load.direction = direction
        return load
        
    def __str__(self) -> str:
        """
        Return a string representation of the UniformLoad object.
        
        Returns:
            str: A string describing the uniform load's direction, force value, position parameters, and load case.
        """
        return (f"UniformLoad(direction={self.direction.name}, "
                f"force={self.force_value}, "
                f"d1={self.d1_value}, d2={self.d2_value}, d3={self.d3_value}, "
                f"load_case={self.load_case.name})")
    
    def to_markdown(self) -> str:
            """
            Generate a detailed Markdown table representation of the UniformLoad object.
            
            Returns:
                str: A string containing a Markdown table with load details.
            """
            markdown = "| Property | Value |\n"
            markdown += "|----------|-------|\n"
            markdown += f"| Type | UniformLoad |\n"
            markdown += f"| Direction | {self.direction.name} |\n"
            markdown += f"| Force Value | {self.force_value:.3f} |\n"
            markdown += f"| D1 | {self.d1_value:.3f} |\n"
            markdown += f"| D2 | {self.d2_value:.3f} |\n"
            markdown += f"| D3 | {self.d3_value:.3f} |\n"
            markdown += f"| Load Case | {self.load_case.name} |\n"
            return markdown
        
    def to_markdown_compact(self) -> str:
            """
            Generate a compact single-line representation for table cells.
            
            Returns:
                str: Compact load description.
            """
            return f"Uniform({self.direction.name}, F={self.force_value:.2f}/m, d1={self.d1_value:.2f}-{self.d2_value:.2f})"