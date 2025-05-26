from base.staad_base.com_array import *

def get_section_property_count(property):
    return property.GetSectionPropertyCount()

def get_section_name(property,property_no):
    return property.GetSectionPropertyName(property_no)
    
def assign_beam_property(property,beam_no,property_no):
    return property.AssignBeamProperty(beam_no,property_no)