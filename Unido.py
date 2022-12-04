#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np


df_prueba = pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv') 
st.write(df_prueba)

st.write(df_prueba.iloc[0])















