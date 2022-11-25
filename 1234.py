#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

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

#url= "https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv"
#datos=pd.read_csv(url,sep=",")
#st.line_chart(data=datos,x="FECHA_UTC",y="MAGNITUD")

st.sidebar.write("hello this is my")
if st.sidebar.button("presionar aquí"):
  st.ballons



