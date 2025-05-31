from base.structural_elements.member import Member
from base.geometry_base.point import Point3D

class Node(Member):
    def __init__(self,node_id:int,point:Point3D,is_support : bool = False):
        self.node_id = node_id
        self.point = point
        self.is_support = is_support
        
    def set_id(self, node_id: int) -> None:
        """
        Set a unique identifier for the node.
        
        Args:
            node_id (int): Unique identifier for the node
        """
        self.node_id = node_id
        
    def __str__(self) -> str:
        """
        String representation of the node.
        
        Returns:
            str: Node information including position and support status
        """
        return (f"Node(id={self.node_id}, point={self.point}, "
                f"is_support={self.is_support}")
        