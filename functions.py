# functions - allow you to code reusable blocks of code 

def greet():                             #def defines a function
    print("Hello, hi there!")

greet()
greet()
greet()

# Parameters and Arguments

def greet(name):
    print(f"Hello, {name}!")  # parameters are placeholder variables that live inside a function

greet("Alex")   # arguments are the values inside the parentheses that define the parameters
greet("Lele")
greet("Sam")

def greet(name, age):   # you can define multiple parameters in a function
    print(f"Hello, {name}! You are {age} years old.")

greet("Alex", 25)

# return values

def addition(a, b):
    return a + b

print(addition(5, 10))

result = addition(5, 10)   # you can store the return value of a function in a variable
print(result)
print(addition(5, 10) + 100)  # you can also use the return value of a function in an expression

#default parameters - you can give a parameter a default value which will be used if no arguement is given

def greet(name, greeting="Hello"):  # default parameter paraments must come after non-default parameters
    print(f"{greeting}, {name}!")
    
    
greet("Alex", "Hi")
greet("Sam")

# variable scope - variables defined inside a function are local to that function and cannot be accessed outside of it

def calculate():
    resulted = 100
    print(resulted)
"""
calculate()
print(resulted)  # this will throw an error because result is not defined outside of the function
"""
def calculate():
    resulted = 100
    return resulted

output = calculate() # you can return the value of a variable from a function and store it in a variable outside of the functionù

print(output) # this will print 100 because the value of resulted was returned from the function and stored in output