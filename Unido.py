#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np


df_prueba = pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv') 
st.write(df_prueba)

number=st.number_input('insertar numero que sale al lado de su ubigeo')


st.write(st.table(df_prueba.iloc[0:10]))

#st.write(df_prueba.iloc[1000])





