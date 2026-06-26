#creating a list

item1 = "apples"
item2 = "peaches"
item3 = "pineapples"

shopping_list = [item1, item2, item3]
print(shopping_list)

#lists can have mixed data types

mixed_data = ["Samuel", 30, 1.73, True]
print(mixed_data)

#accessing items, lists start at 0, so to access the first item, you must call "0"

fruits = ["apples", "bananas", "pears", "peaches", "plums"]
print(fruits[0]) #apples
print(fruits[1]) #bananas
print(fruits[-1]) #negative numbers wrap all the way back around - plums
print(fruits[-2]) #peaches

#you are able to grab a portion of the list using ":"
print(fruits[0:2]) # should print from apples to bananas, does not include 2
print(fruits[1:]) # should print everything but the first item, apples
print(fruits[:4]) # should print everything except plums


#modifying lists

fruits = ["apples", "bananas", "pears"]
fruits.append("grapes") #adds default to the end of a list
print(fruits)

fruits.insert(1, "mango") #inserts "mango" at slot 2, so it should come after apples now
print(fruits)

fruits.remove("bananas") # can choose the item to remove
print(fruits)

popped = fruits.pop() #fruits.pop() removes the last item, we stored it in "popped"
print(popped) #prints what was popped
print(fruits) #prints the list without the removed item

print(len(fruits)) #prints the length of the list, i.e how many items there are

#the "for" loop

fruits = ["apples", "bananas", "pears", "peaches", "plums"]

for fruit in fruits:
    print(fruit)

prices = [1.20, 2.00, 0.75, 3.20]
total = 0

for price in prices:
    total = total + price
print(f"Your total is: {total}")

#ranges, when you don't want to loop infinitely and just want to do something a set amount of times

for i in range(3):
    print(i)  #prints 0, 1, 2

#range can also take a start, a stop, and a step, in that order

for i in range(1, 6): 
    print(i) # prints from 1 to 5

for i in range (1, 10, 2): 
    print(i) #prints from 1 and skips 2 each time

#combining len() and range() allows you to know the position of each item in a list
#looping through a list by index

fruits = ["apples", "bananas", "pears", "peaches", "plums"]

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

#while loops
#a while loop keeps running as long as the condition is true

count = 0

while count < 5:
    count = count + 1
    print(f"Count is: {count}")
print("Done.")

#The key difference from a for loop: for loops over a known sequence, 
# while runs until a condition changes. 
# Be careful: if the condition never becomes False, you get an infinite loop. 
# Ctrl+C in the terminal stops a runaway script.

# a common practical use of a while loop is to keep it running until the user wants to quit

running = True

while running:
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input == "no":
        running = False
print("Goodbye.")


# break and continue - they give finer control within loops

for i in range(10):
    if i == 5:
        break #exits loop immediately
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i) #prints only odd numbers in this case

