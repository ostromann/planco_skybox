#!/usr/bin/env python
# coding: utf-8
import sys
import cv2
import os

import argparse

# Create the parser
my_parser = argparse.ArgumentParser(description='Slice images in folder.')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to folder with images')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path
output_path = input_path+'_sliced'

# create outdir if it doesn't exist yet
if not os.path.exists(output_path):
    os.makedirs(output_path)

nRows = 16 # Number of columns
nCols = 9 # Number of columns

# process images in input_path
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

for file in os.listdir(input_path):
    print(file)
    img_name = file[:-4]
    img = cv2.imread(input_path+'/'+file,1)

    # Dimensions of the image
    sizeX = img.shape[1]
    sizeY = img.shape[0]
    
    for i in range(0,nRows):
        for j in range(0, nCols):
            roi = img[int(i*sizeY/nRows):int(i*sizeY/nRows + sizeY/nRows) ,int(j*sizeX/nCols):int(j*sizeX/nCols + sizeX/nCols)]
            cv2.imwrite(output_path+'/'+img_name+'_'+str(i).zfill(2)+'_'+str(j).zfill(2)+".jpg", roi)