from typing import List
from base.staad_base.root import *
from base.staad_base.geometry import *
from base.staad_base.load import *
from base.staad_base.com_array import *
from base.staad_base.helper import *

get_set = lambda items:set(items) if (items and len(items)>0) else None

class TransformLoadCase:
    def __init__(self, id, source, destination, predicate, source_direction : MemberForceDirection = None, destination_direction:MemberForceDirection = None):
        self.id = id
        self.source = source
        self.destination = destination
        self.predicate = predicate
        self.source_direction = source_direction
        self.destination_direction = destination_direction

    def __repr__(self):
        return (f"TransformLoadCase(id={self.id}, source={self.source}, "
                f"destination={self.destination}, predicate={self.predicate}, "
                f"source_direction={self.source_direction}, destination_direction={self.destination_direction})")

    def to_markdown(self):
        """
        Generates Markdown documentation for this TransformLoadCase instance.

        Returns:
            str: Markdown-formatted string describing the instance.
        """
        markdown = f""" # TransformLoadCase Instance
                        ## Instance Details
                        - **ID**: {self.id}
                        - **Source**: {self.source}
                        - **Destination**: {self.destination}
                        - **Predicate**: {self.predicate}
                        - **Source Direction**: {self.source_direction}
                        - **Destination Direction**: {self.destination_direction}
                    """
        return markdown

def convert_force_operation(STAAD_objects: OpenSTAAD_objects, 
                            transform_load_case_object: TransformLoadCase, 
                            nodes: List[int] = None, 
                            beams: List[int] = None, 
                            generate_markdown: bool = False):
    """
    Convert force operations from source to destination load case with optional markdown output
    
    Args:
        STAAD_objects: OpenSTAAD objects containing geometry, load, property data
        transform_load_case_object: TransformLoadCase object with transformation parameters
        nodes: Optional list of specific nodes
        beams: Optional list of specific beams  
        generate_markdown: If True, returns markdown string instead of printing to console
    
    Returns:
        str: Markdown formatted string if generate_markdown=True, None otherwise
    """
    source = transform_load_case_object.source
    destination = transform_load_case_object.destination
    source_direction = transform_load_case_object.source_direction
    destination_direction = transform_load_case_object.destination_direction
    predicate = transform_load_case_object.predicate
    transform_id = transform_load_case_object.id

    load_object = STAAD_objects.load

    node_set = get_set(nodes)
    beam_set = get_set(beams)

    # Initialize markdown content if requested
    markdown_content = [] if generate_markdown else None
    
    def add_output(text, level=0):
        """Helper function to add output to console or markdown"""
        if generate_markdown:
            if level == 0:  # Main headers
                markdown_content.append(f"## {text}")
            elif level == 1:  # Sub headers
                markdown_content.append(f"### {text}")
            elif level == 2:  # Sub-sub headers
                markdown_content.append(f"#### {text}")
            elif level == 5:  # Success/failure indicators - just append without adding icon
                markdown_content.append(text)  # Text already contains the icon
            elif level == 6:  # Raw table row
                markdown_content.append(text)
            else:  # Regular text
                markdown_content.append(text)
        else:
            print(text)

    # Start processing
    add_output(f"Transformation: {source} → {destination}", 0)

    add_output(f"Selected Nodes: {node_set if node_set else "All"}", 1)
    add_output(f"Selected Beams: {beam_set if beam_set else "All"}", 1)

    for load_case_i in [source]:
        set_load_case_active(load_object, load_case_i)
        load_count_i = get_load_item_count(load_object, load_case_i)
        load_types_i = get_load_item_types(load_object, load_case_i)
        unique_load_types = set([load_type_i_x[1] for load_type_i_x in load_types_i])

        load_type_incidences = {x: [] for x in unique_load_types}
        
        # Process load type incidences
        for load_type_i in unique_load_types:
            load_type_i_count = get_load_type_count(load_object, load_case_i, load_type_i)
            
            for load_index in range(load_type_i_count):
                load_incidences = get_assignment_for_load_type(load_object, load_type_i, load_case_i, load_index)
                load_type_incidences[load_type_i].append(load_incidences)
        
        if generate_markdown:
            # Create concise incidences table
            add_output("| Load Type | Incidences |", 6)
            add_output("|-----------|------------|", 6)
            
            for load_type, incidences_list in load_type_incidences.items():
                if incidences_list and any(incidences_list):
                    # Combine all incidences for this load type
                    all_incidences = []
                    for incidences in incidences_list:
                        if incidences:
                            if isinstance(incidences, (list, tuple)):
                                all_incidences.extend(incidences)
                            else:
                                all_incidences.append(incidences)
                    
                    if all_incidences:
                        incidence_str = str(sorted(set(all_incidences)))
                        # if len(incidence_str) > 40:
                        #     incidence_str = incidence_str[:37] + "..."
                        add_output(f"| {load_type} | `{incidence_str}` |", 6)
            add_output("")

        # Process loads and show results
        results = []
        
        for load_index, load_type_i in load_types_i:
            if load_type_i == LoadItemNo.NodalLoad_Node:
                if (load_type_i in load_type_incidences and 
                    len(load_type_incidences[load_type_i]) > 0 and
                    load_type_incidences[load_type_i][0] is not None):
                    
                    node_forces = get_nodal_load_info(load_object, load_case_i, load_index)
                    if destination:
                        set_load_case_active(load_object, destination)
                        for node_i in load_type_incidences[load_type_i][0]:
                            if((node_set and node_i in node_set) or (not node_set)):
                                transformed_forces = list(map(predicate, node_forces['forces']))
                                success = load_object.AddNodalLoad(node_i, *transformed_forces)
                                results.append(f"Node {node_i}: {'✅' if success else '❌'}")
                            else:
                                results.append(f"Node {node_i}: {'❌'}")


            elif load_type_i in [LoadItemNo.ConcentratedForce, LoadItemNo.UniformForce]:
                if (load_type_i in load_type_incidences and 
                    len(load_type_incidences[load_type_i]) > 0 and
                    load_type_incidences[load_type_i][0] is not None):
                    
                    member_forces = get_member_load_info(load_object, load_case_i, load_index)
                    if destination:
                        set_load_case_active(load_object, destination)
                        
                        for beam_i in load_type_incidences[load_type_i][0]:

                            if(((beam_set and beam_i in beam_set) or (not beam_set)) and 
                                ((not source_direction) or (source_direction == member_forces['direction']))):

                                force_direction = destination_direction if destination_direction else member_forces['direction']
                                transformed_force = first_non_zero(list(map(predicate, member_forces['forces'])))
                                
                                if load_type_i == LoadItemNo.ConcentratedForce:
                                    distances = member_forces['distances'][:2]
                                    success = load_object.AddMemberConcForce(beam_i, force_direction, 
                                                                        transformed_force, *distances)
                                elif load_type_i == LoadItemNo.UniformForce: 
                                    distances = member_forces['distances']
                                    success = load_object.AddMemberUniformForce(beam_i, force_direction, 
                                                                            transformed_force, *distances)
                                
                                results.append(f"Beam {beam_i}: {'✅' if success else '❌'}")
                            else:
                                results.append(f"Beam {beam_i}: {'❌'}")

            # Clean up processed incidences
            if (destination and load_type_i in load_type_incidences and 
                len(load_type_incidences[load_type_i]) > 0):
                load_type_incidences[load_type_i].pop(0)
        
        # Show results
        if generate_markdown and results:
            add_output("Results", 1)
            for result in results:
                add_output(result, 5)
    
    # Return markdown content if requested
    if generate_markdown:
        return "\n".join(markdown_content)
    
    return None


