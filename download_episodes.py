from rss_parser import Parser
from requests import get
import re

rss_url = "https://feeds.megaphone.fm/harmontown"
response = get(rss_url)

rss = Parser.parse(response.text)

for item in rss.channel.items:
  file_link = "https://" + item.enclosure.attributes["url"][30:]
  original_title = item.title.content
  link_title = re.sub(r"\s+", '_', (re.sub(r"[^\w\s]", '', original_title)))
  audio = get(file_link)
  with open("episodes/" + link_title + ".mp3", "wb") as f:
    f.write(audio.content)

  print("downloading: " + link_title + ".mp3")

