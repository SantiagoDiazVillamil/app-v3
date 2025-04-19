import streamlit as st
import joblib
import re

# ---------------- CONFIGURACIÓN ------------------
st.set_page_config(page_title="Tweet Predictor", page_icon="🐦", layout="centered")

# ---------------- ESTILOS ------------------
st.markdown("""
    <style>
        body {
            background-color: #15202B;
            color: white;
        }
        .tweet-container {
            background-color: #192734;
            border: 1px solid #38444D;
            border-radius: 16px;
            padding: 15px;
            margin-bottom: 20px;
        }
        .tweet-avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background-color: #1DA1F2;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 20px;
        }
        .tweet-textarea {
            width: 100%;
            resize: none;
            font-size: 16px;
            border: none;
            outline: none;
            background-color: transparent;
            color: white;
        }
        .tweet-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 10px;
        }
        .tweet-icons {
            color: #1DA1F2;
            font-size: 20px;
            gap: 15px;
        }
        .tweet-post {
            background-color: #1DA1F2;
            border: none;
            border-radius: 999px;
            color: white;
            padding: 6px 16px;
            font-weight: bold;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- MODELO Y VECTORIZADOR ------------------
@st.cache_resource
def cargar_modelo():
    modelo = joblib.load("modelo_ann.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return modelo, vectorizer

modelo, vectorizer = cargar_modelo()

# ---------------- STOPWORDS ------------------
with open("stopwords_en.txt", "r", encoding="utf-8") as f:
    stop_words = [line.strip() for line in f.readlines()]

# ---------------- LIMPIEZA DE TEXTO ------------------
def limpiar_texto(texto):
    texto = texto.replace("'", '').lower()
    texto = " ".join([k for k in texto.split() if k not in stop_words])
    texto = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]', '', texto)
    return texto

# ---------------- UI ------------------
st.markdown("<h2 style='text-align:center; color:white;'>🐦 Tweet Predictor</h2>", unsafe_allow_html=True)

st.markdown("<div class='tweet-container'>", unsafe_allow_html=True)

# Simula fila: Avatar + input
col1, col2 = st.columns([1, 9])
with col1:
    st.markdown("<div class='tweet-avatar'>S</div>", unsafe_allow_html=True)

with col2:
    tweet = st.text_area("", placeholder="What’s happening?", height=100, label_visibility="collapsed")

# Pie: íconos y botón
st.markdown("""
    <div class='tweet-footer'>
        <div class='tweet-icons'>🖼️ 🎞️ 🧵 😊 📅 📍</div>
    </div>
""", unsafe_allow_html=True)

col_a, col_b = st.columns([8, 2])
with col_b:
    if st.button("Post", type="primary", use_container_width=True):
        if tweet.strip() == "":
            st.warning("Please enter a tweet to post.")
        else:
            texto_limpio = limpiar_texto(tweet)
            vector = vectorizer.transform([texto_limpio]).toarray()
            pred = modelo.predict(vector)
            st.success(f"🔮 Model prediction: {pred[0]}")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center; color: #8899A6;'>
        © 2025 · Simulación de X con Streamlit
    </div>
""", unsafe_allow_html=True)
