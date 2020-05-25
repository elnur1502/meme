import requests
from bs4 import BeautifulSoup



def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser').text
    line = soup.find_all('picture').text
    print line.get('img').text


def main():
    url = 'https://9gag.com/meme'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
