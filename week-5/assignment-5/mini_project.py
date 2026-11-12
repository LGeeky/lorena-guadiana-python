# Number Cruncher
numbers = [3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        smallest = numbers[0]
        for i in range(len(numbers)):
            if numbers[i] < smallest:
                smallest = numbers[i]
        print(f"The minimum is {smallest}.")

    elif choice == "2":
        largest = numbers[0]
        for i in range(len(numbers)):
            if numbers[i] > largest:
                largest = numbers[i]
        print(f"The maximum is {largest}.")

    elif choice == "3":
        try:
            target = int(input("Enter a number to search for: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        found_index = -1
        for i in range(len(numbers)):
            if numbers[i] == target:
                found_index = i
                break

        if found_index != -1:
            print(f"Found {target} at index {found_index}.")
        else:
            print(f"{target} was not found.")

    elif choice == "4":
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    temp = numbers[i]
                    numbers[i] = numbers[i + 1]
                    numbers[i + 1] = temp
                    swapped = True
        print(f"List after bubble sort: {numbers}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")