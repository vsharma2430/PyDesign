from copy import deepcopy
from typing import List, Optional
from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.material.material import *
from base.load.load import Load  
from enum import IntEnum

class TierType(IntEnum):
    Piping = 1
    ElectricalIntrumentation = 2
    Flare = 3

class Tier:
    """A class representing a structural tier composed of beams and applied loads.

    Attributes:
        base (Point3D): Reference point for the tier's coordinate system.
        beams (List[Beam3D]): List of Beam3D objects in the tier.
        loads (List[Load]): List of Load objects applied to the tier.
        material (Material): Material type for the tier (default: Material.Steel).
        wind_loads (List[Load]): List of wind Load objects applied to the tier.  # NEW
    """

    def __init__(
        self,
        base: Point3D = Point3D(0, 0, 0),
        beams: Optional[List[Beam3D]] = None,
        int_beams: Optional[List[Beam3D]] = None,
        brackets: Optional[List[Beam3D]] = None,
        loads: Optional[List[Load]] = None,
        clt_loads: Optional[List[Load]] = None,
        wind_loads: Optional[List[Load]] = None,
        material: Material = Material.STEEL,
        tier_type: TierType = TierType.Piping,
        intermediate_transverse_beam: bool = True,
        bracket_provision: bool = False,
    ) -> None:
        """Initialize a Tier with a base point, beams, loads, and material.

        Args:
            base (Point3D, optional): Reference point for the tier. Defaults to Point3D(0, 0, 0).
            beams (Optional[List[Beam3D]], optional): List of Beam3D objects. Defaults to empty list.
            loads (Optional[List[Load]], optional): List of Load objects. Defaults to empty list.
            wind_loads (Optional[List[Load]], optional): List of wind Load objects. Defaults to empty list.  # NEW
            material (Material, optional): Material type for the tier. Defaults to Material.Steel.
        """
        self.base = base
        self.material = material
        self.beams = beams if beams is not None else []
        self.brackets = brackets if brackets is not None else []
        self.int_beams = int_beams if int_beams is not None else []  # FIXED: Changed condition from beams to int_beams
        self.loads = loads if loads is not None else []
        self.clt_loads = clt_loads if clt_loads is not None else []
        self.wind_loads = wind_loads if wind_loads is not None else []  # NEW
        self.tier_type = tier_type 
        
        if tier_type != TierType.Piping:
            self.intermediate_transverse_beam = False
            
        self.intermediate_transverse_beam = intermediate_transverse_beam
        self.bracket_provision = bracket_provision

        # Validate input types
        if not isinstance(base, Point3D):
            raise TypeError("base must be a Point3D object.")
        
        self._validate_beams()
        self._validate_loads()
        self._validate_wind_loads()  # NEW

    def _validate_beams(self) -> None:
        """Validate that all beams are Beam3D objects."""
        if self.beams:
            for beam in self.beams:
                if not isinstance(beam, Beam3D):
                    raise TypeError(f"All beams must be Beam3D objects, found {type(beam)}.")

    def _validate_loads(self) -> None:
        """Validate that all loads are Load objects."""
        if self.loads:
            for load in self.loads:
                if not isinstance(load, Load):
                    raise TypeError(f"All loads must be Load objects, found {type(load)}.")

    def _validate_wind_loads(self) -> None:  # NEW
        """Validate that all wind loads are Load objects."""
        if self.wind_loads:
            for load in self.wind_loads:
                if not isinstance(load, Load):
                    raise TypeError(f"All wind loads must be Load objects, found {type(load)}.")

    def add_beam(self, beam: Beam3D) -> None:
        """Add a single Beam3D to the tier."""
        if not isinstance(beam, Beam3D):
            raise TypeError("beam must be a Beam3D object.")
        self.beams.append(beam)

    def add_bracket(self, beam: Beam3D) -> None:
        """Add a single Beam3D to the tier."""
        if not isinstance(beam, Beam3D):
            raise TypeError("beam must be a Beam3D object.")
        self.bracket_provision = True
        self.brackets.append(beam)

    def add_int_beam(self, beam: Beam3D) -> None:
        """Add a single Beam3D to the tier."""
        if not isinstance(beam, Beam3D):
            raise TypeError("beam must be a Beam3D object.")
        self.int_beams.append(beam)

    def add_load(self, load_obj: Load) -> None:
        """Add a single load to the tier."""
        if not isinstance(load_obj, Load):
            raise TypeError("load_obj must be a Load object.")
        self.loads.append(load_obj)

    def add_clt_load(self, load_obj: Load) -> None:
        """Add a single load to the tier."""
        if not isinstance(load_obj, Load):
            raise TypeError("load_obj must be a Load object.")
        self.clt_loads.append(load_obj)

    def add_wind_load(self, load_obj: Load) -> None:  # NEW
        """Add a single wind load to the tier.

        Args:
            load_obj (Load): Wind Load object to add.

        Raises:
            TypeError: If load_obj is not a Load object.
        """
        if not isinstance(load_obj, Load):
            raise TypeError("load_obj must be a Load object.")
        self.wind_loads.append(load_obj)

    def set_intermediate_transverse_beam(self, check: bool):
        self.intermediate_transverse_beam = check
        return self
    
    def set_bracket_provision(self, check: bool):
        self.bracket_provision = check
        return self

    def get_beam_count(self) -> int:
        """Return the number of beams in the tier."""
        return len(self.beams)

    def get_load_count(self) -> int:
        """Return the number of loads in the tier."""
        return len(self.loads)

    def get_wind_load_count(self) -> int:  # NEW
        """Return the number of wind loads in the tier."""
        return len(self.wind_loads)

    def remove_beam(self, beam: Beam3D) -> None:
        """Remove a specific beam from the tier."""
        try:
            self.beams.remove(beam)
        except ValueError:
            raise ValueError("Beam not found in the tier.")

    def remove_load(self, load_obj: Load) -> None:
        """Remove a specific load from the tier."""
        try:
            self.loads.remove(load_obj)
        except ValueError:
            raise ValueError("Load not found in the tier.")

    def remove_wind_load(self, load_obj: Load) -> None:  # NEW
        """Remove a specific wind load from the tier.

        Args:
            load_obj (Load): Wind Load object to remove.

        Raises:
            ValueError: If the load is not found in the tier.
        """
        try:
            self.wind_loads.remove(load_obj)
        except ValueError:
            raise ValueError("Wind load not found in the tier.")

    def get_total_load(self) -> float:
        """Calculate the total load magnitude applied to the tier."""
        return sum(load.magnitude for load in self.loads if hasattr(load, 'magnitude'))

    def get_total_wind_load(self) -> float:  # NEW
        """Calculate the total wind load magnitude applied to the tier.

        Returns:
            float: Sum of magnitudes of all wind loads.
        """
        return sum(load.magnitude for load in self.wind_loads if hasattr(load, 'magnitude'))

    def shift(self, point: Point3D) -> 'Tier':
        """Create a new Tier shifted by a given Point3D vector."""
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
        """Return a string representation of the Tier."""
        return f"Tier(base={self.base}, beams={self.get_beam_count()}, loads={self.get_load_count()}, wind_loads={self.get_wind_load_count()}, material={self.material})"  # MODIFIED

    def _format_beam_list(self, beam_list: Optional[List[Beam3D]]) -> str:
        if not beam_list:
            return "None"
        return ", ".join([f"{beam.id}" for beam in beam_list])

    def _format_load_list(self, load_list: Optional[List[Load]]) -> str:
        if not load_list:
            return "None"
        return ", ".join([f"{load.load_case}" for load in load_list])

    def to_markdown(self) -> str:
        """Generate a markdown representation of the Tier object."""
        md = f"## Tier @ {self.base} \n"
        md += "| Attribute | Value |\n"
        md += "|-----------|-------|\n"
        md += f"| Base Point | ({self.base.x}, {self.base.y}, {self.base.z}) |\n"
        md += f"| Material | {self.material.name} |\n"
        md += f"| Tier Type | {self.tier_type.name} |\n"
        md += f"| Intermediate Transverse Beam | {self.intermediate_transverse_beam} |\n"
        md += f"| Bracket Provision | {self.bracket_provision} |\n\n"
        
        md += "## Beams\n"
        md += "| Beam Type | Count | Details |\n"
        md += "|-----------|-------|---------|\n"
        md += f"| Main Beams | {len(self.beams) if self.beams else 0} | {self._format_beam_list(self.beams)} |\n"
        md += f"| Intermediate Beams | {len(self.int_beams) if self.int_beams else 0} | {self._format_beam_list(self.int_beams)} |\n"
        md += f"| Brackets | {len(self.brackets) if self.brackets else 0} | {self._format_beam_list(self.brackets)} |\n\n"
        
        md += "## Loads\n"
        md += "| Load Type | Count | Details |\n"
        md += "|-----------|-------|---------|\n"
        md += f"| Standard Loads | {len(self.loads) if self.loads else 0} | {self._format_load_list(self.loads)} |\n"
        md += f"| CLT Loads | {len(self.clt_loads) if self.clt_loads else 0} | {self._format_load_list(self.clt_loads)} |\n"
        md += f"| Wind Loads | {len(self.wind_loads) if self.wind_loads else 0} | {self._format_load_list(self.wind_loads)} |\n"  # NEW
        
        return md
    
    def beams_to_markdown(self) -> str:
        return f"| {self.base.y} | {len(self.beams) if self.beams else 0} | {self._format_beam_list(self.beams)} |\n"
    
    def int_beams_to_markdown(self) -> str:
        return f"| {self.base.y} | {len(self.int_beams) if self.int_beams else 0} | {self._format_beam_list(self.int_beams)} |\n"