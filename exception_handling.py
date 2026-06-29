# exception - When Python encounters something it can't handle, it raises an exception and stops.

# Examples:
# int("hello")     # ValueError
# 10 / 0           # ZeroDivisionError
#open("missing")  # FileNotFoundError

# try/except - You can handle exceptions using a try/except block. 
# The code inside the try block is executed, 
# and if an exception occurs, the code inside the except block 
# is executed instead of stopping the program.

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except:  #broad except, it is better to create more specific exceptions where possible
    print("That wasn't a valid number.")

try:
    number = int(input("Enter a number: "))
    result = 100 / number 
    print(f"100 divided by {number} is {result}.")
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

#Common types of exceptions:

# ValueError - Wrong type of value — int("hello")
# ZeroDivisionError - Dividing by zero
# FileNotFoundError - Opening a file that doesn't exist
# IndexError - Accessing a list index that doesn't exist
# TypeError - Wrong type for an operation — "hello" + 5
# KeyError - Accessing a dictionary key that doesn't exist (Day 11)

# else and finally

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That is not a valid number.")
else:
    print(f"Success! You entered: {number}") # only runs if no exception occurred 
finally:
    print("This always runs, exception or not.") # cleanup code goes here

# else runs only when the try block succeeds with no exceptions. 
# finally always runs regardless — useful for cleanup like closing files or database connections 
# even when something goes wrong.

# Getting the Error Message

try: 
    number = int(input("Enter a number: "))
except ValueError as e:
    print(f"Your error is {e}.") # "a" - Your error is invalid literal for int() with base 10: 'a'.

# as e captures the exception object. 
# Printing it gives you Python's own description of what went wrong, which is useful for logging.

# Loops and Exception Handling

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0: 
            print("That is an invalid age.")
        else:
            break
    except ValueError:
        print("That is not a valid input.")

print(f"Your age is: {age}.")


# Handling missing files

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        return None

content = read_file('missing.txt')
if content is not None:
    print(content)

# Raising Your Own Exceptions

def set_storage_threshold(value):
    if value < 0 or value > 100:
        raise ValueError(f"{value} is not a valid threshold. Must be between 0 and 100.")
    return value

try:
    threshold = set_storage_threshold(150) # not valid
except ValueError as e:
    print(f"Configuration error: {e}")

# raise lets your functions signal that something is wrong in the same way 
# Python's built-in functions do. 
# You'll use this more once you're building larger systems.

