# Generators
# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()
# print(g)

# print(sum(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for i in g:
#     print(i)

# print(sum(g))


# file handling
# 10 mb or more mb file
# 50000 lines file
# 500000 lines add in file
# snap installation
# desktop
# 200 mb file, check in memory, 
# how many cores
# 

# htop in terminal


import sys
def firstn(n):
    nums=[]
    num=0
    while num<n:
        nums.append(num)
        num+=1
    return nums

def firstn_generator(n):
    num = 0
    while num<n:
        yield num
        num+=1

# print(sys.getsizeof(firstn(1000000000)))
# print(sys.getsizeof(firstn_generator(1000000000)))
# don't do this