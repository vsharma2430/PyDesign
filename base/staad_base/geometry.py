from base.staad_base.com_array import *
from base.geometry_base.point import *
from base.structural_elements.beam import *
from base.staad_base.property import *
from base.staad_base.helper import *

def get_node_count(geometry) -> int:
    nodeCount = geometry.GetNodeCount()
    return nodeCount

def get_selected_beam_count(geometry) -> int:
    nodeCount = geometry.GetNoOfSelectedBeams()
    return nodeCount

def get_node_nos(geometry) -> list:
    beamCount = get_node_count(geometry=geometry)
    safe_array_beam_list = make_safe_array_long(beamCount)
    nodes = make_variant_vt_ref(safe_array_beam_list, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer
    geometry.GetNodeList(nodes)
    nodes = nodes[0]
    result = []
    for node in enumerate(nodes):
        result.append(node[1])
    return result

def get_node_incidence(geometry,nodeNo) -> float:
    x,xptr = get_ctype_double()
    y,yptr = get_ctype_double()
    z,zptr = get_ctype_double()
    geometry.GetNodeIncidence(int(nodeNo),xptr,yptr,zptr)
    return Point3D(round(x.value,point_precision),round(y.value,point_precision),round(z.value,point_precision))

def get_node_incidences(geometry) -> dict:
    result = {}
    node_nos = get_node_nos(geometry=geometry)
    for nodeNo in node_nos:
        node_incidence = get_node_incidence(geometry=geometry,nodeNo=nodeNo)
        result[nodeNo] = node_incidence
    return result

def get_beam_count(geometry) -> int:
    beamCount = geometry.GetMemberCount()
    return beamCount

def get_beam_length(geometry,beamNo) -> float:
    beamLength = geometry.GetBeamLength(int(beamNo))
    return round(beamLength,point_precision)

def select_beam(geometry,beamNo) -> None:
    if(isinstance(beamNo,int)):
        geometry.SelectBeam(int(beamNo))
    elif(isinstance(beamNo,Beam3D)):
        geometry.SelectBeam(beamNo.id)
    return 

def get_beam_incidence(geometry,beamNo) -> float:
    nodeA,nodeAptr = get_ctype_long()
    nodeB,nodeBptr = get_ctype_long()
    geometry.GetMemberIncidence(int(beamNo),nodeAptr,nodeBptr)
    return nodeA.value,nodeB.value

def get_beam_nos(geometry,tuple:bool = False) -> list:
    beamCount = get_beam_count(geometry=geometry)
    safe_array_beam_list = make_safe_array_long(beamCount)
    beams = make_variant_vt_ref(safe_array_beam_list, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer
    geometry.GetBeamList(beams)
    beams = beams[0]
    result = []
    for beam in enumerate(beams):
        if(tuple):
            result.append((beam[0],beam[1]))
        else:
            result.append(beam[1])
    return result

def get_selected_beam_nos(geometry,sort:int=1,tuple:bool = False) -> list:
    beamCount = get_selected_beam_count(geometry=geometry)
    safe_array_beam_list = make_safe_array_long(beamCount)
    beams = make_variant_vt_ref(safe_array_beam_list, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer
    geometry.GetSelectedBeams(beams,sort)
    beams = beams[0]
    result = []
    for beam in enumerate(beams):
        if(tuple):
            result.append((beam[0],beam[1]))
        else:
            result.append(beam[1])
    return result

def get_beam_objects(geometry,property=None,nodes=None) -> dict[int,Beam3D]:
    if(nodes is None):
        nodes = get_node_incidences(geometry=geometry)

    result = {}
    beam_nos = get_beam_nos(geometry=geometry)
    for beamNo in beam_nos:
        beam_incidence = get_beam_incidence(geometry=geometry,beamNo=beamNo)
        profile = ''
        if(property):
            profile = get_beam_property_name(property=property,beam_no=beamNo)

        result[beamNo] = Beam3D(id=beamNo,start=nodes[beam_incidence[0]],end=nodes[beam_incidence[1]],profile=profile)
    return result

def add_node(geometry,point:Point3D) -> int:
    if(point is not None):
        point = round(point)
        return geometry.AddNode(point.x,point.y,point.z)
    return None

def add_support_node(geometry,support,point:Point3D,support_id:int) -> int:
    if(point is not None):
        support_node = get_node_number(geometry=geometry,point=point)
        support.AssignSupportToNode(support_node,support_id)
        return support_node

    return None

def add_beam(geometry,beam:Beam3D):
    if(beam is not None and beam.start is not None and beam.end is not None):
        beam_start=round(beam.start)
        beam_end=round(beam.end)
        return geometry.AddBeam(add_node(geometry=geometry,point=beam_start),add_node(geometry=geometry,point=beam_end))
    return None

def get_node_number(geometry,point:Point3D):
    if geometry and point:
        point.__round__()
        return geometry.GetNodeNumber(point.x,point.y,point.z)
    return None

def get_intersect_beams_count(geometry,beams=None,tolerance=0.001):
    return geometry.GetIntersectBeamsCount(beams,tolerance)

def intersect_beams(geometry,tolerance=0.001):
    safe_array_beam_list = make_safe_array_long(get_intersect_beams_count(geometry))
    beams = make_variant_vt_ref(safe_array_beam_list, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer
    geometry.IntersectBeams(2,None,tolerance,beams)
    return open_array(beams)

def get_breakable_beam_count(geometry,nodes):
    return geometry.GetCountOfBreakableBeamsAtSpecificNodes(make_safe_array_long(values=nodes))

def break_beams(geometry,nodes):
    safe_array_beam_list_1 = make_safe_array_long(get_breakable_beam_count(geometry,nodes))
    beams_1 = make_variant_vt_ref(safe_array_beam_list_1, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer

    safe_array_beam_list_2 = make_safe_array_long(get_breakable_beam_count(geometry,nodes))
    beams_2 = make_variant_vt_ref(safe_array_beam_list_2, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer

    geometry.BreakBeamsAtSpecificNodes(make_safe_array_long(values=nodes),beams_1,beams_2)
    return {'existing_beams':open_array(beams_1),'new_beams':open_array(beams_2)}

add_beams_fn = lambda geometry : lambda beams : list(map(lambda beam: add_beam(geometry=geometry, beam=beam), [*beams]))
select_beams_fn = lambda geometry : lambda beams : list(map(lambda beam: select_beam(geometry=geometry, beamNo=beam), [*beams]))