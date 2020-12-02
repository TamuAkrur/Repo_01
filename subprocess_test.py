import subprocess
import os
# Needs to have ffmpeg in path

parent_dir = r"E:\YTDownloads"
default_filename = 'Lamb of God - On The Hook (Official Lyric Video).webm'
new_filename = 'Lamb of God - On The Hook (Official Lyric Video).mp3'
source = os.path.join(parent_dir, default_filename)
destination = os.path.join(parent_dir, new_filename)
print(source, destination)
output = subprocess.run([
    # or subprocess.run (Python 3.5+)
    'ffmpeg', '-i', source, destination], capture_output=True, shell=True)

print(output)
