from base.staad_base.com_array import *

point_precision = 3

def get_node_count(geometry) -> int:
    nodeCount = geometry.GetNodeCount()
    return nodeCount

def get_selected_beam_count(geometry) -> int:
    nodeCount = geometry.GetNoOfSelectedBeams()
    return nodeCount

def get_node_incidence(geometry,nodeNo) -> float:
    x,xptr = get_ctype_double()
    y,yptr = get_ctype_double()
    z,zptr = get_ctype_double()
    geometry.GetNodeIncidence(int(nodeNo),xptr,yptr,zptr)
    return round(x.value,point_precision),round(y.value,point_precision),round(z.value,point_precision)

def get_node_incidences(geometry) -> float:
    result = []
    node_nos = get_node_nos(geometry=geometry)
    for nodeNo in node_nos:
        node_incidence = get_node_incidence(geometry=geometry,nodeNo=nodeNo[1])
        result.append((nodeNo,node_incidence))
    return result

def get_node_nos(geometry,tuple:bool=True) -> list:
    beamCount = get_node_count(geometry=geometry)
    safe_array_beam_list = make_safe_array_long(beamCount)
    nodes = make_variant_vt_ref(safe_array_beam_list, automation.VT_ARRAY | automation.VT_I4) # signed 32 bit integer
    geometry.GetNodeList(nodes)
    nodes = nodes[0]
    result = []
    for node in enumerate(nodes):
        if(tuple):
            result.append((node[0],node[1]))
        else:
            result.append({'id':node[0],'no':node[1]})
    return result

def get_beam_count(geometry) -> int:
    beamCount = geometry.GetMemberCount()
    return beamCount

def get_beam_length(geometry,beamNo) -> float:
    beamLength = geometry.GetBeamLength(int(beamNo))
    return round(beamLength,point_precision)

def select_beam(geometry,beamNo) -> None:
    geometry.SelectBeam(int(beamNo))
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

def get_beam_incidences(geometry) -> float:
    result = []
    beam_nos = get_beam_nos(geometry=geometry)
    for beamNo in beam_nos:
        beam_incidence = get_beam_incidence(geometry=geometry,beamNo=beamNo[1])
        result.append((beamNo,beam_incidence))
    return result
