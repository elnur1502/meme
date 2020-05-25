import requests
from bs4 import BeautifulSoup



def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    images = soup.find_all('img')
    print(images/n)


def main():
    url = 'http://1001mem.ru'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
