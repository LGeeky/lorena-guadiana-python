student = {
    "name": "Marina Carina",
    "grade": 11,
    "subjects": ["Math", "Indigenous Studies", "Nahualt", "Civics"]
}

for key, value in student.items():
    print(key, ":", value)

student["graduated"] = False

print(student)