from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO
import easyocr
import os

app = FastAPI()

# Load YOLO model
MODEL_PATH = "runs part/train/weights/best.pt"
model = YOLO(MODEL_PATH)

# Load OCR reader
reader = easyocr.Reader(['en'], gpu=True)

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    contents = await file.read()
    np_img = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Perform YOLO object detection
    results = model(img)

    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detections.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    # Perform OCR on image
    text_results = reader.readtext(img)
    text_data = [text for (_, text, prob) in text_results if prob > 0.5]

    return {"detections": detections, "text": text_data}
