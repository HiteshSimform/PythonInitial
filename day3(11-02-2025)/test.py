numbers = [1, 3, 10, 45, 6, 50]

# Filter even numbers and then square them
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # Output: [100, 36, 2500]

def is_even(x):
    return x % 2 == 0

def square(x):
    return x**2

result = list(map(square, filter(is_even, numbers)))
print(result)

result = [x**2 for x in numbers if x % 2 == 0]
print(result)