import streamlit as st
import pandas as pd
import numpy as np



#def lectura(a):
    #df = pd.read_csv(a, parse_dates = ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
    #return df

#df_prueba = lectura('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv') 
#st.write(df_prueba)


dfprueba=pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid%20(6).csv')
st.write(dfprueba.reset_index())

option = st.selectbox('ingresar mayor, menor o igual para ver fechas',('=','<','>'))     #STRING QUE GUARDA MI SELECCION ENTRE COMILLAS

number = st.number_input('Insertar numero')

if option == "=":
    number = st.number_input('Insertar numero')
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] == number])
if option == "<":
    number = st.number_input('Insertar numero')
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] < number])
if option ==">":
    number = st.number_input('Insertar numero')
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] > number])

#st.subheader("PRUEBA AREAS")
#chart_data = df_prueba['DISTRITO']

#st.area_chart(chart_data)
