# 🧠 Azure Image Analyzer 📷

This is a simple yet powerful Python application that utilizes **Microsoft Azure's Computer Vision API** to analyze images. It detects visual features like descriptions, tags, and extracts text (OCR) from the image. The results are printed to the console and saved as a structured `output.json` file.

---

## 📌 Features

- 🔍 **Image Analysis**: Extracts image description, identifies tags, and gives a confidence score.
- 🧾 **OCR (Optical Character Recognition)**: Detects and extracts any printed text from the image.
- 📁 **Saves Results**: Output is saved in a clean and readable JSON file.

---

## 🛠️ Technologies Used

- Python 3
- Microsoft Azure Cognitive Services (Computer Vision API)
- `requests` library for API communication
- `dotenv` for managing sensitive environment variables

---

## 🚀 How It Works

1. User adds any image they want to analyze (named `sample_image.jpg`)
2. The script sends the image to Azure’s API
3. The API returns:
   - Descriptions: A sentence describing the image
   - Tags: Objects/concepts detected in the image
   - Text: Any readable text found in the image
4. Output is shown in the terminal and saved in `output.json`

---

## 🧑‍💻 Setup Instructions

### 1. 🔑 Get Azure Credentials

- Go to [Azure Portal](https://portal.azure.com/)
- Search for **Computer Vision** and create a new resource
- Copy your **Subscription Key** and **Endpoint URL**

---

### 2. 🗂️ Clone the Repository

```bash
git clone https://github.com/your-username/azure-image-analyzer.git
cd azure-image-analyzer
