class SteelElectricalSupportTree:
    def __init__(self, height : float = 0, base_width : float = 0,num_branches : int = 0, material_type : str = '',load_capacity : float = 0):
        """
        Initialize a SteelElectricalSupportTree object.

        :param height: Height of the support tree in meters.
        :param base_width: Width of the base in meters.
        :param material_type: Type of steel material (e.g., 'Galvanized Steel', 'Stainless Steel').
        :param num_branches: Number of branches on the support tree.
        :param load_capacity: Maximum load capacity of the support tree in kilograms.
        """
        self.height = height
        self.base_width = base_width
        self.material_type = material_type
        self.num_branches = num_branches
        self.load_capacity = load_capacity

    def calculate_base_area(self):
        """
        Calculate the base area of the support tree.

        :return: Base area in square meters.
        """
        return self.base_width ** 2  # Assuming the base is square-shaped

    def calculate_load_per_branch(self):
        """
        Calculate the maximum load capacity per branch.

        :return: Load per branch in kilograms.
        """
        if self.num_branches == 0:
            raise ValueError("Number of branches cannot be zero.")
        return self.load_capacity / self.num_branches

    def __str__(self):
        """
        Return a string representation of the SteelElectricalSupportTree object.
        """
        return (f"Steel Electrical Support Tree: Height={self.height}m, Base Width={self.base_width}m, "
                f"Material={self.material_type}, Number of Branches={self.num_branches}, "
                f"Load Capacity={self.load_capacity}kg")