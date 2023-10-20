"""
Module Name: evaluate.py

The evaluate.py module is used to test a pre-trained image classification model on a set of test images, calculate accuracy, and compare the predicted labels with the ground truth labels.
"""

import os
import torch
from PIL import Image
import torchvision.models as models
import pandas as pd
from predict_model import predict_image


#root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'*2))
#data_dir = os.path.join(root_dir, 'data/processed')

# set the working directory
os.chdir("/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification")

# Cargar el modelo previamente entrenado
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("models/RESNET34", map_location=torch.device('cpu')))
resnet34.eval()

# Directorio de prueba
test_data_dir = '/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/test/food_test_1'

clases_df = pd.read_csv("/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/models/Output-Food-Dictionary.csv")

# Inicializar la cantidad total de imágenes y el contador de predicciones correctas
total_images = 0
correct_predictions = 0

# Recorre las imágenes en el directorio de prueba y realiza predicciones
for filename in os.listdir(test_data_dir):
    image_path = os.path.join(test_data_dir, filename)
    image = Image.open(image_path).convert('RGB')
    prob, target = predict_image(image, model=resnet34, topk=1)
        
    # Supongamos que el formato del nombre del archivo es "1.jpg"
    filename_without_extension, file_extension = os.path.splitext(filename)
    try:
        true_label = int(filename_without_extension)
    except ValueError:
        # Manejar el caso en el que el formato del nombre de archivo no es un número válido
        print(f'Error: El nombre del archivo "{filename}" no es un número válido')
        continue  # Saltar esta imagen
        
    # Compara la etiqueta predicha con la etiqueta real
    if target == true_label:
        correct_predictions += 1
        
    total_images += 1

# Calcula la precisión
accuracy = correct_predictions / total_images
print(f'Accuracy: {accuracy}')
