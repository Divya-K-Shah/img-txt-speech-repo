import streamlit as st
import numpy as np
import cv2
from PIL import Image
import easyocr
from gtts import gTTS
import os
import tempfile

# Initialize OCR reader
reader = easyocr.Reader(['en'], gpu=True)

def perform_ocr(image_np):
    result = reader.readtext(image_np)
    extracted_text = ' '.join([text for _, text, prob in result if prob > 0.5])
    return extracted_text.strip()

def text_to_speech(text):
    tts = gTTS(text=text, lang='en', slow=False)
    temp_file = os.path.join(tempfile.gettempdir(), "tts_output.mp3")
    tts.save(temp_file)
    return temp_file

# Streamlit UI
st.set_page_config(page_title="OCR + TTS", layout="centered")
st.title("🧠 OCR + Text-to-Speech")
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    image_np = np.array(image)

    if st.button("🔍 Extract Text and Convert to Speech"):
        with st.spinner("Processing..."):
            extracted_text = perform_ocr(image_np)
            if extracted_text:
                st.success("✅ Text Extracted:")
                st.write(extracted_text)

                audio_path = text_to_speech(extracted_text)
                audio_file = open(audio_path, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
            else:
                st.warning("No readable text found.")
