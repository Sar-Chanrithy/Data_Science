# Dictionary = Data ជា Key → Value។
student = {
    "name": "Dara",
    "age": 20,
    "score": 85
}

print(student["name"])
print(student["score"])

# add
student["city"] = "Phnom Penh"
# update
student["score"] = 90
# loop
for key, value in student.items():
    print(key, value)