import requests

API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Open your image file
image_path = "/Users/weiwenesther/Downloads/istockphoto-538665020-612x612.jpg" #random image to test
with open(image_path, "rb") as image:
    image_data = image.read()

response = requests.post(API_URL, headers=HEADERS, data=image_data)

print("Status Code:", response.status_code)
print("Response:", response.json())
