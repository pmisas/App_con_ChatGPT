import streamlit as st
import pandas as pd

# Título de la app
st.title("Calculadora de PAPA (Promedio Acumulado Ponderado de Asignaturas)")

# Inicializar la base de datos de materias
if 'materias' not in st.session_state:
    st.session_state.materias = pd.DataFrame(columns=["Nombre", "Creditos", "Calificacion", "Tipologia"])

# Función para agregar una materia
def agregar_materia(nombre, creditos, calificacion, tipologia):
    nueva_materia = pd.DataFrame({
        "Nombre": [nombre],
        "Creditos": [creditos],
        "Calificacion": [calificacion],
        "Tipologia": [tipologia]
    })
    st.session_state.materias = pd.concat([st.session_state.materias, nueva_materia], ignore_index=True)

# Función para calcular el PAPA global
def calcular_papa_global():
    total_creditos = st.session_state.materias['Creditos'].sum()
    if total_creditos == 0:
        return 0
    suma_ponderada = (st.session_state.materias['Creditos'] * st.session_state.materias['Calificacion']).sum()
    papa_global = suma_ponderada / total_creditos
    return papa_global

# Función para calcular el PAPA por tipología
def calcular_papa_por_tipologia(tipologia):
    materias_filtradas = st.session_state.materias[st.session_state.materias['Tipologia'] == tipologia]
    total_creditos = materias_filtradas['Creditos'].sum()
    if total_creditos == 0:
        return 0
    suma_ponderada = (materias_filtradas['Creditos'] * materias_filtradas['Calificacion']).sum()
    papa_tipologia = suma_ponderada / total_creditos
    return papa_tipologia

# Ingresar los datos de la materia
st.subheader("Agregar nueva materia")
nombre = st.text_input("Nombre de la materia")
creditos = st.number_input("Créditos", min_value=1, max_value=12, step=1)
calificacion = st.number_input("Calificación (0-10)", min_value=0.0, max_value=10.0, step=0.1)
tipologia = st.selectbox("Tipología de la asignatura", ["Obligatoria", "Optativa", "Libre"])

if st.button("Agregar materia"):
    agregar_materia(nombre, creditos, calificacion, tipologia)
    st.success("Materia agregada exitosamente")

# Mostrar las materias ingresadas
if st.checkbox("Mostrar todas las materias"):
    st.write(st.session_state.materias)

# Calcular el PAPA global
if st.button("Calcular PAPA global"):
    papa_global = calcular_papa_global()
    st.write(f"PAPA global: {papa_global:.2f}")

# Calcular el PAPA por tipología
tipologia_seleccionada = st.selectbox("Selecciona una tipología para calcular el PAPA", ["Obligatoria", "Optativa", "Libre"])
if st.button("Calcular PAPA por tipología"):
    papa_tipologia = calcular_papa_por_tipologia(tipologia_seleccionada)
    st.write(f"PAPA de asignaturas {tipologia_seleccionada}: {papa_tipologia:.2f}")
