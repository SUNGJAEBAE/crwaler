# requests 사용 스크래핑
import requests

s = requests.Session()

r = s.get('https://httpbin.org/cookies', cookies={'name': 'kim'})
print(r.text)

r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'kim2'})
print(r2.text)

url = 'https://httpbin.org'

headers = {'user-agent': 'nice-man_1.0.0_win10_ram16_home_chrome'}
r3 = s.get(url, headers=headers, cookies={'name': 'bae'})
print(r3.text)

s.close()

with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.ok)
