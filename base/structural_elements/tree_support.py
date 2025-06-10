from typing import List, Optional
from base.geometry_base.line import Line3D
from base.staad_base.load_enum import MemberDirection
from base.load.conc_load import ConcentratedLoad, LoadCase
from base.load.uniform_load import UniformLoad
from base.structural_elements.beam import Beam3D

class TreeSupportMember:
    """A class representing a tree support member with geometric and structural properties.

    Attributes:
        line3d (Line3D): The 3D line representing the support member's geometry.
        support_member (bool): Indicates if the member is a support member. Defaults to False.
        tree_to_tree_distance (float): Distance between connected trees in meters. Defaults to 0.0.
        tree_load (float): Load applied by the tree in Newtons. Defaults to 0.0.
    """
    def __init__(
        self,
        line: Line3D,
        support_member: bool = True,
        max_tree_to_tree_distance: float = 3.0,
        tree_load: float = 2.8,
        members: List[Beam3D] = []
    ) -> None:
        """Initialize a TreeSupportMember with validation.

        Args:
            line3d (Line3D): The 3D line representing the support member.
            support_member (bool): Whether it is a support member. Defaults to False.
            tree_to_tree_distance (float): Distance between trees in meters. Defaults to 0.0.
            tree_load (float): Load applied by the tree in Newtons. Defaults to 0.0.

        Raises:
            TypeError: If line3d is not a Line3D instance or support_member is not a boolean.
            ValueError: If tree_to_tree_distance or tree_load is negative.
        """
        if not isinstance(line, Line3D):
            raise TypeError("line3d must be an instance of Line3D")
        if not isinstance(support_member, bool):
            raise TypeError("support_member must be a boolean")
        if max_tree_to_tree_distance < 0:
            raise ValueError("tree_to_tree_distance cannot be negative")
        if tree_load < 0:
            raise ValueError("tree_load cannot be negative")

        self.line = line
        self.support_member = support_member
        self.tree_to_tree_distance = max_tree_to_tree_distance
        self.tree_load = tree_load
        self.members = members if members else []

    def __repr__(self) -> str:
        """Return a string representation of the TreeSupportMember."""
        return (f"TreeSupportMember(line3d={self.line}, support_member={self.support_member}, "
                f"tree_to_tree_distance={self.tree_to_tree_distance:.2f}m, "
                f"tree_load={self.tree_load:.2f}N)")

    def calculate_member_length(self) -> float:
        """Calculate the length of the support member based on its 3D line.

        Returns:
            float: The length of the support member in meters.
        """
        return self.line.length()

    def update_load(self, new_load: float) -> None:
        """Update the tree load with validation.

        Args:
            new_load (float): The new load value in Newtons.

        Raises:
            ValueError: If new_load is negative.
        """
        if new_load < 0:
            raise ValueError("new_load cannot be negative")
        self.tree_load = new_load

    def adjust_distance(self, new_distance: float) -> None:
        """Adjust the tree-to-tree distance with validation.

        Args:
            new_distance (float): The new distance between trees in meters.

        Raises:
            ValueError: If new_distance is negative.
        """
        if new_distance < 0:
            raise ValueError("new_distance cannot be negative")
        self.tree_to_tree_distance = new_distance

    def get_tree_load(self):
        return ConcentratedLoad(force_value=self.tree_load*-1,load_case=LoadCase.DeadLoadElecIns)

    def add_member(self, member: Beam3D) -> None:
        """Add a single Beam3D member to the flare."""
        if not isinstance(member, Beam3D):
            raise TypeError("Member must be a Beam3D instance")
        self.members.append(member)

    def add_members(self, members: List[Beam3D]) -> None:
        """Add multiple Beam3D members to the flare."""
        if not all(isinstance(m, Beam3D) for m in members):
            raise TypeError("All members must be Beam3D instances")
        self.members.extend(members)