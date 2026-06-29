"""
🔥 Fire Detection REST API (FastAPI)
Loads: models/fire_cnn_model.h5
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = FastAPI(title="Fire Detection API")

# Global variable for model
MODEL = None


@app.on_event("startup")
def load_ml_model():
    """Loads the model once when the server starts."""
    global MODEL
    print("🔥 Loading MobileNetV2 model from models/fire_cnn_model.h5...")
    # PATH MATCHES YOUR SCREENSHOT EXACTLY
    MODEL = tf.keras.models.load_model('../models/fire_cnn_model.h5')
    print("✅ Model loaded and ready!")


def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """Transforms image - NO manual scaling, let the model handle it!"""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img)

    # ONLY convert data type and add batch dimension. DO NOT DIVIDE BY 127.5!
    img_array = img_array.astype('float32')
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


@app.post("/predict")
async def predict_fire(file: UploadFile = File(...)):
    """Takes an image, returns JSON prediction."""
    try:
        image_bytes = await file.read()
        processed_image = preprocess_image(image_bytes)

        # Predict
        predictions = MODEL.predict(processed_image, verbose=0)
        score = float(predictions[0][0])

        # Training folders were ['fire', 'no_fire'] alphabetically.
        # Index 0 = Fire, Index 1 = No Fire.
        # Sigmoid: < 0.5 is Fire, >= 0.5 is No Fire
        if score < 0.5:
            label = "Fire Detected"
            confidence = (1.0 - score) * 100
        else:
            label = "No Fire (Safe)"
            confidence = score * 100

        return JSONResponse(content={
            "status": "success",
            "label": label,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})