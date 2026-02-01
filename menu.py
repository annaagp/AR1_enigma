import os
import key_manager
import crypto_utils
import backup_manager
import analizar_archivos

def mostrar_menu():
    #Controla el flujo principal del programa en modo texto
    while True: # Mantiene el programa abierto hasta que el usuario decida salir
        print("\n--- DATA BUNKER ---")
        print("1. Generar Clave de Seguridad")
        print("2. Cifrar Archivo")
        print("3. Descifrar Archivo")
        print("4. Crear Backup (Zip)")
        print("5. Restaurar Backup")
        print("6. Eliminar Archivo")
        print("7. Analizar Carpeta")
        print("0. Salir")

        opcion = input("\nSelecciona una opcion: ").strip()
        # GENERAR CLAVE
        if opcion == "1":
            if key_manager.generar_clave():
                print("Clave generada con exito.")
        # CIFRAR ARCHIVO
        elif opcion == "2":
            clave = key_manager.cargar_clave()
            if clave:
                archivo = input("Archivo a cifrar: ")
                if os.path.exists(archivo):
                    crypto_utils.cifrar_archivo(archivo, clave)
                else:
                    print("Error: El archivo no existe.")
        # DESCIFRAR ARCHIVO
        elif opcion == "3":
            clave = key_manager.cargar_clave()
            if clave:
                archivo = input("Archivo .enc a descifrar: ")
                if os.path.exists(archivo):
                    crypto_utils.descifrar_archivo(archivo, clave)
                else:
                    print("Error: El archivo no existe.")
        # CREAR COPIA DE SEGURIDAD (ZIP)
        elif opcion == "4":
            carpeta = input("Carpeta para backup: ").strip()
            nombre = input("Nombre del archivo destino: ").strip()
            if nombre:
                # Validacion automatica de la extension
                if not nombre.endswith(".zip"):
                    nombre += ".zip"
                backup_manager.comprimir_carpeta(carpeta, nombre)
        # RESTAURAR COPIA
        elif opcion == "5":
            archivo_zip = input("Archivo ZIP a restaurar: ").strip()
            destino = input("Carpeta de destino: ").strip()
            if destino:
                backup_manager.restaurar_copia(archivo_zip, destino)
        # ELIMINAR CON PROTECCION
        elif opcion == "6":
            # Lista de archivos que NO se pueden borrar porque el programa los necesita
            protegidos = ["main.py", "menu.py", "key_manager.py", "file_analyzer.py",
                          "crypto_utils.py", "backup_manager.py", "clave.key"]
            borrar = input("Archivo a eliminar: ")
            if borrar in protegidos:
                print("Alerta: No puedes borrar archivos del sistema.")
            elif os.path.exists(borrar):
                if input(f"Seguro que quieres borrar {borrar}? (s/n): ").lower() == "s":
                    os.remove(borrar)# Borra el archivo fisicamente del disco
                    print("Eliminado.")
            else:
                print("El archivo no existe.")
        # ANALIZAR ESTRUCTURA
        elif opcion == "7":
            ruta = input("Carpeta a analizar: ")
            resumen, peso = analizar_archivos.analizar_directorio(ruta)
            if resumen is not None:
                print(f"\n--- {ruta} ---")
                print(f"Peso Total: {peso} KB")
                # Bucle para mostrar cuantos archivos hay de cada tipo (PDF, JPG, etc.)
                for ext, cantidad in resumen.items():
                    print(f" {ext}: {cantidad}")
            else:
                print("La carpeta no existe.")
        elif opcion == "0":
            break # Sale del bucle y termina la función
