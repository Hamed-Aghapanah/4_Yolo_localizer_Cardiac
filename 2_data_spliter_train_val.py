"""   Created on Sat Jun 24 08:45:24 2023

@author       :   Dr Hamed Aghapanah  , PhD bio-electrics

@affiliation  :  Isfahan University of Medical Sciences

"""
import shutil
import os
import numpy as np


path = os.getcwd()
# image_paths = r"F:\project\Tehran\2PROGNOSMART\mfiles\000_Tongueclass1_dataset\image"
# mask_paths = r"F:\project\Tehran\2PROGNOSMART\mfiles\000_Tongueclass1_dataset\mask"
image_paths = r"F:\0001phd\00_thesis\0_mfiles\YOLO\Yolo_localizer_Cardiac\images"
mask_paths = r"F:\0001phd\00_thesis\0_mfiles\YOLO\Yolo_localizer_Cardiac\masks"


val_percent = 0.1
image_path_all =[]
image_path_all_train=[]
image_path_all_val=[]

mask_path_all =[]
mask_path_all_train=[]
mask_path_all_val=[]

lable =[]
f1 =os.listdir(image_paths)
f2 = os.listdir(mask_paths)
L=0

# try:shutil.rmtree('yolo_dataset')
# except:s=1

try:os.mkdir('yolo_dataset')
except:s=1


try:os.mkdir('yolo_dataset/images')
except:s=1
try:os.mkdir('yolo_dataset/images/train')
except:s=1
try:os.mkdir('yolo_dataset/images/val')
except:s=1

try:os.mkdir('yolo_dataset/labels')
except:s=1
try:os.mkdir('yolo_dataset/labels/train')
except:s=1
try:os.mkdir('yolo_dataset/labels/val')
except:s=1


for i in f1:
    L=L+1
    image_path_1=os.listdir(image_paths+'\\'+i)
    L =np.int16 (len (image_path_1) *val_percent)
    R = np.random.permutation(len (image_path_1))
    s=1
    for j in range(len (image_path_1)):
        if s==1:
            print( i, f1 , j,'/' , len (image_path_1))
            s=1
        im_p   = image_paths+'\\'+i+'\\'+image_path_1[j]
        lable_p   = 'txt\\'+image_path_1[j].split(".")[0] +'.txt'
        if R[j]>L:        ### copy in Train
            target='yolo_dataset/images/train/'+image_path_1[j]
            shutil.copyfile(im_p, target)
            
            target='yolo_dataset/labels/train/'+image_path_1[j].split(".")[0] +'.txt'
            shutil.copyfile(lable_p, target)
            
        else:             ### copy in Val
            target='yolo_dataset/images/val/'+image_path_1[j]
            shutil.copyfile(im_p, target)
            target='yolo_dataset/labels/val/'+image_path_1[j].split(".")[0] +'.txt'
            shutil.copyfile(lable_p, target)
        
    
counter=-1
for mask_path in mask_path_all:
    counter=counter+1
    
    
    
    
    