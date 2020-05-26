import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
from fake_useragent import UserAgent
UserAgent().chrome
page_link = 'https://9gag.com/meme'
response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
response



