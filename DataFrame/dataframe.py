import pandas as pd

data = {
    "Name": ["Dara", "Sopha", "Rithy"],
    "Age": [20, 21, 20],
    "Score": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)

print(df.Age)
print(df.Name)
print(df.Score)

print(df["Name"])

print(df.shape)
print(df.shape[0])
print(df.shape[1])

print(df[["Name", "Age"]])


