# https://www.youtube.com/watch?v=K6AJuRK2NE4
# pip install pafy
# Get the latest Version

import pafy
# from pydub import AudioSegment for webm to audio

url = 'https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p'

# video = pafy.new(url)
playlist = pafy.get_playlist(url)

length = len(playlist['items'])

# print(len(playlist['items']))

for x in range(length):
    print(playlist.items())
# print(video.title)

# print(video.viewcount, video.author, video.length)

# For video = getbest()
# For audio = getbestaudio()
# stream = video.getbest(preftype="mp4")
#
# filename = stream.download(quiet=False)
#
# print(filename)
