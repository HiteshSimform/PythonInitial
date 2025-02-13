a = [True, 0, 1, False, True, 2]
b = 0
c = 0
for i in a:
    if isinstance(i, bool):
        b += 1
    elif isinstance(i, int):
        c += 1

print(b, c)
 
print(id(1))
print(id(bool(1)))
num = 1
numBool = bool(1)
print(id(num))
print(id(numBool))


print(isinstance(1.0, float))
print(isinstance(1, float))
print(1 == 1.0)

print(isinstance(True, int))
print(type(isinstance(1, int)))

print(issubclass(bool, int))
print(issubclass(int, bool))

print(isinstance(True, (float, int)))

print(isinstance(str,int))