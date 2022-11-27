import pandas as pd
import numpy as np
import streamlit as st
def download_data():
    url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
    filename="fallecidos_covid"
    urllib.request.urlretrieve(url,filename)
    df=pd.read_csv("fallecidos_covid")
    return df
st.subheader("Datos generales proporcionados por el Ministerio de Salud sobre el número de fallecidos")
c=download_data()

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['DISTRITO', 'PROVINCIA', 'SEXO'])

st.line_chart(chart_data)

