# requests rest api

# GET POST DELETE PUT(update) REPLACE(FETCH: UPDATE, MODIFIY)

import requests

with requests.Session() as s:
    r = s.get('https://api.github.com/events')
    r.raise_for_status()
    jar = requests.cookies.RequestsCookieJar()
    jar.set('name', 'niceman', domain="httpbin.org", path="/cookies")

    r = s.get('http://httpbin.org/cookies', cookies=jar)
    print(r.text)

    r = s.get('https://github.com', timeout=5)
    r = s.post('http://httpbin.org/post',
               data={"id": "testa", "pw": "11"}, cookies=jar)

    print(r.text)
    print(r.headers)
