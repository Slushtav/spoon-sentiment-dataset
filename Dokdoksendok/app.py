import streamlit as st
import cv2
import numpy as np
import joblib
from PIL import Image

# Load model
model = joblib.load("model.pkl")

st.title("🥄 AI Pendeteksi Perasaan Sendok")
st.write("Upload foto sendok untuk mengetahui mood sendok hari ini ✨")

uploaded_file = st.file_uploader("Upload foto sendok", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Tampilkan gambar
    img = Image.open(uploaded_file)
    st.image(img, caption="Foto sendok terupload", use_column_width=True)

    # Preprocessing
    img = img.convert("RGB")
    img = np.array(img)
    img = cv2.resize(img, (128, 128))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = img.flatten().reshape(1, -1)

    # Prediksi
    prediction = model.predict(img)[0]
    proba = model.predict_proba(img)[0]

    st.subheader("Hasil Prediksi 🎉")
    st.write(f"**Perasaan sendok:** `{prediction}`")

    st.write("Probabilitas:")
    for label, p in zip(model.classes_, proba):
        st.write(f"- {label}: {p:.2f}")
