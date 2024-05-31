import os
import time

ORDER_FILE = 'order.txt'
PROCESSED_ORDER_FILE = 'processed_order.txt'
MENU_FILE = 'menu.txt'
SEARCH_NAME_REQUEST_FILE = 'search_request.txt'
SEARCH_NAME_RESULT_FILE = 'search_result.txt'
SEARCH_PRICE_REQUEST_FILE = 'search_price_request.txt'
SEARCH_PRICE_RESULT_FILE = 'search_price.txt'
IMAGE_REQUEST_FILE = 'get_image.txt'
IMAGE_RESULT_FILE = 'get_image_result.txt'
IMAGE_GENERATION_TIMEOUT = 30  # seconds

def view_shop_info():
    print("Welcome to managing Bobalicious")
    print("Enter a number from 1-9.")
    print("We offer a variety of boba drinks. Please check our menu for details.")
    print("NEW FEATURE: Place an order to test what the customer experiences!\n")

def add_item_to_menu(filename):
    item = input("Enter the item name: ")
    small_price = input("Enter the small size price: ")
    medium_price = input("Enter the medium size price: ")
    large_price = input("Enter the large size price: ")
    with open(filename, 'a') as file:
        file.write(f"{item} {small_price} {medium_price} {large_price}\n")
    print(f"Item {item} added to the menu.")

def remove_item_from_menu(filename):
    item_to_remove = input("Enter the item name to remove: ")
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if not line.startswith(item_to_remove):
                file.write(line)
    print(f"Item {item_to_remove} removed from the menu.")

def search_by_boba_name():
    item_to_search = input("Enter the boba name to search: ")

    with open(SEARCH_NAME_REQUEST_FILE, 'w', encoding='utf-8') as file:
        file.write(item_to_search)
    
    print("Searching for boba name...")

    while not os.path.exists(SEARCH_NAME_RESULT_FILE):
        time.sleep(1)

    with open(SEARCH_NAME_RESULT_FILE, 'r', encoding='utf-8') as file:
        print(file.read().strip())

def search_by_price():
    price_to_search = input("Enter the price to search: ")

    with open(SEARCH_PRICE_REQUEST_FILE, 'w', encoding='utf-8') as file:
        file.write(price_to_search)
    
    print("Searching for boba by price...")

    while not os.path.exists(SEARCH_PRICE_RESULT_FILE):
        time.sleep(1)

    with open(SEARCH_PRICE_RESULT_FILE, 'r', encoding='utf-8') as file:
        print(file.read().strip())

def place_an_order():
    item_name = input("Enter the item name to order: ")
    size = input("Enter the size (s, m, l): ")
    quantity = int(input("Enter the quantity: "))

    order_data = f"boba name= {item_name} size of drink= {size} quantity= {quantity}"

    with open(ORDER_FILE, 'w', encoding='utf-8') as file:
        file.write(order_data)
    
    print("Order is being processed...")

    while not os.path.exists(PROCESSED_ORDER_FILE):
        time.sleep(1)

    with open(PROCESSED_ORDER_FILE, 'r', encoding='utf-8') as file:
        print(file.read().strip())
    
    os.remove(PROCESSED_ORDER_FILE)

def generate_image():
    with open(IMAGE_REQUEST_FILE, 'w') as file:
        file.write('get')

    print("Generating image...")

    start_time = time.time()
    while not os.path.exists(IMAGE_RESULT_FILE):
        if time.time() - start_time > IMAGE_GENERATION_TIMEOUT:
            print("Error: Image generation timed out.")
            return
        time.sleep(1)

    with open(IMAGE_RESULT_FILE, 'r') as file:
        image_path = file.read().strip()

    print(f"Generated Image Path: {image_path}")
    
    os.remove(IMAGE_RESULT_FILE)

def about_shop():
    print("This program was made by Benjamin Li. A student at Oregon State University who is taking CS 361 in his Spring 2024 term. The purpose of this project is to create a boba shop so another student can use it.")

def log_out():
    print("Logged out successfully.")
    exit()

def main():
    while True:
        print("What would you like to do: ")
        print("  1. View shop info ")
        print("  2. Add an item to menu ")
        print("  3. Remove an item from menu ")
        print("  4. Search by boba name ")
        print("  5. Search by price ")
        print("  6. Place an order ")
        print("  7. Generate Image ")
        print("  8. About Shop ")
        print("  9. Log out ")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_shop_info()
        elif choice == '2':
            add_item_to_menu(MENU_FILE)
        elif choice == '3':
            remove_item_from_menu(MENU_FILE)
        elif choice == '4':
            search_by_boba_name()
        elif choice == '5':
            search_by_price()
        elif choice == '6':
            place_an_order()
        elif choice == '7':
            generate_image()
        elif choice == '8':
            about_shop()
        elif choice == '9':
            log_out()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
