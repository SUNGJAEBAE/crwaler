import urllib.request as req
from urllib.error import URLError, HTTPError

path_list = ["C:/Users/hsm01/Desktop/web/crawl/result/test2.jpg",
             "C:/Users/hsm01/Desktop/web/crawl/result/test2.html"]

target_url = [
    'http://blogfiles.naver.net/20150919_90/kimiyong88_1442646576744NAFqt_JPEG/B3%95%8C4.JPG',
    'http://google.com'
]

for i, url in enumerate(target_url):
    try:
        response = req.urlopen(url)
        content = response.read()
        print("------------------------------")
        print(f'header info {i}:{response.info()}')
        print(f"http status code: {response.getcode}")
        print()
        print("_---------------------------------")

        with open(path_list[i], 'wb') as f:
            f.write(content)
            print("ok")
    except HTTPError as e:
        print("download failed")
        print("httperror code:", e.code)
    except URLError as e:
        print("download failed")
        print("url Error", e.reason)
    else:
        print()
        print("download success")
