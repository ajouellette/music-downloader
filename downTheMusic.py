#!/usr/bin/env python
#
# downTheMusic.py
#

import os
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus as qp

search = input("Enter songname / lyrics / artist ... or whatever\n> ")
if search == "":
    sys.exit()

print("Searching ...")

# Magic happens here.
search = qp(search)
response = urlopen("https://www.youtube.com/results?search_query=" + search)
html = response.read()
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all('a'):
    if "/watch?v=" in link.get("href"):
        # May change when YouTube gets updated in the future.
        video_link = link.get("href")
        break

# Print title and prompt to download
title = title = soup.find("a", "yt-uix-tile-link").text
print("Found: " + title)
prompt = input("Download song (y/n)? ")
if prompt != "y":
    sys.exit()

# Links are relative on page, making them absolute.
video_link = "http://www.youtube.com/" + video_link
command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 " + video_link

# Download the song.
print ("Downloading...")
os.system(command)
print("Done!")
