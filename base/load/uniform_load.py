from base.load.load import Load
from base.staad_base.load_enum import *
from copy import deepcopy

class UniformLoad(Load):
    def __init__(self, direction: MemberDirection = MemberDirection.Y, force_value: float = -1, 
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
        
    def factor_force_value(self, factor: float):
        load = deepcopy(self)
        load.force_value = self.force_value * factor
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