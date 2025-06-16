from base.staad_base.root import *
from base.staad_base.geometry import *
from base.staad_base.load import *
from base.staad_base.com_array import *
from base.staad_base.helper import *

def get_steel_design_result(output,beam_number:int):
    DesignCode,ptr1 = get_ctype_string()
    DesignStatus,ptr2 = get_ctype_string()
    CriticalRatio,ptr3 = get_ctype_double()
    AllowableRatio,ptr4 = get_ctype_float()
    CriticalLoadCase,ptr5 = get_ctype_double()
    CriticalSection,ptr6 = get_ctype_string()
    CriticalClause,ptr7 = get_ctype_string()
    DesignSection,ptr8 = get_ctype_string()

    safe_array_list = make_safe_array_double(3)
    DesignForces = make_variant_vt_ref(safe_array_list, automation.VT_ARRAY | automation.VT_R8)

    KLByR,ptr10 = get_ctype_double()

    output.GetMemberSteelDesignResults(beam_number,DesignCode,DesignStatus,ptr3,ptr4,ptr5,ptr6,ptr7,ptr8,DesignForces,ptr10)
    
    return{
        'beam':beam_number,
        'critical_ratio':CriticalRatio.value,
        'allowable_ratio':AllowableRatio.value,
        'design_forces':open_array(DesignForces.value),
        'klbyr':KLByR.value,
        'critical_ratio_failure':CriticalRatio.value>AllowableRatio.value,
    }

def get_member_steel_design_results(output,beam_numbers=[]):
    result = {}
    for beam_no in beam_numbers:
        result[beam_no] = get_steel_design_result(output,beam_no)
    return result

def assign_design_command(design,breif_no=1,name=None,value=1,members:list=[]):
    return design.AssignDesignCommand(breif_no,name,value,make_safe_array_long(len(members),values=members))

def assign_design_parameter(design,breif_no=1,name=None,value=1,members:list=[]):
    return design.AssignDesignParameter(breif_no,name,value,make_safe_array_long(len(members),values=members))