# Elian Martinez
# COMP 250-002
# Project 1

# 1. Ask the user to enter the name of a product they want to purchase.
# 2. Ask how many they want to purchase.
# 3. Check whether the product exists in the dictionary.
# 4. If the product exists, check whether there is enough inventory.
# 5. If there is enough inventory, subtract the requested quantity from the inventory and
# display the updated quantity.
# 6. If there is not enough inventory, display an appropriate message without changing the
# inventory.
# 7. If the product does not exist, display an appropriate message.
# 8. After the transaction, display the entire updated inventory.
# 9. Before the program ends, use a loop to examine the inventory and display the names of
# any products that have fewer than 5 items remaining.

inventory = {
    "laptop": 5,
    "mouse": 12,
    "keyboard": 7,
    "headphones": 10
}
user_product = input("Enter the name of the product you want to purchase: ").strip().lower()
product_amount = int(input("How many you want to purchase: "))

if user_product not in inventory: #I am looking for the user input, AND check if it is not in inventory.
    print(f"We don't have {user_product} in the inventory.")
elif product_amount <= inventory[user_product]:
    inventory[user_product] -= product_amount #this one is 
    print(f"Updated quantity: {inventory[user_product]}")
elif product_amount > inventory[user_product]:
    print(f"There is not enough {user_product} in the inventory .")

print(inventory)

for product in inventory:
    if inventory[product] < 5:
        print(f"{product} has less than 5 items remaining.")

