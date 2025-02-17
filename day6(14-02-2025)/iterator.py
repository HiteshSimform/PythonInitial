# 14-02-2025
# Iterators

nums = [7,8,9,5]
# print(nums[3])
# print(nums[5]) # Error : IndexError: list index out of range

for i in nums:
    print(i)

it = iter(nums)
print(it.__next__())

print(next(it))

print("------------------")
for i in nums:
    print(i)


print("------------------")

# __next__ and __iter__ use for create the iteraator

class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val= self.num
            self.num*=2
            return val
        else:
            raise StopIteration
        
values = TopTen()
# print(next(values))
for i in values:
    print(i)