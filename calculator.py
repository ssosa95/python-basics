num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Unknown operation."

print(f"Result: {result}")

# you want float for calculators to include precise 
# numbers, integers only give you whole numbers
# perhaps run a loop for number inputs as well in case
# user inputs something invalid
