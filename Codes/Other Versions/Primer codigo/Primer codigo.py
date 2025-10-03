import os
import time

def leer_archivo(ruta_archivo, max_caracteres=8000):
    try:
        # Verificar si el archivo existe
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{ruta_archivo}' no existe.")
            return
        
        # Abrir y leer el archivo
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
            time.sleep(0.01) 
        
        # Mostrar estadísticas al final
        print("\n" + "=" * 60)
        print(f"\nTotal de caracteres transcritos: {num_caracteres}")
        print(f"Total de líneas: {contenido.count(chr(10)) + 1}")
        
    except UnicodeDecodeError:
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
            print(f"Error al leer el archivo: {e}")
    
    except Exception as e:
        print(f"Error inesperado: {e}")


def main():
    print("PROGRAMA LECTOR DE ARCHIVOS DE TEXTO")
    print("-" * 60)
    
    # Solicitar la ruta del archivo
    ruta = input("Ingresa la ruta del archivo de texto: ").strip()
    
    # Leer y transcribir el archivo
    leer_archivo(ruta)


if __name__ == "__main__":
    main()