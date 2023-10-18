import os
import shutil
import Augmentor
import random

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

# Recorrer las carpetas seleccionadas y copiarlas a data/processed
for folder in selected_folders:
    src_folder = os.path.join(input_data_dir, folder)
    dest_folder = os.path.join(output_data_dir, folder)
    shutil.copytree(src_folder, dest_folder)

# Aplicar aumentación de datos a las imágenes
p = Augmentor.Pipeline(output_data_dir)
p.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
p.zoom_random(probability=0.5, percentage_area=0.8)
p.random_contrast(probability=0.5, min_factor=0.7, max_factor=1.3)
p.process()

print("Data preprocessing has been completed.")
