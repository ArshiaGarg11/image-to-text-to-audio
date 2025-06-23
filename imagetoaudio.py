import pytesseract
from PIL import Image
from gtts import gTTS
import os

# ✅ Set path to tesseract.exe (Windows only)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image
image_path = 'image6.png'  # Replace with your actual image file
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Image file '{image_path}' not found!")
    exit()

# Extract text from image
text = pytesseract.image_to_string(image)
print("Extracted Text:")
print(text)

# Convert text to speech
if text.strip():  # Only convert if text is not empty
    tts = gTTS(text)
    tts.save("output_audio.mp3")
    print("Audio saved as output_audio.mp3")
    os.system("start output_audio.mp3")  # Automatically plays it (Windows only)
else:
    print("No text found in image.")

