names = ("Sok", "Sokha", "Chanda")
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