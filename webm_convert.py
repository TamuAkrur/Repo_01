import subprocess

from pydub import AudioSegment
import ffmpeg

AudioSegment.from_file(r"E:\Test_Folder\Metallica.webm", format="webm").export(r"E:\Test_Folder\file", format="mp3")
