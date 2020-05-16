# fake agent
import json
import urllib.request as req
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.ie)
print(ua.chrome)

headers = {
    'User-agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

url = 'http://finance.daum.net/api/search/ranks?limit=10'

res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

# str->json
rank_json = json.loads(res)['data']

for ele in rank_json:
    print(f"순위 :{ele['rank']}, 금액:{ele['tradePrice']} 회사명:{ele.get('name')}")
