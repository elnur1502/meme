import requests
from bs4 import BeautifulSoup


def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    div2 = soup.find('div', id='stream-2')
    try:
        img = div2.find_all('img').get
        for src in img:
            print img.get('src')
    except:
        pass


def main():
    url = 'https://9gag.com/meme'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
