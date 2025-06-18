from base.geometry_base.rectangle import *
from base.geometry_base.circle import *
from base.staad_base.com_array import *
from base.helper.wrapper import *

def get_section_property_count(property) -> int:
    return property.GetSectionPropertyCount()

def get_section_name(property,property_no) -> int:
    return property.GetSectionPropertyName(property_no)

def get_beam_property_name(property,beam_no) -> str:
    return property.GetBeamSectionDisplayName(beam_no)

def get_property_id(property,beam_no) -> int:
    return property.GetBeamSectionPropertyRefNo(beam_no)
    
def assign_beam_property(property,beam_no,property_no) -> bool:
    return property.AssignBeamProperty(beam_no,property_no)

def assign_beam_specification(property,beam_no,spec_no) -> bool:
    return property.AssignMemberSpecToBeam(beam_no,spec_no)

def set_DOFReleaseArray(fx=0,fy=0,fz=0,mx=0,my=1,mz=1) -> int:
    return make_safe_array_int(6).create([fx,fy,fz,mx,my,mz])

def get_start_end_release_function (property,start_release_spec,end_release_spec):
    def set_start_end_release(beam_ids) -> list[tuple[bool,bool]]:
        result = []
        for beam_id in beam_ids:
            result.append((assign_beam_specification(property,beam_id,start_release_spec),\
                            assign_beam_specification(property,beam_id,end_release_spec)))
        return result
    return set_start_end_release

@memoize_steel_profile_creation
def create_steel_beam_property(property,Country, SectionName, TypeSpec, AddSpec_1, AddSpec_2):
    return property.CreateBeamPropertyFromTable(Country,SectionName,TypeSpec,AddSpec_1,AddSpec_2)

@memoize_concrete_profile_creation
def create_concrete_beam_property(property,geometry):
    if(isinstance(geometry,Rectangle)):
        return property.CreatePrismaticRectangleProperty(geometry.length,geometry.width)
    elif(isinstance(geometry,Circle)):
        return property.CreatePrismaticCircleProperty(geometry.radius)
    else:
        return None
    
def assign_material_to_beam(property,material_name,beam_no):
    return property.AssignMaterialToMember(material_name,beam_no)

assign_specification = lambda property : lambda beams,spec_no : list(map(lambda beam: assign_beam_specification(property=property, beam_no=beam,spec_no=spec_no), [*beams]))
assign_profile = lambda property : lambda beams,property_no : list(map(lambda beam: assign_beam_property(property=property, beam_no=beam,property_no=property_no), [*beams]))
assign_material = lambda property : lambda material_name : lambda beams : list(map(lambda beam: assign_material_to_beam(property=property, beam_no=beam,material_name=material_name), [*beams]))

simple_create_concrete_beam_property_fn = lambda property : lambda profile : create_concrete_beam_property(property,profile)
simple_create_steel_beam_property_fn = lambda property: (
    lambda country=None, profile='': (
        create_steel_beam_property(
            property,
            (35 if ('SHS' in profile or 'RHS' in profile) else 10) if country is None else country,
            profile,0,  0,  0   
        )))