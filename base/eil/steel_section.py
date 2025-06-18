from enum import Enum

class SectionClass(Enum):
    """Steel section classification types"""
    PLASTIC = "PLASTIC"
    COMPACT = "COMPACT"
    SEMI_COMPACT = "SEMI-COMPACT"
    SLENDER = "SLENDER"

class IntendedUse(Enum):
    """Steel section intended use types"""
    BEAMS_COLUMNS = "BEAMS / COLUMNS"
    STRUT_TIE = "STRUT/TIE"
    STRUT_TIE_BRACING = "STRUT/TIE/BRACING"
    SECONDARY_BEAMS_GRAVITY_COLUMNS_STRUT_TIE = "SECONDARY BEAMS / GRAVITY COLUMNS/STRUT/TIE"
    BEAMS_COLUMNS_BRACING_STRUT_TIE = "BEAMS / COLUMNS / BRACING/ STRUT/TIE"
    BEAMS_COLUMNS_BRACING = "BEAMS / COLUMNS / BRACING"
    SECONDARY_BEAMS_GRAVITY_COLUMNS = "SECONDARY BEAMS / GRAVITY COLUMNS"
    LIFT_COKE_DRUM_STR = "LIFT /COKE DRUM STR."
    BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS_ELECTRICAL_TREE = "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS/ELECTRICAL TREE"
    KNEE_BRACING = "KNEE BRACING"
    BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS_ELECTRICAL_TREE_SUPPORTS = "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS, ELECTRICAL TREE & SUPPORTS"
    BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS = "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"
    ELECTRICAL_TREE = "ELECTRICAL TREE"
    MISC_PIPE_SUPPORTS_T_SUPPORTS = "MISC. PIPE SUPPORTS / T SUPPORTS"
    BEAMS_COLUMNS_LADDERS = "BEAMS / COLUMNS/LADDERS"
    CIRCULAR_HORIZONTAL_EQPT_PLTF = "CIRCULAR & HORIZONTAL EQPT.PLTF."
    BRACINGS = "BRACINGS"
    CIRCULAR_HORIZONTAL_EQPT_PLTF_ALT = "CIRCULAR & HORIZONTAL EQPT.PLTF"

class SteelSection:
    def __init__(self, sl_no, section, unit_wt_kg_m, classification: SectionClass, intended_use: IntendedUse, staad_name):
        self.sl_no = sl_no
        self.section = section
        self.unit_wt_kg_m = unit_wt_kg_m
        self.classification = classification
        self.intended_use = intended_use
        self.staad_name = staad_name

    def __repr__(self):
        return (f"SteelSection(sl_no={self.sl_no}, section='{self.section}', "
                f"unit_wt_kg_m={self.unit_wt_kg_m}, classification='{self.classification}', "
                f"intended_use='{self.intended_use}', staad_name='{self.staad_name}')")

