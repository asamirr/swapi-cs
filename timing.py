import time
from functools import wraps 

def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print(f'{f.__name__} took {(end - start):.3f} secs')
        return result
    return wrapper