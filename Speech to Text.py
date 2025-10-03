import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
import os
from pydub import AudioSegment
import shutil

# --- Verificar si ffmpeg está disponible ---
FFMPEG_DISPONIBLE = shutil.which("ffmpeg") is not None

# --- Función para convertir archivos de audio a WAV ---
def convertir_a_wav(ruta_archivo):
    """
    Convierte archivos de audio a formato WAV para compatibilidad con speech_recognition.
    Si ffmpeg no está disponible, solo acepta WAV.
    """
    _, extension = os.path.splitext(ruta_archivo)
    extension = extension.lower()
    
    # Si ya es WAV, no es necesario convertir
    if extension == '.wav':
        return ruta_archivo
    
    # Si no hay ffmpeg, rechazamos otros formatos
    if not FFMPEG_DISPONIBLE:
        print(f"⚠️ ffmpeg no está instalado. Solo se aceptan archivos WAV.")
        return None

    # Crear un nombre temporal para el archivo WAV
    ruta_wav = "temp_audio.wav"
    
    try:
        audio = AudioSegment.from_file(ruta_archivo, format=extension[1:])
        audio.export(ruta_wav, format="wav")
        return ruta_wav
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")
        return None

# --- Función para seleccionar el archivo de audio ---
def seleccionar_archivo():
    """
    Abre una ventana del explorador de archivos para que el usuario elija un archivo de audio.
    """
    root = tk.Tk()
    root.withdraw() 
    
    if FFMPEG_DISPONIBLE:
        tipos = [
            ("Archivos de Audio", "*.wav *.mp3 *.m4a *.ogg *.flac *.aac"),
            ("Todos los archivos", "*.*")
        ]
    else:
        tipos = [("Archivos WAV", "*.wav")]

    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo de audio",
        filetypes=tipos
    )
    return ruta_archivo

# --- Función principal para transcribir el audio ---
def transcribir_audio(ruta_archivo):
    """
    Toma la ruta de un archivo de audio, lo procesa y devuelve el texto transcrito.
    """
    if not ruta_archivo:
        print("No se seleccionó ningún archivo. Saliendo del programa.")
        return

    print(f"📂 Procesando el archivo: {ruta_archivo}")

    # Convertir a WAV si es necesario
    ruta_audio_convertido = convertir_a_wav(ruta_archivo)
    if not ruta_audio_convertido:
        print("❌ No se pudo convertir el archivo a formato compatible.")
        return

    r = sr.Recognizer()

    try:
        with sr.AudioFile(ruta_audio_convertido) as source:
            print("🔊 Ajustando para ruido ambiental...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            print("✍️ Transcribiendo audio...")
            audio_data = r.record(source)
            
            texto = r.recognize_google(audio_data, language="es-ES")
            
            print("\n--- Texto Transcrito ---")
            print(texto)
            print("------------------------\n")
            
    except sr.UnknownValueError:
        print("⚠️ No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"🌐 Error de conexión con el servicio de Google; {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        if ruta_audio_convertido != ruta_archivo and os.path.exists(ruta_audio_convertido):
            os.remove(ruta_audio_convertido)
            print("🗑️ Archivo temporal eliminado.")

# --- Ejecución del programa ---
if __name__ == "__main__":
    ruta_del_audio = seleccionar_archivo()
    transcribir_audio(ruta_del_audio)
