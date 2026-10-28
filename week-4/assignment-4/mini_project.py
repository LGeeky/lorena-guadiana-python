
# My loop will track two variables:top_score (the highest score seen so far) 
# and top_name (the name of the student who has that score).

#The most confusing part of working with a list of dictionaries was keeping track of 
# what I was holding at each level. The students list holds dictionaries, and each 
# dictionary holds values, so I had to think about first getting a student 
# out of the list, then getting a value out of that student. At first I mixed these up.
students = [
    {"name": "Jazmine", "score": 95, "subject": "Math" },
    {"name": "Carlos", "score": 70, "subject": "Spanish" },
    {"name": "Amir", "score": 91, "subject": "Physics" },
    {"name": "Priya", "score": 74, "subject": "Literature" }
]

# Finding the top scorer
# Before the loop, I set top_score and top_name to the values from the first student on the list.
top_score = students[0]["score"]
top_name = students[0]["name"]

#Then I looped through every student and compare their score to the current top_score.
for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

# Calculating the class average
# I added each score to total in the loop, then divided by len(students) after the loop ended
total = 0
for student in students:
    total += student["score"]

average = total / len(students)

# Listing the unique subjects
# I added each subject to a set in the loop to handle unique subjects since .add() ignores duplicates
subjects = set()
for student in students:
    subjects.add(student["subject"])

# Listing the high scorers (score > 75)
# I used the if statement to check if the score is greater than 75, and .append() adds the name 
# to the list if it is.
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print("Top scorer:      ", top_name, f"({top_score})")
print("Class average:   ", average)
print("Subjects offered:", subjects)
print("High scorers:    ", high_scorers)