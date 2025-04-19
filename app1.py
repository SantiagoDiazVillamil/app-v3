import streamlit as st
import joblib
import re
from PIL import Image
import base64

# ---------------- CONFIGURACIÓN ------------------
st.set_page_config(page_title="Tweet Predictor", page_icon="🐦", layout="centered")

# ---------------- MODELO Y VECTORIZADOR ------------------
@st.cache_resource
def cargar_modelo():
    modelo = joblib.load("modelo_ann.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return modelo, vectorizer

modelo, vectorizer = cargar_modelo()

# ---------------- LIMPIEZA DE TEXTO ------------------
with open("stopwords_en.txt", "r", encoding="utf-8") as f:
    stop_words = [line.strip() for line in f.readlines()]

def limpiar_texto(texto):
    texto = texto.replace("'", '').lower()
    texto = " ".join([k for k in texto.split() if k not in stop_words])
    texto = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]', '', texto)
    return texto

# ---------------- ESTILOS ------------------
st.markdown("""
    <style>
        .image-container {
            position: relative;
            text-align: center;
        }

        .tweet-textbox {
            position: absolute;
            top: 100px;
            left: 160px;
            width: 690px;
            height: 90px;
            padding: 10px;
            font-size: 16px;
            border-radius: 10px;
            border: none;
            resize: none;
            z-index: 10;
        }

        .tweet-button {
            position: absolute;
            top: 220px;
            left: 825px;
            background-color: #1DA1F2;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 999px;
            padding: 8px 24px;
            cursor: pointer;
            z-index: 10;
        }

        .result-box {
            margin-top: 30px;
            font-size: 18px;
            background-color: #E8F5FD;
            padding: 15px;
            border-radius: 10px;
            color: #0f1419;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- CABECERA ------------------
st.markdown("<h2 style='text-align: center;'>🐦 Tweet Predictor</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8899A6;'>Simula un tweet y predice su clasificación con IA</p>", unsafe_allow_html=True)

# ---------------- MOSTRAR IMAGEN ------------------
st.markdown("<div class='image-container'>", unsafe_allow_html=True)
image_path = "b79825e5-65fc-49d7-a8c9-5b91a47f3c36.png"
st.image(image_path, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- TEXTBOX Y BOTÓN FLOTANTES (HTML PURO) ------------------
st.components.v1.html(f"""
    <div style="position: relative; top: -610px; height: 0px;">
        <textarea id="customText" class="tweet-textbox" placeholder="What’s happening?"></textarea>
        <button onclick="sendTweet()" class="tweet-button">Post</button>
    </div>
    <script>
        const txt = window.parent.document.querySelector('textarea[data-testid="stTextArea"]');
        const customInput = document.getElementById("customText");
        customInput.addEventListener("input", function() {{
            txt.value = this.value;
            txt.dispatchEvent(new Event("input", {{ bubbles: true }}));
        }});
        function sendTweet() {{
            document.querySelector("button[kind=primary]").click();
        }}
    </script>
""", height=0)

# ---------------- INPUT OCULTO PARA STREAMLIT ------------------
tweet = st.text_area("What's happening?", key="hidden_input", )#label_visibility="collapsed")

# ---------------- PREDICCIÓN ------------------
if st.button("Post"):
    dict_pred={1:'Positive Tweet',-1:'Negative Tweet'}
    if tweet.strip() == "":
        st.warning("Please write something to post.")
    else:
        texto_limpio = limpiar_texto(tweet)
        vector = vectorizer.transform([texto_limpio]).toarray()
        pred = modelo.predict(vector)
        st.markdown(f"<div class='result-box'><b>Model prediction:</b> {dict_pred[pred[0]]}</div>", unsafe_allow_html=True)

# ---------------- FOOTER ------------------
st.markdown("""
    <hr>
    <div style='text-align: center; color: #8899A6;'>
        © 2025 · Simulación de X (Twitter) con Streamlit
    </div>
""", unsafe_allow_html=True)
