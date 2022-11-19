import streamlit as st
import pandas as pd
import numpy as np

st.title("Proyecto Programación 2022-2")
st.title("Fallecidos por covid")
st.write("hola cons")
num= st.slider("num", 0, 100, step=1)
st.write("El numero ingresado es {}".format(num))
st.line_chart()

st.title()
st.write()
st.line_chart()
