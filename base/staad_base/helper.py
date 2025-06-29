point_precision = 3

def try_catch_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except :
            print(f"API error in {func.__name__}")
            return None
    return wrapper

def first_non_zero(lst)->float:
    for val in lst:
        if val != 0:
            return val
    return 0  # or raise an exception if needed

def convert_kn_to_mt(x):
    return x*0.10197162129779283

def unique_list(x):
    return list(dict.fromkeys(x))

open_array = lambda array,index=1 : [x[index] for x in enumerate(array)]