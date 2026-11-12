import numpy as np

# Join 2 arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3 = np.concatenate((arr1, arr2))
print(arr3)

# Join two 2D arrays along rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3)