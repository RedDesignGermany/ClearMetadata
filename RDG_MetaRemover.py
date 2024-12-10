import argparse
import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import mutagen
from moviepy.editor import VideoFileClip
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.wavpack import WavPack
from mutagen.wav import WAVE
from mutagen.mp4 import MP4

# Funktion zum Entfernen von Metadaten aus Bildern
def clear_image_metadata(imgname):
    # Öffnen der Bilddatei
    img = Image.open(imgname)
    # Lesen der Bilddaten ohne Metadaten
    data = list(img.getdata())
    # Erstellen eines neuen Bildes mit denselben Daten, aber ohne Metadaten
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    # Speichern des neuen Bildes, um die Metadaten zu entfernen
    img_without_metadata.save(imgname)
    print(f"Metadata successfully cleared from image '{imgname}'.")

# Funktion zum Entfernen von Metadaten aus PDF-Dateien
def clear_pdf_metadata(pdfname):
    # Öffnen der PDF-Datei
    reader = PdfReader(pdfname)
    writer = PdfWriter()
    # Hinzufügen aller Seiten zur neuen PDF ohne Metadaten
    for page in reader.pages:
        writer.add_page(page)
    # Entfernen aller Metadaten
    for key in list(reader.metadata.keys()):
        writer.add_metadata({key: ''})
    # Speichern der neuen PDF-Datei
    with open(pdfname, "wb") as f:
        writer.write(f)
    print(f"Metadata successfully cleared from PDF '{pdfname}'.")

# Funktion zum Entfernen von Metadaten aus Audiodateien
def clear_audio_metadata(audioname):
    # Öffnen der Audiodatei mit Mutagen
    audio = mutagen.File(audioname)
    if audio is not None:
        # Entfernen und Speichern der Metadaten
        audio.delete()
        audio.save()
        print(f"Metadata successfully cleared from audio '{audioname}'.")
    else:
        print(f"Failed to clear metadata from audio '{audioname}'.")

# Funktion zum Entfernen von Metadaten aus Videodateien
def clear_video_metadata(videoname):
    # Öffnen der Videodatei
    video = VideoFileClip(videoname)
    # Speichern des Videos ohne Metadaten
    video.write_videofile(videoname, codec="libx264", audio_codec="aac", remove_temp=True)
    print(f"Metadata successfully cleared from video '{videoname}'.")

# Funktion zur Erkennung des Dateityps und zum Entfernen der Metadaten
def clear_metadata(filename):
    # Bestimmen der Dateierweiterung
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
        clear_image_metadata(filename)
    elif ext in ['.pdf']:
        clear_pdf_metadata(filename)
    elif ext in ['.mp3', '.flac', '.wav', '.m4a', '.ogg']:
        clear_audio_metadata(filename)
    elif ext in ['.mp4', '.avi', '.mkv', '.mov']:
        clear_video_metadata(filename)
    else:
        print(f"File type '{ext}' not supported for metadata removal.")

# Einrichtung der Befehlszeilenargumente
parser = argparse.ArgumentParser(description="Remove metadata from a file.")
parser.add_argument("file", help="File from which to remove metadata")
# Argumente parsen
args = parser.parse_args()
# Metadaten der angegebenen Datei entfernen
if args.file:
    clear_metadata(args.file)
