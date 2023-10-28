import subprocess
import os
import shutil
import platform

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'*2))

# Add to root_dir the path to the processed data folder
PROCESSED_DIR = os.path.join(ROOT_DIR, 'data//processed')
RAW_DIR = os.path.join(ROOT_DIR, 'data//raw')

# Full path to the folder of uncompressed data
zip_file_path = os.path.join(RAW_DIR, "food-101.zip")

# Check if there are directories with data in the download path
if os.path.exists(RAW_DIR):
    subdirectories = [d for d in os.listdir(RAW_DIR)
                      if os.path.isdir(os.path.join(RAW_DIR, d))]
    if subdirectories:
        # If subdirectories exist, delete them
        for subdirectory in subdirectories:
            subprocess.run(f"rm -r {os.path.join(RAW_DIR, subdirectory)}", shell=True)

DATASET_NAME = 'dansbecker/food-101'
subprocess.run(f"kaggle datasets download {DATASET_NAME} -p {RAW_DIR}", shell=True)
# Extract the downloaded zip file
subprocess.run(f"unzip -q {zip_file_path} -d {RAW_DIR}", shell=True)

# Check the operating system
if platform.system() == "Darwin":
    SOURCE_DIRECTORY = os.path.join(ROOT_DIR, 'data/raw/food-101/food-101/images')
    DESTINATION_DIRECTORY = RAW_DIR

    # Get the list of subdirectories in SOURCE_DIRECTORY
    subdirectories = [d for d in os.listdir(SOURCE_DIRECTORY)
                      if os.path.isdir(os.path.join(SOURCE_DIRECTORY, d))]

    # Move each subdirectory to the destination directory
    for subdirectory in subdirectories:
        source_subdir = os.path.join(SOURCE_DIRECTORY, subdirectory)
        destination_subdir = os.path.join(DESTINATION_DIRECTORY, subdirectory)
        shutil.move(source_subdir, destination_subdir)

if os.path.exists(
    os.path.join(ROOT_DIR, 'data/raw/food-101')
    ):
    # Delete the directory and its contents recursively
    shutil.rmtree(
        os.path.join(ROOT_DIR, 'data/raw/food-101')
        )

os.remove(zip_file_path)
