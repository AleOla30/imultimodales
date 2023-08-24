import streamlit as st
from PIL import Image

st.title('Frist App')

st.header("En este espacio comienzo a desarrollar mis aplicaciónes para interfaces multimodales")
st.write("Esta es una obra generada por mi")
image = Image.open('Interfaces.png')

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
