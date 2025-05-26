from enum import IntEnum
from base.staad_base.com_array import *
from base.staad_base.helper import *

open_array = lambda array,index=1 : [x[index] for x in enumerate(array)]

class LoadType(IntEnum):
    Dead = 0
    Live = 1
    RoofLive = 2
    Wind = 3
    SeismicH = 4
    SeismicV = 5
    Snow = 6
    Fluids = 7
    Soil = 8
    Rain = 9
    Ponding = 10
    Dust = 11
    Traffic = 12
    Temp = 13
    Imperfection = 14
    Accidental = 15
    Flood = 16
    Ice = 17
    WindIce = 18
    CraneHook = 19
    Mass = 20
    Gravity = 21
    Push = 22
    NoneType = 23  # 'None' is a reserved keyword in Python

class LoadItemNo(IntEnum):
    SelfWeight = 4000
    NodalLoad_Node = 3110
    NodalLoad_Inclined = 3120
    NodalLoad_SupportDisplacement = 3910
    NodalLoad_RegionNodeLoad = 3312
    UniformForce = 3210
    UniformMoment = 3220
    ConcentratedForce = 3230
    ConcentratedMoment = 3240
    LinearVarying = 3250
    Trapezoidal = 3260
    Hydrostatic = 3261
    PrePostStress = 3620
    FixedEnd = 3810
    UniformForce_Physical = 3275
    UniformMoment_Physical = 3280
    ConcentratedForce_Physical = 3285
    ConcentratedMoment_Physical = 3290
    Trapezoidal_Physical = 3295
    Area = 3410
    FloorLoadYrange = 3510
    FloorLoadXrange = 3511
    FloorLoadZrange = 3520
    FloorLoadGroup = 3530
    OneWayFloorLoadXrange = 3551
    OneWayFloorLoadYrange = 3552
    OneWayFloorLoadZrange = 3553
    OneWayFloorLoadGroup = 3554
    PressureFullPlate = 3310
    ConcentratedLoad_Plate = 3311
    PartialPlatePressure = 3312
    Trapezoidal_Plate = 3320
    Solid = 3322
    Temperature = 3710
    Strain = 3720
    StrainRate = 3721
    UBCLoad = 4400
    WindLoad = 4600
    WindLoadDynamic = 4610
    IbcLoad = 4405
    Load1893 = 4410
    AijLoad = 4500
    ColombianLoad = 4510
    CFELoad = 4520
    RPALoad = 4530
    NTCLoad = 4540
    NRCLoad = 4550
    NRCLoad2005 = 4560
    NRCLoad2010 = 4561
    TurkishLoad = 4570
    GB50011Load = 4575
    Colombian2010Load = 4576
    TimeHistoryLoad = 4820
    SnowLoadData = 4651
    RepeatLoadData = 4201
    NotionalLoadData = 4223
    ReferenceLoad = 4220
    SpectrumLoad = 4100
    SpectrumData = 4101
    CalculateNaturalFrequency = 4700
    ModalCalculationRequested = 4710
    CalculateRayleighFrequency = 4701
    SnowLoad = 4650
    RepeatLoad = 4200
    NotionalLoad = 4222


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