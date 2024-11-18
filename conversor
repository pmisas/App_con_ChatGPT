import streamlit as st

# Título de la app
st.title('Conversor Universal')

# Subtítulo y descripción
st.subheader('Elige una categoría y selecciona el tipo de conversión que deseas realizar.')

# Opciones de categorías
categorias = [
    'Temperatura', 'Longitud', 'Peso/Masa', 'Volumen', 'Tiempo', 
    'Velocidad', 'Área', 'Energía', 'Presión', 'Tamaño de Datos'
]

# Menú de selección de categorías
categoria = st.selectbox('Selecciona una categoría', categorias)

# Conversión según categoría
if categoria == 'Temperatura':
    conversiones_temperatura = [
        'Celsius a Fahrenheit', 'Fahrenheit a Celsius', 'Celsius a Kelvin', 'Kelvin a Celsius'
    ]
    conversion_temperatura = st.selectbox('Selecciona la conversión', conversiones_temperatura)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_temperatura == 'Celsius a Fahrenheit':
        resultado = (valor * 9/5) + 32
        st.write(f'{valor} °C = {resultado} °F')
    elif conversion_temperatura == 'Fahrenheit a Celsius':
        resultado = (valor - 32) * 5/9
        st.write(f'{valor} °F = {resultado} °C')
    elif conversion_temperatura == 'Celsius a Kelvin':
        resultado = valor + 273.15
        st.write(f'{valor} °C = {resultado} K')
    elif conversion_temperatura == 'Kelvin a Celsius':
        resultado = valor - 273.15
        st.write(f'{valor} K = {resultado} °C')

elif categoria == 'Longitud':
    conversiones_longitud = [
        'Pies a metros', 'Metros a pies', 'Pulgadas a centímetros', 'Centímetros a pulgadas'
    ]
    conversion_longitud = st.selectbox('Selecciona la conversión', conversiones_longitud)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_longitud == 'Pies a metros':
        resultado = valor * 0.3048
        st.write(f'{valor} pies = {resultado} metros')
    elif conversion_longitud == 'Metros a pies':
        resultado = valor / 0.3048
        st.write(f'{valor} metros = {resultado} pies')
    elif conversion_longitud == 'Pulgadas a centímetros':
        resultado = valor * 2.54
        st.write(f'{valor} pulgadas = {resultado} centímetros')
    elif conversion_longitud == 'Centímetros a pulgadas':
        resultado = valor / 2.54
        st.write(f'{valor} centímetros = {resultado} pulgadas')

elif categoria == 'Peso/Masa':
    conversiones_peso = [
        'Libras a kilogramos', 'Kilogramos a libras', 'Onzas a gramos', 'Gramos a onzas'
    ]
    conversion_peso = st.selectbox('Selecciona la conversión', conversiones_peso)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_peso == 'Libras a kilogramos':
        resultado = valor * 0.453592
        st.write(f'{valor} libras = {resultado} kg')
    elif conversion_peso == 'Kilogramos a libras':
        resultado = valor / 0.453592
        st.write(f'{valor} kg = {resultado} libras')
    elif conversion_peso == 'Onzas a gramos':
        resultado = valor * 28.3495
        st.write(f'{valor} onzas = {resultado} gramos')
    elif conversion_peso == 'Gramos a onzas':
        resultado = valor / 28.3495
        st.write(f'{valor} gramos = {resultado} onzas')

elif categoria == 'Volumen':
    conversiones_volumen = [
        'Galones a litros', 'Litros a galones', 'Pulgadas cúbicas a centímetros cúbicos', 'Centímetros cúbicos a pulgadas cúbicas'
    ]
    conversion_volumen = st.selectbox('Selecciona la conversión', conversiones_volumen)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_volumen == 'Galones a litros':
        resultado = valor * 3.78541
        st.write(f'{valor} galones = {resultado} litros')
    elif conversion_volumen == 'Litros a galones':
        resultado = valor / 3.78541
        st.write(f'{valor} litros = {resultado} galones')
    elif conversion_volumen == 'Pulgadas cúbicas a centímetros cúbicos':
        resultado = valor * 16.387
        st.write(f'{valor} pulgadas cúbicas = {resultado} cm³')
    elif conversion_volumen == 'Centímetros cúbicos a pulgadas cúbicas':
        resultado = valor / 16.387
        st.write(f'{valor} cm³ = {resultado} pulgadas cúbicas')

