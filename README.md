# Python Tools Collection 🐍

Una colección de programas para procesamiento de archivos, imágenes y audio.

## Programas incluidos

### 1. 📄 File Symbol Reader
**Archivo:** `File Reader.py`  
Lee un archivo carácter por carácter e imprime todos los símbolos (letras, números, espacios, puntuación).

### 2. 🖼️ Image Analyzer  
**Archivo:** `Image Analyzer.py`  
Analiza una imagen píxel por píxel y extrae los valores RGB de cada uno.

### 3. 🎤 Speech to Text
**Archivo:** `Speech to Text.py`  
Convierte archivos de audio en texto utilizando reconocimiento de voz.

**Nota:**  
- Para procesar **todos los formatos de audio** (`.mp3`, `.m4a`, `.ogg`, `.flac`, `.aac`, etc.) se requiere **FFmpeg**.  
- La instalación de FFmpeg es **opcional**; sin él solo se procesan archivos `.wav`.

## ⚙️ Instalación

Instala dependencias:

```bash
pip install Pillow
pip install numpy
pip install SpeechRecognition
pip install pydub  # necesario para otros formatos de audio
