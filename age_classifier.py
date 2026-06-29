try:    
    age = int(input(f"Enter your age: ")) # you want an integer, not a float because ages are whole numbers
except ValueError:
    print("That is not a valid age.")
if age < 0:
    print(f"That is not a valid age!")   #nested everything in an else statement afterwards so the program doesn't tell me it is invalid but also gives me the other statements about voting and pension eligibility
else:    
    if age < 13:
        print(f"You are a child.")
    elif age < 18:
        print(f"You are a teen.")
    elif age < 26:
        print(f"You are a young adult.")
    elif age < 60:
        print(f"You are an adult.")
    else:
        print(f"You are elderly.")
    
    if age >= 18:
        print(f"You are eligible to vote.")
    else:
        print(f"You are not yet eligible to vote.")

    if age >= 65:
        print(f"You may be eligible for a pension.")
    else:
        print(f"You are not yet eligible for a pension.")