import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURACIÓN
# ==========================================
st.set_page_config(
    page_title="Gabriel Mena | BI Portfolio",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.title("📌 Menú")
st.sidebar.info("Portafolio Profesional")

# ==========================================
# ENCABEZADO
# ==========================================
st.title("👨‍💼 Gabriel Mena López")
st.subheader("Business Intelligence | Data Analytics | Python")

st.write(
    """
    Profesional con experiencia en análisis de datos, indicadores de gestión,
    Business Intelligence y automatización de reportes.
    """
)

# ==========================================
# PERFIL
# ==========================================
col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=180
    )

with col2:
    st.markdown("""
    ### Perfil Profesional

    ✔ Análisis de datos y Business Intelligence

    ✔ Python, SQL, Power BI y Excel

    ✔ Dashboards y KPIs

    ✔ Machine Learning e Inteligencia Artificial

    ✔ Análisis comercial y exportaciones
    """)

# ==========================================
# EXPERIENCIA
# ==========================================
st.header("💼 Experiencia")

st.write("""
**OSINERGMIN**

- Monitoreo y validación de información.
- Elaboración de reportes ejecutivos.
- Atención a usuarios y soporte operativo.
- Seguimiento de indicadores.
""")

# ==========================================
# HABILIDADES
# ==========================================
st.header("🛠 Habilidades")

st.write("Excel")
st.progress(90)

st.write("Power BI")
st.progress(85)

st.write("Python")
st.progress(80)

st.write("SQL")
st.progress(75)

st.write("Machine Learning")
st.progress(65)

# ==========================================
# PROYECTOS
# ==========================================
st.header("📊 Proyectos")

st.markdown("""
### Acceso a la Salud en Perú
- Regresión logística
- Correlaciones
- ENAHO

### Análisis de Exportaciones
- Dashboards comerciales
- Tendencias de mercado

### Business Intelligence
- KPIs
- Automatización de reportes
""")

# ==========================================
# MATRIZ DE CORRELACIÓN (EJEMPLO)
# ==========================================
st.header("📈 Matriz de Correlación")

# Datos de ejemplo
datos = {
    "Python": [75,80,85,90,95],
    "SQL": [70,75,80,85,90],
    "PowerBI": [65,72,78,88,92],
    "Excel": [80,85,90,95,100]
}

df = pd.DataFrame(datos)

corr = df.corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

fig, ax = plt.subplots(figsize=(6,5))

im = ax.imshow(
    np.ma.masked_where(mask, corr),
    aspect="auto"
)

ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45)

ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)

plt.colorbar(im)

st.pyplot(fig)

# ==========================================
# CONTACTO
# ==========================================
st.header("📞 Contacto")

st.write("🌎 Lima, Perú")
st.write("🐙 GitHub: github.com/Andres2150")
st.write("💼 LinkedIn: linkedin.com/in/gabrielmena")

st.success("Gracias por visitar mi portafolio.")
