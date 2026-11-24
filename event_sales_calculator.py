# JJSpectre
# Event-Sales Calculator
# Coursework project, UNC Charlotte (Fall 2026)

items_sold = int(input("Enter the number of items sold: "))
selling_price = float(input("Enter the selling price per item: $"))
item_cost = float(input("Enter the cost per item: $"))
event_expenses = float(input("Enter any additional event expenses: $"))

revenue = items_sold * selling_price
item_cost_total = items_sold * item_cost
total_expenses = item_cost_total + event_expenses
profit = revenue - total_expenses
profit_margin = (profit / revenue) * 100

print()
print("----- EVENT FINANCIAL SUMMARY -----")
print("Items Sold:", items_sold)
print("Revenue: $", revenue)
print("Item Costs: $", item_cost_total)
print("Additional Expenses: $", event_expenses)
print("Total Expenses: $", total_expenses)
print("Profit: $", profit)
print("Profit Margin:", profit_margin, "%")
print("-----------------------------------")
