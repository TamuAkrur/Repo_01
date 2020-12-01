# Python Program to check inbox of Gmail
# Will download any Excel attachments from new mail received
# Made for: https://stackoverflow.com/questions/61366836/download-attachment-from-mail-using-python/

import os
from imbox import Imbox  # pip install imbox
from pathlib import Path
import traceback


# enable less secure apps on your google account
# https://myaccount.google.com/lesssecureapps
def check_mail():
    host = "imap.gmail.com"
    username = "YOUR.G_MAIL@gmail.com"
    password = 'YOURMAILPASSWORD'

    # in Ubuntu 20.04, the program will create the folder, from where it has been executed.
    download_folder = Path(r"E:\Test_Folder\attachment_files")

    # Create folder if not in the system

    if not os.path.isdir(download_folder):
        os.makedirs(download_folder, exist_ok=True)
    # Email Connection settings
    mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)

    # defaults to inbox
    # only messages which are unread
    messages = mail.messages(unread=True)

    for (uid, message) in messages:
        # marks message as read
        mail.mark_seen(uid)
        # TODO: Check file mime type, if XLS, XLSX then download.
        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                # Checking by file name, can add multiple conditions
                # TODO: Add Timestamp on the file name
                if att_fn.endswith('.xls'):
                    download_path = f"{download_folder}/{att_fn}"
                    print("File :" + att_fn + " was downloaded.")
                    # "wb" = File mode, write and binary
                    with open(download_path, "wb") as fp:
                        fp.write(attachment.get('content').read())
                else:
                    print("File :" + att_fn + " was not downloaded.")


            except:
                pass
                print(traceback.print_exc())

    mail.logout()


"""
Available Message filters: 

# Gets all messages from the inbox
messages = mail.messages()

# Unread messages
messages = mail.messages(unread=True)

# Flagged messages
messages = mail.messages(flagged=True)

# Un-flagged messages
messages = mail.messages(unflagged=True)

# Flagged messages
messages = mail.messages(flagged=True)

# Un-flagged messages
messages = mail.messages(unflagged=True)

# Messages sent FROM
messages = mail.messages(sent_from='sender@example.org')

# Messages sent TO
messages = mail.messages(sent_to='receiver@example.org')

# Messages received before specific date
messages = mail.messages(date__lt=datetime.date(2018, 7, 31))

# Messages received after specific date
messages = mail.messages(date__gt=datetime.date(2018, 7, 30))

# Messages received on a specific date
messages = mail.messages(date__on=datetime.date(2018, 7, 30))

# Messages whose subjects contain a string
messages = mail.messages(subject='Christmas')

# Messages from a specific folder
messages = mail.messages(folder='Social')
"""

"""
File mode, write and binary. Since you are writing a .jpg file, it looks fine.

But if you supposed to read that jpg file you need to use 'rb'

More info: 

On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'. 
Python on Windows makes a distinction between text and binary files; the end-of-line characters in text files are 
automatically altered slightly when data is read or written. 
This behind-the-scenes modification to file data is fine for ASCII text files, 
but it’ll corrupt binary data like that in JPEG or EXE files.
"""
