from base.staad_base.root import *
from staad_base.geometry import *
from staad_base.load import *
from staad_base.design import *

if(__name__ == '__main__'):

    openSTAAD,STAAD_objects = get_openSTAAD()

    geometry = STAAD_objects['geometry']
    property = STAAD_objects['property']
    output = STAAD_objects['output']
    beams = get_beam_nos(geometry=geometry)

    if(not output.AreResultsAvailable()):
        print('Analysis started')
        anl_result = run_analysis(openSTAAD)
    
    print(get_selected_beam_nos(geometry))

    print('Getting results')
    print(get_member_steel_design_results(output,beams))