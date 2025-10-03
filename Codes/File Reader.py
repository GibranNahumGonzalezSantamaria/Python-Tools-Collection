import os
import time
# Se importa tkinter y filedialog para abrir el explorador de archivos
import tkinter as tk
from tkinter import filedialog 

def leer_archivo(ruta_archivo, max_caracteres=8000):
    """
    Lee y "transcribe" el contenido de un archivo de texto, 
    verificando el tamaño máximo de caracteres.
    """
    if not ruta_archivo:  # Se verifica si la ruta está vacía (por si se cancela la selección)
        print("Operación cancelada. No se seleccionó ningún archivo.")
        return

    try:
        # El resto de la función leer_archivo permanece igual
        
        # Verificar si el archivo existe
        if not os.path.exists(ruta_archivo):
            # Este chequeo puede ser redundante si se usa filedialog, pero se mantiene por seguridad
            print(f"Error: El archivo '{ruta_archivo}' no existe.")
            return
            
        # Abrir y leer el archivo (intento con UTF-8)
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
        # Verificar que no exceda el máximo de caracteres
        num_caracteres = len(contenido)
        if num_caracteres > max_caracteres:
            print(f"Error: El archivo tiene {num_caracteres} caracteres.")
            print(f"Solo se pueden transcribir archivos con hasta {max_caracteres} caracteres.")
            print("Operación cancelada.")
            return
            
        print("\n" + "=" * 60)
        print(f"TRANSCRIBIENDO ARCHIVO: {ruta_archivo}")
        print("=" * 60 + "\n")
            
        # Transcribir el contenido caracter por caracter
        for caracter in contenido:
            print(caracter, end='', flush=True)
            time.sleep(0.01)  # Pequeña pausa para el efecto de "transcripción"
            
        # Mostrar estadísticas al final
        print("\n" + "=" * 60)
        print(f"\nTotal de caracteres transcritos: {num_caracteres}")
        # Se cuenta el número de saltos de línea y se suma 1 para obtener el total de líneas
        print(f"Total de líneas: {contenido.count(chr(10)) + 1}") 
            
    except UnicodeDecodeError:
        print("Error: El archivo no se puede leer con codificación UTF-8.")
        print("Intentando con codificación latin-1...")
        try:
            # Intento con codificación latin-1
            with open(ruta_archivo, 'r', encoding='latin-1') as archivo:
                contenido = archivo.read()
                
            # Se omite la comprobación de max_caracteres en el bloque 'except', 
            # pero se podría añadir si fuera necesario
                
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
        print(f"Error inesperado: {e}")


def main():
    print("PROGRAMA LECTOR DE ARCHIVOS DE TEXTO")
    print("-" * 60)
    
    # 1. Inicializar la interfaz de Tkinter pero ocultarla
    # Esto evita que se muestre la ventana principal (root) de Tkinter
    root = tk.Tk()
    root.withdraw()
    
    # 2. Abrir el explorador de archivos
    # askopenfilename abre el diálogo de selección de archivos y devuelve la ruta
    # Se añade el filtro para archivos de texto (*.txt)
    ruta = filedialog.askopenfilename(
        title="Selecciona el archivo de texto a transcribir",
        filetypes=(("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    # 3. Leer y transcribir el archivo
    # La variable 'ruta' contendrá la ruta seleccionada o una cadena vacía si se cancela
    leer_archivo(ruta)


if __name__ == "__main__":
    main()
