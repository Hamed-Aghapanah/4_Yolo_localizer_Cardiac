"""   Created on Wed Aug 16 16:19:27 2023

@author       :   Dr Hamed Aghapanah  , PhD bio-electrics

@affiliation  :  Isfahan University of Medical Sciences

"""

import os
import random
import cv2

# Path to the folder containing images
images_folder = "images//Cardiac"
masks_folder = "masks//Cardiac"

# Get a list of image file names in the folder
image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Select 100 random images
random_images = random.sample(image_files, 20)
# Sort the list of image files (optional, for consistent order)
# random_images.sort()
random_images = image_files.sort()
image_files=[]
for i in range(100):
    image_files.append(str(i)+'.png')
random_images=image_files[:100]
# Set the frame width and height
frame_width, frame_height = 800, 600

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
file_name='slideshow_data_base_series.mp4'
output_video = cv2.VideoWriter(file_name, fourcc, 10, (frame_width, frame_height))

logo = cv2.imread('logo.PNG')
logo = cv2.resize(logo, (frame_width, frame_height))
for _ in range(int(0.3 * 50)):  # Each image will appear for 0.3 seconds
    output_video.write(logo)
    
for image_filename in random_images:
    try:
        image_path = os.path.join(images_folder, image_filename)
        mask_path = os.path.join(masks_folder, image_filename)
        image = cv2.imread(image_path)
        mask  = cv2.imread(mask_path)
        if image is not None:
            # Resize the image to match frame dimensions
            image = cv2.resize(image, (frame_width, frame_height))
            # Write the image to the video
            for _ in range(int(0.3 * 10)):  # Each image will appear for 0.3 seconds
                output_video.write(image)
                # image=cv2.rotate(image, 30)
    except:1
for _ in range(int(0.3 * 50)):  # Each image will appear for 0.3 seconds
    output_video.write(logo)
    
# Release the VideoWriter and close the output video file
output_video.release()
os.startfile(file_name)
print("Slideshow video created successfully.")
