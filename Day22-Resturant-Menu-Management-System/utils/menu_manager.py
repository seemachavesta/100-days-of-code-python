import json

file_name = 'resturant_menu.json'

# Function to load data from the 'menu.json' file   
def load_data():
    try:
        # Try to open and read the JSON file
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('File not found')
        return {}
        
def save_data(menu):
    # Function to save the current menu data to 'menu.json'
    with open(file_name, 'w') as file:
        json.dump(menu, file, indent=4)
    print('Data has been successfully upated')

# Helper function to check if a category exists in the menu       
def has_category(category, menu):
    if category in menu:
        return True
    else:
        print(f'Category {category} does not exist in the menu.')
        return False
        
# Function to add a new item to a specific category in the menu        
def add_item(category_name, item_name, price):
    menu = load_data()
    
    # Check if the category exists in the menu
    if has_category(category_name, menu):
        # Check if the item already exists in the category
        if item_name not in menu[category_name]:
            menu[category_name][item_name] = price
            print(f"Added {item_name} to {category_name} with price ${price:.2f}")
        else:
            print(f"Item {item_name} already exists in {category_name}.")
   
    save_data(menu)
            
# Function to display the entire menu
def menu_display():
    menu = load_data()
    
    print("\n" + "=" * 40)
    print(f"{'Restaurant Menu':^40}")
    print("=" * 40)
    
    for category, items in menu.items():
        print(f"\n===== {category} =====")
        for name, price in items.items():
            print(f"{name:<20} ${price:<10.2f}")
        print("-" * 40)
    print()

# Function to display discounted items (items with a price >= $10)   
def discounted_menu(discount: float = 0.10):
    menu = load_data()
    
    print("\n" + "=" * 40)
    print(f"{'Discounted Menu (Items >= $10)':^40}")
    print("=" * 40)
    
    # Iterate through each category and its items
    for category, items in menu.items():
        # Filter items with a price greater than or equal to 10
        filterd_items = filter(lambda item: item[1] >= 10, items.items())
        
        filterd_items = list(filterd_items)
        # Check if there are any items in the filtered list
        if any(filterd_items):
            print(f"\n===== {category} =====")
            for name, price in filterd_items:
                price = price * (1 - discount)
                print(f"{name:<20} ${price:<10.2f}")
            print("-" * 40)

# Function to delete an item from a specific category in the menu        
def delete_item(category,item_name):
    menu = load_data()
    if has_category(category, menu):
        if item_name in menu[category]:
            del menu[category][item_name]
            print('item has been deleted successfully')
        else:
            print(f'Item {item_name} does not exists in menu category.')
        
    save_data(menu)
   
# Function to update the price of an existing item in a category  
def update_item_price(category, item_name, item_price):
    menu = load_data()
    
    if has_category(category, menu):
        if item_name in menu[category]:
            menu[category][item_name] = item_price
            print(f'Item {item_name} price has been updated successfully.')
        else:
            print(f'Item {item_name} does not exists in menu.')
        
    save_data(menu)

# Function to search for an item in a specific category   
def search_item(category, item_name):
    menu = load_data()
    if has_category(category, menu):
        items = menu[category]
        item = next((item for item in items.items() if item[0] == item_name), None)
        if item:
            print(f"Item '{item_name}' exists in category '{category}' with price ${item[1]:.2f}.")
        else:
            print(f"Item '{item_name}' does not exist in category '{category}'.")
        
    
# Function to place an order with a list of item names   
def place_order(order):
    menu = load_data()
    
    available_items = []
    unavailable_items = []
    total_price = 0.0
    found = False
     # Iterate through each item in the order
    for item in order:
        for items in menu.values():
            if item in items:
                found = True
                available_items.append((item, items[item]))
                total_price += items[item]
        if not found:
            unavailable_items.append(item)
            
    print("\nOrder Summary:")
    if available_items:
        print("\nAvailable Items:")
        for name, price in available_items:
            print(f"{name:<20} ${price:<10.2f}")
        print(f"\nTotal Price: ${total_price:.2f}")
        
    if unavailable_items:
        print("\nUnavailable Items:")
        print(", ".join(unavailable_items))

