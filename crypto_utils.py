from cryptography.fernet import Fernet
import os

def cifrar_archivo(nombre_archivo, clave):
    #validaciones iniciales
    if clave == None:
        print("Error: Sin clave no puedo cifrar nada.")
        return
    if os.path.exists(nombre_archivo) == False:
        print("Error: El archivo no esta, asi que no puedo cifrarlo.")
        return
    #proceso de cifrado
    # Inicializa el motor de cifrado Fernet con la clave proporcionada
    f = Fernet(clave)
    # Lee el archivo original en modo binario (rb)
    with open(nombre_archivo, "rb") as file:
        datos = file.read()
    # Aplica el algoritmo de cifrado a los datos
    datos_encriptados = f.encrypt(datos)
    # Define el nuevo nombre
    nombre_final = nombre_archivo + ".enc"
    # Guarda el resultado cifrado en un nuevo archivo binario 
    with open(nombre_final, "wb") as file:
        file.write(datos_encriptados)
    print("He creado el archivo cifrado: " + nombre_final)

def descifrar_archivo(archivo_encriptado, clave):
    #validacion
    if os.path.exists(archivo_encriptado) == False:
        print("Error: No encuentro el archivo cifrado(.enc)")
        return None
    #proceso de descifrado
    # Usamos la misma clave que se uso para cifrar 
    f = Fernet(clave)
    with open(archivo_encriptado, "rb") as file:
        datos_encriptados = file.read()
    # Intenta descifrar. Si la clave es incorrecta, aqui daria un error.
    datos_originales = f.decrypt(datos_encriptados)
    # Limpia el nombre eliminando la extensión ".enc" para restaurar el original
    nombre_salida = archivo_encriptado.replace(".enc", "")
    # Escribe los datos recuperados en un archivo nuevo
    with open(nombre_salida, "wb") as file:
        file.write(datos_originales)
    print("Archivo descifrado temporalmente: " + nombre_salida)
    return nombre_salida