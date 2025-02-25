# 06-02-2025
print("1")

# 07-02-2025
print("Hello World!!")

message = "Hello"
print(message)

message1 = 'Python\'s Learning'  # \ use for single quort during string
print(message1)

# Multiline String

message2 = """Hitesh Jethava AB
Simform Solutions LLP"""
print(message2)

# len() use for find the length of the string
print(len(message2))
print(message2[0])
print(message2[-1])
# print(message2[50])

# Slicing
print(message2[0:10])
print(message2[:6])
print(message2[6:])

print(message2.upper())
print(message2.count('Hitesh'))
print(message2.find('Jethava')) # gives start index of that string

new_message2=message2.replace('AB','HJ')
print(new_message2)

greeting = 'Hello'
name = 'Hitesh'

message3 = greeting + ' , ' + name
print(message3)

message4 = '{}, {}. Welcome!'.format(greeting,name)
print(message4)

message5 = f'{greeting}, {name.upper()}. Welcome!'
print(message5)

# dir function : The dir() function returns all properties and methods of the specified object, without the values.
print(dir(name))

# print(help(str.lower))



# Integers and Floats

num = 10
print(num)
print(type(num))

num1 = 10.1
print(num1)
print(type(num1))