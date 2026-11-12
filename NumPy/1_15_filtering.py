import numpy as np

# Boolean Index Array
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# Boolean Mask
arr = np.array([41, 42, 43, 44, 45, 46])
mask = arr > 43
print(mask)

newarr = arr[mask]
print(newarr)