# List of SteelSection objects
# Create SteelSection objects (corrected from tuples)
steel_sections = [
    SteelSection(1, "ISMB 200", 24.17, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMB200"),
    SteelSection(2, "ISMB 250", 37.3, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMB250"),
    SteelSection(3, "ISMB 300", 46.02, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMB300"),
    SteelSection(4, "ISMB 400", 61.55, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMB400"),
    SteelSection(5, "ISMB 450", 72.38, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMB450"),
    SteelSection(6, "ISMB 500", 86.88, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMB500"),
    SteelSection(7, "ISMB 600", 121, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMB600"),
    SteelSection(8, "ISNPB 200X100X25.09", 25.09, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "NPB200X100X25.09"),
    SteelSection(9, "ISNPB 250X150X39.78", 39.78, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "NPB250X150X39.78"),
    SteelSection(10, "ISNPB 300X150X49.32", 49.32, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "NPB300X150X49.32"),
    SteelSection(11, "ISNPB 400X180X66.31", 66.31, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "NPB400X180X66.31"),
    SteelSection(12, "ISNPB 450X190X77.58", 77.58, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "NPB450X190X77.58"),
    SteelSection(13, "ISNPB 500X200X90.69", 90.69, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "NPB500X200X90.69"),
    SteelSection(14, "ISNPB 600X220X122.45", 122.45, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "NPB600X220X122.45"),
    SteelSection(15, "ISWPB 200X200X42.26", 42.26, SectionClass.SEMI_COMPACT, IntendedUse.STRUT_TIE, "WPB200X200X42.26"),
    SteelSection(16, "ISWPB 250X250X73.15", 73.15, SectionClass.PLASTIC, IntendedUse.STRUT_TIE_BRACING, "WPB250X250X73.14"),
    SteelSection(17, "ISWPB 300X300X100.85", 100.85, SectionClass.SEMI_COMPACT, IntendedUse.SECONDARY_BEAMS_GRAVITY_COLUMNS_STRUT_TIE, "WPB300X300X100.84"),
    SteelSection(18, "ISWPB 300X300X117.03", 117.03, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS_BRACING_STRUT_TIE, "WPB300X300X117.03"),
    SteelSection(19, "ISWPB 360X300X141.81", 125.81, SectionClass.COMPACT, IntendedUse.BEAMS_COLUMNS_BRACING, "WPB360X300X141.81"),
    SteelSection(20, "ISWPB 600X300X128.79", 128.79, SectionClass.SEMI_COMPACT, IntendedUse.SECONDARY_BEAMS_GRAVITY_COLUMNS, "WPB600X300X128.79"),
    SteelSection(21, "ISWPB 600X300X177.78", 177.78, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "WPB600X300X177.77"),
    SteelSection(22, "ISWPB 600X300X285.48", 285.48, SectionClass.PLASTIC, IntendedUse.LIFT_COKE_DRUM_STR, "WPB600X300X285.47"),
    SteelSection(23, "ISWPB 700X300X149.89", 149.89, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "WPB700X300X149.89"),
    SteelSection(24, "ISWPB 700X300X204.48", 204.48, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "WPB700X300X204.48"),
    SteelSection(25, "ISWPB 700X300X240.51", 240.51, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "WPB700X300X240.51"),
    SteelSection(26, "ISWPB 800X300X262.34", 262.34, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "WPB800X300X262.33"),
    SteelSection(27, "ISWPB 900X300X291.46", 291.46, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "WPB900X300X291.45"),
    SteelSection(28, "WPB900X300X333.00 (HE 900 M)", 333, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "WPB900X300X333.00"),
    SteelSection(29, "SHS 72X72X4.8", 9.55, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS_ELECTRICAL_TREE, "75X75X4.9SHS"),
    SteelSection(30, "SHS 40X40X4", 4.2, SectionClass.PLASTIC, IntendedUse.KNEE_BRACING, "40X40X4.0SHS"),
    SteelSection(31, "SHS 45X45X4.5", 5.31, SectionClass.PLASTIC, IntendedUse.KNEE_BRACING, "45X45X4.5SHS"),
    SteelSection(32, "SHS 100X100X6", 16.98, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS_ELECTRICAL_TREE_SUPPORTS, "100X100X6.0SHS"),
    SteelSection(33, "SHS 132X132X5.4", 20.88, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "132X132X5.4SHS"),
    SteelSection(34, "SHS 150X150X6", 26.4, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "150X150X6.0SHS"),
    SteelSection(35, "SHS 150X150X8", 34.38, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "150X150X8.0SHS"),
    SteelSection(36, "SHS 180X180X8", 42.5, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "180X180X8.0SHS"),
    SteelSection(37, "SHS 220X220X8", 51.96, SectionClass.COMPACT, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "220X220X8.0SHS"),
    SteelSection(38, "SHS 220X220X10", 63.92, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "220X220X10.0SHS"),
    SteelSection(39, "SHS 250X250X10", 73.34, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "250X250X10.0SHS"),
    SteelSection(40, "SHS 300X300X12", 105.61, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "300X300X12.0SHS"),
    SteelSection(41, "SHS 350X350X12", 124.45, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "350X350X12.0SHS"),
    SteelSection(42, "SHS 400X400X12", 143.29, SectionClass.PLASTIC, IntendedUse.BRACINGS_MISC_PIPE_SUPPORTS_T_SUPPORTS, "400X400X12.0SHS"),
    SteelSection(43, "RHS 200X100X6", 26.4, SectionClass.PLASTIC, IntendedUse.ELECTRICAL_TREE, "200X100X6.0RHS"),
    SteelSection(44, "RHS 220X140X8", 41.91, SectionClass.PLASTIC, IntendedUse.MISC_PIPE_SUPPORTS_T_SUPPORTS, "220X140X8.0RHS"),
    SteelSection(45, "RHS 260X180X10", 63.92, SectionClass.PLASTIC, IntendedUse.MISC_PIPE_SUPPORTS_T_SUPPORTS, "260X180X10.0RHS"),
    SteelSection(46, "RHS 300X200X10", 73.34, SectionClass.PLASTIC, IntendedUse.MISC_PIPE_SUPPORTS_T_SUPPORTS, "300X200X10.0RHS"),
    SteelSection(47, "RHS 400X200X12", 105.61, SectionClass.PLASTIC, IntendedUse.MISC_PIPE_SUPPORTS_T_SUPPORTS, "400X200X12.0RHS"),
    SteelSection(48, "ISMC 100", 9.56, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS_LADDERS, "ISMC100"),
    SteelSection(49, "ISMC 125", 13.1, SectionClass.PLASTIC, IntendedUse.CIRCULAR_HORIZONTAL_EQPT_PLTF, "ISMC125"),
    SteelSection(50, "ISMC 150", 16.8, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMC150"),
    SteelSection(51, "ISMC 200", 22.3, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMC200"),
    SteelSection(52, "ISMC 250", 30.6, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMC250"),
    SteelSection(53, "ISMC 300", 36.3, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMC300"),
    SteelSection(54, "ISMC 400", 50.1, SectionClass.PLASTIC, IntendedUse.BEAMS_COLUMNS, "ISMC400"),
    SteelSection(55, "ISA 50X50X6", 4.49, SectionClass.PLASTIC, IntendedUse.BRACINGS, "ISA50x50x6"),
    SteelSection(56, "ISA 65X65X6", 5.91, SectionClass.SLENDER, IntendedUse.BRACINGS, "ISA65x65x6"),
    SteelSection(57, "ISA 65X65X8", 7.73, SectionClass.SEMI_COMPACT, IntendedUse.ELECTRICAL_TREE, "ISA65x65x8"),
    SteelSection(58, "ISA 75X75X6", 6.86, SectionClass.SLENDER, IntendedUse.ELECTRICAL_TREE, "ISA75x75x6"),
    SteelSection(59, "ISA 75X75X8", 9, SectionClass.PLASTIC, IntendedUse.BRACINGS, "ISA75x75x8"),
    SteelSection(60, "ISA 90X90X8", 10.92, SectionClass.SLENDER, IntendedUse.BRACINGS, "ISA90x90x8"),
    SteelSection(61, "ISA 100X100X8", 12.18, SectionClass.SEMI_COMPACT, IntendedUse.CIRCULAR_HORIZONTAL_EQPT_PLTF_ALT, "ISA100x100x8"),
    SteelSection(62, "ISA 100X100X10", 15.04, SectionClass.PLASTIC, IntendedUse.BRACINGS, "ISA100x100x10"),
    SteelSection(63, "ISA 110X110X10", 16.58, SectionClass.SLENDER, IntendedUse.BRACINGS, "ISA110x110x10"),
    SteelSection(64, "ISA 110X110X12", 19.68, SectionClass.PLASTIC, IntendedUse.BRACINGS, "ISA110x110x12"),
    SteelSection(65, "ISA 130X130X12", 23.45, SectionClass.SLENDER, IntendedUse.BRACINGS, "ISA130x130x12"),
    SteelSection(66, "ISA 150X150X16", 35.84, SectionClass.PLASTIC, IntendedUse.BRACINGS, "ISA150x150x16"),
    SteelSection(67, "ISA 200X200X20", 59.96, SectionClass.PLASTIC, IntendedUse.BRACINGS, "ISA200x200x20"),
]

sections_by_ref_no = {section.sl_no:section for section in steel_sections}
sections_by_staad_name = {section.staad_name:section for section in steel_sections}