"""
Finding GCD (Greatest Common Divisor)
The GCD (Greatest Common Divisor), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.
"""


"""
Example
Find the HCF of the following two numbers:
"""
import numpy as np

num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

"""
Finding GCD in Arrays
To find the Highest Common Factor of all values in an array, you can use the reduce() metho
"""
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)