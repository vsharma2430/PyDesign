from base.staad_base.root import *
from base.staad_base.geometry import *
from base.staad_base.load import *
from base.staad_base.transform_force import *
from base.staad_base.com_array import *
from base.staad_base.helper import *

if(__name__ == '__main__'):
    openSTAAD,STAAD_objects = get_openSTAAD()

    piperack_convert_objects = [
        TransformLoadCase(id='empty'              , source=401, destination=301, predicate=lambda x:  x * 0.4  , direction=None),
        TransformLoadCase(id='thermal gravity(GX)', source=401, destination=6  , predicate=lambda x: -x * 0.025, direction=4),
        TransformLoadCase(id='thermal gravity(GZ)', source=401, destination=7  , predicate=lambda x: -x * 0.125, direction=6),
        TransformLoadCase(id='thermal lateral(GX)', source=401, destination=8  , predicate=lambda x: -x * 0.05 , direction=4),
        TransformLoadCase(id='thermal lateral(GZ)', source=401, destination=9  , predicate=lambda x: -x * 0.05 , direction=6)
    ]

    for convert_object in piperack_convert_objects:
        convert_force_operation(STAAD_objects= STAAD_objects,transform_load_case_object=convert_object)