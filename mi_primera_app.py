import streamlit as st

# Título de la app
st.title('Mi primera app')

# Autor de la app
st.subheader('Esta app fue elaborada por Paula Carolina Misas Marín.')

# Solicitar el nombre del usuario
nombre_usuario = st.text_input('¿Cuál es tu nombre?')

# Si el usuario ingresa su nombre, mostrar el mensaje de bienvenida
if nombre_usuario:
    st.write(f'{nombre_usuario}, te doy la bienvenida a mi primera app.')
