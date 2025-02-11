# 07-02-2025
# Lists, Tuples, Sets

# Lists and tuples allows to work with sequestial Data
# Sets are unordered collection value

lst = ['Python', 'Django', 'Machine Learning', 'Artificial Intelligence', 'Deep Learning']
print(lst)
print(type(lst))
print(len(lst))
print(lst[2])
print(lst[-2:])
print(lst[:-2])
print(lst[2:])
print(lst[0:2])  # not include 2nd index
print(lst[-6:])
# print(lst[7])  # list out of range error

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

print(lst[0])

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


lst[0]='ABCD'
print(lst)
print(lst_test)


# Tuples : Can't Modify , so immutable
print("-----------------------------------------------------------")

tuple_1 = ('Python', 'Django', 'Machine Learning', 'Artificial Intelligence', 'Deep Learning')
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0]='ABCD'  # it gives error  : TypeError: 'tuple' object does not support item assignment
# print(tuple_1)
# print(tuple_2)

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

# Empty List
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()


print("-----------------------------------------------------------")

# Dictionary
# key : value
# It is like hash map
# key is unique identifier

