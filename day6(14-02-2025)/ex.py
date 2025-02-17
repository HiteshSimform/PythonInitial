a = [True, 0, 1, False, True, 2]
b = 0
c = 0
for i in a:
    if isinstance(i, int):
        b += 1
    elif isinstance(i, bool):
        c += 1

print(b, c)
 