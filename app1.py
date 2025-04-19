import streamlit as st
from PIL import Image

# Configuración de página
st.set_page_config(page_title="Mi Página Web", page_icon="🌐", layout="centered")

# Estilos CSS
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .title {
            text-align: center;
            font-size: 40px;
            color: #2c3e50;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .section-title {
            color: #34495e;
            font-size: 24px;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown('<div class="title">🌐 Bienvenido a Mi Página Web</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Una plantilla elegante y amigable para cualquier propósito</div>', unsafe_allow_html=True)

# Imagen decorativa (puedes usar tu logo o imagen propia)
st.image("https://source.unsplash.com/800x300/?technology,code", use_column_width=True)

# Sección: Sobre mí o propósito
st.markdown('<div class="section-title">📌 Acerca de este sitio</div>', unsafe_allow_html=True)
st.write("""
Este es un ejemplo de cómo puedes construir una aplicación web sencilla con [Streamlit](https://streamlit.io/). 
Puedes usarla para:
- Mostrar información de un proyecto
- Crear un portafolio personal
- Hacer dashboards interactivos
- O simplemente compartir contenido de forma elegante
""")

# Sección: Interacción
st.markdown('<div class="section-title">🧭 Interacción del usuario</div>', unsafe_allow_html=True)

nombre = st.text_input("¿Cómo te llamas?")
color = st.selectbox("¿Cuál es tu color favorito?", ["Azul", "Verde", "Rojo", "Amarillo", "Negro", "Otro"])

if st.button("Enviar"):
    st.success(f"¡Hola, {nombre}! Genial que te guste el color {color} 🎨")

# Sección: Footer
st.markdown("---")
st.markdown("© 2025 · Hecho con ❤️ usando Streamlit")

