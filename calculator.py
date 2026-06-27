num1 = float(input("Enter the first number: ")) #crashes on letter input, need to add error handling for invalid input
num2 = float(input("Enter the second number: ")) #crashes on letter input, need to add error handling for invalid input

operation = input("Choose operation (+, -, *, /): ") #stop program entirely if user inputs something other than the four operations, or add error handling to ask for input again

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
