from lxml.html import fromstring, tostring
import requests


def main():
    """
    네이버 메인 리스트 스크래핑
    """
    session = requests.Session()

    response = session.get("https://www.naver.com")

    urls = scrape_news_list_page(response)
    for name, url in urls.items():
        print(name, url)


def scrape_news_list_page(response):
    urls = {}
    root = fromstring(response.content)
    for a in root.xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li/a'):
        name, url = extract_contents(a)
        urls[name] = url
    return urls


def extract_contents(dom):
    link = dom.get("href")
    name = dom.text
    return name, link


if __name__ == "__main__":
    main()
