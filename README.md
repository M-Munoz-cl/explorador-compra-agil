# 🛒 Mercado Público Compra Ágil Explorer

Aplicación desarrollada en **Python y Streamlit** que utiliza la **API oficial de Compra Ágil de Mercado Público** para facilitar la búsqueda y revisión de oportunidades.

La motivación principal del proyecto surge porque el buscador oficial no permite filtrar las compras por **primer** o **segundo llamado**, obligando a revisar manualmente cada oportunidad.

Mediante el consumo de la API oficial fue posible incorporar este filtro y, además, agregar otras funcionalidades orientadas a mejorar la productividad durante la revisión de compras.

Este proyecto también sirve como práctica personal para aprender desarrollo backend, consumo de APIs y construcción de aplicaciones con Python.

# 🎯 Objetivo

El objetivo del proyecto es complementar el buscador oficial de Mercado Público mediante una aplicación que permita realizar búsquedas más rápidas y cómodas incorporando filtros que actualmente no están disponibles en el sitio web.

Entre ellos:

- Filtrar por primer o segundo llamado.
- Exportar resultados a Excel.
- Acceder rápidamente a la ficha oficial de cada compra.

## Instalación

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear un archivo `.env` en la raíz del proyecto:

```env
TICKET=TU_TICKET_AQUI
```

Ejecutar la aplicación:

```bash
streamlit run src/app.py
```