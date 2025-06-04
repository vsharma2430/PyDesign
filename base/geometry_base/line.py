import math
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