import streamlit as st
from PIL import Image
import random

st.title("🥄 Spoon Sentiment Demo")

uploaded = st.file_uploader("Upload foto sendok kamu!", type=["jpg", "jpeg", "png"])

# List emosi absurd
emotions = [
    "😄 Bahagia",
    "😢 Sedih",
    "😡 Marah",
    "🤯 Stres",
    "😴 Lelah",
    "🤡 Terlalu Banyak Bercanda",
    "🤨 Merasa Diabaikan",
]

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Sendok terdeteksi!", use_column_width=True)

    st.write("🔍 Menganalisis perasaan sendok...")

    # Pilih emosi random + confidence score random
    chosen = random.choice(emotions)
    score = random.randint(50, 100)

    st.subheader(f"📌 Perasaan Sendok: {chosen}")
    st.write(f"📊 Tingkat keyakinan AI: **{score}%**")

    # Pesan terapi absurd
    st.write("💡 *Saran:* Kasih sedikit perhatian, mungkin dia butuh dicuci atau diajak makan mie instan bareng.")
