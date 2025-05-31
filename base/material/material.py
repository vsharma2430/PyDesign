from enum import IntEnum

class Material(IntEnum):
    """An enumeration representing different structural materials with associated integer values.

    This enum is used to define material types for structural elements in a design system.
    Each material is assigned a unique integer value for compatibility with analysis tools.
    """

    STEEL = 1
    CONCRETE = 2
    ALUMINUM = 3
    TIMBER = 4

    @classmethod
    def from_string(cls, material_name: str) -> 'Material':
        """Convert a string to a Material enum member.

        Args:
            material_name (str): Name of the material (case-insensitive).

        Returns:
            Material: Corresponding Material enum member.

        Raises:
            ValueError: If the material_name does not match any enum member.
        """
        try:
            return cls[material_name.upper()]
        except KeyError:
            raise ValueError(f"Invalid material name: {material_name}. "
                            f"Valid options are: {[m.name for m in cls]}")

    @classmethod
    def get_all_materials(cls) -> list['Material']:
        """Return a list of all Material enum members.

        Returns:
            list[Material]: List of all defined materials.
        """
        return list(cls)

    def __str__(self) -> str:
        """Return a human-readable string representation of the material.

        Returns:
            str: Name of the material.
        """
        return self.name.capitalize()