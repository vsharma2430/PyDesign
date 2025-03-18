class SteelWalkway:
    def __init__(self, length, width, thickness, material_type, load_capacity):
        """
        Initialize a SteelWalkway object.

        :param length: Length of the walkway in meters.
        :param width: Width of the walkway in meters.
        :param thickness: Thickness of the steel in millimeters.
        :param material_type: Type of steel material (e.g., 'Carbon Steel', 'Stainless Steel').
        :param load_capacity: Maximum load capacity of the walkway in kilograms.
        """
        self.length = length
        self.width = width
        self.thickness = thickness
        self.material_type = material_type
        self.load_capacity = load_capacity

    def calculate_area(self):
        """
        Calculate the area of the walkway.

        :return: Area in square meters.
        """
        return self.length * self.width

    def calculate_load_per_unit_area(self):
        """
        Calculate the maximum load per unit area.

        :return: Load per unit area in kg/m².
        """
        area = self.calculate_area()
        if area == 0:
            raise ValueError("Area cannot be zero.")
        return self.load_capacity / area

    def __str__(self):
        """
        Return a string representation of the SteelWalkway object.
        """
        return (f"Steel Walkway: Length={self.length}m, Width={self.width}m, "
                f"Thickness={self.thickness}mm, Material={self.material_type}, "
                f"Load Capacity={self.load_capacity}kg")