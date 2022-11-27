import pandas as pd
import numpy as np
import plotly.express as px


excel_file="fallecidos_covid.xslx"
sheetname="fallecidos_covid"
df = pd.read_excel(excel_file,
