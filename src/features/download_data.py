"""
Module Name: download_data.py

The "download_data.py" module automates the download, extraction, and organization of datasets for a machine learning project, handling Kaggle API, data extraction, and directory management.
"""

import subprocess
import os
import shutil

download_path = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw"

# Ruta completa de la carpeta de datos descomprimidos
unzip_path = f"{download_path}/food-101"
zip_file_path = os.path.join(download_path, "food-101.zip")

# Verificar si la carpeta de datos descomprimidos ya existe
if os.path.exists(unzip_path):
    # Si existe, eliminarla
    subprocess.run(f"rm -r {unzip_path}", shell=True)

# Crear un directorio para .kaggle
subprocess.run("mkdir -p ~/.kaggle", shell=True)
# Copiar el archivo kaggle.json al directorio .kaggle
subprocess.run("cp kaggle.json ~/.kaggle/", shell=True)
# Establecer los permisos adecuados para el archivo kaggle.json
subprocess.run("chmod 600 ~/.kaggle/kaggle.json", shell=True)
# Descargar el conjunto de datos usando kaggle
dataset_name = 'dansbecker/food-101'
subprocess.run(f"kaggle datasets download {dataset_name} -p {download_path}", shell=True)
# Extraer el archivo zip descargado
subprocess.run(f"unzip -q {zip_file_path} -d {download_path}", shell=True)

source_directory = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw/food-101/__MACOSX/food-101/images"
destination_directory = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw"

# Obtener la lista de subdirectorios en source_directory
subdirectories = [d for d in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, d))]

# Mover cada subdirectorio al directorio de destino
for subdirectory in subdirectories:
    source_subdir = os.path.join(source_directory, subdirectory)
    destination_subdir = os.path.join(destination_directory, subdirectory)
    shutil.move(source_subdir, destination_subdir)

os.remove(zip_file_path)