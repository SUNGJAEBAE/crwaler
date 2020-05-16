import json
import requests

with requests.Session() as s:
    r = s.get('https://httpbin.org/stream/100', stream=True)

    print(r.text)
    print(f'Encoding : {r.encoding}')
    if r.encoding is None:
        r.encoding = 'UTF-8'
    for line in r.iter_lines(decode_unicode=True):
        # print(line)
        # print(type(line))
        b = json.loads(line)  # str->dict
        for k, v in b.items():
            print(f'key:{k}, value:{v}')
        print()
