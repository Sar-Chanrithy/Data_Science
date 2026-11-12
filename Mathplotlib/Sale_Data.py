import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [12500, 14200, 13800, 16100]
}

df = pd.DataFrame(data)

plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.show()