import pandas as pd
import numpy as np
import plotly.express as px

excel_file="fallecidos_covid.xslx"
sheet_name="fallecidos_covid"
df=pd.read_excel(excel_file,
                sheet_name=sheet_name
                usecols="D:G",
                header=2)
df_dato1=df.groupby(["SEXO"], as_index=false)["PROVINCIA"].count()
df_datos12=df_dato1
st.dataframe(df)
st.write(df_datos12)
pie_chart=px.pie(df_datos12,
                 title="ola1",
                 values="ola2",
                 names="SEXO")
st.plotly_chart(pie_chart)
