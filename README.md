# 🖥️ Hardware Classifier

A deep learning-based image classification project that identifies 
different computer hardware components from images using **TensorFlow/Keras**.

## 📌 Project Overview

The goal of this project is to build a computer vision model capable of recognizing
various computer hardware components from images. It demonstrates the practical application
of deep learning for image classification.

The model can classify the following hardware components:

- GPU
- Hard Disk
- Motherboard
- Processor
- RAM

---

## 📂 Dataset

The project uses multiple datasets, each organized into folders
containing images for different hardware categories.

Datasets included:

- `hardware_dataset`
- `hardware_dataset2`
- `hardware_dataset3`

These datasets are used for training and evaluating the image classification models.

---

## 🤖 Model

The repository includes multiple versions of the trained Keras models:

- `v1_hardware_model.keras`
- `v2_hardware_model.keras`
- `v3_hardware_model.keras`

Each version represents an improved iteration of the hardware classifier.

---

## ✨ Features

- Image-based hardware classification
- Multiple hardware categories
- Pre-trained Keras models included
- Demo video for project presentation

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Computer Vision
- Image Classification

---

## 🧪 How to Test the Model

Before testing, make sure the required Python libraries are installed in your environment, such as TensorFlow, NumPy, Matplotlib, and Pillow.

To test the model using the provided script:

1. Open [prediction.py](prediction.py).
2. Change the `MODEL_PATH` value to one of the following:
   - `v1_hardware_model.keras`
   - `v2_hardware_model.keras`
   - `v3_hardware_model.keras`
3. Run the script:

python prediction.py

4. When prompted, select an image file from your computer.
5. The script will load the selected model version, predict the hardware class, and display the result.

This allows you to test the classifier using any of the available trained model versions.

---

## 📜 License

This project is intended for educational and learning purposes.

