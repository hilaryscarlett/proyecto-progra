import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="FALLECIDOS COVID",
    page_icon="🔴",
)



#---------------------------------------------------------------------------------------
st.sidebar.image('Logo_Oficial.png')
st.sidebar.markdown("<h1 style='text-align: center; color: green;'>Programación Avanzada / Proyecto 2022-2</h1>", unsafe_allow_html=True)


st.sidebar.info("INTEGRANTES: Consuelo, Melanie y Hilary")
                
st.sidebar.success('Recopilación de datos sobre la defuncion por Covid-19 del Ministerio de Salud')


with st.sidebar:
    selected = option_menu(
        menu_title='Menu',
        options = ['Inicio','Datos','Reportes','Equipo'],
        icons = ['house','map','book','people'],
        menu_icon='cast',
        default_index = 0,
    )
    
if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center; color: red;'>SITUACIÓN ACTUAL COVID-19</h1>", unsafe_allow_html=True)
    
    
if selected == 'Datos':
    
   
    st.image('ministerio.png')
    st.markdown("<h1 style='text-align: center; color: black;'>Fallecidos por Covid-19</h1>", unsafe_allow_html=True)
    st.subheader("Datos proporcionados por el Ministerio de Salud (MINSA)")
    st.caption("En esta página web se realizó el registro diario de muertes por Covid-19 y se mostrarán gráficas e imágenes")
    text=st
    
    def download_data():
        url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
        filename="fallecidos_covid"
        urllib.request.urlretrieve(url,filename)
        df=pd.read_csv("fallecidos_covid")
        return df
    
    st.subheader("Datos generales proporcionados por el Ministerio de Salud sobre el número de fallecidos")
    c=download_data()
    #st.write("dimensiones: "+str(c.shape[0])+"filas"+str(c.shape[1])+"columnas")
    st.dataframe(c)
    # CUADRO DE CARACTERÍSTICAS DEL DATASET
    st.subheader("Características del Dataset")
    st.write(c.describe())
    
    df=pd.read_csv=("https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv")
    fig=go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df='FECHA_FALLECIMIENTO',df='SEXO',df='DEPARTAMENTO'],
                   fill_color='lavender',
                   align='left'))
     ])
     fig.update_layput(height=1200,width=600,margin=dict(r=5,l=5,t=5,b=5))
     fig.show()
    
   


   
    
if selected == 'Reportes':
    st.markdown("<h1 style='text-align: center; color: black;'>Ministerio de Salud</h1>", unsafe_allow_html=True)
    
if selected == 'Equipo':
    st.markdown("<h1 style='text-align: center; color: black;'>Ministerio de Salud</h1>", unsafe_allow_html=True)
    
    

#--------------------------------------------------------------------------------------------


#chart_data = pd.DataFrame(
    #np.random.randn(20, 1),
    #columns=["a"])

#st.bar_chart(chart_data)




#tittle=st.text_input('Nombre y Apellidos:')
#st.write(tittle)

#d= st.date_input("Fecha de fallecimiento",datetime.date(2019, 7, 6))
#st.write("ingresar fecha de fallecimiento:", d)

#choice = st.selectbox("Sexo", ["Femenino","Masculino"])


#option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono','Whatsapp'))
#st.write('Seleccionó:', option)

#tittle=st.text_input('Ingrese la opción que eligió')
#st.write("Número de teléfono o email de contecto:", tittle)






