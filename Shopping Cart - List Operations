#8. Shopping Cart - List Operations
(You are creating a shopping cart program. Users should be able to add items to the cart and 
view the final list. Implement a program that allows a user to add items (names of products) until 
they type "done" and then prints all the items in the cart )

cart = []
print("Welcome to the Shopping Cart!")
print("Type the name of the item to add it to the cart. Type 'done' when finished.")

while True:
    item = input("Add item: ")
    if item.lower() == "done":
        break
    cart.append(item)

print("\nYour Shopping Cart contains:")
for index, product in enumerate(cart, start=1):
    print(f"{index}. {product}")

