from functools import lru_cache
from base.staad_base.com_array import *
from base.staad_base.helper import *
from base.staad_base.load_enum import *
from base.load.conc_load import *
from base.load.conc_moment import *
from base.load.uniform_load import *
from base.load.uniform_moment import *
from base.structural_elements.beam import *

open_array = lambda array,index=1 : [x[index] for x in enumerate(array)]

    
def get_load_count(load) -> int:
    loadCount = load.GetPrimaryLoadCaseCount()
    return loadCount 

def get_load_type_count(load,load_case,load_type:LoadType) -> int:
    if(load_case):
        set_load_case_active(load,load_case)

    loadCount = load.GetLoadTypeCount(load_type)
    return loadCount 

def get_load_list_count(load) -> list:
    loadCount = load.GetLoadListCount()
    return loadCount 

def get_load_count_in_load_list(load,load_list_index:int) -> list:
    loadCount = load.GetLoadCountInLoadList(load_list_index)	
    return loadCount 

def set_load_case_active(load,load_case_no) -> bool:
    return load.SetLoadActive(load_case_no)

def get_list_size_for_load_type(load,loadType,loadIndex):
    return load.GetListSizeForLoadType(loadType,loadIndex)

def get_load_nos(load) -> list[int]:
    loadCount = get_load_count(load=load)
    safe_array_load_list = make_safe_array_long(loadCount)
    loads = make_variant_vt_ref(safe_array_load_list, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer
    load.GetPrimaryLoadCaseNumbers(loads)
    return open_array(loads[0])

def get_load_item_count(load,load_no:int) -> list:
    loadItemCount = load.GetLoadItemsCount(load_no)
    return loadItemCount 

def get_load_item_types(load,load_no:int,load_count:int=None) -> list:
    loadItemCount = load_count if load_count != None else load.GetLoadItemsCount(load_no)
    result = []

    for load_item_index in range(loadItemCount):
        loadItemType = load.GetLoadItemType(load_no,load_item_index)
        result.append((load_item_index,loadItemType))
    return result

def get_load_in_load_lists(load,load_list_index:int,tuple:bool=True) -> list:
    loadCount = get_load_count_in_load_list(load=load,load_list_index=load_list_index)
    safe_array_load_list = make_safe_array_long(loadCount)
    loads = make_variant_vt_ref(safe_array_load_list, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer
    load.GetLoadsInLoadList(load_list_index,loads)
    loads = loads[0]
    result = []
    for load in enumerate(loads):
        if(tuple):
            result.append((load[0],load[1]))
        else:
            result.append({'id':load[0],'no':load[1]})
    return result

@try_catch_wrapper
def get_assignment_for_load_type(load,load_type,load_case,load_index):
    if(load_case):
        set_load_case_active(load,load_case)

    if(load_type not in (LoadItemNo.RepeatLoad, LoadItemNo.RepeatLoadData,LoadItemNo.Load1893,4111,4110)):
        list_size_for_load_type_i = get_list_size_for_load_type(load,load_type,load_index)

        if(list_size_for_load_type_i > 0):
            safe_array_load_list = make_safe_array_int(list_size_for_load_type_i)
            loads = make_variant_vt_ref(safe_array_load_list, automation.VT_ARRAY | automation.VT_I4)
            load.GetAssignmentListForLoadType(load_type,load_index,loads)
            return open_array(loads[0])
    return None

def get_nodal_load_count(load,node_no:int) -> list:
    nodalLoadCount = load.GetNodalLoadCount(node_no)
    return nodalLoadCount 

def get_nodal_load_info(load,load_case,load_index_no:int) -> list:
    if(load_case):
        set_load_case_active(load,load_case)

    safe_array_load_list = make_safe_array_double(6)
    forces = make_variant_vt_ref(safe_array_load_list, automation.VT_ARRAY | automation.VT_R8)
    load.GetNodalLoadInfo(load_index_no,forces)
    forces = forces[0]
    return {'forces':list(map(convert_kn_to_mt,open_array(forces)))}

def get_member_load_info(load,load_case,load_index_no:int) -> list:
    if(load_case):
        set_load_case_active(load,load_case)

    direction,direction_ptr = get_ctype_long()
    safe_array_load_list_1 = make_safe_array_double(3)
    safe_array_load_list_2 = make_safe_array_double(3)

    forces = make_variant_vt_ref(safe_array_load_list_1, automation.VT_ARRAY | automation.VT_R8)
    distances = make_variant_vt_ref(safe_array_load_list_2, automation.VT_ARRAY | automation.VT_R8)

    load.GetMemberLoadInfo(load_index_no,direction_ptr,forces,distances)

    forces = forces[0]
    distances = distances[0]

    return {'direction':direction.value,'forces':list(map(convert_kn_to_mt,open_array(forces))),'distances':open_array(distances)}

def add_member_force(load,BeamNo:int, load_object : ConcentratedLoad):
    return load.AddMemberConcForce(BeamNo,load_object.direction,load_object.force_value,load_object.d1_value,load_object.d2_value)

def add_member_uniform_force(load,BeamNo:int, load_object : UniformLoad):
    return load.AddMemberUniformForce(BeamNo,load_object.direction,load_object.force_value,load_object.d1_value,load_object.d2_value,load_object.d3_value)

add_conc_forces_to_members_fn = lambda load : lambda beams, load_object : list(map(lambda beam: add_member_force(load,beam.id if isinstance(beam,Beam3D) else beam,load_object), [*beams]))
add_uniform_forces_to_members_fn = lambda load : lambda beams, load_object : list(map(lambda beam: add_member_uniform_force(load,beam.id if isinstance(beam,Beam3D) else beam,load_object), [*beams]))