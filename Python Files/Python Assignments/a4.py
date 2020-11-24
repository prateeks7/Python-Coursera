import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input("Enter - ")
count = input("count - ")
position = input("position - ")
for i in range(int(count)):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    tags = soup('a')
    links = list()
    for tag in tags:
        links.append(tag.get('href',None))
    url = links[int(position)-1]
names = list()
for tag in tags:
    names.append(tag.contents[0])
print(names[int(position)-1])
