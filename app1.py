import streamlit as st
import joblib
import re
#from nltk.corpus import stopwords

# ---------------- CONFIGURACIÓN ------------------
st.set_page_config(page_title="Tweet Predictor", page_icon="🐦", layout="centered")

# ---------------- ESTILOS ------------------
st.markdown("""
    <style>
        body {
            background-color: #15202B;
            color: white;
        }
        .tweet-box {
            background-color: #192734;
            border: 1px solid #38444D;
            border-radius: 10px;
            padding: 10px;
        }
        .tweet-button {
            background-color: #1DA1F2;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 999px;
            padding: 10px 20px;
            margin-top: 10px;
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

# ---------------- LIMPIEZA DE TEXTO ------------------
# stop_words = stopwords.words('english')
# stop_words += [k.replace("'", '') for k in stop_words]
with open("stopwords_en.txt", "r", encoding="utf-8") as f:
    stop_words = [line.strip() for line in f.readlines()]


def limpiar_texto(texto):
    texto = texto.replace("'", '').lower()
    texto = " ".join([k for k in texto.split() if k not in stop_words])
    texto = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]', '', texto)
    return texto

# ---------------- UI ------------------
st.markdown("""
    <h2 style='color: white; text-align: center;'>🐦 Tweet Predictor</h2>
    <p style='text-align: center; color: #8899A6;'>Ingresa tu tweet y predice el resultado con nuestro modelo</p>
""", unsafe_allow_html=True)

with st.container():
    tweet = st.text_area("", placeholder="¿Qué está pasando?", height=100)

    if st.button("Twittear", help="Publicar tweet", use_container_width=True):
        if tweet.strip() == "":
            st.warning("Por favor escribe algo para twittear.")
        else:
            texto_limpio = limpiar_texto(tweet)
            vector = vectorizer.transform([texto_limpio]).toarray()
            pred = modelo.predict(vector)
            st.success(f"🔮 Predicción del modelo: {pred[0]}")

st.markdown("""
    <hr>
    <div style='text-align: center; color: #8899A6;'>
        © 2025 · Simulación de X (Twitter) con Streamlit
    </div>
""", unsafe_allow_html=True)