import streamlit as st
import pandas as pd
import datetime

# Configuración de la app
st.title('Registro de Finanzas Personales')

# Definir el dataframe global para almacenar la información
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=["Fecha", "Categoría", "Monto", "Tipo", "Descripción"])

# Función para agregar un registro
def agregar_registro(fecha, categoria, monto, tipo, descripcion):
    nuevo_registro = {
        "Fecha": fecha,
        "Categoría": categoria,
        "Monto": monto,
        "Tipo": tipo,
        "Descripción": descripcion
    }
    st.session_state.finanzas = st.session_state.finanzas.append(nuevo_registro, ignore_index=True)

# Función para mostrar los registros
def mostrar_registros():
    st.write(st.session_state.finanzas)

# Sección para agregar nuevos registros
st.subheader('Agregar Nuevo Registro')
fecha = st.date_input('Fecha', value=datetime.date.today())
categoria = st.selectbox('Categoría', ['Ingreso', 'Gasto', 'Ahorro', 'Presupuesto'])
monto = st.number_input('Monto', min_value=0.0, step=0.01)
tipo = st.radio('Tipo de Transacción', ['Ingreso', 'Gasto'])
descripcion = st.text_input('Descripción', '')

# Botón para agregar el registro
if st.button('Agregar Registro'):
    agregar_registro(fecha, categoria, monto, tipo, descripcion)
    st.success('Registro agregado exitosamente.')

# Mostrar los registros
if st.checkbox('Mostrar Registros'):
    mostrar_registros()

# Sección de Reportes
st.subheader('Reportes')
reportes = st.radio('Selecciona un reporte', ['Reporte Semanal', 'Reporte Mensual'])

# Función para generar reportes
def generar_reporte(tipo_reporte):
    # Filtrar por la fecha seleccionada
    if tipo_reporte == 'Reporte Semanal':
        fecha_inicio = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())  # Primer día de la semana
        fecha_fin = fecha_inicio + datetime.timedelta(days=6)  # Último día de la semana

    elif tipo_reporte == 'Reporte Mensual':
        fecha_inicio = datetime.date.today().replace(day=1)  # Primer día del mes
        fecha_fin = (fecha_inicio + pd.DateOffset(months=1) - pd.DateOffset(days=1)).date()  # Último día del mes

    # Filtrar los datos para este período
    registros_periodo = st.session_state.finanzas[(st.session_state.finanzas['Fecha'] >= pd.to_datetime(fecha_inicio)) & 
                                                 (st.session_state.finanzas['Fecha'] <= pd.to_datetime(fecha_fin))]

    # Crear reportes de diferencias
    ingresos_presupuestados = registros_periodo[(registros_periodo['Categoría'] == 'Presupuesto') & (registros_periodo['Tipo'] == 'Ingreso')]
    gastos_presupuestados = registros_periodo[(registros_periodo['Categoría'] == 'Presupuesto') & (registros_periodo['Tipo'] == 'Gasto')]
    
    ingresos_reales = registros_periodo[(registros_periodo['Tipo'] == 'Ingreso') & (registros_periodo['Categoría'] != 'Presupuesto')]
    gastos_reales = registros_periodo[(registros_periodo['Tipo'] == 'Gasto') & (registros_periodo['Categoría'] != 'Presupuesto')]

    # Sumar los valores
    ingresos_presupuestados = ingresos_presupuestados['Monto'].sum()
    gastos_presupuestados = gastos_presupuestados['Monto'].sum()

    ingresos_reales = ingresos_reales['Monto'].sum()
    gastos_reales = gastos_reales['Monto'].sum()

    # Cálculo de las diferencias
    diferencia_ingresos = ingresos_reales - ingresos_presupuestados
    diferencia_gastos = gastos_reales - gastos_presupuestados

    # Mostrar resultados
    st.write(f"Reporte de {tipo_reporte}")
    st.write(f"**Ingresos Presupuestados:** {ingresos_presupuestados}")
    st.write(f"**Ingresos Reales:** {ingresos_reales}")
    st.write(f"**Diferencia de Ingresos:** {diferencia_ingresos}")
    
    st.write(f"**Gastos Presupuestados:** {gastos_presupuestados}")
    st.write(f"**Gastos Reales:** {gastos_reales}")
    st.write(f"**Diferencia de Gastos:** {diferencia_gastos}")

# Generar el reporte seleccionado
if reportes:
    generar_reporte(reportes)

# Sección de Metas de Ahorro
st.subheader('Metas de Ahorro')
meta_ahorro = st.number_input('Meta de Ahorro', min_value=0.0, step=0.01)
ahorro_actual = st.number_input('Ahorro Actual', min_value=0.0, step=0.01)

# Mostrar progreso hacia la meta
if meta_ahorro > 0:
    progreso = (ahorro_actual / meta_ahorro) * 100
    st.write(f"Progreso hacia la meta de ahorro: {progreso:.2f}%")
else:
    st.warning('Por favor, establece una meta de ahorro.')

