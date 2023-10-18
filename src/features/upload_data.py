import subprocess

# Asegúrate de que estás en el directorio raíz de tu proyecto
project_directory = "/Users/violeta/Desktop/gced/Q7/TAED2/project1/taed2-Food_Classification"

# Comando DVC para agregar y subir los datos procesados
dvc_add_command = f"dvc add {project_directory}/data/processed"
dvc_push_command = "dvc push"

# Ejecuta el comando para agregar los datos a DVC
subprocess.run(dvc_add_command, shell=True)

# Ejecuta el comando para subir los datos a DVC
subprocess.run(dvc_push_command, shell=True)

