names = ("Sok", "Sokha", "Chanda")
# Reorder
temp = list(names)
temp.sort()
names = tuple(temp)
print(names)

temp = list(names)
temp.reverse()
names = tuple(temp)
print(names)