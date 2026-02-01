import os
from cryptography.fernet import Fernet
# Definimos el nombre del archivo de forma global para evitar errores de escritura
NOMBRE_CLAVE = "clave.key"

def generar_clave(nom_fitxer=NOMBRE_CLAVE):
    #Crea una nueva llave de cifrado simetrico y la guarda en un archivo
    # Si el archivo ya existe, detenemos el proceso. 
    if os.path.exists(nom_fitxer):
        print("Aviso: La clave ya existe")
        return None
    #generacion
    # Fernet.generate_key() crea una cadena de bytes aleatoria y altamente segura
    clave = Fernet.generate_key()
    #guardado
    # Abrimos el archivo en modo "wb" (escritura binaria) porque la clave no es texto plano
    with open(nom_fitxer, "wb") as f:
        f.write(clave)
    return clave

def cargar_clave(nom_fitxer=NOMBRE_CLAVE):
    #verificacion
    #Lee la llave desde el archivo guardado en el disco
    # Si el usuario intenta cifrar algo sin haber generado la clave primero, avisamos del error
    
    if not os.path.exists(nom_fitxer):
        print("Error: No se encuentra el archivo de la clave (clave.key).")
        return None
    #lectura
    # Abrimos el archivo en modo "rb" (lectura binaria)
    with open(nom_fitxer, "rb") as f:
        clave_cargada = f.read()
    return clave_cargada