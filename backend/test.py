import requests

API_KEY = "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"
url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"  # Correct endpoint
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
