import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request
from PIL import Image
from streamlit_option_menu import option_menu

def download_data():
    url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
    filename="fallecidos_covid"
    urllib.request.urlretrieve(url,filename)
    df=pd.read_csv("fallecidos_covid")
    return df

st.subheader("Datos generales proporcionados por el Ministerio de Salud sobre el número de fallecidos")
c=download_data()

#chart_data = pd.DataFrame(
 #   np.random.randn(20, 3),
#    columns=['DISTRITO', 'PROVINCIA', 'SEXO'])

url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
datos=pd.read_csv(url,sep=",")
#st.line_chart(data=datos, x='FECHA_FALLECIMIENTO',y="EDAD_DECLARADA")


st.subheader("HOLA")
def lectura(a):
    df = pd.read_csv(a, parse_dates = ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
    #names = ['FECHA_CORTE','FECHA_FALLECIMIENTO','EDAD_DECLARADA','SEXO','CLASFIFICACION_DEF','DEPARTAMENTO','PROVINCIA','DISTRITO','UBIGEO','UUID']
    #df.columns = names
    return df

df_prueba = lectura('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv') 
#st.write(df_prueba)

st.subheader("SELECCIONE DEPARTAMENTO")
option = st.selectbox('ingresar criterio',('LIMA','AMAZONAS'))     #STRING QUE GUARDA MI SELECCION ENTRE COMILLAS
st.write(df_prueba['DEPARTAMENTO][option])

st.subheader("PRUEBA AREAS")
chart_data = df_prueba['SEXO']

st.area_chart(chart_data)


#st.header('Ejemplo de mapa')
#df = pd.DataFrame(
#    np.random.randn(1000, 2) /[50, 50]+ [-13.15, -74.22] + [-12.03, -77.04],
#    columns=['lat', 'lon'])
# st.map(df)
