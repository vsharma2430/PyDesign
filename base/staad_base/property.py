from base.staad_base.com_array import *
from base.helper.wrapper import *

def get_section_property_count(property):
    return property.GetSectionPropertyCount()

def get_section_name(property,property_no):
    return property.GetSectionPropertyName(property_no)

def get_beam_property_name(property,beam_no):
    return property.GetBeamSectionDisplayName(beam_no)

def get_property_id(property,beam_no):
    return property.GetBeamSectionPropertyRefNo(beam_no)
    
@memoize_profile_creation
def create_beam_property(property,Country, SectionName, TypeSpec, AddSpec_1, AddSpec_2):
    return property.CreateBeamPropertyFromTable(Country,SectionName,TypeSpec,AddSpec_1,AddSpec_2)

def assign_beam_property(property,beam_no,property_no):
    return property.AssignBeamProperty(beam_no,property_no)

def assign_beam_specification(property,beam_no,spec_no):
    return property.AssignMemberSpecToBeam(beam_no,spec_no)

def set_DOFReleaseArray(fx=0,fy=0,fz=0,mx=0,my=1,mz=1):
    return make_safe_array_int(6).create([fx,fy,fz,mx,my,mz])

def get_start_end_release_function (property,start_release_spec,end_release_spec):
    def set_start_end_release(beam_ids):
        for beam_id in beam_ids:
            assign_beam_specification(property,beam_id,start_release_spec)
            assign_beam_specification(property,beam_id,end_release_spec)
    return set_start_end_release

assign_specification = lambda property : lambda beams,spec_no : list(map(lambda beam: assign_beam_specification(property=property, beam_no=beam,spec_no=spec_no), [*beams]))
assign_profile = lambda property : lambda beams,property_no : list(map(lambda beam: assign_beam_property(property=property, beam_no=beam,property_no=property_no), [*beams]))