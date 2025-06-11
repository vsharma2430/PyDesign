from copy import deepcopy
from base.load.load import Load
from base.staad_base.load_enum import *
from base.geometry_base.point import *
from base.geometry_base.line import *

import copy

class NodalLoad(Load):
    def __init__(self, 
                 FX: float = 0.0,  # Force in X direction
                 FY: float = 0.0,  # Force in Y direction
                 FZ: float = 0.0,  # Force in Z direction
                 MX: float = 0.0,  # Moment about X axis
                 MY: float = 0.0,  # Moment about Y axis
                 MZ: float = 0.0,  # Moment about Z axis
                 load_case=LoadCase.OperatingLoad):
        super().__init__(load_case)
        # Store force and moment components
        self.FX = float(FX) if FX is not None else 0.0
        self.FY = float(FY) if FY is not None else 0.0
        self.FZ = float(FZ) if FZ is not None else 0.0
        self.MX = float(MX) if MX is not None else 0.0
        self.MY = float(MY) if MY is not None else 0.0
        self.MZ = float(MZ) if MZ is not None else 0.0

    def set_fx(self, value):
        """Create a new NodalLoad with updated FX value."""
        new_instance = deepcopy(self)
        new_instance.FX = float(value) if value is not None else 0.0
        return new_instance

    def set_fy(self, value):
        """Create a new NodalLoad with updated FY value."""
        new_instance = deepcopy(self)
        new_instance.FY = float(value) if value is not None else 0.0
        return new_instance

    def set_fz(self, value):
        """Create a new NodalLoad with updated FZ value."""
        new_instance = deepcopy(self)
        new_instance.FZ = float(value) if value is not None else 0.0
        return new_instance

    def set_mx(self, value):
        """Create a new NodalLoad with updated MX value."""
        new_instance = deepcopy(self)
        new_instance.MX = float(value) if value is not None else 0.0
        return new_instance

    def set_my(self, value):
        """Create a new NodalLoad with updated MY value."""
        new_instance = deepcopy(self)
        new_instance.MY = float(value) if value is not None else 0.0
        return new_instance

    def set_mz(self, value):
        """Create a new NodalLoad with updated MZ value."""
        new_instance = deepcopy(self)
        new_instance.MZ = float(value) if value is not None else 0.0
        return new_instance

    def get_magnitude(self):
        """Calculate resultant force magnitude."""
        return (self.FX**2 + self.FY**2 + self.FZ**2)**0.5

    def copy(self):
        """Return a deep copy of the NodalLoad object."""
        return deepcopy(self)

    def __str__(self):
        """String representation of the nodal load."""
        return (f"NodalLoad(FX={self.FX:.2f}, FY={self.FY:.2f}, FZ={self.FZ:.2f}, "
                f"MX={self.MX:.2f}, MY={self.MY:.2f}, MZ={self.MZ:.2f}, "
                f"load_case={self.load_case})")

    def __repr__(self):
        """Formal string representation."""
        return self.__str__()