import ipywidgets as widgets
from IPython.display import HTML,display
from output.dark_theme import *

def create_steel_section_widget(sections):
    """
    Create a detailed widget with dropdown and HTML info display
    """
    # Group sections by intended use, then by classification
    from collections import defaultdict
    
    grouped = defaultdict(lambda: defaultdict(list))
    for section in sections:
        grouped[section.intended_use][section.classification].append(section)
    
    # Create grouped options for dropdown
    options = []
    
    # Sort intended uses alphabetically by their string value
    for intended_use in sorted(grouped.keys(), key=lambda x: x.value):
        # Add a separator/header for intended use (disabled option)
        options.append((f"─── {intended_use.value} ───", None))
        
        # Sort classifications within each intended use by their string value
        for classification in sorted(grouped[intended_use].keys(), key=lambda x: x.value):
            # Add classification subheader if there are multiple classifications
            if len(grouped[intended_use]) > 1:
                options.append((f"  └── {classification.value}", None))
            
            # Sort sections by section name within each classification
            sorted_sections = sorted(grouped[intended_use][classification], 
                                   key=lambda x: x.section)
            
            for section in sorted_sections:
                indent = "    " if len(grouped[intended_use]) > 1 else "  "
                display_name = f"{indent}{section.section} ({section.unit_wt_kg_m} kg/m) - ({section.classification.value})"
                options.append((display_name, section))
    
    # Find first actual section (not a separator) for default value
    default_value = None
    for _, value in options:
        if value is not None:
            default_value = value
            break
    
    dropdown = widgets.Dropdown(
        options=options,
        value=default_value,
        description='Steel Section:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='400px')
    )
    
    # Create HTML widget for details display
    details_html = widgets.HTML()

    def format_section_html(section):
        """Format section data as HTML"""
        return f"""
        <div style="background-color: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px; padding: 20px; margin-top: 10px; font-family: Arial, sans-serif;">
            <h3 style="color: #495057; margin-top: 0; margin-bottom: 15px; border-bottom: 2px solid #007bff; padding-bottom: 5px;">
                📋 Section Details
            </h3>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background-color: #e9ecef;">
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; width: 40%;">EIL Serial No:</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6;">{section.sl_no}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold;">Section:</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #007bff;">{section.section}</td>
                </tr>
                <tr style="background-color: #e9ecef;">
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold;">Unit Weight:</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6;">{section.unit_wt_kg_m} kg/m</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold;">Classification:</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6;">
                        <span style="background-color: #28a745; color: white; padding: 3px 8px; border-radius: 12px; font-size: 12px;">
                            {section.classification.value}
                        </span>
                    </td>
                </tr>
                <tr style="background-color: #e9ecef;">
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold;">Intended Use:</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6;">{section.intended_use.value}</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold;">STAAD Name:</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6;">{section.staad_name}</td>
                </tr>
            </table>
        </div>
        """
    
    def update_details(change):
        """Update the HTML details display when selection changes"""
        section = change['new']
        # Only update if a valid section is selected (not a separator)
        if section is not None:
            details_html.value = format_section_html(section)
    
    # Initial display
    if dropdown.value:
        details_html.value = format_section_html(dropdown.value)
    
    dropdown.observe(update_details, names='value')
    
    # Create vertical box layout
    steel_widget = widgets.VBox([
        dropdown,
        details_html
    ], layout=widgets.Layout(padding='10px'))
    
    return steel_widget, dropdown



def create_button(label,predicate):
    button = widgets.Button(
        description=label,
        layout=dark_layout,
    )
    
    def on_button_clicked(b):
        predicate()
        return
    
    button.on_click(on_button_clicked)
    return button

def insert_profile_button_click(get_section_ref_no,
                                steel_dropdown,
                                staad_section_ref_nos,
                                simple_create_steel_beam_property):
    
    selected_section = steel_dropdown.value
    ref_no = get_section_ref_no(selected_section=selected_section,
                                staad_section_ref_nos=staad_section_ref_nos,
                                simple_create_steel_beam_property=simple_create_steel_beam_property)
    
    display({'section':steel_dropdown.value.staad_name,'ref_no':ref_no})
    return

def apply_profile_button_click(get_section_ref_no,
                               steel_dropdown,
                               staad_section_ref_nos,
                               simple_create_steel_beam_property,
                               geometry,get_selected_beam_nos,
                               beam_list_copy_and_display,
                               assign_profile):
    
    selected_section = steel_dropdown.value
    selected_beams = get_selected_beam_nos(geometry=geometry)
    beam_list_copy_and_display(selected_beams)
    display(assign_profile(beams=selected_beams,property_no=get_section_ref_no(selected_section=selected_section,
                                                                        staad_section_ref_nos=staad_section_ref_nos,
                                                                        simple_create_steel_beam_property=simple_create_steel_beam_property)))
    return
