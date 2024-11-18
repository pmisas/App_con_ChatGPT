import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Título de la app
st.title("Creador de Mapas de Calor para Ciudades Ficticias 🗺️")
st.write("Genera un mapa de calor interactivo para explorar datos ficticios como densidad de población, tráfico o temperatura.")

# Sidebar para configuración
st.sidebar.header("Configuración de la Ciudad")
ciudad = st.sidebar.text_input("Nombre de la ciudad ficticia:", value="Ciudad Ficticia")
parametro = st.sidebar.selectbox(
    "Selecciona el parámetro a visualizar:",
    ["Densidad Poblacional", "Tráfico", "Temperatura"]
)
tamano = st.sidebar.selectbox(
    "Tamaño de la ciudad:",
    ["Pequeña", "Mediana", "Grande"]
)

# Parámetros del tamaño de la ciudad
if tamano == "Pequeña":
    num_puntos = 50
    rango_lat = 0.02
    rango_lon = 0.02
elif tamano == "Mediana":
    num_puntos = 200
    rango_lat = 0.05
    rango_lon = 0.05
else:  # Grande
    num_puntos = 500
    rango_lat = 0.1
    rango_lon = 0.1

# Generar datos ficticios
np.random.seed(42)
centro_lat, centro_lon = 37.7749, -122.4194  # Coordenadas iniciales (puedes cambiar)
latitudes = centro_lat + np.random.uniform(-rango_lat, rango_lat, num_puntos)
longitudes = centro_lon + np.random.uniform(-rango_lon, rango_lon, num_puntos)

# Crear valores para el parámetro seleccionado
if parametro == "Densidad Poblacional":
    valores = np.random.randint(100, 5000, num_puntos)  # Habitantes por zona
    unidad = "habitantes/km²"
elif parametro == "Tráfico":
    valores = np.random.randint(0, 100, num_puntos)  # Congestión en porcentaje
    unidad = "% de tráfico"
else:  # Temperatura
    valores = np.random.normal(25, 5, num_puntos).round(1)  # Temperatura en °C
    unidad = "°C"

# Crear DataFrame
data = pd.DataFrame({
    "lat": latitudes,
    "lon": longitudes,
    "valor": valores
})

# Mostrar estadísticas generales
st.subheader(f"Estadísticas Generales para {ciudad}")
st.write(f"- **Parámetro visualizado:** {parametro}")
st.write(f"- **Máximo:** {data['valor'].max()} {unidad}")
st.write(f"- **Promedio:** {data['valor'].mean():.2f} {unidad}")
st.write(f"- **Mínimo:** {data['valor'].min()} {unidad}")

# Crear el mapa de calor
st.subheader(f"Mapa de Calor para {ciudad}")
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=centro_lat,
        longitude=centro_lon,
        zoom=12,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=data,
            get_position="[lon, lat]",
            get_weight="valor",
            radius=200,
            aggregation=pdk.types.String("SUM"),
        )
    ],
))

# Tabla de datos
st.subheader("Datos Generados")
st.dataframe(data)
