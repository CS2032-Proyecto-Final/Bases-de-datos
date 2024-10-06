import os
import boto3
from botocore.exceptions import NoCredentialsError

# Nombre del bucket de S3
BUCKET_NAME = "bucket-ingesta"

# Conexión al bucket de S3 usando las credenciales configuradas en ~/.aws/credentials
s3 = boto3.client('s3')

# Función para subir un archivo a S3
def upload_to_s3(file_path, bucket, s3_file_path):
    try:
        s3.upload_file(file_path, bucket, s3_file_path)
        print(f"Archivo {file_path} subido exitosamente a {s3_file_path} en {bucket}")
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
    except NoCredentialsError:
        print("Credenciales no disponibles.")

# Directorio donde están los archivos CSV (en este caso, movimientos_db)
csv_directory = "movimientos_db"

# Recorrer las carpetas y subir los archivos CSV al bucket S3
for root, dirs, files in os.walk(csv_directory):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(root, file)
            # Subir cada archivo al bucket S3, manteniendo la estructura de directorios
            s3_file_path = os.path.relpath(file_path, csv_directory)
            upload_to_s3(file_path, BUCKET_NAME, s3_file_path)

