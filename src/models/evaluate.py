"""
Module Name: evaluate.py

The evaluate.py module is used to test a pre-trained image
classification model on a set of test images, calculate accuracy,
and compare the predicted labels with the ground truth labels.
"""

import os
import torch
from PIL import Image
import torchvision.models as models
import pandas as pd
from predict_model import predict_image

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'*2))

# Add to root_dir the path to the processed data folder
TEST_DIR = os.path.join(ROOT_DIR, 'data/test')
MODELS_DIR = os.path.join(ROOT_DIR, 'models')

# Cargar el modelo previamente entrenado
resnet34 = models.resnet34()
resnet34.load_state_dict(torch.load(os.path.join(MODELS_DIR, 'RESNET34'), map_location=torch.device('cpu')))
resnet34.eval()

# Directorio de prueba
TEST_DATA_DIR = os.path.join(TEST_DIR, 'food_test_1')

clases_df = pd.read_csv(os.path.join(MODELS_DIR, 'Output-Food-Dictionary.csv'))

# Inicializar la cantidad total de imágenes y el contador de predicciones correctas
TOTAL_IMAGES = 0
CORRECT_PREDICTIONS = 0

# Recorre las imágenes en el directorio de prueba y realiza predicciones
for filename in os.listdir(TEST_DATA_DIR):
    image_path = os.path.join(TEST_DATA_DIR, filename)
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
        CORRECT_PREDICTIONS += 1

    TOTAL_IMAGES += 1

# Calcula la precisión
accuracy = CORRECT_PREDICTIONS / TOTAL_IMAGES
print(f'Accuracy: {accuracy}')
