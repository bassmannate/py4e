# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.parse, urllib.error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
total = 0

url = input('Enter - ')
req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the p tags
tags = soup('span')
for span_tag in tags:
  count += 1
  total += int(span_tag.text)

print("Count: ",count, "Sum:", total)