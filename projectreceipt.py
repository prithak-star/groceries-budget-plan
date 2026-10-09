print("===================================")
print("   HOUSEHOLD GROCERY BUDGET PLANNER")
print("===================================")

budget = float(input("Enter your grocery budget (NPR): "))

print("\nEnter the price and quantity of each item.")

rice_price = float(input("\nPrice of rice per kg (NPR): "))
rice_quantity = float(input("Quantity of rice (kg): "))

oil_price = float(input("\nPrice of cooking oil per litre (NPR): "))
oil_quantity = float(input("Quantity of cooking oil (litres): "))

egg_price = float(input("\nPrice per egg (NPR): "))
egg_quantity = int(input("Number of eggs: "))

vegetable_price = float(input("\nPrice of vegetables per kg (NPR): "))
vegetable_quantity = float(input("Quantity of vegetables (kg): "))

rice_total = rice_price * rice_quantity
oil_total = oil_price * oil_quantity
egg_total = egg_price * egg_quantity
vegetable_total = vegetable_price * vegetable_quantity

total = rice_total + oil_total + egg_total + vegetable_total

print("\n========== SHOPPING RECEIPT ==========")
print("Rice: NPR", round(rice_total, 2))
print("Cooking oil: NPR", round(oil_total, 2))
print("Eggs: NPR", round(egg_total, 2))
print("Vegetables: NPR", round(vegetable_total, 2))
print("--------------------------------------")
print("Total grocery cost: NPR", round(total, 2))
print("Your budget: NPR", round(budget, 2))

if total > budget:
    print("Status: You are a DEAD MEAT SONN.")
    print("Extra amount needed: NPR", round(total - budget, 2))
else:
    print("Status: You are finee congratss.")
    print("Money remaining: NPR", round(budget - total, 2))

print("======================================")
print("just a simple oneee !")