import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title("Proyecto Programación 2022-2")
st.title("                Fallecidos por covid              ")

d= st.date_input("ingresar fecha de fallecimiento", datetime.data(2019, 7, 6))
st.write("fecha de fallecieminto es")

