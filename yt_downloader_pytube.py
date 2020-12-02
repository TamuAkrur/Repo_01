import os
import subprocess

import pytube
# Some changes in the code as well.
# Requires pytube3 as well

yt = pytube.YouTube("https://youtu.be/OTmQOjsl0eg")

vids = yt.streams.filter(only_audio=True)

# Available Quality
for i in range(len(vids)):
    print(i, '. ', vids[i])

# Which Quality do you wish to download
# vnum = int(input('Enter the value'))
# for now just set to 1
vnum = 1

parent_dir = r"E:\YTDownloads"
vids[vnum].download(parent_dir)
# change name here

default_filename = vids[vnum].default_filename
# get default name using pytube API

# Strip extension and add new extension
new_filename = os.path.splitext(default_filename)[0]+'.mp3'


# If a filename or its folder has spaces or other special characters, you need to enclose it in quotes
source = os.path.join(parent_dir, default_filename)
destination = os.path.join(parent_dir, new_filename)
output = subprocess.run([
    # or subprocess.run (Python 3.5+)
    'ffmpeg', '-i', source, destination], capture_output=True, shell=True)

print(output)
