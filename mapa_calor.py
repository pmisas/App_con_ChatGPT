import streamlit as st
import pandas as pd
from collections import Counter
import re

# Título de la app
st.title("Explorador de Texto Interactivo 📜")
st.write("Analiza tus textos con estadísticas detalladas, gráficos interactivos y un análisis de sentimiento más completo. ¡Todo sin necesidad de instalar librerías adicionales!")

# Texto de ejemplo por defecto
texto_defecto = ( 
    "Hoy ha sido un día maravilloso y feliz. Me siento excelente porque logré cumplir todos mis objetivos. "
    "Sin embargo, la mañana fue algo difícil debido al tráfico horrible. A pesar de eso, estoy positivo "
    "sobre lo que viene y espero tener un futuro brillante lleno de éxito y felicidad."
)

# Entrada de texto
st.header("Ingresa tu texto:")
texto = st.text_area("Escribe o pega tu texto aquí:", value=texto_defecto, height=200)

# Lista de palabras comunes a excluir (artículos, conjunciones, preposiciones)
palabras_excluidas = [
    "que", "y", "o", "la", "el", "los", "las", "de", "en", "a", "para", "por", "con", "si", "no", 
    "como", "sobre", "al", "del", "durante", "entre", "hasta", "muy", "aunque", "ya", "cuando", "porque", 
    "mientras", "cual", "todos", "algún", "uno", "alguna", "ninguno", "ni", "alguien", "aquí", "allí", "esto"
]

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
    "bueno", "feliz", "excelente", "maravilloso", "positivo", "genial", "fantástico", "increíble", "satisfactorio",
    "amor", "alegría", "contento", "brillante", "esperanza", "éxito", "alegre", "confianza", "felicidad", "gozo",
    "inspiración", "ilusión", "optimismo", "paz", "plenitud", "prosperidad", "satisfacción", "serenidad", "sonrisa", 
    "ternura", "tranquilidad", "vitalidad", "vigor", "bienestar", "compasión", "motivación", "proactivo", "valiente"
]
palabras_negativas = [
    "abatido", "aburrido", "agobiado", "aislamiento", "angustia", "ansiedad", "apatía", "arrogancia", "atormentado",
    "vergüenza", "decepción", "desconfianza", "desesperación", "frustración", "ira", "tristeza", "soledad", "pánico",
    "miedo", "resentimiento", "rencor", "desgaste", "desilusión", "desesperanza", "malestar", "nerviosismo", "sufrimiento",
    "tensión", "tóxico", "pesimismo", "triste", "vulgaridad", "horror", "indiferencia", "desolación"
]

# Procesamiento del texto
if texto:
    # Procesar el texto ingresado
    palabras, frases = procesar_texto(texto)
    # Filtrar palabras que no son de interés (excluyendo las palabras comunes)
    palabras_filtradas = [palabra for palabra in palabras if palabra not in palabras_excluidas]
    frecuencia = frecuencia_palabras(palabras_filtradas)

    # Estadísticas básicas
    st.header("Estadísticas del texto")
    num_palabras = len(palabras_filtradas)
    num_frases = len(frases)
    num_caracteres = len(texto)

    st.write(f"- **Número total de palabras (sin palabras comunes):** {num_palabras}")
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
    num_positivas = sum(1 for palabra in palabras_filtradas if palabra in palabras_positivas)
    num_negativas = sum(1 for palabra in palabras_filtradas if palabra in palabras_negativas)

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
