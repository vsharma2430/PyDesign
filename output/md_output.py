from enum import Enum
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
from base.staad_base.transform_force import *
from collections import defaultdict
import ipywidgets as widgets


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


def create_tiers_markdown_table(tiers: List[Tier], title: str = "Tier List") -> str:
    """
    Create a Markdown table for a list of Tier objects, displaying elevation and load counts.
    
    Args:
        tiers (List[Tier]): List of Tier objects to display.
        title (str): Title of the Markdown table (default: "Tier List").
    
    Returns:
        str: Formatted Markdown table as a string.
    """
    markdown = f"# {title}\n\n"
    markdown += "| Tier | Elevation (y) | Loads | Wind Loads | CLT Loads |\n"
    markdown += "|------|---------------|-------|------------|----------|\n"
    
    for i, tier in enumerate(tiers, 1):
        elevation = f"{tier.base.y:.2f}"
        load_count = len(tier.loads)
        wind_load_count = len(tier.wind_loads) if tier.wind_loads else 0
        clt_load_count = len(tier.clt_loads) if tier.clt_loads else 0
        
        markdown += (
            f"| Tier {i} | {elevation} | {load_count} | "
            f"{wind_load_count} | {clt_load_count} |\n"
        )
    
    return markdown


def create_detailed_tiers_load_markdown(tiers: List[Tier], title: str = "Detailed Tier Information") -> str:
    """
    Create detailed Markdown output for tiers with individual load details in a beautified format.
    
    Args:
        tiers (List[Tier]): List of Tier objects to display.
        title (str): Title of the output (default: "Detailed Tier Information").
    
    Returns:
        str: Formatted detailed Markdown as a string.
    """
    markdown = f"# {title}\n\n"

    # Summary Table
    markdown += "## Tier Summary\n\n"
    markdown += "| Tier | Elevation (y) | Type | Std .Piping Loads | CLT Loads | Wind Loads |\n"
    markdown += "|------|---------------|------|-------|-----------|------------|\n"
    for i, tier in enumerate(tiers, 1):
        markdown += (
            f"| Tier {i} | {tier.base.y:.2f}m | {tier.tier_type.name} | "
            f"{len(tier.loads)} | {len(tier.clt_loads)} | {len(tier.wind_loads)} |\n"
        )
    markdown += "\n---\n\n"

    markdown += "> Flare,WW,E&I and Duct loads will be added separately in their respective sections.\n\n"
    markdown += "<details><summary>Details</summary>\n\n"

    # Detailed Tier Information
    for i, tier in enumerate(tiers, 1):
        markdown += f"## Tier {i} - Elevation: {tier.base.y:.2f}m\n\n"

        markdown += "<details><summary>View Tier Details</summary>\n\n"
        markdown += "\n\n"
        markdown += tier.to_markdown() + "\n\n"
        markdown += "</details>\n\n"

        markdown += "<details><summary>View Loads</summary>\n\n"

        # Loads Section
        if tier.loads:
            markdown += "### Loads\n\n"
            markdown += "<details><summary>View Loads</summary>\n\n"
            for j, load in enumerate(tier.loads, 1):
                markdown += "\n\n"
                markdown += load.to_markdown() + "\n\n"
            markdown += "\n\n</details>\n\n"

        # Wind Loads Section
        if tier.wind_loads:
            markdown += "### Wind Loads\n\n"
            markdown += "<details><summary>View Wind Loads</summary>\n\n"
            for j, load in enumerate(tier.wind_loads, 1):
                markdown += "\n\n"
                markdown += load.to_markdown() + "\n\n"
            markdown += "</details>\n\n"

        # CLT Loads Section
        if tier.clt_loads:
            markdown += "### CLT Loads\n\n"
            markdown += "<details><summary>View CLT Loads</summary>\n\n"
            for j, load in enumerate(tier.clt_loads, 1):
                markdown += "\n\n"
                markdown += load.to_markdown() + "\n\n"
            markdown += "</details>\n\n"

        markdown += "</details>\n\n"
        

        # Separator for all tiers except the last
        if i < len(tiers):
            markdown += "---\n\n"

    markdown += "</details>\n\n"

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

