
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
st.sidebar.success('Documentación y recopilación de datos de los registros diarios de muertes por Covid-19 del Ministerio de Salud')

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
    st.markdown("<h1 style='text-align: center; color: red;'>SITUACIÓN ACTUAL DEL COVID-19 EN EL PERÚ</h1>", unsafe_allow_html=True)
    st.subheader("¿QUÉ ES LA COVID-19?")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Una enfermedad infecciosa causada por el coronavirus SARS-CoV-2, que se propaga de persona a persona a través de gotitas, partículas acuosas o aerosoles expulsados por individuos infectados al momento de hablar, toser, estornudar, o incluso respirar. El virus puede ser inhalado por las personas que están cerca al enfermo y también puede contaminar cualquier tipo de superficie (pasamanos, mesas, lapiceros, entre otros), e ingresar al organismo cuando nos tocamos los ojos, nariz o boca con las manos sin lavar luego de haber tocado esas superficies contaminadas. Las personas mayores y las que sufren enfermedades respiratorias, diabetes o cardiopatías podrían desarrollar el virus en un nivel grave, si llegaran a contraerlo.")
    
    with col2:
        st.image("covid199.jpg")
        
    st.subheader("")

    col1, col2 = st.columns(2)
    
    st.subheader("")
    with col1:
        st.subheader("PREVENCIÓN")
        st.markdown("**Para prevenir la infección y frenar la transmisión de la COVID-19, haga lo siguiente:**")
        st.markdown("- Vacúnese cuando haya una vacuna disponible para usted.")
        st.markdown("- Manténgase al menos a 1 metro de distancia de los demás, aunque no parezcan estar enfermos.")
        st.markdown("- Utiilice una mascarilla bien ajustada cuando no sea posible el distanciamiento físico o cuando se encuentre en lugares mal ventilados.")
        st.markdown("- Elija los espacios abiertos y bien ventilados en lugar de los cerrados. Abra una ventana si está en el interior.")
        st.markdown("- Lávese las manos regularmente con agua y jabón o límpielas con un desinfectante de manos a base de alcohol.")
        st.markdown("- Cúbrase la boca y la nariz al toser o estornudar.")
        st.markdown("- Si se siente mal, quédese en casa y aíslese hasta que se recupere.")

       
    with col2:
        st.subheader("SÍNTOMAS")
        st.markdown("Según la OMS, La COVID-19 afecta a diferentes personas de forma distinta. La mayoría de las personas infectadas desarrollarán una enfermedad de leve a moderada y se recuperarán sin necesidad de hospitalización.") 
        st.markdown("**Síntomas más comunes:**")
        st.markdown("- Fiebre") 
        st.markdown("- Tos seca")
        st.markdown("- Cansansio") 
        st.markdown("- Perdida de olfato o gusto")
        st.markdown("**Síntomas graves**")
        st.markdown("- Dificultad para respirar") 
        st.markdown("- Pérdida del habla o la movilidad, o confusión")
        st.markdown("- Dolor en el pecho")
       

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("SALA SITUACIONAL COVID-19")
        st.markdown("**- Número total de personas muestreadas:** 36 561 147")
        st.markdown("**- Total de casos confirmados:** 4 278 977")
        st.markdown("**- Número de pruebas PCR(+):** 1 288 448")
        st.markdown("**- Número de pruebas rápidas(+):** 955 880")
        st.markdown("**- Número de pruebas Antigena:** 1 983 118")
        st.markdown("**- Fallecidos:** 217 428")
        st.markdown("**- Porcentaje de Letalidad:** 5.14%")
        st.markdown(" La disponibilidad de camas UCI con ventiladores en zona COVID-19")
        st.markdown(" durante el estado de emergencia sanitaria es de 518 hasta el día 27/11/22.")
        st.markdown("")
        st.markdown(" En la imagen se muestra la situación de la #COVID19 en Perú hasta las 22:00")
        st.markdown("horas del 1 de diciembre por el Ministerio de Salud")
    with col2:
        st.image("minsaa.jpeg")   
        st.caption("Fuente: Ministerio de Salud")
    
    
    #url 'https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
    #c = pd.read_csv(url, sep=',')
    #st.bar_chart(c)
    
    
