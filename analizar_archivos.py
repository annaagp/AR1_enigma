import os
import collections

def analizar_directorio(ruta):
    #validacion
    #Analiza una carpeta para contar tipos de archivos y calcular el peso total
    # Si la ruta no existe, el programa aborta para no fallar
    if not os.path.exists(ruta):
        return None, 0
    #inicializacion
    contar_extensiones = []# Lista temporal para guardar cada extension encontrada
    peso_total = 0 # Acumulador para el tamano total en bytes
    # os.walk es un generador que entra en cada rincon de la carpeta raiz
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            # os.path.splitext separa el nombre del archivo de su extension
            nombre, extension = os.path.splitext(archivo)
            # Si el archivo no tiene extensión
            if extension == "":
                extension = "Sin extension"
            # Anadimos la extension a nuestra lista para el conteo posterior
            contar_extensiones.append(extension)
            # Unimos la carpeta con el nombre del archivo para obtener su ruta fisica real
            ruta_completa = os.path.join(carpeta_actual, archivo)
            # Sumamos el tamano del archivo actual al total acumulado
            peso_total += os.path.getsize(ruta_completa)
    # collections.Counter cuenta cuantas veces aparece cada extension en la lista
    resumen = dict(collections.Counter(contar_extensiones))
    # Convertimos el peso de bytes a Kilobytes (dividiendo por 1024)
    # round(..., 2) lo deja con solo dos decimales
    peso_kb = round(peso_total / 1024, 2)
    return resumen, peso_kb