# 13-02-2025

# Decorators
def div(a: int, b: int):
    """
    Divides two numbers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.
    """
    print(a / b)


def smart_div(func):
    """
    A decorator that ensures the larger number is divided by the smaller number.

    Args:
        func (function): The function to be decorated (in this case, the div function).

    Returns:
        function: The inner function that performs the smart division.
    """
    def inner(a, b):
        """
        The inner function that swaps the arguments if a < b and then calls the original function.

        Args:
            a (int): The first number.
            b (int): The second number.
        """
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


# div = smart_div(div)
# div(1, 2)

@smart_div
def div(a:int,b:int):
    print(a/b)
div(1.5,5.5)
