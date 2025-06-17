from base.load.nodal_load import *
from base.load.uniform_load import *
from base.load.conc_load import *

uniform_operating_load = UniformLoad(load_case=LoadCase.OperatingLoad)
uniform_empty_load = UniformLoad(load_case=LoadCase.EmptyLoad)

uniform_tg_gx = UniformLoad(load_case=LoadCase.ThermalGravity_GX,direction=MemberDirection.GX)
uniform_tg_gz = UniformLoad(load_case=LoadCase.ThermalGravity_GZ,direction=MemberDirection.GZ)
uniform_tl_gx = UniformLoad(load_case=LoadCase.ThermalLateral_GX,direction=MemberDirection.GX)
uniform_tl_gz = UniformLoad(load_case=LoadCase.ThermalLateral_GZ,direction=MemberDirection.GZ)

uniform_clt_gy = UniformLoad(load_case=LoadCase.ContigencyLoadTransverse,direction=MemberDirection.GY)
uniform_clt_gz = UniformLoad(load_case=LoadCase.ContigencyLoadTransverse,direction=MemberDirection.GZ)

conc_operating_load = ConcentratedLoad(load_case=LoadCase.OperatingLoad)
conc_empty_load = ConcentratedLoad(load_case=LoadCase.EmptyLoad)

conc_tg_gx = ConcentratedLoad(load_case=LoadCase.ThermalGravity_GX,direction=MemberDirection.GX)
conc_tg_gz = ConcentratedLoad(load_case=LoadCase.ThermalGravity_GZ,direction=MemberDirection.GZ)
conc_tl_gx = ConcentratedLoad(load_case=LoadCase.ThermalLateral_GX,direction=MemberDirection.GX)
conc_tl_gz = ConcentratedLoad(load_case=LoadCase.ThermalLateral_GZ,direction=MemberDirection.GZ)

# Tier wind loads to be implemented
wl_gx = NodalLoad(load_case=LoadCase.WindTier_GX)
wl_gx_o = NodalLoad(load_case=LoadCase.WindTier_GX_Opposite)