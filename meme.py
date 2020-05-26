import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
from fake_useragent import UserAgent
UserAgent().chrome
page_link = 'https://9gag.com/meme'

def get_html(site):
  response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
  response
  for key, value in response.request.headers.items():
    print(key+": "+value)

def get_page_data(html):
  soup = BeautifulSoup(html,'html.parser')
  for img in soup.find_all('img'):
    print img.get('src')  

def main():
    page_link = 'https://9gag.com/meme'
    get_page_data(get_html(page_link))


if __name__ == '__main__':
    main()

