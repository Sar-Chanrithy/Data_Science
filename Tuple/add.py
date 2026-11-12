names = ("Sok", "Sokha", "Chanda")

# 1. Add
temp = list(names)
temp.append("Vichet")
names = tuple(temp)

temp = list(names)
temp.extend(["Bora", "Dara"])
names = tuple(temp)

temp = list(names)
temp.insert(1, "Vireak")
names = tuple(temp)
print(names)