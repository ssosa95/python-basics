name = input("What is your name? ").strip()
age_input = input("What is your age? ").strip()
colour = input("What is your favourite colour? ").strip().lower()
###next_year_age = int(age_input) + 1


try:
    age = int(age_input)
except:
    print("That's not a valid age, defaulting to 0.")
    age = 0

print("Nice to meet you,", name + ".", "You are", age, "years old!", "And your favourite colour is", colour + ".")
print("Next year you will be", age + 1)

if colour == "blue":
    print("Blue is my favourite colour as well!")
else:
    print(colour, "is a great colour too!")

print(f"""
      Hello, {name}!
      You are {age} years old.
      Your favorite colour is {colour}.
"""
)


print("--------USER PROFILE--------")
print("Name:", name)
print("Age:", age)
print("Favourite colour:", colour)
print("----------------------------")

