from bs4 import BeautifulSoup
from urllib2 import urlopen
html_doc = urlopen('http://1001mem.ru').read()
soup = BeautifulSoup(html_doc)

for img in soup.find_all('img'):
    print img.get('src')