elif categoria == 'Tiempo':
    conversiones_tiempo = [
        'Horas a minutos', 'Minutos a segundos', 'Días a horas', 'Semanas a días'
    ]
    conversion_tiempo = st.selectbox('Selecciona la conversión', conversiones_tiempo)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_tiempo == 'Horas a minutos':
        resultado = valor * 60
        st.write(f'{valor} horas = {resultado} minutos')
    elif conversion_tiempo == 'Minutos a segundos':
        resultado = valor * 60
        st.write(f'{valor} minutos = {resultado} segundos')
    elif conversion_tiempo == 'Días a horas':
        resultado = valor * 24
        st.write(f'{valor} días = {resultado} horas')
    elif conversion_tiempo == 'Semanas a días':
        resultado = valor * 7
        st.write(f'{valor} semanas = {resultado} días')

elif categoria == 'Velocidad':
    conversiones_velocidad = [
        'Millas por hora a kilómetros por hora', 'Kilómetros por hora a metros por segundo',
        'Nudos a millas por hora', 'Metros por segundo a pies por segundo'
    ]
    conversion_velocidad = st.selectbox('Selecciona la conversión', conversiones_velocidad)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_velocidad == 'Millas por hora a kilómetros por hora':
        resultado = valor * 1.60934
        st.write(f'{valor} mph = {resultado} km/h')
    elif conversion_velocidad == 'Kilómetros por hora a metros por segundo':
        resultado = valor / 3.6
        st.write(f'{valor} km/h = {resultado} m/s')
    elif conversion_velocidad == 'Nudos a millas por hora':
        resultado = valor * 1.15078
        st.write(f'{valor} nudos = {resultado} mph')
    elif conversion_velocidad == 'Metros por segundo a pies por segundo':
        resultado = valor * 3.28084
        st.write(f'{valor} m/s = {resultado} ft/s')

elif categoria == 'Área':
    conversiones_area = [
        'Metros cuadrados a pies cuadrados', 'Pies cuadrados a metros cuadrados',
        'Kilómetros cuadrados a millas cuadradas', 'Millas cuadradas a kilómetros cuadrados'
    ]
    conversion_area = st.selectbox('Selecciona la conversión', conversiones_area)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_area == 'Metros cuadrados a pies cuadrados':
        resultado = valor * 10.7639
        st.write(f'{valor} m² = {resultado} ft²')
    elif conversion_area == 'Pies cuadrados a metros cuadrados':
        resultado = valor / 10.7639
        st.write(f'{valor} ft² = {resultado} m²')
    elif conversion_area == 'Kilómetros cuadrados a millas cuadradas':
        resultado = valor / 2.58999
        st.write(f'{valor} km² = {resultado} mi²')
    elif conversion_area == 'Millas cuadradas a kilómetros cuadrados':
        resultado = valor * 2.58999
        st.write(f'{valor} mi² = {resultado} km²')

elif categoria == 'Energía':
    conversiones_energia = [
        'Julios a calorías', 'Calorías a kilojulios', 'Kilovatios-hora a megajulios', 'Megajulios a kilovatios-hora'
    ]
    conversion_energia = st.selectbox('Selecciona la conversión', conversiones_energia)
    valor = st.number_input('Introduce el valor a convertir', float(0))
    
    if conversion_energia == 'Julios a calorías':
        resultado = valor * 0.239006
        st.write(f'{valor} J = {resultado} cal')
    elif conversion_energia == 'Calorías a kilojulios':
       
