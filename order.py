import time
import os

ORDER_FILE = 'order.txt'
PROCESSED_ORDER_FILE = 'processed_order.txt'

def process_order():
    if not os.path.exists(ORDER_FILE):
        return

    with open(ORDER_FILE, 'r', encoding='utf-8') as file:
        order_data = file.read().strip()

    if not order_data:
        return

    print(f"Order received: {order_data}")

    with open(PROCESSED_ORDER_FILE, 'w', encoding='utf-8') as file:
        file.write("Order placed successfully.")
    time.sleep(5)
    os.remove(ORDER_FILE)
    print(f"Order file {ORDER_FILE} deleted")

while True:
    process_order()
    time.sleep(5)
