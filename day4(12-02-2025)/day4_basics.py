# # 12-02-2025

# # Enclosing
# def outer():
#     x = 'outer x'
#     def inner():
#         # nonlocal x
#         x = 'inner x'  # if i comment this x than x value is 'outer x'
#         print(x)
#     inner()
#     print(x)

# outer()

# # if i comment outer x than it will give the error

# # nonlocal x : use for change the state of the closure

# # slicing Lists and Strings

# my_list = [0,1,2,3,4,5,6,7,8,9]

# print(my_list[1])
# print(my_list[-1])
# print(my_list[-10])

# # list[start:end:step]

# print(my_list[0:6:2])
# print(my_list[-7:-2])
# print(my_list[-1:2:-1])

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# res = list(filter(None, list1))
# print(res)

# # For the strings

# name = 'hitesh'
# print(name)
# print(name[::-1])
# print(name[-2:])

# # List Comprehensions 

# nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = [n for n  in nums]
# print(my_list)

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# print("------------------")
# a = map(lambda n: n**n,nums)
# print(list(a))

# lst = [n for n in nums if n%2==0]
# print(lst)

# my_list = filter(lambda n:n%2==0,nums)
# print(my_list)
# print(list(my_list))

# # 

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# Dictionary Comprehensions

nums = ['1','2','3','4']
names = ['a','b','c','d']

# print(zip(nums,names))

# print(list(zip(nums,names)))

my_dict = {}
for nums,names in zip(nums,names):
    my_dict[nums] = names
print(my_dict)

print(nums)
print(names)

my_dict = {nums:names for nums,names in zip(nums,names)}
print(my_dict)

# if name not equal to c
# my_dict = {num:name for num,name in zip(nums,names) if name != 'c'}
# print(my_dict)

# none case, constant, random, dynamic run time format
# == and is Comparision

# sequence
# iterable and iterators
# generators

# ordered dictionary

# Sorting List , Tuples

# sort and sorted function

# key parameter in sorted

# issubset and issuperset

# attrgetter

# String Formatting

# OS module

import os
# os.chdir('/home/Desktop/Training/Python/day4(12-02-2025)')
# os.makedirs('test/test1')
# os.removedirs('test/test1')
# print(os.listdir())
 
x=10.5
print(int(x))

# File Objects

f = open('day4(12-02-2025)/day4_learning.txt','r')
print(f.readlines())
f.close()

a=7.5+7.5j
b=2.5
print ("Division of complex and float")
print ("a =",a,"b =",b,"a/b =",a/b)
print ("a =",a,"b =",b,"b/a =",b/a)

# Define a complex number and a float
complex_num = 4 + 3j  # 4 + 3i
float_num = 2.0

# Perform the division
result =  float_num / complex_num 

# Print the result
print(f"Result of division: {result}")
