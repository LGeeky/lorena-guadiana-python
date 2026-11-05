# Input Validation with a While Loop
# This program prompts the user to enter a positive integer and validates the input.
while True:
    user_input = input("Enter a positive integer: ")

    try:
        number = int(user_input)
    except ValueError:
        print("That's not a positive integer. Try again.")
        continue

    if number > 0:
        print(f"Got it: {number}")
        break
    else:
        print("That's not a positive integer. Try again.")