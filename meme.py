import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/crocs-Unisex-Classic-Black-Women/dp/B0014C0LSY/ref=sr_1_2?_encoding=UTF8&qid=1560091629&s=fashion-womens-intl-ship&sr=1-2&th=1&psc=1'

r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
s = BeautifulSoup(r.text, "lxml")
img = s.find(id="landingImage")['data-a-dynamic-image']
img = json.loads(img)
for k,v in img.items():
    if '395' in k:
        print(k)
