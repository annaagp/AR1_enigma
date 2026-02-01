import os
from cryptography.fernet import Fernet

NOMBRE_CLAVE = "clave.key"

def generar_clave(nom_fitxer=NOMBRE_CLAVE):
    if os.path.exists(nom_fitxer):
        print("Aviso: La clave ya existe")
        return None
    clave = Fernet.generate_key()
    with open(nom_fitxer, "wb") as f:
        f.write(clave)
    return clave

def cargar_clave(nom_fitxer=NOMBRE_CLAVE):
    if not os.path.exists(nom_fitxer):
        print("Error: No se encuentra el archivo de la clave (clave.key).")
        return None
    with open(nom_fitxer, "rb") as f:
        clave_cargada = f.read()
    return clave_cargada