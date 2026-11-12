# Number Cruncher (refactored into functions)
numbers = [3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]


def find_min(numbers):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest


def find_max(numbers):
    largest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest


def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


def bubble_sort(numbers):
    # Work on a copy so the original list is not changed
    sorted_list = []
    for i in range(len(numbers)):
        sorted_list.append(numbers[i])

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_list) - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = temp
                swapped = True
    return sorted_list


def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    return input("Choose an option (1-5): ")


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            print(f"The minimum is {find_min(numbers)}.")

        elif choice == "2":
            print(f"The maximum is {find_max(numbers)}.")

        elif choice == "3":
            try:
                target = int(input("Enter a number to search for: "))
            except ValueError:
                print("Please enter a whole number.")
                continue

            index = search(numbers, target)
            if index != -1:
                print(f"Found at index {index}.")
            else:
                print("Not found.")

        elif choice == "4":
            result = bubble_sort(numbers)
            print(f"List after bubble sort: {result}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()