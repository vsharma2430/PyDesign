import pickle
from enum import IntEnum
from base.geometry_base.point import Point3D
from base.structural_elements.beam import Beam3D
from base.structural_elements.column import Column3D
from base.piperack.portal import PiperackPortal
from base.structural_elements.brace import BracePattern
from base.staad_base.geometry import *
from copy import deepcopy

class PiperackMembers(IntEnum):
    TierBeams = 0
    Columns = 1
    Pedestals = 2
    LongitudinalBeams = 3
    VerticalBracing = 4
    PlanBracing = 5
    Stubs = 6
    IntermediateTransverseBeams = 7
    IntermediateLongitudinalBeams = 8 
    FlareSupportMembers = 9
    DuctSupportMembers = 10
    TreeSupportMembers = 11
    WWSupportMembers = 12
    BracketBeams = 13
    BracketBraces = 14

class PiperackStructure:
    def __init__(self):
        # Support members
        self.ww_support_members = None
        self.flare_support_members = None
        self.duct_support_members = None
        self.tree_support_members = None
        self.long_beam_elevations_set = None
        
        # Portal-related properties
        self.longitudinal_beams = None
        self.stubs = None
        self.intermediate_transverse_beams = None
        self.intermediate_long_beams = None
        self.plan_braces = None
        self.vertical_braces = None
        self.portal_beam_ids = None
        self.portal_column_ids = None
        self.portal_pedestal_ids = None
        self.support_node_ids = None
        self.long_beam_ids = None
        self.stub_ids = None
        self.intermediate_transverse_ids = None
        self.intermediate_long_ids = None
        self.plan_brace_ids = None
        self.vertical_brace_ids = None
        self.portal_count = None
        self.max_portal_to_portal = None
        self.portal_z_set = None
        
        # Beam and member categorizations
        self.steel_members = None
        self.concrete_members = None
        self.main_columns = None
        self.stub_columns = None
        self.columns_y = None
        self.columns_z = None
        self.stub_columns_y = None
        self.stub_columns_z = None
        self.long_beams = None
        self.int_long_beams = None
        self.portal_beams = None
        self.portal_beam_dict = None
        self.portal_tier_beams = None

