#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import run
import requests
from bs4 import BeautifulSoup

URL = input("Enter URL:")
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"}
DOWNLOAD_PATH = "downloads/"

response = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(response.content, 'lxml')

anchors = soup.find_all('a')

for a in anchors:
    href = a.get("href")
    if any(s in href for s in ["youtube", "youtu"]):
        command = ["you-get", href, "-o", DOWNLOAD_PATH ]
        print("Run:", ' '.join(command))
        run(command)

