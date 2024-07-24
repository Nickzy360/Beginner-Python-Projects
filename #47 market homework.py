CURRENCY = "USD"

fruits = {
    "Banana": 1.45,
    "Apple": 1.50,
    "Blueberries": 2.00,
    "Avocado": 3.00,
    "Mango": 4.00,
    "Pineapple": 5.00,
    "Dragonfruit": 4.00,
    "Grapes": 3.00,
    "Kiwi": 4.00,
    "Durian": 4.00
}

def menu():
    print("\nAvailable fruits and their prices:")
    for name, price in fruits.items():
        print(f"{name} - {price} {CURRENCY}")

def purchase(fruit_name):
    if fruit_name in fruits:
        print(f"You have bought a {fruit_name} for {fruits[fruit_name]} {CURRENCY}.")
        return fruits[fruit_name]
    else:
        print(f"Sorry, we don't have {fruit_name}.")
        return 0

def add_item(name, price):
    if name in fruits:
        print(f"{name} is already in the inventory.")
    else:
        fruits[name] = price
        print(f"{name} has been added to the inventory at {price} {CURRENCY}.")

def remove_item(name):
    if name in fruits:
        del fruits[name]
        print(f"{name} has been removed from the inventory.")
    else:
        print(f"{name} is not in the inventory.")

def select_capacity(capacity):
    print(f"The store's inventory capacity is set to {capacity} items.")
    return capacity

total_cost = 0

select_capacity(10)  # Call select_capacity with the capacity directly

while True:
    menu()
    user_input = input("What would you like to do? (buy/add/remove/exit)\n").lower()
    if user_input == 'exit':
        print(f"Thank you for visiting our shop. Your total cost is {total_cost} {CURRENCY}. Have a great day!")
        break
    elif user_input == 'buy':
        fruit_name = input("Enter the name of the fruit you want to buy:\n")
        cost = purchase(fruit_name)
        total_cost += cost
        if cost:
            another_purchase = input("Would you like to buy anything else? (yes/no)\n").lower()
            if another_purchase != 'yes':
                print(f"Thank you for your purchase. Your total cost is {total_cost} {CURRENCY}. Have a great day!")
                break
    elif user_input == 'add':
        if len(fruits) < 10:  # Directly use the capacity value
            fruit_name = input("Enter the name of the fruit to add:\n")
            fruit_price = float(input(f"Enter the price of {fruit_name}:\n"))
            add_item(fruit_name, fruit_price)
        else:
            print("Inventory is full. Remove an item before adding a new one.")
    elif user_input == 'remove':
        fruit_name = input("Enter the name of the fruit to remove:\n")
        remove_item(fruit_name)
    else:
        print("Invalid option. Please try again.")
