import numpy as np
import pandas as pd


dfprueba=pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv')

option = st.selectbox('mayor - menor - igual para ver fechas',('igual','menor','mayor'))
st.write(option)

number = st.number_input('Insertar numero')

if option == 'igual':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] == number])
if option == 'menor':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] < number])
if option == 'mayor':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] > number])
