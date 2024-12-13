import argparse
import os
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
import hashlib

# Begrüßung
def greet():
    print("\nWelcome to Clear Metadata Script!")
    print(r"   ____ _                   __  __      _            _       _        " + "\n" +
          r"  / ___| | ___  __ _ _ __  |  \/  | ___| |_ __ _  __| | __ _| |_ __ _ " + "\n" +
          r" | |   | |/ _ \/ _` | '__| | |\/| |/ _ \ __/ _` |/ _` |/ _` | __/ _` |" + "\n" +
          r" | |___| |  __/ (_| | |    | |  | |  __/ || (_| | (_| | (_| | || (_| |" + "\n" +
          r"  \____|_|\___|\__,_|_|    |_|  |_|\___|\__\__,_|\__,_|\__,_|\__\__,_|" + "\n" +
           "   made with ♥ by RED DESIGN GERMANY \n")



def show_image_metadata(imgname):
    img = Image.open(imgname)
    if img.info:
        print(f"\nMetadata for image '{imgname}':")
        for key, value in img.info.items():
            print(f"{key}: {value}")
    else:
        print(f"\nNo metadata found for image '{imgname}'.")

def clear_image_metadata(imgname):
    img = Image.open(imgname)
    data = list(img.getdata())
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    img_without_metadata.save(imgname)
    print(f"Metadata successfully cleared from the image '{imgname}'.")

def show_pdf_metadata(pdfname):
    reader = PdfReader(pdfname)
    if reader.metadata:
        print(f"\nMetadata for PDF '{pdfname}':")
        for key, value in reader.metadata.items():
            print(f"{key}: {value}")
    else:
        print(f"\nNo metadata found for PDF '{pdfname}'.")

def clear_pdf_metadata(pdfname):
    reader = PdfReader(pdfname)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    for key in list(reader.metadata.keys()):
        writer.add_metadata({key: ''})
    with open(pdfname, "wb") as f:
        writer.write(f)
    print(f"Metadata successfully cleared from the PDF '{pdfname}'.")

def show_audio_metadata(audioname):
    from mutagen import File
    audio = File(audioname)
    if audio is not None and audio.keys():
        print(f"\nMetadata for audio '{audioname}':")
        for key in audio.keys():
            print(f"{key}: {audio[key]}")
    else:
        print(f"\nNo metadata found for audio '{audioname}'.")

def clear_audio_metadata(audioname):
    from mutagen import File
    audio = File(audioname)
    if audio is not None:
        audio.delete()
        audio.save()
        print(f"Metadata successfully cleared from the audio file '{audioname}'.")
    else:
        print(f"Failed to clear metadata from the audio file '{audioname}'.")

def show_video_metadata(videoname):
    from mutagen import File
    video = File(videoname)
    if video is not None and video.keys():
        print(f"\nMetadata for video '{videoname}':")
        for key in video.keys():
            print(f"{key}: {video[key]}")
    else:
        print(f"\nNo metadata found for video '{videoname}'.")

def clear_video_metadata(videoname):
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(videoname)
    video.write_videofile(videoname, codec="libx264", audio_codec="aac", remove_temp=True)
    print(f"Metadata successfully cleared from the video file '{videoname}'.")

def show_docx_metadata(docxname):
    import docx
    doc = docx.Document(docxname)
    core_properties = doc.core_properties
    metadata = {
        'author': core_properties.author,
        'title': core_properties.title,
        'subject': core_properties.subject,
        'keywords': core_properties.keywords,
        'comments': core_properties.comments,
        'last_modified_by': core_properties.last_modified_by,
        'revision': core_properties.revision
    }
    if any(metadata.values()):
        print(f"\nMetadata for DOCX '{docxname}':")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print(f"\nNo metadata found for DOCX '{docxname}'.")

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
    print(f"Metadata successfully cleared from the DOCX '{docxname}'.")

def show_xlsx_metadata(xlsxname):
    import openpyxl
    workbook = openpyxl.load_workbook(xlsxname)
    properties = workbook.properties
    metadata = {
        'creator': properties.creator,
        'title': properties.title,
        'subject': properties.subject,
        'keywords': properties.keywords,
        'comments': properties.comments,
        'last_modified_by': properties.lastModifiedBy,
        'revision': properties.revision
    }
    if any(metadata.values()):
        print(f"\nMetadata for XLSX '{xlsxname}':")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print(f"\nNo metadata found for XLSX '{xlsxname}'.")

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
    print(f"Metadata successfully cleared from the XLSX '{xlsxname}'.")

