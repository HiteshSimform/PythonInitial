# # 11-02-2025

# class Student:
#     name="Hitesh"
#     # def __init__(self):
#     #     print(self)
#     def __init__(self,fullname):
#         self.name=fullname
#         print("Adding new student in Database")



# s1 = Student()
# print(s1)
# print(s1.name)

# # Constructor

# # __init__

import sys

# Creating a dictionary with 1000 items
my_dict = {i: i * 2 for i in range(1000)}
print("Size of the dictionary:", sys.getsizeof(my_dict))
print(my_dict)

# Adding more items and checking again
for i in range(1000, 2000):
    my_dict[i] = i * 2
print("Size of the dictionary after adding more items:", sys.getsizeof(my_dict))
import sys

# Creating a dictionary with 1000 items
my_dict = {i: i * 2 for i in range(1000)}
print("Size of the dictionary:", sys.getsizeof(my_dict))

# Adding more items and checking again
for i in range(1000, 2000):
    my_dict[i] = i * 2
print("Size of the dictionary after adding more items:", sys.getsizeof(my_dict))

# Clearing the dictionary
my_dict.clear()
print("Size of the dictionary after clearing:", sys.getsizeof(my_dict))

# Clearing the dictionary
my_dict.clear()
print("Size of the dictionary after clearing:", sys.getsizeof(my_dict))



# Constructor

# Default Constructor
# Parameterized Constructor

class Student:

    # default constructor
    def __init__(self):
        pass

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student in Database")

 
#  Static Methods


# 4 Pillars

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# Dunder Function
# Operator Overloading

