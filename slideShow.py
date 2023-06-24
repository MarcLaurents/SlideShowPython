import os
import time
import cv2

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

def display_slide(photo):
    # Display the photo in the same window
    image = cv2.imread(photo)
    resized_image = cv2.resize(image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    window_name = "Slideshow"
    cv2.imshow(window_name, resized_image)
    cv2.waitKey(5000)  # Displaying each photo for 5 seconds

def run_slideshow():
    pictures_dir = "pictures"  # Directory where your photos are stored

    cv2.namedWindow("Slideshow", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Slideshow", WINDOW_WIDTH, WINDOW_HEIGHT)

    photo_files = [file_name for file_name in os.listdir(pictures_dir) if os.path.isfile(os.path.join(pictures_dir, file_name))]
    num_photos = len(photo_files)
    current_photo_index = 0

    while True:
        photo_path = os.path.join(pictures_dir, photo_files[current_photo_index])
        display_slide(photo_path)
        current_photo_index = (current_photo_index + 1) % num_photos
        time.sleep(1)  # Transition time of 1 second between photos

        if cv2.waitKey(1) == 27:  # Wait for ESC key to be pressed
            break

    cv2.destroyAllWindows()

run_slideshow()
