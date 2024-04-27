# Harmontown Transcripts
[Transcripts](https://koratkar.github.io/harmontown/website/) for every available Harmontown episode, transcribed using OpenAI Whisper.

todo:
- [ ] replace rss\_parser library
- [ ] download episodes 
- [ ] create a version of this that can run on any rss feed 
  - [ ] deal with weird urls used for marketing (how?, maybe keep only string after the last "https://")
- [ ] script that can transcribe any episode 
  - semantic search
  - [ ] shell script (or something?) that runs script that can transcribe any episode such that you can stop it and start it whenever 
  - [ ] make this the main file to run, that does everything in "lexicap for any podcast" version
    - [ ] requirements.txt
    - [ ] create a logfile for which podcasts have been done, which podcasts are in progress, etc
      - [ ] basic search (is semantic search feasible on device?)
    - for lexicap-any (come up with a better name):
      - basic checks of whether directories involved exist for clientside 
      - check if the podcast mp3 actually downloads 
      - how do you actually build stuff like this that you just plug and play run kind of deal?
    - Add description and if there are shownotes, create something to find closest link div to that shownote. 

- [ ] standardize use of " vs ' in the files

