import time
import os

SEARCH_PRICE_REQUEST_FILE = 'search_price_request.txt'
SEARCH_PRICE_RESULT_FILE = 'search_price.txt'
MENU_FILE = 'menu.txt'

def search_boba_by_price():
    if not os.path.exists(SEARCH_PRICE_REQUEST_FILE):
        return

    with open(SEARCH_PRICE_REQUEST_FILE, 'r', encoding='utf-8') as file:
        price_to_search = file.read().strip()

    if not price_to_search:
        return

    try:
        price_to_search = float(price_to_search)
    except ValueError:
        with open(SEARCH_PRICE_RESULT_FILE, 'w', encoding='utf-8') as file:
            file.write(f"Invalid price format: {price_to_search}")
        os.remove(SEARCH_PRICE_REQUEST_FILE)
        return

    print(f"Search request received for price: {price_to_search}")

    results = []
    with open(MENU_FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split()
            if any(float(price) == price_to_search for price in parts[1:]):
                results.append(line.strip())

    with open(SEARCH_PRICE_RESULT_FILE, 'w', encoding='utf-8') as file:
        if results:
            file.write("\n".join(results))
            print(f"Search results written to {SEARCH_PRICE_RESULT_FILE}")
        else:
            file.write(f"No items found with price {price_to_search}.")
            print(f"No items found with price {price_to_search}.")

    os.remove(SEARCH_PRICE_REQUEST_FILE)
    print(f"Search request file {SEARCH_PRICE_REQUEST_FILE} deleted")

while True:
    search_boba_by_price()
    time.sleep(5)
