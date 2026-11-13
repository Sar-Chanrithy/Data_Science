import matplotlib.pyplot as plt
import pandas as pd

# Create the DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [12500, 14200, 13800, 16100, 17500, 19000,
              18400, 20200, 21500, 23000, 26800, 31000]
}

df = pd.DataFrame(data)

# Create Bar Chart
plt.figure(figsize=(10, 5))
bars = plt.bar(df['Month'], df['Sales'], color='steelblue', width=0.6)

# Add numbers above bars
plt.bar_label(bars, fmt='{:,.0f}', padding=3, fontsize=9)

# Set Y-axis limit
plt.ylim(0, max(df['Sales']) * 1.12)

# Title and labels
plt.title('Monthly Sales (Jan - Dec)')
plt.xlabel('Month')
plt.ylabel('Sales ($)')

# Grid
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()