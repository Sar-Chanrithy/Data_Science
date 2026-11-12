import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 8, 4, 10, 6]

plt.plot(
    x, y,
    marker='o',
    markersize=12,
    markerfacecolor='pink',
    markeredgecolor='blue',
    markeredgewidth=2,
    linestyle='--',
    linewidth=2,
    color='green'
)

plt.show()