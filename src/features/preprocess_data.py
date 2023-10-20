"""
Module Name: preprocess_data.py

The preprocess_data.py module performs data preprocessing for image classification by applying various data augmentation techniques to a selected subset of image folders, saving the processed images to a new directory.
"""

import os
import shutil
import torchvision.transforms as transforms
import random

from PIL import Image

random.seed(42)

# Directorios de entrada y salida
input_data_dir = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw"
output_data_dir = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/processed"

# Eliminar el contenido de la carpeta de salida si existe
if os.path.exists(output_data_dir):
    shutil.rmtree(output_data_dir)

# Obtener la lista de carpetas disponibles en data/raw
all_folders = os.listdir(input_data_dir)

# Seleccionar 30 carpetas
random.shuffle(all_folders)
selected_folders = all_folders[:30]

# Crear la estructura de directorios en data/processed
os.makedirs(output_data_dir)

transform_list = [
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(p=0.2),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0), 
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), scale=(0.95, 1.05)),  
]

# Definir transformaciones
train_transforms = transforms.Compose(transform_list)

# Recorrer las carpetas seleccionadas y copiarlas a data/processed
for folder in selected_folders:
    src_folder = os.path.join(input_data_dir, folder)
    dest_folder = os.path.join(output_data_dir, folder)
    
    os.makedirs(dest_folder)  # Crear directorio de destino
    
    # Recorrer las imágenes en src_folder, aplicar transformaciones y guardarlas en dest_folder
    for filename in os.listdir(src_folder):
        img_path = os.path.join(src_folder, filename)
        img = Image.open(img_path)  # Asegúrate de importar "PIL.Image"
        img = train_transforms(img)  # Aplicar las transformaciones
        processed_img_path = os.path.join(dest_folder, filename)
        img.save(processed_img_path)  # Guardar la imagen procesada en dest_folder

print("Data preprocessing has been completed.")
