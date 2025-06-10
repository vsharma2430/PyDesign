import math
from copy import deepcopy
from base.geometry_base.shape import Shape
from base.geometry_base.point import Point, Point3D

class LineBase(Shape):
    """Base class for lines in 2D or 3D space."""
    def __init__(self, start, end):
        """
        Initialize a line with start and end points.

        Args:
            start: Starting point of the line (Point or Point3D).
            end: Ending point of the line (Point or Point3D).

        Raises:
            TypeError: If start and end are not of the same type or not Point/Point3D.
        """
        if not isinstance(start, type(end)):
            raise TypeError("Start and end points must be of the same type")
        self.start = start
        self.end = end

    def __str__(self):
        """Return a string representation of the line."""
        return f"{self.__class__.__name__}(start={self.start}, end={self.end})"

    def __repr__(self):
        """Return a formal string representation of the line."""
        return self.__str__()

class Line(LineBase):
    """A 2D line defined by two points in 2D space."""
    def __init__(self, start: Point, end: Point):
        """
        Initialize a 2D line with start and end points.

        Args:
            start (Point): Starting point with x, y coordinates.
            end (Point): Ending point with x, y coordinates.

        Raises:
            TypeError: If start or end is not a Point.
        """
        if not (isinstance(start, Point) and isinstance(end, Point)):
            raise TypeError("Start and end must be Point objects")
        super().__init__(start, end)

    def length(self) -> float:
        """
        Calculate the Euclidean length of the 2D line.

        Returns:
            float: Length of the line. Returns 0.0 for coincident points.
        """
        return math.sqrt((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)

    def slope(self) -> float | None:
        """
        Calculate the slope of the 2D line.

        Returns:
            float: Slope of the line, or None if the line is vertical.
        """
        dx = self.end.x - self.start.x
        if dx == 0:
            return None  # Vertical line, undefined slope
        return (self.end.y - self.start.y) / dx

    def angle_with_horizontal(self) -> float:
        """
        Calculate the angle of the 2D line with the horizontal (x-axis).

        Returns:
            float: Angle in degrees (0 to 180). Returns 0.0 for zero-length lines.

        Raises:
            ValueError: If the line has zero length (undefined angle).
        """
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        length = math.sqrt(dx ** 2 + dy ** 2)
        if length == 0:
            return 0.0  # or raise ValueError("Undefined angle for zero-length line")
        cos_theta = abs(dx) / length  # Angle with x-axis
        cos_theta = min(1.0, max(-1.0, cos_theta))  # Handle numerical errors
        return math.degrees(math.acos(cos_theta))

class Line3D(LineBase):
    """A 3D line defined by two points in 3D space."""
    def __init__(self, start: Point3D, end: Point3D):
        """
        Initialize a 3D line with start and end points.

        Args:
            start (Point3D): Starting point with x, y, z coordinates.
            end (Point3D): Ending point with x, y, z coordinates.

        Raises:
            TypeError: If start or end is not a Point3D.
        """
        if not (isinstance(start, Point3D) and isinstance(end, Point3D)):
            raise TypeError("Start and end must be Point3D objects")
        super().__init__(start, end)

    def shift(self,point:Point3D):
        line = deepcopy(self)
        line.start = line.start + point
        line.end = line.end + point
        return line

    def length(self) -> float:
        """
        Calculate the Euclidean length of the 3D line.

        Returns:
            float: Length of the line. Returns 0.0 for coincident points.
        """
        return math.sqrt(
            (self.end.x - self.start.x) ** 2 +
            (self.end.y - self.start.y) ** 2 +
            (self.end.z - self.start.z) ** 2
        )

    def direction_vector(self) -> tuple[float, float, float]:
        """
        Calculate the direction vector of the 3D line.

        Returns:
            tuple: (dx, dy, dz) representing the direction vector.
        """
        return (
            self.end.x - self.start.x,
            self.end.y - self.start.y,
            self.end.z - self.start.z
        )

    def angle_with_xy_plane(self) -> float:
        """
        Calculate the angle of the 3D line with the XY-plane (horizontal).

        Returns:
            float: Angle in degrees (0 to 90). Returns 0.0 for zero-length lines or
                   lines parallel to the XY-plane.

        Raises:
            ValueError: If the line has zero length (undefined angle).
        """
        dx, dy, dz = self.direction_vector()
        xy_magnitude = math.sqrt(dx ** 2 + dy ** 2)
        line_magnitude = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        
        if line_magnitude == 0:
            return 0.0  # or raise ValueError("Undefined angle for zero-length line")
        if xy_magnitude == 0:
            return 90.0  # Line is vertical (perpendicular to XY-plane)
        
        cos_theta = xy_magnitude / line_magnitude
        cos_theta = min(1.0, max(-1.0, cos_theta))  # Handle numerical errors
        return math.degrees(math.acos(cos_theta))
    
    def contains_point(self, point: Point3D, tolerance: float = 1e-4) -> bool:
        """
        Check if a given 3D point lies on the line segment between start and end points.
        
        Args:
            point: The Point3D to check.
            tolerance: Floating-point tolerance for numerical comparisons (default: 1e-4).
        
        Returns:
            bool: True if the point lies on the line segment, False otherwise.
        """
        # Vector from start to end (direction vector)
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        dz = self.end.z - self.start.z
        
        # Vector from start to the point
        px = point.x - self.start.x
        py = point.y - self.start.y
        pz = point.z - self.start.z
        
        # Check for degenerate line (start = end)
        if abs(dx) < tolerance and abs(dy) < tolerance and abs(dz) < tolerance:
            # Line is a point; check if point equals start
            return (abs(px) < tolerance and 
                    abs(py) < tolerance and 
                    abs(pz) < tolerance)
        
        # Compute t for each coordinate where possible (non-zero denominator)
        t_values = []
        if abs(dx) > tolerance:
            t_values.append(px / dx)
        if abs(dy) > tolerance:
            t_values.append(py / dy)
        if abs(dz) > tolerance:
            t_values.append(pz / dz)
        
        # If no t values (all denominators zero), point must be at start
        if not t_values:
            return (abs(px) < tolerance and 
                    abs(py) < tolerance and 
                    abs(pz) < tolerance)
        
        # Check if all computed t values are approximately equal
        t = t_values[0]
        for t_other in t_values[1:]:
            if abs(t - t_other) > tolerance:
                return False
        
        # Verify the point satisfies the parametric equation
        # (needed for cases where some coordinates are zero)
        if not (abs(px - t * dx) < tolerance and
                abs(py - t * dy) < tolerance and
                abs(pz - t * dz) < tolerance):
            return False
        
        # NEW: Check if the point is within the bounds of the line segment
        # The parameter t should be between 0 and 1 (inclusive) for the point
        # to lie on the line segment between start and end
        return 0.0 <= t <= 1.0