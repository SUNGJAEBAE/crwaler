import urllib.request
from bs4 import BeautifulSoup

url = "https://www.google.com"

soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

a_tags = soup.find_all('a')
result = []
for i in a_tags:
    result.append(i.get_text())

print(result)
