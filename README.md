# **Clear Metadata**

## What does it do?
Clear Metadata, as the name suggests, deletes all “superfluous” metadata from images, videos, PDFs, audios and even docx, xlxs, pptx docs. It's also possible to remove metadata from
 files in a folder. 

## Supported files:
- .pdf
- .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp, .heic
- .mp4, .avi, .mkv, .mov, .wmv, .mpeg
- .mp3, .flac, .wav, .m4a, .ogg, .aac
- .docx, .xlsx, .pptx

## Example call:
To run this script and remove metadata from an image, PDF, audio or video, you can use the following command for

images:
```
python RDG_MetaRemover.py -f your_image.jpg
```
PDFs:
```
python RDG_MetaRemover.py -f your_PFD.pdf
```
audios:
```
python RDG_MetaRemover.py --file your_mp3.mp3
```
videos:
```
python RDG_MetaRemover.py --file your_video.avi
```
or you can remove metadata from ALL files in a folder:
```
python RDG_MetaRemover.py --path path/to/your/folder/
```

## Install dependencies:

Make sure that you install a "working" python version and required modules.

"Working" Python Verison: 
Python 3.13.1

Required python modules: 
- pillow
- PyPDF
- mutagen
- moviepy
- python-docx
- openpyxl
- python-pptx

You can install them all with one command
```
pip install pillow PyPDF2 mutagen moviepy moviepy python-docx openpyxl python-pptx
```
or you can install them individually
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

Made with :white_heart:
[**RED DESIGN GERMANY**](https://www.red-design-germany.net)
