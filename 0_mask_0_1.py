"""   Created on Wed Aug 16 01:21:45 2023

@author       :   Dr Hamed Aghapanah  , PhD bio-electrics

@affiliation  :  Isfahan University of Medical Sciences

"""
# convert all mask 0 1 2 3 ==>0 1 
import os
import cv2
import matplotlib.pyplot as plt

# Path to the folder containing image files
image_folder = 'masks//Cardiac'

# List all image files in the folder
image_files = [file for file in os.listdir(image_folder) if file.endswith('.png')]  # Adjust the extension as needed

# Iterate through each image file, read, binarize, and save
cnt=0
for image_file in image_files:
    # Read the image using OpenCV
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale image

    # Binarize the image using a threshold value (adjust threshold as needed)
    threshold_value = 1
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Save the binarized image using the original filename with a new prefix
    new_image_file = image_file
    new_image_path = os.path.join(image_folder, new_image_file)
    cv2.imwrite(new_image_path, binary_image)
    import numpy as np
    
    if np.sum(binary_image)==0:
        cnt=cnt+1
        print(cnt)
        image_folder_image = 'images//Cardiac//'+image_file
        try:os.remove(image_folder_image)
        except:1
        os.remove(new_image_path)
        

        


print("Binarization and saving complete.")

