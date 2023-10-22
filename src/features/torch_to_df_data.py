"""
Module Name: torch_to_df_data.py

The torch_to_df_data.py module loads, preprocesses, and extracts information
from a dataset of food images, saving relevant data to DataFrames for analysis.
"""

import os
import pandas as pd
import torch
import torchvision.transforms as transforms
from torch.utils.data import Dataset, ConcatDataset
from torchvision.io import read_image
from tqdm import tqdm

class CustomImageDataset(Dataset):
    """
    Custom dataset for loading and transforming food image data.
    """
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = annotations_file
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self): # Returns the number of samples in our dataset.
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])

        image = read_image(img_path)

        to_pil = transforms.ToPILImage()
        image = to_pil(image)

        width, height = image.size

        if width < 224 or height < 224:
            scale_factor = 512 / max(width, height)

            # Calculate the new dimensions
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)

            image = image.resize((new_height, new_width))

        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)

        return image, label
    
OUTPUT_DIRECTORY = '/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/features'
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

train_transforms = transforms.Compose([transforms.ToTensor()])

# Read the folders and load them in a specific class structure

FIRST = False
FIRST_FIRST = True

# Transform the target 'words' into numerical values,
# this dictionary will associate these two values
dictionary = {}
IDX = 0

for dirname, _, filenames in os.walk(
    '/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/processed'
    ):
    if FIRST is True:
        LABEL = dirname[len('/kaggle/input/data-food/external/'):]
        columns = ['file', 'label']
        target = pd.DataFrame(columns=columns)
        for filename in filenames:
            target.loc[len(target)] = [filename, IDX]
        dictionary[IDX] =  LABEL
        sub_dataset = CustomImageDataset(target, dirname, transform = train_transforms)

        if FIRST_FIRST is True:
            train_data = sub_dataset
            FIRST_FIRST = False
        else:
            train_data = ConcatDataset([train_data, sub_dataset])
        IDX = IDX + 1
    FIRST = True

# Split into training and validation set
TRAIN_PERCENTAGE = 0.7
VAL_PERCENTAGE = 0.3

total_length = len(train_data)

train_size = int(TRAIN_PERCENTAGE * total_length)
val_size = total_length - train_size

train_subset, val_subset = torch.utils.data.random_split(
    train_data, [train_size, val_size], generator=torch.Generator().manual_seed(7767)
    )


# Initialize an empty DataFrame.
df = pd.DataFrame(
    columns=['size_dim1', 'size_dim2', 'size_dim3', 'min_colour_range',
             'max_colour_range', 'type_torch.float32']
    )

# Iterate through all tensors (images) in train_data and add size and range to the DataFrame
for i in tqdm(range(len(train_data)), desc="Processing"):
    size = list(map(float, train_data[i][0].size()))  # Convert size to a list of floats.

    # Dynamic range of the colours in the image.
    min_colour_range = float(torch.min(train_data[i][0]))
    max_colour_range = float(torch.max(train_data[i][0]))

    data_type = train_data[i][0].dtype

    data_type = train_data[i][0].dtype
    # Check if all elements are of type torch.float32
    all_elements_float32 = (data_type == torch.float32)

    df = pd.concat(
        [df, pd.DataFrame({'size_dim1': [size[0]], 'size_dim2': [size[1]],
                           'size_dim3': [size[2]], 'min_colour_range': [min_colour_range],
                           'max_colour_range': [max_colour_range],
                           'type_torch.float32': [all_elements_float32]})],
                           ignore_index=True
                           )

# Get the index of the rows with size_dim1 = 1
indexNames = df[df['size_dim1'] == 1].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)

df.to_csv(
    '/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/features/x_data_information.csv',
    index=False
    )

# Initialize an empty DataFrame.
y_df = pd.DataFrame(columns=['label_id'])

# Iterate through all tensors (images) in train_data and add size and range to the DataFrame
for i in tqdm(range(len(train_data)), desc="Processing"):
    label_id = train_data[i][1]

    y_df = pd.concat([y_df, pd.DataFrame({'label_id': [label_id]})], ignore_index=True)

# Delete these row indexes from dataFrame
y_df.drop(indexNames , inplace=True)

y_df.to_csv(
    '/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/features/y_data_information.csv',
    index=False
    )
