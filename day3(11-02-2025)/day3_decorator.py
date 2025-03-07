def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()

display()

# display = decorator_function(display)   this line eqials to 
'''
@decorator_function
def display():
    print('display function ran')
'''
