class Cable:
    def __init__(self, name: str, diameter: float, length: float):
        """
        Represents a cable or wire.
        - name: Name/identifier of the cable.
        - diameter: Diameter of the cable in millimeters.
        - length: Length of the cable in meters.
        """
        self.name = name
        self.diameter = diameter
        self.length = length

    def __str__(self):
        return f"Cable(name={self.name}, diameter={self.diameter}mm, length={self.length}m)"

    def __repr__(self):
        return f"Cable(name={self.name}, diameter={self.diameter}mm, length={self.length}m)"


class InstrumentationDuct:
    def __init__(self, width: float, height: float, length: float, material: str = "steel"):
        """
        Represents an instrumentation duct.
        - width: Width of the duct in millimeters.
        - height: Height of the duct in millimeters.
        - length: Length of the duct in meters.
        - material: Material of the duct (default is steel).
        """
        self.width = width
        self.height = height
        self.length = length
        self.material = material
        self.cables = []

    def add_cable(self, cable: Cable):
        """
        Add a cable to the duct.
        """
        self.cables.append(cable)

    def total_cable_diameter(self):
        """
        Calculate the total diameter of all cables in the duct.
        """
        return sum(cable.diameter for cable in self.cables)

    def is_overcrowded(self):
        """
        Check if the duct is overcrowded (total cable diameter exceeds duct dimensions).
        """
        return self.total_cable_diameter() > self.width or self.total_cable_diameter() > self.height

    def __str__(self):
        return (f"InstrumentationDuct(width={self.width}mm, height={self.height}mm, length={self.length}m, "
                f"material={self.material}, num_cables={len(self.cables)}, overcrowded={self.is_overcrowded()})")

    def __repr__(self):
        return (f"InstrumentationDuct(width={self.width}mm, height={self.height}mm, length={self.length}m, "
                f"material={self.material}, num_cables={len(self.cables)}, overcrowded={self.is_overcrowded()})")