"""
Module Name: download_data.py

The "download_data.py" module automates the download, extraction, and organization
of datasets for a machine learning project, handling Kaggle API, data extraction,
and directory management.
"""

import subprocess
import os
import shutil
import platform

DOWNLOAD_PATH = (
    "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw"
    )

# Full path to the folder of uncompressed data
zip_file_path = os.path.join(DOWNLOAD_PATH, "food-101.zip")

# Check if there are directories with data in the download path
if os.path.exists(DOWNLOAD_PATH):
    subdirectories = [d for d in os.listdir(DOWNLOAD_PATH)
                      if os.path.isdir(os.path.join(DOWNLOAD_PATH, d))]
    if subdirectories:
        # If subdirectories exist, delete them
        for subdirectory in subdirectories:
            subprocess.run(f"rm -r {os.path.join(DOWNLOAD_PATH, subdirectory)}", shell=True)


# Create a directory for .kaggle
subprocess.run("mkdir -p ~/.kaggle", shell=True)
# Copy the kaggle.json file to the .kaggle directory
subprocess.run("cp kaggle.json ~/.kaggle/", shell=True)
# Set the appropriate permissions for the kaggle.json file
subprocess.run("chmod 600 ~/.kaggle/kaggle.json", shell=True)
# Download the dataset using kaggle
DATASET_NAME = 'dansbecker/food-101'
subprocess.run(f"kaggle datasets download {DATASET_NAME} -p {DOWNLOAD_PATH}", shell=True)
# Extract the downloaded zip file
subprocess.run(f"unzip -q {zip_file_path} -d {DOWNLOAD_PATH}", shell=True)

SOURCE_DIRECTORY = (
    "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw/food-101/food-101/images"
    )
DESTINATION_DIRECTORY = (
    "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw"
    )

# Check the operating system
if platform.system() == "Darwin":
    SOURCE_DIRECTORY = (
        "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw/food-101/food-101/images"
        )
    DESTINATION_DIRECTORY = (
        "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw"
        )

    # Get the list of subdirectories in SOURCE_DIRECTORY
    subdirectories = [d for d in os.listdir(SOURCE_DIRECTORY)
                      if os.path.isdir(os.path.join(SOURCE_DIRECTORY, d))]

    # Move each subdirectory to the destination directory
    for subdirectory in subdirectories:
        source_subdir = os.path.join(SOURCE_DIRECTORY, subdirectory)
        destination_subdir = os.path.join(DESTINATION_DIRECTORY, subdirectory)
        shutil.move(source_subdir, destination_subdir)

if os.path.exists(
    "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw/food-101"
    ):
    # Delete the directory and its contents recursively
    shutil.rmtree(
        "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification/data/raw/food-101"
        )

os.remove(zip_file_path)
