class SteelHandrail:
    def __init__(self, length, height, diameter, material_type, load_capacity):
        """
        Initialize a SteelHandrail object.

        :param length: Length of the handrail in meters.
        :param height: Height of the handrail in meters.
        :param diameter: Diameter of the handrail in millimeters.
        :param material_type: Type of steel material (e.g., 'Stainless Steel', 'Carbon Steel').
        :param load_capacity: Maximum load capacity of the handrail in kilograms.
        """
        self.length = length
        self.height = height
        self.diameter = diameter
        self.material_type = material_type
        self.load_capacity = load_capacity

    def calculate_volume(self):
        """
        Calculate the volume of steel used in the handrail.

        :return: Volume in cubic meters.
        """
        radius = (self.diameter / 1000) / 2  # Convert diameter from mm to meters and get radius
        cross_sectional_area = 3.14159 * (radius ** 2)  # Area of a circle (πr²)
        return cross_sectional_area * self.length  # Volume = Area * Length

    def calculate_load_per_unit_length(self):
        """
        Calculate the maximum load capacity per unit length.

        :return: Load per unit length in kg/m.
        """
        if self.length == 0:
            raise ValueError("Length cannot be zero.")
        return self.load_capacity / self.length

    def __str__(self):
        """
        Return a string representation of the SteelHandrail object.
        """
        return (f"Steel Handrail: Length={self.length}m, Height={self.height}m, "
                f"Diameter={self.diameter}mm, Material={self.material_type}, "
                f"Load Capacity={self.load_capacity}kg")