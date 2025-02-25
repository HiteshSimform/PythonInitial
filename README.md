# Python Learning Journey - February 6-7, 2025 (with Advanced Concepts)

This document summarizes my Python learning progress on February 6th and 7th, 2025. It covers basic syntax, strings, lists, tuples, sets, dictionaries, operators, and arithmetic operations.  It also introduces several advanced Python concepts for future learning.

## February 6, 2025

### Basic Output and Variables

*   Demonstrated basic `print()` statements.
*   Assigned and printed string variables.
*   Explored single and multi-line strings.

    ```
    # 06-02-2025
    print("1")

    # 07-02-2025
    print("Hello World!!")

    message = "Hello"
    print(message)

    message1 = 'Python\'s Learning'  # \ use for single quort during string
    print(message1)

    # Multiline String

    message2 = """hfdjs
    jfdksklfd"""
    print(message2)
    ```

### String Manipulation

*   Used `len()` to find string length.
*   Accessed characters using indexing (positive and negative).
*   Implemented string slicing.
*   Used `.upper()`, `.count()`, `.find()`, and `.replace()` methods.
*   Demonstrated string concatenation and formatting using `.format()` and f-strings.
*   Explored the `dir()` function to inspect string methods and `help()` to get method documentation.

    ```
    # len() use for find the length of the string
    print(len(message2))
    print(message2)
    print(message2[-1])
    # print(message2)

    # Slicing
    print(message2[0:10])
    print(message2[:6])
    print(message2[6:])

    print(message2.upper())
    print(message2.count('dsn')) # gives number of occurences
    print(message2.find('dsb')) # gives start index of that string

    new_message2=message2.replace('AB','HJ')
    print(new_message2)

    greeting = 'Hello'
    name = 's'

    message3 = greeting + ' , ' + name
    print(message3)

    message4 = '{}, {}. Welcome!'.format(greeting,name)
    print(message4)

    message5 = f'{greeting}, {name.upper()}. Welcome!'
    print(message5)

    # dir function : The dir() function returns all properties and methods of the specified object, without the values.
    print(dir(name))

    # print(help(str.lower))
    ```

### Integers and Floats

*   Defined and printed integer and float variables.
*   Checked variable types using `type()`.

    ```
    # Integers and Floats

    num = 10
    print(num)
    print(type(num))

    num1 = 10.1
    print(num1)
    print(type(num1))
    ```

## February 7, 2025

### Lists

*   Created and printed lists.
*   Checked list type and length.
*   Accessed list elements using indexing and slicing.
*   Used `append()`, `insert()`, and `extend()` to modify lists.
*   Removed elements using `remove()` and `pop()`.
*   Reversed and sorted lists using `reverse()` and `sort()`.
*   Demonstrated the difference between `sort()` (in-place) and `sorted()` (returns a new list).
*   Used `min()`, `max()`, and `sum()` on a list of numbers.
*   Found the index of an element using `index()` and checked for membership using `in`.
*   Iterated through lists using `for` loops and `enumerate()`.
*   Joined list elements into a string using `join()` and split a string into a list using `split()`.
*   Demonstrated list mutability and how assigning a list to a new variable creates a reference, not a copy.

    ```
    # Lists, Tuples, Sets

    # Lists and tuples allows to work with sequestial Data
    # Sets are unordered collection value

    lst = ['Python', 'Django', 'Machine Learning', 'Artificial Intelligence', 'Deep Learning']
    print(lst)
    print(type(lst))
    print(len(lst))
    print(lst)
    print(lst[-2:])
    print(lst[:-2])
    print(lst[2:])
    print(lst[0:2])  # not include 2nd index
    print(lst[-6:])
    # print(lst)  # list out of range error

    lst.append('Flask')
    print(lst)

    # List is mutable

    # insert
    lst.insert(0,'FastAPI')
    print(lst)

    # add one list to another list

    lst2 = ['New Python', 'New Machine Learning']

    # lst.insert(0,lst2)
    print(lst)

    print(lst)

    # extend method
    lst.extend(lst2)
    print(lst)

    # Remove form list

    lst.remove('New Python')
    print(lst)

    # pop remove the last value
    popped = lst.pop()
    print(popped)
    print(lst)

    # reverse
    lst.reverse()
    print(lst)

    lst.sort()
    print(lst)

    lst.sort(reverse=True)

    print(lst)
    nums  = [1,5,4,2,3]
    # sort ascending
    nums.sort()
    print(nums)

    # sort descending
    nums.sort(reverse=True)
    print(nums)

    # The sort() method is a built-in list method that modifies the list in-place and returns None
    # The sorted() function, on the other hand, returns a new sorted list from the iterable, leaving the original list unchanged234. It accepts any iterable (e.g., list, tuple, string) as an argument, while list.sort() can only be used with lists

    a = [2, 3, 1, 5, 6, 4, 0]
    print(sorted(a))  # Output: [0, 1, 2, 3, 4, 5, 6]
    print(a)  # Output: [2, 3, 1, 5, 6, 4, 0]
    print(a.sort())  # Output: None
    print(a)  # Output: [0, 1, 2, 3, 4, 5, 6]

    # min, max, sum
    print(min(a))
    print(max(a))
    print(sum(a))


    # find the index from the list
    print(lst.index('Deep Learning'))
    print('Deep Learning' in lst)

    print("-----------------------------------------------------------")
    # for

    for i in lst:
        print(i)

    print("-----------------------------------------------------------")

    # enumerate for give the index, we can access index and value by this
    for index , l in enumerate(lst):
        print(index,l)

    print("-----------------------------------------------------------")

    for index , l in enumerate(lst,start=1):
        print(index,l)

    print("-----------------------------------------------------------")

    # join : use for separate the string
    lst_str = ' , '.join(lst)
    # lst_str = ' - '.join(lst)
    print(lst_str)

    print("-----------------------------------------------------------")

    new_list = lst_str.split(' , ')

    print(lst_str)
    print("-----------------------------------------------------------")
    print(new_list)
    print("-----------------------------------------------------------")

    # Example of list is mutable
    lst_test = lst
    print(lst)
    print(lst_test)
    print("-----------------------------------------------------------")


    lst='ABCD'
    print(lst)
    print(lst_test)
    ```

