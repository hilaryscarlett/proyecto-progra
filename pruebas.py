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

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['DISTRITO', 'PROVINCIA', 'SEXO'])
st.line_chart(chart_data)

url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
datos=pd.read_csv(url,sep=",")
st.line_chart(data=datos, x='PROVINCIA',y="EDAD_DECLARADA")

st.header("intento 1")
st.area_chart(data=datos, x="SEXO",y="EDAD_DECLARADA")

st.subheader("")

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['EDAD_DECLARADA','FECHA_FALLECIMIENTO'])
st.area_chart(chart_data)

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['EDAD_DECLARADA', 'DISTRITO', 'UBIGEO'])

st.area_chart(chart_data)


