import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# 1. CONFIGURACIÓN DE LA PÁGINA (Primera instrucción)
# =====================================================
st.set_page_config(
    page_title="Gabriel Mena | Portafolio Streamlit",
    page_icon="📊",
    layout="wide"
)

# Configuración de estilos globales para gráficos estáticos
sns.set_theme(style="whitegrid")

# Inicializar el estado de la aplicación para persistencia de datos entre páginas
if 'df' not in st.session_state:
    st.session_state['df'] = None

# =====================================================
# SIDEBAR / NAVEGACIÓN
# =====================================================
st.sidebar.title("📂 Gabriel Mena López")

pagina = st.sidebar.radio(
    "Seleccione una sección",
    [
        "🏠 Home",
        "📂 2. Carga y Perfil",
        "⚙️ 3. Procesamiento",
        "📊 4. Análisis Visual"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("**Gabriel Andrés Mena López**")
st.sidebar.write("Business Intelligence & Data Analytics")
st.sidebar.write("📩 gmena50@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/andresmena1/)")


# =====================================================
# SECCIÓN 1: HOME
# =====================================================
if pagina == "🏠 Home":
    st.title("📊 Portafolio Profesional: Data Analytics App")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Presentación del Proyecto")
        st.write("""
        Esta es una **Aplicación Interactiva** construida íntegramente en **Python con Streamlit**. 
        El objetivo es demostrar la capacidad de procesar, limpiar y analizar visualmente diversos conjuntos de datos 
        de manera automatizada y dinámica.
        """)
        
        st.subheader("El Objetivo")
        st.info("""
        Construir una app en Streamlit capaz de procesar cualquiera de los cuatro datasets propuestos, 
        mostrando secciones de presentación, carga/procesamiento de datos y análisis visual mediante 
        gráficos interactivos.
        """)

        st.subheader("Tecnologías usadas")
        st.code("Python, Excel, github, Streamlit, Pandas, Plotly, Seaborn, Matplotlib")

    with col2:
        st.header("Datos del Autor")
        st.markdown(f"### **Gabriel Andrés Mena López**")
        st.caption("Instituto DMC")
        st.write("""
        Profesional con amplia experiencia en el sector de hidrocarburos y GLP, especializado en análisis 
        comercial, inteligencia de negocios y gestión de información para la toma de decisiones. Cuento con 
        sólidos conocimientos de la cadena comercial de combustibles, normativa regulatoria del mercado 
        peruano y funcionamiento operativo del Sistema de Control de Órdenes de Pedido (SCOP).
        """)

    st.divider()
    
    st.header("Descripción de los cuatro datasets")
    d1, d2, d3, d4 = st.columns(4)
    
    with d1:
        st.markdown("📂 **Data 1: AI_Impact_on_Jobs_2030.csv**")
        st.caption("Mercado laboral e impacto de la inteligencia artificial en empleos, salarios, habilidades y demanda futura.")
    with d2:
        st.markdown("📂 **Data 2: sample_-_superstore.csv**")
        st.caption("Ventas de una tienda: pedidos, clientes, regiones, categorías, ventas, descuentos y utilidad.")
    with d3:
        st.markdown("📂 **Data 3: synthetic_ecommerce_order_risk_dataset.csv**")
        st.caption("Pedidos de e-commerce con variables de país, dispositivo, método de pago, valor de orden, entrega, devolución, fraude y etiqueta de riesgo.")
    with d4:
        st.markdown("📂 **Data 4: Teen_Mental_Health_Dataset.csv**")
        st.caption("Hábitos digitales, sueño, actividad física, interacción social y variables de bienestar en adolescentes.")


# =====================================================
# SECCIÓN 2: CARGA Y PERFIL
# =====================================================
elif pagina == "📂 2. Carga y Perfil":
    st.title("📂 Carga y Perfil del Dataset")
    st.write("Permitir cargar el archivo CSV con st.file_uploader() o seleccionar uno de los datasets del proyecto. Mostrar vista previa, dimensiones, columnas, tipos de datos y resumen inicial.")
    
    st.divider()
    opcion_carga = st.radio("Seleccione el origen del archivo:", ["Subir mi propio CSV", "Seleccionar un Dataset del Proyecto"], horizontal=True)
    
    df_cargado = None

    if opcion_carga == "Subir mi propio CSV":
        archivo = st.file_uploader("Cargar dataset (CSV)", type=["csv"])
        if archivo:
            df_cargado = pd.read_csv(archivo)
    else:
        dataset_selec = st.selectbox("Elija uno de los datasets predefinidos:", [
            "AI_Impact_on_Jobs_2030.csv", 
            "sample_-_superstore.csv", 
            "synthetic_ecommerce_order_risk_dataset.csv", 
            "Teen_Mental_Health_Dataset.csv"
        ])
        
        try:
            df_cargado = pd.read_csv(dataset_selec)
        except Exception as e:
            st.error(f"Archivo '{dataset_selec}' no encontrado en el directorio local. Por favor, utiliza la opción 'Subir mi propio CSV'.")

    if df_cargado is not None:
        st.session_state['df'] = df_cargado
        st.success("¡Dataset cargado correctamente!")
        
        tab_preview, tab_resumen = st.tabs(["👀 Vista Previa y Estructura", "📊 Resumen Inicial"])
        
        with tab_preview:
            st.subheader("Vista Previa del Dataset")
            st.dataframe(df_cargado.head(10), use_container_width=True)
            
            c1, c2 = st.columns(2)
            c1.metric("Dimensiones de la Data", f"{df_cargado.shape[0]} filas x {df_cargado.shape[1]} columnas")
            with c2:
                st.write("**Columnas y Tipos de Datos:**")
                st.dataframe(df_cargado.dtypes.astype(str).to_frame(name="Tipo"), use_container_width=True)

        with tab_resumen:
            st.subheader("Estadísticas Descriptivas Iniciales")
            st.write(df_cargado.describe(include='all'))
    else:
        st.info("A la espera de un archivo. Sube o selecciona un dataset en la parte superior.")


# =====================================================
# SECCIÓN 3: PROCESAMIENTO
# =====================================================
elif pagina == "⚙️ 3. Procesamiento":
    st.title("⚙️ Procesamiento de Datos")
    st.write("Detectar variables numéricas, categóricas y fechas. Validar datos nulos, duplicados, valores no válidos y aplicar conversiones de fecha o limpieza básica cuando corresponda.")
    
    st.divider()

    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Detección Automática de Variables")
            
            # Saneo para Python 3.14 (evita strings que rompen select_dtypes)
            num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
            date_cols = df.select_dtypes(include=['datetime64[ns]']).columns.tolist()
            
            st.write(f"🔢 **Variables Numéricas:** {', '.join(num_cols) if num_cols else 'Ninguna'}")
            st.write(f"🔤 **Variables Categóricas:** {', '.join(cat_cols) if cat_cols else 'Ninguna'}")
            st.write(f"📅 **Variables de Tipo Fecha:** {', '.join(date_cols) if date_cols else 'Ninguna'}")

        with col2:
            st.subheader("Validación de Calidad de Datos")
            nulos_totales = df.isnull().sum().sum()
            duplicados_totales = df.duplicated().sum()
            
            st.write(f"❓ **Total celdas nulas:** {nulos_totales}")
            st.write(f"👯 **Total registros duplicados:** {duplicados_totales}")
        
        st.divider()
        st.subheader("Herramientas de Limpieza Básica")
        
        c1, c2, c3 = st.columns(3)
        if c1.button("🧼 Eliminar Duplicados"):
            df_limpio = df.drop_duplicates()
            st.session_state['df'] = df_limpio
            st.success("¡Registros duplicados eliminados con éxito!")
            st.rerun()
            
        if c2.button("🩹 Imputar Nulos (Media / Moda)"):
            df_limpio = df.copy()
            for col in df_limpio.columns:
                if df_limpio[col].dtype in [np.float64, np.int64]:
                    df_limpio[col] = df_limpio[col].fillna(df_limpio[col].mean())
                else:
                    if not df_limpio[col].mode().empty:
                        df_limpio[col] = df_limpio[col].fillna(df_limpio[col].mode()[0])
            st.session_state['df'] = df_limpio
            st.success("¡Valores nulos sustituidos convenientemente!")
            st.rerun()
            
        with c3:
            columna_parsear = st.selectbox("Convertir columna de texto a Fecha:", ["Seleccionar"] + cat_cols)
            if columna_parsear != "Seleccionar":
                if st.button("📅 Aplicar Conversión"):
                    df_limpio = df.copy()
                    df_limpio[columna_parsear] = pd.to_datetime(df_limpio[columna_parsear], errors='coerce')
                    st.session_state['df'] = df_limpio
                    st.success(f"¡Columna '{columna_parsear}' transformada a datetime!")
                    st.rerun()
    else:
        st.error("No se detectó ningún dataset activo. Por favor, ve primero a la sección '📂 2. Carga y Perfil'.")


# =====================================================
# SECCIÓN 4: ANÁLISIS VISUAL
# =====================================================
elif pagina == "📊 4. Análisis Visual":
    st.title("🚀 Advanced Analytics Dashboard")
    st.write("Sección ANALIZA TU DATA: Organizada mediante pestañas (tabs) y columnas para gráficos univariados, bivariados, multivariados y temporales con Plotly, Matplotlib y Seaborn.")
    
    st.divider()

    if st.session_state['df'] is not None:
        df = st.session_state['df']
        
        # Mapeo de columnas por tipología
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

        # Render de las 5 pestañas solicitadas
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Exploración",
            "🔍 Calidad de Datos",
            "📉 Visualización Avanzada",
            "🤖 Análisis Estadístico",
            "⚠️ Detección de Anomalías",
        ])

        # --- TAB 1: EXPLORACIÓN ---
        with tab1:
            st.subheader("Vista Previa del Dataset")
            st.dataframe(df.head(10), use_container_width=True)
            st.write(f"Dimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")

        # --- TAB 2: CALIDAD DE DATOS ---
        with tab2:
            st.subheader("🔍 Auditoría de Calidad de Datos")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Filas", df.shape[0])
            col2.metric("Total Columnas", df.shape[1])
            duplicados = df.duplicated().sum()
            col3.metric(
                "Filas Duplicadas",
                duplicados,
                delta_color="inverse" if duplicados > 0 else "normal",
            )

            st.divider()

            st.subheader("Diagnóstico de Nulos")
            nulos_por_col = df.isnull().sum()
            nulos_activos = nulos_por_col[nulos_por_col > 0]

            if not nulos_activos.empty:
                st.warning(f"Se encontraron valores nulos en {len(nulos_activos)} columnas.")
                st.bar_chart(nulos_activos)
            else:
                st.success("¡Integridad de datos: Sin valores nulos detectados!")
                datos_cero = pd.DataFrame({"Nulos": 0}, index=df.columns)
                st.bar_chart(datos_cero)
                st.info("La ausencia de barras confirma que el dataset está completo.")

        # --- TAB 3: VISUALIZACIÓN AVANZADA ---
        with tab3:
            st.subheader("Suite de Visualización")
            tipo_graf = st.radio(
                "Seleccionar tipo de gráfico",
                [
                    "Relación (Plotly)",
                    "Distribución (Seaborn)",
                    "Correlación (Heatmap)",
                    "Boxplot (Outliers)",
                    "Densidad (Skew/Kurt)",
                ],
                horizontal=True,
                key="tipo_graf_suite"
            )

            c1, c2 = st.columns(2)
            with c1:
                col_x = st.selectbox("Eje X", df.columns, key="v_suite_x")
            with c2:
                # Evita error inicial de duplicación forzando un índice diferente por defecto si existe
                default_idx = 1 if len(num_cols) > 1 else 0
                col_y = st.selectbox("Eje Y (Numérico)", num_cols, index=default_idx, key="v_suite_y")

            if tipo_graf == "Relación (Plotly)":
                if col_x == col_y:
                    st.warning("⚠️ Selecciona columnas diferentes para el Eje X y el Eje Y para evitar conflictos de procesamiento en los componentes gráficos.")
                else:
                    fig = px.scatter(
                        df, x=col_x, y=col_y,
                        color=df.columns[0],
                        template="plotly_white",
                    )
                    st.plotly_chart(fig, use_container_width=True)

            elif tipo_graf == "Distribución (Seaborn)":
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.histplot(df[col_y], kde=True, color="teal", ax=ax)
                st.pyplot(fig)

            elif tipo_graf == "Correlación (Heatmap)":
                if len(num_cols) >= 2:
                    corr = df[num_cols].corr()
                    mask = np.triu(np.ones_like(corr, dtype=bool))
                    fig, ax = plt.subplots(figsize=(10, 8))
                    sns.heatmap(
                        corr, mask=mask, annot=True,
                        cmap="coolwarm", fmt=".2f",
                        ax=ax, square=True,
                    )
                    st.pyplot(fig)
                else:
                    st.warning("Se necesitan al menos 2 variables numéricas para estructurar una matriz de correlación.")

            elif tipo_graf == "Boxplot (Outliers)":
                fig = px.box(df, y=col_y, title=f"Outliers: {col_y}", template="plotly_white")
                st.plotly_chart(fig, use_container_width=True)

            elif tipo_graf == "Densidad (Skew/Kurt)":
                from scipy.stats import shapiro

                skew = df[col_y].skew()
                kurt = df[col_y].kurt()
                
                # Saneo para Shapiro: Muestreo si supera los 5000 registros para evitar crasheos de scipy
                df_clean = df[col_y].dropna()
                if len(df_clean) > 5000:
                    df_clean = df_clean.sample(5000, random_state=42)
                
                stat, p = shapiro(df_clean)

                fig, ax = plt.subplots(figsize=(10, 4))
                sns.kdeplot(df[col_y], fill=True, color="purple", ax=ax)
                ax.set_title(
                    f"Normalidad: P-value {p:.4f} | Skew: {skew:.2f} | Kurt: {kurt:.2f}"
                )
                st.pyplot(fig)

        # --- TAB 4: ANÁLISIS ESTADÍSTICO ---
        with tab4:
            st.subheader("Resumen Estadístico Profundo")
            resumen = df.describe().T
            resumen["skew"] = df.skew(numeric_only=True)
            resumen["kurt"] = df.kurt(numeric_only=True)
            st.dataframe(resumen, use_container_width=True)

        # --- TAB 5: DETECCIÓN DE ANOMALÍAS ---
        with tab5:
            st.subheader("⚠️ Detección Automática de Anomalías")
            umbral = st.slider(
                "Seleccionar umbral de Z-Score (sensibilidad)", 1.5, 3.5, 3.0, key="sensibilidad_z"
            )
            col_outlier = st.selectbox(
                "Seleccionar columna para buscar anomalías",
                num_cols,
                key="outlier_target"
            )

            if col_outlier:
                if df[col_outlier].std() == 0:
                    st.error("No es posible calcular anomalías en una columna con varianza o desviación estándar igual a cero.")
                else:
                    z_scores = np.abs(
                        (df[col_outlier] - df[col_outlier].mean()) / df[col_outlier].std()
                    )
                    anomalies = df[z_scores > umbral]

                    if not anomalies.empty:
                        st.warning(f"Se detectaron {len(anomalies)} filas fuera del rango estadístico.")
                        st.dataframe(anomalies, use_container_width=True)
                        csv = anomalies.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            "Descargar Anomalías (CSV)", csv, "anomalias.csv", "text/csv"
                        )
                    else:
                        st.success("¡No se detectaron anomalías significativas con este umbral!")
    else:
        st.error("No hay datos para analizar. Vaya primero a la sección '2. Carga y Perfil'.")
