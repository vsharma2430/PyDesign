from comtypes import client

def get_openSTAAD():
    os = client.GetActiveObject("StaadPro.OpenSTAAD")
    geometry = os.Geometry
    output = os.Output
    property = os.Property
    load = os.Load

    #nodes
    geometry._FlagAsMethod("GetNodeCount")
    geometry._FlagAsMethod("GetNodeList")
    geometry._FlagAsMethod("GetNodeIncidence")
    geometry._FlagAsMethod("GetNodeNumber")
    geometry._FlagAsMethod("SelectNode")

    #beams
    geometry._FlagAsMethod("GetMemberCount")
    geometry._FlagAsMethod("GetBeamList") 
    geometry._FlagAsMethod("GetBeamLength") 
    geometry._FlagAsMethod("GetMemberIncidence") 
    geometry._FlagAsMethod("SelectBeam") 
    geometry._FlagAsMethod("GetNoOfBeamsConnectedAtNode") 
    geometry._FlagAsMethod("GetNoOfSelectedBeams") 
    geometry._FlagAsMethod("GetSelectedBeams") 
    geometry._FlagAsMethod("RenumberBeam") 

    #groups
    geometry._FlagAsMethod("GetGroupCountAll") 
    geometry._FlagAsMethod("GetGroupCount") 
    geometry._FlagAsMethod("GetGroupEntityCount") 
    geometry._FlagAsMethod("GetGroupEntities") 
    geometry._FlagAsMethod("GetGroupNames") 

    #property
    property._FlagAsMethod('GetBeamSectionDisplayName')
    property._FlagAsMethod('GetBeamSectionName')
    property._FlagAsMethod('GetBeamSectionPropertyRefNo')
    property._FlagAsMethod('GetBeamSectionPropertyTypeNo')
    property._FlagAsMethod('GetCountofSectionPropertyValuesEx')
    property._FlagAsMethod('GetCountofSectionPropertyValuesEx')

    property._FlagAsMethod('GetSectionPropertyCount')
    property._FlagAsMethod('GetSectionPropertyName')
    property._FlagAsMethod('GetSectionPropertyType')
    property._FlagAsMethod('GetSectionPropertyValues')
    property._FlagAsMethod('GetSectionPropertyValuesEx')
    property._FlagAsMethod('GetMemberReleaseSpecEx')
    property._FlagAsMethod('GetSectionTableNo')
    
    property._FlagAsMethod('AssignBeamProperty')
    property._FlagAsMethod('CreateAssignProfileProperty')

    #loads
    load._FlagAsMethod("GetPrimaryLoadCaseCount")
    load._FlagAsMethod("GetPrimaryLoadCaseNumbers")
    load._FlagAsMethod("SetLoadActive")

    #load case operations
    load._FlagAsMethod("ClearPrimaryLoadCase")
    load._FlagAsMethod("ClearReferenceLoadCase")
    load._FlagAsMethod("CreateLoadList")
    load._FlagAsMethod("CreateNewPrimaryLoad")
    load._FlagAsMethod("CreateNewPrimaryLoadEx")
    load._FlagAsMethod("CreateNewPrimaryLoadEx2")
    load._FlagAsMethod("DeleteLoadList")
    load._FlagAsMethod("DeletePrimaryLoadCases")
    load._FlagAsMethod("DeleteReferenceLoadCases")
    load._FlagAsMethod("GetActiveLoad")
    load._FlagAsMethod("GetAssignmentListForLoadType")
    load._FlagAsMethod("GetAttribute")
    load._FlagAsMethod("GetListSizeForLoadType")
    load._FlagAsMethod("GetLoadCaseTitle")
    load._FlagAsMethod("GetLoadCountInLoadList")
    load._FlagAsMethod("GetLoadItemsCount")
    load._FlagAsMethod("GetLoadItemType")
    load._FlagAsMethod("GetLoadListCount")
    load._FlagAsMethod("GetLoadsInLoadList")
    load._FlagAsMethod("GetLoadType")
    load._FlagAsMethod("GetLoadTypeCount")
    load._FlagAsMethod("GetPrimaryLoadCaseNumbers")
    load._FlagAsMethod("RemoveAttribute")
    load._FlagAsMethod("SetASDLoadAttribute")
    load._FlagAsMethod("SetLoadType")
    load._FlagAsMethod("SetLSDLoadAttribute")

    #self-weight load  
    load._FlagAsMethod("AddSelfWeightInXYZ")
    load._FlagAsMethod("AddSelfWeightInXYZToGeometry")

    #nodal load  
    load._FlagAsMethod("AddNodalLoad")
    load._FlagAsMethod("AddSupportDisplacement")
    load._FlagAsMethod("GetNodalLoadCount")
    load._FlagAsMethod("GetNodalLoadInfo")
    load._FlagAsMethod("GetNodalLoads")

    #member load
    load._FlagAsMethod("AddMemberAreaLoad")
    load._FlagAsMethod("AddMemberConcForce")
    load._FlagAsMethod("AddMemberConcMoment")
    load._FlagAsMethod("AddMemberFixedEnd")
    load._FlagAsMethod("AddMemberLinearVari")
    load._FlagAsMethod("AddMemberTrapezoidal")
    load._FlagAsMethod("AddMemberUniformForce")
    load._FlagAsMethod("AddMemberUniformMoment")
    load._FlagAsMethod("GetConcForceCount")
    load._FlagAsMethod("GetConcForces")
    load._FlagAsMethod("GetConcMomentCount")
    load._FlagAsMethod("GetConcMoments")
    load._FlagAsMethod("GetLinearVaryingLoadCount")
    load._FlagAsMethod("GetLinearVaryingLoads")
    load._FlagAsMethod("GetMemberLoadInfo")
    load._FlagAsMethod("GetTrapLoadCount")
    load._FlagAsMethod("GetTrapLoads")
    load._FlagAsMethod("GetUDLLoadCount")
    load._FlagAsMethod("GetUDLLoads")
    load._FlagAsMethod("GetUNIMomentCount")
    load._FlagAsMethod("GetUNIMoments")

    load._FlagAsMethod("AddSeismicLoad")
    load._FlagAsMethod("IsDynamicLoadIncluded")

    load._FlagAsMethod("AddWindLoad")

    #output
    output._FlagAsMethod("GetSupportReactions")

    object_dict = {'geometry':geometry,'output':output,'load':load,'property':property}

    return os,object_dict
