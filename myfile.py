#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request

import altair as alt
st.sidebar.write("Fallecidos por covid")

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


chart_data = pd.DataFrame(
    np.random.randn(20, 1),
    columns=["a"])

st.bar_chart(chart_data)



import plotly.express as px


df = pd.DataFrame(
    np.random.randint(1, 6, size=(100, 2)), columns=["Item_Name", "Rating_Score"]
)

df = (
    df.groupby("Rating_Score")
    .count()
    .reset_index()
    .rename(columns={"Item_Name": "Count"})
)
df["Item_Name"] = "Samsung Galaxy S20 FE 5G"
st.dataframe(df)

fig = px.bar(
    df,
    x="Rating_Score",
    y="Count",
    color="Rating_Score",
    text="Count",
)

st.plotly_chart(fig)


tittle=st.text_input('Nombre y Apellidos:')
st.write(tittle)

d= st.date_input("Fecha de fallecimiento",datetime.date(2019, 7, 6))
st.write("ingresar fecha de fallecimiento:", d)

choice = st.selectbox("Sexo", ["Femenino","Masculino"])


option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono','Whatsapp'))
st.write('Seleccionó:', option)

tittle=st.text_input('Ingrese la opción que eligió')
st.write("Número de teléfono o email de contecto:", tittle)






