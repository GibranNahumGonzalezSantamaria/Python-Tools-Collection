# Importamos la biblioteca necesaria para el reconocimiento de voz.
import speech_recognition as sr

# Creamos una instancia del reconocedor de voz.
# Esta es la clase principal que se encarga de todo el proceso.
r = sr.Recognizer()

# Especificamos la ruta a nuestro archivo de audio.
# ASEGÚRATE de que el archivo 'audio.wav' esté en la misma carpeta que tu script,
# o proporciona la ruta completa al archivo.
# Este ejemplo funciona mejor con archivos en formato WAV.
nombre_archivo_audio = "audio.wav"

# Usamos el archivo de audio como la fuente de audio.
# El 'with' se asegura de que el archivo se cierre correctamente después de su uso.
with sr.AudioFile(nombre_archivo_audio) as source:
    
    # El método 'record()' lee el archivo de audio completo y lo guarda en un objeto de audio.
    # Esto prepara el audio para que el motor de reconocimiento lo pueda procesar.
    audio_data = r.record(source)
    
    # Ahora intentamos convertir el audio a texto usando el reconocedor de Google.
    # El parámetro language="es-ES" le indica al reconocedor que el audio está en español.
    # Puedes cambiarlo a "en-US" para inglés, por ejemplo.
    try:
        # El método 'recognize_google()' envía el audio a la API de Google Web Speech
        # y devuelve la transcripción como una cadena de texto.
        texto = r.recognize_google(audio_data, language="es-ES")
        
        # Imprimimos el texto extraído del audio.
        print("El texto del audio es: ")
        print(texto)
        
    # Si Google no puede entender el audio, se lanzará una excepción.
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio.")
        
    # Si hay un problema con la conexión a la API de Google (por ejemplo, sin internet),
    # se lanzará esta otra excepción.
    except sr.RequestError as e:
        print(f"No se pudieron obtener resultados del servicio de Google Speech Recognition; {e}")