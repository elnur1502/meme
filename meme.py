import json
import requests
from bs4 import BeautifulSoup

url = 'https://9gag.com/meme'

r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
s = BeautifulSoup(r.text, "lxml")
img = s.find_all('img')
img = json.load(img)
for k,v in img.items():
    if 'px' in k:
        print(k)
