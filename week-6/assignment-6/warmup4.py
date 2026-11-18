def is_valid_score(score):
    return 0 <= score <= 100

score = int(input("Enter a score: "))

if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")