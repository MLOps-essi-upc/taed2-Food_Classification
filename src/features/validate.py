import great_expectations as gx

context = gx.get_context()


from great_expectations.dataset import PandasDataset
from great_expectations.expectations import (
    ColumnExpectation,
    expect_column_to_exist,
    expect_column_to_have_unique_values
)

# Carga tu dataset (por ejemplo, un DataFrame de pandas)
# Si estás trabajando con imágenes, primero debes cargar los datos y extraer los tamaños y nombres.

# Define tu dataset
dataset = PandasDataset(your_data)  # Reemplaza "your_data" con tus datos

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
