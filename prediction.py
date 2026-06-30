import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
# -----------------------------
# Configuration
# -----------------------------
MODEL_PATH = "v3_hardware_model.keras"
IMAGE_SIZE = (224, 224)
CLASS_NAMES = ["GPU", "Hard Disk", "Motherboard", "Processor", "RAM"]

# -----------------------------
# Load model
# -----------------------------
print("Loading model...")
model = load_model(MODEL_PATH)
print("Model loaded successfully!")

# -----------------------------
# File picker for local image upload
# -----------------------------
print("\nSelect an image file from your computer...")
Tk().withdraw()  # Hide the root window
selected_path = askopenfilename(
    title="Choose an image to classify",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
)

if not selected_path:
    print("No file selected. Exiting.")
    exit()

print(f"Analyzing: {os.path.basename(selected_path)}")

# -----------------------------
# Prepare image for prediction
# -----------------------------
img = image.load_img(selected_path, target_size=IMAGE_SIZE)
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# -----------------------------
# Predict
# -----------------------------
print("Predicting...")
predictions = model.predict(img_array, verbose=0)

winning_index = int(np.argmax(predictions))
confidence = float(np.max(predictions) * 100)
winning_label = CLASS_NAMES[winning_index]

# -----------------------------
# Display results
# -----------------------------
print("\n" + "=" * 40)
print(f"RESULT     : {winning_label}")
print(f"CONFIDENCE : {confidence:.2f}%")
print("=" * 40)

# Show the image
plt.figure(figsize=(4, 4))
plt.imshow(img)
plt.title(f"Predicted: {winning_label} ({confidence:.2f}%)")
plt.axis("off")
plt.show()
