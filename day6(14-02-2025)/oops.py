# 14-02-2025

# Functional Programming
# Object Oriented Programming

# python is also functional Programming

# class A:
#     def config(self):
#         print("Hello")
# a=A()
# a.config()


class A:
    def display(self):
        print("Display method from class A")

class B(A):
    def display(self):
        print("Display method from class B")

class C(A):
    def display(self):
        print("Display method from class C")

class D(B, C):
    pass

d = D()
d.display()
print(D.mro())
