#Comparison operators

a = 10
b = 20

print(a == b) # equal to - False
print(a != b) # does not equal to - True
print(a > b) # greater than - False
print(a < b) # lesser than - True
print(a >= b) # greater than or equal to - False
print(a <= b) # lesser than or equal to - True


#Basic if/else

temperature = 25

if temperature > 30:
    print(f"It is hot outside!")
else:
    print(f"It's not that hot outside.")


#elif for multiple branches

score = 92

if score >= 90:
    print(f"Grade: A")
elif score >= 80:
    print(f"Grade: B")
elif score >= 70:
    print(f"Grade: C")
elif score >= 60:
    print(f"Grade: D") 
else:
    print(f"Grade: F")

#Combining conditions with and/or

age = 25
has_ticket = True

#and - both conditions must be true

if age >= 18 and has_ticket:
    print(f"Permission granted.") #True
else:
    print(f"Permission denied.") #False

#or - at least one is true

is_member = False
has_voucher = True

if is_member or has_voucher:
    print(f"Discount applied.") # statement is true
else:
    print(f"Full price.") # statement is false

#not - flips boolean

is_raining = False


print(not is_raining)
if not is_raining:
    print(f"No need to bring an umbrella.")


