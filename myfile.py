import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime




st.title("Fallecidos por COVID-19")

st.caption("En esta página web se realizó el registro diario de muertes por Covid-19 y se mostrarán gráficas e imágenes")
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





#------------------
# -*- coding: utf-8 -*-
"""PROYECTO PROGRA.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1-GdKL8HLKFka39UNUauwDkSJ2BC5S_PA
"""

!wget https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv

import pandas as pd

pd.read_csv("fallecidos_covid.csv")

#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
st.header("FALLECIDOS COVID")

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

url= "https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv"
datos=pd.read_csv(url,sep=",")
st.line_chart(data=datos,x="FECHA_UTC",y="MAGNITUD")
