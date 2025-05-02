# Define the menu of Restaurant
menu = {"Burger":120, "Pizza":200, "Pasta":150, "Coffee":80, "ColdDrinks":50, "Noodles":100}

# # Great
# print("Welcome to Akki Restaurant")
# print("Burger:- Rs120\nPizza:- Rs200\nPasta:- Rs150\nCoffee:- Rs80\nColdDrinks:- Rs50\nNoodles:- Rs100")

# Greeting
print("Welcome to Akki Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}:- Rs{price}")

# Total Pricing
Order_Total = 0

# Item lists
item_1 = input("Your Order Please: ")
if item_1.lower() in menu:
    Order_Total += menu[item_1]
    print(f"Your order {item_1} has been added to your list")

else:
    print(f"Your order {item_1} Not available!")

extra_Order = input("Do you want to add another order to your list? (Yes/No): ")
if extra_Order == "Y".lower():
    item_2 = input("You second order Please: ")
    if item_2 in menu:
        Order_Total += menu[item_2]
        print(f"Your order {item_2} has been added to your list")
    else:
        print(f"Your order {item_1} Not available!")

print(f"Thank You\nYour Total Bill to Pay is: {Order_Total}Rs")