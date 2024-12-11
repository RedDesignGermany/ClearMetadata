import argparse
import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import mutagen

def clear_image_metadata(imgname):
    from PIL import Image
    img = Image.open(imgname)
    data = list(img.getdata())
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    img_without_metadata.save(imgname)
    print(f"Metadaten erfolgreich aus dem Bild '{imgname}' entfernt.\nRED DESIGN GERMANY \u2764")

def clear_pdf_metadata(pdfname):
    from PyPDF2 import PdfReader, PdfWriter
    reader = PdfReader(pdfname)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    for key in list(reader.metadata.keys()):
        writer.add_metadata({key: ''})
    with open(pdfname, "wb") as f:
        writer.write(f)
    print(f"Metadaten erfolgreich aus der PDF '{pdfname}' entfernt.\nRED DESIGN GERMANY \u2764")

def clear_audio_metadata(audioname):
    from mutagen import File
    audio = File(audioname)
    if audio is not None:
        audio.delete()
        audio.save()
        print(f"Metadaten erfolgreich aus der Audiodatei '{audioname}' entfernt.\nRED DESIGN GERMANY \u2764")
    else:
        print(f"Fehler beim Entfernen der Metadaten aus der Audiodatei '{audioname}'.")

def clear_video_metadata(videoname):
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(videoname)
    video.write_videofile(videoname, codec="libx264", audio_codec="aac", remove_temp=True)
    print(f"Metadaten erfolgreich aus der Videodatei '{videoname}' entfernt.\nRED DESIGN GERMANY \u2764")

def clear_metadata(filename):
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
        print(f"Dateityp '{ext}' wird nicht unterstützt.")

# Einrichtung der Befehlszeilenargumente
parser = argparse.ArgumentParser(
    description=(
r"  ____ _                   __  __      _            _       _             " + "\n" +
r" / ___| | ___  __ _ _ __  |  \/  | ___| |_ __ _  __| | __ _| |_ __ _ ___  " + "\n" +
r"| |   | |/ _ \/ _` | '__| | |\/| |/ _ \ __/ _` |/ _` |/ _` | __/ _` / __| " + "\n" +
r"| |___| |  __/ (_| | |    | |  | |  __/ || (_| | (_| | (_| | || (_| \__ \ " + "\n" +
r" \____|_|\___|\__,_|_|    |_|  |_|\___|\__\__,_|\__,_|\__,_|\__\__,_|___/ " + "\n\n" +
        "Made by RED DESIGN GERMANY \u2764 \n\n" 
        "Die Anwendung Clear Metadatas entfernt Metadaten aus verschiedenen Dateitypen wie Bildern, PDFs, Audios und Videos.\n\n"
        "UNTERSTÜTZTE DATEI-FORMATE:\n"
        "  Bilder: .jpg, .jpeg, .png, .gif, .bmp, .tiff\n"
        "  PDFs:   .pdf\n"
        "  Audios: .mp3, .flac, .wav, .m4a, .ogg\n"
        "  Videos: .mp4, .avi, .mkv, .mov"
    ),
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument("datei", help="Die Datei, von der die Metadaten entfernt werden sollen.")
# Argumente parsen
args = parser.parse_args()
# Metadaten der angegebenen Datei entfernen
if args.datei:
    clear_metadata(args.datei)
