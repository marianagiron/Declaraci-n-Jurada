
from conexion_sheets import obtener_datos

try:
    datos = obtener_datos()

    print("\nPRIMERAS FILAS DE LA HOJA:")
    print(datos.head())

except Exception:
    print("\nNo se pudo cargar Google Sheets.")
    print("Revisa el mensaje de error anterior.")
