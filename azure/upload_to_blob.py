from azure.storage.blob import BlobServiceClient
import os

AZURE_STORAGE_CONNECTION_STRING = "<your_connection_string>"
CONTAINER_NAME = "realestate-data"

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

def upload_file_to_blob(file_path, blob_name):
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"Uploaded {file_path} to blob {blob_name}")

files_to_upload = {
    "../data/processed_toronto_hpi.csv": "data/processed_toronto_hpi.csv",
    "../model/price_model.pkl": "model/price_model.pkl"
}

for local_path, blob_path in files_to_upload.items():
    upload_file_to_blob(local_path, blob_path)
