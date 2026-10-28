students = [
    {"name": "Jazmine", "score": 95, "subject": "Math" },
    {"name": "Carlos", "score": 70, "subject": "Spanish" },
    {"name": "Amir", "score": 91, "subject": "Physics" },
    {"name": "Priya", "score": 74, "subject": "Literature" }
]

# Finding the top scorer
top_score = students[0]["score"]
top_name = students[0]["name"]

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

# Calculating the class average
total = 0
for student in students:
    total += student["score"]

average = total / len(students)

# Listing the unique subjects
subjects = set()
for student in students:
    subjects.add(student["subject"])

# Listing the high scorers (score > 75)
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print("Top scorer:      ", top_name, f"({top_score})")
print("Class average:   ", average)
print("Subjects offered:", subjects)
print("High scorers:    ", high_scorers)