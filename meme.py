import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
from fake_useragent import UserAgent
UserAgent().chrome
page_link = 'https://9gag.com/meme'
response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
response
for key, value in response.request.headers.items():
  print(key+": "+value)

html_doc = urlopen('https://9gag.com/meme').read()
soup = BeautifulSoup(html_doc)

for img in soup.find_all('img'):
    print img.get('src')  



