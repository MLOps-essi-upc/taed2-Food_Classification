import os
import ast
import shutil
import urllib
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import mlflow
import mlflow.pytorch
import dagshub
import great_expectations as gx
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.models as models
import torchvision.datasets as s
import torchvision.transforms as transforms
import matplotlib
import matplotlib.pyplot as plt

from torchvision import transforms
from torch.utils.data import Dataset, DataLoader, ConcatDataset
from torchvision.io import read_image
from torchvision.transforms.functional import to_pil_image
from great_expectations.dataset import PandasDataset
from tqdm import tqdm
from typing import Tuple, Dict, Any, List
from PIL import Image
from typing import Tuple, List
from matplotlib.pyplot import imshow


class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = annotations_file
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self): # returns the number of samples in our dataset.
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        """if len(img_path)< 6:
            print(img_path)"""
            
        image = read_image(img_path)

        to_pil = transforms.ToPILImage()
        image = to_pil(image)
        
        width, height = image.size
        
        if width < 224 or height < 224:
            scale_factor = 512 / max(width, height)
    
        # calculate the new dimensions
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)

            image = image.resize((new_height, new_width))
        
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        
        return image, label
    
train_transforms = transforms.Compose([transforms.ToTensor()])

## read the folders and load them in a specific class structure
first = False
first_first = True

# transform the target 'words' into numerical values, this dictionary will associate these two values
dictionary = {} 
idx = 0

for dirname, _, filenames in os.walk('/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/processed'):

    if first == True:
        label = dirname[len('/kaggle/input/data-food/external/'):]
        columns = ['file', 'label']
        target = pd.DataFrame(columns=columns)
        
        for filename in filenames:
            target.loc[len(target)] = [filename, idx]
        
        dictionary[idx] =  label
        sub_dataset = CustomImageDataset(target, dirname, transform = train_transforms)
        
        if first_first == True:
            train_data = sub_dataset
            first_first = False
        else:
            train_data = ConcatDataset([train_data, sub_dataset])
        
        idx = idx + 1
        
    first = True     

# split into training and validation set
train_percentage = 0.7
val_percentage = 0.3

total_length = len(train_data)

train_size = int(train_percentage * total_length)
val_size = total_length - train_size

train_subset, val_subset = torch.utils.data.random_split(train_data, [train_size, val_size], generator=torch.Generator().manual_seed(7767))


# Initialize an empty DataFrame.
df = pd.DataFrame(columns=['size_dim1', 'size_dim2', 'size_dim3', 'min_colour_range', 'max_colour_range', 'type_torch.float32'])  

# Iterate through all tensors (images) in train_data and add size and range to the DataFrame
for i in tqdm(range(len(train_data)), desc="Processing"): 
    size = list(map(float, train_data[i][0].size()))  # Convert size to a list of floats.
    
    # Dynamic range of the colours in the image.
    min_colour_range = float(torch.min(train_data[i][0]))
    max_colour_range = float(torch.max(train_data[i][0]))

    data_type = train_data[i][0].dtype
    
    data_type = train_data[i][0].dtype
    all_elements_float32 = (data_type == torch.float32)  # Check if all elements are of type torch.float32 

    df = pd.concat([df, pd.DataFrame({'size_dim1': [size[0]], 'size_dim2': [size[1]], 'size_dim3': [size[2]], 'min_colour_range': [min_colour_range], 'max_colour_range': [max_colour_range], 'type_torch.float32': [all_elements_float32]})], ignore_index=True)

# get the index of the rows with size_dim1 = 1
indexNames = df[df['size_dim1'] == 1].index
# delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)

df.to_csv('/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/processed/x_data_information.csv', index=False)

# Initialize an empty DataFrame.
y_df = pd.DataFrame(columns=['label_id'])  

# Iterate through all tensors (images) in train_data and add size and range to the DataFrame
for i in tqdm(range(len(train_data)), desc="Processing"): 
    label_id = train_data[i][1]

    y_df = pd.concat([y_df, pd.DataFrame({'label_id': [label_id]})], ignore_index=True)

# delete these row indexes from dataFrame
y_df.drop(indexNames , inplace=True)

y_df.to_csv('/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/processed/y_data_information.csv', index=False)