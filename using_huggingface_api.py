import requests

API_URL = "https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# Get user input for the prompt
prompt = input("Enter your description: ")

image_bytes = query({
	"inputs": prompt,
})

# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()
