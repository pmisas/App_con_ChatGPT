import streamlit as st
import pandas as pd
from collections import Counter
import re

# Título de la app
st.title("Explorador de Texto Interactivo 📜")
st.write("Analiza tus textos con estadísticas detalladas, gráficos interactivos y un análisis de sentimiento más completo. ¡Todo sin necesidad de instalar librerías adicionales!")

# Entrada de texto
st.header("Ingresa tu texto:")
texto = st.text_area("Escribe o pega tu texto aquí:", height=200)

# Función para procesar texto
def procesar_texto(texto):
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())  # Eliminar puntuación y pasar a minúsculas
    palabras = texto_limpio.split()
    frases = re.split(r'[.!?]', texto)
    frases = [frase.strip() for frase in frases if frase.strip()]  # Eliminar frases vacías
    return palabras, frases

# Función para contar frecuencia de palabras
def frecuencia_palabras(palabras):
    return Counter(palabras)

# Listas extendidas de palabras positivas y negativas
palabras_positivas = [
    "bueno", "feliz", "excelente", "maravilloso", "positivo", "genial", "fantástico", "amable",
    "increíble", "satisfactorio", "amor", "alegría", "contento", "brillante", "esperanza", "éxito"
]
palabras_negativas = [
    "malo", "triste", "horrible", "terrible", "negativo", "decepcionante", "feo", "odioso",
    "difícil", "fallo", "frustración", "pesimismo", "odio", "sufrimiento", "desgracia", "pérdida"
]

# Procesamiento del texto
if texto:
    palabras, frases = procesar_texto(texto)
    frecuencia = frecuencia_palabras(palabras)

    # Estadísticas básicas
    st.header("Estadísticas del texto")
    num_palabras = len(palabras)
    num_frases = len(frases)
    num_caracteres = len(texto)

    st.write(f"- **Número total de palabras:** {num_palabras}")
    st.write(f"- **Número total de frases:** {num_frases}")
    st.write(f"- **Número total de caracteres:** {num_caracteres}")

    # Palabras clave (más frecuentes)
    st.header("Palabras clave")
    palabras_clave = pd.DataFrame(frecuencia.most_common(10), columns=["Palabra", "Frecuencia"])
    st.table(palabras_clave)

    # Gráfico de barras con Streamlit nativo
    st.header("Frecuencia de palabras")
    st.bar_chart(data=palabras_clave.set_index("Palabra"))

    # Análisis de sentimiento
    st.header("Sentimiento del texto")
    num_positivas = sum(1 for palabra in palabras if palabra in palabras_positivas)
    num_negativas = sum(1 for palabra in palabras if palabra in palabras_negativas)

    if num_positivas > num_negativas:
        st.write("El texto tiene un sentimiento general **positivo**. 😊")
    elif num_negativas > num_positivas:
        st.write("El texto tiene un sentimiento general **negativo**. 😟")
    else:
        st.write("El texto tiene un sentimiento general **neutral**. 😐")

    # Detalles del análisis de sentimiento
    st.write(f"- **Palabras positivas detectadas:** {num_positivas}")
    st.write(f"- **Palabras negativas detectadas:** {num_negativas}")
    st.write(f"- **Palabras sin clasificar:** {num_palabras - (num_positivas + num_negativas)}")

    # Proporción de sentimiento
    st.header("Proporción de Sentimiento")
    sentimiento_data = pd.DataFrame({
        "Sentimiento": ["Positivo", "Negativo", "Neutral"],
        "Cantidad": [num_positivas, num_negativas, num_palabras - (num_positivas + num_negativas)]
    })
    st.bar_chart(sentimiento_data.set_index("Sentimiento"))
else:
    st.write("Por favor, ingresa un texto para analizar.")
