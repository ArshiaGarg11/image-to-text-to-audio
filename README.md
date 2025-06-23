# Image To Text To Audio Converter

This project is a simple Python script that extracts text from an image using the pytesseract library and converts it into speech using Google Text-to-Speech (gTTS) library. The output is saved as an MP3 file and can be played instantly.


## Features

- Extracts text from `.png`, `.jpg`, or any image file using OCR (Tesseract)
- Converts the text into natural speech using Google TTS
- Saves and plays the speech as an MP3 file


## Tech Stack

- Python 3.x
- [Pillow](https://python-pillow.org/) — image handling
- [pytesseract](https://pypi.org/project/pytesseract/) — OCR engine (Tesseract wrapper)
- [gTTS](https://pypi.org/project/gTTS/) — Google Text-to-Speech
- Tesseract-OCR — needs to be installed separately


## How to Run

### 1. Install dependencies

```bash
pip install pytesseract Pillow gTTS
```
### 2. Install Tesseract-OCR (this example path is for Windows)
Download from UB Mannheim build
Then set the path in the script:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
### 3. Place your image in the same folder and update the file name in the script.
```python
image_path = 'your_image.png'
```
### 4. Run the script


## Output

-Displays the extracted text in the terminal  
-Creates output_audio.mp3 in the same folder that can be played when needed.


## Example Files

-imagetoaudio.py: Main script  
-image6.png: Sample test image (not included here)  
-output_audio.mp3: Resulting audio file


## Author
Arshia Garg  
Feel free to fork, star, or suggest improvements!
