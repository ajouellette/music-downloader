#!/usr/bin/env python
#
# downTheMusic.py
#

import os
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus as qp
import readline

def download(link):
    """
    Download a video as audio from youtube given a link
    """
    flags = "--extract-audio --audio-format mp3 --audio-quality 0 "
    if "youtube.com" not in link:
        link = "http://youtube.com/" + link
    os.system("youtube-dl " + flags + link)

def main():
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
    title = soup.find("a", "yt-uix-tile-link").text
    print("Found: " + title)
    prompt = input("Download song (Y/n)? ")
    if prompt.lower() == "n":
        return

    # Download the song.
    print ("Downloading...")
    download(video_link)
    print("Done!")
    return

if __name__ == "__main__":
    while True:
        main()

