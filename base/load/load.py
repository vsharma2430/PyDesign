from enum import IntEnum
from base.structural_elements.member import Member

class LoadCase(IntEnum):
    OperatingLoad = 401
    EmptyLoad = 301

class Load:
    def __init__(self,load_case:LoadCase=101,members:list[Member]=None):
        self.load_case = load_case
        self.member = []
        pass