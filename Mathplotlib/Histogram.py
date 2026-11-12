import matplotlib.pyplot as plt
import numpy as np

# Generate 250 students' heights
heights = np.random.normal(170, 10, 250)

# Create Histogram
plt.hist(heights, bins=10, color='skyblue', edgecolor='black')

plt.title("Distribution of Male Student Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Number of Students")

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()