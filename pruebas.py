import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request

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


#url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
#datos=pd.read_csv(url,sep=",")
#st.line_chart(data=datos, x='FECHA_FALLECIMIENTO',y="EDAD_DECLARADA")


st.subheader("HOLA")
def lectura(a):
    df = pd.read_csv(a, parse_dates = ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
    #names = ['FECHA_CORTE','FECHA_FALLECIMIENTO','EDAD_DECLARADA','SEXO','CLASFIFICACION_DEF','DEPARTAMENTO','PROVINCIA','DISTRITO','UBIGEO','UUID']
    #df.columns = names
    return df




#df_prueba = lectura('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv') 
#st.write(df_prueba)


dfprueba=lectura('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid%20(6).csv')
st.subheader("escoje departamento")

option = st.selectbox('ingresar criterio',('SEXO','EDAD_DECLARADA'))     #STRING QUE GUARDA MI SELECCION ENTRE COMILLAS
st.write(dfprueba[option])




#st.subheader("SELECCIONE DEPARTAMENTO")
#option = st.selectbox('ingresar criterio',('LIMA','AMAZONAS'))     #STRING QUE GUARDA MI SELECCION ENTRE COMILLAS
#st.write(df_prueba.loc[option])




#st.subheader("PRUEBA AREAS")
#chart_data = df_prueba['DISTRITO']

st.area_chart(chart_data)