### Tuples

*   Created and printed tuples.
*   Demonstrated that tuples are immutable.

    ```
    # Tuples : Can't Modify , so immutable
    print("-----------------------------------------------------------")

    tuple_1 = ('Python', 'Django', 'Machine Learning', 'Artificial Intelligence', 'Deep Learning')
    tuple_2=tuple_1
    print(tuple_1)
    print(tuple_2)

    # tuple_1='ABCD'  # it gives error  : TypeError: 'tuple' object does not support item assignment
    # print(tuple_1)
    # print(tuple_2)
    ```

### Sets

*   Created and printed sets.
*   Demonstrated that sets are unordered.
*   Checked for membership using `in`.
*   Used `intersection()`, `difference()`, and `union()` methods.

    ```
    # Sets
    # use {}
    # unordered : always changes order during execution
    print("-----------------------------------------------------------")

    set_1 = {'Python', 'Django', 'Machine Learning', 'Artificial Intelligence', 'Deep Learning'}
    print(set_1)
    print('Python' in set_1)

    # intersection method for check the common values in the Sets
    # diffference method use for uncommon data from the both sets
    print("-----------------------------------------------------------")
    set_2 = {'Machine Learning','Machine Learning', 'Artificial Intelligence', 'Deep Learning'}
    print("New : ",set_2)
    print("-----------------------------------------------------------")
    print(set_1.intersection(set_2))
    print(set_1.difference(set_2))

    # union use for combine both the sets and don't repeat similar values
    print(set_1.union(set_2))
    ```

### Dictionaries

*   Created and printed dictionaries.
*   Accessed dictionary values using keys and the `get()` method.
*   Added new key-value pairs and updated existing values.
*   Iterated through dictionaries using `items()`.

    ```
    # Dictionary
    # key : value
    # It is like hash map
    # key is unique identifier
    # key is immutable, value is mutable

    student = {'name':'John','age':25,'courses':['AI','ML','DL']}
    print(student)

    print(student['courses'])

    # get method for access the key
    print(student.get('name'))

    print(student.get('phone','Not Found')) # if kry is not in dictionary, then we can print message by 2nd parameter string

    # we can set the key
    student['phone'] = '1234'
    print(student.get('phone','Not Found'))

    # student name change
    student['name'] = 'XYZ'
    print(student)

    # update
    student.update({'name':'John Doe','age':27,'phone':'1234'})
    print(student)

    print("-----------------------------------------------------------")

    for x in student:
        print(x)

    print("-----------------------------------------------------------")

    for key, value in student.items():
        print(key,value)
    ```

### Comparison Operators

*   Demonstrated the use of comparison operators (==, !=, >, <, >=, <=).

    ```
    # Comparisions

    num_1 = 3
    num_2 = 2

    # Equal
    print(num_1 == num_2)

    # Not Equal
    print(num_1 != num_2)

    # Greater Than
    print(num_1 > num_2)

    # Less Than
    print(num_1 < num_2)

    # Greater or Equal
    print(num_1 >= num_2)

    # Less or Equal
    print(num_1 <= num_2)
    ```

### Type Casting

*   Converted strings to integers using `int()`.

    ```
    # Type Casting

    x = '100'
    y = '200'

    print(x+y)

    x=int(x)
    y=int(y)
    print(x+y)
    ```

### Arithmetic Operations

*   Performed addition, subtraction, multiplication, division, floor division, exponentiation, and modulus operations.
*   Used `abs()` to get the absolute value and `round()` to round numbers.

    ```
    # Arithmetic Operations

    # Addition
    print(10+1)

    # Substractin
    print(10-1)

    # Multiplication
    print(10*2)


    # Division
    print(10/2)

    # Floor Division
    print(10//4)

    # Exponent
    print(10 ** 2)

    # Modulus
    print(10%3)

    print(3*2+1)
    print(3*(2+1))

    num=1
    num=num+1
    print(num)

    x=1
    x+=1
    print(x)

    # abs
    print(abs(-10))


    # round
    print(round(3.75))

    print(round(3.75,1))  # 2nd argument 1 is for till 1st digit we want to round
    ```

