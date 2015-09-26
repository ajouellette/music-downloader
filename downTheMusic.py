#!/usr/bin/env python

import os
import sys
import glob
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus as qp

search = input("Enter songname / lyrics / artist ... or whatever\n> ")
if search == "":
    sys.exit()

search = qp(search)

print("Searching ...")

# Magic happens here.
response = urlopen('https://www.youtube.com/results?search_query=' + search)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    if '/watch?v=' in link.get('href'):
    	print(link.get('href'))
    	# May change when Youtube gets updated in the future.
    	video_link = link.get('href')
    	break

# Links are relative on page, making them absolute.
video_link = 'http://www.youtube.com/' + video_link
command = 'youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 ' + video_link

# Youtube-dl is a proof that god exists.
print ('Downloading...')
os.system(command)
print("Done!")
