import time
from comtypes import client
from enum import IntEnum
from base.staad_base.helper import try_catch_wrapper

class AnalysisStatus(IntEnum):
    """Enum representing the status of an analysis operation."""
    TERMINATED = -1          # Analysis Terminated
    GENERAL_ERROR = 0        # General Error
    IN_PROGRESS = 1          # Analysis is in progress
    COMPLETED_SUCCESS = 2    # Analysis completed without errors or warnings
    COMPLETED_WITH_WARNINGS = 3  # Analysis completed with warnings but without errors
    COMPLETED_WITH_ERRORS = 4    # Analysis completed with errors
    NOT_PERFORMED = 5        # Analysis has not been performed

# Dictionary for message display
ANALYSIS_STATUS_MESSAGES = {
    -1: "Analysis Terminated",
    0: "General Error", 
    1: "Analysis is in progress",
    2: "Analysis completed without errors or warnings",
    3: "Analysis completed with warnings but without errors", 
    4: "Analysis completed with errors",
    5: "Analysis has not been performed"
}

class OpenSTAAD_objects:
    def __init__(self, geometry=None, output=None, load=None, property=None, design=None,support=None):
        self.geometry = geometry if geometry is not None else {}
        self.output = output if output is not None else {}
        self.load = load if load is not None else {}
        self.property = property if property is not None else {}
        self.design = design if design is not None else {}
        self.support = support if support is not None else {}

