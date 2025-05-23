from root import *
from geometry import *
from load import *
from com_array import *
from helper import *

if(__name__ == '__main__'):

    source,destination = 401,None
    predicate = lambda x:x*0.4

    openSTAAD,STAAD_objects = get_openSTAAD()
    geometry_object = STAAD_objects['geometry']
    load_object = STAAD_objects['load']

    node_nos = get_node_incidences(geometry_object)
    beam_nos = get_beam_incidences(geometry_object)
    load_case_nos = get_load_nos(load=load_object)
    
    for load_case_i in [source]:
        set_load_case_active(load_object,load_case_i)
        load_count_i = get_load_item_count(load_object,load_case_i)
        load_types_i = get_load_item_types(load_object,load_case_i)
        unique_load_types = set([load_type_i_x[1] for load_type_i_x in load_types_i])

        print('LOAD CASE : ',load_case_i,load_count_i,load_object.GetLoadCaseTitle(load_case_i))
        print('\tLOAD TYPES FOUND : ',unique_load_types)

        for load_type_i in unique_load_types:
            load_type_i_count = get_load_type_count(load_object,load_case_i,load_type_i)
            
            print('\tLOAD TYPE : ',load_type_i,load_type_i_count)
            
            for load_index in range(load_type_i_count):
                    load_incidences = get_assignment_for_load_type(load_object,load_type_i,load_case_i,load_index)

                    print('\t\tLOAD INDEX : ',load_index)
                    
                    if(load_type_i == LoadItemNo.NodalLoad_Node):
                        node_forces = get_nodal_load_info(load_object,load_case_i,load_index)

                        print('\t\tLOAD INCIDENCES : ',load_incidences)
                        print('\t\t\tLOAD DETAILS (NODE) : ',node_forces)

                        if(destination):
                            set_load_case_active(load_object,destination)
                            for node_i in load_incidences:
                                print('\t\t\t\tLOAD ADD (NODE FORCE) : ',node_i,*list(map(predicate,node_forces['forces'])))
                                
                                success = load_object.AddNodalLoad(node_i,*list(map(predicate,node_forces['forces'])))
                                print('\t\t\t\t\tSUCCESS : ',success)

                    elif(load_type_i in[LoadItemNo.ConcentratedForce,LoadItemNo.ConcentratedMoment,LoadItemNo.UniformMoment,LoadItemNo.UniformForce]):
                        member_forces = get_member_load_info(load_object,load_case_i,load_index)
                        
                        print('\t\t\tLOAD INCIDENCES : ',load_incidences)
                        print('\t\t\tLOAD DETAILS (MEMBER) : ',member_forces)

                        if(destination):
                            set_load_case_active(load_object,destination)
                            if(load_type_i == LoadItemNo.ConcentratedForce):
                                for beam_i in load_incidences:
                                    print('\t\t\t\tLOAD ADD (CON FORCE) : ',beam_i,
                                                                   member_forces['direction'],
                                                                   first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                   *member_forces['distances'][:2])
                                    success = load_object.AddMemberConcForce(beam_i,
                                                                   member_forces['direction'],
                                                                   first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                   *member_forces['distances'][:2])
                                    print('\t\t\t\t\tSUCCESS : ',success)
                                    
                            if(load_type_i == LoadItemNo.UniformForce):
                                for beam_i in load_incidences:
                                    print('\t\t\t\tLOAD ADD (UNI FORCE) : ',beam_i,
                                                                   member_forces['direction'],
                                                                   first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                   *member_forces['distances'])
                                    success = load_object.AddMemberUniformForce(beam_i,
                                                                   member_forces['direction'],
                                                                   first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                   *member_forces['distances'])
                                    print('\t\t\t\t\tSUCCESS : ',success)