# 10-02-2025

# def hello_func():
#     pass

# hello_func()
# print(hello_func)
# print(hello_func())

# def hello_func():
#     print('Hello Function')
# hello_func()

# Keep Code DRY

def hello_func():
    return 'Hello Function'

print(hello_func())

print(len('Test'))

print(hello_func().upper())

def hello_func_1(greeting):
    return '{} Function.'.format(greeting)

print(hello_func_1('Hi'))


def hello_func_2(greeting,name='You'):
    return '{}, {}'.format(greeting,name)

print(hello_func_2('Hi',name='Hitesh'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info()

student_info('AI','ML', name='Hitesh',age=21)

# kwargs is dictionary with key and values

  
# pass by value
# pass by reference
# Function Arguments

# Types of Argumrnts

# formal arguments
# actual argumetns  : position, keyword, default, variable length

def person(name, age):
    print(name)
    print(age)

person("Hitesh",21)

# keyword
person(age=21,name='hitesh')

# default : 
# def person(name, age=18):
#     print(name)
#     print(age)

# person("Hitesh")

# Keyworded Variable Length Arguments

# Global Keyword

# x=globals()['a']
# globals()['a'] = 15

# Pass List to a function
# odd even count

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

lst = [20,25,14,19,16,24,20,47,26]

even,odd=count(lst)
print(even)
print(odd)

print("Even: {} and odd : {}".format(even,odd))



# fibbonacci

def fib(n):
    a=0
    b=1

    if n==1:
        print(a)

    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

fib(10)

# Factorial
