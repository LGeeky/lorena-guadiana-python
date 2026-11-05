# FizzBuzz
# This program prints the numbers from 1 to 30. For multiples of three, it prints "Fizz" instead of the number, 
# and for multiples of five, it prints "Buzz". For numbers which are multiples of both three and five, it prints "FizzBuzz".

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)