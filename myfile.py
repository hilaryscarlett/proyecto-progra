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


###
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
