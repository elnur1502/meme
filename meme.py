from bs4 import BeautifulSoup
from urllib2 import urlopen
from fake_useragent import UserAgent
UserAgent().chrome
response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
response



