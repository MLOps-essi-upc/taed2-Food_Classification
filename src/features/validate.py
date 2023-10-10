import great_expectations as gx
import numpy as np

# context.add_or_update_expectation_suite("iowa_training_suite") -> demo
context = gx.data_context.DataContext("/Users/alexandragonzalezalvarez/Desktop/taed2-Food_Classification/notebooks/processing.ipynb") 

datasource = context.sources.add_or_update_pandas(name="iowa_dataset")

from great_expectations.dataset import PandasDataset
from great_expectations.expectations import (
    ColumnExpectation,
    expect_column_to_exist, # id + label
    expect_column_to_have_unique_values # als ids de les fotos
)

#Read the processed data from processing.ipynb (train_data that is a tensor)
train_data = np.load('/Users/alexandragonzalezalvarez/Desktop/taed2-Food_Classification/notebooks/train_data.pt')

# Define tu dataset
dataset = PandasDataset(train_data)  # Reemplaza "your_data" con tus datos

# Define una expectativa para el tamaño de las imágenes
expect_column_to_exist(
    dataset, 
    column='tamaño_de_imagen',  # Reemplaza con el nombre de tu columna de tamaño
    result_format={'result_format': 'COMPLETE'}
)

# Define una expectativa para la unicidad de los nombres de las imágenes
expect_column_to_have_unique_values(
    dataset, 
    column='nombre_de_imagen',  # Reemplaza con el nombre de tu columna de nombres
    result_format={'result_format': 'COMPLETE'}
)

# Ejecuta las expectativas
results = context.run_validation_operator(
    "action_list_operator",  # El nombre del operador que ejecuta las validaciones
    [expectation1, expectation2]  # Lista de expectativas
)

# Muestra los resultados
for result in results['results']:
    print(result['expectation_config']['expectation_type'], "-", result['success'])
