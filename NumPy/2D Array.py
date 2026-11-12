import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

# 3. 2D Array

# វាស្រដៀង Table / Matrix

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(data)

# 4. Useful functions

numbers = np.array([10, 20, 30, 40, 50])

print(np.mean(numbers))  # Average
print(np.max(numbers))   # Maximum
print(np.min(numbers))   # Minimum
print(np.sum(numbers))   # Total