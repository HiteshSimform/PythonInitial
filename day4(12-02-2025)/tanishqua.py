# Must write code-snippet for any programming language ;)
print("hello World")

# print(id('May'))
# month = 'May'
# print(id(month))

number_1 =  2678
number_2 = '2678'
number_3 = '2679'

print(id(number_1))
print(id(number_2))
number_2 = 2679
print(id(number_3))
print(id(number_2))


for i in range(number_1, number_1+20):
    print(id(i), i)
i = 0
while i < 20:
    print(id(i), i)
    i += 1

