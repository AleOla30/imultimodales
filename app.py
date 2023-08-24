import streamlit as st
from PIL import Image

st.title('Frist App')

st.header("En este espacio comienzo a desarrollar mis aplicaciónes para interfaces multimodales")
st.write("Esta es una obra generada por mi")
image = Image.open('Interfaces.png')

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es mi primera columna")
  st.write("Las interfaces multimodales mejoraran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto')

with col2:
  st.subheader("Esta es mi segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ('visual','auditiva','tactil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('la audicion es fundamental para tu interfaz')
  if modo == 'tactil':
    st.write('el tactil es fundamental para tu interfaz')
  
