import numpy as np
import pandas as pd


dfprueba=pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv')

title = st.text_input('igual', 'mayor','menor')

st.write('usted escogio', title)

number = st.number_input('Insertar numero')

if title == 'igual':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] == number])
if title == 'menor':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] < number])
if title == 'mayor':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] > number])
