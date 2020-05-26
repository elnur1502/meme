import json
import requests
from bs4 import BeautifulSoup

url = 'https://9gag.com/gag/apGv05B'

r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
s = BeautifulSoup(r.text, "lxml")
img = s.find('img')
print(img)

