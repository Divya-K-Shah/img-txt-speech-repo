from fastapi import FastAPI, File, UploadFile
import shutil
import os
from ultralytics import YOLO
import easyocr
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (React) to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to match your frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the YOLO model
MODEL_PATH = "runs part/train/weights/best.pt"  # Update with correct path
model = YOLO(MODEL_PATH)

# Initialize EasyOCR
reader = easyocr.Reader(['en'], gpu=True)

# Directory to store uploaded images
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    # Save the uploaded file
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Perform object detection
    results = model(file_location)

    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            detections.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    # Perform OCR to extract text
    text_results = reader.readtext(file_location)
    extracted_texts = [text[1] for text in text_results]

    return {"detections": detections, "text": extracted_texts}
