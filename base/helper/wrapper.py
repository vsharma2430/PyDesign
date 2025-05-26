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


