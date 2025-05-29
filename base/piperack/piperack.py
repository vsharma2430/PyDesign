from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.structural_elements.column import Column3D
from base.piperack.portal import PiperackPortal
from copy import deepcopy

class Piperack:
    def __init__(self,base:Point3D,portals:list = [],longitudinal_beams:list = []):
        self.base = base
        self.portals = portals
        self.longitudinal_beams = longitudinal_beams
        
    def add_longitudinal_beam(self,beam:Beam3D):
        self.longitudinal_beams.append(beam)
        
    def add_portals(self,portal:PiperackPortal):
        self.portals.append(portal)