def show_pptx_metadata(pptxname):
    import pptx
    presentation = pptx.Presentation(pptxname)
    core_properties = presentation.core_properties
    metadata = {
        'author': core_properties.author,
        'title': core_properties.title,
        'subject': core_properties.subject,
        'keywords': core_properties.keywords,
        'comments': core_properties.comments,
        'last_modified_by': core_properties.last_modified_by,
        'revision': core_properties.revision
    }
    if any(metadata.values()):
        print(f"\nMetadata for PPTX '{pptxname}':")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print(f"\nNo metadata found for PPTX '{pptxname}'.")

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
    print(f"Metadata successfully cleared from the PPTX '{pptxname}'.")

def show_metadata(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic']:
        show_image_metadata(filename)
    elif ext in ['.pdf']:
        show_pdf_metadata(filename)
    elif ext in ['.mp3', '.flac', '.wav', '.m4a', '.ogg', '.aac']:
        show_audio_metadata(filename)
    elif ext in ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.mpeg']:
        show_video_metadata(filename)
    elif ext in ['.docx']:
        show_docx_metadata(filename)
    elif ext in ['.xlsx']:
        show_xlsx_metadata(filename)
    elif ext in ['.pptx']:
        show_pptx_metadata(filename)
    else:
        print(f"File type '{ext}' is not supported.")

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

def hash_file(filepath):
    """Berechne den Hash einer Datei."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def process_directory(directory):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            
            # Berechne den Hash der Datei, um Duplikate zu erkennen
            filehash = hash_file(filepath)
            if filehash in hashes:
                print(f"Duplicate found: {filepath}. Deleting duplicate file.")
                os.remove(filepath)
            else:
                hashes[filehash] = filepath

            # Zeige die Metadaten an
            show_metadata(filepath)
            # Frage den Benutzer, ob die Metadaten gelöscht werden sollen
            user_input = input(f"Do you want to clear metadata for {filepath}? (yes/no): ").strip().lower()
            if user_input == 'yes':
                clear_metadata(filepath)
            else:
                print(f"Skipping metadata clearing for {filepath}.")

if __name__ == "__main__":
    greet()  # Begrüßung aufrufen

    # Einrichtung der Befehlszeilenargumente
    parser = argparse.ArgumentParser(
        description=(
    r"   ____ _                   __  __      _            _       _        " + "\n" +
    r"  / ___| | ___  __ _ _ __  |  \/  | ___| |_ __ _  __| | __ _| |_ __ _ " + "\n" +
    r" | |   | |/ _ \/ _` | '__| | |\/| |/ _ \ __/ _` |/ _` |/ _` | __/ _` |" + "\n" +
    r" | |___| |  __/ (_| | |    | |  | |  __/ || (_| | (_| | (_| | || (_| |" + "\n" +
    r"  \____|_|\___|\__,_|_|    |_|  |_|\___|\__\__,_|\__,_|\__,_|\__\__,_|" + "\n" +
     "   made with ♥ by  RED DESIGN GERMANY \n\n"
        "The Clear Metadata application removes metadata from various file types for a single file such as images, PDFs, audios, videos and Microsoft Office documents or from all files in a specific folder.\n\n"
        "For instance: \n"
        "If you want to remove metadata from a single file:\n"
        "RDG_MetaRemover.py -f test.mp3 \n\n"
        "If you want to remove metadata from all files in a specific folder:\n"
        "RDG_MetaRemover.py -p path/to/folder/ \n\n"
        "**SUPPORTED FILE FORMATS:**\n"
        "  Images: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp, .heic\n"
        "  PDFs:   .pdf\n"
        "  Audios: .mp3, .flac, .wav, .m4a, .ogg, .aac\n"
        "  Videos: .mp4, .avi, .mkv, .mov, .wmv, .mpeg\n"
        "  MSdocs: .docx, .xlsx, .pptx"
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
            show_metadata(args.file)
            user_input = input(f"Do you want to clear metadata for {args.file}? (yes/no): ").strip().lower()
            if user_input == 'yes':
                clear_metadata(args.file)
            else:
                print(f"Skipping metadata clearing for {args.file}.")
        else:
            print(f"'{args.file}' is not a valid file.")
    elif args.path:
        if os.path.isdir(args.path):
            process_directory(args.path)
        else:
            print(f"'{args.path}' is not a valid directory.")
    else:
        print("Please provide either a file or a directory.")
