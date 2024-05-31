import time
import os

SEARCH_REQUEST_FILE = 'search_request.txt'
SEARCH_RESULT_FILE = 'search_result.txt'
MENU_FILE = 'menu.txt'

def search_boba_by_name():
    if not os.path.exists(SEARCH_REQUEST_FILE):
        return

    with open(SEARCH_REQUEST_FILE, 'r', encoding='utf-8') as file:
        item_to_search = file.read().strip()

    if not item_to_search:
        return

    print(f"Search request received: {item_to_search}")

    found = False
    results = []
    with open(MENU_FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if item_to_search.lower() in line.lower():
                results.append(line.strip())
                found = True

    with open(SEARCH_RESULT_FILE, 'w', encoding='utf-8') as file:
        if found:
            file.write("\n".join(results))
            print(f"Search results written to {SEARCH_RESULT_FILE}")
        else:
            file.write(f"No items found with name {item_to_search}.")
            print(f"No items found with name {item_to_search}.")

    os.remove(SEARCH_REQUEST_FILE)
    print(f"Search request file {SEARCH_REQUEST_FILE} deleted")

while True:
    search_boba_by_name()
    time.sleep(5)
