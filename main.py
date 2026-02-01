import menu
import subprocess
import sys

def principal():
    #Función de entrada que permite elegir entre la consola o la interfaz grafica
    print("--- BIENVENIDO A DATA BUNKER ---")
    print("1. Modo Consola (Texto)")
    print("2. Modo Interfaz (Grafico)")
    
    opcion = input("Seleccione modo: ")
    # CAMINO A: Ejecuta la logica directamente en la terminal
    if opcion == "1":
        menu.mostrar_menu()
    # CAMINO B: Lanza la ventana de Tkinter como un proceso separado
    elif opcion == "2":
        # subprocess.run crea un hilo nuevo para la interfaz
        # sys.executable asegura que se use la misma version de Python actual
        # Ejecuta el archivo de interfaz de forma independiente
        subprocess.run([sys.executable, "interfaz.py"])
    else:
        print("Opcion no valida.")
# Si este archivo es importado por otro, no se ejecutara nada automaticamente
if __name__ == "__main__":
    principal()