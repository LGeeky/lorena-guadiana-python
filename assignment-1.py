#Section 1

name = "Student"
age = 45
height = "5.4"

#Section 2

name = input("Please enter your name: ")
Year_of_birth = input("Please enter the year you were born: ")
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f"Hello, {name}! You are approximately {age} years old.")
