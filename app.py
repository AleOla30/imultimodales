import streamlit as st
from PIL import Image

st.title('Frist App')

st.header("En este espacio comienzo a desarrollar mis aplicaciónes para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('Interfaces.png')

st.image(image, caption='Interfaces multimodales')
