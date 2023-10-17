import subprocess
import os

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