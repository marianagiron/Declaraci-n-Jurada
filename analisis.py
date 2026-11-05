
import pandas as pd
import unicodedata
import os
from conexion_sheets import obtener_datos

# MARIANA: FUNCIONES 1 Y 2

def contar_declaraciones_proyecto(datos):
    proyecto = buscar_columna(datos, ["proyecto"])
    return contar_por(datos, proyecto, "Proyecto")


def sumar_importes_proyecto(datos):
    proyecto = buscar_columna(datos, ["proyecto"])
    importe = buscar_columna(datos, ["importe", "monto"])
    return sumar_por(datos, proyecto, importe, "Proyecto")


# IRMA: FUNCIONES 3 Y 4

import os
import shutil
from datetime import datetime


def validar_archivo(archivo):
    if os.path.exists(archivo):
        return True
    return False


def crear_carpeta_por_mes(ruta_base):
    hoy = datetime.now()
    mes = str(hoy.year) + "-" + str(hoy.month)
    carpeta = ruta_base + "/" + mes
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
    return carpeta


import shutil
def copiar_declaracion(archivo, carpeta_destino):
    shutil.copy(archivo, carpeta_destino)
    return carpeta_destino 

# MARIANA Y IRMA: FUNCIONES 5 Y 6

def contar_por_solicitante(datos):
    solicitante = buscar_columna(
        datos, ["solicitante", "declarante"]
    )
    return contar_por(datos, solicitante, "Solicitante")


def contar_por_mes(datos):
    columna_fecha = buscar_columna(datos, ["fecha"])
    conteos = {}

    for valor in datos[columna_fecha]:
        fecha = pd.to_datetime(
            valor, errors="coerce", dayfirst=True
        )

        if pd.isna(fecha):
            mes = "Fecha no valida"
        else:
            mes = fecha.strftime("%Y-%m")

        if mes in conteos:
            conteos[mes] += 1
        else:
            conteos[mes] = 1

#Conectar
datos = pd.DataFrame(obtener_datos())

#mostrar los datos 
print("\n===DATOS DE DECLARACIÓN JURADA===")
 
if datos.empty:
    print("No se encuentraron registros en Google Sheets")
else:
    import pandas as pd
    tabla= pd.DataFrame(datos)

    print(datos.to_string(index=False))

    print("\nTotal de registros:",
    len(datos))
    print("=================================")

