import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import key_manager
import crypto_utils
import backup_manager
import file_analyzer

def generar():
    clave = key_manager.generar_clave()
    if clave:
        messagebox.showinfo("Exito", "Clave generada correctamente.")
    else:
        messagebox.showwarning("Atencion", "La clave ya existe.")

def cifrar():
    clave = key_manager.cargar_clave()
    if not clave:
        messagebox.showerror("Error", "Falta clave.key")
        return
    archivo = filedialog.askopenfilename()
    if archivo:
        crypto_utils.cifrar_archivo(archivo, clave)
        messagebox.showinfo("Exito", "Archivo cifrado.")

def descifrar():
    clave = key_manager.cargar_clave()
    if not clave:
        messagebox.showerror("Error", "Falta clave.key")
        return
    archivo = filedialog.askopenfilename(filetypes=[("Archivos ENC", "*.enc")])
    if archivo:
        salida = crypto_utils.descifrar_archivo(archivo, clave)
        if salida:
            messagebox.showinfo("Exito", f"Restaurado: {salida}")

def backup():
    carpeta = filedialog.askdirectory()
    if carpeta:
        nombre = simpledialog.askstring("Backup", "Nombre del zip:")
        if nombre:
            if not nombre.endswith(".zip"): nombre += ".zip"
            if backup_manager.comprimir_carpeta(carpeta, nombre):
                messagebox.showinfo("Exito", "Backup creado.")

def restaurar():
    zip_file = filedialog.askopenfilename(filetypes=[("ZIP", "*.zip")])
    if zip_file:
        dest = filedialog.askdirectory()
        if dest:
            backup_manager.restaurar_copia(zip_file, dest)
            messagebox.showinfo("Exito", "Restaurado.")

def analizar():
    carpeta = filedialog.askdirectory(title="Carpeta a Analizar")
    if carpeta:
        datos, peso = file_analyzer.analizar_directorio(carpeta)
        texto = f"Peso Total: {peso} KB\n\nArchivos:\n"
        for ext, cant in datos.items():
            texto += f"{ext}: {cant}\n"
        messagebox.showinfo("Analisis", texto)

ventana = tk.Tk()
ventana.title("Data Bunker Pro")
ventana.geometry("300x450")
tk.Label(ventana, text="DATA BUNKER", font=("Arial", 14, "bold")).pack(pady=15)

botones = [
    ("1. Generar Clave", generar),
    ("2. Cifrar Archivo", cifrar),
    ("3. Descifrar Archivo", descifrar),
    ("4. Crear Backup", backup),
    ("5. Restaurar Backup", restaurar),
    ("6. Analizar Carpeta", analizar)
]

for txt, cmd in botones:
    tk.Button(ventana, text=txt, command=cmd, width=25).pack(pady=5)

tk.Button(ventana, text="Salir", command=ventana.quit, bg="#ffcccc").pack(pady=20)
ventana.mainloop()