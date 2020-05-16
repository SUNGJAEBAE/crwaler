import lxml.html
import requests


def main():
    """
    네이버 메인 리스트 스크래핑
    """
    response = requests.get("https://www.naver.com")

    urls = scrape_news_list_page(response)
    for url in urls:
        print(url)


def scrape_news_list_page(response):
    urls = []
    root = lxml.html.fromstring(response.content)
    for a in root.cssselect('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li > a'):
        url = a.get('href')
        urls.append(url)

    return urls


if __name__ == "__main__":
    main()
