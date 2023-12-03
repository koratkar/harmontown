# take transcripts in transcript directory, format them as html, and add them to the html file
import datetime
import os

def stamp_to_seconds(stamp):
  return str((datetime.datetime.strptime(stamp, "%H:%M:%S") - datetime.datetime(1900,1,1)).total_seconds())

for file in os.listdir("transcripts"):
  filename = file.split(".")[0]
  input_file = "transcripts/" + file 
  output_file = "website/" + filename + ".html"
  
  with open(input_file, 'r') as f_in, open(output_file, 'a+') as f_out:

    for line in f_in.read().splitlines():
      
      time_stamp = line.split(" ")[0][1:] 
      stamp = time_stamp.split(".")[0]
      if 2 > time_stamp.count(":"):
        seconds = stamp_to_seconds("00:" + stamp)
      else: 
        seconds = stamp_to_seconds(stamp)
        
      text = line.split("] ")[1]
      f_out.seek(0)
      url = f_out.read().split("--")[1]
      template_html = '<div class="c"><a class="l" href="#time_stamp" id="time_stamp">link</a> | <div class="s"><a href="url#t=seconds">time_stamp</a></div>\n<div class="t">text</div></div>'
      html = template_html.replace("time_stamp", time_stamp).replace("seconds", seconds).replace("url", url).replace("text", text)
      f_out.write(html)

  print(file + " complete")
