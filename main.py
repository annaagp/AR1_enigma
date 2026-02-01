import menu
import subprocess
import sys

def principal():
    print("--- BIENVENIDO A DATA BUNKER ---")
    print("1. Modo Consola (Texto)")
    print("2. Modo Interfaz (Grafico)")
    
    opcion = input("Seleccione modo: ")
    
    if opcion == "1":
        menu.mostrar_menu()
    elif opcion == "2":
        # Ejecuta el archivo de interfaz de forma independiente
        subprocess.run([sys.executable, "interfaz.py"])
    else:
        print("Opcion no valida.")

if __name__ == "__main__":
    principal()