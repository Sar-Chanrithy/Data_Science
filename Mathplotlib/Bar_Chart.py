import matplotlib.pyplot as plt

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

sales = [10, 30, 20, 15]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Quantity")

plt.show()