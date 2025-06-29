from enum import IntEnum

class LoadType(IntEnum):
    Dead = 0
    Live = 1
    RoofLive = 2
    Wind = 3
    SeismicH = 4
    SeismicV = 5
    Snow = 6
    Fluids = 7
    Soil = 8
    Rain = 9
    Ponding = 10
    Dust = 11
    Traffic = 12
    Temp = 13
    Imperfection = 14
    Accidental = 15
    Flood = 16
    Ice = 17
    WindIce = 18
    CraneHook = 19
    Mass = 20
    Gravity = 21
    Push = 22
    NoneType = 23  # 'None' is a reserved keyword in Python

class LoadItemNo(IntEnum):
    SelfWeight = 4000
    NodalLoad_Node = 3110
    NodalLoad_Inclined = 3120
    NodalLoad_SupportDisplacement = 3910
    NodalLoad_RegionNodeLoad = 3312
    UniformForce = 3210
    UniformMoment = 3220
    ConcentratedForce = 3230
    ConcentratedMoment = 3240
    LinearVarying = 3250
    Trapezoidal = 3260
    Hydrostatic = 3261
    PrePostStress = 3620
    FixedEnd = 3810
    UniformForce_Physical = 3275
    UniformMoment_Physical = 3280
    ConcentratedForce_Physical = 3285
    ConcentratedMoment_Physical = 3290
    Trapezoidal_Physical = 3295
    Area = 3410
    FloorLoadYrange = 3510
    FloorLoadXrange = 3511
    FloorLoadZrange = 3520
    FloorLoadGroup = 3530
    OneWayFloorLoadXrange = 3551
    OneWayFloorLoadYrange = 3552
    OneWayFloorLoadZrange = 3553
    OneWayFloorLoadGroup = 3554
    PressureFullPlate = 3310
    ConcentratedLoad_Plate = 3311
    PartialPlatePressure = 3312
    Trapezoidal_Plate = 3320
    Solid = 3322
    Temperature = 3710
    Strain = 3720
    StrainRate = 3721
    UBCLoad = 4400
    WindLoad = 4600
    WindLoadDynamic = 4610
    IbcLoad = 4405
    Load1893 = 4410
    AijLoad = 4500
    ColombianLoad = 4510
    CFELoad = 4520
    RPALoad = 4530
    NTCLoad = 4540
    NRCLoad = 4550
    NRCLoad2005 = 4560
    NRCLoad2010 = 4561
    TurkishLoad = 4570
    GB50011Load = 4575
    Colombian2010Load = 4576
    TimeHistoryLoad = 4820
    SnowLoadData = 4651
    RepeatLoadData = 4201
    NotionalLoadData = 4223
    ReferenceLoad = 4220
    SpectrumLoad = 4100
    SpectrumData = 4101
    CalculateNaturalFrequency = 4700
    ModalCalculationRequested = 4710
    CalculateRayleighFrequency = 4701
    SnowLoad = 4650
    RepeatLoad = 4200
    NotionalLoad = 4222

class MemberDirection(IntEnum):
    X = 1
    Y = 2
    Z = 3
    GX = 4
    GY = 5
    GZ = 6
    PX = 7
    PY = 7
    PZ = 8
    
class LoadCase(IntEnum):
    SelfWeight = 101
    DeadLoadElecIns = 103
    LiveLoad = 201
    EmptyLoad = 301
    OperatingLoad = 401
    ThermalGravity_GX = 6
    ThermalGravity_GZ = 7
    ThermalLateral_GX = 8
    ThermalLateral_GZ = 9
    ContigencyLoadTransverse = 31
    WindColumn_GX = 1101
    WindTier_GX = 1102
    WindColumn_GX_Opposite = 1201
    WindTier_GX_Opposite = 1202
    WindColumn_GZ = 1301
    WindColumn_GZ_Opposite = 1401
    
class MemberForceDirection(IntEnum):
    LocalX = 1
    LocalY = 2
    LocalZ = 3
    GlobalX = 4
    GlobalY = 5
    GlobalZ = 6

