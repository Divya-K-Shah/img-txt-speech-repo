import os
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

# Load YOLO model from your project directory
model_path = os.path.join(os.getcwd(), "runs part/train/weights/best.pt")
model = YOLO(model_path)

# Path to test image (Ensure this image exists)
test_image_path = "E:/KJ Somaiya/Internship/road imgs/1.jpg"

# Check if the image path is valid
if not os.path.exists(test_image_path):
    print(f"Error: Image not found at {test_image_path}")
    exit()

# Perform object detection
results = model(test_image_path, stream=True)

# Load the image
image = cv2.imread(test_image_path)

# Check if image loaded properly
if image is None:
    print("Error: Image not loaded. Check the path!")
    exit()

# Draw bounding boxes
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  
        width = x2 - x1
        height = y2 - y1
        area = width * height

        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  
        cv2.putText(image, f"Area: {area}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_rgb)
plt.axis('off')  
plt.show()
