import csv
import os
from datetime import datetime

input_path = os.path.join("..", "data", "expenses.csv")

# 1. Making surefile exists before opening it
if not os.path.exists(input_path):
    print("Error: ../data/expenses.csv not found.")
else:
    # 2. Reading the CSV into a list of dictionaries
    expenses = []
    with open(input_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 3. Converting amount to a float
            row["amount"] = float(row["amount"])
            expenses.append(row)

    # 4. Keeping only the Food rows
    food_expenses = []
    for row in expenses:
        if row["category"] == "Food":
            food_expenses.append(row)

    # 5. Adding up the Food total
    total = 0
    for row in food_expenses:
        total += row["amount"]

    # 6. Writing the report
    today = datetime.now().strftime("%B %d, %Y")
    with open("food_report.txt", "w") as report:
        report.write(f"Food Expense Report — generated {today}\n")
        for row in food_expenses:
            report.write(f"{row['date']}: ${row['amount']:.2f}\n")
        report.write(f"Total: ${total:.2f}\n")

    print("Report written to food_report.txt")