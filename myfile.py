
import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request
from PIL import Image
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="FALLECIDOS COVID",
    page_icon="🔴",
)

#---------------------------------------------------------------------------------------
st.sidebar.image('Logo_Oficial.png')
st.sidebar.markdown("<h1 style='text-align: center; color: green;'>Programación Avanzada / Proyecto 2022-2</h1>", unsafe_allow_html=True)               
st.sidebar.success('Recopilación de datos sobre la defuncion por Covid-19 del Ministerio de Salud')

#---------------------------------------------------------------------------------------
with st.sidebar:
    selected = option_menu(
        menu_title='Menu',
        options = ['Inicio','Datos','Información estadística','Equipo'],
        icons = ['house','map','book','people'],
        menu_icon='cast',
        default_index = 0,
    )
    
if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center; color: red;'>SITUACIÓN ACTUAL COVID-19</h1>", unsafe_allow_html=True)
    st.subheader("¿QUÉ ES LA COVID-19?")
    st.caption("Una enfermedad infecciosa causada por el coronavirus SARS-CoV-2, que se propaga de persona a persona a través de gotitas, partículas acuosas o aerosoles expulsados por individuos infectados al momento de hablar, toser, estornudar, o incluso respirar. El virus puede ser inhalado por las personas que están cerca al enfermo y también puede contaminar cualquier tipo de superficie (pasamanos, mesas, lapiceros, entre otros), e ingresar al organismo cuando nos tocamos los ojos, nariz o boca con las manos sin lavar luego de haber tocado esas superficies contaminadas. Las personas mayores y las que sufren enfermedades respiratorias, diabetes o cardiopatías podrían desarrollar el virus en un nivel grave, si llegaran a contraerlo.")
    st.image('covid19.jpg')
    st.subheader("SÍNTOMAS:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.caption("- Fiebre") 
        st.caption("- Tos seca")
        st.caption("- Cansansio") 
        st.caption("- Dolor de garganta")
        st.caption("- Dificultad para respirar") 
        st.caption("- Congestión nasal")
        st.caption("- Perdida de olfato o gusto")
        
    with col2:
        st.image("sintomas.jpg",width=None, use_column_width="always")
        
    st.subheader("CASOS POSITIVOS DE COVID-19 EN PERÚ")
    st.caption("Número total de muestras: 36 376 044")
    st.caption("Total de casos confirmados: 4 227 446")
    
    #url 'https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
    #c = pd.read_csv(url, sep=',')
    #st.bar_chart(c)
    
    
    def download():
        url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/casospositivo19.csv'
        filename="casospositivo19"
        urllib.request.urlretrieve(url,filename)
        df=pd.read_csv("casospositivo19")
        return df
    d=download()
    st.dataframe(d)
    st.caption("Fuente: Instituto Nacional de Salud y Centro Nacional de Epidemiología, Prevención y Control de Enfermedades - MINSA")


    #EN OBSERVACIÓN---------------------------------------
    positividad= [10.98,9.22,14.57]
    provincias = ["Lima Metropolitana","Arequipa","Piura"]
    plt.pie(positividad, labels=provincias)
    plt.axis("equal")
    plt.show()
    
    st.subheader("GRÁFICA DE CASOS CONFIRMADOS")
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    positividad= [1840931,271943,174542,170320,162850,150853,147972,137842,130950,121638,120560,109382,75258,67640,63474,61241,59850,58493,54119,50107,44592,43886,31817,29094,27566,20526]
    provincias = ["Lima Metropolitana","Arequipa","Piura","La Libertad","Callao","Ancash","Junin","Cusco","Lima Region","Lambayeque","Ica","Cajamarca","Puno","San Martin","Loreto","Tacna","Moquegua","Huanuco","Ayacucho","Amazonas","Apurimac","Ucayali","Tumbes","Huancavelica","Pasco","Madre de Dios"]
    xx = range(len(provincias))
    ax.bar(xx, positividad, width=1, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(provincias,rotation="vertical")
    plt.show()
    st.pyplot(plt)
    
    st.caption("Elaboración propia con datos del Ministerio de salud")
    #_-----------------------------------------------------------
    st.subheader("FALLECIDOS POR COVID 19")
 
    
    text=st
    
    
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
    

    
if selected == 'Información estadística':    
    st.markdown("<h1 style='text-align: center; color: black;'>INFORMACIÓN GRÁFICA DE LOS FALLECIDOS POR COIVD-19</h1>", unsafe_allow_html=True)
    
    st.subheader("MUERTES POR SEXO")
    porcentaje = [63.27,36.73]
    sexo = ["Masculino","Femenino"]
    colores = ["#60D394","#FFD97D"]
    plt.pie(porcentaje, labels=sexo, autopct="%0.1f %%", colors=colores)
    plt.axis("equal")
    plt.show()
    st.pyplot(plt)
    st.caption("Elaboración propia con datos del Ministerio de salud")
    
    st.subheader("MUERTES POR DEPARTAMENTO")
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    nombres = ['AMAZONAS','ÁNCASH','APURÍMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUÁNUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTÍN','TACNA','TUMBES','UCAYALI']
    datos = [1377,7365,1675,10621,2386,4552,10677,5321,1309,2956,9063,7651,11051,9352,95103,4437,882,1697,1133,13263,4948,3229,2200,1732,3294]
    xx = range(len(nombres))
    ax.bar(xx, datos, width=1, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres,rotation="vertical")
    plt.show()
    st.pyplot(plt)
    st.caption("Elaboración propia con datos del Ministerio de salud")
    
    
    text=st
    
    url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
    datos=pd.read_csv(url,sep=",")
    st.line_chart(data=datos, x="EDAD_DECLARADA", y="UUID")

    st.subheader("¿QUÉ CRITERIOS SE USARON PARA CONFIRMAR LA MUERTE POR COVID?")
    option = st.selectbox('ingresar criterio',('SINADEF', 'SEROLOGICO','VIROLOGICO'))
    st.write('Seleccionó:', option)
    
  
    
       
    
    
#if selected == 'Reportes':
    #st.markdown("<h1 style='text-align: center; color: black;'>Ministerio de Salud</h1>", unsafe_allow_html=True)
    
if selected == 'Equipo':
    st.markdown("<h1 style='text-align: center; color: black;'>Integrantes del Grupo</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Consuelo Gutierrez Lopez")
        st.image("consuelo.jpg")
    with col2:
        st.subheader("Melanie Malca Cruzado")
        st.image("conejo.jpg")
    with col3:
        st.subheader("Hilary Ramirez Castellares")
        st.image("pingui.jpg")
        
    
    

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



#tittle=st.text_input('Ingrese la opción que eligió')
#st.write("Número de teléfono o email de contecto:", tittle)







