import zipfile
import os
import shutil

def comprimir_carpeta(ruta_carpeta, nombre_zip):
    #Toma una carpeta y la convierte en un archivo comprimido ZIP
    try:
        # Crea el archivo ZIP en modo escritura ('w') con compresión estándar
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Recorre la carpeta, sus subcarpetas y archivos
            for raiz, dirs, archivos in os.walk(ruta_carpeta):
                for archivo in archivos:
                    # Crea la ruta absoluta para encontrar el archivo en el disco
                    ruta_completa = os.path.join(raiz, archivo)
                    # Guarda el archivo dentro del ZIP con su ruta relativa
                    zipf.write(ruta_completa, os.path.relpath(ruta_completa, ruta_carpeta))
        return True
    except Exception as e:
        print(f"Error al crear backup: {e}")
        return False

def restaurar_copia(archivo_zip, destino):
    #Extrae el contenido de un archivo ZIP en la ruta especificada
    try:
        # Abre el archivo ZIP en modo lectura ('r')
        with zipfile.ZipFile(archivo_zip, 'r') as zipf:
            # Extrae absolutamente todo el contenido en la carpeta de destino
            zipf.extractall(destino)
        return True
    except Exception as e:
        print(f"Error al restaurar: {e}")
        return False