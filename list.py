students = ["Dara", "Sokha", "Vanna"]

print(students)
print(students[0])
# add
students.append("Chan")
# remove
students.remove("Sokha")
# loop
for student in students:
    print(student)
# list number
scores = [70, 80, 90, 85]

print(sum(scores))
print(max(scores))
print(min(scores))
print(len(scores))
# average
average = sum(scores) / len(scores)

print(average)