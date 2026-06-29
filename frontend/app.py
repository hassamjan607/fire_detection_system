"""
🔥 Fire Detection Professional Frontend (Streamlit)
"""

import streamlit as st
import requests
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(page_title="Fire Detection AI", page_icon="🔥", layout="centered")

# --- Professional CSS ---
st.markdown("""
<style>
    /* Main Container */
    .main { background-color: #f0f2f6; }

    /* Header Card */
    .header-card {
        background: linear-gradient(135deg, #ff4b4b 0%, #d32f2f 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3);
        margin-bottom: 30px;
    }
    .header-card h1 { margin: 0; font-size: 2.5rem; font-weight: 800; }
    .header-card p { margin: 5px 0 0 0; font-size: 1.1rem; opacity: 0.9; }

    /* Upload Card */
    .upload-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Result Cards */
    .result-safe {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
    }
    .result-fire {
        background-color: #ffebee;
        border-left: 5px solid #f44336;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        animation: shake 0.5s;
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0); }
    }
</style>
""", unsafe_allow_html=True)

# --- UI Elements ---
st.markdown('<div class="header-card"><h1>🔥 Fire Detection AI</h1><p>Powered by MobileNetV2 Deep Learning</p></div>',
            unsafe_allow_html=True)

API_URL = "http://localhost:8000/predict"

st.markdown('<div class="upload-card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📷 Upload an image for analysis", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    # Display Image
    img = Image.open(uploaded_file)
    st.image(img, use_column_width=True, caption="Uploaded Image")

    # Predict Button
    if st.button("🚀 Analyze Image", type="primary", use_container_width=True):
        with st.spinner('🔍 Analyzing image for smoke and fire...'):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}

            try:
                response = requests.post(API_URL, files=files)
                data = response.json()

                if data["status"] == "success":
                    label = data["label"]
                    confidence = data["confidence"]

                    if "Safe" in label:
                        st.markdown(f'''
                        <div class="result-safe">
                            <h2 style="color:#2e7d32; margin:0;">✅ {label}</h2>
                            <p style="color:#1b5e20; font-size:20px; margin:10px 0 0 0;">Confidence: {confidence}%</p>
                        </div>
                        ''', unsafe_allow_html=True)
                    else:
                        st.markdown(f'''
                        <div class="result-fire">
                            <h2 style="color:#c62828; margin:0;">🚨 {label} 🚨</h2>
                            <p style="color:#b71c1c; font-size:20px; margin:10px 0 0 0;">Confidence: {confidence}%</p>
                        </div>
                        ''', unsafe_allow_html=True)
                else:
                    st.error(f"Backend Error: {data['message']}")

            except requests.exceptions.ConnectionError:
                st.error(
                    "❌ **Connection Failed!** \n\nPlease make sure the FastAPI backend is running in a separate terminal.")