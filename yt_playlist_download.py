import re
import pytube
from pytube import YouTube

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = 'E:\\YouTube_Downloads'

playlist = pytube.Playlist('https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p')

print('Number of videos in playlist: %s' % len(playlist.video_urls))
counter = 1
for video_url in playlist.video_urls:
    # Custom added so the files present already is skipped
    if not counter < 17:
        YouTube(video_url).streams.get_highest_resolution().download(output_path=DOWNLOAD_DIR)
        print('Videos Downloaded : ', counter)
    counter += 1
# # this fixes the empty playlist.videos list
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
#
# print(len(playlist.video_urls))
#
# for url in playlist.video_urls:
#     print(url)
#
# # physically downloading the audio track
# for video in playlist.videos:
#     print(video)
#     # audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
#     # audioStream.download(output_path=DOWNLOAD_DIR)