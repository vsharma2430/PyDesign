from base.staad_base.load_enum import *
from base.structural_elements.member import Member

class Load:
    def __init__(self,load_case:LoadCase=LoadCase.OperatingLoad):
        self.load_case = load_case
        pass