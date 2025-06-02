class SteelSection:
    def __init__(self, sl_no, section, unit_wt_kg_m, classification, intended_use):
        self.sl_no = sl_no
        self.section = section
        self.unit_wt_kg_m = unit_wt_kg_m
        self.classification = classification
        self.intended_use = intended_use

    def __repr__(self):
        return (f"SteelSection(sl_no={self.sl_no}, section='{self.section}', "
                f"unit_wt_kg_m={self.unit_wt_kg_m}, classification='{self.classification}', "
                f"intended_use='{self.intended_use}')")

# List of SteelSection objects
steel_sections = [
    SteelSection(1, "ISMB 200", 24.17, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(2, "ISMB 250", 37.3, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(3, "ISMB 300", 46.02, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(4, "ISMB 400", 61.55, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(5, "ISMB 450", 72.38, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(6, "ISMB 500", 86.88, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(7, "ISMB 600", 121, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(8, "ISNPB 200X100X25.09", 25.09, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(9, "ISNPB 250X150X39.78", 39.78, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(10, "ISNPB 300X150X49.32", 49.32, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(11, "ISNPB 400X180X66.31", 66.31, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(12, "ISNPB 450X190X77.58", 77.58, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(13, "ISNPB 500X200X90.69", 90.69, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(14, "ISNPB 600X220X122.45", 122.45, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(15, "ISWPB 200X200X42.26", 42.26, "SEMI-COMPACT", "STRUT/TIE"),
    SteelSection(16, "ISWPB 250X250X73.15", 73.15, "PLASTIC", "STRUT/TIE/BRACING"),
    SteelSection(17, "ISWPB 300X300X100.85", 100.85, "SEMI-COMPACT", "SECONDARY BEAMS / GRAVITY COLUMNS/STRUT/TIE"),
    SteelSection(18, "ISWPB 300X300X117.03", 117.03, "PLASTIC", "BEAMS / COLUMNS / BRACING/ STRUT/TIE"),
    SteelSection(19, "ISWPB 360X300X125.81", 125.81, "COMPACT", "BEAMS / COLUMNS / BRACING"),
    SteelSection(20, "ISWPB 600X300X128.79", 128.79, "SEMI-COMPACT", "SECONDARY BEAMS / GRAVITY COLUMNS"),
    SteelSection(21, "ISWPB 600X300X177.78", 177.78, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(22, "ISWPB 600X300X285.48", 285.48, "PLASTIC", "LIFT /COKE DRUM STR."),
    SteelSection(23, "ISWPB 700X300X149.89", 149.89, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(24, "ISWPB 700X300X204.48", 204.48, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(25, "ISWPB 700X300X240.51", 240.51, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(26, "ISWPB 800X300X262.34", 262.34, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(27, "ISWPB 900X300X291.46", 291.46, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(28, "WPB900X300X333.00 (HE 900 M)", 333, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(29, "SHS 75X75X4.9", 9.55, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS/ELECTRICAL TREE"),
    SteelSection(30, "SHS 40X40X4", 4.2, "PLASTIC", "KNEE BRACING"),
    SteelSection(31, "SHS 45X45X4.5", 5.31, "PLASTIC", "KNEE BRACING"),
    SteelSection(32, "SHS 100X100X6", 16.98, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS, ELECTRICAL TREE & SUPPORTS"),
    SteelSection(33, "SHS 132X132X5.4", 20.88, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(34, "SHS 150X150X6", 26.4, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(35, "SHS 150X150X8", 34.38, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(36, "SHS 180X180X8", 42.5, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(37, "SHS 220X220X8", 51.96, "COMPACT", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(38, "SHS 220X220X10", 63.92, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(39, "SHS 250X250X10", 73.34, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(40, "SHS 300X300X12", 105.61, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(41, "SHS 350X350X12", 124.45, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(42, "SHS 400X400X12", 143.29, "PLASTIC", "BRACINGS, MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(43, "RHS 200X100X6", 26.4, "PLASTIC", "ELECTRICAL TREE"),
    SteelSection(44, "RHS 220X140X8", 41.91, "PLASTIC", "MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(45, "RHS 260X180X10", 63.92, "PLASTIC", "MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(46, "RHS 300X200X10", 73.34, "PLASTIC", "MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(47, "RHS 400X200X12", 105.61, "PLASTIC", "MISC. PIPE SUPPORTS / T SUPPORTS"),
    SteelSection(48, "ISMC 100", 9.56, "PLASTIC", "BEAMS / COLUMNS/LADDERS"),
    SteelSection(49, "ISMC 125", 13.1, "PLASTIC", "CIRCULAR & HORIZONTAL EQPT.PLTF."),
    SteelSection(50, "ISMC 150", 16.8, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(51, "ISMC 200", 22.3, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(52, "ISMC 250", 30.6, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(53, "ISMC 300", 36.3, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(54, "ISMC 400", 50.1, "PLASTIC", "BEAMS / COLUMNS"),
    SteelSection(55, "ISA 50X50X6", 4.49, "PLASTIC", "BRACINGS"),
    SteelSection(56, "ISA 65X65X6", 5.91, "SLENDER", "BRACINGS"),
    SteelSection(57, "ISA 65X65X8", 7.73, "SEMI-COMPACT", "ELECTRICAL TREE"),
    SteelSection(58, "ISA 75X75X6", 6.86, "SLENDER", "ELECTRICAL TREE"),
    SteelSection(59, "ISA 75X75X8", 9, "PLASTIC", "BRACINGS"),
    SteelSection(60, "ISA 90X90X8", 10.92, "SLENDER", "BRACINGS"),
    SteelSection(61, "ISA 100X100X8", 12.18, "SEMI-COMPACT", "CIRCULAR & HORIZONTAL EQPT.PLTF"),
    SteelSection(62, "ISA 100X100X10", 15.04, "PLASTIC", "BRACINGS"),
    SteelSection(63, "ISA 110X110X10", 16.58, "SLENDER", "BRACINGS"),
    SteelSection(64, "ISA 110X110X12", 19.68, "PLASTIC", "BRACINGS"),
    SteelSection(65, "ISA 130X130X12", 23.45, "SLENDER", "BRACINGS"),
    SteelSection(66, "ISA 150X150X16", 35.84, "PLASTIC", "BRACINGS"),
    SteelSection(67, "ISA 200X200X20", 59.96, "PLASTIC", "BRACINGS"),
]