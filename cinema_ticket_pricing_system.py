age = int(input(f"How old are you? "))
day_of_the_week = input(f"What day of the week is it? ")
is_member = input("Are you a member? (yes/no) ")
price_reasoning = 0

if age < 3:
    price = 0
    price_reasoning = 0
elif age <=11:
    price = 6
    price_reasoning = price_reasoning + 1
elif age <=17:
    price = 8
    price_reasoning = price_reasoning + 2
elif age <=64:
    price = 12
    price_reasoning = price_reasoning + 3
else:
    price = 8
    price_reasoning = price_reasoning + 4

if day_of_the_week == "Wednesday" and price > 0:
    wednesday_price = 5
    #price_reasoning = price_reasoning * 5 #with final_price=wednesday_price, this is unnecessary
else:
    wednesday_price = price
    price_reasoning = price_reasoning

if is_member == "yes":
    member_price = price * 0.80
    #price_reasoning = price_reasoning * 100 #with final_price=member_price, this is unnecessary
else:
    member_price = price
    price_reasoning = price_reasoning

if price == 0:
    final_price = 0
elif wednesday_price < member_price: #can clean this up using "min(wednesday_price, member_price)"
    final_price = wednesday_price    #can clean this up using "min(wednesday_price, member_price)"
elif wednesday_price > member_price: #can clean this up using "min(wednesday_price, member_price)" 
    final_price = member_price       #can clean this up using "min(wednesday_price, member_price)"
#elif day_of_the_week == "Wednesday":#apply this code if using "min"
    #final_price = wednesday_price
#elif is_member == "yes":
    #final_price = member_price
else:
    final_price = price

print(f"Your ticket price is: €{final_price}.")

if price_reasoning == 0:
    print(f"Reasoning: You are less than 3.")
elif price_reasoning == 1:
    print(f"Reasoning: You are between 3 and 11.")
elif price_reasoning == 2:
    print(f"Reasoning: You are between 12 and 17.")
elif price_reasoning == 3:
    print(f"Reasoning: You are between 18 and 64.")
elif price_reasoning == 4:
    print(f"Reasoning: You have the senior discount.")

if final_price == wednesday_price:
    print(f"Reasoning: You are getting the Wednesday discount.")
elif final_price == member_price:
    print(f"Reasoning: You are getting the member discount.")
"""elif price_reasoning == 5:
    print(f"Reasoning: You are between 3 and 11, and there is the Wednesday discount.")
elif price_reasoning == 10:
    print(f"Reasoning: You are between 12 and 17, and there is the Wednesday discount.")
elif price_reasoning == 15:
    print(f"Reasoning: You are between 18 and 64, and there is the Wednesday discount.")
elif price_reasoning == 20:
    print(f"You are a senior and there is a Wednesday discount.")
elif price_reasoning == 100:
    print(f"Reasoning: You are between 3 and 11 while also being a member.")
elif price_reasoning == 200:
    print(f"Reasoning: You are between 12 and 17 while also being a member.")
elif price_reasoning == 300:
    print(f"Reasoning: You are between 18 and 64 while also being a member.")
else:
    print(f"Reasoning: You have the senior discount while also being a member.")
"""
#Unnecessary and burdensome, good to keep in mind that there are simpler solutions
#Not a massive fan of the current concatenation method. The scenario I have
#suggests that one cannot have both the Wednesday and member discount. It either
#defaults to the Wednesday one if it is less than what someone might get with the membership
#discount or it just applies the membership discount. The original method solved this
#however.
#There was a concatenation method but this current one is better where I made the final_price
#variable reference either discount variable to decide which variable to print.