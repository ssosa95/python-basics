#build the task: store and print a list

items = []

for i in range(5):
    item = input(f"Enter item {i + 1}: ")
    items.append(item)
print("\nYou entered:")
for i in range(len(items)):
    print(f"{i+1}. {items[len(items)-(i+1)]}") #better to use negative indexing, {items[-(i+1)]}

print(f"\nTotal items: {len(items)}")