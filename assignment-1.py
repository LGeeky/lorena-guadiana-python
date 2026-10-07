#Section 1: Variables and Types
#a variable is a name that stores a piece of data. 
#it's like a labeled container where we can choose the label, and Python remembers 
#what's inside

name = "Student"
age = 45
height = "5.4"

print(name,type(name))
print(age,type(age))
print(height,type(height))

#Section 2: User Input and Math
#the input() function is used to take input from the user.

name = input("Please enter your name: ")
Year_of_birth = input("Please enter the year you were born: ")
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f"Hello, {name}! You are approximately {age} years old.")

#Section 3: Type Conversion and f-strings
#the float() function is used to convert numbers or numeric strings into 
#floating-point numbers, which are decimal point

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
product = num1 * num2
print(f"{num1} × {num2} = {product}")

#Section 4: Formatted Receipt

item = "Python textbook"
price = 29.99
quantity = 2
total = price * quantity

print("==========================")
print("           RECEIPT")
print("==========================")
print(f"Item:     {item}")
print(f"Price:    ${price:.2f}")
print(f"Quantity: {quantity}")
print("--------------------------")
print(f"Total:    ${total:.2f}")
print("==========================")

#Section 5: Mini-Project - Profile Card

name = input("What's your name? ")
hometown = input("Where are you from? ")
hobby = input("What's your favorite hobby? ")
fun_fact = input("Tell me one fun fact about yourself: ")
birth_year = int(input("What year were you born? ")) #birth year is wrapped in int() so we can do math with it

#date.today().year gets the current year so the age is calculated automatically
age = date.today().year - birth_year

border = "=" * 45 #centers the title with a 45 character border
title = f"PROFILE: {name}" # sets up the profile card name box at top

print()
print(border)
print(f"{title:^45}")   # centered in 45characters
print(border)
print(f"{'Hometown:':<12}{hometown}")
print(f"{'Hobby:':<12}{hobby}")
print(f"{'Fun fact:':<12}{fun_fact}")
print(f"{'Age:':<12}{age}")