def convert_force_operation_to_markdown(STAAD_objects: OpenSTAAD_objects, 
                                        transform_load_case_object: TransformLoadCase,
                                        nodes: List[int] = None, 
                                        beams: List[int] = None):
    """
    Convenience function to generate markdown output for force conversion operation
    
    Returns:
        str: Markdown formatted string of the conversion process
    """
    return convert_force_operation(STAAD_objects=STAAD_objects, 
                                    transform_load_case_object=transform_load_case_object, 
                                    nodes=nodes,
                                    beams= beams, 
                                    generate_markdown=True)


# Example usage functions for Jupyter notebook
def display_conversion_markdown(STAAD_objects: OpenSTAAD_objects, 
                                transform_objects:List[TransformLoadCase],
                                nodes: List[int] = None, 
                                beams: List[int] = None):
    """
    Display conversion results as markdown in Jupyter notebook
    
    Args:
        STAAD_objects: OpenSTAAD objects
        transform_objects: List of TransformLoadCase objects
    """
    from IPython.display import display, Markdown
    from datetime import datetime
    
    all_markdown = []
    all_markdown.append("# Load Case Conversion Report")
    all_markdown.append(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    all_markdown.append("")
    
    for i, transform_obj in enumerate(transform_objects, 1):
        all_markdown.append(f"---")
        all_markdown.append("")
        markdown_result = convert_force_operation_to_markdown(STAAD_objects=STAAD_objects, transform_load_case_object=transform_obj,nodes=nodes,beams=beams)
        all_markdown.append(markdown_result)
        all_markdown.append("")
    
    # Display the complete markdown
    display(Markdown("\n".join(all_markdown)))
    
    return "\n".join(all_markdown)


def save_conversion_report(STAAD_objects: OpenSTAAD_objects, 
                           transform_objects:List[TransformLoadCase],
                           nodes: List[int] = None, 
                           beams: List[int] = None, 
                           filename="load_conversion_report.md"):
    """
    Save conversion results to a markdown file
    
    Args:
        STAAD_objects: OpenSTAAD objects
        transform_objects: List of TransformLoadCase objects
        filename: Output filename for the markdown report
    """
    from datetime import datetime
    
    markdown_content = display_conversion_markdown(STAAD_objects=STAAD_objects, transform_objects=transform_objects,nodes=nodes,beams=beams)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Conversion report saved to: {filename}")
    return filename