#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
st.header("FALLECIDOS COVID")

def download_data():
  url=https://files.minsa.gob.pe/s/t9AFqRbXw3F55Ho/download
    filename="fallecidos_covid"
    urllib.request.urlretrieve(url,filename)
    df=pd.read_csv("fallecidos_covid")
    return df
  c=download_data()
  st.write("dimensiones: "+str(c.shape[0])+"filas"+str(c.shape[1])+"columnas")
  st.dataframe(c)
  st.subheader("caracteristicas del dataset")
  st.write(c.describe())
  
  
