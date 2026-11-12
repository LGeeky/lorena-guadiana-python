# Linear Search
# This program performs a linear search on a list of names.
# The search pattern looks through data for a specific item or condition. It typically uses a for loop with break,
# or a while loop.

# Each person has an index position number. 
# Lorena is position 0, Sarah is 1, Candace is 2, John is 3, Frances is 4, and Tony is 5.

names = ["Lorena", "Sarah", "Candace", "John", "Frances", "Tony"]

# Telling the program to ask the name to look for.
search_name = input("Enter a name to search for: ")

# Flag for when “not found yet.” Since valid indexes are 0 or above, -1 can’t be confused with a real result.
found_index = -1

# The for loop will iterate through the list of names, checking each one against the search_name.
# If it finds a match, it will set found_index to the current index and break out of the loop.
# If it doesn’t find a match, found_index will remain -1, indicating that the name was not found in the list.
for i in range(len(names)):
    if names[i] == search_name:
        found_index = i
        break

# After the loop, the program checks if found_index is not -1. If it’s not -1, it means the name was found, 
# and it prints the index. If it’s still -1, it means the name was not found, and it prints a message indicating that.
if found_index != -1:
    print(f'Found "{search_name}" at index {found_index}.')
else:
    print(f'"{search_name}" was not found in the list.')