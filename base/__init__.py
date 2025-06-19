from collections import defaultdict
import pyperclip
from IPython.display import display, Markdown
import ipywidgets as widgets
from base.piperack.piperack import *
from base.helper.general import *
from base.geometry_base.line import *
from base.geometry_base.rectangle import *
from base.staad_base.geometry import *
from base.structural_elements.beam import *
from base.structural_elements.column import *
from base.structural_elements.brace import *
from base.piperack.portal import *
from base.piperack.piperack import *
from base.piperack.tier import *
from base.load.nodal_load import *
from base.load.uniform_load import *
from base.staad_base.design import *
from base.staad_base.property import *
from output.md_output import *
from base.staad_base.optimise_member import *
from base.insturmentation_elements.duct import *
from base.structural_elements.walkway import *
from base.piping_elements.flare import *
from base.structural_elements.tree_support import *
from base.load.wind_load import *
from base.staad_base.transform_force import *
from base.pipe_connection.staad_helper import *
from output.button_bar import *
from base.eil.steel_section import *
from base.structural_elements.group import *
from output.profile_table import *
from output.profile_dropdown import *
from output.model_results import *

openSTAAD,STAAD_objects = get_openSTAAD()

geometry = STAAD_objects.geometry
property = STAAD_objects.property
output = STAAD_objects.output
support = STAAD_objects.support
load = STAAD_objects.load
design = STAAD_objects.design

add_beams = add_beams_fn(geometry=geometry)
select_beams = select_beams_fn(geometry=geometry)
assign_profile = assign_profile(property=property)
assign_specification = assign_specification(property=property)

add_conc_forces_to_members = add_conc_forces_to_members_fn(load)
add_uniform_forces_to_members = add_uniform_forces_to_members_fn(load)

simple_create_concrete_beam_property = simple_create_concrete_beam_property_fn(property=property)
simple_create_steel_beam_property = simple_create_steel_beam_property_fn(property=property)

def beam_list_select_and_display(beam_list):
    select_beams(beam_list.keys())
    display(beam_list)

staad_format_id_list = lambda ids : format_consecutive_numbers(group_consecutive_numbers(ids))
staad_format_beam_list = lambda beams : staad_format_id_list([beam.id for beam in beams])

def beam_list_copy_and_display(beam_list):
    if(len(beam_list)> 0 ):
        selected_members = staad_format_id_list(beam_list)
        pyperclip.copy(f'{selected_members}')
        display(Markdown(f'copied **{len(beam_list)}** members : {selected_members}'))
    else:
        display(Markdown(f'No member selected'))

def open_staad_helper_wrapper(predicate):
    open_staad_helper()
    sleep(5)
    predicate()
    sleep(5)

def get_section_ref_no(selected_section,
                       staad_section_ref_nos):
    
    if(selected_section.staad_name):
        if(selected_section.staad_name in staad_section_ref_nos):
            return staad_section_ref_nos[selected_section.staad_name]['id']
        else:
            return simple_create_steel_beam_property(profile=selected_section.staad_name)
    else:
        return None