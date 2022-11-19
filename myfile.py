import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime


st.title("Proyecto Programación 2022-2")
st.title("                Fallecidos por covid              ")
d= st.date_input("fallecidos",datetime.date(2019, 7, 6))
st.write("ingresar fecha de fallecimiento:", d)
option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)

tittle=st.text_input('Ingrese su número de Teléfono')


