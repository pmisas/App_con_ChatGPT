import streamlit as st
import pandas as pd
import datetime

# Título de la app
st.title("Gestor de Finanzas Personales")

# Inicializar el DataFrame global si no existe
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=["Fecha", "Categoría", "Presupuestado", "Real", "Descripción"])

# Función para agregar un registro
def agregar_registro(fecha, categoria, presupuestado, real, descripcion):
    nuevo_registro = pd.DataFrame({
        "Fecha": [fecha],
        "Categoría": [categoria],
        "Presupuestado": [presupuestado],
        "Real": [real],
        "Descripción": [descripcion]
    })
    st.session_state.finanzas = pd.concat([st.session_state.finanzas, nuevo_registro], ignore_index=True)

# Mostrar los registros
def mostrar_registros():
    st.write(st.session_state.finanzas)

# Elegir la categoría
categorias = ['Presupuesto', 'Ingreso', 'Gasto', 'Meta de Ahorro']
categoria = st.selectbox("Selecciona una categoría", categorias)

# Ingresar datos
st.subheader(f"Ingresar datos para {categoria}")

fecha = st.date_input("Fecha", value=datetime.date.today())
presupuestado = st.number_input("Lo Presupuestado", min_value=0.0, step=0.01)
real = st.number_input("Lo Real", min_value=0.0, step=0.01)
descripcion = st.text_input("Descripción")

# Botón para agregar el registro
if st.button("Agregar Registro"):
    agregar_registro(fecha, categoria, presupuestado, real, descripcion)
    st.success("Registro agregado exitosamente.")

# Mostrar los registros
if st.checkbox("Mostrar Todos los Registros"):
    mostrar_registros()

# Función para calcular reportes mensuales y anuales
def calcular_reportes():
    st.subheader("Reportes Financieros")
    
    # Reporte Mensual
    st.write("### Reporte Mensual")
    mes_actual = datetime.date.today().month
    anio_actual = datetime.date.today().year
    registros_mensuales = st.session_state.finanzas[(st.session_state.finanzas['Fecha'].dt.month == mes_actual) & 
                                                   (st.session_state.finanzas['Fecha'].dt.year == anio_actual)]
    
    if not registros_mensuales.empty:
        reporte_mensual = registros_mensuales.groupby('Categoría').agg(
            Presupuestado=('Presupuestado', 'sum'),
            Real=('Real', 'sum')
        ).reset_index()

        reporte_mensual['Diferencia'] = reporte_mensual['Real'] - reporte_mensual['Presupuestado']
        st.write(reporte_mensual)
    else:
        st.write("No hay registros para este mes.")

    # Reporte Anual
    st.write("### Reporte Anual")
    registros_anuales = st.session_state.finanzas[(st.session_state.finanzas['Fecha'].dt.year == anio_actual)]
    
    if not registros_anuales.empty:
        reporte_anual = registros_anuales.groupby('Categoría').agg(
            Presupuestado=('Presupuestado', 'sum'),
            Real=('Real', 'sum')
        ).reset_index()

        reporte_anual['Diferencia'] = reporte_anual['Real'] - reporte_anual['Presupuestado']
        st.write(reporte_anual)
    else:
        st.write("No hay registros para este año.")

# Calcular y mostrar los reportes
if st.button("Generar Reportes Financieros"):
    calcular_reportes()
