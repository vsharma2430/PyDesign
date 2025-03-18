from root import *
from geometry import *

if(__name__ == '__main__'):
    openSTAAD,STAAD_objects = get_openSTAAD()
    geometry_object = STAAD_objects['geometry']

    beam_nos = get_beam_nos(geometry_object)
    node_nos = get_node_nos(geometry_object)

    for nodeNo in node_nos:
        node_incidence = get_node_incidence(geometry=geometry_object,nodeNo=nodeNo[1])
        print(nodeNo,node_incidence)

    for beamNo in beam_nos:
        length = get_beam_length(geometry=geometry_object,beamNo=beamNo[1])
        nodeA,nodeB = get_beam_incidence(geometry=geometry_object,beamNo=beamNo[1])
        print(beamNo,nodeA,nodeB)
    