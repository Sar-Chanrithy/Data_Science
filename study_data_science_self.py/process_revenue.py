import numpy as np

# Months 1 to 4
x = np.array([1, 2, 3, 4])
y = np.array([1000.0, 2000.0, 3000.0, 6400.0])

# Fit a polynomial pattern (degree 2)
model = np.poly1d(np.polyfit(x, y, deg=2))

# Predict Month 5 (ឧសភា / May)
month_5_prediction = model(5)
print(f"Projected Month 5: $ {month_5_prediction:,.2f}")