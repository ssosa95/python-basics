def display_history(history):
    if len(history) == 0:
        print("There is no history yet.")
    else:
        for i in range(len(history)):
            print(f"{i+1}. {history[i]}")

def add(x, y): #Add two numbers.
    return x + y

def subtract(x, y): #subtract two numbers.
    return x - y

def multiply(x, y): #Multiply two numbers.
    return x * y

def divide(x, y): #Divide two numbers.
    if y == 0:
        return None #Denominator cannot be zero.
    return x / y

def calculate(x, y, operation): #Select two numbers and then perform the selected operation
    if operation == "+":
        return add(x, y)
    elif operation == "-":
        return subtract(x, y)
    elif operation == "*":
        return multiply(x, y)
    elif operation == "/":
        return divide(x, y)
    else:
       return None #Invalid operation
    
def display_result(x, y, operation, result): #Display the result of the calculation
    if result is None and operation == "/":
        print("Error: Division by zero.")
    elif result is None:
        print("Error: Invalid operation.") 
    else:
        print(f"""
-------- CALC RESULT --------              
First number: {x}
Second number: {y}
Chosen operation: {operation}
Result: {result}
-----------------------------
""")


history = []

print("CLI Calculator — type 'quit' to exit")

while True:
    x_input = input("\nFirst number (or 'quit' or 'history'): ")
    
    if x_input == "quit":
        break
    if x_input == "history":
        print("\n--- Session History ---")
        display_history(history)
        continue                #continue skips the rest of the current iteration and goes back to the top of the loop, keeping the calculator running.
    x = float(x_input)
    operation = input("Operation (+, -, *, /): ")
    y = float(input("Second number: "))
    
    result = calculate(x, y, operation)
    display_result(x, y, operation, result)
    if result is not None:
        history.append(f"{x} {operation} {y} = {result}")
    
print("\n--- Session History ---")
display_history(history)
print("Goodbye!")   