@try_catch_wrapper
def get_openSTAAD() -> OpenSTAAD_objects:
    os = client.GetActiveObject("StaadPro.OpenSTAAD")

    geometry = os.Geometry
    output = os.Output
    property = os.Property
    load = os.Load
    design = os.Design
    support = os.Support

    os._FlagAsMethod("Analyze")
    os._FlagAsMethod("AnalyzeEx")
    os._FlagAsMethod("AnalyzeModel")
    os._FlagAsMethod("CloseSTAADFile")
    os._FlagAsMethod("CreateNamedView")
    os._FlagAsMethod("GetAnalysisStatus")
    os._FlagAsMethod("GetApplicationVersion")
    os._FlagAsMethod("GetBaseUnit")
    os._FlagAsMethod("GetCONNECTEDProjectInfo")
    os._FlagAsMethod("GetErrorMessage")
    os._FlagAsMethod("GetFullJobInfo")
    os._FlagAsMethod("GetInputUnitForForce")
    os._FlagAsMethod("GetInputUnitForLength")
    os._FlagAsMethod("GetMainWindowHandle")
    os._FlagAsMethod("GetProcessHandle")
    os._FlagAsMethod("GetProcessId")
    os._FlagAsMethod("GetShortJobInfo")
    os._FlagAsMethod("GetSTAADFile")
    os._FlagAsMethod("GetSTAADFileFolder")
    os._FlagAsMethod("IsAnalyzing")
    os._FlagAsMethod("IsPhysicalModel")
    os._FlagAsMethod("ModifyNamedView")
    os._FlagAsMethod("NewSTAADFile")
    os._FlagAsMethod("OpenSTAADFile")
    os._FlagAsMethod("Quit")
    os._FlagAsMethod("RemoveNamedView")
    os._FlagAsMethod("SaveModel")
    os._FlagAsMethod("SaveNamedView")
    os._FlagAsMethod("SetCONNECTEDProjectInfo")
    os._FlagAsMethod("SetFullJobInfo")
    os._FlagAsMethod("SetInputUnitForForce")
    os._FlagAsMethod("SetInputUnitForLength")
    os._FlagAsMethod("SetInputUnits")
    os._FlagAsMethod("SetShortJobInfo")
    os._FlagAsMethod("SetSilentMode")
    os._FlagAsMethod("UpdateStructure")

    #nodes
    geometry._FlagAsMethod("AddNode")
    geometry._FlagAsMethod("GetNodeCount")
    geometry._FlagAsMethod("GetNodeList")
    geometry._FlagAsMethod("GetNodeIncidence")
    geometry._FlagAsMethod("GetNodeNumber")
    geometry._FlagAsMethod("SelectNode")
    geometry._FlagAsMethod("GetNoOfSelectedNodes")
    geometry._FlagAsMethod("GetSelectedNodes")

    #beams
    geometry._FlagAsMethod("AddBeam")
    geometry._FlagAsMethod("GetMemberCount")
    geometry._FlagAsMethod("GetBeamList") 
    geometry._FlagAsMethod("GetBeamLength") 
    geometry._FlagAsMethod("GetMemberIncidence") 
    geometry._FlagAsMethod("ClearMemberSelection") 
    geometry._FlagAsMethod("SelectBeam") 
    geometry._FlagAsMethod("GetNoOfBeamsConnectedAtNode") 
    geometry._FlagAsMethod("GetNoOfSelectedBeams") 
    geometry._FlagAsMethod("GetSelectedBeams") 
    geometry._FlagAsMethod("RenumberBeam") 
    
    geometry._FlagAsMethod("BreakBeamsAtSpecificNodes") 
    geometry._FlagAsMethod("GetCountOfBreakableBeamsAtSpecificNodes") 
    
    geometry._FlagAsMethod("GetIntersectBeamsCount") 
    geometry._FlagAsMethod("IntersectBeams") 
    
    #support
    support._FlagAsMethod("AssignSupportToNode")
    support._FlagAsMethod("CreateSupportFixed")
    support._FlagAsMethod("CreateSupportPinned")
    support._FlagAsMethod("GetSupportCount")
    support._FlagAsMethod("GetSupportNodes")
    support._FlagAsMethod("GetSupportType")

    #groups
    geometry._FlagAsMethod("GetGroupCountAll") 
    geometry._FlagAsMethod("GetGroupCount") 
    geometry._FlagAsMethod("GetGroupEntityCount") 
    geometry._FlagAsMethod("GetGroupEntities") 
    geometry._FlagAsMethod("GetGroupNames") 

    #materials
    property._FlagAsMethod('GetBeamMaterialName')
    property._FlagAsMethod('GetElementMaterialName')
    property._FlagAsMethod('GetIsotropicMaterialAssignedBeamCount')
    property._FlagAsMethod('GetIsotropicMaterialAssignedBeamList')
    property._FlagAsMethod('GetIsotropicMaterialCount')
    property._FlagAsMethod('GetIsotropicMaterialProperties')
    property._FlagAsMethod('GetIsotropicMaterialPropertiesAssigned')
    property._FlagAsMethod('GetMaterialProperty')
    property._FlagAsMethod('GetOrthotropic2DMaterialCount')
    property._FlagAsMethod('GetOrthotropic2DMaterialProperties')
    property._FlagAsMethod('GetOrthotropic3DMaterialCount')
    property._FlagAsMethod('GetOrthotropic3DMaterialProperties')
    property._FlagAsMethod('GetPlateMaterialName')
    property._FlagAsMethod('RemoveBeamMaterialHelper')
    property._FlagAsMethod('RemoveMaterialFromBeam')
        
    property._FlagAsMethod('AssignMaterialToMember')
    property._FlagAsMethod('AssignMaterialToPlate')
    property._FlagAsMethod('AssignMaterialToSolid')
    property._FlagAsMethod('SetMaterialID')
    property._FlagAsMethod('SetMaterialName')

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
    property._FlagAsMethod('CreateBeamPropertyFromTable')
    property._FlagAsMethod('CreatePrismaticCircleProperty')
    property._FlagAsMethod('CreatePrismaticRectangleProperty')
    
    property._FlagAsMethod('CreateMemberReleaseSpec')
    property._FlagAsMethod('CreateMemberTrussSpec')
    property._FlagAsMethod('CreateMemberOffsetSpec')
    property._FlagAsMethod('AssignMemberSpecToBeam')

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
    output._FlagAsMethod("AreResultsAvailable")

    output._FlagAsMethod("GetBasePressures")
    output._FlagAsMethod("GetMatInfluenceAreas")
    output._FlagAsMethod("GetNodeDisplacements")
    output._FlagAsMethod("GetSupportReactions")

    output._FlagAsMethod("GetIntermediateDeflectionAtDistance")
    output._FlagAsMethod("GetIntermediateMemberAbsTransDisplacements")
    output._FlagAsMethod("GetIntermediateMemberForcesAtDistance")
    output._FlagAsMethod("GetIntermediateMemberTransDisplacements")
    output._FlagAsMethod("GetMaxSectionDisplacement")
    output._FlagAsMethod("GetMemberEndDisplacements")
    output._FlagAsMethod("GetMemberEndForces")
    output._FlagAsMethod("GetMinMaxAxialForce")
    output._FlagAsMethod("GetMinMaxBendingMoment")
    output._FlagAsMethod("GetMinMaxShearForce")
    output._FlagAsMethod("GetPMemberEndForces")
    output._FlagAsMethod("GetPMemberIntermediateForcesAtDistance")

    output._FlagAsMethod("CreateSteelDesignCommand")
    
    output._FlagAsMethod("AssignDesignCommand")
    output._FlagAsMethod("AssignDesignGroup")
    output._FlagAsMethod("AssignDesignParameter")
    output._FlagAsMethod("CreateDesignBrief")
    output._FlagAsMethod("GetDesignBriefCode")
    output._FlagAsMethod("GetMemberDesignParameters")
    output._FlagAsMethod("GetMemberDesignSectionName")
    output._FlagAsMethod("GetMemberSteelDesignMaxFailureRatio")
    output._FlagAsMethod("GetMemberSteelDesignMinFailureRatio")
    output._FlagAsMethod("GetMemberSteelDesignRatio")
    output._FlagAsMethod("GetMemberSteelDesignResults")
    output._FlagAsMethod("GetMultipleMemberSteelDesignMaxRatio")
    output._FlagAsMethod("GetMultipleMemberSteelDesignRatio")
    output._FlagAsMethod("GetMultipleMemberSteelDesignResults")
    output._FlagAsMethod("GetSteelDesignParameterBlockCount")
    output._FlagAsMethod("GetSteelDesignParameterBlockNameByIndex")
    output._FlagAsMethod("IsMultipleMemberSteelDesignResultsAvailable")

    return os,OpenSTAAD_objects(geometry=geometry,output=output,load=load,property=property,design=design,support=support)

