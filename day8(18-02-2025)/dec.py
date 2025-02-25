# def mydecorator(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper

# @mydecorator
# def dosomething():
#     print("Hi")

# dosomething()



# def mydecorator(func):
#     def wrapper(self,a,b):
#         self.a=a
#         self.b=b

#         func()
#         y = a+b
#     return wrapper

# @mydecorator
# def add(self,a,b):
#     return self.a*self.b

# print(add(3,4))

# def mydecorator(func):
#     def wrapper(self, a, b):
#         self.a = a
#         self.b = b
#         return func(self, a, b) 
#     return wrapper

# class Calculator:
#     @mydecorator
#     def add(self, a, b):
#         return self.a + self.b 
# calc = Calculator()
# print(calc.add(3, 4))


def mydecorator(func):
    def wrapper(*args,**kwargs):
        print("Start")
        res = func(*args,**kwargs)
        print("End")
        return res
    return wrapper

@mydecorator
def add(a,b):
    return a+b
print(add(1,2))
