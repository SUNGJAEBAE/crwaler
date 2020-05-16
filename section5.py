import urllib.request
from urllib.parse import urlparse
import requests
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)
print(f'type : {type(mem)}')
print(f'geturl : {mem.geturl()}')
print(f'status : {mem.status}')
print(f'headers : {mem.getheaders()}')
print(f'getcode : {mem.getcode()}')
print(f'read : {mem.read(400).decode("EUC-KR")}')
#print(f'parse : {urlparse("http://www.encar.co.kr?test=test").query()}')

API = "https://api.ipify.org"
values = {
    'format': 'json'
}
print(f'before param :{values}')
params = urllib.parse.urlencode(values)
print(f'after param : {params}')

URL = API+"?"+params
print(URL)

data = urllib.request.urlopen(URL).read()
text = data.decode('UTF-8')
print(f'response = {text}')
