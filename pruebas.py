import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['provincia', 'distrito'])

st.map(df)


