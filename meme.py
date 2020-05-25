import requests
from bs4 import BeautifulSoup



def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml').text
    divs = soup.find('div', class='main-wrap').find_all('a')
    
    for a in divs:
        td = a.find_all('img')
    
        print(td)


def main():
    url = 'https://9gag.com/meme'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
