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
    
if selected == 'INICIO':
    st.markdown("<h1 style='text-align: center; color: red;'>SITUACIÓN ACTUAL COVID-19</h1>", unsafe_allow_html=True)
    st.subheader("¿QUÉ ES LA COVID-19?")
    st.caption("Una enfermedad infecciosa causada por el coronavirus SARS-CoV-2, que se propaga de persona a persona a través de gotitas, partículas acuosas o aerosoles expulsados por individuos infectados al momento de hablar, toser, estornudar, o incluso respirar. El virus puede ser inhalado por las personas que están cerca al enfermo y también puede contaminar cualquier tipo de superficie (pasamanos, mesas, lapiceros, entre otros), e ingresar al organismo cuando nos tocamos los ojos, nariz o boca con las manos sin lavar luego de haber tocado esas superficies contaminadas. Las personas mayores y las que sufren enfermedades respiratorias, diabetes o cardiopatías podrían desarrollar el virus en un nivel grave, si llegaran a contraerlo.")
    st.subheader("SINTOMAS:")
    st.caption("- Fiebre") 
    st.caption("- Tos seca")
    st.caption("- Cansansio") 
    st.caption("- Dolor de garganta")
    st.caption("- Dificultad para respirar") 
    st.caption("- Congestión nasal")
    text=st
    
if selected == 'DATOS':
  
   
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
    

    
if selected == 'INFORMACIÓN ESTADÍSTICA':    
    st.markdown("<h1 style='text-align: center; color: black;'>Ministerio de Salud</h1>", unsafe_allow_html=True)

    
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






