# Import the required module for text
# to speech conversion
from gtts import gTTS
import time

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome Mr. Bond, These are your schedule for today. Would like me to bring you a hot coffee?'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("sparta.mp3")

# Playing the converted file
os.system("../Scripts_1/sparta.mp3")

