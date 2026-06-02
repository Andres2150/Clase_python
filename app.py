import streamlit as st

st.title("Proyecto final Diploma BI")

st.sidebar.title("Parametros")

st.sidebar.image("dmc.jpg", use_container_width=True)
st.write("Elaborado por Gabriel Mena")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título
st.title("🏥 Acceso a la Salud en el Perú")
st.subheader("Ejemplo de análisis ENAHO 2020")

# Cargar archivo
archivo = st.file_uploader(
    "Cargar archivo Excel",
    type=["xlsx"]
)

if archivo:

    df = pd.read_excel(archivo)

    # Vista previa
    st.write("### Vista previa de los datos")
    st.dataframe(df.head())

    # Seleccionar variable numérica
    variable = st.selectbox(
        "Seleccione una variable numérica",
        df.select_dtypes(include="number").columns
    )

    # Estadísticas básicas
    st.write("### Estadísticas")
    st.write(df[variable].describe())

    # Histograma
    st.write("### Distribución")
    fig, ax = plt.subplots()

    sns.histplot(
        df[variable],
        kde=True,
        ax=ax
    )

    st.pyplot(fig)

else:
    st.info("Cargue un archivo Excel para comenzar.")
```
