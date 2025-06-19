import ipywidgets as widgets
from IPython.display import HTML, display
from collections import defaultdict
from output.dark_theme import dark_layout, dark_vbox

def create_steel_section_widget(sections):
    """Create a widget with dropdown and HTML info display."""
    # Group sections
    grouped = defaultdict(lambda: defaultdict(list))
    for s in sections:
        grouped[s.intended_use][s.classification].append(s)

    # Create dropdown options
    options = []
    for use in sorted(grouped, key=lambda x: x.value):
        options.append((f"─── {use.value} ───", None))
        for cls in sorted(grouped[use], key=lambda x: x.value):
            if len(grouped[use]) > 1:
                options.append((f"   └─── {cls.value}", None))
            for s in sorted(grouped[use][cls], key=lambda x: x.sl_no):
                indent = "    " if len(grouped[use]) > 1 else "  "
                options.append((f"{indent}{s.section} ({s.unit_wt_kg_m} kg/m) - ({cls.value})", s))

    # Set default value
    default = next((v for _, v in options if v), None)
    dropdown = widgets.Dropdown(
        options=options,
        value=default,
        description='Steel Section : ',
        style={'description_width': 'initial'},
        layout={'width': '550px', 'margin': '5px'}
    )
    details_html = widgets.HTML(layout={'width': '550px', 'margin': '5px'})

    def format_section_html(section, theme='dark'):
        """Format section data as HTML."""
        themes = {
            'dark': {
                'bg': '#1e1e1e', 'border': '#444', 'text': '#fff', 'header': '#fff', 'accent': '#00bfff',
                'table_border': '#555', 'row_alt': '#2a2a2a', 'row': '#252525', 'label': '#fff',
                'section': '#00bfff', 'value': '#fff', 'badge_bg': '#28a745', 'badge_text': '#fff', 'unit': '#ccc'
            }
        }
        c = themes[theme]
        get_val = lambda obj, attr, default='N/A': getattr(obj, attr, default).value if hasattr(getattr(obj, attr, default), 'value') else getattr(obj, attr, default)

        return f"""
        <div style="background: {c['bg']}; border: 1px solid {c['border']}; border-radius: 8px; padding: 2%; margin: 0; font-family: Arial; color: {c['text']}; width: 100%;">
            <h3 style="color: {c['header']}; margin: 0 0 15px; border-bottom: 2px solid {c['accent']}; padding-bottom: 5px; font-weight: bold;">📋 Section Details</h3>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: {c['row_alt']};"><td style="padding: 12px; border: 1px solid {c['table_border']}; font-weight: bold; width: 40%; color: {c['label']};">EIL Serial No:</td><td style="padding: 12px; border: 1px solid {c['table_border']}; color: {c['value']}; font-weight: bold;">{get_val(section, 'sl_no')}</td></tr>
                <tr style="background: {c['row']};"><td style="padding: 12px; border: 1px solid {c['table_border']}; font-weight: bold; color: {c['label']};">Section:</td><td style="padding: 12px; border: 1px solid {c['table_border']}; color: {c['section']}; font-size: 16px; font-weight: bold;">{get_val(section, 'section')}</td></tr>
                <tr style="background: {c['row_alt']};"><td style="padding: 12px; border: 1px solid {c['table_border']}; font-weight: bold; color: {c['label']};">Unit Weight:</td><td style="padding: 12px; border: 1px solid {c['table_border']}; text-align: right; color: {c['value']}; font-weight: bold;"><span style="font-size: 15px;">{get_val(section, 'unit_wt_kg_m')}</span> <span style="color: {c['unit']}; font-size: 13px;">kg/m</span></td></tr>
                <tr style="background: {c['row']};"><td style="padding: 12px; border: 1px solid {c['table_border']}; font-weight: bold; color: {c['label']};">Classification:</td><td style="padding: 12px; border: 1px solid {c['table_border']};"><span style="background: {c['badge_bg']}; color: {c['badge_text']}; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: bold;">{get_val(section, 'classification')}</span></td></tr>
                <tr style="background: {c['row_alt']};"><td style="padding: 12px; border: 1px solid {c['table_border']}; font-weight: bold; color: {c['label']};">Intended Use:</td><td style="padding: 12px; border: 1px solid {c['table_border']}; color: {c['value']}; font-weight: bold;">{get_val(section, 'intended_use')}</td></tr>
                <tr style="background: {c['row']};"><td style="padding: 12px; border: 1px solid {c['table_border']}; font-weight: bold; color: {c['label']};">STAAD Name:</td><td style="padding: 12px; border: 1px solid {c['table_border']}; color: {c['value']}; font-weight: bold; font-family: monospace; background: #333; border-radius: 4px;">{get_val(section, 'staad_name')}</td></tr>
            </table>
        </div>
        """

    def update_details(change):
        """Update HTML display on selection change."""
        if change['new']:
            details_html.value = format_section_html(change['new'])

    # Initial display
    if dropdown.value:
        details_html.value = format_section_html(dropdown.value)

    dropdown.observe(update_details, names='value')
    # Handle dark_vbox as a list
    if isinstance(dark_vbox, list):
        # If dark_vbox is a list with a dictionary, use the first dictionary
        if dark_vbox and isinstance(dark_vbox[0], dict):
            layout_dict = dark_vbox[0]
        else:
            # Fallback to default layout if dark_vbox is a list but not usable
            layout_dict = {'background': '#1e1e1e', 'border': '1px solid #444', 'padding': '5px'}
    else:
        # Assume dark_vbox is already a dictionary
        layout_dict = dark_vbox if isinstance(dark_vbox, dict) else {}

    # Merge with fixed width properties
    layout_dict.update({
        'width': '600px',
        'max_width': '600px',
        'margin': '5px auto'
    })

    steel_widget = widgets.VBox(
        [dropdown, details_html],
        layout=layout_dict
    )
    return steel_widget, dropdown

def create_button(label, predicate):
    """Create a button with a callback."""
    button = widgets.Button(description=label, layout=dark_layout)
    button.on_click(lambda b: predicate())
    return button

def insert_profile_button_click(get_section_ref_no, steel_dropdown, staad_section_ref_nos):
    """Handle insert profile button click."""
    selected = steel_dropdown.value
    ref_no = get_section_ref_no(selected, staad_section_ref_nos)
    display({'section': selected.staad_name, 'ref_no': ref_no})

def apply_profile_button_click(get_section_ref_no, steel_dropdown, staad_section_ref_nos, geometry,
                               property, get_selected_beam_nos, beam_list_copy_and_display,
                               assign_profile, assign_material):
    """Handle apply profile button click."""
    selected = steel_dropdown.value
    beams = get_selected_beam_nos(geometry)
    beam_list_copy_and_display(beams)
    assign_profile(beams, get_section_ref_no(selected, staad_section_ref_nos))
    assign_material(property)('STEEL')(beams)