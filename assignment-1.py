#Section 1: Variables and Types

name = "Student"
age = 45
height = "5.4"

print(name,type(name))
print(age,type(age))
print(height,type(height))

#Section 2: User Input and Math

name = input("Please enter your name: ")
Year_of_birth = input("Please enter the year you were born: ")
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f"Hello, {name}! You are approximately {age} years old.")

#Section 3: Type Conversion and f-strings
      
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
print("         RECEIPT")
print("==========================")
print(f"Item:     {item}")
print(f"Price:    ${price:.2f}")
print(f"Quantity: {quantity}")
print("--------------------------")
print(f"Total:    ${total:.2f}")
print("==========================")
