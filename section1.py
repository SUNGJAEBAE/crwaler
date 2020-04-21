#urllib 쓰기

import urllib.request as req

#파일 url
img_url='''http://blogfiles.naver.net/20150919_90/kimiyong88_1442646576744NAFqt_JPEG/B3%95%8C4.JPG'''
html_url='http://google.com'

#다운받을 경로
save_path1='''C:/Users/hsm01/Desktop/web/crawl/result/test1.jpg'''
save_path2='''C:/Users/hsm01/Desktop/web/crawl/result/index.html'''

try:
    file1, header1=req.urlretrieve(img_url,save_path1)
    file2, header2=req.urlretrieve(html_url,save_path2)
except Exception as e:
    print('failed')
    print(e)

else:
    print(header1)
    print(header2)
    print(file1)