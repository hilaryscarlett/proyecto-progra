import numpy as np
import pandas as pd


dfprueba=pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid%20(6).csv')
#st.write(dfprueba.reset_index())
option = st.selectbox('mayor - menor - igual para ver fechas',('igual','menor','mayor'))

number = st.number_input('Insertar numero')

if option == 'igual':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] == number])
if option == 'menor':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] < number])
if option == 'mayor':
    st.write(dfprueba.loc[dfprueba['EDAD_DECLARADA'] > number])
