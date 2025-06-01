from copy import deepcopy
from typing import List, Optional
from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.material.material import *
from base.load.load import Load  

class Tier:
    """A class representing a structural tier composed of beams and applied loads.

    Attributes:
        base (Point3D): Reference point for the tier's coordinate system.
        beams (List[Beam3D]): List of Beam3D objects in the tier.
        loads (List[Load]): List of Load objects applied to the tier.
        material (Material): Material type for the tier (default: Material.Steel).
    """

    def __init__(
        self,
        base: Point3D = Point3D(0, 0, 0),
        beams: Optional[List[Beam3D]] = None,
        loads: Optional[List[Load]] = None,
        material: Material = Material.STEEL
    ) -> None:
        """Initialize a Tier with a base point, beams, loads, and material.

        Args:
            base (Point3D, optional): Reference point for the tier. Defaults to Point3D(0, 0, 0).
            beams (Optional[List[Beam3D]], optional): List of Beam3D objects. Defaults to empty list.
            loads (Optional[List[Load]], optional): List of Load objects. Defaults to empty list.
            material (Material, optional): Material type for the tier. Defaults to Material.Steel.

        Raises:
            TypeError: If beams or loads contain invalid types.
        """
        self.base = base
        self.material = material
        self.beams = beams if beams is not None else []
        self.loads = loads if loads is not None else []

        # Validate input types
        if not isinstance(base, Point3D):
            raise TypeError("base must be a Point3D object.")
        
        self._validate_beams()
        self._validate_loads()

    def _validate_beams(self) -> None:
        """Validate that all beams are Beam3D objects.

        Raises:
            TypeError: If any beam is not a Beam3D object.
        """
        if(self.beams):
            for beam in self.beams:
                if not isinstance(beam, Beam3D):
                    raise TypeError(f"All beams must be Beam3D objects, found {type(beam)}.")

    def _validate_loads(self) -> None:
        """Validate that all loads are Load objects.

        Raises:
            TypeError: If any load is not a Load object.
        """
        if(self.loads):
            for load in self.loads:
                if not isinstance(load, Load):
                    raise TypeError(f"All loads must be Load objects, found {type(load)}.")

    def add_beam(self, beam: Beam3D) -> None:
        """Add a single Beam3D to the tier.

        Args:
            beam (Beam3D): Beam3D object to add.

        Raises:
            TypeError: If beam is not a Beam3D object.
        """
        if not isinstance(beam, Beam3D):
            raise TypeError("beam must be a Beam3D object.")
        self.beams.append(beam)

    def add_load(self, load_obj: Load) -> None:
        """Add a single load to the tier.

        Args:
            load_obj (Load): Load object to add.

        Raises:
            TypeError: If load_obj is not a Load object.
        """
        if not isinstance(load_obj, Load):
            raise TypeError("load_obj must be a Load object.")
        self.loads.append(load_obj)

    def get_beam_count(self) -> int:
        """Return the number of beams in the tier.

        Returns:
            int: Number of beams.
        """
        return len(self.beams)

    def get_load_count(self) -> int:
        """Return the number of loads in the tier.

        Returns:
            int: Number of loads.
        """
        return len(self.loads)

    def remove_beam(self, beam: Beam3D) -> None:
        """Remove a specific beam from the tier.

        Args:
            beam (Beam3D): Beam3D object to remove.

        Raises:
            ValueError: If the beam is not found in the tier.
        """
        try:
            self.beams.remove(beam)
        except ValueError:
            raise ValueError("Beam not found in the tier.")

    def remove_load(self, load_obj: Load) -> None:
        """Remove a specific load from the tier.

        Args:
            load_obj (Load): Load object to remove.

        Raises:
            ValueError: If the load is not found in the tier.
        """
        try:
            self.loads.remove(load_obj)
        except ValueError:
            raise ValueError("Load not found in the tier.")

    def get_total_load(self) -> float:
        """Calculate the total load magnitude applied to the tier.

        Returns:
            float: Sum of magnitudes of all loads.
        """
        return sum(load.magnitude for load in self.loads if hasattr(load, 'magnitude'))
    
    def shift(self, point: Point3D) -> 'Tier':
        """Create a new Tier shifted by a given Point3D vector.

        Args:
            point (Point3D): Vector to shift the tier's base and beams by.

        Returns:
            Tier: A new Tier object with shifted base and beams.

        Raises:
            TypeError: If point is not a Point3D object.
        """
        if not isinstance(point, Point3D):
            raise TypeError("point must be a Point3D object.")
        
        new_tier = deepcopy(self)
        new_tier.base = self.base.__add__(point)
        new_tier.beams = []
        
        for beam in self.beams:
            new_tier.beams.append(beam.shift(point))
        
        # Loads are not shifted as they are typically defined relative to beams
        return new_tier

    def __str__(self) -> str:
        """Return a string representation of the Tier.

        Returns:
            str: Description of the tier including beam and load counts.
        """
        return f"Tier(base={self.base}, beams={self.get_beam_count()}, loads={self.get_load_count()}, material={self.material})"