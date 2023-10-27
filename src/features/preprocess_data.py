"""
Module Name: preprocess_data.py

The preprocess_data.py module performs data preprocessing for
image classification by applying various data augmentation
techniques to a selected subset of image folders, saving the
processed images to a new directory.
"""

import os
import shutil
import random
import torchvision.transforms as transforms
from PIL import Image

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'*2))

# Add to root_dir the path to the processed data folder
PROCESSED_DIR = os.path.join(ROOT_DIR, 'data/processed')
RAW_DIR = os.path.join(ROOT_DIR, 'data/raw')

random.seed(42)

# Remove the contents of the output directory if it exists
if os.path.exists(PROCESSED_DIR):
    shutil.rmtree(PROCESSED_DIR)

# Get the list of available folders in data/raw
all_folders = os.listdir(RAW_DIR)

# Select 30 folders
random.shuffle(all_folders)
selected_folders = all_folders[:30]

# Create the directory structure in data/processed
os.makedirs(PROCESSED_DIR)

transform_list = [
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(p=0.2),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), scale=(0.95, 1.05)),
]

# Define transformations
train_transforms = transforms.Compose(transform_list)

# Iterate through the selected folders and copy them to data/processed
for folder in selected_folders:
    src_folder = os.path.join(RAW_DIR, folder)
    dest_folder = os.path.join(PROCESSED_DIR, folder)

    os.makedirs(dest_folder)  # Create the destination directory

    # Iterate through the images in src_folder, apply transformations, and save them to dest_folder
    for filename in os.listdir(src_folder):
        img_path = os.path.join(src_folder, filename)
        img = Image.open(img_path)  # Make sure to import "PIL.Image"
        img = train_transforms(img)  # Apply the transformations
        processed_img_path = os.path.join(dest_folder, filename)
        img.save(processed_img_path)  # Save the processed image to dest_folder

print("Data preprocessing has been completed.")
