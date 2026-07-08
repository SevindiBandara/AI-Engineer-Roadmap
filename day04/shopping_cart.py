items = []
print("Welcome to the Shopping Cart Program!")
print("Enter the items you want to add to your cart. Type 'done' when you're finished.")

while True:
    item = input("Enter an item (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    items.append(item)
    
print("\n===========Shopping Cart===========")
for i in range(len(items)):
    print(f"Item {i +1}: {items[i]}")
    
