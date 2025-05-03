Image to Text to Speech Converter
This project allows users to upload an image, extract the text from it using Optical Character Recognition (OCR), and then convert the extracted text into speech using a text-to-speech engine. It is designed to help visually impaired users access written content more easily.

Features
Upload or capture an image containing text

Extract text from the image using Tesseract OCR

Convert the extracted text to speech using pyttsx3

Simple user interface built with Streamlit

Technologies Used
Python

Streamlit

pytesseract (Tesseract OCR)

Pillow (PIL)

pyttsx3

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Divya-K-Shah/img-txt-speech-repo.git
cd img-txt-speech-repo
Install the required packages:

nginx
Copy
Edit
pip install -r requirements.txt
Install Tesseract OCR:

Windows: Download from https://github.com/tesseract-ocr/tesseract

Add the Tesseract installation path to your system environment variables.

Run the Streamlit application:

arduino
Copy
Edit
streamlit run app.py
Project Structure
bash
Copy
Edit
img-txt-speech-repo/
├── app.py                # Main application file
├── requirements.txt      # Dependencies
├── utils/                # Helper functions (if any)
└── assets/               # Static files like images or audio (optional)
Future Improvements
Add support for multiple languages

Improve user interface design

Integrate real-time image capture

Enhance speech customization (speed, voice, etc.)
