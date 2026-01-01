import numpy as np
arr = np.array(6)
print(arr)
print(arr.ndim)
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)
arr = np.array([
                [1, 2, 3],
                [4, 5, 6]
            ])
print(arr)
print(arr.ndim)
arr = np.array([
                [
                    [1, 2, 3],
                    [4, 5, 6]
                ],
                [
                    [1, 2, 3],
                    [4, 5, 6]
                ]
            ])
print(arr)
print(arr.ndim)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
