# importar streamlit
import streamlit as st
# importamos la funcion obtener datos de nuestro api.py
from src.api import obtener_datos
from datetime import datetime, date, timedelta
from src.formato_excel import dar_formato
import pandas as pd
import io

# Fechas

filtrar_por_fecha = st.checkbox(
    "Filtrar por fecha de publicación"
)

if filtrar_por_fecha:
    fecha_inicio = st.date_input(
        "Desde",
        value=date.today(),
        max_value=date.today()
    )

    fecha_fin = st.date_input(
        "Hasta",
        value=date.today(),
        max_value=date.today()
    )

    if fecha_inicio > fecha_fin:
        st.error("La fecha inicial no puede ser mayor que la fecha final.")
        st.stop()

else:
    fecha_inicio = None
    fecha_fin = None

# equivalente a un h1 de html (cada vez que se abra la pagina se vera ese titulo)
st.title("Buscador de Compras Ágiles")

# Inicializar el Session State para guardar los datos entre clics
if "datos_busqueda" not in st.session_state:
    st.session_state.datos_busqueda = None

#diccionario con regiones 
REGIONES = {
    "Arica y Parinacota": 15,
    "Tarapacá": 1,
    "Antofagasta": 2,
    "Atacama": 3,
    "Coquimbo": 4,
    "Valparaíso": 5,
    "Metropolitana": 13,
    "O'Higgins": 6,
    "Maule": 7,
    "Ñuble": 16,
    "Biobío": 8,
    "La Araucanía": 9,
    "Los Ríos": 14,
    "Los Lagos": 10,
    "Aysén": 11,
    "Magallanes": 12
}

LLAMADOS = {
    "Primer Llamado" : 1,
    "Segundo Llamado": 2
}

# creamos y mostramos el selectbox donde el texto seran las claves del diccionario (nombres)
region_nombre = st.selectbox(
    "Region",
    REGIONES.keys()
)

# aca obtenemso el numero. Si el usuario elige tarapaca , region valdra 1 (esto ya que region nombre almacena el nombre de la region)
region = REGIONES[region_nombre]

llamado_nombre = st.selectbox(
    "Llamado",
    LLAMADOS.keys()
)

llamado = LLAMADOS[llamado_nombre]

if st.button("Buscar"):

    with st.spinner("Buscando oportunidades..."):
        
        oportunidades = obtener_datos(region, llamado, fecha_inicio, fecha_fin)

    if not oportunidades:
        st.warning(
            "No fue posible obtener datos de Mercado Público. "
            "Intenta nuevamente en unos minutos."
        )
    else:
        st.success(f"Se encontraron {len(oportunidades)} oportunidades")

    datos = []

    for item in oportunidades:

        datos.append(
            {"Codigo": item["codigo"],
             "Nombre": item["nombre"],
             "Organismo": item["institucion"]["organismo_comprador"],
             "Presupuesto": item['montos']['monto_disponible_clp'],
             "Fecha de cierre": item["fecha_cierre_mostrar"],
             "Ofertas": f"https://buscador.mercadopublico.cl/ficha?code={item['codigo']}"}
        )
    
    st.session_state.datos_busqueda = datos
    #st.dataframe(datos)

# Si ya existen datos guardados en la sesion , los mostramos y habilitamos la exportacion
if st.session_state.datos_busqueda is not None:
    # Convertimos a DataFrame
    df = pd.DataFrame(st.session_state.datos_busqueda)

    # Convertimos la fecha desde texto a datetime real
    df["Fecha de cierre"] = pd.to_datetime(
        df["Fecha de cierre"],
        format="%d-%m-%Y %H:%M",
        errors="coerce"
    )

    # Mostramos tabla
    st.dataframe(
        df,
        hide_index=True,
        width="stretch",
        column_config={
            "Ofertas": st.column_config.LinkColumn(
                "Ofertas",
                display_text="🔗 Revisar"
            ),
            "Presupuesto": st.column_config.NumberColumn(
                "Presupuesto",
                format="$%d"
            ),
            "Fecha de cierre": st.column_config.DatetimeColumn(
                "Fecha de cierre",
                format="DD-MM-YYYY HH:mm"
            )
        }
    )

    # Crear buffer para almacenar el Excel en memoria
    buffer = io.BytesIO()

    # Escribe el Excel dentro del buffer
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Informe")
        ws = writer.sheets["Informe"]
        dar_formato(ws)

    nombre_archivo = f"reporte_{datetime.now():%Y%m%d_%H%M%S}.xlsx"

    st.download_button(
        label="Descargar Excel",
        data=buffer.getvalue(),
        file_name=nombre_archivo,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )