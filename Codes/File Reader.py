import os  # 🗂️ Para interactuar con el sistema de archivos
import time  # ⏱️ Para pausas entre caracteres y efecto de "transcripción"
import tkinter as tk  # 🖼️ Interfaz gráfica para abrir ventanas de selección de archivos
from tkinter import filedialog  # 📂 Para abrir el explorador de archivos

def leer_archivo(ruta_archivo, max_caracteres=8000):
    """
    📜 Lee un archivo de texto y lo muestra carácter por carácter.
    ⚠️ Verifica que no supere un máximo de caracteres.
    """
    if not ruta_archivo:  # ❌ Si no se selecciona archivo
        print("Operación cancelada. No se seleccionó ningún archivo.")
        return

    try:
        # 🔍 Comprobar que el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{ruta_archivo}' no existe.")
            return
            
        # 📖 Abrir el archivo en modo lectura con codificación UTF-8
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
        # 📏 Verificar número máximo de caracteres
        num_caracteres = len(contenido)
        if num_caracteres > max_caracteres:
            print(f"Error: El archivo tiene {num_caracteres} caracteres.")
            print(f"Solo se pueden transcribir archivos con hasta {max_caracteres} caracteres.")
            print("Operación cancelada.")
            return
            
        # ✨ Mostrar encabezado antes de "transcribir"
        print("\n" + "=" * 60)
        print(f"TRANSCRIBIENDO ARCHIVO: {ruta_archivo}")
        print("=" * 60 + "\n")
            
        # 🔤 Mostrar cada carácter con un pequeño retraso
        for caracter in contenido:
            print(caracter, end='', flush=True)
            time.sleep(0.01)  # ⏳ Pausa para efecto de escritura en tiempo real
            
        # 📊 Estadísticas al final
        print("\n" + "=" * 60)
        print(f"\nTotal de caracteres transcritos: {num_caracteres}")
        print(f"Total de líneas: {contenido.count(chr(10)) + 1}")  # 📝 Contar saltos de línea
            
    except UnicodeDecodeError:
        # ⚡ Si falla UTF-8, intentar latin-1
        print("Error: El archivo no se puede leer con codificación UTF-8.")
        print("Intentando con codificación latin-1...")
        try:
            with open(ruta_archivo, 'r', encoding='latin-1') as archivo:
                contenido = archivo.read()
                
            print("\n" + "=" * 60)
            print(f"TRANSCRIBIENDO ARCHIVO: {ruta_archivo}")
            print("=" * 60 + "\n")
                
            for caracter in contenido:
                print(caracter, end='', flush=True)
                time.sleep(0.01)
                
            print("\n" + "=" * 60)
                
        except Exception as e:
            print(f"Error al leer el archivo con latin-1: {e}")
            
    except Exception as e:
        # ❗ Captura de errores inesperados
        print(f"Error inesperado: {e}")


def main():
    print("PROGRAMA LECTOR DE ARCHIVOS DE TEXTO 📄")
    print("-" * 60)
    
    # 🖼️ Inicializar Tkinter pero ocultar ventana principal
    root = tk.Tk()
    root.withdraw()
    
    # 📂 Abrir explorador para seleccionar archivo de texto
    ruta = filedialog.askopenfilename(
        title="Selecciona el archivo de texto a transcribir",
        filetypes=(("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    # 🔤 Leer y transcribir archivo
    leer_archivo(ruta)


if __name__ == "__main__":
    main()  # ▶️ Ejecutar programa
