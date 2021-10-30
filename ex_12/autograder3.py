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

count_count = 0
position_count = 0

while True:
  url = input('Enter URL: ')
  if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    break
while True:  
  try:
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    break
  except:
    print("You must enter a integer for both values!")

# Retrieve all of the p tags
while count_count < count + 1:
  #retrieve current url and find all 'a' elements
  req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
  html = urlopen(req).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup.find_all('a')
  count_count += 1
  for tag in tags:
    position_count += 1
    while position_count < position + 1:
      #position_count += 1
      #for tag in tags:
      print(str(tag['href']))
      url = str(tag['href'])
        #position_count += 1

