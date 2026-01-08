"""
How To Create Your Own ufunc
To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""
"""
How To Create Your Own ufunc
To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""
import numpy as np
def myadd(x, y):
    return x + y
x = np.frompyfunc(myadd, 2, 1)
print(x(5, 3))
print(x([1, 2, 3], 
        [4, 5, 6]))
# print(myadd(5, 3))

# print(myadd([1, 2, 3], 
#             [4, 5, 6]))
print(type(np.add))

# print(type(np.myadd))
print(type(np.concatenate))
# print(type(np.blahblah))
# Use an if statement to check if the function is a ufunc or not:
if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')