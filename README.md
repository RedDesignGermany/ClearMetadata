# **ClearMetadata**
Clear all hidden Metadatas with Pyhton

## Was macht das Script?
ClearMetadatas, wie der Name es schon anmuten lässt, löscht alle "überflüssigen" Metadatas aus Bildern, Videos, PDFs und Audios in der Version 1.0..

## Beispielaufruf:
Um das Skript auszuführen und die Metadaten eines Bildes, PDFs, Audios oder Videos zu entfernen, kannst du den folgenden Befehl im Terminal verwenden:
...
**Für Bilder:**
zsh
python RDG_MetaRemover.py your_image.jpg

**Für PDFs:**
zsh
python RDG_MetaRemover.py your_PFD.pdf

**Für Audios:**
zsh
python RDG_MetaRemover.py your_mp3.mp3

**Für Videos:**
zsh
python RDG_MetaRemover.py your_video.avi
...

## Abhängigkeiten installieren:
Stelle sicher, dass du die erforderlichen Bibliotheken installierst:
...
zsh
pip install pillow PyPDF2 mutagen moviepy
...
