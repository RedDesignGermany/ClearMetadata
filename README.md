# **Clear Metadata**
made with :white_heart: by RED DESIGN GERMANY

## What does it do?
Clear Metadata, as the name suggests, deletes all “superfluous” metadata from images, videos, PDFs, audios and even docx, xlxs, pptx docs. It's also possible to remove the metadata from the files in a folder. \nInstead of the -f or --file argument, -p or --path path/to/folder/ must be entered

## Supported files:
- .pdf
- jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp, .heic
- .mp4, .avi, .mkv, .mov, .wmv, .mpeg
- .mp3, .flac, .wav, .m4a, .ogg, .aac
- .docx, .xlsx, .pptx

## Example call:
To run the script and remove the metadata of an image, PDF, audio or video, you can use the following command:
```
**for images:**
zsh
python RDG_MetaRemover.py -f your_image.jpg
```
```
**for PDFs:**
zsh
python RDG_MetaRemover.py -f your_PFD.pdf
```
```
**for audio:**
zsh
python RDG_MetaRemover.py --file your_mp3.mp3
```
```
**for video:**
zsh
python RDG_MetaRemover.py --file your_video.avi
```
```
**for files within a folder:**
zsh
python RDG_MetaRemover.py --path path/to/your/folder/
```

## Install dependencies:
Make sure that you install the required libraries/modules:
Required python modules: 
- pillow
- PyPDF
- mutagen
- moviepy
- python-docx
- openpyxl
- python-pptx

You can use a single commant to install all of them
```
pip install pillow PyPDF2 mutagen moviepy moviepy python-docx openpyxl python-pptx
```
or you can install them individually
  
```
pip install pillow PyPDF2 mutagen moviepy
```
```
pip install pillow
```
```
pip install PyPDF2
```
```
pip install mutagen
```
```
pip install moviepy
```
```
pip install python-docx
```
```
pip install openpyxl
```
```
pip install python-pptx
```
