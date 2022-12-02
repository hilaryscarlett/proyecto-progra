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
    datos=pd.read_csv(url,sep=",")
    filename="fallecidos_covid"
    urllib.request.urlretrieve(url,filename)
    df=pd.read_csv("fallecidos_covid")
    return df

st.subheader("Datos generales proporcionados por el Ministerio de Salud sobre el número de fallecidos")
c=download_data()

chart_data = pd.Dataframe(
    np.random.randn(20, 3),
    columns=['DISTRITO', 'PROVINCIA', 'SEXO'])
st.line_chart(chart_data)


st.line_chart(data=datos, x='FECHA_FALLECIMIENTO', y='EDAD_DECLARADA')


st.subheader("")

chart_data = pd.DataFrame(
    np.random.randn(100, 1),
    columns=['EDAD_DECLARADA'])

st.line_chart(chart_data)

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['EDAD_DECLARADA', 'DISTRITO', 'UBIGEO'])

st.area_chart(chart_data)


