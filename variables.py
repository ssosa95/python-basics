name = "Samuel" 
age = 30 
height = 1.73
is_learning = True

print(name)
print(age)
print(height)
print(is_learning)

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_learning)) # <class 'bool'>

a = 20
b = 6

print (a + b) #addition - 26
print (a - b) #subtraction - 14 
print (a * b) #multiplication - 120 
print (a / b) #divison (always returns a float) - 3.333333
print (a // b) #floor division (drops the decimal) - 3
print (a % b) #modulus (the remainder after division -> 20/6 -> 18/6 is 3, 2 is left over)
print (a ** b) #exponent 20^6

first_name = "Paolo"
last_name = "Maldini"

#Concatenation and f-strings

full_name = first_name + " " + last_name
print(full_name)

greeting = f"""Hello, {first_name}! Your full name is {full_name}."""
print(greeting)

age = 52
print(f"In 10 years you will be {age + 10}.")

#inputs 

name = input("What is your name? ")
print(f"Hello, {name}!")

#input always returns a string so convert integers back to integers
age_text = input("What is your age? ")
age = int(age_text)
print(f"Next year you will be {age + 1}!")