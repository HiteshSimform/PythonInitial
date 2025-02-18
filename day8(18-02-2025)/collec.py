from collections import Counter, namedtuple, deque

x = "aaabbccd"
print(Counter(x))

# namedtuple
# A namedtuple provides an easy way to create a lightweight object type with named fields, making the code more readable.
Person = namedtuple('Person',['name','age','city'])
p1=Person(name="Hitesh",age=21,city="Rajkot")

print(p1.name)
print(p1[1])

print(p1._fields) 
print(p1._asdict())

# deque

dq = deque([1,2,3,4,5])
dq.append(6)
print(dq)

dq.appendleft(0)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq.rotate(2)
print(dq)

dq.rotate(-1)
print(dq)

# Counter
