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
    print(f"Metadata successfully cleared from image '{imgname}'.\nRED DESIGN GERMANY \u2764")

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
    print(f"Metadata successfully cleared from PDF '{pdfname}'.\nRED DESIGN GERMANY \u2764")

def clear_audio_metadata(audioname):
    from mutagen import File
    audio = File(audioname)
    if audio is not None:
        audio.delete()
        audio.save()
        print(f"Metadata successfully cleared from audio '{audioname}'\nRED DESIGN GERMANY \u2764")
    else:
        print(f"Failed to clear metadata from audio '{audioname}'.\nRED DESIGN GERMANY \u2764")

def clear_video_metadata(videoname):
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(videoname)
    video.write_videofile(videoname, codec="libx264", audio_codec="aac", remove_temp=True)
    print(f"Metadata successfully cleared from video '{videoname}'.\nRED DESIGN GERMANY \u2764")

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
        print(f"File type '{ext}' not supported for metadata removal.\nRED DESIGN GERMANY \u2764")
    
# Einrichtung der Befehlszeilenargumente
parser = argparse.ArgumentParser(description="Remove metadata from a file.n/Supported files: .pdf, .mp3, .wav, .avi, .mkv, .flac, .mp4, .ogg, .jpg, .jpeg, .png, .bmp, .tiff \nRED DESIGN GERMANY \u2764")
parser.add_argument("file", help="File from which to remove metadata")
# Argumente parsen
args = parser.parse_args()
# Metadaten der angegebenen Datei entfernen
if args.file:
    clear_metadata(args.file)
