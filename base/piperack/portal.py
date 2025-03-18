from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.structural_elements.column import Column3D

class PiperackPortal:
    def __init__(self):
        """
        Initialize a Piperack Portal with empty lists of beams and columns.
        """
        self.beams = []
        self.columns = []
        self.walkways = []
        self.ducts = []
        self.trees = []
        self.handrails = []

    def add_beam(self, beam: Beam3D):
        """
        Add a beam to the piperack portal.
        """
        if type(beam) is Beam3D:
            self.beams.append(beam)
        return self

    def add_column(self, column: Column3D):
        """
        Add a column to the piperack portal.
        """
        if type(column) is Column3D:
            self.columns.append(column)
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
    
    def shift(self, point : Point3D):
        """
        Shift elements by point
        """
        for beam in self.beams:
            beam.shift(point)
        for column in self.columns:
            column.shift(point)
        return self

    def __str__(self):
        """
        Return a string representation of the Piperack Portal.
        """
        return (f"PiperackPortal(beams={len(self.beams)}, columns={len(self.columns)}, "
                f"total_length_of_members={self.total_length_of_members():.2f})")

    def __repr__(self):
        """
        Return a formal string representation of the Piperack Portal.
        """
        return (f"PiperackPortal(beams={len(self.beams)}, columns={len(self.columns)}, "
                f"total_length_of_members={self.total_length_of_members():.2f})")