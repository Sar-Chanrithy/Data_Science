import pandas as pd

data = {
    "Name": ["Dara", "Soka", "Vanna"],
    "Age": [20, 21, 19],
    "Score": [85, 90, 70]
}

df = pd.DataFrame(data)

print(df)