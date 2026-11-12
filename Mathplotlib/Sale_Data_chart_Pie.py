import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [12500, 14200, 13800, 16100, 17500, 19000,
              18400, 20200, 21500, 23000, 26800, 31000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 8))

plt.pie(
    df['Sales'],
    labels=df['Month'],
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False
)

plt.title('Monthly Sales Share (Jan - Dec)')
plt.tight_layout()
plt.show()