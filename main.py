# pip install moviepy

import moviepy.editor

# read the video file you intend to convert, ensure the video file is in the same directory as this script. 
# You should rename the function argument below to the name of the video file you wish to convert 

video = moviepy.editor.VideoFileClip("video.mp4")


# extract only the audio
audio = video.audio

# save the audio file

audio.write_audiofile('audio.mp4')

#initialize the conversion by running the command "python main.py" on your terminal


