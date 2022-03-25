import re
import glob
from PIL import Image
from pathlib import Path
import random
import json 
import os 


# new_result = "/home/azhar/image_generator/new_result"
# output = "/home/azhar/image_generator/output_result"
# photos = glob.glob("/home/azhar/image_generator/out-sample-word/*.jpg")
# background_images = glob.glob("/home/azhar/image_generator/Blank_ids/*.jpg")


import argparse

parser = argparse.ArgumentParser(description='passing folder paths ')
parser.add_argument('background_image_folder_path',help='background image folder path write here')
parser.add_argument('cropped_image_folder_path',help='cropped_image_folder path write here')
parser.add_argument('generated_image_folder_path',help='generated_image_folder result  write here')

args = parser.parse_args()

print(args[0])
print(args[1])
print(args[2])
print(args[3])

id_images = []
crop_images = [] 


for i in background_images :
  id_images.append(i)
for i in photos :
  crop_images.append(i)

print(len(id_images))


for image in id_images : 
    parent_image = Image.open(image)
    p = Path(image)
    p_width, p_height = parent_image.size
    print(f"parent_image_orginal  width : { p_width }{p_height}")
    
    #image placing position which can change every time 
    position_width = 5
    position_height = 5

    for child_image in crop_images:
        c = Path(child_image)
        c_image = Image.open(child_image)
        c_width, c_height = c_image.size

        if (p_width - position_width) > c_width :
              print(p_width,position_width)
              parent_image.paste(c_image,(position_width,position_height))
              position_width = position_width + c_width + 40 
        else :
              print(" Line width Over")
              position_height = position_height + c_height + 100 
              position_width = 0 
              parent_image.paste(c_image,(position_width,position_height))
              position_width = position_width + c_width + 40 
              # parent_image.paste(c_image,(position_width,position_height))
              print (" Printing on next line")
              if position_height > p_height : 
                print("height over")
                break

    parent_image.save(f"{output}/{p.stem}{c.stem}.jpg")
       