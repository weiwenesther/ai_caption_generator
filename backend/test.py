import requests
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"  # Correct endpoint
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
