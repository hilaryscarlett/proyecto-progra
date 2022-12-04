#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np


df_prueba = pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv') 
st.write(df_prueba)

number=st.number_input('insertar numero que sale al lado de su ubigeo')

filtro= st.selectbox('ingresar mayor, menor o igual para ver fechas',('=','<','>'))     #STRING QUE GUARDA MI SELECCION ENTRE COMILLAS

num = st.number_input('Insertar numero')

if filtro == "=":
    st.write(df_prueba.loc[df_prueba['EDAD_DECLARADA'] == num])
if filtro == "<":
    st.write(df_prueba.loc[df_prueba['EDAD_DECLARADA'] < num])
if filtro ==">":
    st.write(df_prueba.loc[df_prueba['EDAD_DECLARADA'] > num])



st.subheader("PRUEBA AREAS")
chart_data = df_prueba['SEXO']['UUID']
st.area_chart(chart_data)





#st.write(st.table(df_prueba.iloc[0:10]))

#st.write(df_prueba.iloc[1000])