def run_analysis(openSTAAD,silent=1,hidden=0,wait=0,wait_interval=5):
    openSTAAD.SetSilentMode(1)

    time.sleep(wait_interval/2)
    print('Analysis Started')

    retVal = openSTAAD.AnalyzeEx(silent,hidden,wait)
    count = 1

    while openSTAAD.IsAnalyzing():
        time.sleep(wait_interval)
        print('Analysis running',''.join(['.'*count]))
        count = count + 1
        
    return retVal

def get_staad_file_name():
    import win32com.client
    from win32com.client import VARIANT
    import pythoncom

    try:
        # Initialize COM (required for standalone scripts)
        pythoncom.CoInitialize()

        # Connect to a running STAAD.Pro instance
        objOpenSTAAD = win32com.client.GetObject(Class="StaadPro.OpenSTAAD")

        # Create VARIANT for file name (string, passed by reference)
        fileName = VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, "")
        bFullPath = VARIANT(pythoncom.VT_BOOL, True)

        # Get the STAAD file name
        objOpenSTAAD.GetSTAADFile(fileName, bFullPath)

        # Store the result before releasing the object
        result = fileName.value

        # Explicitly release the COM object
        objOpenSTAAD = None

        return result

    except Exception as e:
        print(f"Error retrieving STAAD file name: {e}")
        return None

    finally:
        # Uninitialize COM
        pythoncom.CoUninitialize()

def get_staad_profiles():
    import win32com.client
    from win32com.client import VARIANT
    import pythoncom

    try:
        pythoncom.CoInitialize()
        objOpenSTAAD = win32com.client.GetObject(Class="StaadPro.OpenSTAAD")
        result = []
        property = objOpenSTAAD.Property
        property._FlagAsMethod('GetSectionPropertyCount')
        property._FlagAsMethod('GetSectionPropertyName')
        property._FlagAsMethod('GetSectionPropertyType')
        property._FlagAsMethod('GetSectionPropertyCountry')
        
        count = property.GetSectionPropertyCount()
        for i in range(1,count+1):
            sectionName = VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, "")
            property.GetSectionPropertyName(i,sectionName)
            sctn_type = property.GetSectionPropertyType(i)
            country = property.GetSectionPropertyCountry(i)
            result.append({'id':i,'name':sectionName.value,'type':sctn_type,'country':country})

        objOpenSTAAD = None
        return result

    except Exception as e:
        print (f"Error retrieving STAAD profiles: {e}")
        return None

    finally:
        pythoncom.CoUninitialize()

def replace_selfweight(file_path, old_text='SELFWEIGHT Y -1', new_text='SELFWEIGHT Y -1 LIST 1 TO 10'):
    """
    Opens a file, replaces the first line containing old_text with new_text,
    and writes the modified content back to the file.
    
    Args:
        file_path (str): Path to the input file
        old_text (str): Text to search for in the file (default: 'SELFWEIGHT Y -1')
        new_text (str): Text to replace the matching line (default: 'SELFWEIGHT Y -1 LIST 1 TO 10')
    
    Returns:
        bool: True if replacement was successful, False if old_text was not found
    """
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Replace the first line containing old_text
        replaced = False
        for i, line in enumerate(lines):
            if old_text in line:
                lines[i] = new_text + '\n'
                replaced = True
                break
        
        if not replaced:
            print(f"Warning: '{old_text}' not found in {file_path}")
            return False
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        print(f"Successfully replaced '{old_text}' with '{new_text}' in {file_path}")
        return True
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return False
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False