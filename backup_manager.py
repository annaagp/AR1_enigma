import zipfile
import os
import shutil

def comprimir_carpeta(ruta_carpeta, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for raiz, dirs, archivos in os.walk(ruta_carpeta):
                for archivo in archivos:
                    ruta_completa = os.path.join(raiz, archivo)
                    zipf.write(ruta_completa, os.path.relpath(ruta_completa, ruta_carpeta))
        return True
    except Exception as e:
        print(f"Error al crear backup: {e}")
        return False

def restaurar_copia(archivo_zip, destino):
    try:
        with zipfile.ZipFile(archivo_zip, 'r') as zipf:
            zipf.extractall(destino)
        return True
    except Exception as e:
        print(f"Error al restaurar: {e}")
        return False