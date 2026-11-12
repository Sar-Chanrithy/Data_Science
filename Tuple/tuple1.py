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

# 2. Remove
temp = list(names)
temp.remove("Sok")
names = tuple(temp)

temp = list(names)
last_name = temp.pop()
names = tuple(temp)

temp = list(names)
temp.pop(0)
names = tuple(temp)
print(names)
print(last_name)

# 3. Reorder
temp = list(names)
temp.sort()
names = tuple(temp)
print(names)

temp = list(names)
temp.reverse()
names = tuple(temp)
print(names)