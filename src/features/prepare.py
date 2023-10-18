from pathlib import Path

import pandas as pd
import yaml
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

from src import PROCESSED_DATA_DIR, RAW_DATA_DIR

# Path of the parameters file
params_path = Path("params.yaml")

# Path of the input data folder
input_folder_path = RAW_DATA_DIR

# Path of the files to read
train_path = input_folder_path / "train.csv"
test_path = input_folder_path / "test.csv"

# Read dataset from csv file
train_data = pd.read_csv(train_path, index_col="Id")
test_data = pd.read_csv(test_path, index_col="Id")

# Read data preparation parameters
with open(params_path, "r") as params_file:
    try:
        params = yaml.safe_load(params_file)
        params = params["prepare"]
    except yaml.YAMLError as exc:
        print(exc)


# ================ #
# DATA PREPARATION #
# ================ #

# Remove rows with missing target
train_data.dropna(axis=0, subset=["SalePrice"], inplace=True)

# Separate target from predictors
y = train_data.SalePrice

# Create a DataFrame called `X` holding the predictive features.
X_full = train_data.drop(["SalePrice"], axis=1)

# To keep things simple, we'll use only numerical predictors
X = X_full.select_dtypes(exclude=["object"])
X_test = test_data.select_dtypes(exclude=["object"])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    train_size=params["train_size"],
    test_size=params["test_size"],
    random_state=params["random_state"],
)

# Handle Missing Values with Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Imputation removed column names so we put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns
X_train = imputed_X_train
X_valid = imputed_X_valid

# Path of the output data folder
Path("data/processed").mkdir(exist_ok=True)
prepared_folder_path = PROCESSED_DATA_DIR

X_train_path = prepared_folder_path / "X_train.csv"
y_train_path = prepared_folder_path / "y_train.csv"
X_valid_path = prepared_folder_path / "X_valid.csv"
y_valid_path = prepared_folder_path / "y_valid.csv"

X_train.to_csv(X_train_path, index=False)
print("Writing file {} to disk.".format(X_train_path))

y_train.to_csv(y_train_path)
print("Writing file {} to disk.".format(y_train_path))

X_valid.to_csv(X_valid_path, index=False)
print("Writing file {} to disk.".format(X_valid_path))

y_valid.to_csv(y_valid_path)
print("Writing file {} to disk.".format(y_valid_path))





####################################



import subprocess
import os
import shutil
import Augmentor
import random




download_path = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw"

if not os.path.exists(download_path):
    # Create a directory for .kaggle
    subprocess.run("mkdir -p ~/.kaggle", shell=True)
    # Copy the kaggle.json file to the .kaggle directory
    subprocess.run("cp kaggle.json ~/.kaggle/", shell=True)
    # Set appropriate permissions for the kaggle.json file
    subprocess.run("chmod 600 ~/.kaggle/kaggle.json", shell=True)
    # Download the dataset using kaggle
    dataset_name = 'dansbecker/food-101'
    subprocess.run(f"kaggle datasets download {dataset_name} -p {download_path}", shell=True)
    # Extract the downloaded zip file
    zip_name = dataset_name.split('/')[-1]
    subprocess.run(f"unzip -q ./{zip_name}.zip -d .", shell=True)
else:
    print(f"The file already exists. There's no need to download it again.")


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
