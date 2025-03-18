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

    #nodal load
    load._FlagAsMethod("AddNodalLoad")
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

    object_dict = {'geometry':geometry,'output':output}

    return os,object_dict
