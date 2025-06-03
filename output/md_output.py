from enum import Enum
from IPython.display import Markdown, display
from dataclasses import dataclass
from typing import Union, Dict

from base.helper.general import *
from base.geometry_base.rectangle import *
from base.staad_base.geometry import *
from base.structural_elements.beam import *
from base.structural_elements.column import *
from base.structural_elements.brace import *
from base.piperack.portal import *
from base.piperack.piperack import *
from base.piperack.tier import *
from base.staad_base.load import *
from base.staad_base.design import *
from base.staad_base.property import *

from base.staad_base.optimise_member import *

def create_profile_markdown_table(
    concrete_profiles: Dict[Enum, Union[Rectangle, str, int, float]],
    steel_profiles: Dict[Enum, Union[str, int, float]],
    profile_ids: Dict[Enum, int]
) -> str:
    """
    Create a Markdown table for profiles and their IDs.
    
    Args:
        concrete_profiles: Dictionary of concrete member types and profiles.
        steel_profiles: Dictionary of steel member types and profiles.
        profile_ids: Dictionary of member types and their profile IDs.
    
    Returns:
        Formatted Markdown table as a string.
    """
    markdown = "## Profile List\n\n"
    markdown += "| Member Type | Profile | Profile ID |\n"
    markdown += "|-------------|---------|------------|\n"
    
    # Add concrete profiles
    for member_type, profile in concrete_profiles.items():
        markdown += f"| {member_type.value} | {str(profile)} | {profile_ids.get(member_type, 'N/A')} |\n"
    
    # Add steel profiles
    for member_type, profile in steel_profiles.items():
        markdown += f"| {member_type.value} | {profile} | {profile_ids.get(member_type, 'N/A')} |\n"
    
    return markdown

def create_spec_markdown_table(start_release_spec,end_release_spec,truss_spec,offset_member_spec):
    markdown_output = "## Member Specifications Created\n\n"
    markdown_output += "| Specification Type | Details |\n"
    markdown_output += "|-------------------|---------|\n"
    markdown_output += f"| Start Release | {start_release_spec} |\n"
    markdown_output += f"| End Release | {end_release_spec} |\n"
    markdown_output += f"| Truss | {truss_spec} |\n"
    markdown_output += f"| Offset Member | {offset_member_spec} |\n"
    return markdown_output

def create_tiers_markdown_table(tiers, title="Tier List"):
    markdown = "# Tier List\n\n"
    markdown += "| Tier Number | Elevation (y) | Load Type |\n"
    markdown += "|-------------|---------------|-----------|\n"
    
    # Iterate through tiers and add to markdown table
    for i, tier in enumerate(tiers, 1):
        elevation = tier.base.y
        load_types = ", ".join(str(load) for load in tier.loads) if tier.loads else "None"
        markdown += f"| Tier {i} | {elevation} | {load_types} |\n"
    
    return markdown

def create_beams_markdown_table(beams):
    """
    Convert a list of Beam3D objects to a Markdown table with start, end, and profile.
    
    Args:
        beams (list): List of Beam3D objects.
        
    Returns:
        str: Markdown table string containing beam start, end, and profile.
    """
    # Header for the Markdown table
    markdown = "| ID | Start (x,y,z) | End (x,y,z) | Profile |\n"
    markdown += "|----|---------------|-------------|---------|\n"
    
    # Iterate through beams with an index as ID
    for idx, beam in enumerate(beams, 1):
        start = f"({beam.start.x:.2f}, {beam.start.y:.2f}, {beam.start.z:.2f})"
        end = f"({beam.end.x:.2f}, {beam.end.y:.2f}, {beam.end.z:.2f})"
        markdown += f"| {idx} | {start} | {end} | {beam.profile} |\n"
    
    return markdown


def wind_load_definition_markdown(wind_loads):
    # Markdown table header
    markdown = "| Start Elevation | End Elevation | Windward Load | Leeward Load |\n"
    markdown += "|-----------------|---------------|---------------|--------------|\n"
    
    # Add each WindLoad object as a row
    for load in wind_loads:
        markdown += f"| {load.start_ele:.1f} | {load.end_ele:.1f} | {load.windward:.4f} | {load.leeward:.4f} |\n"
    
    # Display the Markdown
    return markdown

def wind_load_assignment_markdown(heading,wind_loads):
    # Markdown table header
    markdown = "#####{heading}\n"
    markdown = "| Col_id | Load |\n"
    markdown += "|-----------------|---------------|\n"
    
    # Add each WindLoad object as a row
    for col_id,load in wind_loads:
        markdown += f"| {col_id} | {load} |\n"
    
    # Display the Markdown
    return markdown

