from typing import List, Optional
from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.structural_elements.column import Column3D
from copy import deepcopy

class PiperackPortal:
    """A class representing a piperack portal structure with beams, columns, and other structural elements.

    Attributes:
        base (Point3D): The base point of the piperack portal in 3D space.
        beams (List[Beam3D]): List of beams in the portal.
        columns (List[Column3D]): List of columns in the portal.
        pedestals (List[Column3D]): List of pedestal columns in the portal.
        walkways (List): List of walkways (placeholder for future implementation).
        ducts (List): List of ducts (placeholder for future implementation).
        trees (List): List of trees (placeholder for future implementation).
        handrails (List): List of handrails (placeholder for future implementation).
    """

    def __init__(self, base: Point3D):
        """Initialize a Piperack Portal with a base point.

        Args:
            base (Point3D): The base point for the portal in 3D space.

        Raises:
            TypeError: If base is not a Point3D object.
        """
        if not isinstance(base, Point3D):
            raise TypeError("Base must be a Point3D object")
        self.base :Point3D = base
        self.beams: List[Beam3D] = []
        self.columns: List[Column3D] = []
        self.pedestals: List[Column3D] = []
        self.walkways: List = []
        self.ducts: List = []
        self.trees: List = []
        self.handrails: List = []

    def add_beam(self, beam: Beam3D) -> 'PiperackPortal':
        """Add a beam to the piperack portal.

        Args:
            beam (Beam3D): The beam to add, shifted relative to the portal's base.

        Returns:
            PiperackPortal: Self, for method chaining.

        Raises:
            TypeError: If beam is not a Beam3D object.
        """
        if not isinstance(beam, Beam3D):
            raise TypeError("Beam must be a Beam3D object")
        self.beams.append(beam.shift(point=self.base))
        return self

    def add_column(self, column: Column3D) -> 'PiperackPortal':
        """Add a column to the piperack portal.

        Args:
            column (Column3D): The column to add, shifted relative to the portal's base.

        Returns:
            PiperackPortal: Self, for method chaining.

        Raises:
            TypeError: If column is not a Column3D object.
        """
        if not isinstance(column, Column3D):
            raise TypeError("Column must be a Column3D object")
        self.columns.append(column.shift(point=self.base))
        return self

    def add_pedestal(self, pedestal: Column3D) -> 'PiperackPortal':
        """Add a pedestal column to the piperack portal.

        Args:
            pedestal (Column3D): The pedestal column to add, shifted relative to the portal's base.

        Returns:
            PiperackPortal: Self, for method chaining.

        Raises:
            TypeError: If pedestal is not a Column3D object.
        """
        if not isinstance(pedestal, Column3D):
            raise TypeError("Pedestal must be a Column3D object")
        self.pedestals.append(pedestal.shift(point=self.base))
        return self

    def total_length_of_members(self) -> float:
        """Calculate the total length of all beams, columns, and pedestals in the portal.

        Returns:
            float: The total length of all structural members.
        """
        total_length = sum(
            beam.length() for beam in self.beams
        ) + sum(
            column.length() for column in self.columns
        ) + sum(
            pedestal.length() for pedestal in self.pedestals
        )
        return total_length

    def shift(self, point: Point3D) -> 'PiperackPortal':
        """Create a new PiperackPortal shifted by the specified point.

        Args:
            point (Point3D): The point to shift the portal by.

        Returns:
            PiperackPortal: A new PiperackPortal instance with shifted coordinates.

        Raises:
            TypeError: If point is not a Point3D object.
        """
        if not isinstance(point, Point3D):
            raise TypeError("Point must be a Point3D object")
        
        new_portal = deepcopy(self)
        new_portal.base = self.base.__add__(point)
        
        new_portal.beams = [beam.shift(point) for beam in self.beams]
        new_portal.columns = [column.shift(point) for column in self.columns]
        new_portal.pedestals = [pedestal.shift(point) for pedestal in self.pedestals]
        new_portal.walkways = deepcopy(self.walkways)  # Placeholder for future implementation
        new_portal.ducts = deepcopy(self.ducts)
        new_portal.trees = deepcopy(self.trees)
        new_portal.handrails = deepcopy(self.handrails)
        
        return new_portal

    def get_member_count(self) -> dict:
        """Get the count of each type of structural member.

        Returns:
            dict: A dictionary with counts of beams, columns, and pedestals.
        """
        return {
            "beams": len(self.beams),
            "columns": len(self.columns),
            "pedestals": len(self.pedestals),
            "walkways": len(self.walkways),
            "ducts": len(self.ducts),
            "trees": len(self.trees),
            "handrails": len(self.handrails)
        }

    def clear_members(self, member_type: Optional[str] = None) -> 'PiperackPortal':
        """Clear specified member types or all members from the portal.

        Args:
            member_type (Optional[str]): The type of member to clear ('beams', 'columns', 'pedestals', etc.).
                                        If None, clears all members.

        Returns:
            PiperackPortal: Self, for method chaining.

        Raises:
            ValueError: If member_type is provided but invalid.
        """
        valid_member_types = {"beams", "columns", "pedestals", "walkways", "ducts", "trees", "handrails"}
        
        if member_type is None:
            self.beams.clear()
            self.columns.clear()
            self.pedestals.clear()
            self.walkways.clear()
            self.ducts.clear()
            self.trees.clear()
            self.handrails.clear()
        elif member_type in valid_member_types:
            getattr(self, member_type).clear()
        else:
            raise ValueError(f"Invalid member_type. Must be one of {valid_member_types}")
        
        return self

    def __str__(self) -> str:
        """Return a string representation of the Piperack Portal.

        Returns:
            str: Informal string representation of the portal.
        """
        return (f"PiperackPortal(base={self.base}, "
                f"beams={len(self.beams)}, columns={len(self.columns)}, pedestals={len(self.pedestals)})")

    def __repr__(self) -> str:
        """Return a formal string representation of the Piperack Portal.

        Returns:
            str: Formal string representation of the portal.
        """
        return (f"PiperackPortal(base={self.base}, beams={len(self.beams)}, "
                f"columns={len(self.columns)}, pedestals={len(self.pedestals)}, "
                f"total_length={self.total_length_of_members():.2f})")