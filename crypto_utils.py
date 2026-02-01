from cryptography.fernet import Fernet
import os

def cifrar_archivo(nombre_archivo, clave):
    if clave == None:
        print("Error: Sin clave no puedo cifrar nada.")
        return
    if os.path.exists(nombre_archivo) == False:
        print("Error: El archivo no esta, asi que no puedo cifrarlo.")
        return
    
    f = Fernet(clave)
    with open(nombre_archivo, "rb") as file:
        datos = file.read()
    
    datos_encriptados = f.encrypt(datos)
    nombre_final = nombre_archivo + ".enc"
    
    with open(nombre_final, "wb") as file:
        file.write(datos_encriptados)
    print("He creado el archivo cifrado: " + nombre_final)

def descifrar_archivo(archivo_encriptado, clave):
    if os.path.exists(archivo_encriptado) == False:
        print("Error: No encuentro el archivo cifrado(.enc)")
        return None
    
    f = Fernet(clave)
    with open(archivo_encriptado, "rb") as file:
        datos_encriptados = file.read()
    
    datos_originales = f.decrypt(datos_encriptados)
    nombre_salida = archivo_encriptado.replace(".enc", "")
    
    with open(nombre_salida, "wb") as file:
        file.write(datos_originales)
    print("Archivo descifrado temporalmente: " + nombre_salida)
    return nombre_salida