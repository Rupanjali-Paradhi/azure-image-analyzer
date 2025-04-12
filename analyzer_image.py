import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# Set your Azure Computer Vision credentials
subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")
endpoint = os.getenv("AZURE_ENDPOINT")

analyze_url = f"{endpoint}/vision/v3.2/analyze"
ocr_url = f"{endpoint}/vision/v3.2/ocr"

# Load image
image_path = "sample_image.jpg"
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Tags,Color'}

# Analyze Image
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()
analysis = response.json()

# OCR (Read Text)
ocr_response = requests.post(ocr_url, headers=headers, data=image_data)
ocr_response.raise_for_status()
ocr_result = ocr_response.json()

# Save output
output = {
    "description": analysis["description"]["captions"],
    "tags": analysis["tags"],
    "ocr_text": [line["text"] for region in ocr_result["regions"] for line in region["lines"] for word in line["words"]]
}

with open("output.json", "w") as f:
    json.dump(output, f, indent=4)

print("✅ Image analysis complete. Output saved to output.json.")
