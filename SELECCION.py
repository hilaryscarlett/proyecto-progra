import numpy as np
import pandas as pd


#def lectura(a):
    #df = pd.read_csv(a, parse_dates = ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
    #return df

df_prueba2=pd.read_csv('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid_2.csv')

option = st.selectbox('ingresar criterio',('LIMA','AMAZONAS')) 
st.write(df_prueba2['EDAD_DECLARADA']['UBIGEO'][option])
