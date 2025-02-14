# 14-02-2025

# Exception Handling

a=5
b=2

try:
    print("resource Open")
    print(a/b)
    print("resource Closed")
except Exception as e:
    print("Not Divide by Zero : ", e)
finally:
    print("resource Closed")