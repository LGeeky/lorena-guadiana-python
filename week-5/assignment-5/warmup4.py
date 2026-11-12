# FizzBuzz
# This program prints the numbers from 1 to 30. For multiples of three, it prints "Fizz" instead of the number, 
# and for multiples of five, it prints "Buzz". For numbers which are multiples of both three and five, it prints "FizzBuzz".

# The program uses a for loop to iterate through the numbers from 1 to 30. 
# It checks each number to see if it is divisible by both 3 and 5, just 3, or just 5, and prints the appropriate output. 
for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)