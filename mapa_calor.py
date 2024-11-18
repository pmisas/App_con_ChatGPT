import streamlit as st
import pandas as pd
from collections import Counter
import re

# Título de la app
st.title("Explorador de Texto Interactivo 📜")
st.write("Analiza tus textos con estadísticas detalladas, gráficos interactivos y un análisis de sentimiento más completo. ¡Todo sin necesidad de instalar librerías adicionales!")
texto_defecto = ( "Hoy ha sido un día maravilloso y feliz. Me siento excelente porque logré cumplir todos mis objetivos. " "Sin embargo, la mañana fue algo difícil debido al tráfico horrible. A pesar de eso, estoy positivo " "sobre lo que viene y espero tener un futuro brillante lleno de éxito y felicidad." )

# Entrada de texto
st.header("Ingresa tu texto:")
texto = st.text_area("Escribe o pega tu texto aquí:", value = texto_defecto,  height=200)

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
    "increíble", "satisfactorio", "amor", "alegría", "contento", "brillante", "esperanza", "éxito", " Alegre", " Amor", " Apoyo", " Armonía", " Bienestar", " Bendición", " Cariño", " Comodidad", " Confiabilidad", " Confort", " Confianza",
    " Contento", " Creatividad", " Éxito", " Felicidad", " Gratitud", " Esperanza", " Gozo", " Ilusión", " Inspiración", " Júbilo", " Lleno de vida", " Luminoso", " Optimismo", " Paz", " Plenitud", " Prosperidad", " Relajación", " Seguridad",
    " Satisfacción", " Serenidad", " Sonrisa", " Solaz", " Ternura", " Tranquilidad", " Vitalidad", " Vigor", " Bienaventuranza", " Entusiasmo", " Euforia", " Estabilidad", " Compasión", " Curación", " Fe", " Cariñoso", " Complacido",
    " Motivación", " Alivio", " Paz interior", " Optimista", " Aceptación", " Amable", " Apreciación", " Atento", " Bello", " Brillante", " Cálido", " Carismático", " Cautivador", " Claro", " Comprometido", " Consciente", " Convivialidad",
    " Creativo", " Determinado", " Dedicado", " Elegante", " Emprendedor", " Empático", " Encantador", " Enérgico", " Entusiasta", " Exitoso", " Excepcional", " Generoso", " Hábil", " Heroico", " Honesto", " Imparable", " Inteligente",
    " Justo", " Leal", " Luminoso", " Magnífico", " Noble", " Optimista", " Perseverante", " Positivo", " Precioso", " Proactivo", " Profesional", " Prudente", " Puntual", " Resiliente", " Respetuoso", " Sabio", " Sensato", " Sincero",
    " Solidario", " Valiente", " Aprobado", " Alcanzado", " Afortunado", " Avanzado", " Bien logrado", " Campeón", " Certificación", " Conquista", " Cumplido", " Crecido", " Destacado", " Elevado", " Excelencia", " Excelente",
    " Exitoso", " Finalista", " Galardonado", " Grandeza", " Hito", " Impresionante", " Influente", " Innovador", " Jubiloso", " Logrado", " Máximo", " Mejorado", " Mejoría", " Obtenido", " Oportunidad", " Reconocido", " Realizado",
    " Recompensa", " Remarcable", " Triunfo", " Unido", " Valorado", " Victorioso", " Vencedor", " Valoración", " Creación", " Progreso", " Productivo", " Próspero", " Triunfante", " Fulminante", " Brillante", " Respetado",
    " Emprendimiento", " Innovación", " Resuelto", " Apoyo", " Apreciado", " Amoroso", " Cariñoso", " Cálido", " Comprometido", " Comprensivo", " Conectado", " Convivencia", " Considerado", " Cooperación", " Desinteresado",
    " Dedicación", " Empático", " Equilibrado", " Estimado", " Fraternidad", " Generoso", " Harmonioso", " Integridad", " Incondicional", " Leal", " Motivador", " Noble", " Paciente", " Positivo", " Preocupado", " Proactivo", " Respetuoso",
    " Solidario", " Sincero", " Tierno", " Unión", " Valioso", " Vínculo", " Amistoso", " Reconocimiento", " Afecto", " Compasivo", " Comprensión", " Confianza", " Honestidad", " Lealtad", " Apasionado", " Emocionalmente disponible",
    " Consideración", " Cumplimiento", " Sociable", " Amistad", " Escucha activa", " Alegre", " Amable", " Energético", " Estable", " Fresco", " Saludable", " Revitalizado", " Robusto", " Renovado", " Vigoroso", " Bienestar", " Activo",
    " Refrescante", " Sin estrés", " Confortable", " Rejuvenecido", " Cuidado", " Plenitud", " Positivo", " Relajado", " Alivio", " Apoyo", " Aceptación", " Cuidado", " Abundancia", " Bienestar emocional", " Bienestar físico",
    " Claridad", " Condición", " Energía positiva", " Equilibrio", " Estimulación", " Firmeza", " Fortaleza", " Generosidad", " Gratificación", " Luminiscencia", " Magnanimidad", " Ponderación", " Seguridad emocional", " Serene",
    " Sereneza", " Solidaridad", " Tranquilidad mental", " Validez", " Vitalidad", " Acción positiva", " Brillo", " Comunidad", " Concentración", " Convivencia pacífica", " Creatividad mental", " Desarrollo", " Éxito profesional",
    " Éxito personal", " Empatía", " Entusiasmo", " Evolución", " Fortaleza mental", " Gratitud", " Iluminación", " Innovación", " Logro personal", " Motivación", " Nueva oportunidad", " Participación", " Persistencia",
    " Rejuvenecimiento", " Renovación", " Resiliencia", " Sabiduría", " Sentimiento positivo", " Serenidad mental", " Simpatía", " Sinceridad", " Socialización", " Superación", " Tolerancia", " Visión positiva", " Zen", " Cautivante",
    " Atracción", " Atractivo", " Bienestar integral", " Compromiso", " Consistencia", " Creatividad", " Disciplina", " Divertido", " Fascinante", " Facilidad", " Galardón", " Gratitud continua", " Apoyo constante", " Amor eterno",
    " Belleza", " Bondad", " Carácter", " Carismático", " Conexión profunda", " Creatividad sin límites", " Éxito en equipo", " Fascinación", " Fantástico", " Feliz", " Generosidad infinita", " Iluminación interior", " Increíble",
    " Indestructible", " Lleno de energía", " Magia", " Motivación constante", " Movido por el amor", " Nueva perspectiva", " Organizado", " Ordenado", " Pasión", " Paz interior", " Plenitud emocional", " Propósito", " Realización",
    " Renovación personal", " Sabiduría", " Sensibilidad", " Sentimiento profundo", " Sinceridad genuina", " Trabajo en equipo", " Unidad", " Vitalidad interior", " Vida positiva", " Visión optimista", " Esperanza renovada",
    " Valoración profunda", " Aprecio", " Vitalidad compartida", " Imparable", " Refrescante", " Sanación", " Aceptación personal", " Actitud positiva", " Atención plena", " Avance", " Bienestar constante", " Caminar hacia el éxito",
    " Colaboración", " Comodidad", " Comunión", " Conciencia plena", " Conocimiento", " Empoderamiento", " Estabilidad emocional", " Esfuerzo positivo", " Esperanza colectiva", " Esperanza diaria", " Firme en la vida",
    " Generosidad sincera", " Gracia", " Indestructibilidad", " Mejora continua", " Progreso constante", " Resiliencia personal", " Sabiduría interior", " Transformación personal", " Transformación positiva", " Vigor inquebrantable",
    " Vida plena", " Trabajo con pasión"
]
palabras_negativas = [
    "Abatido", "Aburrido", "Agobiado", "Aislamiento", "Alarma", "Amargura", "Angustia", "Ansiedad", "Apatía", "Arrogancia", "Atormentado", "Avergonzado", "Bajo ánimo", "Bajo rendimiento", "Bastardo", "Basto", "Blanco", "Cansado",
    "Carencia", "Censura", "Confusión", "Contradicción", "Crueldad", "Decepción", "Desconfianza", "Desesperación", "Desgaste", "Desgarrador", "Desilusión", "Desinterés", "Desmoralizado", "Desnudo", "Desorden", "Desorientado", "Desprecio",
    "Destrucción", "Desvalido", "Desvinculación", "Dificultad", "Discriminación", "Disgusto", "Desesperanza", "Egoísmo", "Envidia", "Escaso", "Estancado", "Excesivo", "Fallido", "Frustración", "Furia", "Golpe", "Gravedad", "Grave", "Horror",
    "Hostilidad", "Impotencia", "Indiferencia", "Ira", "Irrelevante", "Irresponsabilidad", "Irritación", "Jamás", "Jodido", "Lamentable", "Lento", "Malestar", "Malicioso", "Maldición", "Malo", "Mancillado", "Mentira", "Miseria", "Miserable",
    "Molesto", "Negligencia", "Nerviosismo", "Noche oscura", "Odioso", "Pánico", "Perdido", "Perseverante", "Pesimismo", "Pésimo", "Rechazo", "Resignación", "Rencor", "Represión", "Resentimiento", "Ruin", "Ruido", "Sufrimiento", "Soledad",
    "Tensión", "Terror", "Tristeza", "Tóxico", "Triste", "Venganza", "Vergüenza", "Violencia", "Vulgaridad", "Abandono", "Aflicción", "Aislado", "Angustioso", "Antipatía", "Apatía", "Atascado", "Azotado", "Bajo estado de ánimo",
    "Bajo rendimiento", "Cero", "Cínico", "Confusión", "Contundente", "Desamparo", "Desagrado", "Desgaste emocional", "Desilusionado", "Desinteresado", "Desordenado", "Desorientación", "Desprecio", "Desprotegido", "Destruir",
    "Dificultoso", "Distorcionado", "Disperso", "Destrucción", "Injusticia", "Insoportable", "Inseguridad", "Insoportable", "Inútil", "Indiferente", "Irritable", "Malos recuerdos", "Maldición", "Maldito", "Malicioso", "Mentira",
    "Miserable", "Molesto", "Mortal", "Nefasto", "Noche oscura", "Oscuro", "Pérdida", "Pesimista", "Pesadilla", "Preocupación", "Prejuicio", "Pánico", "Rencoroso", "Represivo", "Ruin", "Ruido molesto", "Rencoroso", "Rechazado",
    "Sufrimiento", "Sufrimiento psicológico", "Tóxico", "Tristeza", "Terrorífico", "Tristeza", "Tormenta", "Vulgar", "Abandono", "Abuso", "Apatía", "Atascado", "Cansado", "Cero energía", "Confusión mental", "Culpa", "Desilusión",
    "Desamparado", "Desesperanza", "Desgarrador", "Desgaste emocional", "Desorientación", "Desesperación", "Desconfianza", "Dificultad económica", "Dificultoso", "Frustrante", "Horrible", "Hostil", "Indiferencia", "Indolencia",
    "Inquietante", "Inseguro", "Irritable", "Irritación", "Maldición constante", "Malo", "Malos recuerdos", "Maltratado", "Miseria", "Molesto", "Noche oscura", "Pesimismo", "Pérdida constante", "Preocupación constante", "Pánico constante",
    "Rechazado", "Resentimiento", "Ruin", "Sufrimiento psicológico", "Tensión constante", "Tóxico", "Tristeza profunda", "Venganza", "Vulgar", "Vulnerabilidad", "Bajo rendimiento", "Cansancio", "Desgaste mental", "Desolación", "Desorientación",
    "Desprecio", "Desquiciado", "Desventaja", "Dificultad personal", "Desesperación constante", "Exceso de preocupación", "Falta de apoyo", "Frustración profunda", "Insoportable", "Inestabilidad emocional", "Irritación constante", "Malestar",
    "Molesto", "Nerviosismo constante", "Pesimismo general", "Pérdida", "Preocupación profunda", "Rechazo continuo", "Resentimiento constante", "Ruin", "Sufrimiento extremo", "Tensión emocional", "Tóxico", "Tormento", "Vulgaridad", "Injusticia",
    "Indefensión", "Vulnerabilidad emocional", "Estrés", "Frustración", "Inquietud", "Ansiedad constante", "Irritación profunda", "Pánico", "Vulgar", "Pesimismo", "Tristeza profunda", "Desesperación"
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
