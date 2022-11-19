import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime



st.title("Fallecidos por COVID-19")

st.caption("En esta página web se realiza el registro diaria de muertes por Covid-19")
text=st
d= st.date_input("fallecidos",datetime.date(2019, 7, 6))
st.write("ingresar fecha de fallecimiento:", d)
option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)

tittle=st.text_input('Ingrese la opción que eligió')


