import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime



st.title("Fallecidos por COVID-19")

st.caption("En esta página web se realiza el registro diaria de muertes por Covid-19")
text=st

tittle=st.text_input('Nombre y Apellidos:')
st.write(tittle)

d= st.date_input("Fecha de fallecimiento",datetime.date(2019, 7, 6))
st.write("ingresar fecha de fallecimiento:", d)

choice = st.selectbox("Sexo", ["Femenino","Masculino"])


option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono','Whatsapp'))
st.write('Seleccionó:', option)

tittle=st.text_input('Ingrese la opción que eligió')
st.write("Número de teléfono o email de contecto:", tittle)

