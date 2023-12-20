"""   Created on Wed Aug 16 16:19:27 2023

@author       :   Dr Hamed Aghapanah  , PhD bio-electrics

@affiliation  :  Isfahan University of Medical Sciences

"""

import os
import cv2

images_folder1 = os.getcwd()+"\\1_DATA_Rajaii\\images";
image_files_local = [f for f in os.listdir(images_folder1) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

image_files_local=image_files_local[:20]

images_folder2 = os.getcwd()+"\\1_DATA_ACDC2017\\images";
image_files_acdc=[]
for i in range(20):
    image_files_acdc.append(str(i+1)+'.png')

images_folder3 = os.getcwd()+"\\1_MnM2\\images";
image_files_MM = [f for f in os.listdir(images_folder3) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
image_files_MM=image_files_MM[:20]




# Set the frame width and height
frame_width, frame_height = 800, 600

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
file_name='all_datasets.mp4'
output_video = cv2.VideoWriter(file_name, fourcc, 10, (frame_width, frame_height))

logo = cv2.imread('logo.PNG')
logo_mm= cv2.imread('1_MnM2.PNG')
logo_rajaii= cv2.imread('1_DATA_Rajaii.PNG')
logo_acdc= cv2.imread('1_DATA_ACDC2017.PNG')

logo_mm = cv2.resize(logo_mm, (frame_width, frame_height))
logo_rajaii = cv2.resize(logo_rajaii, (frame_width, frame_height))
logo = cv2.resize(logo, (frame_width, frame_height))
logo_acdc = cv2.resize(logo_acdc, (frame_width, frame_height))
logo000=0*logo

for _ in range(int(0.3 * 50)):  # Each image will appear for 0.3 seconds
    output_video.write(logo)
for _ in range(int(0.3 * 10)):  # Each image will appear for 0.3 seconds
    output_video.write(logo000)
for _ in range(int(0.3 * 50)):  # Each image will appear for 0.3 seconds
    output_video.write(logo_rajaii)
    

for image_filename in image_files_local:
    image_path = os.path.join(images_folder1, image_filename)
    image = cv2.imread(image_path)
    if image is not None:
        image = cv2.resize(image, (frame_width, frame_height))
        text_color = (0, 255, 255);   text_position = (30, 30)   
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5;     font_thickness = 1
        image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = cv2.putText(image_bgr, image_filename[:-4], text_position, font, font_scale, text_color, font_thickness)



        for _ in range(int(0.3 * 10)):  # Each image will appear for 0.3 seconds
            output_video.write(image)




for _ in range(int(0.3 * 10)):  # Each image will appear for 0.3 seconds
    output_video.write(logo000)
for _ in range(int(0.3 * 50)):  # Each image will appear for 0.3 seconds
    output_video.write(logo_acdc)

for image_filename in image_files_acdc:
    image_path = os.path.join(images_folder2, image_filename)
    image = cv2.imread(image_path)
    if image is not None:
        image = cv2.resize(image, (frame_width, frame_height))
        text_color = (0, 255, 255);   text_position = (30, 30)   
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5;     font_thickness = 1
        image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = cv2.putText(image_bgr, image_filename[:-4], text_position, font, font_scale, text_color, font_thickness)

        for _ in range(int(0.3 * 10)):  # Each image will appear for 0.3 seconds
            output_video.write(image)





for _ in range(int(0.3 * 10)):  # Each image will appear for 0.3 seconds
    output_video.write(logo000)
for _ in range(int(0.3 * 50)):  # Each image will appear for 0.3 seconds
    output_video.write(logo_mm)

for image_filename in image_files_MM:
    image_path = os.path.join(images_folder3, image_filename)
    image = cv2.imread(image_path)
    if image is not None:
        image = cv2.resize(image, (frame_width, frame_height))
        text_color = (0, 255, 255);   text_position = (30, 30)   
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5;     font_thickness = 1
        image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = cv2.putText(image_bgr, image_filename[:-4], text_position, font, font_scale, text_color, font_thickness)

        for _ in range(int(0.3 * 10)):  # Each image will appear for 0.3 seconds
            output_video.write(image)
    
    
    
for _ in range(int(0.3 * 50)):  # Each image will appear for 0.3 seconds
    output_video.write(logo)
    
output_video.release()
os.startfile(file_name)
print("Slideshow video created successfully.")
