import argparse
import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter

# Funktionen zur Entfernung von Metadaten
def clear_image_metadata(imgname):
    from PIL import Image
    img = Image.open(imgname)
    data = list(img.getdata())
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    img_without_metadata.save(imgname)
    print(f"Metadata successfully cleared from the image '{imgname}'.\nRED DESIGN GERMANY \u2764")

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
    print(f"Metadata successfully cleared from the PDF '{pdfname}'.\nRED DESIGN GERMANY \u2764")

def clear_audio_metadata(audioname):
    from mutagen import File
    audio = File(audioname)
    if audio is not None:
        audio.delete()
        audio.save()
        print(f"Metadata successfully cleared from the audio file '{audioname}'.\nRED DESIGN GERMANY \u2764")
    else:
        print(f"Failed to clear metadata from the audio file '{audioname}'.")

def clear_video_metadata(videoname):
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(videoname)
    video.write_videofile(videoname, codec="libx264", audio_codec="aac", remove_temp=True)
    print(f"Metadata successfully cleared from the video file '{videoname}'.\nRED DESIGN GERMANY \u2764")

def clear_docx_metadata(docxname):
    import docx
    doc = docx.Document(docxname)
    core_properties = doc.core_properties
    core_properties.author = None
    core_properties.title = None
    core_properties.subject = None
    core_properties.keywords = None
    core_properties.comments = None
    core_properties.last_modified_by = None
    core_properties.revision = None
    doc.save(docxname)
    print(f"Metadata successfully cleared from the DOCX '{docxname}'.\nRED DESIGN GERMANY \u2764")

def clear_xlsx_metadata(xlsxname):
    import openpyxl
    workbook = openpyxl.load_workbook(xlsxname)
    properties = workbook.properties
    properties.creator = None
    properties.title = None
    properties.subject = None
    properties.keywords = None
    properties.comments = None
    properties.lastModifiedBy = None
    properties.revision = None
    workbook.save(xlsxname)
    print(f"Metadata successfully cleared from the XLSX '{xlsxname}'.\nRED DESIGN GERMANY \u2764")

def clear_pptx_metadata(pptxname):
    import pptx
    presentation = pptx.Presentation(pptxname)
    core_properties = presentation.core_properties
    core_properties.author = None
    core_properties.title = None
    core_properties.subject = None
    core_properties.keywords = None
    core_properties.comments = None
    core_properties.last_modified_by = None
    core_properties.revision = None
    presentation.save(pptxname)
    print(f"Metadata successfully cleared from the PPTX '{pptxname}'.\nRED DESIGN GERMANY \u2764")

def clear_metadata(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic']:
        clear_image_metadata(filename)
    elif ext in ['.pdf']:
        clear_pdf_metadata(filename)
    elif ext in ['.mp3', '.flac', '.wav', '.m4a', '.ogg', '.aac']:
        clear_audio_metadata(filename)
    elif ext in ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.mpeg']:
        clear_video_metadata(filename)
    elif ext in ['.docx']:
        clear_docx_metadata(filename)
    elif ext in ['.xlsx']:
        clear_xlsx_metadata(filename)
    elif ext in ['.pptx']:
        clear_pptx_metadata(filename)
    else:
        print(f"File type '{ext}' is not supported.")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            clear_metadata(filepath)

# Einrichtung der Befehlszeilenargumente
parser = argparse.ArgumentParser(
    description=(
r"   ____ _                   __  __      _            _       _        " + "\n" +
r"  / ___| | ___  __ _ _ __  |  \/  | ___| |_ __ _  __| | __ _| |_ __ _ " + "\n" +
r" | |   | |/ _ \/ _` | '__| | |\/| |/ _ \ __/ _` |/ _` |/ _` | __/ _` |" + "\n" +
r" | |___| |  __/ (_| | |    | |  | |  __/ || (_| | (_| | (_| | || (_| |" + "\n" +
r"  \____|_|\___|\__,_|_|    |_|  |_|\___|\__\__,_|\__,_|\__,_|\__\__,_|" + "\n" +
        "               made with \u2764 by RED DESIGN GERMANY \n\n"
        "The Clear Metadata application removes metadata from various file types for a single file such as images, PDFs, audios, videos and Microsoft Office documents or files from an entire folder.\n\n"
        "For instance: \n"
        "If you want to remove metadata from a single file use:"
        "RDG_MetaRemover.py -f test.mp3 "
        "If you want to remove metadata from a single file use:"
        "use RDG_MetaRemover.py -p path/to/folder/ if you want to remove the metadata of the files within a folder."
        "SUPPORTED FILE FORMATS:\n"
        "  Images: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp, .heic\n"
        "  PDFs:   .pdf\n"
        "  Audios: .mp3, .flac, .wav, .m4a, .ogg, .aac\n"
        "  Videos: .mp4, .avi, .mkv, .mov, .wmv, .mpeg\n"
        "  Microsoft Office documents: .docx, .xlsx, .pptx"
    ),
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument("-f", "--file", help="The file from which to remove metadata.") 
parser.add_argument("-p", "--path", help="The directory from which to remove metadata from all files within this directory.")
# Argumente parsen
args = parser.parse_args()

# Metadaten der angegebenen Datei oder des angegebenen Verzeichnisses entfernen
if args.file:
    if os.path.isfile(args.file):
        clear_metadata(args.file)
    else:
        print(f"'{args.file}' is not a valid file.")
elif args.path:
    if os.path.isdir(args.path):
        process_directory(args.path)
    else:
        print(f"'{args.path}' is not a valid directory.")
else:
    print("Please provide either a file or a directory.")
