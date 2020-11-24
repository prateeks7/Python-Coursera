import urllib.request, urllib.parse, urllib.error
import re

url = input("Enter - ")
count = input("count - ")
position = input("position - ")
for i in range(int(count)):
    html = urllib.request.urlopen(url)
    alinks = list()
    anames = list()
    for line in html:
        all = line.decode()
        if 'href' in all:
            links = re.findall('href="(.*)"',all)
            alinks.append(links[0])
    url = alinks[int(position)-1]
print(re.findall('by_(.*).html',alinks[int(position)-1])[0])
