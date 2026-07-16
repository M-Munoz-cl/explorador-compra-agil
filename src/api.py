# para solicitud
import requests
from config import BASE_URL, HEADERS
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

PALABRAS_EXCLUIDAS = [
    "servicio",
    "mantención",
    "mantencion",
    "mantenimiento",
    "reparación",
    "reparacion",
    "instalación",
    "instalacion",
    "seguro",
    "traslado",
    "examen",
    "medicamento"
]

def obtener_pagina(region, numero_pagina):
    response = requests.get(
        f"{BASE_URL}/v2/compra-agil",
        headers=HEADERS,
        params={
            "ttl_cambio_ms": 2592000000,
            "tamano_pagina": 20,
            "numero_pagina": numero_pagina,
            "estado": "publicada",
            "region": region
        },
        timeout=30
    )

    if response.status_code != 200:
        print(f"Error HTTP {response.status_code}")
        return [], {}
    
    data = response.json()

    if "payload" not in data:
        print("La API respondió sin payload")
        return [], {}
    
    return (
        data["payload"]["items"],
        data["payload"]["paginacion"]
    )

def obtener_datos(region, llamado, fecha_inicio, fecha_fin):
    compras_filtradas = []

    items, paginacion = obtener_pagina(region, 1)

    if not paginacion:
        return []

    total_paginas = paginacion["total_paginas"]
    print(f"Total páginas: {total_paginas}")

    todos_los_items = list(items)

    with ThreadPoolExecutor(max_workers=20) as executor:

        resultados = executor.map(
            obtener_pagina,
            [region] * (total_paginas - 1),
            range(2, total_paginas + 1)
        )

        for items_pagina, paginacion in resultados:
            todos_los_items.extend(items_pagina)


    for item in todos_los_items:
        
        if fecha_inicio and fecha_fin:
            fecha_publicacion = datetime.strptime(
                item["fechas"]["fecha_publicacion"],
                "%Y-%m-%d %H:%M"
            ).date()

            if not (fecha_inicio <= fecha_publicacion <= fecha_fin):
                continue

        nombre = item["nombre"].lower()

        if any(palabra in nombre for palabra in PALABRAS_EXCLUIDAS):
                continue
        
        estado_convocatoria = item["convocatoria"]["estado_convocatoria"]

        if estado_convocatoria == llamado: #and item["resumen"]["total_ofertas_recibidas"] <= 3:

            if llamado == 1:
                # evaluamos llamado para saber que fecha de cierre almacenar
                fecha_cierre = item["fechas"]["fecha_cierre_primer_llamado"] 
            else:
                fecha_cierre = item["fechas"]["fecha_cierre_segundo_llamado"]


            
            # convertimos esa fecha a objeto datetime (de texto a datetime)
            try:
                fecha = datetime.strptime(
                    fecha_cierre,
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                )
            except ValueError:
                fecha = datetime.strptime(
                    fecha_cierre,
                    "%Y-%m-%dT%H:%M:%SZ"
                )


            # le damos formato que vera el usuario (de datetime a texto) y lo almacenamos en una clave nueva del diccionario
            item["fecha_cierre_mostrar"] = fecha.strftime("%d-%m-%Y %H:%M")

            compras_filtradas.append(item)
        
        


 
    return compras_filtradas


