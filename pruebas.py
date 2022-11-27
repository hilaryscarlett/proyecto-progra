import pandas as pd
import numpy as np



with st.sidebar:
  selected=option_menu(
    menu_title = "Menú",
    options=["inicio","local","reported","equipo"],
    icons=["house","map","book","people"],
    menu_icon="cast",
    default_index =0,
  )
  
