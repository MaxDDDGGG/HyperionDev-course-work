# Prepare menu as a list and stock and price as dictionaries
menu = ['Breakfast', 'Second Breakfast', 'Elevenses', 'Lunch']
stock = {'Breakfast': 5, 'Second Breakfast': 5, 'Elevenses': 11, 'Lunch': 13}
price = {'Breakfast': 10, 'Second Breakfast': 15, 'Elevenses': 11, 'Lunch': 16}

#start a counter for total stock
total_stock = 0  

# add the item name and then item cost by multiplying the price and item cost together
# Add the item cost to the total stock counter on each loop
for item in menu:
    item_cost = stock[item] * price[item]
    print(f"{item}: {item_cost}")
    total_stock += item_cost
    
# print the total stock with a space between it and the list of stock items and prices
print(f"\nTotal Stock: {total_stock}")