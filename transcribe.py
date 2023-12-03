# use whisper tiny.en to transcribe each file as webvtt and under the same name as the MP3 in the transcripts directory
import os

for file in os.listdir("episodes"):
  ep_name = file.split('.')[0]
  os.system("whisper --model tiny.en --output_dir vtt_transcripts/ --output_format vtt -- episodes/" + file + " > transcripts/" + ep_name + ".txt")
  print("completed transcription of: " + file)

# html portion
# - take file, and turn into html file for each
# - link to index in each file
# - format each line as nice html
# - create div link for each line as it is now nice html 
