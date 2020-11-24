import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

url = input("Enter - ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tag = soup('span')
sum=0
for tags in tag:
    sum=sum+int(tags.contents[0])
print(sum)
