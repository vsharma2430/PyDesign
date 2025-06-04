from enum import IntEnum
from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.structural_elements.column import Column3D
from base.piperack.portal import PiperackPortal
from copy import deepcopy

class PiperackMembers(IntEnum):
    TierBeams = 0
    Columns = 1
    Pedestals = 2
    LongitudinalBeams = 3
    VerticalBracing = 4
    PlanBracing = 5
    Stubs = 6
    IntermediateTransverseBeams = 7
    IntermediateLongitudinalBeams = 8 
    FlareSupportMembers = 9
    DuctSupportMembers = 10
    TreeSupportMembers = 11
    WWSupportMembers = 12
    BracketBeams = 13
    BracketBraces = 14

class Piperack:
    def __init__(self,base:Point3D,portals:list = [],longitudinal_beams:list = []):
        self.base = base
        self.portals = portals
        self.longitudinal_beams = longitudinal_beams
        
    def add_longitudinal_beam(self,beam:Beam3D):
        self.longitudinal_beams.append(beam)
        
    def add_portals(self,portal:PiperackPortal):
        self.portals.append(portal)