def transform_load_case_markdown(transform_objects):
    """
    Generate a markdown table for transform load cases.
    
    Args:
        transform_objects: Iterable of objects with id, source, destination, predicate, and direction attributes.
    
    Returns:
        str: Formatted markdown table as a string.
    
    Raises:
        AttributeError: If an object lacks required attributes.
        TypeError: If predicate is not callable or input is invalid.
    """
    markdown_table = """
## Transform Load Case Table
> #### Source Load Case -> Force value = 1
| ID                    | Source | Destination | Predicate Value | Direction |
|-----------------------|--------|-------------|-----------------|-----------|
"""
    
    try:
        obj:TransformLoadCase
        for obj in transform_objects:
            # Safely access direction and handle None
            direction_str = str(obj.destination_direction) if obj.destination_direction is not None else 'None'
            
            # Calculate and format predicate value with error handling
            try:
                predicate_value = f"{obj.predicate(x=1):.3f}"
            except (TypeError, AttributeError) as e:
                predicate_value = "Error"
            
            # Use consistent string formatting for alignment
            markdown_table += (
                f"| {obj.id:<21} | {obj.source:^6} | {obj.destination:^11} "
                f"| {predicate_value:^15} | {direction_str:^9} |\n"
            )
    
    except AttributeError as e:
        raise AttributeError(f"Invalid object in transform_objects: missing required attribute - {e}")
    
    return markdown_table

def md_elevation_wise_column_table(columns_z):
    markdown_output = '### Column Table\n'
    markdown_output += '| Elevation | Columns |\n'
    markdown_output += '|-----------|---------|\n'

    for z in sorted(columns_z.keys()):  # Sort elevations in ascending order
        beam_ids = ', '.join([str(beam.id) for beam in columns_z[z]])
        markdown_output += f'| {z} | {beam_ids} |\n'
    return markdown_output

def md_tier_wise_beams(tiers):
    markdown_output = '### Tier Beams Table\n'
    markdown_output += '| Tier Elevation | Count | Beams |\n'
    markdown_output += '|-----------|---------| -------|\n'

    for tier_x in tiers:
        markdown_output += tier_x.beams_to_markdown()
    return markdown_output

def md_tier_wise_int_beams(tiers):
    markdown_output = '### Tier Intermediate Beams Table\n'
    markdown_output += '| Tier Elevation | Count | Int. Beams |\n'
    markdown_output += '|-----------|---------| -------|\n'

    for tier_x in tiers:
        markdown_output += tier_x.int_beams_to_markdown()
    return markdown_output

def md_vertical_braces(columns_z,vertical_braces):
    columns_z = defaultdict(list)
    for beam in vertical_braces:
        columns_z[beam.start.y].append(beam)

    markdown_output = '### Vertical Braces\n'
    markdown_output += '| Elevation | Braces |\n'
    markdown_output += '|-----------|---------|\n'
    for z in sorted(columns_z.keys()):  # Sort elevations in ascending order
        beam_ids = ', '.join([str(beam.id) for beam in columns_z[z]])
        markdown_output += f'| {z} | {beam_ids} |\n'
    return markdown_output


def md_plan_braces(columns_z,plan_braces):
    columns_z = defaultdict(list)
    for beam in plan_braces:
        columns_z[beam.start.y].append(beam)

    markdown_output = '### Plan Braces\n'
    markdown_output += '| Elevation | Braces |\n'
    markdown_output += '|-----------|---------|\n'
    for z in sorted(columns_z.keys()):  # Sort elevations in ascending order
        beam_ids = ', '.join([str(beam.id) for beam in columns_z[z]])
        markdown_output += f'| {z} | {beam_ids} |\n'    
    return markdown_output

def md_long_beams(title='Long Beams',long_beams=[]):
    long_dict = group_beams_by_y(long_beams)
    markdown_output = f'### {title}\n'
    markdown_output += '| Elevation | Beams |\n'
    markdown_output += '|-----------|---------|\n'
    for z in sorted(long_dict.keys()):  # Sort elevations in ascending order
        beam_ids = ', '.join([str(beam.id) for beam in long_dict[z]])
        markdown_output += f'| {z} | {beam_ids} |\n'    
    return markdown_output
