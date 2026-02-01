import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import key_manager
import crypto_utils
import backup_manager
import analizar_archivos

def generar():
    # Intenta crear la llave. Si ya existe, lanza un aviso de atencion.
    clave = key_manager.generar_clave()
    if clave:
        #Genera una nova clau de xifratge mitjançant el gestor de claus
        messagebox.showinfo("Exito", "Clave generada correctamente.")
    else:
        messagebox.showwarning("Atencion", "La clave ya existe.")

def cifrar():
    #Carga la clave actual y cifra un archivo seleccionado por el usuario
    # Primero busca la llave; si no esta, no permite continuar.
    clave = key_manager.cargar_clave()
    if not clave:
        messagebox.showerror("Error", "Falta clave.key")
        return
    # Abre el explorador de archivos de Windows/Mac/Linux para elegir el archivo.
    archivo = filedialog.askopenfilename()
    if archivo:
        crypto_utils.cifrar_archivo(archivo, clave)
        messagebox.showinfo("Exito", "Archivo cifrado.")

def descifrar():
    #Proceso inverso: convierte un archivo .enc en su formato original
    clave = key_manager.cargar_clave()
    if not clave:
        messagebox.showerror("Error", "Falta clave.key")
        return
    # Solo permite seleccionar archivos que terminen en .enc
    archivo = filedialog.askopenfilename(filetypes=[("Archivos ENC", "*.enc")])
    if archivo:
        salida = crypto_utils.descifrar_archivo(archivo, clave)
        if salida:
            messagebox.showinfo("Exito", f"Restaurado: {salida}")

def backup():
    #Comprime una carpeta completa en un archivo ZIP
    # Pide al usuario que seleccione una carpeta completa
    carpeta = filedialog.askdirectory()
    if carpeta:
        # Abre un cuadro de texto para que el usuario escriba el nombre del ZIP
        nombre = simpledialog.askstring("Backup", "Nombre del zip:")
        if nombre:
            if not nombre.endswith(".zip"): nombre += ".zip"
            if backup_manager.comprimir_carpeta(carpeta, nombre):
                messagebox.showinfo("Exito", "Backup creado.")

def restaurar():
    #Descomprime un archivo ZIP en la ubicacion seleccionada
    # Selecciona el archivo comprimido y luego la carpeta donde se volcaran los datos.
    zip_file = filedialog.askopenfilename(filetypes=[("ZIP", "*.zip")])
    if zip_file:
        dest = filedialog.askdirectory()
        if dest:
            backup_manager.restaurar_copia(zip_file, dest)
            messagebox.showinfo("Exito", "Restaurado.")

def analizar():
    #Escanea una carpeta para mostrar estadísticas de peso y tipos de archivos
    carpeta = filedialog.askdirectory(title="Carpeta a Analizar")
    if carpeta:
        # Llama al analizador y prepara un texto con el resumen de archivos encontrados.
        datos, peso = file_analyzer.analizar_directorio(carpeta)
        texto = f"Peso Total: {peso} KB\n\nArchivos:\n"
        for ext, cant in datos.items():
            texto += f"{ext}: {cant}\n"
            # Muestra los resultados en una ventana de informacion
        messagebox.showinfo("Analisis", texto)

#configuracion de la interfaz grafica
# Creacion de la ventana principal
ventana = tk.Tk()
ventana.title("Data Bunker Pro")
ventana.geometry("300x450")
# Etiqueta de titulo superior
tk.Label(ventana, text="DATA BUNKER", font=("Arial", 14, "bold")).pack(pady=15)
# Lista de configuracion para crear los botones de forma automatica 
botones = [
    ("1. Generar Clave", generar),
    ("2. Cifrar Archivo", cifrar),
    ("3. Descifrar Archivo", descifrar),
    ("4. Crear Backup", backup),
    ("5. Restaurar Backup", restaurar),
    ("6. Analizar Carpeta", analizar)
]
# Bucle que dibuja cada boton en la pantalla
for txt, cmd in botones:
    tk.Button(ventana, text=txt, command=cmd, width=25).pack(pady=5)
# Boton de salida con color diferente para resaltar
tk.Button(ventana, text="Salir", command=ventana.quit, bg="#ffcccc").pack(pady=20)
# Mantiene la ventana abierta escuchando clics
ventana.mainloop()