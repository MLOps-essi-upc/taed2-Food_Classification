"""
Module Name: modelling.py

This module provides utility functions for training and evaluating models with MLflow integration.
"""

import os
import torch
from PIL import Image
import torchvision.models as models
import pandas as pd
from predict_model import predict_image

# Configuración de directorios y carga de modelo
os.chdir("/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification")
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load("models/RESNET34", map_location=torch.device('cpu')))
resnet34.eval()

# Directorio de prueba y carga de etiquetas
test_data_dir = '/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/test/food_test_1'
clases_df = pd.read_csv("/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/models/Output-Food-Dictionary.csv")

# Función para calcular la pérdida cruzada
criterion = torch.nn.CrossEntropyLoss()

# Inicializar variables para métricas
total_images = 0
correct_predictions = 0
total_loss = 0.0

# Recorre las imágenes en el directorio de prueba y realiza predicciones
for filename in os.listdir(test_data_dir):
    image_path = os.path.join(test_data_dir, filename)
    image = Image.open(image_path).convert('RGB')
    probs, target = predict_image(image, model=resnet34, topk=1)
    
    # Supongamos que el formato del nombre del archivo es "1.jpg"
    filename_without_extension, file_extension = os.path.splitext(filename)
    try:
        true_label = int(filename_without_extension)
    except ValueError:
        # Manejar el caso en el que el formato del nombre de archivo no es un número válido
        print(f'Error: El nombre del archivo "{filename}" no es un número válido')
        continue  # Saltar esta imagen
    
    true_label = torch.tensor([true_label], dtype=torch.float)  # Convertir la etiqueta real a tensor de punto flotante
    loss = criterion(probs, true_label)  # Calcular la pérdida cruzada
    total_loss += loss.item()  # Sumar la pérdida a la pérdida total

    # Compara la etiqueta predicha con la etiqueta real
    if target == true_label.item():
        correct_predictions += 1
        
    total_images += 1

# Calcular el accuracy
accuracy = correct_predictions / total_images

# Calcular la pérdida promedio
average_loss = total_loss / total_images

print(f'Accuracy: {accuracy}')
print(f'Average Loss: {average_loss}')
