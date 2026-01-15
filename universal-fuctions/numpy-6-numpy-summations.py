"""
Summations
What is the difference between summation and addition?

Addition is done between two arguments whereas summation happens over n elements.
"""

"""
Example
Add the values in arr1 to the values in arr2
"""
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)

print(arr1)
print(arr2)
print(newarr)

"""
Example
Sum the values in arr1 and the values in arr2
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])

print(newarr)

"""
Summation Over an Axis
If you specify axis=1, NumPy will sum the numbers in each array.
"""
# If you specify axis=1, NumPy will sum the numbers in each array.
"""
Example
Perform summation in the following array over 1st axis
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)
print(newarr)


"""
Example
Perform summation in the following array over 0th axis
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=0)
print(newarr)

"""
Cummulative Sum
Cummulative sum means partially adding the elements in array.

E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

Perfom partial sum with the cumsum() function.
"""
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)