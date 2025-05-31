import time 
from logging import Logger

def timeis(func): 
    '''Decorator that reports the execution time.'''
  
    def wrap(*args, **kwargs): 
        start = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 
          
        print(func.__name__, end-start) 
        return result 
    return wrap 

def design_details(code:str=None,clause=None,units=None): 
    '''Decorator that reports design details.'''
    def decorator(func):
        def wrap(*args, **kwargs): 
            result = func(*args, **kwargs) 
            if(code!=None):
                print(func.__name__, f'belongs to {code} Cl. {clause}') 
            if(units is not None):
                return result * units
            else:
                return result
        return wrap
    return decorator 

def print(func): 
    '''Decorator that prints in a single line in jupyer'''
    def wrap(*args, **kwargs): 
        result = func(*args, **kwargs) 
        print(result) 
        return result 
    return wrap 

def memoize_steel_profile_creation(func):
    cache = {}
    def memoized(*args):
        # Convert args to a cache key (assuming profile is the second argument)
        key = (args[0], str(args[1]), args[2], args[3], args[4])  # Convert profile to string if needed
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    return memoized

def memoize_concrete_profile_creation(func):
    cache = {}
    
    def memoized(*args):
        # Create a cache key based on the string representation of arguments
        key = (str(args[0]), str(args[1]))
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    
    return memoized
