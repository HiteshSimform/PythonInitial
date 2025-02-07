import time
import functools

def measure_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@measure_execution_time
def sleepy_function(duration):
    time.sleep(duration)

sleepy_function(2)
# Output: Execution time of sleepy_function: 2.0008 seconds


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2) 
    
print(fib(40))
