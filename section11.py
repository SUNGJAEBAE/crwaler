from bs4 import BeautifulSoup
import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
opener = req.build_opener()
opener.addheaders = [('User-agent', UserAgent().chrome)]
req.install_opener(opener)

base = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="
quote = req.quote('카구야')
url = base+quote

print('Request URL : {}'.format(url))
res = req.urlopen(url)
savePath = "C:/Users/hsm01/Desktop/web/crawl/result2"
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    print("folder creation failed")
    print(f"folder name : {e.filename}")
    raise RuntimeError("system exit!")
else:
    print("folder created")

soup = BeautifulSoup(res, "html.parser")
# print(soup.prettify())

img_list = soup.select(
    'div.img_area> a.thumb._thumb > img')

for i, img in enumerate(img_list, 1):
    #print(img['data-source'], i)
    fullFileName = os.path.join(savePath, str(i)+'.png')
    print(fullFileName)
    req.urlretrieve(img['data-source'], fullFileName)

# 더 많이 하려면 selenium을 배워서 한다
