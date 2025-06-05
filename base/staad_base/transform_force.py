from base.staad_base.root import *
from base.staad_base.geometry import *
from base.staad_base.load import *
from base.staad_base.com_array import *
from base.staad_base.helper import *

class TransformLoadCase:
    def __init__(self, id, source, destination, predicate, direction):
        self.id = id
        self.source = source
        self.destination = destination
        self.predicate = predicate
        self.direction = direction

    def __repr__(self):
        return (f"TransformLoadCase(id={self.id}, source={self.source}, "
                f"destination={self.destination}, predicate={self.predicate}, direction={self.direction})")
    
def convert_force_operation (openSTAAD,STAAD_objects,transform_load_case_object):
        source = transform_load_case_object.source
        destination = transform_load_case_object.destination
        direction = transform_load_case_object.direction
        predicate = transform_load_case_object.predicate

        load_object = STAAD_objects.load

        for load_case_i in [source]:
            set_load_case_active(load_object,load_case_i)
            load_count_i = get_load_item_count(load_object,load_case_i)
            load_types_i = get_load_item_types(load_object,load_case_i)
            unique_load_types = set([load_type_i_x[1] for load_type_i_x in load_types_i])

            load_type_incidences = {x:[] for x in unique_load_types}
            print('LOAD CASE : ',load_case_i,load_count_i,load_object.GetLoadCaseTitle(load_case_i))
            print('\tLOAD TYPES FOUND : ',load_types_i)

            for load_type_i in unique_load_types:
                load_type_i_count = get_load_type_count(load_object,load_case_i,load_type_i)
                
                print('\tLOAD TYPE,COUNT : ',load_type_i,load_type_i_count)
                
                for load_index in range(load_type_i_count):
                    load_incidences = get_assignment_for_load_type(load_object,load_type_i,load_case_i,load_index)
                    load_type_incidences[load_type_i].append(load_incidences)
            
            print('\t\tLOAD INCIDENCES : ',load_type_incidences)
            
            print('\tLOAD DETAILS : ',load_type_i,load_type_i_count)

            for load_index,load_type_i in load_types_i:
                print('\t\tLOAD INDEX: ',load_index)
                
                if(load_type_i == LoadItemNo.NodalLoad_Node):
                    node_forces = get_nodal_load_info(load_object,load_case_i,load_index)

                    print('\t\t\tLOAD DETAILS (NODE) : ',node_forces)

                    if(destination):
                        set_load_case_active(load_object,destination)
                        for node_i in load_type_incidences[load_type_i][0]:
                            print('\t\t\t\tLOAD ADD (NODE FORCE) : ',node_i,*list(map(predicate,node_forces['forces'])))
                            
                            success = load_object.AddNodalLoad(node_i,*list(map(predicate,node_forces['forces'])))
                            print('\t\t\t\t\tSUCCESS : ',success)

                elif(load_type_i in[LoadItemNo.ConcentratedForce,LoadItemNo.ConcentratedMoment,LoadItemNo.UniformMoment,LoadItemNo.UniformForce]):
                    member_forces = get_member_load_info(load_object,load_case_i,load_index)
                    
                    print('\t\t\tLOAD DETAILS (MEMBER) : ',member_forces)

                    if(destination):
                        set_load_case_active(load_object,destination)
                        if(load_type_i == LoadItemNo.ConcentratedForce):
                            for beam_i in load_type_incidences[load_type_i][0]:
                                print('\t\t\t\tLOAD ADD (CON FORCE) : ',beam_i,
                                                                direction if direction else member_forces['direction'],
                                                                first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                *member_forces['distances'][:2])
                                
                                success = load_object.AddMemberConcForce(beam_i,
                                                                direction if direction else member_forces['direction'],
                                                                first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                *member_forces['distances'][:2])
                                
                                print('\t\t\t\t\tSUCCESS : ',success)
                                
                        if(load_type_i == LoadItemNo.UniformForce):
                            for beam_i in load_type_incidences[load_type_i][0]:
                                print('\t\t\t\tLOAD ADD (UNI FORCE) : ',beam_i,
                                                                direction if direction else member_forces['direction'],
                                                                first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                *member_forces['distances'])
                                
                                success = load_object.AddMemberUniformForce(beam_i,
                                                                direction if direction else member_forces['direction'],
                                                                first_non_zero(list(map(predicate,member_forces['forces']))),
                                                                *member_forces['distances'])
                                
                                print('\t\t\t\t\tSUCCESS : ',success)

                if(destination and len(load_type_incidences[load_type_i])>0):
                    load_type_incidences[load_type_i].pop(0)
                    # print('\t\t',load_type_incidences)
                    