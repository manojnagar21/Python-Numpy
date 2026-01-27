from functools import reduce
# map
nums = [1, 2, 3, 4, 5]
newList = []
"""
def square(n):
    return n * n
"""
"""
for x in nums:
    # newList.append(x * x)
    newList.append(square(x))
print(newList)
"""

# newList = list(map(square, nums))
newList = list(map(lambda x: x * x, nums))
# print(newList)

# filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = []
"""
def findEven(n):
    if n % 2 == 0:
        return n
"""
"""
for x in nums:
    # if x % 2 == 0:
        # newList.append(x)
    if findEven(x) == None:
        pass
    else:
        newList.append(findEven(x))
print(newList)
"""

newList = list(filter(lambda x: x % 2 == 0, nums))

# print(newList)

#reduce
nums = [1, 2, 3, 4, 5]
sum = 0

"""
def addSum(nums):
    sum = 0
    for x in nums:
        sum = sum + x
    return sum
"""
"""
for x in nums:
    sum = sum + x

print(sum)
"""
# print(addSum(nums))
print(reduce(lambda x, y: x + y, nums))

# lambda
nums = [1, 2, 3, 4, 5]
newList = []

"""
def square(n):
    return n * n
"""

newList = list(map(lambda x: x * x, nums))
print(newList)


a = lambda a, b: a + b
print(a(3, 2))
print(a(5, 2))


def myFunc(num):
    return lambda x: x * num

a = myFunc(5)
print(a(2))
print(a(4))

b = myFunc(10)
print(b(2))
print(b(4))