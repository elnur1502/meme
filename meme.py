import requests
from bs4 import BeautifulSoup
import os


def download_image(url, fileName):          #save image function
    path = os.path.join("imgs", fileName)
    f = open(path, 'wb')
    f.write(requests.get(url).content)
    f.close()


def fetch_url(url):                        # fetching url
    page = requests.get(url)
    return page

def parse_html(htmlPage):                  #parsing the url
    soup = BeautifulSoup(htmlPage, "html.parser")
    return soup


def retrieve_jpg_urls(soup):

    list_of_urls = soup.find_all('list')       #classes wanted
    parsed_urls = []
    for index in range(len(list_of_urls)):
        try:
            parsed_urls.append(soup.find_all('img')[index].attrs['src']) #img wanted inside class
        except:
            next
    return parsed_urls


def main():
    htmlPage = fetch_url("https://9gag.com/")
    soup = parse_html(htmlPage.content)
    jpgUrls = retrieve_jpg_urls(soup)
    for index in range(len(jpgUrls)):
        try:
            download_image(jpgUrls[index], "savedpic{}.jpg".format(index))
        except:
            print("failed to parse image with url {}".format(jpgUrls[index]))
    print("")

if __name__ == "__main__":
    main()
