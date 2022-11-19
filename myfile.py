import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime

!wget https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv

pd.read_csv("fallecidos_covid.csv")


st.title("Fallecidos por COVID-19")

st.caption("En esta página web se realiza el registro diaria de muertes por Covid-19")
text=st

st.bar_chart(data='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv, *, x=12, y=500', 
             ancho=0, 
             alto=0, 
             use_container_width=Verdadero)









tittle=st.text_input('Nombre y Apellidos:')
st.write(tittle)

d= st.date_input("Fecha de fallecimiento",datetime.date(2019, 7, 6))
st.write("ingresar fecha de fallecimiento:", d)

choice = st.selectbox("Sexo", ["Femenino","Masculino"])


option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono','Whatsapp'))
st.write('Seleccionó:', option)

tittle=st.text_input('Ingrese la opción que eligió')
st.write("Número de teléfono o email de contecto:", tittle)


