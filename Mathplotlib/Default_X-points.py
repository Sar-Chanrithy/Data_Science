import matplotlib.pyplot as plt
import numpy as np

# If we do not specify the points on the x-axis,
# they will get the default values 0, 1, 2, 3
ypoints = np.array([2, 4, 5, 5, 7, 8])

plt.plot(ypoints)
plt.show()
