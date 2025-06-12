from base.load.load import Load
from base.staad_base.load_enum import *
from base.geometry_base.point import *
from base.geometry_base.line import *

class ConcentratedLoad(Load):
    """
    Represents a concentrated force applied to a beam member at a specific point.

    Args:
        direction (MemberDirection): The direction of the applied force.
        force_value (float): The magnitude of the force (positive or negative).
        global_apply_point (Point3D): The 3D point where the load is applied.
        d1_value (float): First positional parameter for load application.
        d2_value (float): Second positional parameter for load application.
        load_case (LoadCase): The load case category (default: OperatingLoad).
    """
    def __init__(
        self,
        direction : MemberDirection = MemberDirection.Y,
        force_value: float = -1.0,
        global_apply_point: Point3D = Point3D(0, 0, 0),
        d1_value: float = 0.0,
        d2_value: float = 0.0,
        load_case: LoadCase = LoadCase.OperatingLoad
    ) -> None:

        self.direction: MemberDirection = direction
        self.force_value: float = force_value
        self.global_apply_point: Point3D = global_apply_point
        self.d1_value: float = d1_value
        self.d2_value: float = d2_value
        self.load_case: LoadCase = load_case

        self._validate_inputs()

    def set_global_apply_point(self, point: Point3D):
        """
        Set the global application point for the concentrated load.

        Args:
            point (Point3D): The 3D point where the load is applied.

        Raises:
            TypeError: If point is not a Point3D instance.
        """
        if not isinstance(point, Point3D):
            raise TypeError(f"Global apply point must be a Point3D, got {type(point)}")
        load = deepcopy(self)
        load.global_apply_point = point
        return load

    def set_force_value(self, force_value: float):
        """
        Set the force value for the concentrated load.

        Args:
            force_value (float): The magnitude of the force (positive or negative).

        Raises:
            TypeError: If force_value is not a number.
        """
        if not isinstance(force_value, (int, float)):
            raise TypeError(f"Force value must be a number, got {type(force_value)}")
        load = deepcopy(self)
        load.force_value = float(force_value)
        return load

    def set_direction(self, direction: MemberDirection):
        """
        Set the direction of the concentrated load.

        Args:
            direction (MemberDirection): The direction of the applied force.

        Raises:
            TypeError: If direction is not a MemberDirection enum.
        """
        if not isinstance(direction, MemberDirection):
            raise TypeError(f"Direction must be a MemberDirection enum, got {type(direction)}")
        load = deepcopy(self)
        load.direction = direction
        return load

    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if not isinstance(self.direction, MemberDirection):
            raise TypeError(f"Direction must be a MemberDirection enum, got {type(self.direction)}")
        if not isinstance(self.force_value, (int, float)):
            raise TypeError(f"Force value must be a number, got {type(self.force_value)}")
        if not isinstance(self.global_apply_point, Point3D):
            raise TypeError(f"Global apply point must be a Point3D, got {type(self.global_apply_point)}")
        if not isinstance(self.d1_value, (int, float)) or not isinstance(self.d2_value, (int, float)):
            raise TypeError("d1_value and d2_value must be numbers")
        if not isinstance(self.load_case, LoadCase):
            raise TypeError(f"Load case must be a LoadCase enum, got {type(self.load_case)}")
        
        # Ensure non-negative positional parameters if required by context
        if self.d1_value < 0 or self.d2_value < 0:
            raise ValueError("Positional parameters d1_value and d2_value must be non-negative")

    def __str__(self) -> str:
        """Return a string representation of the concentrated load."""
        return (f"ConcentratedLoad(direction={self.direction}, force={self.force_value}, "
                f"point={self.global_apply_point}, d1={self.d1_value}, d2={self.d2_value}, "
                f"load_case={self.load_case})")

    def set_d1_from_global_point(self,line:Line3D):
        if(line.contains_point(self.global_apply_point)):
            self.d1_value = line.start.distance_to(self.global_apply_point)
            return True
        else:
            return False
        
    def set_d1(self, d1:float):
        load = deepcopy(self)
        load.d1_value = d1
        return load
    
    def to_markdown(self) -> str:
        """
        Generate a detailed Markdown table representation of the ConcentratedLoad object.
        
        Returns:
            str: A string containing a Markdown table with load details.
        """
        markdown = "| Property | Value |\n"
        markdown += "|----------|-------|\n"
        markdown += f"| Type | ConcentratedLoad |\n"
        markdown += f"| Direction | {self.direction.name} |\n"
        markdown += f"| Force Value | {self.force_value:.3f} |\n"
        markdown += f"| Apply Point | ({self.global_apply_point.x:.3f}, {self.global_apply_point.y:.3f}, {self.global_apply_point.z:.3f}) |\n"
        markdown += f"| D1 | {self.d1_value:.3f} |\n"
        markdown += f"| D2 | {self.d2_value:.3f} |\n"
        markdown += f"| Load Case | {self.load_case.name} |\n"
        return markdown
    
    def to_markdown_compact(self) -> str:
        """
        Generate a compact single-line representation for table cells.
        
        Returns:
            str: Compact load description.
        """
        return f"Conc({self.direction.name}, F={self.force_value:.2f}, d1={self.d1_value:.2f})"