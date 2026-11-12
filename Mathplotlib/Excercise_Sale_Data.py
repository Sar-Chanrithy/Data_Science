import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [12500, 14200, 13800, 16100, 17500, 19000,
              18400, 20200, 21500, 23000, 26800, 31000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
bars = plt.bar(df['Month'], df['Sales'], color='steelblue', width=0.6)

plt.bar_label(bars, fmt='{:,.0f}', padding=3, fontsize=9)
plt.ylim(0, max(df['Sales']) * 1.12)

plt.title('Monthly Sales (Jan - Dec)')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()