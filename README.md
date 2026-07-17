# Explorador Compra Ágil

Aplicación desarrollada en **Python + Streamlit** para facilitar la búsqueda de oportunidades de Compra Ágil en Mercado Público utilizando la API oficial. Permite filtrar resultados por región, tipo de llamado y fecha de publicación, además de exportar la información a Excel para su posterior análisis.

## 🚀 Demo

https://TU-APP.streamlit.app

## ✨ Funcionalidades

- Consulta la API oficial de Compra Ágil.
- Filtro por región.
- Filtro por Primer o Segundo Llamado.
- Filtro opcional por fecha de publicación.
- Exclusión automática de rubros definidos por palabras clave.
- Exportación de resultados a Excel.
- Acceso directo a la ficha de cada compra.

## 🛠️ Tecnologías

- Python
- Streamlit
- Requests
- Pandas
- OpenPyXL

## 📦 Instalación

```bash
git clone https://github.com/M-Munoz-cl/explorador-compra-agil.git
cd explorador-compra-agil
pip install -r requirements.txt
```

Crear un archivo `.env`:

```env
TICKET=TU_TICKET
```

Ejecutar la aplicación:

```bash
streamlit run src/app.py
```

## 📋 Roadmap

- Base de datos PostgreSQL para historial de compras.
- Dashboard con estadísticas.
- Búsqueda avanzada.
- Sistema de scoring de oportunidades.
- Nuevos filtros y mejoras de interfaz.

## 📄 Licencia

Proyecto desarrollado con fines educativos y de apoyo al análisis de oportunidades en Mercado Público.