if selected == 'Datos':
    st.image('ministerio.png')
    st.markdown("<h1 style='text-align: center; color: black;'>Fallecidos por Covid-19</h1>", unsafe_allow_html=True)
    st.subheader("Datos proporcionados por el Ministerio de Salud (MINSA)")
    st.info("Es el registro diario de muertes por Covid-19. Cada registro es igual a una persona, la cual puede caracterizarse por sexo, edad y ubicación geográfica hasta nivel de distrito; además, el 06.mayo.2021 se agregó el código UBIGEO. Desde que se publicó este dataset, cada registro representaba un fallecido confirmado por covid-19, quienes cumplen con criterios clínicos y de laboratorio (prueba molecular, antigénica o pruebas serológicas.")


    
    def download_data():
        url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv'
        filename="fallecidos_covid"
        urllib.request.urlretrieve(url,filename)
        df=pd.read_csv("fallecidos_covid")
        return df
    
    
    c=download_data()
    #st.write("dimensiones: "+str(c.shape[0])+"filas"+str(c.shape[1])+"columnas")
    st.subheader("Tabla de datos de fallecidos por Covid-19")
    st.dataframe(c)
    # CUADRO DE CARACTERÍSTICAS DEL DATASET
    st.subheader("Características del Dataset")
    st.write(c.describe())
    
   
    st.subheader("CASOS POSITIVOS DE COVID-19 EN PERÚ")
    
    def download():
        url='https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/casospositivo19.csv'
        filename="casospositivo19"
        urllib.request.urlretrieve(url,filename)
        df=pd.read_csv("casospositivo19")
        return df
    d=download()
    st.dataframe(d)
    st.caption("Fuente: Instituto Nacional de Salud y Centro Nacional de Epidemiología, Prevención y Control de Enfermedades - MINSA")
       

    
if selected == 'Información estadística':    
    st.markdown("<h1 style='text-align: center; color: black;'>INFORMACIÓN GRÁFICA DE LOS FALLECIDOS POR COVID-19</h1>", unsafe_allow_html=True)
    
    st.subheader("MUERTES POR SEXO")
    porcentaje = [63.27,36.73]
    sexo = ["Masculino","Femenino"]
    colores = ["#B0CFF8","#F8CFD9"]
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

 
    
    st.subheader("MUERTES MAYORES A:")
    number = st.number_input('insertar numero')
    st.write('usted escogio observar muertes de edad mayor a:', number)
    st.write(datos.loc[datos['EDAD_DECLARADA'] > number])

    
    st.subheader("MUERTES EN EL DEPARTAMENTO:")
    number = st.text_input('Ingrese el departamento')
    #st.write('usted escogio observar muertes de edad mayor a:', number)
    st.write(datos.loc[datos['DEPARTAMENTO'] = number])

    
#if selected == 'Reportes':
    #st.markdown("<h1 style='text-align: center; color: black;'>Ministerio de Salud</h1>", unsafe_allow_html=True)
    
if selected == 'Equipo':
    st.markdown("<h1 style='text-align: center; color: black;'>Integrantes del Grupo</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("¿Quiénes somos?")
        st.warning("Somos estudiantes de 5to ciclo de la carrera Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia. Realizamos este proyecto con el entusiasmo de qué otras personas puedan estar informadas sobre la situación actual del Covid-19 en el Perú; asimismo comunicar el impacto que tiene por el número de perdidas humanas por esta enfermeda. Es por ello que en la página se muestra algunas tablas y gráficos sobre los datos de fallecidos por Covid-19 del Ministerio de Salud.")
    with col2:
        st.image("ingamb.png")
        
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Consuelo Gutierrez Lopez")
        st.image("consuelo.jpg")
    with col2:
        st.subheader("Melanie Malca Cruzado")
        st.image("melanie.jpg")
    with col3:
        st.subheader("Hilary Ramirez Castellares")
        st.image("hilarypreciosisima.jpeg")
        
    
    

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







