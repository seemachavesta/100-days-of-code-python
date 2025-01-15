import utils.menu_manager as menu_manager

user_option = """
1. Display Menu
2. Add Item
3. Update Item Price
4. Delete Item
5. View Discounted Menu
6. Search Item
7. Place Order
8. Exit
Enter your choice: """

def prompt_add_item():
    category = input("Enter category: ").strip()
    item_name = input("Enter item name: ").strip()
    try:
        price = float(input("Enter item price: ").strip())
        if price < 0:
            print("Price can't be negative ")
            return 
        menu_manager.add_item(category, item_name, price) 
    except ValueError:
        print("Invalid input. Please enter a numeric value for price.")


def prompt_update_item_price():
    category = input("Enter category: ").strip()
    item_name = input("Enter item name: ").strip()
    try:
        new_price = float(input("Enter new item price: ").strip())
        if new_price < 0:
            print("Price can't be negative ")
            return
        menu_manager.update_item_price(category, item_name, new_price)
    except ValueError:
        print("Invalid input. Please enter a numeric value for price.")


def prompt_search_item():
    category = input("Enter category: ").strip()
    item_name = input("Enter item name: ").strip()
    if category and item_name:
        menu_manager.search_item(category, item_name)
    else:
        print("Please enter valid category and item name. ")
  

def prompt_delete_item():
    category = input("Enter category: ").strip()
    item_name = input("Enter item name: ").strip()
    menu_manager.delete_item(category,item_name)

def prompt_menu_order():
    order = []
    while True:
        item = input('Enter item name: ').strip()
        order.append(item)
        choice = input('Anything else (y/n): ').lower().strip()

        if choice == 'n':
            break
        elif choice != 'y':
            print('Invalid choice. Please enter "y" or "n".')
    
    menu_manager.place_order(order)

  
        
    
def main():
    while True:
        print("\n" + "=" * 40)
        print(f"{'Restaurant Management System':^40}")
        print("=" * 40)
        choice = int(input(user_option))
        print("=" * 40)
        if choice == 1:
            menu_manager.menu_display()
        elif choice == 2:
            prompt_add_item()
        elif choice == 3:
            prompt_update_item_price()
        elif choice == 4:
            prompt_delete_item()
        elif choice == 5:
            menu_manager.discounted_menu()
        elif choice == 6:
            prompt_search_item()
        elif choice == 7:
            prompt_menu_order()
        elif choice == 8:
            confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm == 'y':
                print("Exiting the program. Goodbye!")
                break
            elif confirm == 'n':
                print("Returning to the menu...")
            else:
                print("Invalid input. Returning to the menu...")
            break
        else:
            print('Invalid Choice')


if __name__ == '__main__':
    main()