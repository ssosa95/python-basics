def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def get_result(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a,b)
    elif operation == "*":
        return multiply(a,b)
    elif operation == "/":
        return divide(a,b)
    else:
        return "That is not a valid operation."
    
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Choose the operation you will use (+, -, *, /):  ")

result = get_result(a, b, operation)

print(f"""
------CALC RESULT------
First number: {a}
Second number: {b}
Chosen operation: {operation}
Result: {result}
-----------------------
""") #calc means calculator