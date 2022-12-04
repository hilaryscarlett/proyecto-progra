def lectura(a):
    df = pd.read_csv(a, parse_dates = ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
    return df

st.subheader("escoje departamento")
df_prueba2=lectura('https://raw.githubusercontent.com/hilaryscarlett/proyecto-progra/main/fallecidos_covid_2.csv')

option = st.selectbox('ingresar criterio',('LIMA','AMAZONAS'))     #STRING QUE GUARDA MI SELECCION ENTRE COMILLAS
st.write(df_prueba2['EDAD_DECLARADA']['UBIGEO'][option])
