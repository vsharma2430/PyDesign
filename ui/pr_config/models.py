from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z
    
    def shift_y(self, offset):
        return Point3D(self.x, self.y + offset, self.z)

class BracePattern(Enum):
    X_Pattern = "X_Pattern"
    V_Pattern = "V_Pattern"

class TierType(Enum):
    Standard = "Standard"
    ElectricalIntrumentation = "ElectricalIntrumentation"
    Flare = "Flare"

@dataclass
class TierConfig:
    elevation: float = 0.0
    tier_type: str = "Standard"
    operating_load: float = -0.4
    wind_load_pos: float = 1.42
    wind_load_neg: float = -1.42
    intermediate_transverse_beam: bool = True
    bracket_provision: bool = False

@dataclass
class FlareConfig:
    position: float = 0.0
    design_load: float = 0.0
    support_member: bool = False

@dataclass
class WalkwayConfig:
    position: float = 0.0

@dataclass
class DuctConfig:
    width: float = 1.2
    height: float = 0.4
    position: float = 0.0

@dataclass
class ElectricTreeConfig:
    position: float = 0.0