class Piperack:
    def __init__(self,name = 'MPR'):
        self.name = name        
        # Base point and dimensions
        self.base_point_of_first_portal = Point3D()
        self.width_of_piperack = 8
        self.portal_distances = None
        self.column_distances = None
        self.long_beam_elevations = None
        
        # Bracing and structural details
        self.braces_placement = None
        self.brace_pattern = BracePattern.X_Pattern
        self.bracket_size = 2
        self.max_expansion_bay_length = 8
        
        # Tiers and derived properties
        self.tiers = None
        self.portals = None
        self.tier_elevations = None
        self.tier_dict = None
        
        # Components
        self.flares = None
        self.walkways = None
        self.ducts = None
        self.electric_trees = None
        
        # Foundation 
        self.pedestal_height = None
        self.foundation_depth = None

    def export_to_pickle(self, filename):
        """
        Exports the Piperack object to a pickle file.
        
        Args:
            filename (str): The name of the file to save the pickle object to.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    
    @staticmethod
    def load_from_pickle(filename):
        """
        Loads a Piperack object from a pickle file.
        
        Args:
            filename (str): The name of the file to read the pickle object from.
            
        Returns:
            Piperack: The deserialized Piperack object.
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def generate_structural_components(self, geometry,property):
        """
        Generates structural components and their IDs based on the piperack configuration.
        Returns a PiperackStructure object with all components as properties.
        """
        structure = PiperackStructure()
        
        # Support members
        structure.ww_support_members = [line for ww_x in self.walkways for line in ww_x.get_member_lines()]
        structure.flare_support_members = [line for flare in self.flares if flare.support_member for line in flare.lines]
        structure.duct_support_members = [line for duct_x in self.ducts for line in duct_x.get_member_lines()]
        structure.tree_support_members = [et.line for et in self.electric_trees if et.support_member]
        structure.long_beam_elevations_set = set(self.long_beam_elevations)
        
        # Portal-related initialization
        structure.longitudinal_beams = []
        structure.stubs = []
        structure.intermediate_transverse_beams = []
        structure.intermediate_long_beams = []
        structure.plan_braces = []
        structure.vertical_braces = []
        structure.portal_beam_ids = []
        structure.portal_column_ids = []
        structure.portal_pedestal_ids = []
        structure.support_node_ids = []
        structure.long_beam_ids = []
        structure.stub_ids = []
        structure.intermediate_transverse_ids = []
        structure.intermediate_long_ids = []
        structure.plan_brace_ids = []
        structure.vertical_brace_ids = []
        structure.portal_count = len(self.portal_distances)
        
        # Create first portal
        portal = PiperackPortal(base=self.base_point_of_first_portal)
        column_distances_set = set(self.column_distances)
        
        for z_column in self.column_distances:
            support_point = Point3D(z_column, 0, 0) - Point3D(0, self.pedestal_height, 0)
            portal.add_pedestal(Column3D(base=support_point, height=self.pedestal_height))
            portal.add_column(Column3D(base=Point3D(z_column, 0, 0), height=self.tier_elevations[-1]))
        
        for tier_x in self.tier_elevations:
            for column_x in range(len(self.column_distances)-1):
                portal.add_beam(Beam3D(
                    start=Point3D(self.column_distances[column_x], tier_x, 0),
                    end=Point3D(self.column_distances[column_x+1], tier_x, 0)
                ))
        
        # Create all portals by shifting the first portal
        portals = [portal.shift(Point3D(0, 0, dist)) for dist in self.portal_distances]
        
        # Create longitudinal beams between portals
        for portal_i in range(len(portals)-1):
            for z_column in self.column_distances:
                for long_beam in self.long_beam_elevations:
                    long_beam_x = Beam3D(
                        start=Point3D(z_column, long_beam, portals[portal_i].base.z),
                        end=Point3D(z_column, long_beam, portals[portal_i+1].base.z)
                    )
                    structure.longitudinal_beams.append(long_beam_x)
        
        structure.max_portal_to_portal = max([
            portals[portal_i].base.distance_to(portals[portal_i+1].base)
            for portal_i in range(len(portals)-1)
        ])
        
        portal_zs = [portal.base.z for portal in portals]
        structure.portal_z_set = set(portal_zs)
        
        # Get nodes and beams from geometry
        nodes = get_node_incidences(geometry=geometry)
        beam_objects = get_beam_objects(geometry=geometry, property=property, nodes=nodes)
        
        tier_elevations = [tier.base.y for tier in self.tiers]
        portal_zs = [portal.base.z for portal in portals]
        
        # Categorize members
        structure.steel_members = [
            beam for beam in beam_objects.values()
            if beam.start.y >= self.base_point_of_first_portal.y
        ]
        structure.concrete_members = [
            beam for beam in beam_objects.values()
            if beam.start.y < self.base_point_of_first_portal.y
        ]
        
        structure.main_columns = [
            beam for beam in structure.steel_members
            if (not beam.start.eq_y(beam.end) and
                beam.start.eq_x(beam.end) and
                beam.start.eq_z(beam.end)) and
                beam.start.z in portal_zs
        ]

        structure.stub_columns = [
            beam for beam in structure.steel_members
            if (not beam.start.eq_y(beam.end) and
                beam.start.eq_x(beam.end) and
                beam.start.eq_z(beam.end)) and
                beam.start.z not in portal_zs
        ]

        structure.columns_y = group_beams_by_y(structure.main_columns)
        structure.columns_z = group_beams_by_z(structure.main_columns)

        structure.stub_columns_y = group_beams_by_y(structure.stub_columns)
        structure.stub_columns_z = group_beams_by_z(structure.stub_columns)
        
        structure.vertical_braces = [
            beam for beam in beam_objects.values()
            if (not beam.start.eq_y(beam.end) and
                beam.start.eq_x(beam.end) and
                not beam.start.eq_z(beam.end))
        ]
        
        structure.plan_braces = [
            beam for beam in beam_objects.values()
            if (beam.start.eq_y(beam.end) and
                not beam.start.eq_x(beam.end) and
                not beam.start.eq_z(beam.end))
        ]
        
        structure.long_beams = [
            beam for beam in beam_objects.values()
            if (beam.start.eq_x(beam.end) and
                beam.start.eq_y(beam.end) and
                not beam.start.eq_z(beam.end) and
                (beam.start.y in structure.long_beam_elevations_set) and
                (beam.start.x in column_distances_set))
        ]
        
        structure.int_long_beams = [
            beam for beam in beam_objects.values()
            if (beam.start.eq_x(beam.end) and
                beam.start.eq_y(beam.end) and
                not beam.start.eq_z(beam.end) and
                (beam.start.y in set(tier_elevations)) and
                not (beam.start.x in column_distances_set))
        ]
        
        # Initialize beam dictionaries
        structure.portal_beams = {}
        structure.intermediate_transverse_beams = {}
        portal_beam_dict = {portal.base.z: [] for portal in portals}
        portal_tier_beams = {portal_z: {tier: [] for tier in tier_elevations} for portal_z in portal_zs}
        
        # Process beams
        for beam_no, beam in beam_objects.items():
            if (portal_zs[0] <= beam.start.z <= portal_zs[-1] and
                    portal_zs[0] <= beam.end.z <= portal_zs[-1]):
                tier_y = None
                portal_z = None
                chosen_one_1, chosen_one_2 = False, False
                
                for tier_x in tier_elevations:
                    if (beam.start.eq_z(beam.end) and
                            beam.start.eq_y(tier_x) and
                            beam.end.eq_y(tier_x)):
                        chosen_one_1 = True
                        tier_y = tier_x
                
                for portal in portal_zs:
                    if (beam.start.eq_z(portal) and beam.end.eq_z(portal)):
                        chosen_one_2 = True
                        portal_z = portal
                
                if chosen_one_1 and chosen_one_2:
                    structure.portal_beams[beam_no] = beam
                    if tier_y and tier_y in self.tier_dict:
                        self.tier_dict[tier_y].add_beam(beam)
                    if portal_z and portal_z in portal_beam_dict:
                        portal_beam_dict[portal_z].append(beam)
                    portal_tier_beams[portal_z][tier_y].append(beam_no)
                
                if chosen_one_1 and not chosen_one_2:
                    structure.intermediate_transverse_beams[beam_no] = beam
                    if tier_y in self.tier_dict:
                        self.tier_dict[tier_y].add_int_beam(beam)
        
        structure.portal_beam_dict = portal_beam_dict
        structure.portal_tier_beams = portal_tier_beams
        
        return structure