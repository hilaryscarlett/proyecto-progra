#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="FALLECIDOS COVID",
    page_icon="🟡",
)

with st.sidebar:
    selected = option_menu(
        menu_title = 'Menu', 
        options = ['Inicio', 'Reportes','Equipo'],
        icons = ['house', 'book', 'people'],
        menu_icon='cast',default_index = 0,

st.sidebar.image('ministerio.png')        
st.sidebar.write("✝️","DATOS DE LOS FALLECIDOS")
st.sidebar.write("Datos")



st.image('ministerio.png')
st.header("FALLECIDOS POR COVID-19")
st.subheader("Datos proporcionados por el Ministerio de Salud (MINSA)")
st.caption("En esta página web se realizó el registro diario de muertes por Covid-19 y se mostrarán gráficas e imágenes")
text=st


def download_data():
  url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
  filename="fallecidos_covid"
  urllib.request.urlretrieve(url,filename)
  df=pd.read_csv("fallecidos_covid")
  return df
 
#  
st.subheader("Datos generales proporcionados por el Ministerio de Salud sobre el número de fallecidos")
c=download_data()
#st.write("dimensiones: "+str(c.shape[0])+"filas"+str(c.shape[1])+"columnas")
st.dataframe(c)

# CUADRO DE CARACTERÍSTICAS DEL DATASET
st.subheader("Caracteríticas del Dataset")
st.write(c.describe())


chart_data = pd.DataFrame(
    np.random.randn(20, 1),
    columns=["a"])

st.bar_chart(chart_data)




tittle=st.text_input('Nombre y Apellidos:')
st.write(tittle)

d= st.date_input("Fecha de fallecimiento",datetime.date(2019, 7, 6))
st.write("ingresar fecha de fallecimiento:", d)

choice = st.selectbox("Sexo", ["Femenino","Masculino"])


option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono','Whatsapp'))
st.write('Seleccionó:', option)

tittle=st.text_input('Ingrese la opción que eligió')
st.write("Número de teléfono o email de contecto:", tittle)






