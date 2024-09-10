import os
from azure.storage.blob import BlobServiceClient
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure Blob Storage Configuration
connection_string = os.getenv("AZURE_CONNECTION_STRING")
container_name = "weathercontainer1"
blob_name = "metar_knkx.json"

# Weather API Configuration
aviation_url = "https://aviationweather.gov/api/data/metar?ids=KNKX&format=json&taf=true&hours=96&bbox=40%2C-90%2C45%2C-85&date=2024-08-13T20%3A10%3A01Z"

def get_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for non-200 status codes
        return response.content
    except requests.RequestException as e:
        raise Exception(f"Error fetching data from {url}: {e}")

def upload_to_azure(data, connection_string, container_name, blob_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(data, overwrite=True)
        print(f"Data uploaded to Azure Blob Storage: {blob_name}")
    except Exception as e:
        raise Exception(f"Failed to upload data to Azure Blob Storage: {e}")

if __name__ == "__main__":
    weather_data = get_weather_data(aviation_url)
    upload_to_azure(weather_data, connection_string, container_name, blob_name)
