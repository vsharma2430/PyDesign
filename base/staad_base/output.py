from staad_base.com_array import *

def get_support_reaction(output,nodeNo, loadcaseNo):
    safe_array_reactions = make_safe_array_double(6)
    reactions = make_variant_vt_ref(safe_array_reactions, automation.VT_ARRAY | automation.VT_R8)
    output.GetSupportReactions(nodeNo, loadcaseNo, reactions)
    return reactions
