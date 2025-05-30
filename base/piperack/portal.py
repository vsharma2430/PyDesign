from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.structural_elements.column import Column3D
from copy import deepcopy

class PiperackPortal:
    def __init__(self,base:Point3D):
        """
        Initialize a Piperack Portal with empty lists of beams and columns.
        """
        self.base = base
        self.beams = []
        self.columns = []
        self.pedestals = []
        self.walkways = []
        self.ducts = []
        self.trees = []
        self.handrails = []

    def add_beam(self, beam: Beam3D):
        """
        Add a beam to the piperack portal.
        """
        if type(beam) is Beam3D:
            self.beams.append(beam.shift(point=self.base))
        return self

    def add_column(self, column: Column3D):
        """
        Add a column to the piperack portal.
        """
        if type(column) is Column3D:
            self.columns.append(column.shift(point=self.base))
        return self
    
    def add_pedestal(self, column: Column3D):
        """
        Add a column to the piperack portal.
        """
        if type(column) is Column3D:
            self.pedestals.append(column.shift(point=self.base))
        return self
    
    def total_length_of_members(self):
        """
        Calculate the total length of all beams and columns in the piperack portal.
        """
        total_length = 0
        for beam in self.beams:
            total_length += beam.length()
        for column in self.columns:
            total_length += column.length()
        return total_length
    
    def shift(self, point: Point3D):
        new_portal = deepcopy(self)
        
        new_portal.base = self.base.__add__(point)
        new_portal.beams = []
        new_portal.columns = []
        new_portal.pedestals = []
        beam:Beam3D
        for beam in self.beams:
            new_portal.beams.append(beam.shift(point))
            
        column:Column3D
        for column in self.columns:
            new_portal.columns.append(column.shift(point))
        
        pedestal:Column3D
        for pedestal in self.pedestals:
            new_portal.pedestals.append(pedestal.shift(point))

        return new_portal

    def __str__(self):
        """
        Return a string representation of the Piperack Portal.
        """
        return (f"PiperackPortal base={self.base} (beams={len(self.beams)}, columns={len(self.columns)}")

    def __repr__(self):
        """
        Return a formal string representation of the Piperack Portal.
        """
        return (f"PiperackPortal(beams={len(self.beams)}, columns={len(self.columns)}, "
                f"total_length_of_members={self.total_length_of_members():.2f})")