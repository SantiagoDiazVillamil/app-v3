import streamlit as st
import joblib
import re

# ---------------- CONFIGURACIÓN ------------------
st.set_page_config(page_title="Tweet Predictor", page_icon="🐦", layout="centered")

# ---------------- ESTILOS PERSONALIZADOS ------------------
st.markdown("""
    <style>
        body {
            background-color: #15202B;
        }
        .tweet-card {
            background-color: #192734;
            border-radius: 16px;
            padding: 15px;
            display: flex;
            flex-direction: row;
            gap: 15px;
            border: 1px solid #38444D;
        }
        .avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background-color: #1DA1F2;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 20px;
            color: white;
        }
        .content {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        textarea {
            background-color: transparent;
            border: none;
            resize: none;
            outline: none;
            color: white;
            font-size: 16px;
            min-height: 80px;
        }
        .icons {
            color: #1DA1F2;
            margin-top: 10px;
            font-size: 20px;
        }
        .tweet-button {
            float: right;
            background-color: #1DA1F2;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 999px;
            padding: 8px 20px;
            margin-top: 10px;
            cursor: pointer;
        }
        .prediction-label {
            margin-top: 20px;
            display: inline-block;
            padding: 8px 16px;
            background-color: #1DA1F2;
            color: white;
            border-radius: 999px;
            font-weight: bold;
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
st.markdown("<p style='text-align:center; color:#8899A6;'>Ingresa tu tweet y predice el resultado con nuestro modelo</p>", unsafe_allow_html=True)

# Simulación del tweet box
st.markdown("<div class='tweet-card'>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 9])
with col1:
    st.markdown("<div class='avatar'>S</div>", unsafe_allow_html=True)
with col2:
    tweet = st.text_area(" ", placeholder="¿Qué está pasando?", label_visibility="collapsed")

st.markdown("""
    <div class='icons'>🖼️ 🎞️ 🧵 😊 📅 📍</div>
    <form action="" method="post">
        <button class='tweet-button' type='submit'>Post</button>
    </form>
</div>
""", unsafe_allow_html=True)

# Evaluación del modelo
if tweet.strip():
    texto_limpio = limpiar_texto(tweet)
    vector = vectorizer.transform([texto_limpio]).toarray()
    pred = modelo.predict(vector)
    st.markdown(f"<div class='prediction-label'>🔮 Predicción: {pred[0]}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center; color: #8899A6;'>
        © 2025 · Simulación de X (Twitter) con Streamlit
    </div>
""", unsafe_allow_html=True)
