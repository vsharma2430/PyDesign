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