# https://learn.microsoft.com/en-us/windows/win32/wmisdk/numbers

from comtypes import automation
import ctypes

def get_ctype(type:ctypes,tuple:bool=True):
    variable = type()
    pointer = ctypes.pointer(variable)
    if(tuple):
        return variable,pointer
    else:
        return {'variable':variable,'pointer':pointer}
    
def get_ctype_long(tuple:bool=True):
    return get_ctype(type=ctypes.c_long,tuple=tuple)

def get_ctype_float(tuple:bool=True):
    return get_ctype(type=ctypes.c_float,tuple=tuple)
    
def get_ctype_double(tuple:bool=True):
    return get_ctype(type=ctypes.c_double,tuple=tuple)

def get_ctype_string(tuple:bool=True):
    return get_ctype(type=ctypes.c_char,tuple=tuple)

def make_safe_array_int(size): 
    return automation._midlSAFEARRAY(ctypes.c_int).create([0]*size)

def make_safe_array_long(size): 
    return automation._midlSAFEARRAY(ctypes.c_long).create([0]*size)

def make_safe_array_float(size): 
    return automation._midlSAFEARRAY(ctypes.c_float).create([0]*size)

def make_safe_array_double(size): 
    return automation._midlSAFEARRAY(ctypes.c_double).create([0]*size)

def make_variant_vt_ref(obj, var_type):
    var = automation.VARIANT()
    var._.c_void_p = ctypes.addressof(obj)
    var.vt = var_type | automation.VT_BYREF
    return var
