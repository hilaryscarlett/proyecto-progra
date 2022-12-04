#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import urllib.request



df_prueba = lectura('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid.csv') 
st.write(df_prueba)

st.write(df_prueba.iloc[0])















