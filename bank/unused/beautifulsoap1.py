from bs4 import BeautifulSoup
import requests
import re
import os

url="http://python123.io/ws/demo.html"
r=requests.get(url)
demo=r.text
soup= BeautifulSoup(demo,"html.parser")
tag=soup.a
#print(soup.prettify())

for tag in soup.find_all(re.compile('b')):

    print(tag.name)

print(soup.find_all(id=re.compile('link')))