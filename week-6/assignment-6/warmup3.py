# Short Example 1: A variable defined inside a function can't be used outside it

def make_message():
    message = "Hello from inside the function!"

make_message()

# This line causes an error, so it is commented out:
# print(message)

# The error it produced was:
# NameError: name 'message' is not defined


# Short Example 2: Using return to fix the problem

def make_message_with_return():
    message = "Hello from inside the function!"
    return message

result = make_message_with_return()
print(result)