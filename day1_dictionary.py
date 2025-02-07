# Dictionary
# key : value
# It is like hash map
# key is unique identifier
# key is immutable, value is mutable

student = {'name':'John','age':25,'courses':['AI','ML','DL']}
print(student)

print(student['courses'])

# get method for access the key
print(student.get('name'))

print(student.get('phone','Not Found')) # if kry is not in dictionary, then we can print message by 2nd parameter string 

# we can set the key
student['phone'] = '1234'
print(student.get('phone','Not Found'))

# student name change
student['name'] = 'XYZ'
print(student)

# update
student.update({'name':'John Doe','age':27,'phone':'1234'})
print(student)

print("-----------------------------------------------------------")

for x in student:
    print(x)

print("-----------------------------------------------------------")

for key, value in student.items():
    print(key,value)

