# OBS-recording-compression
Simple script to automate screen recording via OBS and the following recording compression.

# Script explained
This script has two features, the first is to allow the registration of the desktop (or any other window) via OBS and to automatically compress the registration via ffmpeg to facilitate its storage, the second is to compress (as said via ffmpeg) a video chosen by the user.

# Instructions for use
First of all you have to start OBS (OBS_portable\bin\64bit\obs64.exe) and set from the program settings the same folder where this script is located as destination folder for recordings, also set the desired resolution and fps. After this you have to add "Display Capture" to the sources list, or "Window Capture", specifying in this second case which window you want to record. Finally disable the microphone from the OBS audio mixer, in case you want to record computer audio only. At this point to start recording or to compress a video just use the python file "video_record_compression.py" (in this case you have to install the required modules if you don't already have them), or the corresponding .exe file.

# Documentation
ffmpeg
- https://gist.github.com/lukehedger/277d136f68b028e22bed
- https://askubuntu.com/questions/352920/fastest-way-to-convert-videos-batch-or-single
- https://www.ffmpeg.org/ (I used a Windows build from gyan.dev) 

subprocess
- https://stackabuse.com/executing-shell-commands-with-python/ 

pyinstaller
- https://datatofish.com/executable-pyinstaller/
