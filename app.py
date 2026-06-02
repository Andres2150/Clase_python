import streamlit as st

st.title("Proyecto final Diploma BI")

st.sidebar.title("Parametros")

st.write("Elaborado por Gabriel Mena")

import streamlit as st

# Configuración
st.set_page_config(
    page_title="Gabriel Mena | CV",
    page_icon="📊",
    layout="wide"
)

# Encabezado
st.title("👨‍💼 Gabriel Mena López")
st.subheader("Analista de Negocios | Business Intelligence | Data Analytics")

st.markdown("""
Profesional con experiencia en análisis de datos, monitoreo de información,
atención a usuarios y generación de reportes para la toma de decisiones.
Actualmente enfocado en Business Intelligence, Python, Machine Learning y análisis comercial.
""")

# Columnas
col1, col2 = st.columns([1,2])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=180)

with col2:
    st.markdown("""
### 📌 Perfil Profesional

- Experiencia en análisis y validación de datos.
- Conocimiento de Python, SQL, Power BI y Excel.
- Desarrollo de dashboards e indicadores de gestión.
- Interés en inteligencia artificial y analítica avanzada.
- Orientado a la mejora de procesos y toma de decisiones basada en datos.
""")

# Experiencia
st.header("💼 Experiencia Profesional")

st.markdown("""
**OSINERGMIN**

- Monitoreo y validación de información relacionada con hidrocarburos líquidos.
- Elaboración de reportes e indicadores.
- Atención y resolución de consultas a nivel nacional.
- Seguimiento de incidencias técnicas y operativas.
""")

# Habilidades
st.header("🛠️ Habilidades")

st.progress(90, text="Excel")
st.progress(80, text="Power BI")
st.progress(75, text="Python")
st.progress(70, text="SQL")
st.progress(60, text="Machine Learning")

# Proyectos
st.header("📊 Proyectos Destacados")

st.markdown("""
### 1. Acceso a la Salud en el Perú (ENAHO)
- Correlación y regresión logística.
- Identificación de factores que influyen en el acceso a consultas médicas.

### 2. Análisis de Exportaciones
- Visualización de tendencias comerciales.
- Construcción de dashboards ejecutivos.

### 3. Business Intelligence
- Automatización de reportes.
- Indicadores KPI y storytelling con datos.
""")

# Formación
st.header("🎓 Formación")

st.markdown("""
- Diplomado en Business Intelligence.
- Cursos de Python para Ciencia de Datos.
- Formación en análisis comercial y exportaciones.
- Capacitación continua en Inteligencia Artificial.
""")

# Contacto
st.header("📞 Contacto")

st.write("📧 correo@ejemplo.com")
st.write("🌎 Lima, Perú")
st.write("💼 LinkedIn: linkedin.com/in/gabrielmena")
st.write("🐙 GitHub: github.com/Andres2150")

st.success("Gracias por visitar mi perfil profesional.")
