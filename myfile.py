#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request

st.title("Fallecidos por COVID-19")

st.caption("En esta página web se realizó el registro diario de muertes por Covid-19 y se mostrarán gráficas e imágenes")
text=st


def download_data():
  url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
  filename="fallecidos_covid"
  urllib.request.urlretrieve(url,filename)
  df=pd.read_csv("fallecidos_covid")
  return df
  
c=download_data()
st.write("dimensiones: "+str(c.shape[0])+"filas"+str(c.shape[1])+"columnas")
st.dataframe(c)
st.subheader("caracteristicas del dataset")
st.write(c.describe())





tittle=st.text_input('Nombre y Apellidos:')
st.write(tittle)

d= st.date_input("Fecha de fallecimiento",datetime.date(2019, 7, 6))
st.write("ingresar fecha de fallecimiento:", d)

choice = st.selectbox("Sexo", ["Femenino","Masculino"])


option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono','Whatsapp'))
st.write('Seleccionó:', option)

st.sidebar.write("esto esta en el sidebar")
if st.sidebar.button("mi boton opcional")
    st.ballons()

tittle=st.text_input('Ingrese la opción que eligió')
st.write("Número de teléfono o email de contecto:", tittle)






