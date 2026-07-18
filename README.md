# Mercado Público Tools

Aplicación desarrollada en **Python + Streamlit** para facilitar el trabajo diario con procesos de **Compra Ágil de Mercado Público**.

Actualmente integra un buscador de oportunidades mediante la API oficial y un generador de fichas técnicas en PDF para apoyar la preparación de ofertas.

---

## Demo

https://explorador-compra-agil-2kmvfenrmtigp3nsn75x5c.streamlit.app/

---

# Funcionalidades

## Buscador de Compras Ágiles

- Consulta la API oficial de Compra Ágil.
- Filtro por región.
- Filtro por Primer y Segundo Llamado.
- Filtro por fecha de publicación.
- Exclusión automática mediante palabras clave.
- Acceso directo a la ficha de Mercado Público.
- Exportación de resultados a Excel.

---

## Generador de Fichas Técnicas

Herramienta para crear fichas técnicas en PDF.

Incluye:

- Ingreso de título.
- Imagen mediante carga desde el computador.
- Imagen mediante botón para pegar.
- Vista previa en tiempo real.
- Ajuste automático de títulos largos.
- Escalado proporcional de imágenes.
- Descripciones multipágina.
- Conservación de párrafos.
- Descarga inmediata del PDF.
- Generación consecutiva de múltiples fichas.

---

# Tecnologías

- Python
- Streamlit
- Requests
- Pandas
- OpenPyXL
- ReportLab
- Pillow
- streamlit-paste-button

---

# Instalación

Clonar el repositorio

```bash
git clone https://github.com/M-Munoz-cl/explorador-compra-agil.git
cd explorador-compra-agil
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear un archivo `.env`

```env
TICKET=TU_TICKET
```

Ejecutar la aplicación

```bash
streamlit run streamlit_app.py
```

---

# Estructura del proyecto

```

├── pages/
│   ├── buscador.py
│   └── generador_fichas.py
│
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── config.py
│   ├── formato_excel.py
│   └── ...
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# Arquitectura

El proyecto sigue una separación simple de responsabilidades.

### streamlit_app.py

Punto de entrada de la aplicación.

Se encarga únicamente de:

- configurar Streamlit
- registrar las páginas
- manejar la navegación

---

### pages/

Contiene toda la interfaz gráfica.

Ejemplo:

```
pages/
```

- buscador.py
- generador_fichas.py

Aquí se encuentran los componentes de Streamlit:

- botones
- tablas
- formularios
- gráficos
- navegación

Las páginas consumen funciones desde `src`, evitando duplicar lógica.

Ejemplo:

```python
from src.api import obtener_datos
```

---

### src/

Contiene únicamente la lógica del proyecto.

Ejemplo:

- conexión con la API
- filtros
- exportación
- configuración
- funciones reutilizables

Los módulos internos utilizan imports relativos.

Ejemplo:

```python
from .config import BASE_URL, HEADERS
```

Con esto se mantiene una separación clara entre la interfaz y la lógica de negocio.

---

# Roadmap

## Buscador

- Base de datos PostgreSQL.
- Dashboard.
- Nuevos filtros.

## Herramientas

- Logo configurable.
- Pie de página institucional.
- Generación automática de especificaciones técnicas.

---

# Objetivo

Construir una plataforma que centralice distintas herramientas para proveedores de Mercado Público, facilitando la búsqueda de oportunidades, la generación de documentación técnica y la preparación de ofertas desde una única aplicación.

---

# Licencia

Proyecto desarrollado con fines educativos y como herramienta de apoyo para proveedores que participan en procesos de Compra Ágil de Mercado Público.