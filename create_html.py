from rss_parser import Parser
from requests import get
import re

rss_url = "https://feeds.megaphone.fm/harmontown"
response = get(rss_url)

rss = Parser.parse(response.text)

def make_html(ep_list):
  original_html = '<!doctypehtml><html lang=en><meta charset=UTF-8><meta content="width=device-width,initial-scale=1"name=viewport><meta content="ie=edge"http-equiv=X-UA-Compatible><title>Harmontown Transcripts</title><style>body{font-family:sans-serif;font-size:18px;color:#111;padding:0 0 1em 0}.l{color:#050}.s{display:inline-block}.e{display:inline-block}.t{display:inline-block}</style><h1>Harmontown Transcripts</h1><div>These are transcripts for every Harmontown episode, transcribed using OpenAI Whisper. Code available at <a href=https://github.com/koratkar/harmontwon>koratkar/harmontown</a>. Inspired by <a href=https://https://karpathy.ai/lexicap/index.html>Lexicap</a>.</div><div><h2>Episodes:</h2></div><div><ol reversed>ep_list</ol></div></body></html>'
  
  return original_html.replace("ep_list", ep_list)

def make_episode_html(title, link):
  original_html = '<!doctypehtml><html lang=en><meta charset=UTF-8><meta content="width=device-width,initial-scale=1"name=viewport><meta content="ie=edge"http-equiv=X-UA-Compatible><title>Harmontown Transcripts</title><!--ep_link--><style>body{font-family:sans-serif;font-size:18px;color:#111;padding:0 0 1em 0}.l{color:#050}.s{display:inline-block}.e{display:inline-block}.t{display:inline-block}</style><a href=index.html>back to index</a><h2><a href=ep_link>ep_title</a></h2>'
  return original_html.replace("ep_title", title).replace("ep_link", link) 

ep_list = ''
for item in rss.channel.items:
  file_link = "https://" + item.enclosure.attributes["url"][30:]
  original_title = item.title.content
  link_title = re.sub(r"\s+", '_', (re.sub(r"[^\w\s]", '', original_title)))
  print('making file: ' + link_title)
  ep_list += '<li><a href="' + link_title + '.html">' + original_title + '</a></li>'
  with open("website/" + link_title + ".html", "w") as f:
    ep_html = make_episode_html(original_title, file_link)
    f.write(ep_html)

html = make_html(ep_list)
with open("website/index.html", "a") as f:
  f.write(html)
