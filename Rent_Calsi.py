Room = int(input("Room 🏠 amount: "))
Grocery = int(input("Grocery 🥛🧼🧽 amount: "))
Food = int(input("Food ordered 🍕🍔 amount: "))
Water = int(input("Water 💧 amount: "))
electricity = int(input("Electricity ⚡ amount: "))
charge_per_unit = int(input("Electricity per unit  charge: "))
persons = int(input("Total persons 😁😎 in room: "))

total_bill = electricity * charge_per_unit
calsi_rent = (Room + Grocery + Food + Water + total_bill)
total_amount = calsi_rent // persons

print(calsi_rent,"Each person will pay: 💰💰",total_amount)