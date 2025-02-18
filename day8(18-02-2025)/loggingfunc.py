import time
import functools

def advanced_decorator(max_calls=5):
    def decorator(func):
        cache = {}
        call_count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count
            call_count += 1

            if call_count > max_calls:
                raise Exception(f"Function {func.__name__} has exceeded max call limit of {max_calls}")

            # Log function call details
            print(f"Calling function {func.__name__} with arguments: {args} and kwargs: {kwargs}")

            # Check cache first
            if (args, tuple(kwargs.items())) in cache:
                print("Using cached result...")
                return cache[(args, tuple(kwargs.items()))]

            start_time = time.time()

            # Call the actual function
            result = func(*args, **kwargs)

            end_time = time.time()

            # Log execution time
            print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")

            # Log return value
            print(f"Function {func.__name__} returned: {result}")

            # Cache the result
            cache[(args, tuple(kwargs.items()))] = result

            return result

        return wrapper

    return decorator

# Example usage

@advanced_decorator(max_calls=3)
def multiply(a, b):
    time.sleep(1)  # Simulate a time-consuming operation
    return a * b

try:
    print(multiply(3, 4))  # First call
    print(multiply(3, 4))  # Cached result
    print(multiply(2, 5))  # Another call
    print(multiply(3, 4))  # Cached result
    print(multiply(3, 4))  # Will raise exception after the max call limit
except Exception as e:
    print(e)
