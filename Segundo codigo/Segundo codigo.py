from PIL import Image
import numpy as np
import os

def obtener_matriz_colores(ruta_imagen, max_dimension=400):
    """
    Extrae la matriz de colores de una imagen.
    
    Args:
        ruta_imagen (str): Ruta del archivo de imagen
        max_dimension (int): Dimensión máxima (ancho o alto) de la imagen
    
    Returns:
        numpy.ndarray: Matriz de colores de la imagen
    """
    # Verificar si el archivo existe
    if not os.path.exists(ruta_imagen):
        raise FileNotFoundError(f"No se encontró la imagen en: {ruta_imagen}")
    
    # Abrir la imagen
    img = Image.open(ruta_imagen)
    
    # Obtener dimensiones originales
    ancho, alto = img.size
    print(f"Dimensiones originales: {ancho}x{alto}")
    print(f"Modo de la imagen: {img.mode}")
    
    # Convertir imágenes con transparencia o modos especiales a RGB
    if img.mode in ('RGBA', 'LA', 'P'):
        print(f"Convirtiendo de {img.mode} a RGB...")
        # Crear fondo blanco
        fondo = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        # Pegar la imagen sobre el fondo blanco
        fondo.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        img = fondo
    elif img.mode != 'RGB' and img.mode != 'L':
        print(f"Convirtiendo de {img.mode} a RGB...")
        img = img.convert('RGB')
    
    # Redimensionar si excede el máximo
    if ancho > max_dimension or alto > max_dimension:
        # Calcular el factor de escala manteniendo la proporción
        factor = min(max_dimension / ancho, max_dimension / alto)
        nuevo_ancho = int(ancho * factor)
        nuevo_alto = int(alto * factor)
        
        img = img.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
        print(f"Imagen redimensionada a: {nuevo_ancho}x{nuevo_alto}")
    
    # Convertir a matriz numpy
    matriz = np.array(img)
    
    # Determinar el tipo de imagen
    if len(matriz.shape) == 2:
        print("Tipo: Imagen en escala de grises")
        print(f"Forma de la matriz: {matriz.shape} (alto, ancho)")
    elif len(matriz.shape) == 3:
        canales = matriz.shape[2]
        if canales == 3:
            print("Tipo: Imagen a color (RGB)")
            print(f"Forma de la matriz: {matriz.shape} (alto, ancho, canales RGB)")
        elif canales == 4:
            print("Tipo: Imagen a color con transparencia (RGBA)")
            print(f"Forma de la matriz: {matriz.shape} (alto, ancho, canales RGBA)")
    
    return matriz


def mostrar_info_matriz(matriz):
    """
    Muestra información detallada sobre la matriz de colores.
    
    Args:
        matriz (numpy.ndarray): Matriz de colores
    """
    print("\n--- Información de la Matriz ---")
    print(f"Dimensiones: {matriz.shape}")
    print(f"Tipo de datos: {matriz.dtype}")
    print(f"Valor mínimo: {matriz.min()}")
    print(f"Valor máximo: {matriz.max()}")
    
    # Mostrar una muestra de la esquina superior izquierda (5x5 píxeles)
    print("\nMuestra de píxeles (esquina superior izquierda 5x5):")
    if len(matriz.shape) == 2:
        print(matriz[:5, :5])
    else:
        print(matriz[:5, :5, :])


# Ejemplo de uso
if __name__ == "__main__":
    # Solicitar la ruta de la imagen al usuario
    ruta = input("Ingresa la ruta de la imagen: ").strip()
    
    try:
        # Obtener la matriz de colores
        matriz_colores = obtener_matriz_colores(ruta, max_dimension=400)
        
        # Mostrar información de la matriz
        mostrar_info_matriz(matriz_colores)
        
        # Guardar la matriz en un archivo (opcional)
        guardar = input("\n¿Deseas guardar la matriz en un archivo .npy? (s/n): ").strip().lower()
        if guardar == 's':
            nombre_archivo = input("Nombre del archivo (sin extensión): ").strip()
            np.save(f"{nombre_archivo}.npy", matriz_colores)
            print(f"Matriz guardada en: {nombre_archivo}.npy")
            print("Puedes cargarla luego con: np.load('nombre_archivo.npy')")
        
        print("\n¡Proceso completado!")
        
    except Exception as e:
        print(f"Error: {e}")