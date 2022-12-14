from pytube import YouTube
import os
from moviepy.editor import *

url = "https://www.youtube.com/watch?v=xcJtL7QggTI"
yt = YouTube(url)

streams = yt.streams
print(streams)

# Download video part
video = yt.streams.get_by_itag(248)
video_file  = video.download()
os.rename(video_file, "video.mp4")

# Download audio part
audio = yt.streams.get_by_itag(140)
audio_file = audio.download()
os.rename(audio_file, "audio.mp3")

# Merge audio and video in one file
output_file = "export.mp4"

output_clip = VideoFileClip("video.mp4")
output_clip = output_clip.without_audio() # Remove audio tracks from this video (if any)

audio_track = AudioFileClip("audio.mp3")
output_clip = output_clip.set_audio(audio_track)
output_clip.write_videofile(output_file)