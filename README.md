````markdown
# 🔥 AI-Powered Fire & Smoke Detection System

An end-to-end Deep Learning application designed for building safety and early fire risk detection. This system uses **Convolutional Neural Networks (Transfer Learning via MobileNetV2)** to classify images as **Fire** or **No Fire**.

To increase reliability and interpretability, the system features a decoupled **FastAPI Backend** and a modern **Streamlit Frontend**, equipped with **Grad-CAM (Explainable AI)** to visually highlight the exact region of the image where the model detects fire.

---

# 📸 Project Demo

*(You can add screenshots of your Streamlit app here in the future.)*

**Safe Scenario**
- Detects normal environments with high confidence.

**Fire Scenario**
- Detects flames or smoke and applies a Grad-CAM heatmap to highlight the detected fire region.

Example:

```markdown
<img width="691" height="388" alt="image" src="https://github.com/user-attachments/assets/7db941d2-5214-400c-8f82-e696ec4e0c4f" />

```

---

# 🏗️ System Architecture

The project follows a modern, production-ready architecture.

- **Training Module (`train_cnn.ipynb`)**
  - Trains the MobileNetV2 model using custom fire and no-fire images.

- **Backend (`backend/`)**
  - Built using FastAPI.
  - Loads the trained model.
  - Performs image preprocessing.
  - Predicts fire/no-fire.
  - Generates Grad-CAM visualizations.

- **Frontend (`frontend/`)**
  - Built using Streamlit.
  - Allows users to upload images.
  - Displays prediction results with confidence scores and Grad-CAM heatmaps.

---

# 📁 Directory Structure

```text
Fire detection/
│
├── backend/
│   └── api.py
│
├── frontend/
│   └── app.py
│
├── fire_dataset/
│   ├── fire/
│   └── no_fire/
│
├── models/
│   └── fire_cnn_model.h5
│
├── train_cnn.ipynb
├── requirements.txt
└── README.md
```

---

# 🧠 Technology Stack

| Component | Technology | Purpose |
|------------|------------|---------|
| Deep Learning | TensorFlow, Keras | Model Training |
| CNN Model | MobileNetV2 | Transfer Learning |
| Explainable AI | Grad-CAM, OpenCV | Fire Region Visualization |
| Backend | FastAPI, Uvicorn | REST API |
| Frontend | Streamlit | User Interface |
| Image Processing | Pillow, NumPy | Image Handling |

---

# ⚙️ Installation

## Prerequisites

- Python 3.8+
- pip

---

## Clone Repository

```bash
git clone https://github.com/your-username/Fire-detection.git
cd Fire-detection
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install tensorflow streamlit fastapi uvicorn pillow opencv-python python-multipart numpy
```

---

# 🚀 Running the Project

## Step 1 — Prepare Dataset

Place images inside the following folders:

```text
fire_dataset/
│
├── fire/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
└── no_fire/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

A balanced dataset is recommended (for example, 1000 fire images and 1000 no-fire images).

---

## Step 2 — Train the Model

Open

```text
train_cnn.ipynb
```

Run all cells.

After training completes, the model will be saved as:

```text
models/fire_cnn_model.h5
```

---

## Step 3 — Start FastAPI Backend

Open a terminal.

```bash
cd backend

uvicorn api:app --reload --port 8000
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## Step 4 — Start Streamlit Frontend

Open another terminal.

```bash
cd frontend

streamlit run app.py
```

The browser will automatically open:

```
http://localhost:8501
```

---

# ✨ Features

- Transfer Learning using MobileNetV2
- Binary Classification (Fire / No Fire)
- FastAPI REST API
- Modern Streamlit User Interface
- Grad-CAM Explainable AI
- Confidence Score Display
- Heatmap Overlay
- Clean Modular Architecture
- Easy Deployment

---

# 🧠 Model Details

| Property | Value |
|-----------|-------|
| Model | MobileNetV2 |
| Framework | TensorFlow/Keras |
| Input Size | 224 × 224 |
| Output | Fire / No Fire |
| Loss Function | Binary Crossentropy |
| Optimizer | Adam |
| Learning Rate | 0.0001 |
| Metrics | Accuracy |

---

# 📊 Training Pipeline

1. Load Dataset
2. Resize Images (224×224)
3. Normalize Pixel Values
4. Data Augmentation
5. Transfer Learning
6. Fine Tuning
7. Train Model
8. Save Best Model
9. Deploy Using FastAPI
10. Visualize Predictions Using Grad-CAM

---

# 📈 Future Improvements

- Real-Time CCTV Fire Detection
- Live Webcam Detection
- Smoke Segmentation
- Video Processing
- IoT Sensor Integration
- Firebase Alert System
- Email Notifications
- SMS Alerts
- Android Application
- Cloud Deployment (AWS/Azure/GCP)

---

# ⚠️ Limitations

- Performance depends on dataset quality.
- Designed for image classification only.
- Does not currently support real-time video streams.
- May misclassify unusual fire scenarios if not included in training data.

---

# 👨‍💻 Author

**Hassam Jan**

BS Artificial Intelligence

Deep Learning • Computer Vision • Machine Learning

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Acknowledgements

- TensorFlow
- Keras
- FastAPI
- Streamlit
- OpenCV
- MobileNetV2
- Grad-CAM Research Paper
````
