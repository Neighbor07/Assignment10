import time
import random

image_set = ["milktea", "mango", "strawberry", "watermelon", "matcha"]
IMAGE_REQUEST_FILE = 'get_image.txt'
IMAGE_RESULT_FILE = 'get_image_result.txt'

while True:
    with open(IMAGE_REQUEST_FILE, 'r') as f:
        command = f.read().strip()

    if command == 'get':
        print("Received 'get' command, processing...")
        time.sleep(3) 
        
        rand_num = random.randint(0, 10)
        image_index = rand_num % len(image_set)
        selected_image = image_set[image_index]
        image_path = f'images/{selected_image}.jpg'

        with open(IMAGE_RESULT_FILE, 'w') as f:
            f.write(str(image_path))
        
        # Clear the request
        with open(IMAGE_REQUEST_FILE, 'w') as f:
            f.write('')
        
        print(f"Processed request and generated image path: {image_path}")
    else:
        time.sleep(1)