## What is Python?

*   Python is a versatile, high-level programming language known for its readability and wide range of applications. It is interpreted, object-oriented, and dynamically-typed.  It supports multiple programming paradigms [2].

## Introduction to Advanced Python Concepts

This section introduces several advanced Python concepts for future learning and exploration [1][3][4].

### 1. List Comprehensions
*   **Description**:  A concise way to create new lists based on existing iterables [1].
*   **Example**:  `squares = [x**2 for x in range(10)]` (creates a list of squares from 0 to 9).
*   **Real-life Use**:  Transforming data, filtering data, creating subsets of data.
*   **Further Learning**:  [https://python-course.eu/advanced-python/list-comprehension.php](https://python-course.eu/advanced-python/list-comprehension.php) [3]

### 2. Dictionary and Set Comprehensions

*   **Description**: Similar to list comprehensions but create dictionaries or sets [1].
*   **Example**: `square_map = {x: x**2 for x in range(5)}` (creates a dictionary mapping numbers to their squares).
*   **Real-life Use**:  Creating lookup tables, frequency counts.

### 3. Generators

*   **Description**: Functions that produce a sequence of values using the `yield` keyword. Generators are memory-efficient because they generate values on demand [3].
*   **Example**:

    ```
    def even_numbers(max):
        n = 0
        while n < max:
            yield n
            n += 2

    for num in even_numbers(10):
        print(num)
    ```

*   **Real-life Use**:  Reading large files, processing infinite streams of data.
*   **Further Learning**: [https://python-course.eu/advanced-python/generators-iterators.php](https://python-course.eu/advanced-python/generators-iterators.php) [3]

### 4. Iterators and Iterables

*   **Description**: An iterable is an object that can return an iterator. An iterator is an object that produces the next value in a sequence [3].
*   **Real-life Use**:  Custom data structures, efficient data processing.
*   **Further Learning**: [https://python-course.eu/advanced-python/iterators-iterables.php](https://python-course.eu/advanced-python/iterators-iterables.php) [3]

### 5. Decorators

*   **Description**:  A way to modify or extend the behavior of functions or methods.  Decorators are often used for logging, access control, and instrumentation [1].
*   **Example**:

    ```
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()
    ```

*   **Real-life Use**:  Implementing authentication, caching, logging.
*   **Further Learning**: [https://python-course.eu/advanced-python/decorators.php](https://python-course.eu/advanced-python/decorators.php) [3]

### 6. Closures

*   **Description**: An inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing [1].
*   **Real-life Use**:  Data encapsulation, creating specialized functions.

### 7. Lambda Functions

*   **Description**:  Small, anonymous functions defined using the `lambda` keyword [3].
*   **Example**:  `add = lambda x, y: x + y`
*   **Real-life Use**:  Short, simple operations, often used with `map()`, `filter()`, and `reduce()`.
*   **Further Learning**: [https://python-course.eu/advanced-python/lambda-functions.php](https://python-course.eu/advanced-python/lambda-functions.php) [3]

### 8. Map, Filter, Reduce

*   **Description**:
    *   `map()`: Applies a function to each item in an iterable.
    *   `filter()`:  Creates a new iterable with items that satisfy a condition.
    *   `reduce()`:  Applies a function cumulatively to the items of an iterable, reducing it to a single value [3].
*   **Real-life Use**:  Data transformation, data filtering, aggregation.
*   **Further Learning**: [https://python-course.eu/advanced-python/lambda-functions.php](https://python-course.eu/advanced-python/lambda-functions.php) [3]

### 9. Regular Expressions

*   **Description**:  A sequence of characters that define a search pattern.  Used for pattern matching in strings [3].
*   **Real-life Use**:  Data validation, parsing text, searching for patterns.
*   **Further Learning**: [https://python-course.eu/advanced-python/regular-expressions.php](https://python-course.eu/advanced-python/regular-expressions.php) [3]

### 10. Everything is an Object

*   **Description**: In Python, everything is treated as an object, including functions and modules [1]. This allows for powerful and flexible programming techniques.
*   **Real-life Use**:  Metaprogramming, dynamic code generation.

### 11. Extended Keyword Arguments
*   **Description**:  Using `*args` and `**kwargs` to pass a variable number of arguments to a function [1].
    *   `*args`:  Passes a variable number of positional arguments.
    *   `**kwargs`: Passes a variable number of keyword arguments.
*   **Real-life Use**: Creating flexible APIs, function decorators.

### 12. Testing

*   **Description**: Writing tests for your code to ensure it works correctly. Python has built-in modules like `unittest` and `doctest`, and popular third-party libraries like `pytest` [3].
*   **Real-life Use**: Ensuring code quality, preventing regressions.
*   **Further Learning**: [https://python-course.eu/advanced-python/testing-pytest.php](https://python-course.eu/advanced-python/testing-pytest.php) [3]

## Summary

This learning session covered fundamental Python concepts.  I've also started exploring advanced concepts, including comprehensions, generators, decorators, and more.  I will continue to delve deeper into these topics to become a proficient Python developer.
