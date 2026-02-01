import os
import collections

def analizar_directorio(ruta):
    if not os.path.exists(ruta):
        return None, 0
    contar_extensiones = []
    peso_total = 0
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            nombre, extension = os.path.splitext(archivo)
            if extension == "":
                extension = "Sin extension"
            contar_extensiones.append(extension)
            ruta_completa = os.path.join(carpeta_actual, archivo)
            peso_total += os.path.getsize(ruta_completa)
    resumen = dict(collections.Counter(contar_extensiones))
    peso_kb = round(peso_total / 1024, 2)
    return resumen, peso_kb