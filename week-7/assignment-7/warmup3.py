import os

# Printing the current working directory
print(os.getcwd())

# Checking that the expenses file exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# Building the path from its parts and printing it
path = os.path.join("..", "data", "expenses.csv")
print(path)