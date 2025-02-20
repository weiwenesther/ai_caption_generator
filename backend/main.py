import os
import requests
from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

load_dotenv()  

app = FastAPI()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

@app.post("/generate-caption/")
async def generate_caption(file: UploadFile = File(...)):
    image_data = await file.read()

    response = requests.post(HUGGINGFACE_API_URL, headers=HEADERS, data=image_data)

    if response.status_code == 200:
        caption = response.json()[0]["generated_text"]
        return {"caption": caption}
    else:
        return {"error": "Failed to generate caption"}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
