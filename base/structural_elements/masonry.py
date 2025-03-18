import math 
from base import *
from base.helper.wrapper import *

@design_details(code='IS 1893 (I):2016' ,clause= '7.9.2.1' , units=MPa)
def modulus_of_elasticity_masonry_infill(compressive_strength:float):
    return 550*compressive_strength

@design_details(code='IS 1893 (I):2016' ,clause= '7.9.2.1' , units=MPa)
def compressive_strength_masonry_prism(compressive_strength_brick:float,compressive_strength_mortar:float):
    return 0.433*pow(compressive_strength_brick,0.64)*pow(compressive_strength_mortar,0.36)

@design_details(code='IS 1893 (I):2016' ,clause= '7.9.2.2')
def get_alpha_h(height:float,
                modulus_elasticity_urm_infill:float,
                modulus_elasticity_rc_mrf:float,
                moment_inertia_column:float,
                thickness_infill:float,
                angle_strut_horizontal:float,):
    return height * (pow(
                            ( modulus_elasticity_urm_infill*thickness_infill* math.sin(2*angle_strut_horizontal)) / 
                            (4*modulus_elasticity_rc_mrf*moment_inertia_column*height)
                    ,0.25))

@design_details(code='IS 1893 (I):2016' ,clause= '7.9.2.2' , units=m)
def equivalent_diagonal_strut(alpha_h:float,Lds:float):
    return 0.175*pow(alpha_h,-0.4)*Lds

